<?php
// Pruebas de las reglas del núcleo, sin servidor web. Uso: php pruebas/prueba_reglas.php
// Cada prueba nombra la regla (RN) o el requisito de producto que comprueba.
$tmp = sys_get_temp_dir() . '/biblio_v2_reglas_' . getmypid() . '.sqlite';
@unlink($tmp);
putenv('BIBLIO_DB=' . $tmp);
require __DIR__ . '/../src/db.php';

$fallos = 0;
$n = 0;
function comprobar($desc, $cond)
{
    global $fallos, $n;
    $n++;
    if (!$cond) {
        $fallos++;
    }
    echo ($cond ? 'CORRECTO ' : 'FALLA    ') . $desc . PHP_EOL;
}
function lanza($pdo, $sql)
{
    try {
        $pdo->exec($sql);
        return false;
    } catch (PDOException $e) {
        return true;
    }
}
function contar($pdo, $sql)
{
    return (int) $pdo->query($sql)->fetchColumn();
}

$pdo = conectar();
crear_esquema($pdo);
$pdo->exec("INSERT INTO obras (titulo, autor, edicion) VALUES ('Obra A', 'Autor A', 'Ed. 1'), ('Obra B', 'Autor B', 'Ed. 1')");
$pdo->exec("INSERT INTO ejemplares (obra_id, codigo) VALUES (1, 'A-1'), (1, 'A-2'), (2, 'B-1'), (2, 'B-2')");
$pdo->exec("INSERT INTO lectores (codigo, nombre, curso, activo) VALUES ('L1', 'Uno', '3.º', 1), ('L2', 'Dos', '3.º', 1), ('L3', 'Tres', '2.º', 0)");

// Modelo
comprobar('Modelo: dos ejemplares de la misma obra se distinguen por su código', contar($pdo, "SELECT COUNT(DISTINCT codigo) FROM ejemplares WHERE obra_id = 1") === 2);
comprobar('Modelo: el código de ejemplar no se repite', lanza($pdo, "INSERT INTO ejemplares (obra_id, codigo) VALUES (1, 'A-1')"));
comprobar('Modelo: no se crea un ejemplar de una obra inexistente', lanza($pdo, "INSERT INTO ejemplares (obra_id, codigo) VALUES (99, 'Z-1')"));

// Préstamo contra un ejemplar identificable
comprobar('Préstamo válido de A-1 a L1', registrar_prestamo($pdo, 'A-1', 'L1', '2026-03-02') === null);
$p = $pdo->query("SELECT * FROM prestamos WHERE id = 1")->fetch();
comprobar('El préstamo queda vinculado al ejemplar A-1, no a la obra', $p['ejemplar_id'] == 1);
comprobar('RN-03: vence 7 días después de la salida (2026-03-09)', $p['fecha_vencimiento'] === '2026-03-09');
comprobar('A-2, otro ejemplar de la misma obra, sigue disponible', registrar_prestamo($pdo, 'A-2', 'L2', '2026-03-02') === null);

// RN-01
comprobar('RN-01: segundo préstamo de A-1 rechazado', registrar_prestamo($pdo, 'A-1', 'L2', '2026-03-03') === 'El ejemplar ya tiene un préstamo activo.');
comprobar('RN-01: la base rechaza un segundo préstamo activo aunque se salteen las reglas del código',
    lanza($pdo, "INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (1, 2, '2026-03-03', '2026-03-10')"));
comprobar('RN-01: A-1 sigue con un único préstamo activo', contar($pdo, "SELECT COUNT(*) FROM prestamos WHERE ejemplar_id = 1 AND fecha_devolucion IS NULL") === 1);

// RN-02
comprobar('RN-02: L1 recibe su segundo préstamo (B-1)', registrar_prestamo($pdo, 'B-1', 'L1', '2026-03-03') === null);
comprobar('RN-02: L1 no recibe un tercero (B-2)', registrar_prestamo($pdo, 'B-2', 'L1', '2026-03-03') === 'El lector ya tiene 2 préstamos activos.');

// RN-04 y validaciones
comprobar('RN-04: lector inactivo rechazado', registrar_prestamo($pdo, 'B-2', 'L3', '2026-03-03') === 'El lector está inactivo y no puede recibir préstamos.');
comprobar('Ejemplar inexistente rechazado', registrar_prestamo($pdo, 'X-9', 'L2', '2026-03-03') === 'El ejemplar no existe.');
comprobar('Lector inexistente rechazado', registrar_prestamo($pdo, 'B-2', 'L9', '2026-03-03') === 'El lector no existe.');
comprobar('Fecha imposible rechazada (2026-02-30)', registrar_prestamo($pdo, 'B-2', 'L2', '2026-02-30') === 'La fecha no es válida.');
comprobar('Los rechazos no dejaron préstamos a medias (hay 3)', contar($pdo, 'SELECT COUNT(*) FROM prestamos') === 3);

// Consultas
$v = prestamos_vencidos($pdo, '2026-03-10');
comprobar('Vencidos al 2026-03-10: los dos préstamos del 2026-03-02', count($v) === 2);
comprobar('Vencidos al 2026-03-09: ninguno (vencen ese día)', count(prestamos_vencidos($pdo, '2026-03-09')) === 0);
$cat = catalogo($pdo, 'Obra A');
comprobar('Catálogo: Obra A con 2 ejemplares y 0 disponibles', $cat[0]['ejemplares'] == 2 && $cat[0]['disponibles'] == 0);

// RN-05: devolución e historial
comprobar('Devolución de A-1', registrar_devolucion($pdo, 1, '2026-03-05') === null);
comprobar('RN-05: doble devolución rechazada', registrar_devolucion($pdo, 1, '2026-03-06') !== null);
comprobar('RN-05: la base impide cambiar la fecha de una devolución ya registrada',
    lanza($pdo, "UPDATE prestamos SET fecha_devolucion = '2026-03-07' WHERE id = 1"));
comprobar('RN-05: el préstamo devuelto sigue en el historial', contar($pdo, 'SELECT COUNT(*) FROM prestamos WHERE id = 1') === 1);
comprobar('RN-05: la base no permite borrar préstamos', lanza($pdo, 'DELETE FROM prestamos WHERE id = 1'));
comprobar('RN-05: la base no permite cambiar el ejemplar de un préstamo', lanza($pdo, 'UPDATE prestamos SET ejemplar_id = 2 WHERE id = 1'));
comprobar('Devolución anterior a la salida rechazada', registrar_devolucion($pdo, 2, '2026-03-01') !== null);
comprobar('A-1 vuelve a estar disponible y se presta a L2', registrar_prestamo($pdo, 'A-1', 'L2', '2026-03-06') === null);
comprobar('Historial de A-1: 2 préstamos, 1 activo', contar($pdo, 'SELECT COUNT(*) FROM prestamos WHERE ejemplar_id = 1') === 2
    && contar($pdo, 'SELECT COUNT(*) FROM prestamos WHERE ejemplar_id = 1 AND fecha_devolucion IS NULL') === 1);

// RN-06
comprobar('RN-06: no se borra un ejemplar con historial', lanza($pdo, "DELETE FROM ejemplares WHERE codigo = 'A-1'"));
comprobar('RN-06: no se borra un lector con historial', lanza($pdo, "DELETE FROM lectores WHERE codigo = 'L1'"));
comprobar('RN-06: el ejemplar se inactiva', inactivar($pdo, 'ejemplares', 'B-2') === null);
comprobar('Un ejemplar inactivo no se presta', registrar_prestamo($pdo, 'B-2', 'L2', '2026-03-06') === 'El ejemplar está dado de baja.');
comprobar('Un ejemplar inactivo no cuenta en el catálogo', catalogo($pdo, 'Obra B')[0]['ejemplares'] == 1);

// Otros
comprobar('Zona horaria de Paraguay', date_default_timezone_get() === 'America/Asuncion');
comprobar('Versión del esquema registrada (2)', contar($pdo, 'PRAGMA user_version') === 2);
$pdo->exec("INSERT INTO obras (titulo, autor, edicion) VALUES ('Ñandutí y güira', 'Autoría ñ', 'Ed.')");
comprobar('Tildes y ñ se guardan y se leen iguales', $pdo->query("SELECT titulo FROM obras WHERE autor = 'Autoría ñ'")->fetchColumn() === 'Ñandutí y güira');

$pdo = null;
@unlink($tmp);
echo PHP_EOL . "Resultado: " . ($n - $fallos) . " de $n correctas" . PHP_EOL;
exit($fallos ? 1 : 0);
