<?php
// Instalación, respaldo y restauración sin pérdida de datos. Uso: php pruebas/prueba_respaldo.php
// Del Piloto B v2.3 (instalador protegido y respaldo consistente), más la restauración segura del lote 4:
// una instalación de prueba no borra una base existente y una restauración no destruye datos sin aviso
// ni sin un respaldo verificado de lo que había.
require __DIR__ . '/_comun.php';
list($dir, $ruta) = base_de_prueba('respaldo');
require __DIR__ . '/../src/db.php';
$raiz = dirname(__DIR__);
$fallos = 0;
$n = 0;

function php_script($script, $args = '', $entrada = null)
{
    $cmd = escapeshellarg(PHP_BINARY) . ' ' . escapeshellarg($GLOBALS['raiz'] . '/' . $script) . ' ' . $args . ' 2>&1';
    if ($entrada !== null) {
        $cmd = 'echo ' . escapeshellarg($entrada) . ' | ' . $cmd;
    }
    exec($cmd, $out, $cod);
    return array($cod, implode("\n", $out));
}
function prestamos_en($archivo)
{
    return (int) (new PDO('sqlite:' . $archivo))->query('SELECT COUNT(*) FROM prestamos')->fetchColumn();
}
function sha()
{
    return hash_file('sha256', $GLOBALS['ruta']);
}
function prestar($pdo, $ej, $le, $fecha)
{
    $pdo->exec("INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES ($ej, $le, '$fecha', date('$fecha', '+7 days'))");
}

// 1. Instalador protegido.
list($cod) = php_script('instalar.php', '--clave=prueba-solo-local');
comprobar('Instalación inicial con datos ficticios', $cod === 0);
$pdo = conectar();
prestar($pdo, 1, 1, '2026-03-02');
prestar($pdo, 4, 2, '2026-03-02');
cerrar_conexion();
$h = sha();
list($cod) = php_script('instalar.php', '--clave=prueba-solo-local');
comprobar('Instalar de nuevo sin --reiniciar: se niega (código 1) y la base queda idéntica', $cod === 1 && sha() === $h);
list($cod) = php_script('instalar.php', '--reiniciar', 'NO');
comprobar('--reiniciar sin escribir REINICIAR: cancela y la base queda idéntica', $cod === 1 && sha() === $h);

// 2. Respaldo consistente con otra conexión en modo WAL (del Piloto B).
$otra = new PDO('sqlite:' . $ruta);
$otra->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$otra->exec('PRAGMA journal_mode = WAL');
$otra->exec('PRAGMA wal_autocheckpoint = 0');
prestar($otra, 5, 2, '2026-03-03');
$confirmados = (int) $otra->query('SELECT COUNT(*) FROM prestamos')->fetchColumn();
exec(escapeshellarg(PHP_BINARY) . ' -r ' . escapeshellarg('copy($argv[1], $argv[2]);') . ' ' . escapeshellarg($ruta) . ' ' . escapeshellarg($dir . '/copia.sqlite'));
comprobar("Copiar el archivo a mano pierde lo que está en -wal (" . prestamos_en($dir . '/copia.sqlite') . " de $confirmados préstamos)", prestamos_en($dir . '/copia.sqlite') < $confirmados);
$otra->exec('BEGIN IMMEDIATE');
prestar($otra, 6, 2, '2026-03-04');
list($cod) = php_script('respaldar.php');
$r = glob($dir . '/respaldos/respaldo_*.sqlite');
comprobar("respaldar.php con la otra conexión abierta: tiene los $confirmados préstamos confirmados y no el que está sin confirmar",
    $cod === 0 && count($r) === 1 && prestamos_en($r[0]) === $confirmados);
$respaldo = $r[0];

// 3. Restauración: se niega sin tocar nada cuando no corresponde.
list($cod) = php_script('restaurar.php', '--si ' . escapeshellarg($respaldo));
comprobar('restaurar.php se niega mientras otra conexión tiene una escritura en curso', $cod === 1);
$otra->exec('ROLLBACK');
$otra->exec('PRAGMA journal_mode = DELETE');
$otra = null;
$pdo = conectar();
prestar($pdo, 6, 2, '2026-03-05');
cerrar_conexion();
$h = sha();
$antes = prestamos_en($ruta);
list($cod, $sal) = php_script('restaurar.php', '--si ' . escapeshellarg($dir . '/no_existe.sqlite'));
comprobar('Restaurar un archivo que no existe: se niega y la base queda idéntica', $cod === 1 && sha() === $h);
file_put_contents($dir . '/roto.sqlite', random_bytes(4096));
list($cod, $sal) = php_script('restaurar.php', '--si ' . escapeshellarg($dir . '/roto.sqlite'));
comprobar('Restaurar un archivo dañado: se niega («El respaldo no sirve») y la base queda idéntica', $cod === 1 && strpos($sal, 'no sirve') !== false && sha() === $h);
$viejo = new PDO('sqlite:' . $dir . '/viejo.sqlite');
$viejo->exec('CREATE TABLE prestamos (id INTEGER); PRAGMA user_version = 2');
$viejo = null;
list($cod, $sal) = php_script('restaurar.php', '--si ' . escapeshellarg($dir . '/viejo.sqlite'));
comprobar('Restaurar un respaldo de otra versión del esquema (la del Piloto B): se niega y la base queda idéntica', $cod === 1 && sha() === $h);
list($cod) = php_script('restaurar.php', '--si ' . escapeshellarg($ruta));
comprobar('Restaurar la base en uso sobre sí misma: se niega', $cod === 1 && sha() === $h);
list($cod) = php_script('restaurar.php', escapeshellarg($respaldo), 'no');
comprobar('Sin escribir RESTAURAR: cancela y la base queda idéntica', $cod === 1 && sha() === $h);

// 4. Restauración confirmada: respaldo previo verificado y base igual al respaldo.
list($cod, $sal) = php_script('restaurar.php', escapeshellarg($respaldo), 'RESTAURAR');
comprobar('Con confirmación, restaurar.php termina bien', $cod === 0 && strpos($sal, 'comprobada') !== false);
comprobar("La base vuelve a tener los $confirmados préstamos del respaldo", prestamos_en($ruta) === $confirmados);
$previo = glob($dir . '/respaldos/antes_de_restaurar_*.sqlite');
comprobar("Antes de restaurar guardó la base anterior, con sus $antes préstamos", count($previo) === 1 && prestamos_en($previo[0]) === $antes);
comprobar('Ese respaldo previo pasa PRAGMA integrity_check', $previo && (new PDO('sqlite:' . $previo[0]))->query('PRAGMA integrity_check')->fetchColumn() === 'ok');
$pdo = conectar();
comprobar('La base restaurada conserva el índice de RI-01 y los disparadores del historial',
    contar($pdo, "SELECT COUNT(*) FROM sqlite_master WHERE name IN ('un_prestamo_activo_por_ejemplar', 'prestamos_sin_borrado', 'lector_con_historial')") === 3);
comprobar('La base restaurada conserva las cuentas (se puede volver a ingresar)', contar($pdo, 'SELECT COUNT(*) FROM cuentas') === 2);
cerrar_conexion();
list($cod) = php_script('restaurar.php', '--si ' . escapeshellarg($previo[0]));
comprobar("Deshacer la restauración con el respaldo previo devuelve los $antes préstamos", $cod === 0 && prestamos_en($ruta) === $antes);

// 5. Reinicio controlado (del Piloto B): si no puede respaldar, no toca la base.
foreach (glob($dir . '/respaldos/*') as $f) {
    unlink($f);
}
rmdir($dir . '/respaldos');
file_put_contents($dir . '/respaldos', 'esto no es una carpeta');
$h = sha();
list($cod) = php_script('instalar.php', '--reiniciar --si --clave=prueba-solo-local');
comprobar('Sin respaldo posible, el reinicio se niega y la base queda idéntica', $cod === 1 && sha() === $h);
unlink($dir . '/respaldos');
list($cod, $sal) = php_script('instalar.php', '--reiniciar --si --clave=prueba-solo-local');
comprobar('Con respaldo posible, el reinicio guarda un respaldo verificado y deja la base sin préstamos',
    $cod === 0 && strpos($sal, 'Respaldo verificado') !== false && prestamos_en($ruta) === 0 && count(glob($dir . '/respaldos/antes_de_reiniciar_*.sqlite')) === 1);

exec('rm -rf ' . escapeshellarg($dir));
terminar_prueba();
