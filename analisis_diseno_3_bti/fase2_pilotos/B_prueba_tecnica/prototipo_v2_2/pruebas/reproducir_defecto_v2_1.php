<?php
// Reproduce el defecto del reinicio de la v2.1: instalar.php --reiniciar continúa aunque otra conexión
// tenga una transacción abierta, y borra el archivo de la base. Lo que esa conexión confirma después
// va a parar a un archivo ya borrado y se pierde.
// Uso: php pruebas/reproducir_defecto_v2_1.php <ruta a prototipo_v2_1 o prototipo_v2_2>
$proto = $argv[1];
$dir = sys_get_temp_dir() . '/repro_v21_' . getmypid();
@mkdir($dir);
$ruta = "$dir/biblioteca.sqlite";
putenv("BIBLIO_DB=$ruta");
exec(escapeshellarg(PHP_BINARY) . ' ' . escapeshellarg("$proto/instalar.php") . ' --clave=x 2>&1');
$otra = new PDO("sqlite:$ruta");
$otra->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$otra->exec('BEGIN IMMEDIATE');
$otra->exec("INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (1, 1, '2026-03-02', '2026-03-09')");
echo "Otra conexión tiene un préstamo sin confirmar.\n";
exec(escapeshellarg(PHP_BINARY) . ' ' . escapeshellarg("$proto/instalar.php") . ' --reiniciar --si --clave=x 2>&1', $out, $cod);
echo 'instalar.php --reiniciar terminó con código ' . $cod . ($cod === 0 ? ' (siguió adelante)' : ' (se negó)') . "\n";
try {
    $otra->exec('COMMIT');
    echo "La otra conexión confirmó su préstamo sin error.\n";
} catch (PDOException $e) {
    echo 'La otra conexión NO pudo confirmar su préstamo: ' . $e->getMessage() . "\n";
}
$otra = null;
$n = (int) (new PDO("sqlite:$ruta"))->query('SELECT COUNT(*) FROM prestamos')->fetchColumn();
echo "Préstamos en la base después: $n" . ($n === 0 ? ' (el préstamo de la otra conexión se perdió)' : ' (el préstamo de la otra conexión se conservó)') . "\n";
exec('rm -rf ' . escapeshellarg($dir));
