<?php
// PT-01 y PT-02: consulta pública de disponibilidad (OP-03, se construye en el Capítulo 13).
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/mensajes.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/../src/reglas.php';
require __DIR__ . '/_plantilla.php';

$q = isset($_GET['q']) ? (string) $_GET['q'] : null;
$r = $q === null ? null : consultar_disponibilidad(conectar(), $q);
cabecera('Buscar un título', 'PT-01');
?>
<form method="get"><label>Título o parte del título <input name="q" value="<?= e($q) ?>"></label> <button>Buscar</button></form>
<?php aviso($r); ?>
<?php pie();
