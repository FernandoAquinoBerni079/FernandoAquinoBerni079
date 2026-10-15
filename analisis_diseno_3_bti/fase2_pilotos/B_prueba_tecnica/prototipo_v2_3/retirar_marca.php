<?php
// Retiro seguro de una marca de mantenimiento huérfana (por ejemplo, después de un corte de energía).
// Uso:
//   php retirar_marca.php             diagnóstico: comprueba todo y no cambia nada
//   php retirar_marca.php --retirar   retira la marca solo si todas las comprobaciones salen bien
// Códigos de salida: 0 = sin marca, o diagnóstico/retiro correcto; 1 = se niega (mantenimiento o conexión
// en curso); 2 = la base no pasó las comprobaciones: la marca queda puesta y hay que restaurar un respaldo.
//
// Pasos (ver PROCEDIMIENTO_RETIRO_MARCA_MANTENIMIENTO.md):
//  1. Si no hay marca, no hay nada que hacer.
//  2. Si el proceso que creó la marca sigue vivo, es un mantenimiento en curso: no se toca.
//  3. Antes de abrir la base, se copia todo (base, diario -journal, -wal, -shm y la marca) a
//     datos/incidentes/<fecha>/. La copia se hace ANTES de abrir la base con SQLite.
//  4. Se abre la base sin pasar por conectar() (que la rechaza por la marca) y se toma el bloqueo
//     exclusivo sin esperar. Si otra conexión la tiene tomada, se niega. Al abrirla, SQLite deshace la
//     transacción que el corte dejó a medias (diario «caliente») o recupera lo confirmado del -wal.
//  5. Se comprueba la integridad, las claves foráneas, la versión del esquema y que existan las tablas,
//     el índice único (RN-01) y los disparadores del historial (RN-05, RN-06).
//  6. Se informa el estado: cantidades por tabla y comparación con el respaldo que tomó el reinicio
//     interrumpido (si lo hay). Los respaldos posteriores a la marca que no pasan la verificación se
//     apartan a la carpeta del incidente: nunca se usan para restaurar.
//  7. Solo con --retirar y todo correcto: se libera el bloqueo, se quita la marca y se comprueba que
//     conectar() vuelva a funcionar. Todo queda anotado en datos/incidentes/<fecha>/informe.txt.
require __DIR__ . '/src/db.php';
require __DIR__ . '/src/respaldo.php';

$retirar = in_array('--retirar', array_slice($argv, 1), true);
$base = ruta_base();
$marca = ruta_marca_mantenimiento();
$informe = array();
function decir($t)
{
    global $informe;
    $informe[] = $t;
    echo $t . PHP_EOL;
}
function terminar($cod)
{
    global $dir_incidente, $informe;
    if (!empty($dir_incidente)) {
        file_put_contents($dir_incidente . '/informe.txt', implode(PHP_EOL, $informe) . PHP_EOL);
    }
    exit($cod);
}

// 1. ¿Hay marca?
if (!file_exists($marca)) {
    echo "No hay marca de mantenimiento ($marca). No hay nada que hacer.\n";
    exit(0);
}
$contenido = trim((string) @file_get_contents($marca));
$partes = preg_split('/\s+/', $contenido);
$fecha_marca = isset($partes[0]) ? strtotime($partes[0]) : false;
$pid = isset($partes[1]) ? (int) $partes[1] : 0;
if ($fecha_marca === false) {
    $fecha_marca = filemtime($marca);
}
decir('Marca de mantenimiento encontrada: ' . $marca);
decir('  creada el ' . date('Y-m-d H:i:s', $fecha_marca) . ($pid ? " por el proceso $pid" : ' (sin proceso registrado)'));

// 2. ¿El mantenimiento sigue en curso?
if ($pid > 0 && $pid !== getmypid()) {
    $vivo = function_exists('posix_kill') ? @posix_kill($pid, 0) : file_exists("/proc/$pid");
    $cmd = is_readable("/proc/$pid/cmdline") ? str_replace("\0", ' ', (string) @file_get_contents("/proc/$pid/cmdline")) : '';
    if ($vivo && ($cmd === '' || stripos($cmd, 'php') !== false)) {
        decir("El proceso $pid sigue activo: es un mantenimiento en curso. No se toca nada; esperá a que termine.");
        exit(1);
    }
    if ($vivo) {
        decir("Aviso: el número de proceso $pid existe, pero no es PHP ($cmd); se toma como reutilizado por el sistema.");
    }
}

// 3. Copia del estado, antes de abrir la base con SQLite.
$dir_incidente = dirname($base) . '/incidentes/marca_' . date('Ymd_His');
if (!is_dir($dir_incidente) && !mkdir($dir_incidente, 0775, true)) {
    decir('No se pudo crear la carpeta del incidente. No se tocó nada.');
    exit(1);
}
$copiados = array();
foreach (array('', '-journal', '-wal', '-shm', '.mantenimiento') as $suf) {
    if (file_exists($base . $suf)) {
        if (!copy($base . $suf, $dir_incidente . '/' . basename($base) . $suf)) {
            decir("No se pudo copiar $base$suf. No se tocó nada.");
            terminar(1);
        }
        $copiados[] = basename($base) . $suf . ' (' . filesize($base . $suf) . ' bytes)';
    }
}
decir('Copia del estado guardada en ' . $dir_incidente . ': ' . implode(', ', $copiados));
$habia_diario = file_exists($base . '-journal') && filesize($base . '-journal') > 0;
$habia_wal = file_exists($base . '-wal') && filesize($base . '-wal') > 0;
if ($habia_diario) {
    decir('Hay un diario de transacción (-journal): el corte interrumpió una escritura. SQLite la va a deshacer al abrir la base.');
}
if ($habia_wal) {
    decir('Hay un archivo -wal: SQLite va a recuperar lo confirmado al abrir la base.');
}
if (!file_exists($base) || filesize($base) === 0) {
    decir('La base no existe o está vacía. La marca queda puesta: restaurá un respaldo (ver el procedimiento).');
    terminar(2);
}

// 4. Bloqueo exclusivo sin esperar.
$problemas = array();
try {
    $pdo = new PDO('sqlite:' . $base);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_TIMEOUT, 0);
    try {
        $pdo->exec('BEGIN EXCLUSIVE');
    } catch (PDOException $e) {
        if (stripos($e->getMessage(), 'locked') !== false || stripos($e->getMessage(), 'busy') !== false) {
            decir('Otra conexión tiene la base tomada. Detené el servidor (Ctrl+C) y cerrá otros programas, y volvé a ejecutar. No se tocó nada.');
            terminar(1);
        }
        throw $e;
    }
    // 5. Comprobaciones (dentro de la transacción exclusiva).
    $integridad = $pdo->query('PRAGMA integrity_check')->fetchColumn();
    if ($integridad !== 'ok') {
        $problemas[] = 'integrity_check: ' . $integridad;
    }
    if ($pdo->query('PRAGMA foreign_key_check')->fetch()) {
        $problemas[] = 'hay referencias inválidas (foreign_key_check)';
    }
    $version = (int) $pdo->query('PRAGMA user_version')->fetchColumn();
    if ($version !== VERSION_ESQUEMA) {
        $problemas[] = "versión del esquema $version (se esperaba " . VERSION_ESQUEMA . ')';
    }
    $nombres = $pdo->query("SELECT name FROM sqlite_master")->fetchAll(PDO::FETCH_COLUMN);
    $requeridos = array('obras', 'ejemplares', 'lectores', 'prestamos', 'usuarios', 'un_prestamo_activo_por_ejemplar',
        'prestamos_sin_borrado', 'prestamos_datos_fijos', 'devolucion_unica', 'ejemplar_con_historial', 'lector_con_historial');
    $faltan = array_diff($requeridos, $nombres);
    if ($faltan) {
        $problemas[] = 'faltan objetos del esquema: ' . implode(', ', $faltan);
    }
    $cuentas = array();
    if (!$faltan) {
        foreach (array('obras', 'ejemplares', 'lectores', 'prestamos', 'usuarios') as $t) {
            $cuentas[$t] = (int) $pdo->query("SELECT COUNT(*) FROM \"$t\"")->fetchColumn();
        }
        if ($cuentas['usuarios'] === 0) {
            $problemas[] = 'no hay ninguna cuenta de bibliotecaria';
        }
    }
} catch (PDOException $e) {
    $problemas[] = 'la base no se pudo leer: ' . $e->getMessage();
}

if ($problemas) {
    decir('La base NO pasó las comprobaciones:');
    foreach ($problemas as $p) {
        decir('  - ' . $p);
    }
    decir('La marca queda puesta, para que nadie use esta base. Restaurá el último respaldo verificado (ver el procedimiento, paso 6).');
    $pdo = null;
    terminar(2);
}
decir('La base pasó las comprobaciones: integridad, claves foráneas, esquema v' . VERSION_ESQUEMA . ', índice único y disparadores del historial.');
decir('  Cantidades: ' . implode(', ', array_map(function ($k, $v) { return "$k $v"; }, array_keys($cuentas), $cuentas)));
if ($habia_diario && file_exists($base . '-journal') && filesize($base . '-journal') > 0) {
    decir('Aviso: el diario sigue presente después de abrir la base.');
}

// 6. Respaldos tomados después de la marca (los del reinicio interrumpido).
$posteriores = array();
foreach (glob(dirname($base) . '/respaldos/*.sqlite') ?: array() as $r) {
    if (filemtime($r) >= $fecha_marca - 1) {
        $posteriores[] = $r;
    }
}
$bueno = null;
foreach ($posteriores as $r) {
    $ok = false;
    try {
        $c = new PDO('sqlite:' . $r, null, null, array(PDO::SQLITE_ATTR_OPEN_FLAGS => PDO::SQLITE_OPEN_READONLY));
        $c->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $ok = $c->query('PRAGMA integrity_check')->fetchColumn() === 'ok';
        $nr = $ok ? (int) $c->query('SELECT COUNT(*) FROM prestamos')->fetchColumn() : null;
        $c = null;
    } catch (PDOException $e) {
        $ok = false;
    }
    if ($ok) {
        $bueno = array($r, $nr);
        decir('Respaldo del reinicio interrumpido, verificado: ' . basename($r) . " ($nr préstamos).");
    } else {
        rename($r, $dir_incidente . '/' . basename($r) . '.incompleto');
        decir('Respaldo incompleto (el corte lo interrumpió): ' . basename($r) . ' se apartó a la carpeta del incidente. No usarlo.');
    }
}
if ($bueno !== null && isset($cuentas['prestamos'])) {
    if ($cuentas['prestamos'] === $bueno[1]) {
        decir('Indicio: la base tiene los mismos préstamos que el respaldo previo: el reinicio no llegó a confirmarse y los datos anteriores siguen en la base.');
    } else {
        decir('Indicio: la base tiene distinta cantidad de préstamos que el respaldo previo: el reinicio llegó a confirmarse. Los datos anteriores están en ' . basename($bueno[0]) . '.');
    }
} elseif (!$posteriores) {
    decir('No hay respaldos posteriores a la marca: el corte ocurrió antes de que el reinicio empezara a copiar o a modificar la base.');
}

$pdo->exec('ROLLBACK');
$pdo = null;

if (!$retirar) {
    decir('Diagnóstico terminado: se puede retirar la marca. Para hacerlo: php retirar_marca.php --retirar');
    terminar(0);
}

// 7. Retiro de la marca y prueba de conexión.
if (!unlink($marca)) {
    decir('No se pudo borrar la marca. Revisá los permisos de la carpeta datos/.');
    terminar(1);
}
try {
    $prueba = conectar();
    $prueba->query('SELECT COUNT(*) FROM prestamos')->fetchColumn();
    cerrar_conexion();
} catch (Exception $e) {
    decir('La marca se retiró, pero la conexión de prueba falló: ' . $e->getMessage());
    terminar(2);
}
decir('Marca retirada. La conexión de prueba funcionó: el sistema puede volver a usarse.');
terminar(0);
