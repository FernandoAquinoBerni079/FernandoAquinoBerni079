<?php
// Comprobación de la Práctica 11 (lote 4 v1.1): la carga del lote de Mbokaja con la correspondencia fija da los
// mensajes y las cantidades que espera la guía docente. Usa el código de la referencia docente SIN MODIFICARLO, sobre
// una base temporal propia con los datos ficticios de ejemplo: no toca ninguna base instalada ni la base Arapoty.
// Los pasos se leen de secuencia.json, que build/reproducir.py genera desde caso/mbokaja_u4.py (PASOS_P11).
// Uso: php comprobar_practica_11.php [carpeta del sistema]   (por defecto, la referencia docente)
$sistema = realpath($argv[1] ?? (__DIR__ . '/../proyecto/referencia_docente'));
require $sistema . '/pruebas/_comun.php';
list($dir, $ruta) = base_de_prueba('practica_11');
require $sistema . '/src/db.php';
require $sistema . '/src/mensajes.php';
require $sistema . '/src/auth.php';
require $sistema . '/src/reglas.php';
require $sistema . '/src/datos_ejemplo.php';
$fallos = 0;
$n = 0;
$pdo = conectar();
$pdo->exec('BEGIN');
crear_esquema($pdo);
sembrar_ejemplo($pdo, null);
$pdo->exec('COMMIT');
$bib = cuenta('bibliotecaria');
$sec = json_decode(file_get_contents(__DIR__ . '/secuencia.json'), true);
$operacion = array('OA-01' => 'alta_ejemplar', 'OA-02' => 'alta_obra_edicion', 'OA-03' => 'alta_lector');

foreach ($sec['pasos'] as $p) {
    list($paso, $fuente, $op, $entradas, $esperado) = $p;
    $antes = huella($pdo);
    $r = call_user_func_array($operacion[$op], array_merge(array($pdo, $bib), $entradas));
    $sin_cambios = $r['ok'] || huella($pdo) === $antes;
    comprobar(sprintf('Paso %d (%s, %s %s) → %s%s', $paso, $fuente, $op, implode(' · ', array_filter($entradas, 'strlen')),
        $esperado, $r['ok'] ? '' : ' y sin cambios'), $r['codigo'] === $esperado && $sin_cambios);
}
foreach ($sec['consultas'] as $c) {
    list($texto, $obras, $ejemplares, $disponibles, $mensaje) = $c;
    $r = consultar_disponibilidad($pdo, $texto);
    if ($mensaje !== null) {
        comprobar("Consulta pública «{$texto}» → $mensaje", $r['codigo'] === $mensaje);
        continue;
    }
    $f = $r['filas'];
    comprobar("Consulta pública «{$texto}» → $obras obra, $ejemplares ejemplares, $disponibles disponibles",
        count($f) === $obras && (int) $f[0]['ejemplares'] === $ejemplares && (int) $f[0]['disponibles'] === $disponibles);
}
comprobar('Ningún dato de lectores en la consulta pública',
    !array_filter(consultar_disponibilidad($pdo, 'a')['filas'], function ($f) { return isset($f['lector']) || isset($f['nombre']); }));
cerrar_conexion();
exec('rm -rf ' . escapeshellarg($dir));
echo 'Entorno: ' . php_uname('s') . ' ' . php_uname('r') . ', PHP ' . PHP_VERSION . ', SQLite '
    . (new PDO('sqlite::memory:'))->query('SELECT sqlite_version()')->fetchColumn() . PHP_EOL;
terminar_prueba();
