<?php
// Pruebas de las reglas del núcleo, sin servidor web. Uso: php pruebas/prueba_reglas.php
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

$tmp = sys_get_temp_dir() . '/biblio_prueba_' . getmypid() . '.sqlite';
putenv('BIBLIO_DB=' . $tmp);
@unlink($tmp);
$pdo = conectar();
crear_esquema($pdo);
$pdo->exec("INSERT INTO libros (titulo, autor, ejemplares) VALUES ('Libro A', 'Autor A', 1), ('Libro B', 'Autor B', 2)");
$pdo->exec("INSERT INTO lectores (nombre, curso) VALUES ('Lector 1', '3.º'), ('Lector 2', '2.º')");

comprobar('Libro A empieza con 1 disponible', disponibles($pdo, 1) === 1);
comprobar('Préstamo válido se registra', registrar_prestamo($pdo, 1, 1, '2026-10-14') === null);
comprobar('Libro A queda con 0 disponibles', disponibles($pdo, 1) === 0);
comprobar('Segundo préstamo de Libro A se rechaza', registrar_prestamo($pdo, 1, 2, '2026-10-14') !== null);
comprobar('El rechazo no deja filas a medias', (int) $pdo->query('SELECT COUNT(*) FROM prestamos')->fetchColumn() === 1);
comprobar('Libro inexistente se rechaza', registrar_prestamo($pdo, 99, 1, '2026-10-14') === 'El libro no existe.');
comprobar('Lector inexistente se rechaza', registrar_prestamo($pdo, 2, 99, '2026-10-14') === 'El lector no existe.');
comprobar('Devolución válida se registra', registrar_devolucion($pdo, 1, '2026-10-15') === null);
comprobar('Libro A vuelve a 1 disponible', disponibles($pdo, 1) === 1);
comprobar('Doble devolución se rechaza', registrar_devolucion($pdo, 1, '2026-10-15') !== null);
$fk = false;
try {
    $pdo->exec("INSERT INTO prestamos (libro_id, lector_id, fecha_salida) VALUES (50, 50, '2026-10-14')");
} catch (PDOException $e) {
    $fk = true;
}
comprobar('La base rechaza un préstamo con claves inexistentes (foreign_keys activo)', $fk);
$chk = false;
try {
    $pdo->exec("INSERT INTO libros (titulo, autor, ejemplares) VALUES ('X', 'Y', -1)");
} catch (PDOException $e) {
    $chk = true;
}
comprobar('La base rechaza ejemplares negativos (CHECK)', $chk);
$pdo->exec("INSERT INTO libros (titulo, autor, ejemplares) VALUES ('Ñandutí y güira: acentos', 'Autoría ñ', 1)");
$t = $pdo->query("SELECT titulo FROM libros WHERE autor = 'Autoría ñ'")->fetchColumn();
comprobar('Los textos con tildes y ñ se guardan y se leen iguales', $t === 'Ñandutí y güira: acentos');

comprobar('La zona horaria es la de Paraguay', date_default_timezone_get() === 'America/Asuncion');

@unlink($tmp);

// La carpeta del proyecto puede tener espacios y tildes (por ejemplo, «Mis documentos»).
$dir = sys_get_temp_dir() . '/Análisis y Diseño ' . getmypid();
@mkdir($dir);
$ruta = $dir . '/biblioteca.sqlite';
$otra = new PDO('sqlite:' . $ruta);
$otra->exec('CREATE TABLE t (x INTEGER)');
$otra = null;
comprobar('La base se crea en una carpeta con espacios y tildes', file_exists($ruta));
@unlink($ruta);
@rmdir($dir);

echo PHP_EOL . "Resultado: " . ($n - $fallos) . " de $n correctas" . PHP_EOL;
exit($fallos ? 1 : 0);
