<?php
// PT-07: préstamos activos y vencidos (OP-04), con fecha de referencia explícita. Zona Bibliotecaria.
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/mensajes.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/../src/reglas.php';
require __DIR__ . '/_plantilla.php';

$cuenta = exigir_zona('Bibliotecaria');
$ref = isset($_GET['fecha']) ? (string) $_GET['fecha'] : date('Y-m-d');
$r = listar_prestamos_activos(conectar(), $cuenta, $ref);
cabecera('Préstamos activos y vencidos', 'PT-07');
?>
<form method="get"><label>Fecha de referencia <input name="fecha" value="<?= e($ref) ?>"></label> <button>Ver</button></form>
<?php aviso($r); ?>
<?php if ($r['filas']): ?>
<table id="activos">
<tr><th>Ejemplar</th><th>Título</th><th>Lector</th><th>Salida</th><th>Vence</th><th>Estado al <?= e($ref) ?></th></tr>
<?php foreach ($r['filas'] as $p): ?>
<tr><td><?= e($p['ejemplar']) ?></td><td><?= e($p['titulo']) ?></td><td><?= e($p['lector'] . ' ' . $p['nombre']) ?></td><td><?= e($p['fecha_salida']) ?></td><td><?= e($p['fecha_vencimiento']) ?></td><td><?= $p['vencido'] ? 'Vencido' : 'En plazo' ?></td></tr>
<?php endforeach; ?>
</table>
<?php endif; ?>
<p><a href="inicio.php">Volver al inicio</a></p>
<?php pie();
