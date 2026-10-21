# -*- coding: utf-8 -*-
"""Capítulo 13 — «Información útil e integración» (Work §6: secciones 13.1 a 13.4 y cierre «Revisión de unidad IV:
circuito funcional completo; H4»; encuentros 25 y 26).

OP-03 pública, OP-04 con fecha de referencia y OP-05 para bibliotecaria y dirección (PT-09 en la zona compartida del
lote 3 v1.1, ME-13 en el servidor). El informe mensual se construye en el Encuentro 25 (Tabla 11.1) y se trata en 13.2
como consulta de un período de referencia definido; 13.3 integra los módulos y los revisa contra el alcance mínimo de
Work §7.2. Decisión 5 de Fernando: la Práctica 13 es un complemento editorial breve e integrador, ubicada en el
Encuentro 25 o como actividad complementaria, con datos nuevos (MI-01 a MI-07) que exigen comprobar una integración o
una incidencia; no reduce las 2 HC de evaluación del Encuentro 26. H4: rúbrica de C7 a C9 con cuatro niveles, 60/40
como propuesta editorial, ausencia de evidencia registrada aparte y variante individual del banco de la guía.
Capacidades de Work §5.2: C3 y C8 (Encuentro 25) y C7 a C9 (Encuentro 26, H4). El libro no publica resuelto el
informe mensual (OP-05): su consulta de referencia está solo en la guía docente."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'caso'))
import construccion as C
import mbokaja_u4 as MB
X = C.X

NUM = 13
UNIDAD = 'Unidad IV — Construir el prototipo por incrementos'
CAPITULO = 'Capítulo 13'
TITULO = 'Información útil e integración'
ENCUENTROS = (25, 26)
SECCIONES = ['13.1 Búsqueda de ejemplares disponibles y préstamos activos',
             '13.2 Vencimientos y fecha de referencia',
             '13.3 Integración de módulos y revisión del alcance mínimo',
             '13.4 Demostración del incremento y registro de pendientes']
REVISION_WORK = 'Revisión de unidad IV: circuito funcional completo; H4'
PRACTICA_WORK = 'complemento editorial: comprobar la integración con el registro de una semana e identificar incidencias'

ROTULO_CAPACIDAD = ('Capacidades propuestas para el programa institucional (C3 y C8 en el Encuentro 25; en el H4, C7 a '
                    'C9; no son capacidades oficiales del MEC)')
CAPACIDAD = ('C3. Especifica y prioriza requisitos verificables.\n'
             'C8. Integra un prototipo funcional con persistencia.\n'
             'En el H4 se evalúan juntas C7 a C9.')
TEMA = ('Consulta pública de disponibilidad como dato derivado, sin datos de lectores, y préstamos activos para la '
        'bibliotecaria. Vencimientos calculados respecto de una fecha de referencia definida e informe mensual por curso '
        'al prestar. Integración de los módulos y revisión contra el alcance mínimo. Demostración del incremento, lista '
        'de incidencias y revisión de la Unidad IV (H4).')
INDICADORES = [
    'Construye la consulta pública de disponibilidad sin datos de lectores y la lista de préstamos activos para la bibliotecaria.',
    'Calcula los vencidos respecto de una fecha de referencia escrita, para que el resultado se pueda comprobar.',
    'Construye el informe mensual por curso al prestar y comprueba que la suma de los grupos coincide con el total.',
    'Integra los módulos y revisa el prototipo contra el alcance mínimo, con la prueba de cada función.',
    'Demuestra el circuito completo, registra las incidencias con su gravedad y destino, y resuelve individualmente una variante.',
]
TIEMPO = ('Dos encuentros de 5 HC (25 y 26 de la secuencia anual). Encuentro 25: 1 HC de diseño, 3 de práctica y 1 de '
          'verificación. Encuentro 26: 2 HC de integración, 1 de demostración y 2 de evaluación (H4).')

APERTURA = [
    'El sistema ya registra. Ahora tiene que informar: qué hay disponible para el que busca un libro, quién tiene cada '
    'ejemplar, qué está vencido y cuánto se leyó en el mes. Es la información que pidieron la bibliotecaria y la dirección '
    'desde el relevamiento.',
    'Al final del capítulo, el equipo junta todo lo construido en la Unidad IV, lo revisa contra el alcance mínimo, lo '
    'demuestra y registra lo que todavía falla. Esa demostración y esa lista de incidencias son el hito H4.',
]
ARTICULACION = [
    'Con el Capítulo 4: las consultas cumplen RF-07, RF-08 y RF-09, con sus criterios de aceptación (C3).',
    'Con el Capítulo 7: «disponible» es un dato derivado, y el informe se agrupa por el curso al prestar (RI-08).',
    'Con la Unidad V: la lista de incidencias del H4 es el punto de partida de la matriz de pruebas y de las '
    'correcciones.',
]

AVISO_ENTORNO = C.AVISO_ENTORNO

# ------------------------------------------------------------------ encuentro 25
E25_TITULO = 'Encuentro 25 — Consultas, vencimientos e informe'

S131 = ('13.1 Búsqueda de ejemplares disponibles y préstamos activos', [
    'La consulta pública (OP-03) es la única operación que no pide sesión. Por eso tiene una regla estricta: no devuelve '
    'ningún dato de lectores (RNF-03). Muestra cada obra que coincide con lo que se escribió, cuántos ejemplares tiene y '
    'cuántos están disponibles (Código 13.1).',
    'La cantidad de disponibles no se guarda en ningún lado: se cuenta en el momento, como los ejemplares activos sin '
    'préstamo activo. Si se guardara, habría que actualizarla en cada préstamo y en cada devolución, y tarde o temprano '
    'no coincidiría. Es el dato derivado del Capítulo 7.',
    'La lista de préstamos activos (OP-04) sí muestra quién tiene cada ejemplar, porque es para la bibliotecaria: está en '
    'su zona y la operación comprueba el rol (ME-13). Es lo que pidió el encargado de Mbokaja desde el principio: saber '
    'quién tiene cada libro.',
])
CODIGOS_S131 = ['Código 13.1']
EXPLICA = {
    'Código 13.1': 'COUNT(e.id) cuenta los ejemplares activos de la obra y COUNT(p.id), los que tienen un préstamo sin '
                   'devolver; la resta son los disponibles. La consulta no nombra ninguna columna de lectores. Los signos '
                   '% y _ que escriba la persona se buscan como texto, no como comodines.',
}
EJ131 = ('Ejemplo resuelto 13.1: buscar «arroyo»', [
    'Consigna: con los datos iniciales y EJ-0457 prestado, escribir qué muestra la consulta pública para «arroyo».',
    '«Cuentos del arroyo Arapoty»: tres ejemplares activos (EJ-0457, EJ-0458 y EJ-0512; EJ-0459 está inactivo y no se '
    'cuenta), dos disponibles.',
    '«El arroyo y la escuela»: un ejemplar, EJ-0601, disponible. Si estuviera prestado: «%s»' % C.MENSAJES_PHP['ME-09'],
    'Para «zzz»: «%s» En ningún caso aparece el nombre ni el código de un lector (P-12).' % C.MENSAJES_PHP['ME-08'],
])

S132 = ('13.2 Vencimientos y fecha de referencia', [
    'Un préstamo está vencido si su vencimiento es anterior a la fecha de referencia. Si el cálculo usara siempre «hoy», '
    'el resultado cambiaría cada día y no se podría comprobar: la misma prueba daría otra cosa mañana. Por eso OP-04 '
    'recibe la fecha de referencia como dato de entrada, escrita, y la pantalla la muestra (Figura 13.1 y Código 13.2).',
    'El vencimiento ya está guardado en el préstamo (RI-07): la consulta solo lo compara. Un préstamo que vence el mismo '
    'día de la fecha de referencia todavía no está vencido.',
    'El informe mensual (OP-05) es otra consulta con un período definido: el mes. Agrupa los préstamos del mes por el '
    'curso que tenía el estudiante al prestar (RI-08), agrega la fila «Docentes» y cuenta el total de nuevo, sin sumar a '
    'mano. Lo pueden pedir la bibliotecaria y la dirección: PT-09 está en la zona compartida, y la operación comprueba el '
    'rol en el servidor.',
])
LEAD_FIG131 = ('La Figura 13.1 muestra tres préstamos activos y una fecha de referencia. Solo el que vence antes de esa '
               'fecha se marca como vencido.')
EPI_FIG131 = 'Figura 13.1 — Préstamos activos y vencidos respecto de la fecha de referencia 15/03.'
CODIGOS_S132 = ['Código 13.2']
EXPLICA['Código 13.2'] = ('El signo «?» de la comparación recibe la fecha de referencia. La marca «vencido» la calcula '
                          'la consulta; la pantalla solo la muestra. Las demás partes de OP-04 (permiso, fecha válida, '
                          'lista vacía con ME-10) las escribe tu equipo con su contrato.')
TABLA_131_ROTULO = 'Tabla 13.1 — Préstamos activos al 15/03 (los de la Figura 13.1)'
TABLA_131 = (['Ejemplar', 'Salida', 'Vencimiento', 'Fecha de referencia', 'Marca'],
             [['EJ-0458', '05/03', '12/03', '15/03', 'vencido'],
              ['EJ-0512', '10/03', '17/03', '15/03', 'en plazo'],
              ['EJ-0601', '14/03', '21/03', '15/03', 'en plazo']])
EJ132 = ('Ejemplo resuelto 13.2: comprobar el informe de un mes', [
    'Consigna: la dirección pide el informe de marzo. ¿Cómo se comprueba que es correcto, sin rehacerlo a mano?',
    'Se comprueban tres cosas (P-09). La suma de los grupos coincide con el total, que la operación contó de nuevo. Los '
    'préstamos a docentes están en la fila «Docentes», no en un grupo «sin curso». Y si un estudiante cambió de curso '
    'después, sus préstamos de marzo siguen en el curso que tenía (RI-08).',
    'El formato es el de la Tabla 7.8: un grupo por curso, la fila «Docentes» y el total.',
])
ACT_E25 = [
    ('Ejercitá', [
        'Con la Figura 13.1, decidí la marca de cada préstamo si la fecha de referencia fuera 12/03 y si fuera 22/03.',
    ]),
    ('Resolvé', [
        'Construí OP-03, OP-04 y OP-05 en la base de tu equipo, con sus contratos y los Códigos 13.1 y 13.2. Agregá PT-02, '
        'PT-07 y PT-09. Ejecutá P-04, P-08, P-09 y P-12.',
        'Pedí el informe (PT-09) con la cuenta de dirección y con la de bibliotecaria; después intentá entrar a PT-07 con '
        'la cuenta de dirección. Anotá qué responde el sistema en cada caso.',
    ]),
    ('Pensá y decidí', [
        'Un compañero propone agregar a la consulta pública el nombre de quien tiene el libro, «para que el lector sepa a '
        'quién pedírselo». Explicá qué requisito lo impide y por qué.',
    ]),
]

# ------------------------------------------------------------------ práctica (complemento editorial, Encuentro 25)
PRACTICA_TITULO = 'Práctica 13 — Una semana en Mbokaja: integración e incidencias (complemento editorial)'
PRACTICA_INTRO = [
    'Esta práctica no figura en el índice de Work: es un complemento editorial breve, para el Encuentro 25 o como '
    'actividad complementaria. No reemplaza ni reduce el H4. El sistema de prueba de Mbokaja se usó una semana, con plazo '
    'de siete días (M-N1). El encargado anotó lo que pasó (MI-01 a MI-07). Algunos resultados del sistema no coinciden '
    'con lo que pasó: hay que descubrir por qué.',
]
NIVELES = [
    ('Nivel 1 — Guiado', [
        'A partir de MI-01 a MI-04, escribí cuál debería ser el estado del sistema el viernes 10: préstamos activos y '
        'disponibles del título de MB-104.',
        'Compará con MI-05. Explicá la diferencia: ¿falla una operación o faltó registrar algo? Decidí cómo se corrige sin '
        'borrar datos.',
    ]),
    ('Nivel 2 — Intermedio', [
        'Calculá el vencimiento de MB-104 (MI-01, M-N1) y decidí si, con fecha de referencia 13 de abril, tiene que '
        'aparecer como vencido. Compará con MI-07.',
        'Si el sistema se equivoca, registrá la incidencia: pantalla u operación, descripción, gravedad y la prueba que la '
        'reproduce.',
    ]),
    ('Nivel 3 — Ampliación', [
        'Comprobá MI-06: ¿cuántos préstamos de abril tiene que contar el informe y por qué grupo? Decidí si hay una '
        'incidencia o si coincide.',
        'Armá la lista de incidencias de la semana con el formato de la Tabla 13.3 y proponé, para cada una, la prueba de '
        'regresión que la Unidad V tendría que ejecutar después de corregirla.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: la diferencia de MI-05 se explica por un registro que faltó y se corrige con una '
                    'devolución, no borrando; el vencimiento de MB-104 se calcula con el plazo y la marca de MI-07 se '
                    'compara con la regla; cada incidencia tiene gravedad, destino y una prueba que la reproduce; lo que '
                    'coincide también se anota.')

# ------------------------------------------------------------------ encuentro 26
E26_TITULO = 'Encuentro 26 — Integración, demostración y revisión de la Unidad IV'

S133 = ('13.3 Integración de módulos y revisión del alcance mínimo', [
    'Integrar es comprobar que las partes funcionan juntas: que el ejemplar dado de alta en el Capítulo 10 se puede '
    'prestar, que la devolución lo vuelve a mostrar disponible en la consulta pública, que el préstamo aparece en el '
    'informe con el curso correcto. Cada módulo pasó su prueba; ahora se prueba el circuito completo.',
    'La revisión se hace contra el alcance mínimo que fija Work §7.2 para el prototipo (Tabla 13.2). Cada función tiene '
    'un resultado verificable, la operación que lo cumple y la prueba que lo demuestra. Si una fila no tiene prueba con '
    'resultado, la función no está demostrada, aunque «ande».',
    'El recorrido de integración es el de la ficha de entorno (E-6a): consultar sin sesión, ingresar, dar de alta un '
    'ejemplar, prestarlo, intentar prestarlo otra vez, devolverlo, ver el informe con la cuenta de dirección y salir. Se '
    'hace también con la computadora desconectada de internet (P-13).',
])
TABLA_132_ROTULO = 'Tabla 13.2 — Revisión contra el alcance mínimo de producto (Work §7.2)'
TABLA_132 = (['Función', 'Resultado verificable (Work §7.2)', 'Cómo lo cumple el prototipo', 'Operación', 'Prueba'],
             [list(a) for a in C.ALCANCE])
EJ133 = ('Ejemplo resuelto 13.3: una fila sin prueba', [
    'Consigna: en la revisión del equipo modelo, la fila «Persistencia y entrega» tiene PA-01 y E-11 con resultado, pero '
    'E-12 (restauración) dice «no se hizo». ¿Está cumplida?',
    'No del todo. La persistencia está demostrada (PA-01) y el respaldo existe (E-11), pero la restauración no se probó. '
    'Se anota como pendiente, con fecha y responsable. No se marca como cumplida.',
    'La instalación y la restauración por otro equipo, siguiendo la guía, son evidencia de la Unidad VI. En el H4 alcanza '
    'con mostrar que el respaldo y la restauración propios funcionan.',
])

S134 = ('13.4 Demostración del incremento y registro de pendientes', [
    'La demostración se hace ante otro equipo, que actúa como bibliotecaria y como dirección. El equipo no explica el '
    'código: muestra que el circuito funciona con datos ficticios, incluidos los rechazos, y que los datos siguen después '
    'de reiniciar.',
    'Lo que no funciona o funciona mal se registra como incidencia: dónde pasa, qué pasa, qué gravedad tiene, en qué '
    'estado está y cuándo se resuelve (Tabla 13.3). Una incidencia registrada no es un fracaso: es la evidencia de que el '
    'equipo prueba en serio. Lo que sí es un problema es ocultarla o inventar un resultado.',
])
TABLA_133_ROTULO = 'Tabla 13.3 — Lista de incidencias del equipo modelo (formato; ejemplos ficticios)'
TABLA_133 = (['Código', 'Dónde', 'Qué pasa', 'Gravedad', 'Estado', 'Destino'], [list(i) for i in C.INCIDENCIAS])

H4_TITULO = 'Revisión de la Unidad IV — Hito H4: circuito funcional completo y lista de incidencias'
H4_TEXTO = [
    'El H4 es la revisión de la Unidad IV. Cada equipo demuestra su prototipo mínimo completo: catálogo, lectores, '
    'préstamo, devolución, consultas e informe, con los datos guardados entre ejecuciones. Muestra las condiciones '
    'mínimas de aceptación que corresponden a esta unidad (Work §4.3): el circuito de préstamo y devolución ejecutable, '
    'la persistencia comprobada, ninguna pérdida de historial, el rechazo del préstamo simultáneo del mismo ejemplar y la '
    'evidencia de las pruebas de cada incremento. Entrega la lista de incidencias.',
    'Durante la revisión, el docente le propone a cada integrante una variante: un cambio de regla, de mensaje o de dato '
    'que no se resolvió antes. Cada estudiante explica, solo, qué capa toca, qué archivo cambiaría y qué prueba lo '
    'comprobaría. No hace falta programarla en el momento: se evalúa el razonamiento y la trazabilidad.',
]
H4_LISTA = ('Antes de presentar: lista de verificación del equipo', [
    '1. ¿Funciona el recorrido completo de E-6a, también sin internet?',
    '2. ¿Cada operación comprueba el rol en el servidor y responde ME-13 sin cambiar datos?',
    '3. ¿Los datos siguen después de reiniciar, y el respaldo y la restauración propios funcionan?',
    '4. ¿P-07 se ejecutó con procesos independientes, y su resultado está anotado con el entorno?',
    '5. ¿Ninguna operación borra préstamos, lectores ni ejemplares con historia?',
    '6. ¿Cada fila de la Tabla 13.2 tiene su prueba con resultado, o figura como pendiente?',
    '7. ¿La lista de incidencias tiene gravedad, estado y destino?',
    '8. ¿La bitácora tiene las versiones de la unidad y los aportes de cada integrante?',
])
H4_EVALUACION = ('Cómo se evalúa el H4', [
    'Se evalúan seis criterios, que cubren las capacidades C7, C8 y C9, con los cuatro niveles de desempeño de los hitos '
    'anteriores: Sólido, Logrado, En desarrollo e Inicial. La rúbrica completa está en la guía docente, y tu docente la '
    'comparte antes de la revisión.',
    'Cada criterio combina un 60 % de evidencia del producto del equipo y un 40 % de evidencia individual: la resolución '
    'de tu variante, tu aporte registrado en la bitácora y la observación del docente. La proporción y los niveles son '
    'una propuesta editorial: la institución decide cómo se convierten en calificación.',
    'Si falta una evidencia, se registra como ausente y se acuerda cuándo entregarla; no se confunde con un desempeño de '
    'nivel inicial. Que una prueba no se haya podido ejecutar en la computadora del colegio se registra como pendiente del '
    'entorno, no como falla del equipo.',
])
RUBRICA_H4 = [
    ('Circuito funcional completo', 'C8',
     ['Catálogo, lectores, préstamo, devolución, consultas e informe integrados; el recorrido de E-6a funciona sin internet y el equipo muestra un caso no previsto.',
      'El recorrido de E-6a funciona de punta a punta con datos ficticios.',
      'Funcionan partes del circuito, pero no el recorrido completo.',
      'No hay un circuito ejecutable.'],
     'Demostración y recorrido E-6a', 'Explica qué módulo cumple cada paso'),
    ('Reglas en el servidor y en la base', 'C8',
     ['Rechaza toda entrada inválida con su mensaje; permisos con ME-13 en cada operación; RI-01 con sus dos protecciones; historial protegido en la base.',
      'Rechaza las entradas inválidas principales; permisos en el servidor; RI-01 protegido.',
      'Algunas reglas solo en la pantalla, o un permiso que falta.',
      'Las reglas dependen de la pantalla.'],
     'Pruebas de rechazo, P-07, P-11 y Tabla 11.3', 'Explica una protección y su prueba'),
    ('Persistencia, respaldo e historial', 'C8',
     ['Datos que siguen al reiniciar, respaldo y restauración propios probados, y consulta de control sin anomalías.',
      'Persistencia demostrada y respaldo hecho; historial sin pérdidas.',
      'Persistencia sin demostrar o respaldo sin probar.',
      'Los datos se pierden o se borra historial.'],
     'PA-01, E-11, E-12 y consulta de control', 'Explica cómo demostró la persistencia'),
    ('Evidencia de pruebas', 'C9',
     ['Pruebas de cada incremento con esperado, obtenido y entorno; una prueba nueva propuesta para un hallazgo propio.',
      'Pruebas de cada incremento con esperado, obtenido y entorno.',
      'Pruebas incompletas o sin resultado obtenido.',
      'Sin evidencia de pruebas.'],
     'Resultados de pruebas y Tabla 13.2', 'Resuelve su variante y nombra la prueba que la comprueba'),
    ('Incidencias y pendientes', 'C9',
     ['Lista con gravedad, estado y destino, cada incidencia reproducible; los pendientes del entorno separados de las fallas.',
      'Lista de incidencias con gravedad y destino.',
      'Lista incompleta o sin gravedad.',
      'Sin lista, o con resultados inventados.'],
     'Lista de incidencias y ficha de entorno', 'Explica una incidencia y cómo la reproduciría'),
    ('Versiones, bitácora y trabajo del equipo', 'C7',
     ['Versiones del prototipo citadas con sus pruebas, bitácora al día con aportes de todos y correcciones registradas.',
      'Versiones identificables y bitácora con aportes.',
      'Versiones sin registro o bitácora irregular.',
      'Sin versiones ni bitácora.'],
     'Bitácora y versiones 0.1 a 0.x', 'Aporte propio registrado y observación del docente'),
]
ACT_E26 = [
    ('Ejercitá', [
        'Completá la Tabla 13.2 para el prototipo de tu equipo: en cada fila, la prueba y su resultado obtenido, o '
        '«pendiente» con el motivo.',
    ]),
    ('Resolvé', [
        'Hacé el recorrido de integración de E-6a con la computadora desconectada de internet y registrá el resultado de '
        'cada paso (P-13).',
        'Después de la demostración, armá la lista de incidencias de tu equipo con el formato de la Tabla 13.3 y registrá '
        'la versión del prototipo que se revisó.',
    ]),
]

REPASO = ('Para repasar', [
    'La consulta pública cuenta los disponibles en el momento y nunca muestra datos de lectores.',
    'Los vencidos se calculan respecto de una fecha de referencia escrita, para que el resultado se pueda comprobar.',
    'El informe agrupa por el curso al prestar, agrega «Docentes» y cuenta el total de nuevo.',
    'Integrar es probar el circuito completo; la revisión se hace contra el alcance mínimo, fila por fila.',
    'Lo que falla se registra como incidencia; lo que no se probó, como pendiente. Nada se inventa.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, los Encuentros 25 y 26 se reúnen en el Encuentro 19: «Solo disponibles, activos y '
    'vencidos con fecha de referencia.» El informe mensual (OP-05) pasa a actividad complementaria o a la Unidad V.',
    'No se omiten: el recorrido de integración, la revisión contra la Tabla 13.2, la lista de incidencias y el H4. La '
    'Práctica 13 pasa a actividad complementaria.',
])

# ------------------------------------------------------------------ evaluación
EVAL_ID = 'ADS3-L4-C13-f'
EVAL_TITULO = 'Evaluación del Capítulo 13'
EVAL_TEXTO_BASE = ('Texto base — Préstamo de mapas de la mapoteca (situación de evaluación, ficticia)', [
    'MP-1 Cualquier persona puede consultar qué mapas están disponibles, sin iniciar sesión.',
    'MP-2 Los mapas se prestan por tres días.',
    'MP-3 La coordinadora quiere ver los préstamos vencidos al cierre de cada viernes.',
    'MP-4 La dirección pide cuántos mapas se prestaron en el mes, por curso.',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', '¿Qué puede mostrar la consulta pública de MP-1?',
     ['El título del mapa y cuántos hay disponibles.', 'Quién tiene cada mapa.', 'El curso de quien lo retiró.',
      'Los préstamos vencidos.']),
    ('mc', 'Un mapa salió el lunes 2 (MP-2). Con fecha de referencia viernes 6 (MP-3), ¿cómo se marca si no volvió?',
     ['Vencido, porque vencía el jueves 5.', 'En plazo, porque vence el viernes 6.', 'En plazo, porque vence el lunes 9.',
      'No se puede saber sin la fecha de hoy.']),
    ('mc', '¿Por qué el total del informe de MP-4 se cuenta de nuevo y no se suma a mano?',
     ['Para comprobar que la suma de los grupos coincide.', 'Porque es más rápido.', 'Para no mostrar los grupos.',
      'Porque la dirección no sabe sumar.']),
    ('mc', 'Una función del alcance mínimo «anda», pero no tiene prueba con resultado. ¿Cómo se registra en la revisión?',
     ['Como pendiente, con motivo y responsable.', 'Como cumplida.', 'No se registra.', 'Como incidencia grave.']),
    ('vf', 'La cantidad de mapas disponibles conviene guardarla en una columna y actualizarla en cada préstamo.',
     False, 'Falso. Es un dato derivado: se cuenta en el momento, así no deja de coincidir.'),
    ('vf', 'Registrar una incidencia en la demostración muestra que el equipo prueba en serio.',
     True, 'Verdadero. Lo que no se admite es ocultarla o inventar un resultado.'),
    ('vf', 'Si un estudiante cambió de curso, sus préstamos del mes anterior pasan a contarse en el curso nuevo.',
     False, 'Falso. Se agrupan por el curso que tenía al prestar.'),
    ('ab', 'Escribí el contrato de la consulta de vencidos de MP-3: entradas, precondición, resultado y errores, con sus '
           'fuentes (MP-…).',
     'Entradas: fecha de referencia y cuenta. Precondición: rol de coordinadora (MP-3). Resultado: préstamos activos con '
     'la marca de vencido si el vencimiento es anterior a la fecha de referencia (MP-2, MP-3). Errores: fecha inválida, '
     'sin préstamos activos, sin permiso. Un punto por cada parte.', 4),
    ('ab', 'Escribí dos incidencias posibles de un sistema de la mapoteca con el formato de la Tabla 13.3 y la prueba que '
           'reproduce cada una.',
     'Cada incidencia con dónde, qué pasa, gravedad, estado y destino (1 punto cada una) y su prueba reproducible '
     '(1 punto cada una).', 4),
]
EVAL_PUNTAJE = ('Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno). '
                'Es opcional: el instrumento principal del cierre de la unidad es el H4.')
