<?php
// PT-06: registrar devolución (OP-02, CU-02). Zona Bibliotecaria.
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/mensajes.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/../src/reglas.php';
require __DIR__ . '/_plantilla.php';

$cuenta = exigir_zona('Bibliotecaria');
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $r = csrf_valida()
        ? registrar_devolucion(conectar(), $cuenta, $_POST['ejemplar'] ?? '', date('Y-m-d'))
        : resultado(false, 'MV-12');
    guardar_aviso($r, 'devolucion.php');
}
cabecera('Registrar devolución', 'PT-06');
aviso(tomar_aviso());
formulario_inicio();
?>
<label>Código del ejemplar devuelto <input name="ejemplar" autocomplete="off"></label>
<button>Confirmar devolución</button> <a href="inicio.php">Volver al inicio</a>
</form>
<?php pie();
