<?php
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/_plantilla.php';

$error = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!csrf_valida()) {
        $error = 'El formulario venció. Volvé a intentar.';
    } elseif (ingresar(conectar(), (string) ($_POST['usuario'] ?? ''), (string) ($_POST['clave'] ?? ''))) {
        header('Location: operaciones.php', true, 303);
        exit;
    } else {
        $error = 'Usuario o clave incorrectos.';
    }
}
cabecera('Ingresar');
?>
<?php if ($error): ?><p class="error" id="error"><?= e($error) ?></p><?php endif; ?>
<form method="post">
<input type="hidden" name="csrf" value="<?= e(ficha_csrf()) ?>">
<p><label>Usuario <input name="usuario" autocomplete="username"></label></p>
<p><label>Clave <input name="clave" type="password" autocomplete="current-password"></label></p>
<button>Ingresar</button>
</form>
<?php pie();
