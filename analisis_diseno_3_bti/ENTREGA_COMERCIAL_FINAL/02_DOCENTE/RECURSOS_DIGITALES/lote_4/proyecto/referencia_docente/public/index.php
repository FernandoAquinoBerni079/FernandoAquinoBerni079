<?php
// PT-01 y PT-02: consulta pública de disponibilidad (OP-03). Sin sesión; ningún dato de lectores (RNF-03).
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/mensajes.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/../src/reglas.php';
require __DIR__ . '/_plantilla.php';

$q = isset($_GET['q']) ? (string) $_GET['q'] : null;
$r = $q === null ? null : consultar_disponibilidad(conectar(), $q);
cabecera($r ? 'Disponibilidad' : 'Buscar un título', $r ? 'PT-02' : 'PT-01');
?>
<form method="get"><label>Título o parte del título <input name="q" value="<?= e($q) ?>"></label> <button>Buscar</button></form>
<?php aviso($r); ?>
<?php if ($r && $r['filas']): ?>
<table id="disponibilidad">
<tr><th>Título</th><th>Autor</th><th>Disponibles</th></tr>
<?php foreach ($r['filas'] as $o): ?>
<tr><td><?= e($o['titulo']) ?></td><td><?= e($o['autor']) ?></td><td><?= (int) $o['disponibles'] > 0 ? e($o['disponibles']) : e(mensaje('ME-09')) ?></td></tr>
<?php endforeach; ?>
</table>
<?php endif; ?>
<?php pie();
