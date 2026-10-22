<?php
// Contratos de las operaciones, sin servidor web. Uso: php pruebas/prueba_contratos.php
// Cada comprobación nombra la prueba prevista (P-xx, Capítulo 6) o la de una operación auxiliar (PA-xx)
// y el mensaje que espera (ME, MA o MV). Las fechas son fijas para que el resultado se pueda repetir.
require __DIR__ . '/_comun.php';
list($dir, $ruta) = base_de_prueba('contratos');
require __DIR__ . '/../src/db.php';
require __DIR__ . '/../src/mensajes.php';
require __DIR__ . '/../src/auth.php';
require __DIR__ . '/../src/reglas.php';
require __DIR__ . '/../src/datos_ejemplo.php';
$fallos = 0;
$n = 0;

$pdo = conectar();
$pdo->exec('BEGIN');
crear_esquema($pdo);
sembrar_ejemplo($pdo, 'prueba-solo-local');
$pdo->exec('COMMIT');
$bib = cuenta('bibliotecaria');
$dir_ = cuenta('direccion');
$codigo = function ($r) {
    return $r['codigo'];
};

// Rechazo sin cambios: la operación devuelve el código esperado y la base queda idéntica.
function rechaza($desc, $f, $esperado)
{
    global $pdo;
    $antes = huella($pdo);
    $r = $f();
    comprobar("$desc → $esperado y sin cambios", $r['codigo'] === $esperado && !$r['ok'] && huella($pdo) === $antes);
    return $r;
}

echo "-- OA-01 dar de alta un ejemplar (Capítulo 10)\n";
$r = alta_ejemplar($pdo, $bib, 'ej-0800', ' ED-0060 ');
comprobar('PA-01: alta de EJ-0800 en ED-0060 → MA-01', $r['ok'] && $r['codigo'] === 'MA-01');
// Evidencia de persistencia: se cierra la conexión y se abre otra, como al reiniciar.
cerrar_conexion();
$otra = new PDO('sqlite:' . $ruta);
$n_ej = $otra->query("SELECT COUNT(*) FROM ejemplares
    WHERE codigo = 'EJ-0800' AND activo = 1")->fetchColumn();
comprobar('PA-01: el ejemplar sigue al abrir la base con otra conexión', $n_ej == 1);
$otra = null;
$pdo = conectar();
rechaza('PA-01: código repetido', function () use ($pdo, $bib) { return alta_ejemplar($pdo, $bib, 'EJ-0800', 'ED-0060'); }, 'MA-02');
rechaza('PA-01: formato inválido (EJ-80)', function () use ($pdo, $bib) { return alta_ejemplar($pdo, $bib, 'EJ-80', 'ED-0060'); }, 'MV-02');
rechaza('PA-01: edición inexistente', function () use ($pdo, $bib) { return alta_ejemplar($pdo, $bib, 'EJ-0801', 'ED-9999'); }, 'MA-03');
rechaza('PA-01: falta el código', function () use ($pdo, $bib) { return alta_ejemplar($pdo, $bib, '  ', 'ED-0060'); }, 'MV-01');
rechaza('PA-01: cuenta de dirección', function () use ($pdo, $dir_) { return alta_ejemplar($pdo, $dir_, 'EJ-0801', 'ED-0060'); }, 'ME-13');
rechaza('PA-01: sin sesión', function () use ($pdo) { return alta_ejemplar($pdo, null, 'EJ-0801', 'ED-0060'); }, 'ME-13');
$r = alta_ejemplar($pdo, $bib, "EJ-0802'; DROP TABLE ejemplares; --", 'ED-0060');
comprobar('PA-01: una entrada con comillas no altera la consulta (MV-02 y la tabla sigue)', $r['codigo'] === 'MV-02'
    && contar($pdo, 'SELECT COUNT(*) FROM ejemplares') === 7);

echo "-- OA-02, OA-03, OA-04 y OP-06 (Capítulo 11)\n";
$r = alta_obra_edicion($pdo, $bib, 'OB-0050', 'Leyendas del caso', 'Autora del caso (ficticia)', 'ED-0080', 'Editorial del caso, 2024');
comprobar('PA-02: obra y edición nuevas → MA-04', $r['codigo'] === 'MA-04');
$r = alta_obra_edicion($pdo, $bib, 'OB-0031', '', '', 'ED-0081', 'Edición donada, 2025');
comprobar('PA-02: edición nueva de una obra existente, sin repetir título y autor → MA-04', $r['codigo'] === 'MA-04'
    && contar($pdo, "SELECT COUNT(*) FROM ediciones d JOIN obras o ON o.id = d.obra_id WHERE o.codigo = 'OB-0031'") === 3);
rechaza('PA-02: código de edición repetido', function () use ($pdo, $bib) { return alta_obra_edicion($pdo, $bib, 'OB-0051', 'Otra', 'Otro', 'ED-0080', ''); }, 'MA-05');
rechaza('PA-02: obra nueva sin título', function () use ($pdo, $bib) { return alta_obra_edicion($pdo, $bib, 'OB-0052', '', 'Autor', 'ED-0082', ''); }, 'MV-01');
$r = alta_lector($pdo, $bib, 'LE-0300', 'Estudiante E (ficticio)', 'estudiante', '1.º BTI');
comprobar('PA-03: alta de un estudiante con curso → MA-06', $r['codigo'] === 'MA-06');
$r = alta_lector($pdo, $bib, 'LE-0301', 'Docente F (ficticio)', 'docente', '');
comprobar('PA-03: alta de un docente sin curso → MA-06', $r['codigo'] === 'MA-06');
rechaza('PA-03: estudiante sin curso (RI-06)', function () use ($pdo, $bib) { return alta_lector($pdo, $bib, 'LE-0302', 'Estudiante G', 'estudiante', ''); }, 'MV-03');
rechaza('PA-03: docente con curso (RI-06)', function () use ($pdo, $bib) { return alta_lector($pdo, $bib, 'LE-0302', 'Docente H', 'docente', '3.º BTI'); }, 'MV-04');
rechaza('PA-03: código de lector repetido', function () use ($pdo, $bib) { return alta_lector($pdo, $bib, 'LE-0300', 'Otro', 'estudiante', '1.º BTI'); }, 'MA-05');
rechaza('PA-03: tipo de lector desconocido', function () use ($pdo, $bib) { return alta_lector($pdo, $bib, 'LE-0302', 'Otro', 'visitante', ''); }, 'MV-01');
rechaza('PA-03: cuenta de dirección', function () use ($pdo, $dir_) { return alta_lector($pdo, $dir_, 'LE-0302', 'Otro', 'estudiante', '1.º BTI'); }, 'ME-13');
$directo = function ($sql) use ($pdo) {
    try {
        $pdo->exec($sql);
        return false;
    } catch (PDOException $e) {
        return true;
    }
};
comprobar('RI-06 en la base: un estudiante sin curso se rechaza aunque se saltee la función',
    $directo("INSERT INTO lectores (codigo, nombre, tipo, curso) VALUES ('LE-0303', 'X', 'estudiante', NULL)"));
comprobar('RI-06 en la base: un docente con curso también se rechaza',
    $directo("INSERT INTO lectores (codigo, nombre, tipo, curso) VALUES ('LE-0304', 'X', 'docente', '3.º')"));

echo "-- OP-01 registrar préstamo (Capítulo 12)\n";
$r = registrar_prestamo($pdo, $bib, 'LE-0123', 'EJ-0457', '2026-03-05');
comprobar('P-01: préstamo válido de EJ-0457 a LE-0123 → ME-04', $r['ok'] && $r['codigo'] === 'ME-04');
comprobar('P-02 y RI-07: con el plazo de 7 días, vence el 12/03 y el mensaje lo dice', $r['texto'] === 'Préstamo registrado. Vence el 12/03.'
    && contar($pdo, "SELECT COUNT(*) FROM prestamos WHERE fecha_vencimiento = '2026-03-12'") === 1);
comprobar('RI-08: el préstamo guarda el curso del estudiante ese día (2.º BTI)',
    $pdo->query('SELECT curso_al_prestar FROM prestamos WHERE id = 1')->fetchColumn() === '2.º BTI');
$r = rechaza('P-07: segunda solicitud sobre EJ-0457', function () use ($pdo, $bib) { return registrar_prestamo($pdo, $bib, 'LE-0124', 'EJ-0457', '2026-03-05'); }, 'ME-03');
comprobar('P-07: el mensaje es el de la Tabla 8.6 (ME-03), con el ejemplar y su vencimiento', $r['texto'] === 'No se puede prestar: el ejemplar EJ-0457 ya está prestado y vence el 12/03. Elegí otro ejemplar disponible.');
comprobar('P-07: segunda barrera de RI-01: la base rechaza un segundo préstamo activo con SQL directo',
    $directo("INSERT INTO prestamos (ejemplar_id, lector_id, fecha_salida, fecha_vencimiento) VALUES (1, 2, '2026-03-05', '2026-03-12')"));
comprobar('P-07: EJ-0457 sigue con un solo préstamo activo', contar($pdo, 'SELECT COUNT(*) FROM prestamos WHERE ejemplar_id = 1 AND fecha_devolucion IS NULL') === 1);
comprobar('P-06a: el estudiante recibe su segundo préstamo', registrar_prestamo($pdo, $bib, 'LE-0123', 'EJ-0458', '2026-03-05')['codigo'] === 'ME-04');
$r = rechaza('P-06a: un tercer préstamo del estudiante', function () use ($pdo, $bib) { return registrar_prestamo($pdo, $bib, 'LE-0123', 'EJ-0512', '2026-03-05'); }, 'ME-02');
comprobar('P-06a: ME-02 con el máximo de los estudiantes, leído de Parámetro', $r['texto'] === 'No se puede prestar: el lector ya tiene 2 préstamos activos, el máximo para estudiantes. Tiene que devolver uno antes.');
for ($i = 0; $i < 5; $i++) {
    alta_ejemplar($pdo, $bib, sprintf('EJ-09%02d', $i), 'ED-0060');
    registrar_prestamo($pdo, $bib, 'LE-0201', sprintf('EJ-09%02d', $i), '2026-03-05');
}
comprobar('P-06b: la docente tiene cinco préstamos activos', contar($pdo, "SELECT COUNT(*) FROM prestamos p JOIN lectores l ON l.id = p.lector_id WHERE l.codigo = 'LE-0201' AND p.fecha_devolucion IS NULL") === 5);
$r = rechaza('P-06b: un sexto préstamo de la docente', function () use ($pdo, $bib) { return registrar_prestamo($pdo, $bib, 'LE-0201', 'EJ-0512', '2026-03-05'); }, 'ME-02');
comprobar('P-06b: ME-02 dice el máximo de los docentes (5)', strpos($r['texto'], '5 préstamos activos, el máximo para docentes') !== false);
comprobar('RI-08: el préstamo de una docente no guarda curso', contar($pdo, "SELECT COUNT(*) FROM prestamos p JOIN lectores l ON l.id = p.lector_id WHERE l.codigo = 'LE-0201' AND p.curso_al_prestar IS NOT NULL") === 0);
rechaza('P-05: lector inactivo (LE-0125)', function () use ($pdo, $bib) { return registrar_prestamo($pdo, $bib, 'LE-0125', 'EJ-0512', '2026-03-05'); }, 'ME-01');
rechaza('OP-01: ejemplar inexistente', function () use ($pdo, $bib) { return registrar_prestamo($pdo, $bib, 'LE-0124', 'EJ-9999', '2026-03-05'); }, 'ME-05');
rechaza('OP-01: ejemplar dado de baja (EJ-0459, RI-03)', function () use ($pdo, $bib) { return registrar_prestamo($pdo, $bib, 'LE-0124', 'EJ-0459', '2026-03-05'); }, 'MV-06');
rechaza('OP-01: lector inexistente', function () use ($pdo, $bib) { return registrar_prestamo($pdo, $bib, 'LE-9999', 'EJ-0512', '2026-03-05'); }, 'MV-05');
rechaza('OP-01: fecha imposible (2026-02-30)', function () use ($pdo, $bib) { return registrar_prestamo($pdo, $bib, 'LE-0124', 'EJ-0512', '2026-02-30'); }, 'MV-08');
rechaza('P-11: préstamo sin sesión', function () use ($pdo) { return registrar_prestamo($pdo, null, 'LE-0124', 'EJ-0512', '2026-03-05'); }, 'ME-13');
rechaza('P-11: préstamo con la cuenta de dirección', function () use ($pdo, $dir_) { return registrar_prestamo($pdo, $dir_, 'LE-0124', 'EJ-0512', '2026-03-05'); }, 'ME-13');
$pdo->exec("UPDATE parametros SET valor = 10 WHERE nombre = 'plazo_dias'");
$r = registrar_prestamo($pdo, $bib, 'LE-0124', 'EJ-0512', '2026-04-01');
comprobar('RI-07: con el plazo cambiado a 10 días, el préstamo nuevo vence el 11/04', $r['texto'] === 'Préstamo registrado. Vence el 11/04.');
comprobar('RI-07: el préstamo de marzo conserva su vencimiento del 12/03', $pdo->query('SELECT fecha_vencimiento FROM prestamos WHERE id = 1')->fetchColumn() === '2026-03-12');
$pdo->exec("UPDATE parametros SET valor = 7 WHERE nombre = 'plazo_dias'");

echo "-- OP-02 registrar devolución (Capítulo 12)\n";
$r = registrar_devolucion($pdo, $bib, 'EJ-0457', '2026-03-09');
comprobar('P-03: devolución de EJ-0457 → ME-07', $r['ok'] && $r['codigo'] === 'ME-07');
comprobar('P-03 y RI-04: el préstamo sigue en el historial, con su fecha de devolución', contar($pdo, "SELECT COUNT(*) FROM prestamos WHERE id = 1 AND fecha_devolucion = '2026-03-09'") === 1);
rechaza('OP-02: segunda devolución del mismo ejemplar', function () use ($pdo, $bib) { return registrar_devolucion($pdo, $bib, 'EJ-0457', '2026-03-10'); }, 'ME-06');
rechaza('OP-02: ejemplar inexistente', function () use ($pdo, $bib) { return registrar_devolucion($pdo, $bib, 'EJ-9999', '2026-03-10'); }, 'ME-05');
rechaza('OP-02: devolución con la cuenta de dirección', function () use ($pdo, $dir_) { return registrar_devolucion($pdo, $dir_, 'EJ-0458', '2026-03-10'); }, 'ME-13');
rechaza('OP-02: devolución anterior a la salida', function () use ($pdo, $bib) { return registrar_devolucion($pdo, $bib, 'EJ-0458', '2026-03-01'); }, 'MV-10');
comprobar('RI-04: la base no permite borrar un préstamo', $directo('DELETE FROM prestamos WHERE id = 1'));
comprobar('RI-04: la base no permite cambiar una devolución ya registrada', $directo("UPDATE prestamos SET fecha_devolucion = '2026-03-10' WHERE id = 1"));
comprobar('RI-07: la base no permite cambiar el vencimiento de un préstamo', $directo("UPDATE prestamos SET fecha_vencimiento = '2026-04-30' WHERE id = 2"));
comprobar('P-03: EJ-0457 vuelve a prestarse', registrar_prestamo($pdo, $bib, 'LE-0124', 'EJ-0457', '2026-03-10')['codigo'] === 'ME-04');

echo "-- OP-03 y OP-04 (Capítulo 13)\n";
$c = consultar_disponibilidad($pdo, 'arroyo arapoty');
comprobar('P-08: «arroyo arapoty» encuentra la obra OB-0031', $c['ok'] && count($c['filas']) === 1 && $c['filas'][0]['codigo'] === 'OB-0031');
comprobar('P-08: cuenta los disponibles de toda la obra (EJ-0512; EJ-0457 y EJ-0458 prestados, EJ-0459 inactivo) → 0', (int) $c['filas'][0]['disponibles'] === 0);
$c = consultar_disponibilidad($pdo, 'escuela');
comprobar('P-08: «escuela» encuentra El arroyo y la escuela: 7 ejemplares, 2 disponibles (EJ-0601 y EJ-0800; los otros 5, prestados a la docente)', count($c['filas']) === 1 && (int) $c['filas'][0]['ejemplares'] === 7 && (int) $c['filas'][0]['disponibles'] === 2);
comprobar('P-12: la consulta pública devuelve solo datos de la obra, ningún dato de lectores',
    array_keys($c['filas'][0]) === array('codigo', 'titulo', 'autor', 'ejemplares', 'disponibles'));
comprobar('OP-03: sin coincidencias → ME-08', $codigo(consultar_disponibilidad($pdo, 'zzz')) === 'ME-08');
comprobar('OP-03: el comodín % se busca como texto, no trae todo → ME-08', $codigo(consultar_disponibilidad($pdo, '%')) === 'ME-08');
$a = listar_prestamos_activos($pdo, $bib, '2026-03-20');
$vencidos = array_values(array_filter($a['filas'], function ($f) { return $f['vencido']; }));
comprobar('P-04: los préstamos activos muestran qué lector tiene cada ejemplar', $a['ok'] && count($a['filas']) === contar($pdo, 'SELECT COUNT(*) FROM prestamos WHERE fecha_devolucion IS NULL')
    && $a['filas'][0]['lector'] !== '');
comprobar('OP-04: al 2026-03-20 están vencidos los 7 préstamos que vencían el 12/03 o el 17/03', count($vencidos) === 7);
comprobar('OP-04: al 2026-03-12 no está vencido el que vence ese día', count(array_filter(listar_prestamos_activos($pdo, $bib, '2026-03-12')['filas'], function ($f) { return $f['vencido']; })) === 0);
comprobar('OP-04: con la cuenta de dirección → ME-13', $codigo(listar_prestamos_activos($pdo, $dir_, '2026-03-20')) === 'ME-13');
comprobar('OP-04: fecha de referencia inválida → MV-08', $codigo(listar_prestamos_activos($pdo, $bib, '20/03/2026')) === 'MV-08');

echo "-- OP-05 informe mensual por curso (Capítulo 13)\n";
$i = informe_mensual($pdo, $dir_, '2026-03');
$suma = array_sum(array_map(function ($f) { return (int) $f['prestamos']; }, $i['filas']));
comprobar('P-09: la dirección pide el informe de marzo y la suma por grupo coincide con el total recontado', $i['ok'] && $suma === $i['total'] && $i['total'] === contar($pdo, "SELECT COUNT(*) FROM prestamos WHERE fecha_salida LIKE '2026-03-%'"));
$grupos = array_column($i['filas'], 'prestamos', 'grupo');
comprobar('P-09: fila «Docentes» con los 5 préstamos de la docente y ningún grupo «sin curso»', isset($grupos['Docentes']) && (int) $grupos['Docentes'] === 5 && !array_filter(array_keys($grupos), function ($g) { return $g === null || $g === ''; }));
comprobar('OP-05: la bibliotecaria también puede pedir el informe', informe_mensual($pdo, $bib, '2026-03')['ok']);
comprobar('OP-05: sin sesión → ME-13', $codigo(informe_mensual($pdo, null, '2026-03')) === 'ME-13');
comprobar('OP-05: mes inválido → MV-11', $codigo(informe_mensual($pdo, $bib, '2026-13')) === 'MV-11');
$pdo->exec("UPDATE lectores SET curso = '3.º BTI' WHERE codigo = 'LE-0123'");
comprobar('RI-08: si el estudiante cambia de curso, el informe de marzo no cambia', informe_mensual($pdo, $dir_, '2026-03')['filas'] === $i['filas']);

echo "-- OP-06 inactivar y OA-04 corregir lector (Capítulo 11)\n";
$hist = contar($pdo, "SELECT COUNT(*) FROM prestamos p JOIN lectores l ON l.id = p.lector_id WHERE l.codigo = 'LE-0124'");
comprobar('P-10: inactivar al lector LE-0124 → MA-08', $codigo(inactivar($pdo, $bib, 'lector', 'LE-0124')) === 'MA-08');
comprobar('P-10: su historial se conserva', contar($pdo, "SELECT COUNT(*) FROM prestamos p JOIN lectores l ON l.id = p.lector_id WHERE l.codigo = 'LE-0124'") === $hist && $hist > 0);
rechaza('OP-06: el lector inactivo no recibe préstamos nuevos', function () use ($pdo, $bib) { return registrar_prestamo($pdo, $bib, 'LE-0124', 'EJ-0601', '2026-03-20'); }, 'ME-01');
rechaza('OP-06: con la cuenta de dirección', function () use ($pdo, $dir_) { return inactivar($pdo, $dir_, 'ejemplar', 'EJ-0601'); }, 'ME-13');
rechaza('OP-06: código inexistente o ya inactivo', function () use ($pdo, $bib) { return inactivar($pdo, $bib, 'lector', 'LE-0124'); }, 'MV-07');
comprobar('RI-05: la base no permite borrar un lector con historial', $directo("DELETE FROM lectores WHERE codigo = 'LE-0124'"));
comprobar('RI-05: la base no permite cambiar el código de un ejemplar con historial', $directo("UPDATE ejemplares SET codigo = 'EJ-0999' WHERE codigo = 'EJ-0457'"));
comprobar('PA-04: corregir el nombre de LE-0123 → MA-07', $codigo(editar_lector($pdo, $bib, 'LE-0123', 'Estudiante A (ficticio, corregido)', '3.º BTI')) === 'MA-07');
rechaza('PA-04: corregir dejando sin curso a un estudiante', function () use ($pdo, $bib) { return editar_lector($pdo, $bib, 'LE-0123', 'Estudiante A', ''); }, 'MV-03');
rechaza('PA-04: lector inexistente', function () use ($pdo, $bib) { return editar_lector($pdo, $bib, 'LE-9999', 'X', '1.º'); }, 'MV-07');

echo "-- OA-05 corregir una obra (Capítulo 11)\n";
$ed_antes = contar($pdo, "SELECT COUNT(*) FROM ediciones d JOIN obras o ON o.id = d.obra_id WHERE o.codigo = 'OB-0031'");
comprobar('PA-05: corregir el título de OB-0031 → MA-09', $codigo(editar_obra($pdo, $bib, 'OB-0031', 'Cuentos del arroyo Arapoty (corregido)', 'Autora del caso (ficticia)')) === 'MA-09');
comprobar('PA-05: el título cambió y sus ediciones siguen', contar($pdo, "SELECT COUNT(*) FROM obras WHERE codigo = 'OB-0031' AND titulo LIKE '%(corregido)'") === 1 && contar($pdo, "SELECT COUNT(*) FROM ediciones d JOIN obras o ON o.id = d.obra_id WHERE o.codigo = 'OB-0031'") === $ed_antes);
rechaza('PA-05: título vacío', function () use ($pdo, $bib) { return editar_obra($pdo, $bib, 'OB-0031', '', 'X'); }, 'MV-01');
rechaza('PA-05: obra inexistente', function () use ($pdo, $bib) { return editar_obra($pdo, $bib, 'OB-9999', 'X', 'Y'); }, 'MV-07');
rechaza('PA-05: con la cuenta de dirección', function () use ($pdo, $dir_) { return editar_obra($pdo, $dir_, 'OB-0031', 'X', 'Y'); }, 'ME-13');

echo "-- Otros\n";
comprobar('Zona horaria de Paraguay', date_default_timezone_get() === 'America/Asuncion');
comprobar('Versión del esquema registrada (3)', contar($pdo, 'PRAGMA user_version') === 3);
comprobar('Ninguna contraseña se guarda en claro', contar($pdo, "SELECT COUNT(*) FROM cuentas WHERE clave_hash = 'prueba-solo-local' OR clave_hash NOT LIKE '$%'") === 0);
cerrar_conexion();
exec('rm -rf ' . escapeshellarg($dir));
terminar_prueba();
