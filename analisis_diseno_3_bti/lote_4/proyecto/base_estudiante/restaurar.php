<?php
// Restaura un respaldo sin destruir datos sin aviso. Uso:
//   php restaurar.php datos/respaldos/respaldo_AAAAMMDD_HHMMSS.sqlite        (pide escribir RESTAURAR)
//   opción: --si (no pide confirmación; solo para pruebas automáticas)
// Pasos:
//  1. Comprueba el respaldo ANTES de tocar nada: se abre solo para lectura, tiene que pasar integrity_check,
//     tener la versión de esquema de este sistema y todas sus tablas.
//  2. Muestra cuántos registros tiene la base actual y cuántos el respaldo, y pide confirmación.
//  3. Hace un respaldo verificado de la base actual (datos/respaldos/antes_de_restaurar_*.sqlite).
//  4. Reemplaza el contenido dentro del mismo archivo, con el mantenimiento controlado del Piloto B
//     (src/mantenimiento.php): se niega si otra conexión usa la base, y si algo falla no cambia nada.
//  5. Comprueba que la base restaurada tenga las mismas cantidades que el respaldo.
require __DIR__ . '/src/db.php';
require __DIR__ . '/src/respaldo.php';

const TABLAS = array('parametros', 'obras', 'ediciones', 'ejemplares', 'lectores', 'cuentas', 'prestamos');

$args = array_slice($argv, 1);
$sin_preguntar = in_array('--si', $args, true);
$archivos = array_values(array_filter($args, function ($a) {
    return strpos($a, '--') !== 0;
}));
if (count($archivos) !== 1) {
    fwrite(STDERR, "Indicá el archivo de respaldo: php restaurar.php datos/respaldos/respaldo_....sqlite\nNo se modificó nada.\n");
    exit(1);
}
$origen = $archivos[0];
$ruta = ruta_base();

function cantidades(PDO $p)
{
    $c = array();
    foreach (TABLAS as $t) {
        $c[$t] = (int) $p->query('SELECT COUNT(*) FROM "' . $t . '"')->fetchColumn();
    }
    return $c;
}

// 1. El respaldo tiene que servir antes de tocar la base.
if (!is_file($origen) || filesize($origen) === 0) {
    fwrite(STDERR, "No existe el respaldo $origen. No se modificó nada.\n");
    exit(1);
}
if (file_exists($ruta) && realpath($origen) === realpath($ruta)) {
    fwrite(STDERR, "Ese archivo es la base en uso, no un respaldo. No se modificó nada.\n");
    exit(1);
}
try {
    $r = new PDO('sqlite:' . $origen, null, null, array(PDO::SQLITE_ATTR_OPEN_FLAGS => PDO::SQLITE_OPEN_READONLY));
    $r->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $estado = $r->query('PRAGMA integrity_check')->fetchColumn();
    $version = (int) $r->query('PRAGMA user_version')->fetchColumn();
    if ($estado !== 'ok' || $version !== VERSION_ESQUEMA) {
        throw new RuntimeException($estado !== 'ok' ? "no pasó integrity_check ($estado)" : "es de la versión de esquema $version, no de la " . VERSION_ESQUEMA);
    }
    $en_respaldo = cantidades($r);
} catch (Exception $e) {
    fwrite(STDERR, 'El respaldo no sirve: ' . $e->getMessage() . ". No se modificó nada.\n");
    exit(1);
}
$r = null;

// 2. Confirmación con las cantidades a la vista.
$actual = null;
if (file_exists($ruta) && filesize($ruta) > 0) {
    try {
        $actual = cantidades(conectar());
        cerrar_conexion();
    } catch (Exception $e) {
        fwrite(STDERR, 'No se pudo leer la base actual: ' . $e->getMessage() . ". No se modificó nada.\n");
        exit(1);
    }
}
echo "Respaldo a restaurar: $origen\n  " . json_encode($en_respaldo, JSON_UNESCAPED_UNICODE) . "\n";
echo "Base actual: " . ($actual ? json_encode($actual, JSON_UNESCAPED_UNICODE) : 'no existe') . "\n";
if (!$sin_preguntar) {
    echo "El contenido de la base actual se va a reemplazar por el del respaldo. Antes se guarda una copia verificada.\n"
        . "Detené el servidor (Ctrl+C) y cerrá cualquier otro programa que tenga la base abierta.\nEscribí RESTAURAR para confirmar: ";
    if (trim((string) fgets(STDIN)) !== 'RESTAURAR') {
        fwrite(STDERR, "Cancelado. No se modificó nada.\n");
        exit(1);
    }
}

// 3 y 4. Respaldo de la base actual y reemplazo del contenido en un mantenimiento controlado.
if ($actual === null) {
    $pdo = conectar();
    $pdo->exec('BEGIN');
    crear_esquema($pdo);
    $pdo->exec('COMMIT');
    cerrar_conexion();
}
// El número de proceso evita que dos restauraciones en el mismo segundo choquen: nunca se pisa un respaldo.
$copia = dirname($ruta) . '/respaldos/antes_de_restaurar_' . date('Ymd_His') . '_' . getmypid() . '.sqlite';
$error = reiniciar_con_mantenimiento($copia, function (PDO $pdo) use ($origen, $en_respaldo) {
    $r = new PDO('sqlite:' . $origen, null, null, array(PDO::SQLITE_ATTR_OPEN_FLAGS => PDO::SQLITE_OPEN_READONLY));
    $r->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    foreach (TABLAS as $t) {
        foreach ($r->query('SELECT * FROM "' . $t . '"')->fetchAll(PDO::FETCH_ASSOC) as $fila) {
            $cols = array_keys($fila);
            $st = $pdo->prepare('INSERT INTO "' . $t . '" ("' . implode('", "', $cols) . '") VALUES (' . implode(', ', array_fill(0, count($cols), '?')) . ')');
            $st->execute(array_values($fila));
        }
    }
    // 5. Si las cantidades no coinciden, la excepción deshace todo y la base queda como estaba.
    if (cantidades($pdo) !== $en_respaldo) {
        throw new RuntimeException('la base restaurada no tiene las mismas cantidades que el respaldo');
    }
});
if ($error !== null) {
    fwrite(STDERR, $error . "\n");
    exit(1);
}
echo "Copia de la base anterior, verificada: $copia\n";
echo "Restauración terminada y comprobada: la base tiene lo mismo que el respaldo.\n";
