<?php
// PT-08: lectores y ejemplares (zona Bibliotecaria). En la base: el formulario del alta de un ejemplar (OA-01),
// que se completa en el Capítulo 10. Los demás formularios se agregan en el Capítulo 11.
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/mensajes.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/../src/reglas.php';
require __DIR__ . '/_plantilla.php';

$cuenta = exigir_zona('Bibliotecaria');
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $r = csrf_valida()
        ? alta_ejemplar(conectar(), $cuenta, (string) ($_POST['codigo'] ?? ''), (string) ($_POST['edicion'] ?? ''))
        : resultado(false, 'MV-12');
    guardar_aviso($r, 'lectores.php');
}
cabecera('Lectores y ejemplares', 'PT-08');
aviso(tomar_aviso());
?>
<h2>Alta de un ejemplar</h2>
<?php formulario_inicio('alta_ejemplar'); ?>
<label>Código del ejemplar (etiqueta) <input name="codigo" placeholder="EJ-0000"></label>
<label>Código de la edición <input name="edicion" placeholder="ED-0000"></label>
<button>Dar de alta el ejemplar</button>
</form>
<p><a href="inicio.php">Volver al inicio</a></p>
<?php pie();
