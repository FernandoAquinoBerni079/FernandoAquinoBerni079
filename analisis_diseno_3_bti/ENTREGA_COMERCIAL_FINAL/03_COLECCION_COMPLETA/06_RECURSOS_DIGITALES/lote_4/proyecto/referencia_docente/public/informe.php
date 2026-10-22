<?php
// PT-09: informe mensual por curso (OP-05). Zona «Bibliotecaria o dirección»: el servidor comprueba el rol.
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/mensajes.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/../src/reglas.php';
require __DIR__ . '/_plantilla.php';

$cuenta = exigir_zona('Bibliotecaria o dirección');
$mes = isset($_GET['mes']) ? (string) $_GET['mes'] : date('Y-m');
$r = informe_mensual(conectar(), $cuenta, $mes);
cabecera('Informe mensual por curso', 'PT-09');
?>
<form method="get"><label>Mes (año-mes) <input name="mes" value="<?= e($mes) ?>"></label> <button>Ver informe</button></form>
<?php aviso($r); ?>
<?php if ($r['ok']): ?>
<table id="informe">
<tr><th>Grupo</th><th>Préstamos</th></tr>
<?php foreach ($r['filas'] as $f): ?>
<tr><td><?= e($f['grupo']) ?></td><td><?= e($f['prestamos']) ?></td></tr>
<?php endforeach; ?>
<tr><th>Total (contado de nuevo)</th><th><?= e($r['total']) ?></th></tr>
</table>
<?php endif; ?>
<?php pie();
