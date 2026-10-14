<?php
// Crea la base y carga datos de ejemplo. Uso: php instalar.php
// Si la base ya existe, la borra y la vuelve a crear (solo para el prototipo).
require __DIR__ . '/src/db.php';

$ruta = ruta_base();
if (file_exists($ruta)) {
    unlink($ruta);
}
$pdo = conectar();
crear_esquema($pdo);

$libros = array(
    array('Cuentos de la selva', 'Horacio Quiroga', 2),
    array('El hombre que calculaba', 'Malba Tahan', 1),
    array('Platero y yo', 'Juan Ramón Jiménez', 3),
    array('Manual de primeros auxilios escolares', 'Equipo editorial (ficticio)', 1),
);
$st = $pdo->prepare('INSERT INTO libros (titulo, autor, ejemplares) VALUES (?, ?, ?)');
foreach ($libros as $l) {
    $st->execute($l);
}
$lectores = array(
    array('Rocío Giménez', '3.º BTI'),
    array('Tobías Acosta', '1.º BC'),
    array('Prof. Nilda Cáceres', 'Docente'),
);
$st = $pdo->prepare('INSERT INTO lectores (nombre, curso) VALUES (?, ?)');
foreach ($lectores as $l) {
    $st->execute($l);
}
echo "Base creada en: " . realpath($ruta) . PHP_EOL;
echo "Libros: " . count($libros) . " · Lectores: " . count($lectores) . PHP_EOL;
