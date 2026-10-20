# -*- coding: utf-8 -*-
"""Capítulo 6 — «Priorizar y mantener la coherencia» (Work §6: secciones 6.1 a 6.4 y revisión de la Unidad II con H2;
encuentros 11 y 12).

La prioridad se justifica con razones (circuito, reglas, valor, dependencias), sin matriz ponderada (control E del
lote 1). La planificación de incrementos usa una columna «depende de», sin PERT ni teoría de grafos (Work §3,
Matemática Aplicada). La trazabilidad, las pruebas previstas, la solicitud SC-01 y el catálogo v1.1 están en
caso/requisitos.py. El H2 se aplica sobre el proyecto de cada equipo; la nueva necesidad no está en el dossier ni en el
buzón (la elige el docente del banco de la guía)."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'caso'))
import requisitos as R
import modelos as MO
import mbokaja_u2 as MB
D = R.D

NUM = 6
UNIDAD = 'Unidad II — Especificar qué debe resolver el sistema'
CAPITULO = 'Capítulo 6'
TITULO = 'Priorizar y mantener la coherencia'
ENCUENTROS = (11, 12)
SECCIONES = ['6.1 Alcance mínimo y funcionalidades postergables',
             '6.2 Trazabilidad entre necesidad, requisito, modelo y prueba',
             '6.3 Iteraciones, tareas, dependencias y responsabilidades',
             '6.4 Solicitud de cambio y análisis de impacto']
REVISION_WORK = 'Revisión de unidad II: nueva necesidad del usuario y actualización del dossier; H2'
PRACTICA_WORK = 'trazar, planificar y cambiar el catálogo de otra biblioteca'

ROTULO_CAPACIDAD = ('Capacidades propuestas para el programa institucional (C3, C4 y C7; no son capacidades oficiales '
                    'del MEC)')
CAPACIDAD = ('C3. Especifica y prioriza requisitos verificables.\n'
             'C4. Modela procesos e interacciones del sistema.\n'
             'C7. Organiza y registra el trabajo colaborativo.')
TEMA = ('Alcance mínimo, prioridad justificada y funcionalidades postergables. Matriz de trazabilidad entre necesidad, '
        'regla, requisito, caso de uso, criterio de aceptación y prueba prevista. Incrementos, tareas, responsables, '
        'dependencias, estimación y versiones. Solicitud de cambio y análisis de impacto. Revisión de la Unidad II '
        '(hito H2).')
INDICADORES = [
    'Distingue el alcance mínimo de las funcionalidades postergables y justifica cada prioridad con criterios explícitos.',
    'Construye una matriz de trazabilidad entre necesidad, regla, requisito, caso de uso, criterio de aceptación y prueba prevista, y detecta omisiones.',
    'Planifica incrementos con tareas, responsables, dependencias, estimaciones y versiones identificables.',
    'Tramita una solicitud de cambio con su análisis de impacto, su decisión y la nueva versión del catálogo y de los modelos.',
    'Actualiza el dossier del equipo y explica individualmente el impacto de un cambio acotado.',
]
TIEMPO = ('Dos encuentros de 5 HC (11 y 12 de la secuencia anual). El Encuentro 12 incluye la revisión de la Unidad II '
          '(hito H2).')

APERTURA = [
    'El equipo ya tiene un catálogo de requisitos y modelos que lo explican. Ahora aparecen tres preguntas que todo '
    'proyecto real tiene que responder: qué se hace primero, cómo se sabe que nada quedó suelto y qué se hace cuando '
    'alguien pide un cambio.',
    'En este capítulo priorizás con razones, armás la matriz que une cada necesidad con su prueba, planificás los '
    'incrementos del prototipo y tramitás una solicitud de cambio. Al final, tu equipo defiende sus requisitos y sus '
    'modelos en la revisión de la unidad: el hito H2.',
]
ARTICULACION = [
    'Con los Capítulos 4 y 5: la matriz de trazabilidad usa el catálogo, los casos de uso y los criterios de aceptación '
    'que ya escribiste.',
    'Con el Capítulo 3: el alcance mínimo y las exclusiones se acordaron allí; acá se ordena el trabajo dentro de ese '
    'alcance. Un pedido fuera del alcance se tramita como solicitud de cambio.',
    'Con la Unidad IV: los incrementos que se planifican acá son los de los Encuentros 19 a 26. Las pruebas previstas se '
    'diseñan y se ejecutan en los Capítulos 14 a 16.',
]

# ------------------------------------------------------------------ encuentro 11
E11_TITULO = 'Encuentro 11 — Prioridades, trazabilidad e incrementos'

S61 = ('6.1 Alcance mínimo y funcionalidades postergables', [
    'El alcance mínimo es lo que el prototipo tiene que hacer para que el circuito de préstamo y devolución funcione y '
    'las reglas se cumplan. Se acordó en el Capítulo 3 (Tabla 3.5) y los requisitos imprescindibles del catálogo lo '
    'cubren. Una funcionalidad postergable aporta valor, pero el circuito funciona sin ella: se registra, se le asigna '
    'prioridad y se hace si sobra tiempo o en una versión posterior.',
    'Para priorizar se usan los tres niveles de 4.3 (imprescindible, importante y deseable) y cuatro preguntas, en este '
    'orden. ¿Sin esto funciona el circuito? ¿Sin esto se viola una regla acordada? ¿Cuánto valor aporta y a quién? '
    '¿Depende de algo que todavía no está? La última pregunta no cambia el nivel, pero sí el orden: un requisito no '
    'puede construirse antes que aquello de lo que depende.',
    'No se suman puntajes. Cada prioridad lleva su razón escrita, y la razón cita la fuente: una necesidad, una regla o '
    'un pedido. Así, si alguien no está de acuerdo, se discute la razón, no un número.',
])
TABLA_61_ROTULO = 'Tabla 6.1 — Pedidos fuera del núcleo y su prioridad'
TABLA_61 = (['Pedido', 'Fuente', 'Prioridad', 'Razón', 'Decisión'],
            [['Renovar el préstamo sin traer el libro', 'E3-L4, N-13', 'Deseable', 'El circuito funciona sin esto y falta una regla de renovación.', 'Postergado; se propone la regla a la dirección.'],
             ['Reservar unos treinta ejemplares por tres semanas para el plan lector', 'E2-L8, N-12', 'Importante', 'Aporta mucho a los docentes, pero choca con el plazo del reglamento (D1-A3).', 'Postergado hasta que la dirección decida la regla.'],
             ['Ver los préstamos de los alumnos de un curso', 'B-01', 'Importante', 'Lo cubre en parte RF-08; exige cuidar la privacidad (RNF-03).', 'Incremento 4, si hay tiempo.'],
             ['Informe mensual impreso', 'B-04', 'Importante', 'Es una salida de RF-09, que ya está en el catálogo.', 'Se resuelve con RF-09.'],
             ['Avisar al lector cuando vence su préstamo', 'Propuesta del equipo', 'Fuera del núcleo', 'Notificaciones externas (Work §7.2) y sin internet (RS-01).', 'Excluido; extensión posible.'],
             ['Reservas en línea y códigos de barras', 'Capítulo 3, Tabla 3.6', 'Fuera del núcleo', 'Exclusiones acordadas en el alcance.', 'Excluido.']])

EJ61 = ('Ejemplo resuelto 6.1: priorizar la renovación', [
    'Consigna: decidir la prioridad de la renovación pedida por Iván (E3-L4) y justificarla con las cuatro preguntas.',
    '¿Sin esto funciona el circuito? Sí: el lector puede devolver y volver a pedir el libro. No es imprescindible.',
    '¿Sin esto se viola una regla? No: ninguna regla acordada habla de renovaciones.',
    '¿Cuánto valor aporta y a quién? Al lector le ahorra un viaje; a la bibliotecaria le agrega una operación. Valor '
    'medio.',
    '¿Depende de algo? Sí: de una regla nueva (cuántas veces, por cuántos días, si se renueva un préstamo vencido), que '
    'tiene que aprobar la dirección (E5-L8), y de RF-02, que calcula el vencimiento.',
    'Decisión: deseable y postergada. Se registra la necesidad N-13 con su fuente y se le propone la regla a la dirección. '
    'Si se aprueba, entra por solicitud de cambio (6.4).',
])

S62 = ('6.2 Trazabilidad entre necesidad, requisito, modelo y prueba', [
    'Trazar es poder seguir el hilo de cada cosa del proyecto hacia atrás y hacia adelante. Hacia atrás, para saber por '
    'qué existe: este requisito está porque la bibliotecaria lo necesita (una necesidad) o porque una regla lo exige. '
    'Hacia adelante, para saber qué hay que construir y cómo se va a comprobar: el caso de uso que lo usa, su criterio de '
    'aceptación y la prueba que lo verifica.',
    'La matriz de trazabilidad pone ese hilo en una tabla: una fila por requisito y una columna por eslabón. Sirve para '
    'tres cosas. Encontrar omisiones: una fila con un hueco es algo que falta. Encontrar sobrantes: un requisito sin '
    'necesidad ni regla puede ser una idea del equipo. Y calcular el impacto de un cambio: si cambia un eslabón, la '
    'fila dice qué más hay que revisar (6.4).',
    'Las pruebas todavía no se diseñan: se identifican con un código (P-01, P-02…) y una descripción breve, y se '
    'desarrollan en los Capítulos 14 a 16. Identificarlas ahora asegura que ningún requisito llegue a la Unidad V sin '
    'una forma de comprobarlo.',
])
LEAD_FIG61 = ('La Figura 6.1 extiende la cadena de la Figura 4.2 con el eslabón del Capítulo 5: el flujo alternativo 5a '
              'de CU-01 es donde el sistema hace cumplir RN-01.')
EPI_FIG61 = 'Figura 6.1 — Cadena de trazabilidad de RF-04, de la necesidad a la prueba, con su caso de uso.'

TABLA_62_ROTULO = 'Tabla 6.2 — Matriz de trazabilidad del catálogo v1.0'


def _ca(rid):
    origen, donde = R.DONDE_CA[rid]
    return donde if origen != 'DOCENTE' else 'a escribir por el equipo'


TABLA_62 = (['Requisito', 'Necesidad', 'Regla', 'Caso de uso', 'Criterio (dónde está)', 'Prueba'],
            [[r, ', '.join(n) or '—', ', '.join(rn) or '—', cu, _ca(r), p] for r, n, rn, cu, p in R.TRAZABILIDAD])

EJ62 = ('Ejemplo resuelto 6.2: leer la matriz para encontrar lo que falta', [
    'Consigna: revisar la Tabla 6.2 y anotar las omisiones y lo que hay que hacer con cada una.',
    'Seis requisitos tienen el criterio «a escribir por el equipo»: RF-01, RF-03, RF-08, RF-10, RNF-02 y RS-02. El de '
    'RNF-03 está en el Desafío del Encuentro 8, que es optativo. El equipo completa los que falten antes del H2.',
    'RF-09 y RF-10 apuntan a casos de uso sin desarrollar (CU-04 y CU-05). La Actividad 2 del Encuentro 10 ya desarrolló '
    'CU-05; falta CU-04.',
    'RF-02 y RF-05 no tienen necesidad: salen de reglas (RN-03 y RN-02). No es un error. La matriz muestra que, si la '
    'regla cambia, estos requisitos se revisan aunque nadie los haya pedido.',
    'Ningún requisito queda sin prueba prevista: P-01 a P-15 cubren los quince. P-07 es la del ejemplo de la Figura 6.1.',
])

S63 = ('6.3 Iteraciones, tareas, dependencias y responsabilidades', [
    'Un incremento es una parte del prototipo que funciona sola y se puede mostrar. El prototipo no se construye todo de '
    'una vez: se construye por incrementos, uno después de otro, y cada uno se prueba antes de seguir. Si algo sale mal, '
    'se descubre temprano y con poco trabajo perdido.',
    'Para cada incremento se arma una lista de tareas. Cada tarea tiene un responsable (un rol del equipo, no «todos»), '
    'una estimación en HC, de qué depende y en qué estado está. Una dependencia dice qué tiene que estar terminado antes: '
    'no se puede registrar un préstamo sin lectores ni ejemplares cargados. Con la columna «depende de» alcanza para '
    'ordenar el trabajo; no hacen falta diagramas de red.',
    'Cada vez que un documento cambia de forma importante, se le da una versión nueva (v1.0, v1.1…) y se anota en la '
    'bitácora qué cambió y por qué. La versión del catálogo, la de los modelos y la del prototipo se citan entre sí: la '
    'prueba P-07 de la versión 0.3 del prototipo comprueba el RF-04 del catálogo v1.1.',
])
TABLA_63_ROTULO = 'Tabla 6.3 — Incrementos del prototipo (Unidad IV)'
TABLA_63 = (['Incremento', 'Encuentros', 'Qué se puede mostrar al terminar', 'Requisitos', 'Depende de'],
            [['1. Base', '19 y 20', 'Una operación completa de punta a punta, con datos ficticios guardados', 'RS-01, RS-02', '—'],
             ['2. Catálogo y lectores', '21 y 22', 'Ejemplares y lectores cargados, inactivación y permisos mínimos', 'RF-10, RNF-02, RNF-03', 'Incremento 1'],
             ['3. Préstamo y devolución', '23 y 24', 'El circuito con sus rechazos y el historial', 'RF-01 a RF-06, RF-08', 'Incremento 2'],
             ['4. Consultas e integración', '25 y 26', 'Disponibilidad, vencidos e informe mensual; H4', 'RF-07, RF-09, RNF-01', 'Incremento 3']])
TABLA_64_ROTULO = 'Tabla 6.4 — Tareas del Incremento 3 (equipo modelo)'
TABLA_64 = (['Tarea', 'Responsable', 'HC', 'Depende de', 'Estado'],
            [['T3.1 Repasar CU-01 y CU-02 y sus criterios', 'Registro', '0,5', '—', 'Pendiente'],
             ['T3.2 Registrar un préstamo válido (RF-01, RF-02)', 'Desarrollo A', '2', 'Incremento 2', 'Pendiente'],
             ['T3.3 Rechazos de lector y ejemplar (RF-04 a RF-06)', 'Desarrollo B', '2', 'T3.2', 'Pendiente'],
             ['T3.4 Registrar la devolución (RF-03, RF-08)', 'Desarrollo A', '2', 'T3.2', 'Pendiente'],
             ['T3.5 Ejecutar P-01 a P-07 y anotar resultados', 'Verificación', '1,5', 'T3.3 y T3.4', 'Pendiente'],
             ['T3.6 Actualizar la bitácora y la versión del prototipo', 'Versiones', '0,5', 'T3.5', 'Pendiente']])

EJ63 = ('Ejemplo resuelto 6.3: ordenar las tareas de un incremento', [
    'Consigna: decidir el orden de las tareas de la Tabla 6.4 y quién hace cada una.',
    'T3.2 va primero entre las de desarrollo: sin un préstamo registrado no se puede rechazar uno repetido ni devolverlo.',
    'T3.3 y T3.4 dependen de T3.2 pero no entre sí: dos integrantes pueden hacerlas a la vez. Así se aprovechan las 10 HC '
    'del incremento.',
    'T3.5 espera a T3.3 y T3.4, y la hace otro rol: quien construyó no es el mejor para encontrar sus propios errores.',
    'Las estimaciones suman 8,5 HC de las 10 del incremento. Quedan 1,5 HC de margen para imprevistos: un plan sin '
    'margen falla con el primer problema.',
])

ACT_E11 = [
    ('Ejercitá', [
        'Asigná una prioridad (imprescindible, importante o deseable) a cada pedido y justificala con las cuatro preguntas '
        'de 6.1:\n'
        '(a) RF-07, la consulta de disponibilidad;\n'
        '(b) mostrar en la consulta la tapa de cada libro;\n'
        '(c) RNF-02, que solo la bibliotecaria registre préstamos;\n'
        '(d) un informe de los títulos que más se piden.',
    ]),
    ('Resolvé', [
        'Completá dos filas de la Tabla 6.2 que dicen «a escribir por el equipo»: escribí el criterio de aceptación '
        '«Dado… cuando… entonces…» de RF-03 y el de RF-08.',
        'Armá la lista de tareas del Incremento 2 (Tabla 6.3): al menos cuatro tareas, con responsable, estimación en HC, '
        'dependencia y estado.',
    ]),
    ('Pensá y decidí', [
        'Un integrante propone empezar por el informe mensual (RF-09), «porque es lo que pide la dirección». Explicá qué '
        'pasaría con el plan y qué le responderías.',
    ]),
    ('Desafío', [
        'Agregá a la Tabla 6.2 la fila de RNF-04 (de la consigna común de la Práctica 4): necesidad, regla, caso de uso, '
        'criterio y una prueba prevista con el próximo código libre.',
    ]),
]

# ------------------------------------------------------------------ encuentro 12
E12_TITULO = 'Encuentro 12 — Solicitud de cambio y revisión de la Unidad II'

S64 = ('6.4 Solicitud de cambio y análisis de impacto', [
    'Los requisitos cambian: aparece una necesidad nueva, cambia una regla, un interesado se da cuenta de algo. Que '
    'cambien no es un problema; el problema es cambiarlos sin saber qué más se rompe. Por eso, todo cambio después de '
    'acordado el catálogo entra por una solicitud de cambio.',
    'La solicitud dice quién pide el cambio y cuándo, qué se pide y por qué, con su fuente. Después viene el análisis de '
    'impacto: con la matriz de trazabilidad se buscan las reglas, los requisitos, los casos de uso, los criterios y las '
    'pruebas afectados, y se estima cuánto trabajo agrega y en qué incremento. Con eso, quien tiene autoridad decide: se '
    'acepta, se rechaza o se posterga. Si se acepta, se actualizan el catálogo y los modelos con una versión nueva, y se '
    'conserva la anterior.',
    'El equipo analiza y propone; no decide un cambio de regla. Las reglas son de la institución (E5-L8): el equipo le '
    'muestra a la dirección qué implica el cambio para que decida con información.',
])
D3_LEAD = ('En la semana del Encuentro 11 llegó una nota nueva de la dirección. Es un registro nuevo del dossier: se cita '
           'igual que los otros.')
TABLA_65_ROTULO = 'Tabla 6.5 — Solicitud de cambio SC-01'
TABLA_65 = (['Campo', 'Contenido'], [list(x) for x in R.SC01])
LEAD_FIG62 = ('La Figura 6.2 muestra el análisis de impacto de SC-01: qué cambia, qué es nuevo y qué se revisa aunque '
              'no cambie.')
EPI_FIG62 = 'Figura 6.2 — Impacto de la solicitud de cambio SC-01 sobre reglas, requisitos, modelos y pruebas.'
TABLA_66_ROTULO = 'Tabla 6.6 — Cambios del catálogo v1.0 a la v1.1'
TABLA_66 = (['Elemento', 'Cambio', 'Detalle'], [list(x) for x in R.CAMBIOS_V11])

EJ64 = ('Ejemplo resuelto 6.4: el análisis de impacto de SC-01', [
    'Consigna: analizar la nota D3 con la matriz de trazabilidad y preparar la decisión.',
    'Paso 1. Ubicar el cambio: D3-1 cambia la regla RN-02, que pasa a decir «' + R.REGLA_V11[1] + '».',
    'Paso 2. Seguir la fila de RN-02 en la Tabla 6.2: llega a RF-05, a CU-01 (flujo 4b) y a P-06.',
    'Paso 3. RF-05 dice «el máximo vigente», así que su texto no cambia: el Desafío del Encuentro 7 lo anticipaba. Pero el '
    'máximo ahora depende del tipo de lector, y el catálogo no tiene ningún requisito que lo registre. Aparece una '
    'omisión: hace falta ' + R.RF11[0] + ', «' + R.RF11[2] + '».',
    'Paso 4. Revisar los modelos y las pruebas: CU-01 compara con el máximo del tipo de lector, y P-06 se desdobla en dos '
    'pruebas, una para cada tipo.',
    'Paso 5. Estimar y decidir: media HC más en los Incrementos 2 y 3. La dirección acepta, con la conformidad de la '
    'bibliotecaria. El catálogo pasa a la v1.1 (Tabla 6.6) y la v1.0 se conserva.',
])

ACT_E12 = [
    ('Ejercitá', [
        'Indicá qué elementos de la Tabla 6.2 habría que revisar con cada cambio:\n'
        '(a) la dirección decide que el plazo de préstamo sea de diez días;\n'
        '(b) la bibliotecaria pide que el informe mensual separe a los docentes de los estudiantes;\n'
        '(c) el colegio consigue internet estable en la biblioteca.',
    ]),
    ('Resolvé', [
        'Completá una solicitud de cambio, con los campos de la Tabla 6.5, para el pedido (a) de la actividad anterior. '
        'Incluí la nueva versión de los elementos que cambian.',
    ]),
    ('Pensá y decidí', [
        'El cambio (c) parece una buena noticia. Explicá por qué igual conviene tramitarlo como solicitud de cambio y qué '
        'riesgo tendría eliminar RS-01 del catálogo.',
    ]),
    ('Desafío', [
        'Preparate para el H2: elegí un requisito de tu catálogo y explicá, en cinco líneas, qué pasaría en tus modelos y '
        'en tus pruebas si su regla cambiara.',
    ]),
]

H2_TITULO = 'Revisión de la Unidad II — Hito H2: requisitos y modelos funcionales versionados'
H2_TEXTO = [
    'El H2 cierra la Unidad II. Cada equipo presenta su catálogo de requisitos y sus modelos (proceso actual y '
    'propuesto, contexto y casos de uso), con la matriz de trazabilidad. Durante la revisión, el docente entrega una '
    'necesidad nueva de un usuario, que no está en el dossier ni en el buzón: el equipo la registra en su dossier, la '
    'tramita como solicitud de cambio y muestra cómo quedan el catálogo y los modelos en la versión nueva.',
    'Qué se presenta: el catálogo versionado (al menos ocho requisitos funcionales y cuatro de calidad o restricciones, '
    'con fuente, prioridad y criterio de aceptación), los modelos comentados, la matriz de trazabilidad, la solicitud de '
    'cambio con su análisis de impacto y la bitácora con las versiones.',
    'Si tu curso trabaja con su propia biblioteca, el H2 se hace sobre ese relevamiento; si no, sobre el dossier del '
    'caso. En los dos casos, cada integrante explica el impacto de un cambio acotado que le propone el docente.',
]
H2_LISTA = ('Antes de presentar: lista de verificación del equipo', [
    '1. ¿Cada requisito tiene identificador, fuente, prioridad con razón y criterio «Dado… cuando… entonces…»?',
    '2. ¿Hay al menos un criterio de aceptación sobre un requisito de calidad?',
    '3. ¿El proceso actual y el propuesto usan solo la notación de actividades, con carriles y guardas?',
    '4. ¿El diagrama de contexto tiene un solo sistema y flujos rotulados con sustantivos?',
    '5. ¿Los tres casos de uso prioritarios tienen escenario principal y al menos un flujo alternativo?',
    '6. ¿Cada requisito citado en un modelo existe en el catálogo?',
    '7. ¿La matriz de trazabilidad no tiene huecos sin explicar?',
    '8. ¿El catálogo y los modelos tienen versión, y la bitácora dice qué cambió?',
])
H2_EVALUACION = ('Cómo se evalúa el H2', [
    'Se evalúan cinco criterios con los cuatro niveles de desempeño del H1: Sólido, Logrado, En desarrollo e Inicial. La '
    'rúbrica completa está en la guía docente, y tu docente la comparte antes de la revisión.',
    'Igual que en el H1, cada criterio combina un 60 % de evidencia del producto del equipo y un 40 % de evidencia '
    'individual: tu explicación del impacto de un cambio acotado, tu aporte registrado en la bitácora y la observación '
    'del docente. La proporción y los niveles son una propuesta editorial: la institución decide cómo se convierten en '
    'calificación.',
    'Si falta una evidencia, se registra como ausente y se acuerda cuándo entregarla; no se confunde con un desempeño de '
    'nivel inicial.',
])
RUBRICA_H2 = [
    ('Catálogo de requisitos', 'C3',
     ['Requisitos sin soluciones, con fuente que respalda, criterio comprobable y prioridad razonada; detecta y corrige ambigüedades.',
      'Al menos ocho funcionales y cuatro de calidad o restricciones, con fuente, criterio y prioridad.',
      'Requisitos compuestos, sin criterio o con fuentes que no respaldan.',
      'Lista de deseos o de soluciones técnicas, sin fuentes.'],
     'Catálogo versionado', 'Explica de dónde sale un requisito y cómo se comprueba'),
    ('Procesos y contexto', 'C4',
     ['Proceso actual con problemas marcados, proceso propuesto con decisiones justificadas y contexto con flujos rastreables al dossier.',
      'Proceso actual y propuesto y diagrama de contexto, cada uno con su notación.',
      'Diagramas con notaciones mezcladas, acciones sin carril o flujos con verbos.',
      'Diagramas que no corresponden al caso o sin notación reconocible.'],
     'Diagramas de actividades y de contexto comentados', 'Explica una decisión del proceso propuesto'),
    ('Casos de uso y flujos alternativos', 'C4, C3',
     ['Tres casos de uso prioritarios con flujos alternativos que descubren una omisión y la convierten en requisito.',
      'Tres casos de uso con escenario principal, un flujo alternativo cada uno y requisitos citados que existen.',
      'Casos de uso que son pasos o pantallas, o flujos alternativos sin resultado.',
      'Sin casos de uso o sin flujos alternativos.'],
     'Diagrama de casos de uso y plantillas', 'Resuelve un flujo alternativo nuevo que propone el docente'),
    ('Trazabilidad y solicitud de cambio', 'C3, C7',
     ['Matriz completa; el análisis de impacto encuentra lo que cambia, lo nuevo y lo que se revisa, y estima el trabajo.',
      'Matriz con pocos huecos explicados; solicitud de cambio con requisitos, modelos y pruebas afectados y su decisión.',
      'Matriz incompleta o solicitud sin análisis de impacto.',
      'Cambio aplicado sin solicitud ni registro.'],
     'Matriz de trazabilidad y solicitud de cambio', 'Explica el impacto de un cambio acotado'),
    ('Dossier, versiones y trabajo del equipo', 'C2, C7',
     ['Dossier actualizado con la necesidad nueva; versiones citadas entre sí; bitácora al día con aportes de todos.',
      'Dossier actualizado y catálogo y modelos con versión nueva registrada en la bitácora.',
      'Versiones sin registro de cambios o bitácora irregular.',
      'Sin versiones ni bitácora.'],
     'Dossier, bitácora y versiones', 'Aporte propio registrado en la bitácora y observación del docente'),
]

# ------------------------------------------------------------------ práctica
PRACTICA_TITULO = 'Práctica 6 — Trazar, planificar y cambiar el catálogo de otra biblioteca'
PRACTICA_INTRO = [
    'Seguís con la Escuela Básica Mbokaja. Usá los requisitos MR-01 a MR-08 de la Práctica 5 y los casos de uso que '
    'escribiste en ella. Llegó una solicitud de la directora que no se parece a la del ejemplo: cambia un plazo y la '
    'forma de registrar a los docentes.',
]
NIVELES = [
    ('Nivel 1 — Guiado', [
        'Completá la matriz de trazabilidad de MR-01, MR-02, MR-04 y MR-05: necesidad (MN o V), caso de uso y paso, criterio '
        'de aceptación breve y prueba prevista (PM-01, PM-02…).\n'
        'MR-__ | Necesidad: ____ | Caso de uso: ____ | Criterio: Dado ____, cuando ____, entonces ____ | Prueba: PM-__',
        'Señalá un requisito MR que no aparezca en ningún caso de uso de tu Práctica 5. ¿Es una omisión del modelo o del '
        'catálogo?',
    ]),
    ('Nivel 2 — Intermedio', [
        'Priorizá MR-01 a MR-08 con las cuatro preguntas de 6.1. Tené en cuenta M-F4 (el encargado tendrá menos horas) y '
        'M-F5 (voluntarios los miércoles).',
        'Planificá dos incrementos para Mbokaja, con al menos tres tareas cada uno: responsable, estimación en HC, '
        'dependencia y estado.',
    ]),
    ('Nivel 3 — Ampliación', [
        'Tramitá MC-1 como solicitud de cambio, con los campos de la Tabla 6.5. Usá tu matriz para encontrar las normas, '
        'los requisitos, los casos de uso y las pruebas afectados.',
        'MC-1 cambia la norma M-N1. Explicá quién decide, qué opciones le presentarías a la directora y cómo quedaría la '
        'nueva versión del catálogo si acepta.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: cada fila de la matriz cita fuentes que existen; las prioridades tienen razón y '
                    'no se suman puntajes; cada tarea tiene responsable, estimación y dependencia; la solicitud de cambio '
                    'dice qué cambia, qué se revisa y quién decide.')

REPASO = ('Para repasar', [
    'El alcance mínimo hace funcionar el circuito y cumplir las reglas; lo postergable se registra con su prioridad y su razón.',
    'La prioridad se justifica con cuatro preguntas: circuito, reglas, valor y dependencias. No se suman puntajes.',
    'La matriz de trazabilidad une necesidad, regla, requisito, caso de uso, criterio y prueba; sus huecos son omisiones.',
    'Cada incremento se puede mostrar; cada tarea tiene responsable, estimación y dependencia, y cada documento, su versión.',
    'Un cambio entra por solicitud: se analiza su impacto con la matriz, decide quien tiene autoridad y se versiona el resultado.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, los Encuentros 11 y 12 se unen en uno: el plan de incrementos se reduce a la '
    'Tabla 6.3, sin la lista de tareas, y la solicitud de cambio se resuelve dentro de la revisión del H2.',
    'En ese encuentro no se omiten: la matriz de trazabilidad (Tabla 6.2), una solicitud de cambio con su análisis de '
    'impacto y el H2. Pasan a lectura domiciliaria: los Ejemplos resueltos 6.1 y 6.3 y la Práctica 6.',
])

# ------------------------------------------------------------------ evaluación
EVAL_ID = 'ADS3-L2-C6'
EVAL_TITULO = 'Evaluación del Capítulo 6'
EVAL_TEXTO_BASE = ('Texto base — Solicitudes de soporte de la sala de informática (situación de evaluación, ficticia)', [
    'W-1 Los docentes anotan en un cuaderno las fallas de las computadoras de la sala, y muchas se pierden.',
    'W-2 El encargado quiere saber qué solicitudes siguen pendientes.',
    'W-3 Requisitos: SR-1 registrar una solicitud con la computadora y la falla; SR-2 asignar un responsable; SR-3 cambiar el estado (pendiente, en curso, resuelta); SR-4 listar las pendientes.',
    'W-4 El encargado pide que, al cerrar una solicitud, quede anotado qué se hizo para resolverla.',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', 'En una matriz de trazabilidad, ¿qué muestra un requisito sin prueba prevista?',
     ['Que todavía no hay una forma de comprobar ese requisito.',
      'Que el requisito es una regla de negocio.',
      'Que el requisito es deseable.',
      'Que la necesidad está mal escrita.']),
    ('mc', '¿Qué pedido se puede postergar sin afectar el circuito mínimo del texto base?',
     ['Avisar al docente por mensaje cuando su solicitud se resuelva.',
      'Registrar una solicitud con la computadora y la falla.',
      'Cambiar el estado de una solicitud.',
      'Listar las solicitudes pendientes.']),
    ('mc', '¿Quién decide si se acepta un cambio que modifica una regla de la institución?',
     ['Quien tiene autoridad sobre esa regla, después del análisis de impacto.',
      'El integrante del equipo que recibió el pedido.',
      'El integrante que programa esa parte.',
      'Nadie: los cambios se aceptan siempre.']),
    ('mc', '«Cambiar el estado» depende de «Registrar una solicitud». ¿Qué significa?',
     ['Que no se puede terminar la primera sin tener hecha la segunda.',
      'Que las dos las hace la misma persona.',
      'Que la primera es más importante que la segunda.',
      'Que se pueden hacer en cualquier orden.']),
    ('vf', 'Si un cambio no modifica el texto de un requisito, no hay que revisar sus criterios ni sus pruebas.',
     False, 'Falso. Pueden cambiar los datos del criterio y de la prueba, como RF-05 con el cambio de RN-02 (SC-01).'),
    ('vf', 'Cada versión nueva del catálogo se identifica y se registra qué cambió.',
     True, 'Verdadero. La versión anterior se conserva y la bitácora dice qué cambió y por qué.'),
    ('vf', 'Para priorizar alcanza con que el equipo vote el pedido que más le gusta.',
     False, 'Falso. La prioridad se justifica con razones: circuito, reglas, valor y dependencias.'),
    ('ab', 'Armá la matriz de trazabilidad de SR-1 a SR-4 (necesidad W-…, requisito, criterio breve y prueba prevista) y '
           'señalá una omisión.',
     'SR-1 y SR-3 salen de W-1; SR-2 y SR-4, de W-2 (se acepta W-1 para SR-2 si se justifica). Cada fila con un criterio '
     'observable, por ejemplo: «Dada una solicitud pendiente, cuando el encargado la pasa a resuelta, entonces deja de '
     'figurar en la lista de pendientes». Pruebas PS-1 a PS-4. Omisiones posibles: ninguna regla dice quién puede cambiar '
     'el estado; no hay requisito de calidad (nada dice cuánto puede esperar una solicitud). Un punto por cada dos '
     'filas correctas, uno por los criterios y uno por la omisión.', 4),
    ('ab', 'Con W-4, completá una solicitud de cambio: qué cambia, qué requisitos y pruebas afecta, quién decide y la '
           'nueva versión del catálogo.',
     'Qué cambia: al pasar a «resuelta», se anota qué se hizo. Afecta a SR-3 (cambio de estado) y a su prueba; puede '
     'requerir un requisito nuevo SR-5 «registrar la solución de cada solicitud resuelta». Decide el encargado, que es '
     'quien pide y usa el registro, con conocimiento de la dirección si cambia una regla. Nueva versión del catálogo con '
     'SR-5 y el cambio anotado en la bitácora. Un punto por cada parte.', 4),
]
EVAL_PUNTAJE = ('Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno). '
                'El instrumento principal de la unidad es el H2.')
