# -*- coding: utf-8 -*-
"""Fragmentos de código del libro. Cada uno se LEE del proyecto de referencia docente (no se copia a mano):
se busca la primera línea que empieza con `desde` y se toma hasta la primera línea siguiente que empieza con
`hasta`, inclusive. Cada fragmento dice archivo, propósito, requisito o contrato, entradas, resultado y prueba
(decisión 4 de Fernando). El verificador comprueba que el texto esté tal cual en el archivo y que ninguna línea
pase de ANCHO caracteres, para que se imprima sin cortes."""
import os
AQUI = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(os.path.dirname(AQUI), 'proyecto', 'referencia_docente')
ANCHO = 96

# id: (archivo, desde, hasta, ocurrencia de hasta, propósito, requisito o contrato, entradas, resultado, prueba)
FRAGMENTOS = {
    'Código 10.1': ('public/lectores.php', '<h2>Alta de un ejemplar</h2>', '</form>', 1,
                    'Formulario de la pantalla PT-08 para el alta de un ejemplar (presentación).',
                    'OA-01; boceto de PT-08 (Capítulo 8)', 'Código del ejemplar y código de la edición',
                    'Envía el pedido al servidor con la ficha CSRF', 'PA-01'),
    'Código 10.2': ('src/reglas.php', 'function alta_ejemplar(', "        return resultado(false, 'MV-02'", 1,
                    'Primera parte de OA-01: permiso, limpieza de las entradas y validación en el servidor.',
                    'OA-01; RNF-02 (ME-13); diccionario de Ejemplar (Tabla 7.5)', 'Cuenta, código del ejemplar y de la edición',
                    'ME-13, MV-01 o MV-02 sin tocar la base; si todo está bien, sigue', 'PA-01'),
    'Código 10.3': ('src/reglas.php', "    $ed = fila($pdo, 'SELECT id FROM ediciones", "    return resultado(true, 'MA-01'", 1,
                    'Segunda parte de OA-01: buscar la edición y guardar el ejemplar con consultas parametrizadas.',
                    'OA-01; RF-07; código único (Tabla 7.5)', 'Códigos ya validados',
                    'MA-01, o MA-03 si la edición no existe, o MA-02 si el código ya está', 'PA-01'),
    'Código 10.4': ('pruebas/prueba_contratos.php', '// Evidencia de persistencia', '$otra = null;', 1,
                    'Evidencia de persistencia: el dato sigue al abrir la base con otra conexión.',
                    'Work §7.2 (persistencia); OA-01', 'La base después del alta de EJ-0800',
                    'CORRECTO si el ejemplar está y activo', 'PA-01'),
    'Código 11.1': ('src/reglas.php', 'function validar_lector(', '}', 1,
                    'Validaciones del lector en el servidor, con un mensaje para cada caso.',
                    'OA-03 y OA-04; RF-11; RI-06', 'Código, nombre, tipo y curso',
                    'null si está bien; si no, MV-01 a MV-04', 'PA-03'),
    'Código 11.2': ('src/auth.php', '// Para las páginas: si la cuenta', '}', 1,
                    'Autorización por zona en cada pantalla: si el rol no corresponde, ME-13 y fin.',
                    'RNF-02; zonas de la Figura 8.1 (lote 3 v1.1)', 'La zona de la pantalla y la cuenta de la sesión',
                    '403 con ME-13, o la cuenta para seguir', 'P-11'),
    'Código 11.3': ('src/reglas.php', 'function sin_permiso(', '}', 1,
                    'La misma comprobación dentro de cada operación: ocultar un botón no alcanza.',
                    'RNF-02; Work §7.5; Tabla 9.2', 'Cuenta y roles que admite la operación',
                    'ME-13 o null', 'P-11'),
    'Código 11.4': ('src/reglas.php', '    // Baja lógica:', '    $st->execute(array($codigo));', 1,
                    'Baja lógica: el lector o el ejemplar se marca inactivo; nada se borra.',
                    'OP-06; RI-05 (RN-06)', 'Tabla y código', 'Una fila marcada inactiva', 'P-10'),
    'Código 11.5': ('src/esquema.sql', 'CREATE TRIGGER codigo_ejemplar_con_historial', 'END', 1,
                    'Protección en la base: el código de un ejemplar con historial no se cambia.',
                    'RI-05; Tabla 7.3', 'Una modificación del código', 'La base la rechaza', 'prueba_garantias.php'),
    'Código 12.1': ('src/reglas.php', "    $docente = $le['tipo'] === 'docente';", '    }', 1,
                    'El máximo de préstamos se lee de Parámetro según el tipo de lector.',
                    'OP-01, flujo 4b; RI-02; RN-02 v1.1 (SC-01)', 'Lector activo', 'ME-02 con el máximo del tipo, o sigue',
                    'P-06a y P-06b'),
    'Código 12.2': ('src/reglas.php', "        $pdo->exec('BEGIN IMMEDIATE');", "        return resultado(true, 'ME-04'", 1,
                    'Primera barrera de RI-01: comprobar y registrar en una sola operación atómica.',
                    'OP-01; RI-01, RI-07, RI-08', 'Lector, ejemplar y fecha ya validados',
                    'ME-04 con el vencimiento, o el error de la comprobación sin cambios', 'P-01, P-02, P-07'),
    'Código 12.3': ('src/esquema.sql', '-- RI-01, segunda barrera', 'WHERE fecha_devolucion IS NULL', 1,
                    'Segunda barrera de RI-01: la base no admite dos préstamos activos del mismo ejemplar.',
                    'RI-01; RN-01', 'Cualquier inserción en prestamos', 'La base rechaza el segundo préstamo activo', 'P-07'),
    'Código 12.4': ('src/reglas.php', '        // Una sola sentencia:', '        $st->execute(array($fecha, $ej[\'id\']));', 1,
                    'Devolución única: una sola sentencia cierra el préstamo activo del ejemplar.',
                    'OP-02; RI-04 (RN-05)', 'Ejemplar y fecha', 'Un préstamo cerrado, o ninguno (ME-06)', 'P-03'),
    'Código 13.1': ('src/reglas.php', '    // Los comodines de LIKE', '        GROUP BY o.id ORDER BY o.titulo");', 1,
                    'Consulta pública: disponibles contados en el momento, sin datos de lectores.',
                    'OP-03; RF-07; RNF-03', 'Parte del título', 'Obras con ejemplares y disponibles', 'P-08 y P-12'),
    'Código 13.2': ('src/reglas.php', "    $st = $pdo->prepare('SELECT e.codigo AS ejemplar", "        WHERE p.fecha_devolucion IS NULL ORDER BY", 1,
                    'Préstamos activos, con vencidos calculados respecto de una fecha de referencia.',
                    'OP-04; RF-08', 'Fecha de referencia', 'Lista con la marca «vencido»', 'P-04'),
    'Código 13.3': ('src/reglas.php', "    $st = $pdo->prepare(\"SELECT CASE WHEN l.tipo = 'docente'", "        'total' => (int) $total['n']);", 1,
                    'Informe mensual por curso al prestar, con la fila «Docentes» y el total recontado.',
                    'OP-05; RF-09; RI-08', 'Mes (año-mes)', 'Filas por grupo y total', 'P-09'),
}


def extraer(fid):
    archivo, desde, hasta, ocurrencia = FRAGMENTOS[fid][:4]
    lineas = open(os.path.join(REF, archivo), encoding='utf8').read().split('\n')
    i = next(k for k, l in enumerate(lineas) if l.startswith(desde))
    vistas = 0
    for j in range(i, len(lineas)):
        if lineas[j].startswith(hasta) and (j > i or desde == hasta):
            vistas += 1
            if vistas == ocurrencia:
                return [l.rstrip() for l in lineas[i:j + 1]]
    raise ValueError('fragmento sin final: %s' % fid)


def ficha(fid):
    a, _, _, _, prop, req, ent, res, prueba = FRAGMENTOS[fid]
    return {'archivo': 'referencia_docente/' + a, 'proposito': prop, 'requisito': req, 'entradas': ent,
            'resultado': res, 'prueba': prueba}


if __name__ == '__main__':
    for f in FRAGMENTOS:
        ls = extraer(f)
        print('%s  %-30s %3d líneas, máx. %d columnas' % (f, FRAGMENTOS[f][0], len(ls), max(len(l) for l in ls)))
