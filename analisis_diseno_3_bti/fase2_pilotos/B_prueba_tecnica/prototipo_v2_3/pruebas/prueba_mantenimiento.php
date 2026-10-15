<?php
// Reinicio con conexiones activas: el instalador debe negarse o esperar, nunca reemplazar la base
// mientras otra conexión la usa. Uso: php pruebas/prueba_mantenimiento.php
$dir = sys_get_temp_dir() . '/biblio_v22_mant_' . getmypid();
@mkdir($dir);
$ruta = $dir . '/biblioteca.sqlite';
putenv('BIBLIO_DB=' . $ruta);
require __DIR__ . '/../src/db.php';
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
function instalar($args)
{
    exec(escapeshellarg(PHP_BINARY) . ' ' . escapeshellarg($GLOBALS['raiz'] . '/instalar.php') . ' ' . $args . ' 2>&1', $out, $cod);
    return array($cod, implode(' ', $out));
}
function abrir($modo = null)
{
    $p = new PDO('sqlite:' . $GLOBALS['ruta']);
    $p->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $p->setAttribute(PDO::ATTR_TIMEOUT, 5);
    if ($modo) {
        $p->exec("PRAGMA journal_mode = $modo");
    }
    return $p;
}
function prestamos()
{
    $p = abrir();
    return (int) $p->query('SELECT COUNT(*) FROM prestamos')->fetchColumn();
}
function respaldos()
{
    return count(glob($GLOBALS['dir'] . '/respaldos/antes_de_reiniciar_*.sqlite') ?: array());
}
function base_con_prestamos($modo)
{
    foreach (glob($GLOBALS['dir'] . '/*') as $f) {
        is_dir($f) ? exec('rm -rf ' . escapeshellarg($f)) : unlink($f);
    }
    instalar('--clave=prueba-1234');
    $p = abrir($modo);
    $p->exec("INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (1, 1, '2026-03-02', '2026-03-09'), (4, 2, '2026-03-02', '2026-03-09')");
    $p = null;
}
$marca = $ruta . '.mantenimiento';

foreach (array('DELETE', 'WAL') as $modo) {
    echo "-- Base en modo $modo" . PHP_EOL;

    // 1. Escritura sin confirmar en otra conexión: no se reinicia y la escritura sigue viva.
    base_con_prestamos($modo);
    $otra = abrir();
    $otra->exec('BEGIN IMMEDIATE');
    $otra->exec("INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (5, 3, '2026-03-03', '2026-03-10')");
    $t0 = microtime(true);
    list($cod, $sal) = instalar('--reiniciar --si --clave=prueba-1234');
    $dt = round(microtime(true) - $t0, 1);
    comprobar("$modo: con una escritura sin confirmar en otra conexión, el reinicio se niega (código $cod, esperó $dt s)", $cod === 1 && strpos($sal, 'Hay otra conexión') !== false);
    comprobar("$modo: …no dejó respaldo a medias ni marca de mantenimiento", respaldos() === 0 && !file_exists($marca));
    $otra->exec('COMMIT');
    $otra = null;
    comprobar("$modo: …y la escritura de la otra conexión se confirmó sobre la base intacta (3 préstamos)", prestamos() === 3);

    // 2. Transacción de lectura abierta en otra conexión: tampoco se reinicia.
    $otra = abrir();
    $otra->exec('BEGIN');
    $otra->query('SELECT COUNT(*) FROM prestamos')->fetchAll();
    list($cod) = instalar('--reiniciar --si --clave=prueba-1234');
    $otra->exec('COMMIT');
    $otra = null;
    comprobar("$modo: con una lectura en curso en otra conexión, el reinicio se niega y la base queda igual", $cod === 1 && prestamos() === 3);

    // 3. Una transacción que termina durante la espera: el reinicio espera y su respaldo la incluye.
    $script = 'putenv("BIBLIO_DB=' . $ruta . '"); $p = new PDO("sqlite:' . $ruta . '"); $p->setAttribute(3, 2);'
        . '$p->exec("BEGIN IMMEDIATE"); $p->exec("INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (6, 3, \'2026-03-04\', \'2026-03-11\')");'
        . 'echo "listo\n"; fflush(STDOUT); usleep(1500000); $p->exec("COMMIT");';
    $proc = proc_open(array(PHP_BINARY, '-r', $script), array(1 => array('pipe', 'w')), $pipes);
    fgets($pipes[1]);                       // la otra transacción ya está abierta
    list($cod, $sal) = instalar('--reiniciar --si --clave=prueba-1234');
    proc_close($proc);
    $r = glob($dir . '/respaldos/antes_de_reiniciar_*.sqlite');
    $en_resp = $r ? (int) (new PDO('sqlite:' . $r[0]))->query('SELECT COUNT(*) FROM prestamos')->fetchColumn() : -1;
    comprobar("$modo: si la otra transacción termina dentro de la espera, el reinicio se hace después (código $cod)", $cod === 0);
    comprobar("$modo: …y el respaldo incluye lo que esa transacción confirmó (4 préstamos; tiene $en_resp)", $en_resp === 4);
    comprobar("$modo: …la base reiniciada queda sin préstamos y sin marca de mantenimiento", prestamos() === 0 && !file_exists($marca));
}

// 3b. Durante la ventana de mantenimiento ninguna otra conexión puede leer ni escribir.
foreach (array('DELETE', 'WAL') as $modo) {
    base_con_prestamos($modo);
    $cmd = 'BIBLIO_DB=' . escapeshellarg($ruta) . ' BIBLIO_PRUEBA_PAUSA=2 ' . escapeshellarg(PHP_BINARY) . ' '
        . escapeshellarg($raiz . '/instalar.php') . ' --reiniciar --si --clave=prueba-1234';
    $proc = proc_open($cmd, array(1 => array('pipe', 'w'), 2 => array('pipe', 'w')), $pp);
    $t = microtime(true);
    while (!file_exists($marca) && microtime(true) - $t < 3) {
        usleep(20000);
    }
    usleep(500000);                          // el instalador ya tomó el bloqueo y está en la pausa
    $intruso = new PDO('sqlite:' . $ruta);
    $intruso->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $intruso->setAttribute(PDO::ATTR_TIMEOUT, 0);
    $lee = $escribe = true;
    try {
        $intruso->query('SELECT COUNT(*) FROM prestamos')->fetchAll();
    } catch (PDOException $e) {
        $lee = false;
    }
    try {
        $intruso->exec("INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (6, 3, '2026-03-04', '2026-03-11')");
    } catch (PDOException $e) {
        $escribe = false;
    }
    $intruso = null;
    $rechazo = false;
    try {
        conectar();
    } catch (EnMantenimiento $e) {
        $rechazo = true;
    }
    cerrar_conexion();
    stream_get_contents($pp[1]);
    $cod = proc_close($proc);
    comprobar("$modo: durante el mantenimiento otra conexión no puede leer ni escribir", !$escribe && !$lee);
    comprobar("$modo: durante el mantenimiento conectar() rechaza conexiones nuevas", $rechazo);
    comprobar("$modo: el reinicio termina bien y no queda nada de la escritura intentada", $cod === 0 && prestamos() === 0);
}

// 4. WAL: una conexión que ya leyó la base y quedó abierta, aunque inactiva, también impide el reinicio.
base_con_prestamos('WAL');
$inactiva = abrir();
$inactiva->query('SELECT COUNT(*) FROM prestamos')->fetchAll();
list($cod) = instalar('--reiniciar --si --clave=prueba-1234');
comprobar('WAL: con otra conexión abierta e inactiva, el reinicio se niega y la base queda igual', $cod === 1 && prestamos() === 2);
$inactiva = null;

// 5. DELETE: una conexión inactiva no impide el reinicio, pero la base no se reemplaza:
//    esa conexión ve después la base nueva y lo que escribe queda en el mismo archivo.
base_con_prestamos('DELETE');
$ino = fileinode($ruta);
$inactiva = abrir();
$inactiva->query('SELECT COUNT(*) FROM prestamos')->fetchAll();
list($cod) = instalar('--reiniciar --si --clave=prueba-1234');
comprobar('DELETE: con otra conexión inactiva, el reinicio se hace (código ' . $cod . ')', $cod === 0);
comprobar('DELETE: la base es el mismo archivo (mismo inodo); no se borró ni se reemplazó', fileinode($ruta) === $ino);
$ve = (int) $inactiva->query('SELECT COUNT(*) FROM prestamos')->fetchColumn();
comprobar("DELETE: la conexión que quedó abierta ve la base reiniciada ($ve préstamos)", $ve === 0);
$inactiva->exec("INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (1, 1, '2026-03-05', '2026-03-12')");
$inactiva = null;
comprobar('DELETE: lo que escribe esa conexión queda en la base (no en un archivo huérfano)', prestamos() === 1);

// 6. Marca de mantenimiento: rechaza conexiones nuevas, un segundo reinicio y el respaldo.
file_put_contents($marca, 'prueba');
$h = hash_file('sha256', $ruta);
$rechazo = false;
try {
    conectar();
} catch (EnMantenimiento $e) {
    $rechazo = true;
}
comprobar('Con la marca de mantenimiento, conectar() rechaza conexiones nuevas', $rechazo);
list($cod, $sal) = instalar('--reiniciar --si --clave=prueba-1234');
comprobar('Con la marca, otro reinicio se niega («mantenimiento en curso») y la base queda idéntica', $cod === 1 && strpos($sal, 'mantenimiento en curso') !== false && hash_file('sha256', $ruta) === $h);
exec(escapeshellarg(PHP_BINARY) . ' ' . escapeshellarg($raiz . '/respaldar.php') . ' 2>&1', $o, $cod);
comprobar('Con la marca, respaldar.php se niega sin error de PHP', $cod === 1 && strpos(implode(' ', $o), 'mantenimiento') !== false && stripos(implode(' ', $o), 'fatal') === false);
$puerto = 8790;
$srv = proc_open(array(PHP_BINARY, '-S', "127.0.0.1:$puerto", '-t', $raiz . '/public'), array(1 => array('file', '/dev/null', 'w'), 2 => array('file', '/dev/null', 'w')), $p2, null, array('BIBLIO_DB' => $ruta, 'PATH' => getenv('PATH')));
usleep(700000);
$ctx = stream_context_create(array('http' => array('ignore_errors' => true)));
$html = @file_get_contents("http://127.0.0.1:$puerto/", false, $ctx);
$estado = isset($http_response_header[0]) ? $http_response_header[0] : '';
comprobar('Con la marca, el catálogo web responde 503 con aviso de mantenimiento (' . trim($estado) . ')', strpos($estado, '503') !== false && strpos((string) $html, 'mantenimiento') !== false);
unlink($marca);
$html = @file_get_contents("http://127.0.0.1:$puerto/", false, $ctx);
$estado = isset($http_response_header[0]) ? $http_response_header[0] : '';
comprobar('Sin la marca, el catálogo vuelve a responder 200', strpos($estado, '200') !== false);
proc_terminate($srv);
proc_close($srv);

exec('rm -rf ' . escapeshellarg($dir));
echo PHP_EOL . "Resultado: " . ($n - $fallos) . " de $n correctas" . PHP_EOL;
exit($fallos ? 1 : 0);
