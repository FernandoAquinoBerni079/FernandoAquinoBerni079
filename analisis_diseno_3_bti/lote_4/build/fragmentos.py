# -*- coding: utf-8 -*-
"""Fragmentos de código del libro y de la guía. Cada uno se LEE del proyecto (no se copia a mano): se busca la
primera línea que empieza con `desde` (si `desde` es una tupla, cada ancla se busca a partir de la anterior) y se
toma hasta la primera línea siguiente que empieza con `hasta`, inclusive. Cada fragmento dice archivo, propósito,
requisito o contrato, entradas, resultado y prueba (decisión 4 de Fernando). El verificador comprueba que el texto
esté tal cual en el archivo y que ninguna línea pase de ANCHO caracteres, para que se imprima sin cortes.

FRAGMENTOS van en el libro del estudiante. Son la operación de ejemplo del Capítulo 10 (OA-01, resuelta a propósito:
decisión 3), lo que la base ya trae (autorización, esquema) y las protecciones que el capítulo explica (las dos
barreras de RI-01, la devolución en una sola sentencia, las consultas con dato derivado y fecha de referencia).
REFERENCIA va solo en la guía docente: son partes de operaciones que construyen los equipos (validar_lector,
comprobar_prestamo, informe_mensual), para que el libro no publique esas actividades resueltas."""
import os
AQUI = os.path.dirname(os.path.abspath(__file__))
PROY = os.path.join(os.path.dirname(AQUI), 'proyecto')
ANCHO = 96

# id: (archivo (distribución/ruta), desde, hasta, ocurrencia de hasta, propósito, requisito o contrato, entradas,
#      resultado, prueba)
FRAGMENTOS = {
    'Código 10.1': ('referencia_docente/public/lectores.php', '<h2>Alta de un ejemplar</h2>', '</form>', 1,
                    'Formulario de la pantalla PT-08 para el alta de un ejemplar (presentación).',
                    'OA-01; boceto de PT-08 (Capítulo 8)', 'Código del ejemplar y código de la edición',
                    'Envía el pedido al servidor con la ficha CSRF y el botón «Guardando…» (ME-11)', 'PA-01'),
    'Código 10.2': ('base_estudiante/public/lectores.php', "$cuenta = exigir_zona('Bibliotecaria');", '}', 1,
                    'Procesamiento del pedido en la página: zona, ficha CSRF, operación y aviso después de redirigir.',
                    'OA-01; RNF-02; patrón POST-redirección-GET (Capítulo 12)', 'El pedido POST del formulario',
                    'El resultado de alta_ejemplar() guardado para mostrarlo una sola vez', 'PA-01'),
    'Código 10.3': ('referencia_docente/src/reglas.php', 'function alta_ejemplar(', "        return resultado(false, 'MV-02'", 1,
                    'Primera parte de OA-01: permiso, limpieza de las entradas y validación en el servidor.',
                    'OA-01; RNF-02 (ME-13); diccionario de Ejemplar (Tabla 7.5)', 'Cuenta, código del ejemplar y de la edición',
                    'ME-13, MV-01 o MV-02 sin tocar la base; si todo está bien, sigue', 'PA-01'),
    'Código 10.4': ('referencia_docente/src/reglas.php', "    $ed = fila($pdo, 'SELECT id FROM ediciones", "    return resultado(true, 'MA-01'", 1,
                    'Segunda parte de OA-01: buscar la edición y guardar el ejemplar con consultas parametrizadas.',
                    'OA-01; RF-07; código único (Tabla 7.5)', 'Códigos ya validados',
                    'MA-01, o MA-03 si la edición no existe, o MA-02 si el código ya está', 'PA-01'),
    'Código 10.5': ('referencia_docente/pruebas/prueba_contratos.php', '// Evidencia de persistencia', '$otra = null;', 1,
                    'Evidencia de persistencia: el dato sigue al abrir la base con otra conexión.',
                    'Work §7.2 (persistencia); OA-01', 'La base después del alta de EJ-0800',
                    'CORRECTO si el ejemplar está y activo', 'PA-01'),
    'Código 11.1': ('referencia_docente/src/auth.php', '// Para las páginas: si la cuenta', '}', 1,
                    'Autorización por zona en cada pantalla: si el rol no corresponde, ME-13 y fin.',
                    'RNF-02; zonas de la Figura 8.1 (lote 3 v1.1)', 'La zona de la pantalla y la cuenta de la sesión',
                    '403 con ME-13, o la cuenta para seguir', 'P-11'),
    'Código 11.2': ('referencia_docente/src/reglas.php', 'function sin_permiso(', '}', 1,
                    'La misma comprobación dentro de cada operación: ocultar un botón no alcanza.',
                    'RNF-02; Work §7.5; Tabla 9.2', 'Cuenta y roles que admite la operación',
                    'ME-13 o null', 'P-11'),
    'Código 11.3': ('referencia_docente/src/reglas.php', '    // Baja lógica:', '    $st->execute(array($codigo));', 1,
                    'Baja lógica: el lector o el ejemplar se marca inactivo; nada se borra.',
                    'OP-06; RI-05 (RN-06)', 'Tabla y código', 'Una fila marcada inactiva', 'P-10'),
    'Código 11.4': ('referencia_docente/src/esquema.sql', 'CREATE TRIGGER codigo_ejemplar_con_historial', 'END', 1,
                    'Protección en la base: el código de un ejemplar con historial no se cambia.',
                    'RI-05; Tabla 7.3', 'Una modificación del código', 'La base la rechaza', 'prueba_garantias.php'),
    'Código 12.1': ('referencia_docente/src/reglas.php', ('function registrar_prestamo(', '    try {'),
                    "        return resultado(true, 'ME-04'", 1,
                    'Primera barrera de RI-01: comprobar y registrar en una sola operación atómica.',
                    'OP-01; RI-01, RI-07, RI-08', 'Lector, ejemplar y fecha ya validados',
                    'ME-04 con el vencimiento, o el error de la comprobación sin cambios', 'P-01, P-02, P-07'),
    'Código 12.4': ('referencia_docente/src/reglas.php', ('function registrar_prestamo(', "        return resultado(true, 'ME-04'",
                                                         '    } catch (PDOException $e) {'),
                    '        throw $e;', 1,
                    'Si algo falla a mitad de camino: se deshace todo, y la segunda barrera responde ME-03.',
                    'OP-01; RI-01; Capítulo 12.4 (fallos previsibles)', 'Un error de la base durante la operación',
                    'Ningún préstamo a medias; ME-03 si la base rechazó un segundo préstamo activo', 'P-07'),
    'Código 12.2': ('referencia_docente/src/esquema.sql', '-- RI-01, segunda barrera', 'WHERE fecha_devolucion IS NULL', 1,
                    'Segunda barrera de RI-01: la base no admite dos préstamos activos del mismo ejemplar.',
                    'RI-01; RN-01', 'Cualquier inserción en prestamos', 'La base rechaza el segundo préstamo activo', 'P-07'),
    'Código 12.3': ('referencia_docente/src/reglas.php', '        // Una sola sentencia:', '        $st->execute(array($fecha, $ej[\'id\']));', 1,
                    'Devolución única: una sola sentencia cierra el préstamo activo del ejemplar.',
                    'OP-02; RI-04 (RN-05)', 'Ejemplar y fecha', 'Un préstamo cerrado, o ninguno (ME-06)', 'P-03'),
    'Código 13.1': ('referencia_docente/src/reglas.php', '    // Los comodines de LIKE', '        GROUP BY o.id ORDER BY o.titulo");', 1,
                    'Consulta pública: disponibles contados en el momento, sin datos de lectores.',
                    'OP-03; RF-07; RNF-03', 'Parte del título', 'Obras con ejemplares y disponibles', 'P-08 y P-12'),
    'Código 13.2': ('referencia_docente/src/reglas.php', "    $st = $pdo->prepare('SELECT e.codigo AS ejemplar", "        WHERE p.fecha_devolucion IS NULL ORDER BY", 1,
                    'Préstamos activos, con vencidos calculados respecto de una fecha de referencia.',
                    'OP-04; RF-08', 'Fecha de referencia', 'Lista con la marca «vencido»', 'P-04'),
}

# Solo en la guía docente (partes de operaciones que construyen los equipos).
REFERENCIA = {
    'Referencia R-1': ('referencia_docente/src/reglas.php', 'function validar_lector(', '}', 1,
                       'Validaciones del lector en el servidor, con un mensaje para cada caso.',
                       'OA-03 y OA-04; RF-11; RI-06', 'Código, nombre, tipo y curso',
                       'null si está bien; si no, MV-01 a MV-04', 'PA-03'),
    'Referencia R-2': ('referencia_docente/src/reglas.php', 'function comprobar_prestamo(', '}', 1,
                       'Comprobaciones de OP-01 en el orden de CU-01: lector (4a, 4b) y ejemplar (5a).',
                       'OP-01; RI-01, RI-02, RI-03; RN-02 v1.1 (SC-01)', 'Códigos del lector y del ejemplar',
                       'El primer error que corresponde, o el lector y el ejemplar para seguir', 'P-05, P-06a, P-06b, P-07'),
    'Referencia R-3': ('referencia_docente/src/reglas.php', "    $st = $pdo->prepare(\"SELECT CASE WHEN l.tipo = 'docente'", "        'total' => (int) $total['n']);", 1,
                       'Informe mensual por curso al prestar, con la fila «Docentes» y el total recontado.',
                       'OP-05; RF-09; RI-08', 'Mes (año-mes)', 'Filas por grupo y total', 'P-09'),
}
TODOS = dict(FRAGMENTOS, **REFERENCIA)


def _lineas(archivo):
    return open(os.path.join(PROY, archivo), encoding='utf8').read().split('\n')


def extraer(fid):
    archivo, desde, hasta, ocurrencia = TODOS[fid][:4]
    lineas = _lineas(archivo)
    i = 0
    for ancla in (desde if isinstance(desde, tuple) else (desde,)):
        i = next(k for k in range(i, len(lineas)) if lineas[k].startswith(ancla))
    ultima = desde[-1] if isinstance(desde, tuple) else desde
    vistas = 0
    for j in range(i, len(lineas)):
        if lineas[j].startswith(hasta) and (j > i or ultima == hasta):
            vistas += 1
            if vistas == ocurrencia:
                return [l.rstrip() for l in lineas[i:j + 1]]
    raise ValueError('fragmento sin final: %s' % fid)


def ficha(fid):
    a, _, _, _, prop, req, ent, res, prueba = TODOS[fid]
    return {'archivo': a, 'proposito': prop, 'requisito': req, 'entradas': ent, 'resultado': res, 'prueba': prueba}


def del_capitulo(n):
    return [f for f in FRAGMENTOS if f.startswith('Código %d.' % n)]


if __name__ == '__main__':
    for f in TODOS:
        ls = extraer(f)
        print('%-15s %-48s %3d líneas, máx. %d columnas' % (f, TODOS[f][0], len(ls), max(len(l) for l in ls)))
