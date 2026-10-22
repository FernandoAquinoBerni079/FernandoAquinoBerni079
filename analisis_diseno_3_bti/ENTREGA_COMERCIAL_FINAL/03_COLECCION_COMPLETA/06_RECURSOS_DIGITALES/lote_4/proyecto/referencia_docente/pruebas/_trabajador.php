<?php
// Proceso auxiliar de prueba_carrera.php: abre SU PROPIA conexión, espera la señal de largada e intenta un préstamo.
// Uso interno: php _trabajador.php <base> <lector> <ejemplar> <largada_en_microsegundos>
putenv('BIBLIO_DB=' . $argv[1]);
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/mensajes.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/../src/reglas.php';
$pdo = conectar();
$largada = (float) $argv[4];
while (microtime(true) * 1e6 < $largada) {
    usleep(200);
}
$r = registrar_prestamo($pdo, array('id' => 1, 'usuario' => 'bibliotecaria1', 'rol' => 'bibliotecaria'), $argv[2], $argv[3], '2026-03-02');
echo $r['codigo'];
