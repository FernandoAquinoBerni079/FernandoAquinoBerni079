<?php
// PT-08: lectores y ejemplares. Zona Bibliotecaria.
// Alta de ejemplar (OA-01, Capítulo 10); obra y edición (OA-02), alta y corrección de lectores (OA-03, OA-04)
// corrección de una obra (OA-05) e inactivación (OP-06), Capítulo 11.
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/mensajes.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/../src/reglas.php';
require __DIR__ . '/_plantilla.php';

$cuenta = exigir_zona('Bibliotecaria');
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $pdo = conectar();
    $v = function ($k) {
        return (string) ($_POST[$k] ?? '');
    };
    $accion = $v('accion');
    if (!csrf_valida()) {
        $r = resultado(false, 'MV-12');
    } elseif ($accion === 'alta_ejemplar') {
        $r = alta_ejemplar($pdo, $cuenta, $v('codigo'), $v('edicion'));
    } elseif ($accion === 'alta_obra') {
        $r = alta_obra_edicion($pdo, $cuenta, $v('obra'), $v('titulo'), $v('autor'), $v('edicion'), $v('editorial'));
    } elseif ($accion === 'editar_obra') {
        $r = editar_obra($pdo, $cuenta, $v('obra'), $v('titulo'), $v('autor'));
    } elseif ($accion === 'alta_lector') {
        $r = alta_lector($pdo, $cuenta, $v('codigo'), $v('nombre'), $v('tipo'), $v('curso'));
    } elseif ($accion === 'editar_lector') {
        $r = editar_lector($pdo, $cuenta, $v('codigo'), $v('nombre'), $v('curso'));
    } elseif ($accion === 'inactivar') {
        $r = inactivar($pdo, $cuenta, $v('que'), $v('codigo'));
    } else {
        $r = resultado(false, 'MV-01', 'la operación');
    }
    guardar_aviso($r, 'lectores.php', $_POST);
}
cabecera('Lectores y ejemplares', 'PT-08');
aviso(tomar_aviso());
$previo = tomar_entradas('alta_lector');   // v2 (IN-02)
?>
<h2>Alta de un ejemplar</h2>
<?php formulario_inicio('alta_ejemplar'); ?>
<label>Código del ejemplar (etiqueta) <input name="codigo" placeholder="EJ-0000"></label>
<label>Código de la edición <input name="edicion" placeholder="ED-0000"></label>
<button>Dar de alta el ejemplar</button>
</form>

<h2>Obra y edición</h2>
<?php formulario_inicio('alta_obra'); ?>
<label>Código de la obra <input name="obra" placeholder="OB-0000"></label>
<label>Título (si la obra es nueva) <input name="titulo"></label>
<label>Autor (si la obra es nueva) <input name="autor"></label>
<label>Código de la edición <input name="edicion" placeholder="ED-0000"></label>
<label>Editorial y año <input name="editorial"></label>
<button>Registrar la edición</button>
</form>

<h2>Corregir el título o el autor de una obra</h2>
<?php formulario_inicio('editar_obra'); ?>
<label>Código de la obra <input name="obra" placeholder="OB-0000"></label>
<label>Título <input name="titulo"></label>
<label>Autor <input name="autor"></label>
<button>Guardar los cambios</button>
</form>

<h2>Alta de un lector</h2>
<?php formulario_inicio('alta_lector'); ?>
<label>Código del lector
<input name="codigo" placeholder="LE-0000"
    value="<?= valor($previo, 'codigo') ?>"></label>
<label>Nombre <input name="nombre" value="<?= valor($previo, 'nombre') ?>"></label>
<label>Tipo <select name="tipo">
<option value="estudiante"<?= elegido($previo, 'tipo', 'estudiante') ?>>Estudiante</option>
<option value="docente"<?= elegido($previo, 'tipo', 'docente') ?>>Docente</option>
</select></label>
<label>Curso (solo estudiantes)
<input name="curso" value="<?= valor($previo, 'curso') ?>"></label>
<button>Registrar el lector</button>
</form>

<h2>Corregir los datos de un lector</h2>
<?php formulario_inicio('editar_lector'); ?>
<label>Código del lector <input name="codigo" placeholder="LE-0000"></label>
<label>Nombre <input name="nombre"></label>
<label>Curso (solo estudiantes) <input name="curso"></label>
<button>Guardar los cambios</button>
</form>

<h2>Inactivar un lector o un ejemplar</h2>
<?php formulario_inicio('inactivar'); ?>
<label>Qué <select name="que"><option value="lector">Lector</option><option value="ejemplar">Ejemplar</option></select></label>
<label>Código <input name="codigo"></label>
<button>Inactivar</button>
</form>
<p><a href="inicio.php">Volver al inicio</a></p>
<?php pie();
