<?php
// PT-05: registrar préstamo (OP-01, CU-01). Zona Bibliotecaria.
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/mensajes.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/../src/reglas.php';
require __DIR__ . '/_plantilla.php';

$cuenta = exigir_zona('Bibliotecaria');
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $r = csrf_valida()
        ? registrar_prestamo(conectar(), $cuenta, $_POST['lector'] ?? '', $_POST['ejemplar'] ?? '', date('Y-m-d'))
        : resultado(false, 'MV-12');
    guardar_aviso($r, 'prestamo.php');
}
cabecera('Registrar préstamo', 'PT-05');
aviso(tomar_aviso());
formulario_inicio();
?>
<label>Código del lector <input name="lector" autocomplete="off"></label>
<label>Código del ejemplar <input name="ejemplar" autocomplete="off"></label>
<button>Prestar</button> <a href="inicio.php">Volver al inicio</a>
</form>
<?php pie();
