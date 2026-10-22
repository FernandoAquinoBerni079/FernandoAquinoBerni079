<?php
// Reglas de negocio: las operaciones del sistema (Capítulo 9, Tablas 9.3 y 9.4) y las auxiliares de la
// Unidad IV. Versión BASE DEL ESTUDIANTE: la comprobación del rol ya está preparada (sin_permiso, ME-13);
// cada operación tiene su contrato y la construís en el capítulo indicado. Hasta entonces devuelve PENDIENTE.

function sin_permiso($cuenta, array $roles)
{
    return tiene_rol($cuenta, $roles) ? null : resultado(false, 'ME-13');
}

// Respuesta de una operación que todavía no se construyó. No cambia ningún dato.
function pendiente($operacion, $capitulo)
{
    return array('ok' => false, 'codigo' => 'PENDIENTE', 'texto' => "$operacion todavía no está construida (Capítulo $capitulo).", 'filas' => array(), 'total' => 0);
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
    // Encuentro 20 (Capítulo 10, secciones 10.3 y 10.4): completá, en este orden,
    //  1. limpiar las entradas (espacios y mayúsculas) y comprobar que no falte ninguna (MV-01);
    //  2. validar en el servidor el formato EJ- y cuatro cifras (MV-02);
    //  3. buscar la edición con una consulta parametrizada (MA-03 si no existe);
    //  4. guardar el ejemplar con una consulta parametrizada y, si el código ya existe, devolver MA-02;
    //  5. devolver MA-01.
    return pendiente('OA-01 dar de alta un ejemplar', 10);
}

// ---------------------------------------------------------------- Capítulo 11
// OA-02 registrar una obra y su edición. Errores: MV-01, MV-02, MA-05, ME-13. Prueba: PA-02.
function alta_obra_edicion(PDO $pdo, $cuenta, $codigo_obra, $titulo, $autor, $codigo_edicion, $editorial_anio)
{
    return pendiente('OA-02 registrar una obra y su edición', 11);
}

// OA-05 corregir el título o el autor de una obra; el código y el historial no cambian.
// Errores: MV-01, MV-07, ME-13. Prueba: PA-05.
function editar_obra(PDO $pdo, $cuenta, $codigo, $titulo, $autor)
{
    return pendiente('OA-05 corregir una obra', 11);
}

// OA-03 registrar un lector (RF-11, RI-06). Errores: MV-01 a MV-04, MA-05, ME-13. Prueba: PA-03.
function alta_lector(PDO $pdo, $cuenta, $codigo, $nombre, $tipo, $curso)
{
    return pendiente('OA-03 registrar un lector', 11);
}

// OA-04 corregir nombre o curso de un lector, sin cambiar su código ni su historial (RI-08). Prueba: PA-04.
function editar_lector(PDO $pdo, $cuenta, $codigo, $nombre, $curso)
{
    return pendiente('OA-04 corregir un lector', 11);
}

// OP-06 inactivar lector o ejemplar (Tabla 9.3). Resultado: inactivo, historial intacto (RI-05). Pruebas: P-10, P-11.
function inactivar(PDO $pdo, $cuenta, $que, $codigo)
{
    return pendiente('OP-06 inactivar lector o ejemplar', 11);
}

// ---------------------------------------------------------------- Capítulo 12
// OP-01 registrar préstamo (Tabla 9.4): ME-01, ME-02, ME-03, ME-05, ME-13; RI-01 con dos barreras.
// Pruebas: P-01, P-02, P-05, P-06a, P-06b, P-07.
function registrar_prestamo(PDO $pdo, $cuenta, $codigo_lector, $codigo_ejemplar, $fecha)
{
    return pendiente('OP-01 registrar préstamo', 12);
}

// OP-02 registrar devolución (Tabla 9.4): ME-05, ME-06, ME-13; no se borra nada (RI-04). Prueba: P-03.
function registrar_devolucion(PDO $pdo, $cuenta, $codigo_ejemplar, $fecha)
{
    return pendiente('OP-02 registrar devolución', 12);
}

// ---------------------------------------------------------------- Capítulo 13
// OP-03 consultar disponibilidad (pública, sin datos de lectores): ME-08, ME-09. Pruebas: P-08, P-12.
function consultar_disponibilidad(PDO $pdo, $texto)
{
    return pendiente('OP-03 consultar disponibilidad', 13);
}

// OP-04 listar préstamos activos con fecha de referencia: ME-10, ME-13. Prueba: P-04.
function listar_prestamos_activos(PDO $pdo, $cuenta, $fecha_ref)
{
    return pendiente('OP-04 listar préstamos activos', 13);
}

// OP-05 informe mensual por curso, para bibliotecaria y dirección: ME-13. Prueba: P-09.
function informe_mensual(PDO $pdo, $cuenta, $mes)
{
    return pendiente('OP-05 informe mensual por curso', 13);
}
