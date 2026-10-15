<?php
// Proceso auxiliar de prueba_carrera.php: espera la señal de largada e intenta un préstamo.
// Uso interno: php _trabajador.php <base> <ejemplar> <lector> <largada_en_microsegundos>
putenv('BIBLIO_DB=' . $argv[1]);
require __DIR__ . '/../src/db.php';
$pdo = conectar();
$largada = (float) $argv[4];
while (microtime(true) * 1e6 < $largada) {
    usleep(200);
}
$r = registrar_prestamo($pdo, $argv[2], $argv[3], '2026-03-02');
echo $r === null ? 'REGISTRADO' : $r;
