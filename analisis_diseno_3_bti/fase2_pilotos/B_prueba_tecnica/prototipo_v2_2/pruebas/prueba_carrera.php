<?php
// Solicitudes simultáneas en procesos separados contra la misma base. Uso: php pruebas/prueba_carrera.php
// Comprueba que RN-01 y RN-02 se cumplen cuando varias operaciones llegan a la vez.
// Alcance: procesos de una misma computadora sobre un disco local. No reemplaza una
// prueba con varias computadoras, con red ni en Windows.
require __DIR__ . '/../src/db.php';

$RONDAS = 5;
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

function base_nueva($ruta, $n_ejemplares, $n_lectores)
{
    @unlink($ruta);
    $pdo = new PDO('sqlite:' . $ruta);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    crear_esquema($pdo);
    $pdo->exec("INSERT INTO obras (titulo, autor, edicion) VALUES ('Obra', 'Autor', 'Ed.')");
    for ($i = 1; $i <= $n_ejemplares; $i++) {
        $pdo->exec("INSERT INTO ejemplares (obra_id, codigo) VALUES (1, 'E-$i')");
    }
    for ($i = 1; $i <= $n_lectores; $i++) {
        $pdo->exec("INSERT INTO lectores (codigo, nombre, curso) VALUES ('L-$i', 'Lector $i', '3.º')");
    }
}

// Lanza todos los pedidos con la misma hora de largada y junta las respuestas.
function carrera($ruta, $pedidos)
{
    $largada = sprintf('%.0f', (microtime(true) + 1.5) * 1e6);
    $procs = array();
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

$ruta = sys_get_temp_dir() . '/biblio_v2_carrera_' . getmypid() . '.sqlite';
$resumen = array();

for ($r = 1; $r <= $RONDAS; $r++) {
    // Escenario 1: 12 lectores piden el mismo ejemplar a la vez.
    base_nueva($ruta, 1, 12);
    $ped = array();
    for ($i = 1; $i <= 12; $i++) {
        $ped[] = array('E-1', "L-$i");
    }
    $res = carrera($ruta, $ped);
    $pdo = new PDO('sqlite:' . $ruta);
    $activos = (int) $pdo->query('SELECT COUNT(*) FROM prestamos WHERE fecha_devolucion IS NULL')->fetchColumn();
    $ok = count(array_keys($res, 'REGISTRADO'));
    foreach ($res as $x) {
        $resumen['RN-01: ' . $x] = (isset($resumen['RN-01: ' . $x]) ? $resumen['RN-01: ' . $x] : 0) + 1;
    }
    comprobar("Ronda $r, RN-01: 12 pedidos simultáneos del mismo ejemplar → $ok registrado, $activos préstamo activo", $ok === 1 && $activos === 1);
    $pdo = null;

    // Escenario 2: un lector pide 8 ejemplares distintos a la vez.
    base_nueva($ruta, 8, 1);
    $ped = array();
    for ($i = 1; $i <= 8; $i++) {
        $ped[] = array("E-$i", 'L-1');
    }
    $res = carrera($ruta, $ped);
    $pdo = new PDO('sqlite:' . $ruta);
    $activos = (int) $pdo->query('SELECT COUNT(*) FROM prestamos WHERE fecha_devolucion IS NULL')->fetchColumn();
    $ok = count(array_keys($res, 'REGISTRADO'));
    foreach ($res as $x) {
        $resumen['RN-02: ' . $x] = (isset($resumen['RN-02: ' . $x]) ? $resumen['RN-02: ' . $x] : 0) + 1;
    }
    comprobar("Ronda $r, RN-02: 8 pedidos simultáneos del mismo lector → $ok registrados, $activos préstamos activos", $ok === 2 && $activos === 2);
    $pdo = null;
}
@unlink($ruta);

echo PHP_EOL . 'Respuestas recibidas en las ' . $RONDAS . ' rondas:' . PHP_EOL;
ksort($resumen);
foreach ($resumen as $k => $v) {
    echo "  $v × $k" . PHP_EOL;
}
echo PHP_EOL . "Resultado: " . ($n - $fallos) . " de $n correctas" . PHP_EOL;
exit($fallos ? 1 : 0);
