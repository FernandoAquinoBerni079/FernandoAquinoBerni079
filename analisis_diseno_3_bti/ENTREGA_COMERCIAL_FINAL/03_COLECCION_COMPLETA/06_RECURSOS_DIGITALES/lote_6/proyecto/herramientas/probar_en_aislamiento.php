<?php
// Pruebas funcionales de un paquete recibido, en aislamiento (Capítulo 17). Herramienta del docente: vive fuera del
// paquete y es la única que ejecuta código del paquete, siguiendo el procedimiento de herramientas/LEEME.md.
// Uso: php probar_en_aislamiento.php <carpeta del paquete> [--limite=SEGUNDOS]
// - Solo ejecuta pruebas de una lista cerrada, que están en esta herramienta. Nunca ejecuta un texto del paquete:
//   arma ella misma cada comando, sin pasar por la consola del sistema.
// - Se niega a correr con una cuenta de administrador y con un paquete que tenga enlaces simbólicos.
// - Trabaja en una copia descartable, con un entorno mínimo y un tiempo límite por prueba, y la borra al terminar.
// - El corte de la red no lo puede hacer PHP: lo pide el procedimiento (equipo sin red o espacio de red aislado).
const PRUEBAS_PERMITIDAS = array('prueba_contratos', 'prueba_garantias', 'prueba_respaldo');
$op = array();
foreach (array_slice($argv, 1) as $a) {
    if (preg_match('/^--([a-z-]+)(?:=(.*))?$/', $a, $m)) {
        $op[$m[1]] = isset($m[2]) ? $m[2] : true;
    } else {
        $op['paquete'] = $a;
    }
}
function salir($texto)
{
    fwrite(STDERR, $texto . PHP_EOL . 'No se ejecutó ninguna prueba.' . PHP_EOL);
    exit(2);
}
if (empty($op['paquete']) || !is_dir($op['paquete'])) {
    salir('Uso: php probar_en_aislamiento.php <carpeta del paquete> [--limite=SEGUNDOS]');
}
if (function_exists('posix_geteuid')) {
    if (posix_geteuid() === 0) {
        salir('Esta herramienta no se ejecuta con una cuenta de administrador: usá una cuenta sin permisos.');
    }
} elseif (empty($op['cuenta-sin-permisos-de-administrador'])) {
    salir('En Windows, confirmá que usás una cuenta estándar: --cuenta-sin-permisos-de-administrador');
}
$origen = rtrim(realpath($op['paquete']), '/\\');
$limite = isset($op['limite']) ? max(1, (int) $op['limite']) : 120;
$todo = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($origen, FilesystemIterator::SKIP_DOTS),
                                      RecursiveIteratorIterator::SELF_FIRST);
foreach ($todo as $f) {
    if ($f->isLink()) {
        salir('El paquete tiene un enlace simbólico (' . $f->getFilename() . '): no se copia ni se prueba.');
    }
}

// Copia descartable, sin bases de datos.
$copia = sys_get_temp_dir() . '/ads_aislado_' . bin2hex(random_bytes(6));
mkdir($copia, 0700);
foreach ($todo as $f) {
    $rel = substr($f->getPathname(), strlen($origen) + 1);
    if ($f->isDir()) {
        mkdir("$copia/$rel", 0700, true);
    } elseif (!preg_match('/\.sqlite/', $rel)) {
        copy($f->getPathname(), "$copia/$rel");
    }
}
mkdir("$copia/.tmp", 0700);
$entorno = array('PATH' => '/usr/bin:/bin', 'HOME' => $copia, 'TMPDIR' => "$copia/.tmp", 'LANG' => 'C.UTF-8');

// Solo las pruebas de la lista cerrada que el paquete trae.
$faltas = array();
foreach (PRUEBAS_PERMITIDAS as $nombre) {
    if (!is_file("$copia/pruebas/$nombre.php")) {
        continue;
    }
    // El comando es una lista de argumentos: no pasa por la consola del sistema.
    $comando = array(PHP_BINARY, "pruebas/$nombre.php");
    $tubos_def = array(array('pipe', 'r'), array('pipe', 'w'), array('pipe', 'w'));
    $proc = proc_open($comando, $tubos_def, $tubos, $copia, $entorno);
    fclose($tubos[0]);
    stream_set_blocking($tubos[1], false);
    stream_set_blocking($tubos[2], false);
    $salida = '';
    $inicio = time();
    do {
        $salida .= stream_get_contents($tubos[1]);
        stream_get_contents($tubos[2]);
        $estado = proc_get_status($proc);
        usleep(100000);
    } while ($estado['running'] && time() - $inicio < $limite);
    if ($estado['running']) {
        proc_terminate($proc, 9);
        $ultima = "superó el tiempo límite de $limite s";
        $codigo = -1;
    } else {
        $salida .= stream_get_contents($tubos[1]);
        $lineas = array_filter(array_map('trim', explode("\n", $salida)));
        $ultima = (string) end($lineas);
        $codigo = $estado['exitcode'];
    }
    proc_close($proc);
    $bien = $codigo === 0 && strpos($ultima, 'Resultado:') === 0;
    $estado_prueba = $bien ? 'PRUEBA BIEN  ' : 'PRUEBA FALLA ';
    echo $estado_prueba . "pruebas/$nombre.php — $ultima" . PHP_EOL;
    if (!$bien) {
        $faltas[] = "INCOHERENCIA [C] la prueba pruebas/$nombre.php no terminó bien";
    }
}

// Se borra la copia.
$borrar = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($copia, FilesystemIterator::SKIP_DOTS),
                                        RecursiveIteratorIterator::CHILD_FIRST);
foreach ($borrar as $f) {
    $f->isDir() && !$f->isLink() ? rmdir($f->getPathname()) : unlink($f->getPathname());
}
rmdir($copia);
echo implode(PHP_EOL, $faltas) . ($faltas ? PHP_EOL : '');
echo 'Resultado: ' . count($faltas) . ' incoherencias (pruebas en una copia descartable, ya borrada)' . PHP_EOL;
exit($faltas ? 1 : 0);
