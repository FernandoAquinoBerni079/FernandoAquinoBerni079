<?php
// ¿Quién garantiza cada regla? Uso: php pruebas/prueba_garantias.php
// Se intenta violar cada regla con SQL directo, sin pasar por las funciones PHP.
// «SQLite» = la base rechaza la operación por sí sola. «Solo PHP» = la base la acepta:
// la regla vale únicamente si la operación pasa por registrar_prestamo() u otra función del núcleo.
$tmp = sys_get_temp_dir() . '/biblio_v21_garantias_' . getmypid() . '.sqlite';
@unlink($tmp);
putenv('BIBLIO_DB=' . $tmp);
require __DIR__ . '/../src/db.php';

$pdo = conectar();
crear_esquema($pdo);
$pdo->exec("INSERT INTO obras (titulo, autor, edicion) VALUES ('Obra', 'Autor', 'Ed.')");
$pdo->exec("INSERT INTO ejemplares (obra_id, codigo, activo) VALUES (1, 'E-1', 1), (1, 'E-2', 1), (1, 'E-3', 1), (1, 'E-4', 0)");
$pdo->exec("INSERT INTO lectores (codigo, nombre, curso, activo) VALUES ('L-1', 'Uno', '3.º', 1), ('L-2', 'Inactivo', '3.º', 0)");
$pdo->exec("INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento, fecha_devolucion) VALUES (1, 1, '2026-03-02', '2026-03-09', NULL), (2, 1, '2026-03-02', '2026-03-09', NULL), (3, 1, '2026-02-01', '2026-02-08', '2026-02-05')");

function intento(PDO $p, $sql)
{
    $p->exec('SAVEPOINT x');
    try {
        $p->exec($sql);
        $p->exec('ROLLBACK TO x');
        $p->exec('RELEASE x');
        return 'Solo PHP';
    } catch (PDOException $e) {
        $p->exec('ROLLBACK TO x');
        $p->exec('RELEASE x');
        return 'SQLite';
    }
}

$casos = array(
    array('RN-01', 'Segundo préstamo activo del mismo ejemplar', "INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (1, 1, '2026-03-03', '2026-03-10')", 'SQLite'),
    array('RN-02', 'Tercer préstamo activo del mismo lector', "INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (3, 1, '2026-03-03', '2026-03-10')", 'Solo PHP'),
    array('RN-03', 'Plazo distinto de 7 días', "INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (3, 1, '2026-03-03', '2026-03-30')", 'Solo PHP'),
    array('RN-04', 'Préstamo a un lector inactivo', "INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (3, 2, '2026-03-03', '2026-03-10')", 'Solo PHP'),
    array('Baja', 'Préstamo de un ejemplar dado de baja', "INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (4, 1, '2026-03-03', '2026-03-10')", 'Solo PHP'),
    array('RN-05', 'Borrar un préstamo', 'DELETE FROM prestamos WHERE id = 3', 'SQLite'),
    array('RN-05', 'Cambiar una devolución ya registrada', "UPDATE prestamos SET fecha_devolucion = '2026-02-06' WHERE id = 3", 'SQLite'),
    array('RN-05', 'Cambiar el ejemplar de un préstamo', 'UPDATE prestamos SET ejemplar_id = 3 WHERE id = 1', 'SQLite'),
    array('RN-06', 'Borrar un ejemplar con historial', 'DELETE FROM ejemplares WHERE id = 3', 'SQLite'),
    array('RN-06', 'Borrar un lector con historial', 'DELETE FROM lectores WHERE id = 1', 'SQLite'),
    array('Integridad', 'Préstamo de un ejemplar inexistente (con foreign_keys activo)', "INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (99, 1, '2026-03-03', '2026-03-10')", 'SQLite'),
    array('Integridad', 'Vencimiento anterior a la salida', "INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (3, 1, '2026-03-03', '2026-03-01')", 'SQLite'),
    array('Integridad', 'Código de ejemplar repetido', "INSERT INTO ejemplares (obra_id, codigo) VALUES (1, 'E-1')", 'SQLite'),
);

$fallos = 0;
printf("%-11s %-62s %-9s %s\n", 'Regla', 'Intento con SQL directo', 'Esperado', 'Resultado');
foreach ($casos as $c) {
    $r = intento($pdo, $c[2]);
    if ($r !== $c[3]) {
        $fallos++;
    }
    printf("%-11s %-62s %-9s %s%s\n", $c[0], $c[1], $c[3], $r, $r === $c[3] ? '' : '  <-- DISTINTO');
}

// Matiz: las claves foráneas dependen de PRAGMA foreign_keys, que activa conectar() en cada conexión.
$otra = new PDO('sqlite:' . $tmp);
$otra->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$r = intento($otra, "INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (98, 1, '2026-03-03', '2026-03-10')");
printf("%-11s %-62s %-9s %s%s\n", 'Integridad', 'Ejemplar inexistente desde una conexión SIN foreign_keys', 'Solo PHP', $r, $r === 'Solo PHP' ? '' : '  <-- DISTINTO');
if ($r !== 'Solo PHP') {
    $fallos++;
}
$otra = null;
$pdo = null;
@unlink($tmp);
echo PHP_EOL . 'Resultado: ' . (count($casos) + 1 - $fallos) . ' de ' . (count($casos) + 1) . ' clasificaciones confirmadas' . PHP_EOL;
exit($fallos ? 1 : 0);
