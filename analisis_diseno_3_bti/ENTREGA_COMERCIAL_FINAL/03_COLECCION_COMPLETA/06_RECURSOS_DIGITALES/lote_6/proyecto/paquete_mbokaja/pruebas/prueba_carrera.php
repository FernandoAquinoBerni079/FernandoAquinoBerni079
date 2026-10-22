<?php
// Pedidos simultáneos en PROCESOS SEPARADOS, cada uno con su propia conexión a la misma base (P-07, RI-01 y RI-02).
// Uso: php pruebas/prueba_carrera.php
// Alcance: procesos de una misma computadora sobre un disco local. Es la prueba válida de simultaneidad:
// no se usa el servidor incorporado de PHP, que en Windows atiende los pedidos de a uno. No reemplaza una
// prueba en las computadoras de la institución.
require __DIR__ . '/_comun.php';
require __DIR__ . '/../src/db.php';
$RONDAS = 5;
$fallos = 0;
$n = 0;

function base_nueva($ruta, $n_ejemplares, $lectores)
{
    @unlink($ruta);
    $pdo = new PDO('sqlite:' . $ruta);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    crear_esquema($pdo);
    $pdo->exec("INSERT INTO parametros VALUES ('plazo_dias', 7), ('maximo_estudiante', 2), ('maximo_docente', 5)");
    $pdo->exec("INSERT INTO obras (codigo, titulo, autor) VALUES ('OB-0001', 'Obra de prueba', 'Autor de prueba')");
    $pdo->exec("INSERT INTO ediciones (codigo, obra_id) VALUES ('ED-0001', 1)");
    for ($i = 1; $i <= $n_ejemplares; $i++) {
        $pdo->exec(sprintf("INSERT INTO ejemplares (codigo, edicion_id) VALUES ('EJ-%04d', 1)", $i));
    }
    foreach ($lectores as $i => $tipo) {
        $pdo->exec(sprintf("INSERT INTO lectores (codigo, nombre, tipo, curso) VALUES ('LE-%04d', 'Lector %d', '%s', %s)", $i + 1, $i + 1, $tipo, $tipo === 'estudiante' ? "'3.º BTI'" : 'NULL'));
    }
}

// Lanza todos los pedidos con la misma hora de largada y junta las respuestas.
function carrera($ruta, $pedidos)
{
    $largada = sprintf('%.0f', (microtime(true) + 1.5) * 1e6);
    $procs = array();
    $salidas = array();
    foreach ($pedidos as $p) {
        $cmd = array(PHP_BINARY, __DIR__ . '/_trabajador.php', $ruta, $p[0], $p[1], $largada);
        $procs[] = proc_open($cmd, array(1 => array('pipe', 'w'), 2 => array('pipe', 'w')), $pipes);
        $salidas[] = $pipes;
    }
    $res = array();
    foreach ($procs as $i => $pr) {
        $res[] = trim(stream_get_contents($salidas[$i][1]) . stream_get_contents($salidas[$i][2]));
        proc_close($pr);
    }
    return $res;
}

$ruta = sys_get_temp_dir() . '/biblio_l4_carrera_' . getmypid() . '.sqlite';
$resumen = array();
$anotar = function ($regla, $res) use (&$resumen) {
    foreach ($res as $x) {
        $resumen["$regla: $x"] = (isset($resumen["$regla: $x"]) ? $resumen["$regla: $x"] : 0) + 1;
    }
};
for ($r = 1; $r <= $RONDAS; $r++) {
    // P-07 / RI-01: 12 lectores piden el mismo ejemplar a la vez.
    base_nueva($ruta, 1, array_fill(0, 12, 'estudiante'));
    $ped = array();
    for ($i = 1; $i <= 12; $i++) {
        $ped[] = array(sprintf('LE-%04d', $i), 'EJ-0001');
    }
    $res = carrera($ruta, $ped);
    $anotar('RI-01', $res);
    $pdo = new PDO('sqlite:' . $ruta);
    $activos = (int) $pdo->query('SELECT COUNT(*) FROM prestamos WHERE fecha_devolucion IS NULL')->fetchColumn();
    $ok = count(array_keys($res, 'ME-04'));
    comprobar("Ronda $r, P-07 (RI-01): 12 procesos piden EJ-0001 a la vez → $ok registrado (ME-04), " . count(array_keys($res, 'ME-03')) . " rechazos ME-03, $activos préstamo activo",
        $ok === 1 && $activos === 1 && count(array_keys($res, 'ME-03')) === 11);
    $pdo = null;

    // RI-02: un estudiante pide 8 ejemplares distintos a la vez (máximo 2) y una docente, 8 (máximo 5).
    foreach (array(array('estudiante', 2), array('docente', 5)) as $caso) {
        base_nueva($ruta, 8, array($caso[0]));
        $ped = array();
        for ($i = 1; $i <= 8; $i++) {
            $ped[] = array('LE-0001', sprintf('EJ-%04d', $i));
        }
        $res = carrera($ruta, $ped);
        $anotar('RI-02 ' . $caso[0], $res);
        $pdo = new PDO('sqlite:' . $ruta);
        $activos = (int) $pdo->query('SELECT COUNT(*) FROM prestamos WHERE fecha_devolucion IS NULL')->fetchColumn();
        $ok = count(array_keys($res, 'ME-04'));
        comprobar("Ronda $r, RI-02 ($caso[0], máximo $caso[1]): 8 pedidos simultáneos → $ok registrados, $activos activos", $ok === $caso[1] && $activos === $caso[1]);
        $pdo = null;
    }
}
@unlink($ruta);
echo PHP_EOL . 'Respuestas recibidas en las ' . $RONDAS . ' rondas (código del mensaje):' . PHP_EOL;
ksort($resumen);
foreach ($resumen as $k => $v) {
    echo "  $v × $k" . PHP_EOL;
}
echo 'Entorno: ' . PHP_OS_FAMILY . ' ' . php_uname('r') . ', PHP ' . PHP_VERSION . ', SQLite ' . (new PDO('sqlite::memory:'))->query('SELECT sqlite_version()')->fetchColumn() . PHP_EOL;
terminar_prueba();
