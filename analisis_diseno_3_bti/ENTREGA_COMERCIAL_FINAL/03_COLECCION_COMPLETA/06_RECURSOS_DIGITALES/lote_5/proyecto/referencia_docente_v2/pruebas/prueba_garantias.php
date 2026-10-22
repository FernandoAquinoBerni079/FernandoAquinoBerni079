<?php
// ¿Quién garantiza cada regla? Uso: php pruebas/prueba_garantias.php   (adaptada del Piloto B v2.3)
// Se intenta violar cada restricción del Capítulo 7 con SQL directo, sin pasar por src/reglas.php.
// «SQLite» = la base la rechaza por sí sola. «Solo PHP» = la base la acepta: la regla vale únicamente si la
// operación pasa por las reglas de negocio. Por eso las reglas se comprueban siempre en el servidor (Capítulo 9).
require __DIR__ . '/_comun.php';
list($dir, $ruta) = base_de_prueba('garantias');
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/datos_ejemplo.php';

$pdo = conectar();
$pdo->exec('BEGIN');
crear_esquema($pdo);
sembrar_ejemplo($pdo, 'prueba-solo-local');
$pdo->exec('COMMIT');
// Ejemplares 1 y 2 prestados al lector 1 (estudiante, máximo 2); el ejemplar 4 ya devuelto.
$pdo->exec("INSERT INTO prestamos (ejemplar_id, lector_id, curso_al_prestar, fecha_salida, fecha_vencimiento, fecha_devolucion) VALUES
    (1, 1, '2.º BTI', '2026-03-02', '2026-03-09', NULL), (2, 1, '2.º BTI', '2026-03-02', '2026-03-09', NULL), (4, 1, '2.º BTI', '2026-02-01', '2026-02-08', '2026-02-05')");

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
$ins = "INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES ";
$casos = array(
    array('RI-01', 'Segundo préstamo activo del mismo ejemplar', $ins . "(1, 2, '2026-03-03', '2026-03-10')", 'SQLite'),
    array('RI-02', 'Tercer préstamo activo de un estudiante', $ins . "(4, 1, '2026-03-03', '2026-03-10')", 'Solo PHP'),
    array('RI-03', 'Préstamo a un lector inactivo', $ins . "(4, 3, '2026-03-03', '2026-03-10')", 'Solo PHP'),
    array('RI-03', 'Préstamo de un ejemplar dado de baja', $ins . "(3, 2, '2026-03-03', '2026-03-10')", 'Solo PHP'),
    array('RI-04', 'Borrar un préstamo', 'DELETE FROM prestamos WHERE id = 3', 'SQLite'),
    array('RI-04', 'Cambiar una devolución ya registrada', "UPDATE prestamos SET fecha_devolucion = '2026-02-06' WHERE id = 3", 'SQLite'),
    array('RI-05', 'Borrar un ejemplar con historial', 'DELETE FROM ejemplares WHERE id = 4', 'SQLite'),
    array('RI-05', 'Borrar un lector con historial', 'DELETE FROM lectores WHERE id = 1', 'SQLite'),
    array('RI-05', 'Cambiar el código de un ejemplar con historial', "UPDATE ejemplares SET codigo = 'EJ-0999' WHERE id = 1", 'SQLite'),
    array('RI-06', 'Estudiante sin curso', "INSERT INTO lectores (codigo, nombre, tipo) VALUES ('LE-0900', 'X', 'estudiante')", 'SQLite'),
    array('RI-06', 'Docente con curso', "INSERT INTO lectores (codigo, nombre, tipo, curso) VALUES ('LE-0901', 'X', 'docente', '3.º')", 'SQLite'),
    array('RI-07', 'Vencimiento con un plazo distinto del vigente', $ins . "(5, 2, '2026-03-03', '2026-03-30')", 'Solo PHP'),
    array('RI-07', 'Cambiar el vencimiento de un préstamo registrado', "UPDATE prestamos SET fecha_vencimiento = '2026-04-30' WHERE id = 1", 'SQLite'),
    array('RI-08', 'Préstamo de un estudiante sin el curso del día', $ins . "(5, 2, '2026-03-03', '2026-03-10')", 'Solo PHP'),
    array('Integridad', 'Préstamo de un ejemplar inexistente (con foreign_keys activo)', $ins . "(99, 1, '2026-03-03', '2026-03-10')", 'SQLite'),
    array('Integridad', 'Vencimiento anterior a la salida', $ins . "(5, 2, '2026-03-03', '2026-03-01')", 'SQLite'),
    array('Integridad', 'Código de ejemplar repetido', "INSERT INTO ejemplares (codigo, edicion_id) VALUES ('EJ-0457', 1)", 'SQLite'),
    array('Integridad', 'Código de ejemplar con otro formato', "INSERT INTO ejemplares (codigo, edicion_id) VALUES ('457', 1)", 'SQLite'),
    array('RNF-02', 'Cuenta con un rol que no existe', "INSERT INTO cuentas (usuario, clave_hash, rol) VALUES ('x', 'x', 'voluntario')", 'SQLite'),
);
$fallos = 0;
$n = 0;
printf("%-11s %-60s %-9s %s\n", 'Regla', 'Intento con SQL directo', 'Esperado', 'Resultado');
foreach ($casos as $c) {
    $r = intento($pdo, $c[2]);
    $n++;
    if ($r !== $c[3]) {
        $fallos++;
    }
    printf("%-11s %-60s %-9s %s%s\n", $c[0], $c[1], $c[3], $r, $r === $c[3] ? '' : '  <-- DISTINTO');
}
// Matiz: las claves foráneas dependen de PRAGMA foreign_keys, que activa conectar() en cada conexión.
$otra = new PDO('sqlite:' . $ruta);
$otra->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$r = intento($otra, $ins . "(98, 1, '2026-03-03', '2026-03-10')");
$n++;
if ($r !== 'Solo PHP') {
    $fallos++;
}
printf("%-11s %-60s %-9s %s\n", 'Integridad', 'Ejemplar inexistente desde una conexión SIN foreign_keys', 'Solo PHP', $r);
$otra = null;
cerrar_conexion();
exec('rm -rf ' . escapeshellarg($dir));
echo PHP_EOL . 'Resultado: ' . ($n - $fallos) . " de $n clasificaciones confirmadas" . PHP_EOL;
exit($fallos ? 1 : 0);
