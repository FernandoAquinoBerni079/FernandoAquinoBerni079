<?php
// Retiro de una marca de mantenimiento después de un corte (retirar_marca.php).
// Simula cortes reales: el proceso que hacía el mantenimiento muere con SIGKILL en distintos momentos.
// Uso: php pruebas/prueba_marca_huerfana.php   (solo Linux; requiere las extensiones posix y pdo_sqlite)
$dir = sys_get_temp_dir() . '/biblio_v23_marca_' . getmypid();
@mkdir($dir);
$ruta = $dir . '/biblioteca.sqlite';
putenv('BIBLIO_DB=' . $ruta);
require __DIR__ . '/../src/db.php';
$raiz = dirname(__DIR__);
$marca = $ruta . '.mantenimiento';

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
function php($script, $args = '')
{
    exec(escapeshellarg(PHP_BINARY) . ' ' . escapeshellarg($script) . ' ' . $args . ' 2>&1', $out, $cod);
    return array($cod, implode("\n", $out));
}
function retirar($args = '')
{
    return php($GLOBALS['raiz'] . '/retirar_marca.php', $args);
}
function abrir()
{
    $p = new PDO('sqlite:' . $GLOBALS['ruta']);
    $p->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $p->setAttribute(PDO::ATTR_TIMEOUT, 5);
    return $p;
}
function prestamos()
{
    return (int) abrir()->query('SELECT COUNT(*) FROM prestamos')->fetchColumn();
}
function base_nueva()
{
    exec('rm -rf ' . escapeshellarg($GLOBALS['dir']) . '/*');
    php($GLOBALS['raiz'] . '/instalar.php', '--clave=prueba-1234');
    $p = abrir();
    $p->exec("INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (1, 1, '2026-03-02', '2026-03-09'), (4, 2, '2026-03-02', '2026-03-09')");
    $p = null;
}
function incidentes()
{
    return glob($GLOBALS['dir'] . '/incidentes/marca_*') ?: array();
}

// 0. Sin marca.
base_nueva();
list($cod, $sal) = retirar();
comprobar("Sin marca: no hace nada (código $cod)", $cod === 0 && strpos($sal, 'No hay marca') !== false && !incidentes());

// 1. Mantenimiento en curso: la marca tiene el número de un proceso PHP vivo.
$vivo = proc_open(array(PHP_BINARY, '-r', 'sleep(30);'), array(), $pipes);
$pid = proc_get_status($vivo)['pid'];
file_put_contents($marca, date('c') . " $pid\n");
$h = hash_file('sha256', $ruta);
list($cod, $sal) = retirar('--retirar');
comprobar("Proceso del mantenimiento vivo: se niega (código $cod), la marca sigue y la base no cambió",
    $cod === 1 && strpos($sal, 'mantenimiento en curso') !== false && file_exists($marca) && hash_file('sha256', $ruta) === $h);
proc_terminate($vivo, 9);
proc_close($vivo);

// 2. Corte durante la espera del reinicio (antes del respaldo): la base no se tocó.
base_nueva();
$proc = proc_open(array(PHP_BINARY, $raiz . '/instalar.php', '--reiniciar', '--si', '--clave=prueba-1234'),
    array(1 => array('pipe', 'w'), 2 => array('pipe', 'w')), $pipes, null, array('BIBLIO_DB' => $ruta, 'BIBLIO_PRUEBA_PAUSA' => '30'));
$t0 = microtime(true);
while (!file_exists($marca) && microtime(true) - $t0 < 10) {
    usleep(50000);
}
usleep(800000);   // ya tomó el bloqueo y está en la pausa
proc_terminate($proc, 9);
proc_close($proc);
comprobar('Corte simulado durante el reinicio: quedó la marca huérfana', file_exists($marca));
$rechazo = false;
try {
    cerrar_conexion();
    conectar();
} catch (EnMantenimiento $e) {
    $rechazo = true;
}
comprobar('Con la marca huérfana, conectar() sigue rechazando conexiones', $rechazo);
list($cod, $sal) = retirar();
comprobar("Diagnóstico sin --retirar: correcto (código $cod), la marca sigue y no cambia la base", $cod === 0 && file_exists($marca) && strpos($sal, 'se puede retirar') !== false);
comprobar('El diagnóstico guardó la copia del estado y su informe en datos/incidentes/', count(incidentes()) >= 1 && file_exists(incidentes()[0] . '/informe.txt') && file_exists(incidentes()[0] . '/biblioteca.sqlite'));
list($cod, $sal) = retirar('--retirar');
comprobar("Con --retirar: retira la marca (código $cod) y la conexión de prueba funciona", $cod === 0 && !file_exists($marca) && strpos($sal, 'Marca retirada') !== false);
comprobar('Los dos préstamos anteriores al corte siguen en la base', prestamos() === 2);

// 3. Corte a mitad del reinicio: tablas borradas y recreadas sin confirmar, con diario caliente.
base_nueva();
list($cod, $sal) = php(__DIR__ . '/_corte.php', escapeshellarg($ruta) . ' diario');
comprobar('Corte a mitad del reinicio: quedan la marca y un diario (-journal) caliente', file_exists($marca) && file_exists($ruta . '-journal') && filesize($ruta . '-journal') > 0);
list($cod, $sal) = retirar('--retirar');
comprobar("SQLite deshace la transacción interrumpida al abrir; el retiro sale bien (código $cod)", $cod === 0 && !file_exists($marca) && strpos($sal, 'diario de transacción') !== false);
comprobar('Después del retiro: los dos préstamos originales siguen y no quedó la tabla del reinicio a medias',
    prestamos() === 2 && !abrir()->query("SELECT 1 FROM sqlite_master WHERE name = 'relleno'")->fetch());
$inc = incidentes();
comprobar('La copia del incidente conserva el diario caliente para revisión', (bool) glob(end($inc) . '/biblioteca.sqlite-journal'));

// 4. Base en modo WAL: lo confirmado antes del corte se recupera.
base_nueva();
list($cod, $sal) = php(__DIR__ . '/_corte.php', escapeshellarg($ruta) . ' wal');
comprobar('Corte con la base en modo WAL: quedan la marca y un -wal con datos', file_exists($marca) && file_exists($ruta . '-wal') && filesize($ruta . '-wal') > 0);
list($cod, $sal) = retirar('--retirar');
comprobar("Retiro en modo WAL (código $cod) y el préstamo confirmado antes del corte aparece", $cod === 0 && !file_exists($marca) && prestamos() === 3);

// 5. Otra conexión tiene la base tomada: se niega sin tocar nada.
base_nueva();
file_put_contents($marca, date('c') . " 999999\n");
$otra = abrir();
$otra->exec('BEGIN EXCLUSIVE');
list($cod, $sal) = retirar('--retirar');
comprobar("Otra conexión con la base tomada: se niega (código $cod) y la marca sigue", $cod === 1 && strpos($sal, 'Otra conexión') !== false && file_exists($marca));
$otra->exec('ROLLBACK');
$otra = null;

// 6. Respaldo a medias posterior a la marca: se aparta y no se usa.
@mkdir($dir . '/respaldos');
$parcial = $dir . '/respaldos/antes_de_reiniciar_' . date('Ymd_His') . '.sqlite';
file_put_contents($parcial, 'SQLite format 3' . str_repeat("\0", 50));
touch($parcial, time() + 1);
list($cod, $sal) = retirar('--retirar');
comprobar("Respaldo incompleto posterior a la marca: se aparta a la carpeta del incidente (código $cod)",
    $cod === 0 && !file_exists($parcial) && strpos($sal, 'Respaldo incompleto') !== false && (bool) glob($dir . '/incidentes/*/*.incompleto'));

// 7. Base dañada: no se retira la marca.
base_nueva();
file_put_contents($marca, date('c') . " 999999\n");
$f = fopen($ruta, 'r+');
fwrite($f, str_repeat("\0", 100));
fclose($f);
list($cod, $sal) = retirar('--retirar');
comprobar("Base dañada: no pasa las comprobaciones (código $cod), la marca queda puesta y se indica restaurar",
    $cod === 2 && file_exists($marca) && strpos($sal, 'Restaurá') !== false);
$rechazo = false;
try {
    cerrar_conexion();
    conectar();
} catch (EnMantenimiento $e) {
    $rechazo = true;
}
comprobar('Con la base dañada, el sistema sigue bloqueado por la marca', $rechazo);

// 8. Esquema incompleto (falta un disparador del historial): no se retira la marca.
base_nueva();
abrir()->exec('DROP TRIGGER prestamos_sin_borrado');
file_put_contents($marca, date('c') . " 999999\n");
list($cod, $sal) = retirar('--retirar');
comprobar("Falta el disparador del historial (RN-05): no se retira la marca (código $cod)", $cod === 2 && file_exists($marca) && strpos($sal, 'prestamos_sin_borrado') !== false);

exec('rm -rf ' . escapeshellarg($dir));
echo PHP_EOL . "Resultado: " . ($n - $fallos) . " de $n correctos" . PHP_EOL;
exit($fallos ? 1 : 0);
