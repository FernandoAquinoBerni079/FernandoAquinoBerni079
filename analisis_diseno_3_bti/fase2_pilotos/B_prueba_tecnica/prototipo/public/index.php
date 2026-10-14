<?php
// Prototipo mínimo: catálogo con disponibilidad, préstamo y devolución.
// Se ejecuta con el servidor incorporado de PHP: php -S localhost:8000 -t public
require __DIR__ . '/../src/db.php';

function e($s)
{
    return htmlspecialchars((string) $s, ENT_QUOTES, 'UTF-8');
}

$pdo = conectar();
$mensaje = '';
$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $accion = isset($_POST['accion']) ? $_POST['accion'] : '';
    $hoy = date('Y-m-d');
    if ($accion === 'prestar') {
        $libro = filter_input(INPUT_POST, 'libro_id', FILTER_VALIDATE_INT);
        $lector = filter_input(INPUT_POST, 'lector_id', FILTER_VALIDATE_INT);
        if (!$libro || !$lector) {
            $error = 'Elegí un libro y un lector.';
        } else {
            $r = registrar_prestamo($pdo, $libro, $lector, $hoy);
            if ($r === null) {
                $mensaje = 'Préstamo registrado.';
            } else {
                $error = $r;
            }
        }
    } elseif ($accion === 'devolver') {
        $p = filter_input(INPUT_POST, 'prestamo_id', FILTER_VALIDATE_INT);
        $r = $p ? registrar_devolucion($pdo, $p, $hoy) : 'Préstamo no válido.';
        if ($r === null) {
            $mensaje = 'Devolución registrada.';
        } else {
            $error = $r;
        }
    }
}

$q = isset($_GET['q']) ? trim($_GET['q']) : '';
$st = $pdo->prepare('SELECT l.id, l.titulo, l.autor, l.ejemplares,
        l.ejemplares - (SELECT COUNT(*) FROM prestamos p WHERE p.libro_id = l.id AND p.fecha_devolucion IS NULL) AS disponibles
    FROM libros l WHERE l.titulo LIKE ? OR l.autor LIKE ? ORDER BY l.titulo');
$st->execute(array('%' . $q . '%', '%' . $q . '%'));
$libros = $st->fetchAll();
$lectores = $pdo->query('SELECT id, nombre, curso FROM lectores ORDER BY nombre')->fetchAll();
$abiertos = $pdo->query('SELECT p.id, l.titulo, r.nombre, p.fecha_salida FROM prestamos p
    JOIN libros l ON l.id = p.libro_id JOIN lectores r ON r.id = p.lector_id
    WHERE p.fecha_devolucion IS NULL ORDER BY p.id')->fetchAll();
?>
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Biblioteca escolar — prototipo</title>
<style>
body { font-family: sans-serif; max-width: 52rem; margin: 1rem auto; padding: 0 1rem; }
table { border-collapse: collapse; width: 100%; margin: .5rem 0 1rem; }
th, td { border: 1px solid #bbb; padding: .3rem .5rem; text-align: left; }
.ok { color: #1b5e20; } .error { color: #b71c1c; }
</style>
</head>
<body>
<h1>Biblioteca escolar — prototipo</h1>
<?php if ($mensaje): ?><p class="ok" id="mensaje"><?= e($mensaje) ?></p><?php endif; ?>
<?php if ($error): ?><p class="error" id="error"><?= e($error) ?></p><?php endif; ?>

<h2>Catálogo</h2>
<form method="get"><input name="q" value="<?= e($q) ?>" placeholder="Título o autor"> <button>Buscar</button></form>
<table>
<tr><th>Título</th><th>Autor</th><th>Ejemplares</th><th>Disponibles</th></tr>
<?php foreach ($libros as $l): ?>
<tr><td><?= e($l['titulo']) ?></td><td><?= e($l['autor']) ?></td><td><?= e($l['ejemplares']) ?></td><td><?= e($l['disponibles']) ?></td></tr>
<?php endforeach; ?>
</table>

<h2>Registrar préstamo</h2>
<form method="post">
<input type="hidden" name="accion" value="prestar">
<select name="libro_id"><option value="">Libro…</option>
<?php foreach ($libros as $l): ?><option value="<?= e($l['id']) ?>"><?= e($l['titulo']) ?></option><?php endforeach; ?>
</select>
<select name="lector_id"><option value="">Lector…</option>
<?php foreach ($lectores as $r): ?><option value="<?= e($r['id']) ?>"><?= e($r['nombre'] . ' (' . $r['curso'] . ')') ?></option><?php endforeach; ?>
</select>
<button>Prestar</button>
</form>

<h2>Préstamos sin devolver</h2>
<table>
<tr><th>N.º</th><th>Libro</th><th>Lector</th><th>Salida</th><th></th></tr>
<?php foreach ($abiertos as $p): ?>
<tr><td><?= e($p['id']) ?></td><td><?= e($p['titulo']) ?></td><td><?= e($p['nombre']) ?></td><td><?= e($p['fecha_salida']) ?></td>
<td><form method="post"><input type="hidden" name="accion" value="devolver"><input type="hidden" name="prestamo_id" value="<?= e($p['id']) ?>"><button>Devolver</button></form></td></tr>
<?php endforeach; ?>
</table>
</body>
</html>
