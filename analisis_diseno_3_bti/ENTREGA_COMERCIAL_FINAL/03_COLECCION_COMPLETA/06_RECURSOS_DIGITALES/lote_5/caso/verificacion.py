# -*- coding: utf-8 -*-
"""Fuente única de la verificación de la Unidad V (Capítulos 14 a 16). Caso Arapoty, ficticio.

Lee sin modificarlos `lote_3/caso/diseno.py` (catálogo v1.1, contratos, mensajes) y `lote_4/caso/construccion.py`
(operaciones auxiliares, incidencias, resultados). Contiene:
  - la matriz de pruebas del equipo modelo (CASOS), que build/reproducir.py EJECUTA de verdad sobre copias
    descartables cargadas con el conjunto DP: el «obtenido» sale de la ejecución, no se escribe a mano;
  - la condición de cada resultado o incidencia (comprobado, reproducido, simulado o pendiente);
  - las sesiones de uso del equipo modelo (simulación rotulada), el acta de aceptación y el registro de regresión;
  - la corrección de IN-02 (ejemplo central) y la solicitud de cambio SC-02 (ejemplo complementario);
  - el banco de variantes del H5 (V5).
El conjunto reservado DR no está acá (dr_plantilla.py tiene solo su estructura)."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
L5 = os.path.dirname(AQUI)
ADS = os.path.dirname(L5)
sys.path.insert(0, os.path.join(ADS, 'lote_4', 'caso'))
sys.path.insert(1, os.path.join(ADS, 'lote_3', 'caso'))
import construccion as C4
import datos_prueba_u5 as DP
X = C4.X
R = X.R

CONDICIONES = [
    ('Comprobado', 'Se ejecutó y su resultado quedó registrado con el entorno en que corrió.'),
    ('Reproducido', 'Una incidencia que se volvió a provocar a propósito, con pasos que cualquiera puede repetir.'),
    ('Simulado', 'Datos de un caso ficticio, rotulados como tales: sirven para practicar, no son evidencia del sistema.'),
    ('Pendiente', 'No se pudo probar todavía (por ejemplo, en las computadoras del colegio). No se da por bueno.'),
]
CLASES = [
    ('Normal', 'Lo que pasa casi siempre: datos correctos y una operación permitida.'),
    ('Límite', 'Justo en el borde de una regla: el máximo, el mismo día del vencimiento, un carácter especial.'),
    ('Excepción', 'Algo fuera de lo común que el sistema tiene que manejar: una fecha imposible, la base ocupada.'),
    ('Rechazo', 'Una operación que no se debe hacer: el sistema la rechaza con su mensaje y no cambia datos.'),
]

# ------------------------------------------------------------------ matriz de pruebas del equipo modelo
# (id, requisito, prueba prevista, clase, qué se prueba, operación, cuenta, entradas, código esperado, control, esperado)
# Los casos se ejecutan EN ORDEN sobre una copia cargada con DP (el estado de uno es el punto de partida del siguiente).
R_ = DP.FECHA_REFERENCIA
CASOS = [
    ('C-01', 'RF-01', 'P-01', 'Normal', 'Préstamo válido de un estudiante con un préstamo activo',
     'OP-01', 'bibliotecaria', ['LE-1001', 'EJ-1004', R_], 'ME-04',
     {'sql': "SELECT COUNT(*) FROM prestamos p JOIN lectores l ON l.id = p.lector_id WHERE l.codigo = 'LE-1001' AND p.fecha_devolucion IS NULL", 'valor': 2},
     'ME-04; LE-1001 queda con 2 activos'),
    ('C-02', 'RF-02', 'P-02', 'Normal', 'El vencimiento se calcula con el plazo de 7 días y se guarda',
     'OP-01', 'bibliotecaria', ['LE-1005', 'EJ-1005', R_], 'ME-04',
     {'texto': '19/05'}, 'ME-04 con «Vence el 19/05»'),
    ('C-03', 'RF-05', 'P-06a', 'Límite', 'Estudiante en su máximo (2) pide un tercero',
     'OP-01', 'bibliotecaria', ['LE-1001', 'EJ-1008', R_], 'ME-02',
     {'texto': 'el máximo para estudiantes'}, 'ME-02 con el máximo de estudiantes; sin préstamo nuevo'),
    ('C-04', 'RF-05', 'P-06b', 'Límite', 'Docente con 4 activos pide el quinto (máximo 5)',
     'OP-01', 'bibliotecaria', ['LE-1003', 'EJ-1007', R_], 'ME-04', None, 'ME-04: se registra'),
    ('C-05', 'RF-05', 'P-06b', 'Límite', 'Docente en su máximo (5) pide el sexto',
     'OP-01', 'bibliotecaria', ['LE-1003', 'EJ-1008', R_], 'ME-02',
     {'texto': 'el máximo para docentes'}, 'ME-02 con el máximo de docentes; sin préstamo nuevo'),
    ('C-06', 'RF-04', 'P-07', 'Rechazo', 'Segunda solicitud sobre un ejemplar ya prestado',
     'OP-01', 'bibliotecaria', ['LE-1005', 'EJ-1001', R_], 'ME-03',
     {'sql': "SELECT COUNT(*) FROM prestamos p JOIN ejemplares e ON e.id = p.ejemplar_id WHERE e.codigo = 'EJ-1001' AND p.fecha_devolucion IS NULL", 'valor': 1},
     'ME-03; EJ-1001 sigue con un solo préstamo activo'),
    ('C-07', 'RF-06', 'P-05', 'Rechazo', 'Préstamo a un lector inactivo',
     'OP-01', 'bibliotecaria', ['LE-1004', 'EJ-1008', R_], 'ME-01', None, 'ME-01; sin préstamo nuevo'),
    ('C-08', 'RF-10', 'P-10', 'Rechazo', 'Préstamo de un ejemplar dado de baja, que tiene historial',
     'OP-01', 'bibliotecaria', ['LE-1005', 'EJ-1006', R_], 'MV-06',
     {'sql': "SELECT COUNT(*) FROM prestamos p JOIN ejemplares e ON e.id = p.ejemplar_id WHERE e.codigo = 'EJ-1006'", 'valor': 1},
     'MV-06; el historial de EJ-1006 sigue con su préstamo'),
    ('C-09', 'RF-03', 'P-03', 'Normal', 'Devolución de un ejemplar prestado',
     'OP-02', 'bibliotecaria', ['EJ-1004', '2026-05-14'], 'ME-07', None, 'ME-07; el préstamo queda en el historial'),
    ('C-10', 'RF-03', 'P-03', 'Rechazo', 'Segunda devolución del mismo ejemplar',
     'OP-02', 'bibliotecaria', ['EJ-1004', '2026-05-15'], 'ME-06', None, 'ME-06; no se cierra ningún préstamo'),
    ('C-11', 'RF-03', 'P-03', 'Excepción', 'Devolución con fecha anterior a la salida',
     'OP-02', 'bibliotecaria', ['EJ-1002', '2026-05-01'], 'MV-10', None, 'MV-10; el préstamo sigue activo'),
    ('C-12', 'RF-08', 'P-04', 'Límite', 'Vencidos con fecha de referencia 12/05: uno vencido y uno que vence ese día',
     'OP-04', 'bibliotecaria', [R_], None,
     {'filas': [({'ejemplar': 'EJ-1001'}, {'vencido': 1}), ({'ejemplar': 'EJ-1002'}, {'vencido': 0})]},
     'EJ-1001 vencido; EJ-1002 en plazo (vence ese mismo día)'),
    ('C-13', 'RF-07', 'P-08', 'Límite', 'Búsqueda con el signo «%» en el texto',
     'OP-03', None, ['100%'], None, {'filas_cuenta': 1, 'filas': [({'codigo': 'OB-1003'}, {'disponibles': 0})]},
     'Solo «Diccionario 100% escolar», con 0 disponibles (su ejemplar se prestó en C-04)'),
    ('C-14', 'RF-07', 'P-08', 'Límite', 'Búsqueda con el signo «_» en el texto',
     'OP-03', None, ['_'], None, {'filas_cuenta': 1, 'filas': [({'codigo': 'OB-1004'}, {})]}, 'Solo «Juegos_de_patio»'),
    ('C-15', 'RNF-03', 'P-12', 'Normal', 'La consulta pública no devuelve datos de lectores',
     'OP-03', None, ['río'], None, {'sin_campos': ['lector', 'nombre', 'curso']}, 'Obras y disponibles, sin datos de lectores'),
    ('C-16', 'RF-09', 'P-09', 'Normal', 'Informe de abril: el préstamo cuenta en el curso que tenía al prestar',
     'OP-05', 'direccion', ['2026-04'], None, {'filas': [({'grupo': '1.º BTI'}, {'prestamos': 1})], 'total': 1},
     '1.º BTI: 1 (aunque LE-1005 hoy está en 2.º BTI); total 1'),
    ('C-17', 'RNF-02', 'P-11', 'Rechazo', 'Préstamo pedido con la cuenta de dirección',
     'OP-01', 'direccion', ['LE-1005', 'EJ-1008', R_], 'ME-13', None, 'ME-13; sin préstamo nuevo'),
    ('C-18', 'RNF-02', 'P-11', 'Rechazo', 'Préstamos activos pedidos sin sesión',
     'OP-04', None, [R_], 'ME-13', None, 'ME-13'),
    ('C-19', 'RF-09', 'P-09', 'Límite', 'Informe de un mes sin préstamos',
     'OP-05', 'bibliotecaria', ['2026-01'], None, {'total': 0, 'filas_cuenta': 0},
     'Correcto, sin filas y total 0 (el contrato v1.1 no pide un mensaje: ver SC-02)'),
    ('C-20', 'RNF-01', 'P-14', 'Excepción', 'PT-08: después de un error al dar de alta un lector, se conserva lo escrito y el tipo',
     'HTTP', 'bibliotecaria', ['pruebas/prueba_in02.sh'], None, None,
     'Vuelven el código, el nombre y el tipo elegido (Docente)'),
]
CLASE_DE = {c[0]: c[3] for c in CASOS}


def casos_json():
    return [{'id': c[0], 'requisito': c[1], 'prueba': c[2], 'clase': c[3], 'descripcion': c[4], 'operacion': c[5],
             'cuenta': c[6], 'entradas': c[7], 'esperado_codigo': c[8], 'control': c[9], 'esperado': c[10]} for c in CASOS]


# ------------------------------------------------------------------ incidencias de partida (Capítulo 14) con su condición
# (código, dónde, qué pasa, condición, evidencia)
INCIDENCIAS_PARTIDA = [
    ('IN-01', 'PT-07', 'Con la fecha de referencia vacía, MV-08 «no dice qué fecha usar».', 'Simulado',
     'No se reproduce: el mensaje sí da el formato y un ejemplo. Detalle real menor: «La fecha  no es válida» (IN-01 bis).'),
    ('IN-01 bis', 'PT-07', 'Con la fecha vacía, el mensaje dice «La fecha  no es válida», con un espacio doble.', 'Reproducido',
     'lote_5_plan/reproduccion_incidencias_u4.txt'),
    ('IN-02', 'PT-08', 'Después de un error en el alta de un lector, el formulario no conserva lo escrito ni el tipo.', 'Reproducido',
     'prueba_in02.sh: 5 de 7 sobre la referencia del lote 4 (falla), 7 de 7 sobre la v2'),
    ('IN-03', 'PT-09', 'Un mes sin préstamos muestra solo «Total 0», sin un mensaje que diga que está vacío.', 'Reproducido',
     'Comportamiento conforme al contrato de OP-05 v1.1: se trata como mejora (SC-02), no como defecto'),
    ('MI-05, MI-07', 'Mbokaja', 'La semana de Mbokaja (Práctica 13).', 'Simulado', 'Datos ficticios de práctica'),
    ('E-1 a E-12', 'Entorno', 'Prueba de campo en las computadoras del colegio y en Windows.', 'Pendiente', 'No hay acta de campo'),
]

# ------------------------------------------------------------------ reporte de defecto (formato) con IN-02
REPORTE_IN02 = [
    ('Código', 'IN-02'),
    ('Pantalla y operación', 'PT-08, alta de un lector (OA-03)'),
    ('Requisito', 'RNF-01 (la bibliotecaria registra sin ayuda); regla de los mensajes del Capítulo 8'),
    ('Pasos para reproducirlo', '1. Ingresar con bibliotecaria1. 2. En PT-08, alta de lector: LE-0990, un nombre, tipo Docente, curso 6. 3. Registrar.'),
    ('Esperado', 'MV-04 y el formulario con lo escrito, con «Docente» elegido, para corregir solo el curso.'),
    ('Obtenido', 'MV-04, pero el formulario vacío y con «Estudiante» elegido: hay que escribir todo de nuevo.'),
    ('Gravedad', 'Media: no se pierden datos guardados, pero invita a cargar mal el tipo (RF-11).'),
    ('Entorno', 'Referencia docente del lote 4; Linux, PHP 8.3.6, SQLite 3.45.1 (contenedor de construcción)'),
    ('Condición', 'Reproducido (prueba_in02.sh: 5 de 7)'),
]

# ------------------------------------------------------------------ sesiones de uso del equipo modelo (simulación rotulada)
SESIONES = [  # (sesión, rol, tarea nueva, observación (lo que hizo), dificultad, requisito)
    ('S1', 'Bibliotecaria (compañera en rol)', 'Registrar dos préstamos seguidos para el mismo lector y devolver uno',
     'Escribió el código del lector dos veces; buscó la lista de activos antes de prestar el segundo.', 'Ninguna grave', 'RNF-01'),
    ('S1', 'Bibliotecaria (compañera en rol)', 'Dar de alta un lector docente',
     'Eligió «Docente», escribió un curso; ante MV-04 volvió a escribir todo y dejó «Estudiante» elegido.', 'Reproduce IN-02', 'RNF-01, RF-11'),
    ('S2', 'Dirección (compañero en rol)', 'Ver el informe de un mes en que la biblioteca estuvo cerrada',
     'Vio la tabla con «Total 0» y preguntó si el sistema había fallado.', 'Ver SC-02', 'RF-09'),
    ('S2', 'Dirección (compañero en rol)', 'Intentar ver los préstamos activos',
     'Escribió la dirección de PT-07; leyó ME-13 y volvió al informe.', 'Ninguna', 'RNF-02'),
]
SESIONES_NOTA = ('Las sesiones del equipo modelo son una simulación del libro, con compañeros en roles. Las de tu equipo '
                 'son reales: las hacen dos compañeros con roles distintos, con tareas nuevas, sobre el sistema funcionando.')

# ------------------------------------------------------------------ aceptación por criterios (equipo modelo)
# (requisito, texto (resumido), evidencia, estado). El estado SALE DE LOS RESULTADOS de la matriz (resultados_pruebas):
# «Aceptado» solo si todos sus casos dieron el resultado esperado; lo que no tiene evidencia queda «Pendiente».
CASOS_EXTRA = {'RF-11': ['C-04', 'C-05'], 'RNF-01': ['C-20']}
PENDIENTES_ENTORNO = {'RS-01': 'P-13 sin internet en la computadora del colegio',
                      'RS-02': 'E-3: licencias del navegador y del editor que usa el colegio'}


def resultados(version):
    p = os.path.join(L5, 'resultados_pruebas', 'resumen.json')
    if not os.path.exists(p):
        return {}
    return {c['id']: c for c in json.load(open(p, encoding='utf8'))['matriz'][version]['casos']}


def acta(version='v1_lote4'):
    res = resultados(version)
    filas = []
    for r in X.CATALOGO_V11:
        cod = r[0]
        casos = [c[0] for c in CASOS if c[1] == cod] + CASOS_EXTRA.get(cod, [])
        texto = r[2] if len(r[2]) <= 72 else r[2][:72].rsplit(' ', 1)[0].rstrip(',;:') + '…'
        if cod in PENDIENTES_ENTORNO:
            filas.append((cod, texto, PENDIENTES_ENTORNO[cod], 'Pendiente'))
        elif not casos:
            filas.append((cod, texto, 'Sin caso en la matriz', 'Pendiente'))
        else:
            malos = sorted(set(c for c in casos if not res.get(c, {}).get('correcto')))
            filas.append((cod, texto, ', '.join(sorted(set(casos))),
                          'Aceptado' if not malos else 'No aceptado (%s)' % ', '.join(malos)))
    return filas


# ------------------------------------------------------------------ prioridad de correcciones (Capítulo 15.4)
PRIORIDADES = [  # (incidencia, gravedad, frecuencia, requisito, decisión)
    ('IN-02', 'Media', 'Cada vez que hay un error en el alta', 'RNF-01', 'Se corrige en la Unidad V (referencia v2)'),
    ('IN-03', 'Baja (no es defecto)', 'En los meses sin préstamos', 'RF-09', 'Solicitud de mejora SC-02: se tramita'),
    ('IN-01 bis', 'Baja', 'Solo con la fecha vacía', 'RNF-01', 'Límite conocido de la versión candidata'),
]

# ------------------------------------------------------------------ SC-02 (formato de SC-01, Capítulo 6)
SC02 = [
    ('Identificador', 'SC-02'),
    ('Quién la pide y cuándo', 'La dirección, después de la sesión de uso S2 del Encuentro 30.'),
    ('Qué se pide', 'Que el informe de un mes sin préstamos diga que está vacío, en lugar de mostrar solo «Total 0».'),
    ('Por qué', 'En la sesión S2 la dirección pensó que el sistema había fallado (RF-09, regla de los mensajes del Capítulo 8).'),
    ('Qué no es', 'No es un incumplimiento: el contrato de OP-05 v1.1 no preveía un mensaje para ese caso. Es una mejora.'),
    ('Requisitos afectados', 'RF-09 no cambia de texto; su criterio de aceptación agrega el caso del mes vacío.'),
    ('Contrato y pantalla', 'OP-05 devuelve un resultado correcto, sin filas, con el mensaje ME-14; PT-09 muestra ME-14 y no la tabla.'),
    ('Mensaje nuevo', 'ME-14 (vacío, PT-09): «No hay préstamos registrados en 2026-01. El informe está vacío: no es un error.»'),
    ('Pruebas afectadas', 'P-09 agrega el caso del mes vacío; C-19 de la matriz cambia su esperado; regresión de P-09 y del núcleo.'),
    ('Decisión', 'Aceptada por la dirección, con la conformidad de la bibliotecaria. Se registra en la bitácora.'),
    ('Nueva versión', 'Catálogo v1.2 (criterio de RF-09), contrato de OP-05 v1.2, Tabla 8.6 con ME-14. Las versiones v1.1 se conservan.'),
]

# ------------------------------------------------------------------ regresión (Capítulo 16)
NUCLEO_REGRESION = ['P-01', 'P-03', 'P-07', 'P-11']
# Esperados que cambian con SC-02 (versión con el cambio aprobado): caso → código esperado
ESPERADO_SC02 = {'C-19': 'ME-14'}
REGRESION_IN02 = [  # (qué se vuelve a correr, por qué)
    ('prueba_in02.sh', 'La prueba nueva de la corrección: tiene que pasar en la v2 y fallar en la versión anterior.'),
    ('prueba_http.sh', 'La corrección toca _plantilla.php, que usan todas las pantallas: se recorre E-6a completo.'),
    ('prueba_contratos.php', 'Núcleo: P-01, P-03, P-07 y P-11, más los contratos, aunque las operaciones no cambiaron.'),
    ('Matriz C-01 a C-20', 'Toda la matriz del equipo, con DP: C-20 tiene que pasar y los demás seguir igual.'),
]
REGRESION_SC02 = [
    ('prueba_contratos.php', 'P-09 con el caso del mes vacío (ME-14) y el núcleo.'),
    ('prueba_http.sh', 'PT-09 con un mes con préstamos y otro vacío.'),
    ('Matriz C-01 a C-20', 'C-19 con el esperado nuevo (ME-14); los demás sin cambios.'),
]

# ------------------------------------------------------------------ H5: banco de variantes (reportes de defecto nuevos)
BANCO_H5 = [
    ('V5-1', 'Reporte: «Al devolver EJ-1003, la lista de activos lo sigue mostrando hasta que se cierra la sesión».',
     'Reproducir; si se confirma, la causa estaría en la consulta de OP-04 o en una pantalla que guarda la lista; regresión: P-03, P-04 y C-12.'),
    ('V5-2', 'Reporte: «El informe de mayo cuenta dos veces un préstamo devuelto y vuelto a prestar el mismo día».',
     'Distinguir dos préstamos de un préstamo contado dos veces; revisar la consulta de OP-05 y RI-08; regresión: P-09 y C-16.'),
    ('V5-3', 'Reporte: «Un estudiante con el curso “ 2.º BTI” (con un espacio delante) aparece en un grupo aparte del informe».',
     'Causa en la validación de OA-03 u OA-04 (limpiar espacios) y en datos ya cargados; corrección mínima y regresión: PA-03, PA-04 y P-09.'),
    ('V5-4', 'Reporte: «Con la cuenta de dirección se ve el botón “Prestar” en el menú».',
     'Presentación (menú por rol); comprobar que el servidor rechaza igual (ME-13); regresión: P-11 y la Tabla 11.3.'),
    ('V5-5', 'Reporte: «Después de restaurar un respaldo, la última devolución del día no aparece».',
     'Decidir si es un defecto o el comportamiento esperado (el respaldo es anterior a la devolución); revisar E-11 y E-12; registrar como límite si corresponde.'),
]


# ------------------------------------------------------------------ tablas que salen de los resultados reales
def resumen():
    p = os.path.join(L5, 'resultados_pruebas', 'resumen.json')
    return json.load(open(p, encoding='utf8')) if os.path.exists(p) else None


def _obtenido(r):
    o = r.get('obtenido', {})
    if 'resultado' in o:                                 # caso HTTP
        return o['resultado'].replace('Resultado: ', '')
    partes = [o['codigo']] if o.get('codigo') else []
    if 'sql' in o:
        partes.append('control: %s' % o['sql'])
    if 'filas_cuenta' in o:
        partes.append('%d fila(s)' % o['filas_cuenta'])
    if 'total' in o:
        partes.append('total %s' % o['total'])
    if o.get('filas'):
        for f in o['filas']:
            if f and 'vencido' in f:
                partes.append('%s %s' % (f['ejemplar'], 'vencido' if int(f['vencido']) else 'en plazo'))
            elif f and 'grupo' in f:
                partes.append('%s: %s' % (f['grupo'], f['prestamos']))
            elif f and 'disponibles' in f:
                partes.append('%s: %s disp.' % (f['codigo'], f['disponibles']))
    if 'campos' in o:
        partes.append('campos: %s' % ', '.join(o['campos']))
    return '; '.join(partes) or 'sin mensaje'


def filas_matriz(version):
    res = {c['id']: c for c in resumen()['matriz'][version]['casos']}
    filas = []
    for c in CASOS:
        r = res[c[0]]
        if r['correcto']:
            cond = 'Comprobado: coincide'
        elif c[0] == 'C-20':
            cond = 'Reproducido: IN-02'
        else:
            cond = 'No coincide'
        filas.append([c[0], c[1], c[3], c[10], _obtenido(r), cond])
    return filas


def cobertura():
    filas = []
    for r in X.CATALOGO_V11:
        casos = sorted(set([c[0] for c in CASOS if c[1] == r[0]] + CASOS_EXTRA.get(r[0], [])))
        lim = [c for c in casos if CLASE_DE.get(c) != 'Normal']
        if r[0] in PENDIENTES_ENTORNO:
            nota = 'Pendiente del entorno: ' + PENDIENTES_ENTORNO[r[0]]
        elif not casos:
            nota = 'Hueco: sin caso'
        elif not lim:
            nota = 'Solo casos normales: agregar un límite o un rechazo'
        else:
            nota = 'Cubierto'
        filas.append([r[0], r[4], ', '.join(casos) or '—', str(len(lim)), nota])
    return filas


def entorno_texto():
    e = resumen()['entorno']
    return '%s, PHP %s, SQLite %s (contenedor de construcción, %s)' % (e['sistema'], e['php'], e['sqlite'], e['fecha'])


def filas_permisos(version='v1_lote4'):
    det = resumen()['integracion'][version]['permisos_detalle']
    filas = {}
    for l in det:
        m = __import__('re').match(r'^(CORRECTO|FALLA)\s+((?:OP|OA)-\d\d) con ([^:]+): (.*)$', l)
        if m:
            filas.setdefault(m.group(2), {})[m.group(3)] = ('Permitida' if 'permitida' in m.group(4) else 'ME-13') + \
                ('' if m.group(1) == 'CORRECTO' else ' (FALLA)')
    return [[op, f.get('sin sesión', '—'), f.get('bibliotecaria', '—'), f.get('dirección', '—')] for op, f in sorted(filas.items())]


def filas_regresion(version):
    r = resumen()
    filas = [[p, d['resultado'].replace('Resultado: ', '')] for p, d in r['regresion'][version].items()]
    m = r['matriz'][version]
    filas.append(['Matriz C-01 a C-20 con DP', '%d de %d correctos' % (m['correctos'], m['total'])])
    return filas
