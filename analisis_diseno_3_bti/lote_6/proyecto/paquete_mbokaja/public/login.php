<?php
// PT-03: ingreso del personal. Si falla, ME-12 (autenticación). La bibliotecaria va a PT-04; la dirección, a PT-09.
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/mensajes.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/_plantilla.php';

$r = null;
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!csrf_valida()) {
        $r = resultado(false, 'MV-12');
    } else {
        $error = ingresar(conectar(), (string) ($_POST['usuario'] ?? ''), (string) ($_POST['clave'] ?? ''));
        if ($error === null) {
            header('Location: ' . (cuenta_actual()['rol'] === 'direccion' ? 'informe.php' : 'inicio.php'), true, 303);
            exit;
        }
        $r = resultado(false, 'ME-12');
    }
}
cabecera('Ingreso del personal', 'PT-03');
aviso($r);
formulario_inicio();
?>
<label>Usuario <input name="usuario" autocomplete="username"></label>
<label>Contraseña <input name="clave" type="password" autocomplete="current-password"></label>
<button>Ingresar</button>
</form>
<?php pie();
