# -*- coding: utf-8 -*-
"""Capítulo 12 — «Préstamos y devoluciones consistentes» (Work §6: secciones 12.1 a 12.4 y práctica «resolver dos
solicitudes incompatibles y explicar la protección elegida»; encuentros 23 y 24).

Implementa OP-01 y OP-02 con los contratos del lote 3 v1.1 (Tabla 9.4) sin cambios. Decisión 6 de Fernando: RI-01 se
explica con sus dos protecciones (operación atómica y restricción de unicidad sobre los préstamos activos de cada
ejemplar); la prueba de carrera se documenta con el entorno en que corrió (Linux, contenedor de construcción); para
Windows se exigen dos conexiones o procesos independientes, no el servidor incorporado de PHP, y los resultados
pendientes se registran sin declararlos aprobados. El libro muestra las protecciones (Códigos 12.1 a 12.4), no las
comprobaciones de OP-01 (comprobar_prestamo), que construye el equipo y están solo en la guía docente.
Capacidades de Work §5.2: C5, C8 y C9 en los dos encuentros."""
import os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'caso'))
import construccion as C
import mbokaja_u4 as MB
X = C.X

NUM = 12
UNIDAD = 'Unidad IV — Construir el prototipo por incrementos'
CAPITULO = 'Capítulo 12'
TITULO = 'Préstamos y devoluciones consistentes'
ENCUENTROS = (23, 24)
SECCIONES = ['12.1 Precondiciones y reglas de la operación de préstamo',
             '12.2 Doble envío, disponibilidad y operaciones atómicas',
             '12.3 Devolución, estado del ejemplar y conservación de historial',
             '12.4 Fallos previsibles y comprobación de resultados']
PRACTICA_WORK = 'resolver dos solicitudes incompatibles y explicar la protección elegida'

ROTULO_CAPACIDAD = ('Capacidades propuestas para el programa institucional (C5, C8 y C9 en los Encuentros 23 y 24; no '
                    'son capacidades oficiales del MEC)')
CAPACIDAD = ('C5. Justifica el modelo de información y sus reglas de integridad.\n'
             'C8. Integra un prototipo funcional con persistencia.\n'
             'C9. Verifica y mejora la solución a partir de evidencia.')
TEMA = ('El préstamo como operación con precondiciones y reglas, en el orden del caso de uso. Doble envío, pedidos '
        'simultáneos y las dos protecciones de RI-01: operación atómica y restricción de unicidad. Devolución única que '
        'conserva el historial. Fallos previsibles y comprobación del estado final con una consulta.')
INDICADORES = [
    'Construye el préstamo comprobando, en el orden del contrato, el permiso, el lector, el máximo de su tipo y el ejemplar.',
    'Explica las dos protecciones de RI-01 y por qué hacen falta las dos.',
    'Evita el doble envío del formulario y prueba la simultaneidad con procesos independientes, registrando el entorno.',
    'Construye la devolución única, que cierra el préstamo correcto y conserva el historial.',
    'Comprueba con una consulta que, después de cada prueba, no quedó ningún dato a medias ni dos préstamos activos de un ejemplar.',
]
TIEMPO = ('Dos encuentros de 5 HC (23 y 24 de la secuencia anual), cada uno con 1 HC de diseño, 3 de práctica y 1 de '
          'verificación.')

APERTURA = [
    'El préstamo es la operación central del sistema y la más delicada. Tiene que respetar todas las reglas a la vez: el '
    'lector activo, el máximo de su tipo, el ejemplar disponible. Y tiene que respetarlas también cuando dos pedidos '
    'llegan al mismo tiempo, o cuando alguien pulsa dos veces «Prestar» porque la pantalla tardó.',
    'La devolución parece simple, pero tiene su trampa: cerrar el préstamo correcto, una sola vez, sin borrar nada. Al '
    'terminar el capítulo, el circuito de préstamo y devolución funciona y se puede demostrar con pruebas.',
]
ARTICULACION = [
    'Con el Capítulo 5: el orden de las comprobaciones es el de CU-01 y CU-02, con sus flujos alternativos.',
    'Con el Capítulo 7: RI-01 a RI-04, RI-07 y RI-08 se hacen cumplir en la operación y en la base.',
    'Con el Capítulo 9: los contratos de OP-01 y OP-02 (Tabla 9.4) se implementan tal como están; el Capítulo 9 anunció '
    'que acá se programa la protección de RI-01 ante pedidos simultáneos.',
]

AVISO_ENTORNO = C.AVISO_ENTORNO

# ------------------------------------------------------------------ encuentro 23
E23_TITULO = 'Encuentro 23 — El préstamo y sus protecciones'

S121 = ('12.1 Precondiciones y reglas de la operación de préstamo', [
    'El contrato de OP-01 (Capítulo 9) ya dice qué tiene que pasar. Implementarlo es comprobar cada precondición y cada '
    'regla, en el orden del caso de uso CU-01, y responder el mensaje que corresponde al primer problema que aparece. Si '
    'no hay ninguno, se registra el préstamo.',
    'El orden importa. El permiso va primero: sin él, no se consulta nada. Después, el lector (flujos 4a y 4b de CU-01) '
    'y, al final, el ejemplar (flujo 5a). La Tabla 12.1 es la especificación de las comprobaciones que construye tu '
    'equipo, en la función comprobar_prestamo() de la base.',
    'El máximo no se escribe en el código: se lee de Parámetro según el tipo del lector, dos para estudiantes y cinco para '
    'docentes (RN-02 v1.1, SC-01). El vencimiento se calcula al prestar con el plazo vigente y se guarda (RI-07). Si el '
    'lector es estudiante, se guarda su curso de ese día (RI-08).',
])
CONTRATOS_S121 = ['OP-01']
TABLA_121_ROTULO = 'Tabla 12.1 — Comprobaciones de OP-01, en orden'
TABLA_121 = (['Paso', 'Qué se comprueba', 'Regla o flujo', 'Si no se cumple', 'Prueba'],
             [['1', 'La cuenta tiene rol de bibliotecaria', 'RNF-02', 'ME-13', 'P-11'],
              ['2', 'Están los dos códigos y la fecha es válida', 'Validación', 'MV-01, MV-08', 'PA de validación'],
              ['3', 'El lector existe', 'Validación', 'MV-05', '—'],
              ['4', 'El lector está activo', 'RI-03; CU-01, 4a', 'ME-01', 'P-05'],
              ['5', 'Sus préstamos activos no llegan al máximo de su tipo', 'RI-02; CU-01, 4b', 'ME-02 con el máximo', 'P-06a, P-06b'],
              ['6', 'El ejemplar existe', 'CU-01', 'ME-05', '—'],
              ['7', 'El ejemplar está activo', 'RI-03', 'MV-06', '—'],
              ['8', 'El ejemplar no tiene un préstamo activo', 'RI-01; CU-01, 5a', 'ME-03 con el vencimiento', 'P-07'],
              ['9', 'Se registra: vencimiento y curso al prestar', 'RI-07, RI-08', '— (ME-04)', 'P-01, P-02']])
EJ121 = ('Ejemplo resuelto 12.1: el máximo según el tipo de lector', [
    'Consigna: decidir qué responde OP-01 cuando el lector ya tiene préstamos activos (situación de prueba).',
    'LE-0123 es estudiante y tiene dos préstamos activos. Un tercero responde: «%s»' % C.con_datos('ME-02', 2, 'estudiantes'),
    'LE-0201 es docente y tiene dos préstamos activos. Un tercero se registra: su máximo es cinco. El sexto respondería: '
    '«%s»' % C.con_datos('ME-02', 5, 'docentes'),
    'Si la dirección cambiara el máximo de los docentes, se cambia el valor en Parámetro y ninguna línea de código.',
])
EJ122 = ('Ejemplo resuelto 12.2: lo que guarda un préstamo', [
    'Consigna: LE-0123 (estudiante de 2.º BTI) retira EJ-0457 el 2 de marzo. ¿Qué queda guardado?',
    'El préstamo con el ejemplar EJ-0457, el lector LE-0123, la fecha de salida 2026-03-02 y el vencimiento 2026-03-09, '
    'con el plazo de 7 días de ese día (RI-07, P-02). El curso al prestar: 2.º BTI (RI-08). La fecha de devolución, '
    'vacía.',
    'La bibliotecaria ve: «%s» Si después el plazo cambia, este vencimiento no cambia: ya está guardado.'
    % C.con_datos('ME-04', '09/03'),
])

S122 = ('12.2 Doble envío, disponibilidad y operaciones atómicas', [
    'En Mbokaja, un voluntario pulsó dos veces «Guardar» porque la pantalla no cambió, y quedaron dos préstamos iguales '
    '(OBS-4). El sistema lo evita de dos maneras en la pantalla: el botón se desactiva y dice «Guardando…» mientras se '
    'envía (ME-11), y después de registrar, la página redirige, así que recargarla no vuelve a enviar el pedido (patrón '
    'POST-redirección-GET). Pero eso no alcanza: dos computadoras pueden enviar a la vez el mismo ejemplar (Figura 12.1).',
    'RI-01 tiene dos protecciones. La primera está en las reglas de negocio: la comprobación y el registro se hacen en una '
    'sola operación atómica (Código 12.1). BEGIN IMMEDIATE reserva la base para escribir: si llega otro pedido, espera a '
    'que este termine. Así, el segundo pedido comprueba cuando el primero ya registró, y encuentra el ejemplar prestado.',
    'La segunda está en la persistencia: un índice único sobre los préstamos sin fecha de devolución (Código 12.2). '
    'Aunque una operación tuviera un error, o alguien escribiera en la base sin pasar por las reglas, la base no admite un '
    'segundo préstamo activo del mismo ejemplar. Con las dos, el sistema no depende de una sola línea de código.',
])
LEAD_FIG121 = ('La Figura 12.1 muestra dos pedidos que llegan casi a la vez por EJ-0457 y dónde actúa cada protección.')
EPI_FIG121 = 'Figura 12.1 — Dos pedidos simultáneos del mismo ejemplar y las dos protecciones de RI-01.'
CODIGOS_S122 = ['Código 12.1', 'Código 12.2']
EXPLICA = {
    'Código 12.1': 'Todo lo que está entre BEGIN IMMEDIATE y COMMIT ocurre como una sola cosa: o se hace todo o no se '
                   'hace nada. Si la comprobación encuentra un problema, ROLLBACK deshace y se responde el error. Las '
                   'comprobaciones de comprobar_prestamo() las escribe tu equipo con la Tabla 12.1.',
    'Código 12.2': 'El índice es parcial: solo cuenta los préstamos con fecha_devolucion vacía. Un ejemplar puede tener '
                   'muchos préstamos en su historia, pero uno solo activo.',
}
RONDAS_ROTULO = 'Tabla 12.2 — Prueba de pedidos simultáneos: resultado y entorno'


def tabla_rondas():
    """Lee el resultado de prueba_carrera.php (build/reproducir.py) con el entorno en que corrió."""
    p = os.path.join(C.L4, 'resultados_pruebas', 'referencia_docente__prueba_carrera.txt')
    t = open(p, encoding='utf8').read()
    n = lambda clave, cod: sum(int(a) for a, b, c in re.findall(r'(\d+) × (RI-0[12][^:]*): (ME-\d\d)', t)
                               if b.strip() == clave and c == cod)
    rondas = len(re.findall(r'CORRECTO Ronda \d+, P-07', t))
    entorno = re.search(r'^Entorno: (Linux[^\n]*)$', t, re.M).group(1)
    filas = [['P-07 (RI-01)', '12 procesos piden el mismo ejemplar a la vez',
              '%d registrados (uno por ronda), %d rechazos ME-03' % (n('RI-01', 'ME-04'), n('RI-01', 'ME-03')),
              'Nunca dos préstamos activos'],
             ['RI-02 estudiante', '8 pedidos a la vez para un lector con máximo 2',
              '%d registrados, %d rechazos ME-02' % (n('RI-02 estudiante', 'ME-04'), n('RI-02 estudiante', 'ME-02')),
              'Nunca más de 2 activos'],
             ['RI-02 docente', '8 pedidos a la vez para un lector con máximo 5',
              '%d registrados, %d rechazos ME-02' % (n('RI-02 docente', 'ME-04'), n('RI-02 docente', 'ME-02')),
              'Nunca más de 5 activos'],
             ['Entorno', 'Procesos independientes, cada uno con su conexión; %d rondas' % rondas, entorno,
              'No es una computadora escolar'],
             ['Windows', 'Protocolo de la guía docente', 'Pendiente', 'No se declara aprobado']]
    return (['Caso', 'Cómo se probó', 'Resultado (todas las rondas)', 'Qué se comprobó'], filas)


TABLA_122 = tabla_rondas()
PROTOCOLO = ('Cómo se prueba la simultaneidad', C.PROTOCOLO_CONCURRENCIA)

ACT_E23 = [
    ('Ejercitá', [
        'Ordená las comprobaciones de OP-01 y escribí qué mensaje responde cada caso:\n'
        '(a) LE-0125, que está inactivo, pide EJ-0458; (b) LE-0124 pide EJ-0459, dado de baja; (c) LE-0124 pide EJ-0457, '
        'que ya está prestado.',
    ]),
    ('Resolvé', [
        'Construí comprobar_prestamo() y registrar_prestamo() en la base de tu equipo, con la Tabla 12.1 y el Código 12.1. '
        'Agregá la pantalla PT-05 con el formulario del Capítulo 8. Ejecutá P-01, P-02, P-05, P-06a, P-06b y P-07.',
        'Registrá en la bitácora el resultado de cada prueba y el entorno en que la ejecutaste.',
    ]),
    ('Pensá y decidí', [
        'Un compañero propone quitar el índice único «porque la operación ya comprueba RI-01». Explicá qué caso dejaría de '
        'estar protegido.',
    ]),
]

# ------------------------------------------------------------------ encuentro 24
E24_TITULO = 'Encuentro 24 — Devolución, historial y fallos previsibles'

S123 = ('12.3 Devolución, estado del ejemplar y conservación de historial', [
    'Devolver es completar la fecha de devolución del préstamo activo del ejemplar (RI-04). No se borra el préstamo: pasa '
    'al historial. Y el ejemplar vuelve a estar disponible sin que haya que cambiar nada en él, porque «disponible» es un '
    'dato derivado: un ejemplar activo sin préstamo activo.',
    'La devolución es única. Se hace con una sola sentencia que cierra el préstamo activo de ese ejemplar (Código 12.3). '
    'Si el ejemplar no tenía un préstamo activo, la sentencia no cambia ninguna fila y la operación responde ME-06. Si dos '
    'pedidos de devolución llegan a la vez, solo uno encuentra el préstamo abierto.',
    'La base también protege el historial: no deja borrar un préstamo, no deja cambiar sus datos fijos (ejemplar, lector, '
    'fechas de salida y vencimiento) y no deja cambiar una fecha de devolución ya completada.',
])
CONTRATOS_S123 = ['OP-02']
CODIGOS_S123 = ['Código 12.3']
EXPLICA['Código 12.3'] = ('La condición fecha_devolucion IS NULL elige el préstamo activo, y solo ese. Después, la '
                          'operación mira cuántas filas cambiaron: una, ME-07; ninguna, ME-06. Las demás comprobaciones '
                          'de OP-02 (permiso, ejemplar existente, fecha) las escribe tu equipo con su contrato.')
EJ123 = ('Ejemplo resuelto 12.3: devolver dos veces el mismo ejemplar', [
    'Consigna: EJ-0457 vuelve el 9 de marzo. Al rato, otra persona escanea la misma etiqueta y pide devolverlo otra vez.',
    'Primera devolución: «%s»' % C.MENSAJES_PHP['ME-07'],
    'Segunda: «%s»' % C.MENSAJES_PHP['ME-06'],
    'Comprobación (P-03): el préstamo tiene la fecha 2026-03-09 y sigue en el historial; EJ-0457 vuelve a contarse como '
    'disponible; no hay ningún préstamo nuevo ni ninguno borrado.',
])

S124 = ('12.4 Fallos previsibles y comprobación de resultados', [
    'Algunos fallos se pueden prever: la base ocupada por otra operación, un corte en medio del registro, un formulario '
    'abierto desde hace horas, una fecha imposible. Para cada uno, el sistema tiene que dejar los datos como estaban y '
    'decir qué pasó (Tabla 12.3). Lo que no puede pasar es un préstamo a medias.',
    'Si algo falla entre BEGIN IMMEDIATE y COMMIT, ROLLBACK deshace todo (Código 12.4). Si lo que falló fue la segunda '
    'barrera, porque la base rechazó un segundo préstamo activo, la operación responde ME-03 como si lo hubiera detectado '
    'la comprobación.',
    'Un resultado se comprueba en los datos, no solo en el mensaje. Después de cada prueba, una consulta revisa que no '
    'haya ejemplares con dos préstamos activos, que ningún lector supere su máximo y que el historial tenga los préstamos '
    'que tenía antes (Ejemplo resuelto 12.4).',
])
CODIGOS_S124 = ['Código 12.4']
EXPLICA['Código 12.4'] = ('Cualquier error de la base durante la operación termina acá. Primero se deshace todo; '
                          'después se mira qué falló. Si fue el índice único (UNIQUE), se responde ME-03 con el '
                          'vencimiento del préstamo que ganó. Si fue otra cosa, el error sigue y no se informa un éxito falso.')
TABLA_123_ROTULO = 'Tabla 12.3 — Fallos previsibles del préstamo y la devolución'
TABLA_123 = (['Fallo', 'Qué hace el sistema', 'Qué ve la bibliotecaria', 'Cómo se comprueba'],
             [['Doble clic en «Prestar»', 'Botón desactivado; un solo pedido', 'Guardando… y ME-04', 'Un solo préstamo nuevo'],
              ['Recargar la página después de prestar', 'Redirección: no se reenvía', 'La pantalla con el aviso', 'Ningún préstamo nuevo'],
              ['Dos computadoras, el mismo ejemplar', 'Operación atómica e índice único', 'ME-04 en una, ME-03 en la otra', 'P-07: un préstamo activo'],
              ['La base está ocupada', 'No espera para siempre; no registra', 'MV-09', 'Ningún dato cambió'],
              ['Error en medio del registro', 'ROLLBACK', 'El error, nunca un éxito falso', 'Ningún préstamo a medias'],
              ['Formulario abierto desde hace horas', 'Rechaza la ficha vencida', 'MV-12', 'Ningún dato cambió'],
              ['Devolución con fecha anterior a la salida', 'La base la rechaza', 'MV-10', 'El préstamo sigue activo']])
EJ124 = ('Ejemplo resuelto 12.4: comprobar el estado final', [
    'Consigna: después de ejecutar P-07, demostrar en los datos que no quedó ningún ejemplar con dos préstamos activos.',
    'Consulta de control: SELECT ejemplar_id, COUNT(*) FROM prestamos WHERE fecha_devolucion IS NULL GROUP BY '
    'ejemplar_id HAVING COUNT(*) > 1. Resultado esperado: ninguna fila.',
    'Se anota en la bitácora: la prueba, el resultado esperado, el obtenido y el entorno. Si la consulta devolviera una '
    'fila, no se borra a mano: se registra como incidencia y se busca la causa.',
])
ACT_E24 = [
    ('Ejercitá', [
        'Para cada caso, escribí qué responde OP-02 y cómo quedan los datos:\n'
        '(a) devolver EJ-0601 sin préstamo activo; (b) devolver EJ-9999; (c) devolver EJ-0457 prestado el 2 de marzo, con '
        'fecha 1 de marzo.',
    ]),
    ('Resolvé', [
        'Construí registrar_devolucion() en la base de tu equipo, con su contrato y el Código 12.3. Agregá PT-06 y ejecutá '
        'P-03. Completá la parte de P-10 que quedó pendiente en el Encuentro 22.',
        'Aplicá la consulta de control del Ejemplo resuelto 12.4 después de tus pruebas y anotá el resultado.',
    ]),
    ('Pensá y decidí', [
        'La bibliotecaria pide poder «anular» un préstamo cargado por error. Proponé cómo hacerlo sin borrar historial y '
        'qué requisito nuevo implicaría.',
    ]),
    ('Desafío', [
        'Escribí una fila más para la Tabla 12.3 con un fallo previsible que no esté, y la prueba que lo comprueba.',
    ]),
]

# ------------------------------------------------------------------ práctica
PRACTICA_TITULO = 'Práctica 12 — Dos voluntarios, el mismo libro y un libro dañado'
PRACTICA_INTRO = [
    'En Mbokaja, un miércoles, dos voluntarios cargaron al mismo tiempo, en dos computadoras, el mismo libro para dos '
    'lectores distintos (MS-6). Ese mismo día volvió un libro con hojas arrancadas (MS-1), y la norma dice que se repone '
    'con otro igual (M-N5). Usá el contrato de devolución que escribiste en la Práctica 9.',
    'Esta práctica se resuelve en papel: se explica, se diseña la prueba y se decide. No hace falta ejecutar nada en la '
    'computadora de Mbokaja.',
]
NIVELES = [
    ('Nivel 1 — Guiado', [
        'Explicá qué pasa con los dos pedidos de MS-6 en el sistema: cuál se registra, qué ve el otro voluntario y qué '
        'protección actúa en cada momento. Usá la Figura 12.1.',
        'Escribí el mensaje que ve el segundo voluntario, con la regla de los mensajes del Capítulo 8.',
    ]),
    ('Nivel 2 — Intermedio', [
        'Diseñá la prueba de MS-6 para la computadora de Mbokaja: cuántos procesos, con qué datos, qué resultado esperás y '
        'qué consulta de control usás. Explicá por qué no sirve abrir dos pestañas del navegador contra el servidor '
        'incorporado de PHP.',
        'Escribí cómo registrarías el resultado si la prueba no se pudo ejecutar en esa computadora.',
    ]),
    ('Nivel 3 — Ampliación', [
        'Para el libro dañado de MS-1, decidí qué operaciones se hacen y en qué orden: la devolución, la baja del ejemplar '
        'dañado y el alta del que lo repone. Ningún dato con historia se borra.',
        'Decidí si esas operaciones tienen que ser una sola operación atómica o pueden ser tres, y explicá qué pasaría si '
        'el sistema fallara entre la segunda y la tercera.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: se registra un solo préstamo de MB-104; el otro voluntario recibe un mensaje '
                    'útil; la prueba usa procesos independientes y se anota con su entorno, o como pendiente; el libro '
                    'dañado queda en el historial, inactivo, y el que lo repone es un ejemplar nuevo.')

REPASO = ('Para repasar', [
    'El préstamo comprueba, en el orden del contrato, el permiso, el lector, el máximo de su tipo y el ejemplar.',
    'El botón desactivado y la redirección evitan el doble envío; no alcanzan contra dos computadoras.',
    'RI-01 tiene dos protecciones: la operación atómica y el índice único sobre los préstamos activos.',
    'La devolución es única, cierra el préstamo correcto y no borra nada.',
    'Un resultado se comprueba en los datos, y cada prueba se registra con el entorno en que corrió.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, los Encuentros 23 y 24 pasan a ser el 17 y el 18, sin cambios: el préstamo, la '
    'prevención de duplicados, la devolución y el historial se conservan completos.',
    'Si aun así falta tiempo, no se omiten: la Tabla 12.1, las dos protecciones de RI-01 con P-07 y la devolución única '
    'con P-03. Pasan a lectura domiciliaria: el Ejemplo resuelto 12.4 y el nivel 3 de la Práctica 12.',
])

# ------------------------------------------------------------------ evaluación
EVAL_ID = 'ADS3-L4-C12'
EVAL_TITULO = 'Evaluación del Capítulo 12'
EVAL_TEXTO_BASE = ('Texto base — Préstamo de calculadoras científicas (situación de evaluación, ficticia)', [
    'CA-1 Cada calculadora se presta a un solo estudiante por vez.',
    'CA-2 Un estudiante puede tener, como máximo, una calculadora.',
    'CA-3 Las calculadoras se prestan desde dos mesas a la vez, en los exámenes.',
    'CA-4 La devolución se anota y el préstamo queda en el historial.',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', 'Por CA-3, dos mesas pueden pedir la misma calculadora a la vez. ¿Qué protege CA-1 en ese caso?',
     ['Comprobar y registrar en una operación atómica, y una restricción única en la base.',
      'Desactivar el botón después del primer clic.', 'Pedir a las mesas que se avisen.', 'Revisar el historial al final del día.']),
    ('mc', '¿En qué orden se comprueba un préstamo?',
     ['Permiso, estudiante, máximo y calculadora.', 'Calculadora, permiso y estudiante.', 'Máximo, calculadora y permiso.',
      'Da igual el orden.']),
    ('mc', 'Se pide devolver una calculadora que no tiene préstamo activo. ¿Qué pasa?',
     ['No se cambia nada y se informa que no había un préstamo activo.', 'Se borra el último préstamo.',
      'Se registra una devolución vacía.', 'Se presta de nuevo.']),
    ('mc', 'Después de una prueba de pedidos simultáneos, ¿cómo se comprueba el resultado?',
     ['Con una consulta que busca calculadoras con más de un préstamo activo.', 'Mirando solo el último mensaje.',
      'Preguntando a las mesas.', 'Reiniciando el sistema.']),
    ('vf', 'Si el botón se desactiva al pulsarlo, ya no puede haber dos préstamos de la misma calculadora.',
     False, 'Falso. Evita el doble clic en una pantalla, no dos mesas a la vez (CA-3).'),
    ('vf', 'Devolver una calculadora completa la fecha de devolución y no borra el préstamo.',
     True, 'Verdadero (CA-4).'),
    ('vf', 'Una prueba de pedidos simultáneos que solo se ejecutó en otra computadora vale como aprobada para la del colegio.',
     False, 'Falso. Vale para el entorno en que corrió; en la del colegio queda pendiente hasta probarla.'),
    ('ab', 'Escribí la tabla de comprobaciones del préstamo de una calculadora: paso, qué se comprueba, fuente (CA-…) y '
           'mensaje si no se cumple.',
     'Permiso de quien registra; estudiante existe y no tiene ya una calculadora (CA-2); calculadora existe; '
     'calculadora sin préstamo activo (CA-1); registrar. Un punto por el orden, uno por las fuentes, uno por los '
     'mensajes y uno por el registro final.', 4),
    ('ab', 'Explicá las dos protecciones que usarías para CA-1 y qué caso cubre cada una.',
     'Operación atómica: el segundo pedido comprueba después de que el primero registró. Restricción única en la base: '
     'cubre un error de la operación o un dato escrito sin pasar por ella. Dos puntos por cada protección bien explicada.', 4),
]
EVAL_PUNTAJE = 'Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno).'
