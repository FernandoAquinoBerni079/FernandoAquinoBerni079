<?php
// Catálogo público: solo consulta. No hay formularios que modifiquen datos.
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/_plantilla.php';

$pdo = conectar();
$q = isset($_GET['q']) ? trim((string) $_GET['q']) : '';
$obras = catalogo($pdo, $q);

cabecera('Biblioteca escolar — catálogo');
?>
<form method="get"><input name="q" value="<?= e($q) ?>" placeholder="Título o autor"> <button>Buscar</button></form>
<table>
<tr><th>Título</th><th>Autor</th><th>Edición</th><th>Ejemplares</th><th>Disponibles</th></tr>
<?php foreach ($obras as $o): ?>
<tr><td><?= e($o['titulo']) ?></td><td><?= e($o['autor']) ?></td><td><?= e($o['edicion']) ?></td><td><?= e($o['ejemplares']) ?></td><td><?= e($o['disponibles']) ?></td></tr>
<?php endforeach; ?>
</table>
<?php if (!$obras): ?><p>No hay resultados.</p><?php endif; ?>
<?php pie();
