<?php
// Respaldo antes de reiniciar: consistencia y verificación. Uso: php pruebas/prueba_respaldo.php
// Compara el método anterior (copy() del archivo) con el actual (VACUUM INTO + verificación).
$dir = sys_get_temp_dir() . '/biblio_v22_respaldo_' . getmypid();
@mkdir($dir);
$ruta = $dir . '/biblioteca.sqlite';
putenv('BIBLIO_DB=' . $ruta);
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/respaldo.php';
$raiz = dirname(__DIR__);

$fallos = 0;
$n = 0;
function comprobar($desc, $cond)
{
    global $fallos, $n;
    $n++;
    if (!$cond) {
        $fallos++;
    }
    echo ($cond ? 'CORRECTO ' : 'FALLA    ') . $desc . PHP_EOL;
}
function prestamos_en($archivo)
{
    $p = new PDO('sqlite:' . $archivo);
    return (int) $p->query('SELECT COUNT(*) FROM prestamos')->fetchColumn();
}
function instalar($args)
{
    exec(escapeshellarg(PHP_BINARY) . ' ' . escapeshellarg($GLOBALS['raiz'] . '/instalar.php') . ' ' . $args . ' 2>&1', $out, $cod);
    return array($cod, implode("\n", $out));
}

list($cod) = instalar('--clave=prueba-1234');
comprobar('Instalación inicial', $cod === 0);
$pdo = conectar();
registrar_prestamo($pdo, 'EJ-0001', 'L-001', '2026-03-02');
registrar_prestamo($pdo, 'EJ-0004', 'L-002', '2026-03-02');
cerrar_conexion();

// Otra conexión pasa la base a modo WAL, confirma dos préstamos y queda abierta:
// lo confirmado sigue en el archivo -wal, todavía no en biblioteca.sqlite.
$otra = new PDO('sqlite:' . $ruta);
$otra->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$otra->exec('PRAGMA journal_mode = WAL');
$otra->exec('PRAGMA wal_autocheckpoint = 0');
$otra->exec("INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (2, 3, '2026-03-03', '2026-03-10')");
$otra->exec("INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (5, 3, '2026-03-03', '2026-03-10')");
$confirmados = (int) $otra->query('SELECT COUNT(*) FROM prestamos')->fetchColumn();
comprobar("Hay $confirmados préstamos confirmados; parte de ellos está solo en el archivo -wal", $confirmados === 4 && filesize($ruta . '-wal') > 0);

// Método anterior: copiar el archivo.
// La copia se hace en otro proceso: si este proceso abriera y cerrara el archivo de la base con
// copy(), el sistema operativo soltaría los bloqueos POSIX de $otra (advertencia de la documentación
// de SQLite: abrir y cerrar el archivo de una base por fuera de SQLite rompe sus bloqueos).
exec(escapeshellarg(PHP_BINARY) . ' -r ' . escapeshellarg('copy($argv[1], $argv[2]);') . ' ' . escapeshellarg($ruta) . ' ' . escapeshellarg($dir . '/copia_anterior.sqlite'));
$en_copia = prestamos_en($dir . '/copia_anterior.sqlite');
comprobar("Método anterior (copy): la copia tiene $en_copia de $confirmados préstamos (pierde lo que está en -wal)", $en_copia < $confirmados);

// Una escritura sin confirmar mientras se respalda: no debe aparecer en el respaldo.
$otra->exec('BEGIN IMMEDIATE');
$otra->exec("INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (6, 3, '2026-03-04', '2026-03-11')");

// v2.2: respaldar.php sí puede trabajar con la otra conexión abierta (solo lee una instantánea).
exec(escapeshellarg(PHP_BINARY) . ' ' . escapeshellarg($raiz . '/respaldar.php') . ' 2>&1', $o0, $c0);
$r0 = glob($dir . '/respaldos/respaldo_*.sqlite');
$en_r0 = $r0 ? prestamos_en($r0[0]) : -1;
comprobar("respaldar.php con la otra conexión abierta: el respaldo tiene los $confirmados préstamos confirmados (tiene $en_r0)", $c0 === 0 && $en_r0 === $confirmados);
$sin_confirmar = $r0 ? (int) (new PDO('sqlite:' . $r0[0]))->query('SELECT COUNT(*) FROM prestamos WHERE ejemplar_id = 6')->fetchColumn() : -1;
comprobar('…y no incluye la escritura sin confirmar (ejemplar 6)', $sin_confirmar === 0);
$chk = $r0 ? (new PDO('sqlite:' . $r0[0]))->query('PRAGMA integrity_check')->fetchColumn() : '';
comprobar('…y pasa PRAGMA integrity_check', $chk === 'ok');
foreach ($r0 as $f) {
    unlink($f);
}

// v2.2: el reinicio, en cambio, se niega mientras la otra conexión tenga la transacción abierta.
list($cod, $salida) = instalar('--reiniciar --si --clave=prueba-1234');
comprobar('instalar.php --reiniciar se niega mientras otra conexión usa la base (detalle en prueba_mantenimiento.php)', $cod === 1);
$otra->exec('ROLLBACK');
$otra = null;

// Sin otras conexiones, el reinicio se hace con respaldo verificado.
list($cod, $salida) = instalar('--reiniciar --si --clave=prueba-1234');
comprobar('Sin otras conexiones, instalar.php --reiniciar termina bien', $cod === 0);
$resp = glob($dir . '/respaldos/antes_de_reiniciar_*.sqlite');
comprobar('Dejó un respaldo «antes_de_reiniciar»', count($resp) === 1);
$enr = $resp ? prestamos_en($resp[0]) : -1;
comprobar("El respaldo tiene los $confirmados préstamos confirmados (tiene $enr)", $enr === $confirmados);
$guardado = $dir . '/respaldo_previo_guardado.sqlite';
copy($resp[0], $guardado);
$chk = $resp ? (new PDO('sqlite:' . $resp[0]))->query('PRAGMA integrity_check')->fetchColumn() : '';
comprobar('El respaldo pasa PRAGMA integrity_check', $chk === 'ok');
comprobar('El instalador informa «Respaldo verificado»', strpos($salida, 'Respaldo verificado') !== false);
comprobar('La base reiniciada queda sin préstamos', prestamos_en($ruta) === 0);
$ic = (new PDO('sqlite:' . $ruta))->query('PRAGMA integrity_check')->fetchColumn();
comprobar('La base reiniciada (en el mismo archivo) pasa PRAGMA integrity_check', $ic === 'ok');

// Si el respaldo no se puede hacer, el instalador no toca la base.
$pdo = conectar();
registrar_prestamo($pdo, 'EJ-0001', 'L-001', '2026-03-05');
cerrar_conexion();
foreach (glob($dir . '/respaldos/*') as $f) {
    unlink($f);
}
rmdir($dir . '/respaldos');
file_put_contents($dir . '/respaldos', 'esto no es una carpeta');   // impide crear la carpeta de respaldos
$h = hash_file('sha256', $ruta);
list($cod, $salida) = instalar('--reiniciar --si --clave=prueba-1234');
comprobar('Sin respaldo posible, el instalador se niega (código 1)', $cod === 1);
comprobar('…y la base queda idéntica (mismo SHA-256)', hash_file('sha256', $ruta) === $h);
unlink($dir . '/respaldos');

// respaldar.php usa el mismo procedimiento.
exec(escapeshellarg(PHP_BINARY) . ' ' . escapeshellarg($raiz . '/respaldar.php') . ' 2>&1', $out, $cod);
$r = glob($dir . '/respaldos/respaldo_*.sqlite');
comprobar('respaldar.php crea un respaldo verificado con el mismo procedimiento', $cod === 0 && count($r) === 1 && prestamos_en($r[0]) === 1);

// Restauración manual del respaldo previo al reinicio.
foreach (array('', '-wal', '-shm', '-journal') as $suf) {
    @unlink($ruta . $suf);
}
copy($guardado, $ruta);
comprobar("Restaurar el respaldo previo devuelve los $confirmados préstamos", file_exists($ruta) && prestamos_en($ruta) === $confirmados);

exec('rm -rf ' . escapeshellarg($dir));
echo PHP_EOL . "Resultado: " . ($n - $fallos) . " de $n correctas" . PHP_EOL;
exit($fallos ? 1 : 0);
