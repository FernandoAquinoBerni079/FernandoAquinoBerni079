<?php
// Préstamo, devolución y consultas de la bibliotecaria. Exige sesión con ese rol.
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/_plantilla.php';

exigir_bibliotecaria();
$pdo = conectar();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $accion = (string) ($_POST['accion'] ?? '');
    $hoy = date('Y-m-d');
    if (!csrf_valida()) {
        $r = 'El formulario venció. Recargá la página y volvé a intentar.';
    } elseif ($accion === 'prestar') {
        $ej = trim((string) ($_POST['ejemplar'] ?? ''));
        $le = trim((string) ($_POST['lector'] ?? ''));
        $r = ($ej === '' || $le === '') ? 'Elegí un ejemplar y un lector.' : registrar_prestamo($pdo, $ej, $le, $hoy);
        $ok = 'Préstamo registrado.';
    } elseif ($accion === 'devolver') {
        $id = filter_var($_POST['prestamo_id'] ?? '', FILTER_VALIDATE_INT);
        $r = $id ? registrar_devolucion($pdo, $id, $hoy) : 'Préstamo no válido.';
        $ok = 'Devolución registrada.';
    } else {
        $r = 'Operación desconocida.';
    }
    // Patrón POST-redirección-GET: recargar la página no reenvía el formulario.
    $_SESSION['aviso'] = $r === null ? array('ok', $ok) : array('error', $r);
    header('Location: operaciones.php', true, 303);
    exit;
}

$aviso = $_SESSION['aviso'] ?? null;
unset($_SESSION['aviso']);
$ref = isset($_GET['fecha']) && sumar_dias((string) $_GET['fecha'], 0) !== null ? (string) $_GET['fecha'] : date('Y-m-d');
$csrf = ficha_csrf();

cabecera('Operaciones de la bibliotecaria');
?>
<?php if ($aviso): ?><p class="<?= e($aviso[0]) ?>" id="<?= $aviso[0] === 'ok' ? 'mensaje' : 'error' ?>"><?= e($aviso[1]) ?></p><?php endif; ?>

<h2>Registrar préstamo</h2>
<form method="post">
<input type="hidden" name="csrf" value="<?= e($csrf) ?>"><input type="hidden" name="accion" value="prestar">
<select name="ejemplar"><option value="">Ejemplar disponible…</option>
<?php foreach (ejemplares_disponibles($pdo) as $x): ?><option value="<?= e($x['codigo']) ?>"><?= e($x['codigo'] . ' — ' . $x['titulo']) ?></option><?php endforeach; ?>
</select>
<select name="lector"><option value="">Lector…</option>
<?php foreach (lectores_activos($pdo) as $x): ?><option value="<?= e($x['codigo']) ?>"><?= e($x['nombre'] . ' (' . $x['curso'] . ')') ?></option><?php endforeach; ?>
</select>
<button>Prestar</button>
</form>

<h2>Préstamos activos</h2>
<table>
<tr><th>N.º</th><th>Ejemplar</th><th>Título</th><th>Lector</th><th>Salida</th><th>Vence</th><th></th></tr>
<?php foreach (prestamos_activos($pdo) as $p): ?>
<tr><td><?= e($p['id']) ?></td><td><?= e($p['codigo']) ?></td><td><?= e($p['titulo']) ?></td><td><?= e($p['nombre']) ?></td><td><?= e($p['fecha_salida']) ?></td><td><?= e($p['fecha_vencimiento']) ?></td>
<td><form method="post"><input type="hidden" name="csrf" value="<?= e($csrf) ?>"><input type="hidden" name="accion" value="devolver"><input type="hidden" name="prestamo_id" value="<?= e($p['id']) ?>"><button>Devolver</button></form></td></tr>
<?php endforeach; ?>
</table>

<h2>Vencidos al <?= e($ref) ?></h2>
<form method="get"><label>Fecha de referencia <input name="fecha" value="<?= e($ref) ?>"></label> <button>Ver</button></form>
<table id="vencidos">
<tr><th>N.º</th><th>Ejemplar</th><th>Título</th><th>Lector</th><th>Venció</th></tr>
<?php foreach (prestamos_vencidos($pdo, $ref) as $p): ?>
<tr><td><?= e($p['id']) ?></td><td><?= e($p['codigo']) ?></td><td><?= e($p['titulo']) ?></td><td><?= e($p['nombre']) ?></td><td><?= e($p['fecha_vencimiento']) ?></td></tr>
<?php endforeach; ?>
</table>
<?php pie();
