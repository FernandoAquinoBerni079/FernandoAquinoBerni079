<?php
// Reglas de negocio: las operaciones del sistema (Capítulo 9, Tablas 9.3 y 9.4) y las
// auxiliares de la Unidad IV. Cada función empieza con su contrato y comprueba el rol en el
// servidor antes de hacer nada: si no alcanza, devuelve ME-13 y no cambia ningún dato.
// Versión de REFERENCIA DOCENTE: todas las operaciones están completas.

function sin_permiso($cuenta, array $roles)
{
    return tiene_rol($cuenta, $roles) ? null : resultado(false, 'ME-13');
}

// ---------------------------------------------------------------- Capítulo 10
// OA-01 dar de alta un ejemplar (operación auxiliar de PT-08; no es OP-06).
//   Entradas: código del ejemplar, código de una edición ya cargada, cuenta.
//   Precondición: rol de bibliotecaria (RNF-02).
//   Resultado: un ejemplar nuevo, activo, de esa edición (RF-07, RF-10). MA-01.
//   Errores: MV-01 (falta un dato), MV-02 (formato), MA-03 (edición inexistente),
//            MA-02 (código repetido), ME-13.
//   Prueba: PA-01.
function alta_ejemplar(PDO $pdo, $cuenta, $codigo, $codigo_edicion)
{
    if ($r = sin_permiso($cuenta, array('bibliotecaria'))) {
        return $r;
    }
    $codigo = strtoupper(trim((string) $codigo));
    $codigo_edicion = strtoupper(trim((string) $codigo_edicion));
    if ($codigo === '' || $codigo_edicion === '') {
        $falta = $codigo === '' ? 'el código del ejemplar' : 'el código de la edición';
        return resultado(false, 'MV-01', $falta);
    }
    if (!preg_match('/^EJ-[0-9]{4}$/', $codigo)) {
        return resultado(false, 'MV-02', $codigo, 'EJ- y cuatro cifras');
    }
    $ed = fila($pdo, 'SELECT id FROM ediciones WHERE codigo = ?', array($codigo_edicion));
    if (!$ed) {
        return resultado(false, 'MA-03', $codigo_edicion);
    }
    try {
        $st = $pdo->prepare('INSERT INTO ejemplares (codigo, edicion_id) VALUES (?, ?)');
        $st->execute(array($codigo, $ed['id']));
    } catch (PDOException $e) {
        if (strpos($e->getMessage(), 'UNIQUE') !== false) {
            return resultado(false, 'MA-02', $codigo);
        }
        throw $e;
    }
    return resultado(true, 'MA-01', $codigo, $codigo_edicion);
}

// ---------------------------------------------------------------- Capítulo 11
// OA-02 registrar una obra y su edición (o una edición nueva de una obra que ya existe).
//   Entradas: código de obra, título y autor (si la obra es nueva), código de edición,
//   editorial y año, cuenta. Precondición: rol de bibliotecaria.
//   Resultado: la edición queda registrada. MA-04.
//   Errores: MV-01, MV-02, MA-05 (código de edición repetido), ME-13. Prueba: PA-02.
function alta_obra_edicion(PDO $pdo, $cuenta, $codigo_obra, $titulo, $autor, $codigo_edicion,
    $editorial_anio)
{
    if ($r = sin_permiso($cuenta, array('bibliotecaria'))) {
        return $r;
    }
    $codigo_obra = strtoupper(trim((string) $codigo_obra));
    $codigo_edicion = strtoupper(trim((string) $codigo_edicion));
    $titulo = trim((string) $titulo);
    $autor = trim((string) $autor);
    $editorial_anio = trim((string) $editorial_anio);
    $codigos = array(array($codigo_obra, 'OB', 'el código de la obra'),
        array($codigo_edicion, 'ED', 'el código de la edición'));
    foreach ($codigos as $c) {
        if ($c[0] === '') {
            return resultado(false, 'MV-01', $c[2]);
        }
        if (!preg_match('/^' . $c[1] . '-[0-9]{4}$/', $c[0])) {
            return resultado(false, 'MV-02', $c[0], $c[1] . '- y cuatro cifras');
        }
    }
    $pdo->exec('BEGIN IMMEDIATE');
    try {
        $obra = fila($pdo, 'SELECT id FROM obras WHERE codigo = ?', array($codigo_obra));
        if (!$obra) {
            if ($titulo === '' || $autor === '') {
                $pdo->exec('ROLLBACK');
                return resultado(false, 'MV-01', $titulo === '' ? 'el título' : 'el autor');
            }
            $st = $pdo->prepare('INSERT INTO obras (codigo, titulo, autor) VALUES (?, ?, ?)');
            $st->execute(array($codigo_obra, $titulo, $autor));
            $obra = array('id' => $pdo->lastInsertId());
        }
        $st = $pdo->prepare('INSERT INTO ediciones (codigo, obra_id, editorial_anio)
            VALUES (?, ?, ?)');
        $st->execute(array($codigo_edicion, $obra['id'],
            $editorial_anio === '' ? null : $editorial_anio));
        $pdo->exec('COMMIT');
    } catch (PDOException $e) {
        $pdo->exec('ROLLBACK');
        if (strpos($e->getMessage(), 'UNIQUE') !== false) {
            return resultado(false, 'MA-05', $codigo_edicion);
        }
        throw $e;
    }
    return resultado(true, 'MA-04', $codigo_obra, $codigo_edicion);
}

// OA-03 registrar un lector (RF-11: tipo; RI-06: curso obligatorio solo para estudiantes).
//   Entradas: código, nombre, tipo, curso, cuenta. Precondición: rol de bibliotecaria.
//   Resultado: lector activo. MA-06.
//   Errores: MV-01, MV-02, MV-03 (estudiante sin curso), MV-04 (docente con curso), MA-05,
//            ME-13. Prueba: PA-03.
function alta_lector(PDO $pdo, $cuenta, $codigo, $nombre, $tipo, $curso)
{
    if ($r = sin_permiso($cuenta, array('bibliotecaria'))) {
        return $r;
    }
    $codigo = strtoupper(trim((string) $codigo));
    $nombre = trim((string) $nombre);
    $curso = trim((string) $curso);
    if ($r = validar_lector($codigo, $nombre, $tipo, $curso)) {
        return $r;
    }
    try {
        $st = $pdo->prepare('INSERT INTO lectores (codigo, nombre, tipo, curso)
            VALUES (?, ?, ?, ?)');
        $st->execute(array($codigo, $nombre, $tipo, $tipo === 'estudiante' ? $curso : null));
    } catch (PDOException $e) {
        if (strpos($e->getMessage(), 'UNIQUE') !== false) {
            return resultado(false, 'MA-05', $codigo);
        }
        throw $e;
    }
    return resultado(true, 'MA-06', $codigo);
}

// Validaciones del diccionario (Tabla 7.5) en el servidor, con un mensaje para cada caso.
function validar_lector($codigo, $nombre, $tipo, $curso)
{
    if ($codigo === '' || $nombre === '') {
        $falta = $codigo === '' ? 'el código del lector' : 'el nombre';
        return resultado(false, 'MV-01', $falta);
    }
    if (!preg_match('/^LE-[0-9]{4}$/', $codigo)) {
        return resultado(false, 'MV-02', $codigo, 'LE- y cuatro cifras');
    }
    if ($tipo !== 'estudiante' && $tipo !== 'docente') {
        return resultado(false, 'MV-01', 'el tipo de lector (estudiante o docente)');
    }
    if ($tipo === 'estudiante' && $curso === '') {
        return resultado(false, 'MV-03');                    // RI-06: el curso es obligatorio
    }
    if ($tipo === 'docente' && $curso !== '') {
        return resultado(false, 'MV-04');                    // RI-06: el docente no lleva curso
    }
    return null;
}

// OA-04 corregir el nombre o el curso de un lector. El código y el historial no cambian;
// los préstamos ya hechos conservan el curso que tenían (RI-08).
//   Errores: MV-01, MV-03, MV-04, MV-07, ME-13. Prueba: PA-04.
function editar_lector(PDO $pdo, $cuenta, $codigo, $nombre, $curso)
{
    if ($r = sin_permiso($cuenta, array('bibliotecaria'))) {
        return $r;
    }
    $codigo = strtoupper(trim((string) $codigo));
    $le = fila($pdo, 'SELECT tipo FROM lectores WHERE codigo = ?', array($codigo));
    if (!$le) {
        return resultado(false, 'MV-07', 'un lector', $codigo);
    }
    $nombre = trim((string) $nombre);
    $curso = trim((string) $curso);
    if ($r = validar_lector($codigo, $nombre, $le['tipo'], $curso)) {
        return $r;
    }
    $st = $pdo->prepare('UPDATE lectores SET nombre = ?, curso = ? WHERE codigo = ?');
    $st->execute(array($nombre, $le['tipo'] === 'estudiante' ? $curso : null, $codigo));
    return resultado(true, 'MA-07', $codigo);
}

// OA-05 corregir el título o el autor de una obra. El código, las ediciones, los ejemplares y el
// historial no cambian. Errores: MV-01, MV-07, ME-13. Prueba: PA-05.
function editar_obra(PDO $pdo, $cuenta, $codigo, $titulo, $autor)
{
    if ($r = sin_permiso($cuenta, array('bibliotecaria'))) {
        return $r;
    }
    $codigo = strtoupper(trim((string) $codigo));
    $titulo = trim((string) $titulo);
    $autor = trim((string) $autor);
    if (!fila($pdo, 'SELECT id FROM obras WHERE codigo = ?', array($codigo))) {
        return resultado(false, 'MV-07', 'una obra', $codigo);
    }
    if ($titulo === '' || $autor === '') {
        return resultado(false, 'MV-01', $titulo === '' ? 'el título' : 'el autor');
    }
    $st = $pdo->prepare('UPDATE obras SET titulo = ?, autor = ? WHERE codigo = ?');
    $st->execute(array($titulo, $autor, $codigo));
    return resultado(true, 'MA-09', $codigo);
}

// OP-06 inactivar lector o ejemplar (Tabla 9.3). Precondición: rol de bibliotecaria.
//   Resultado: queda inactivo; su historial no cambia (RI-05). MA-08.
//   Errores: ME-13; validación MV-07. Pruebas: P-10 y P-11.
function inactivar(PDO $pdo, $cuenta, $que, $codigo)
{
    if ($r = sin_permiso($cuenta, array('bibliotecaria'))) {
        return $r;
    }
    $tablas = array('lector' => array('lectores', 'un lector', 'Lector'),
        'ejemplar' => array('ejemplares', 'un ejemplar', 'Ejemplar'));
    if (!isset($tablas[$que])) {
        return resultado(false, 'MV-01', 'si es un lector o un ejemplar');
    }
    $codigo = strtoupper(trim((string) $codigo));
    // Baja lógica: se marca inactivo. Nada se borra y el historial queda como estaba.
    $st = $pdo->prepare('UPDATE ' . $tablas[$que][0] . ' SET activo = 0
        WHERE codigo = ? AND activo = 1');
    $st->execute(array($codigo));
    if ($st->rowCount() !== 1) {
        return resultado(false, 'MV-07', $tablas[$que][1], $codigo);
    }
    return resultado(true, 'MA-08', $tablas[$que][2], $codigo);
}

// ---------------------------------------------------------------- Capítulo 12
// OP-01 registrar préstamo (Tabla 9.4). Precondición: rol de bibliotecaria (RNF-02).
//   Resultado: préstamo nuevo con fecha de salida, curso del estudiante (RI-08) y vencimiento
//   con el plazo vigente (RI-07). ME-04.
//   Errores: ME-01 (RI-03), ME-02 (RI-02), ME-03 (RI-01), ME-05, ME-13.
//   Validación: MV-01, MV-05, MV-06, MV-08, MV-09.
//   Pruebas: P-01, P-02, P-05, P-06a, P-06b, P-07.
// RI-01 tiene dos barreras: esta operación es atómica (BEGIN IMMEDIATE toma el permiso de
// escritura antes de leer, así dos pedidos no comprueban las reglas al mismo tiempo) y la base
// tiene un índice único de préstamos activos por ejemplar (src/esquema.sql), que rechaza el
// segundo préstamo aunque alguien saltee esta función.
function registrar_prestamo(PDO $pdo, $cuenta, $codigo_lector, $codigo_ejemplar, $fecha)
{
    if ($r = sin_permiso($cuenta, array('bibliotecaria'))) {
        return $r;
    }
    $codigo_lector = strtoupper(trim((string) $codigo_lector));
    $codigo_ejemplar = strtoupper(trim((string) $codigo_ejemplar));
    if ($codigo_lector === '' || $codigo_ejemplar === '') {
        $falta = $codigo_lector === '' ? 'el código del lector' : 'el código del ejemplar';
        return resultado(false, 'MV-01', $falta);
    }
    if (sumar_dias((string) $fecha, 0) === null) {
        return resultado(false, 'MV-08', $fecha);
    }
    try {
        $pdo->exec('BEGIN IMMEDIATE');      // primera barrera: nadie más escribe hasta COMMIT
    } catch (PDOException $e) {
        return resultado(false, 'MV-09');
    }
    try {
        $r = comprobar_prestamo($pdo, $codigo_lector, $codigo_ejemplar);
        if ($r['error'] !== null) {
            $pdo->exec('ROLLBACK');
            return $r['error'];
        }
        $vence = sumar_dias($fecha, parametro($pdo, 'plazo_dias'));                 // RI-07
        $le = $r['lector'];
        $curso = $le['tipo'] === 'estudiante' ? $le['curso'] : null;                // RI-08
        $st = $pdo->prepare('INSERT INTO prestamos (ejemplar_id, lector_id, curso_al_prestar,
            fecha_salida, fecha_vencimiento) VALUES (?, ?, ?, ?, ?)');
        $st->execute(array($r['ejemplar']['id'], $le['id'], $curso, $fecha, $vence));
        $pdo->exec('COMMIT');
        return resultado(true, 'ME-04', fecha_visible($vence));
    } catch (PDOException $e) {
        try {
            $pdo->exec('ROLLBACK');             // nada queda a medias
        } catch (PDOException $e2) {
        }
        if (strpos($e->getMessage(), 'UNIQUE') !== false) {   // segunda barrera de RI-01
            $v = fila($pdo, 'SELECT p.fecha_vencimiento FROM prestamos p
                JOIN ejemplares e ON e.id = p.ejemplar_id
                WHERE e.codigo = ? AND p.fecha_devolucion IS NULL', array($codigo_ejemplar));
            $vence = $v ? fecha_visible($v['fecha_vencimiento']) : '';
            return resultado(false, 'ME-03', $codigo_ejemplar, $vence);
        }
        throw $e;
    }
}

// Comprobaciones de OP-01 en el orden de CU-01: lector (flujos 4a y 4b) y ejemplar (flujo 5a).
function comprobar_prestamo(PDO $pdo, $codigo_lector, $codigo_ejemplar)
{
    $sale = function ($error) {
        return array('error' => $error, 'lector' => null, 'ejemplar' => null);
    };
    $le = fila($pdo, 'SELECT id, tipo, curso, activo FROM lectores WHERE codigo = ?',
        array($codigo_lector));
    if (!$le) {
        return $sale(resultado(false, 'MV-05', $codigo_lector));
    }
    if (!$le['activo']) {
        return $sale(resultado(false, 'ME-01'));                         // RI-03, flujo 4a
    }
    $docente = $le['tipo'] === 'docente';
    $maximo = parametro($pdo, $docente ? 'maximo_docente' : 'maximo_estudiante');
    $n = fila($pdo, 'SELECT COUNT(*) AS n FROM prestamos
        WHERE lector_id = ? AND fecha_devolucion IS NULL', array($le['id']));
    if ((int) $n['n'] >= $maximo) {                                     // RI-02, flujo 4b
        return $sale(resultado(false, 'ME-02', $maximo, $docente ? 'docentes' : 'estudiantes'));
    }
    $ej = fila($pdo, 'SELECT id, activo FROM ejemplares WHERE codigo = ?',
        array($codigo_ejemplar));
    if (!$ej) {
        return $sale(resultado(false, 'ME-05'));
    }
    if (!$ej['activo']) {
        return $sale(resultado(false, 'MV-06', $codigo_ejemplar));       // RI-03
    }
    $activo = fila($pdo, 'SELECT fecha_vencimiento FROM prestamos
        WHERE ejemplar_id = ? AND fecha_devolucion IS NULL', array($ej['id']));
    if ($activo) {                                                      // RI-01, flujo 5a
        $vence = fecha_visible($activo['fecha_vencimiento']);
        return $sale(resultado(false, 'ME-03', $codigo_ejemplar, $vence));
    }
    return array('error' => null, 'lector' => $le, 'ejemplar' => $ej);
}

// OP-02 registrar devolución (Tabla 9.4). Precondición: rol de bibliotecaria.
//   Resultado: el préstamo activo del ejemplar recibe la fecha de devolución; no se borra
//   nada (RI-04). ME-07. Errores: ME-05, ME-06, ME-13. Validación: MV-01, MV-08, MV-10.
//   Prueba: P-03.
function registrar_devolucion(PDO $pdo, $cuenta, $codigo_ejemplar, $fecha)
{
    if ($r = sin_permiso($cuenta, array('bibliotecaria'))) {
        return $r;
    }
    $codigo_ejemplar = strtoupper(trim((string) $codigo_ejemplar));
    if ($codigo_ejemplar === '') {
        return resultado(false, 'MV-01', 'el código del ejemplar');
    }
    if (sumar_dias((string) $fecha, 0) === null) {
        return resultado(false, 'MV-08', $fecha);
    }
    $ej = fila($pdo, 'SELECT id FROM ejemplares WHERE codigo = ?', array($codigo_ejemplar));
    if (!$ej) {
        return resultado(false, 'ME-05');                                // CU-02, flujo 1a
    }
    try {
        // Una sola sentencia: si dos pedidos llegan a la vez, solo uno encuentra el préstamo.
        $st = $pdo->prepare('UPDATE prestamos SET fecha_devolucion = ?
            WHERE ejemplar_id = ? AND fecha_devolucion IS NULL');
        $st->execute(array($fecha, $ej['id']));
    } catch (PDOException $e) {
        if (strpos($e->getMessage(), 'CHECK') !== false) {
            $s = fila($pdo, 'SELECT fecha_salida FROM prestamos
                WHERE ejemplar_id = ? AND fecha_devolucion IS NULL', array($ej['id']));
            return resultado(false, 'MV-10', $s ? $s['fecha_salida'] : '');
        }
        throw $e;
    }
    if ($st->rowCount() !== 1) {
        return resultado(false, 'ME-06');                                // CU-02, flujo 2a
    }
    return resultado(true, 'ME-07');
}

// ---------------------------------------------------------------- Capítulo 13
// OP-03 consultar disponibilidad (pública). Entrada: parte del título.
//   Resultado: obras que coinciden, con sus ejemplares disponibles contados (dato derivado);
//   nunca datos de lectores (RNF-03). Errores: ME-08 (sin coincidencias); cada obra sin
//   disponibles muestra ME-09. Validación: MV-01. Pruebas: P-08 y P-12.
function consultar_disponibilidad(PDO $pdo, $texto)
{
    $texto = trim((string) $texto);
    if ($texto === '') {
        return resultado(false, 'MV-01', 'una parte del título') + array('filas' => array());
    }
    // Los comodines de LIKE (% y _) se escapan: se busca el texto tal como se escribió.
    $patron = '%' . strtr($texto, array('\\' => '\\\\', '%' => '\\%', '_' => '\\_')) . '%';
    $st = $pdo->prepare("SELECT o.codigo, o.titulo, o.autor,
            COUNT(e.id) AS ejemplares,
            COUNT(e.id) - COUNT(p.id) AS disponibles
        FROM obras o
        JOIN ediciones d ON d.obra_id = o.id
        JOIN ejemplares e ON e.edicion_id = d.id AND e.activo = 1
        LEFT JOIN prestamos p ON p.ejemplar_id = e.id AND p.fecha_devolucion IS NULL
        WHERE o.titulo LIKE ? ESCAPE '\\'
        GROUP BY o.id ORDER BY o.titulo");
    $st->execute(array($patron));
    $filas = $st->fetchAll();
    if (!$filas) {
        return resultado(false, 'ME-08') + array('filas' => array());
    }
    return array('ok' => true, 'codigo' => null, 'texto' => '', 'filas' => $filas);
}

// OP-04 listar préstamos activos (Tabla 9.3). Entradas: fecha de referencia, cuenta.
//   Precondición: rol de bibliotecaria. Resultado: préstamos sin devolución con ejemplar y
//   lector, y los vencidos marcados respecto de la fecha de referencia (no siempre «hoy»).
//   Errores: ME-10, ME-13. Validación: MV-08. Prueba: P-04.
function listar_prestamos_activos(PDO $pdo, $cuenta, $fecha_ref)
{
    if ($r = sin_permiso($cuenta, array('bibliotecaria'))) {
        return $r + array('filas' => array());
    }
    if (sumar_dias((string) $fecha_ref, 0) === null) {
        return resultado(false, 'MV-08', $fecha_ref) + array('filas' => array());
    }
    $st = $pdo->prepare('SELECT e.codigo AS ejemplar, o.titulo, l.codigo AS lector,
            l.nombre, p.fecha_salida, p.fecha_vencimiento,
            p.fecha_vencimiento < ? AS vencido
        FROM prestamos p
        JOIN ejemplares e ON e.id = p.ejemplar_id
        JOIN ediciones d ON d.id = e.edicion_id
        JOIN obras o ON o.id = d.obra_id
        JOIN lectores l ON l.id = p.lector_id
        WHERE p.fecha_devolucion IS NULL ORDER BY p.fecha_vencimiento, e.codigo');
    $st->execute(array($fecha_ref));
    $filas = $st->fetchAll();
    if (!$filas) {
        return resultado(true, 'ME-10') + array('filas' => array());
    }
    return array('ok' => true, 'codigo' => null, 'texto' => '', 'filas' => $filas);
}

// OP-05 informe mensual por curso (Tabla 9.3). Entradas: mes (año-mes), cuenta.
//   Precondición: rol de bibliotecaria o de dirección, comprobado por el servidor (RNF-02).
//   Resultado: préstamos del mes por curso al prestar (RI-08), la fila «Docentes» y el total
//   contado de nuevo. Errores: ME-13. Validación: MV-11. Prueba: P-09.
//   SC-02 (Unidad V): si el mes no tiene préstamos, el resultado es correcto, sin filas, con el
//   mensaje de estado vacío ME-14. Prueba: P-09 (caso del mes vacío).
function informe_mensual(PDO $pdo, $cuenta, $mes)
{
    $vacio = array('filas' => array(), 'total' => 0);
    if ($r = sin_permiso($cuenta, array('bibliotecaria', 'direccion'))) {
        return $r + $vacio;
    }
    $mes = trim((string) $mes);
    if (!preg_match('/^[0-9]{4}-(0[1-9]|1[0-2])$/', $mes)) {
        return resultado(false, 'MV-11', $mes) + $vacio;
    }
    $st = $pdo->prepare("SELECT CASE WHEN l.tipo = 'docente' THEN 'Docentes'
                ELSE p.curso_al_prestar END AS grupo,
            COUNT(*) AS prestamos
        FROM prestamos p JOIN lectores l ON l.id = p.lector_id
        WHERE substr(p.fecha_salida, 1, 7) = ?
        GROUP BY grupo ORDER BY l.tipo = 'docente', grupo");
    $st->execute(array($mes));
    $filas = $st->fetchAll();
    // El total se vuelve a contar en los préstamos del mes; no se suma a mano.
    $total = fila($pdo, 'SELECT COUNT(*) AS n FROM prestamos
        WHERE substr(fecha_salida, 1, 7) = ?', array($mes));
    if ((int) $total['n'] === 0) {
        return resultado(true, 'ME-14', $mes) + $vacio;                  // SC-02
    }
    return array('ok' => true, 'codigo' => null, 'texto' => '', 'filas' => $filas,
        'total' => (int) $total['n']);
}
