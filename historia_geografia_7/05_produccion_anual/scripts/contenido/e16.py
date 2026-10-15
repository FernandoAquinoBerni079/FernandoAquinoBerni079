"""Encuentro 16 — Continuación D: la autonomía y sus límites (H3; temas H3d y H3e).

Taller de consolidación de la Clase 10: lectura segmentada de la Real
Provisión, cuadro «qué autorizaba / qué no autorizaba», debate guiado sobre
la deposición de Cabeza de Vaca (1544) y comparación con una elección actual.
"""
import curriculo as C

TITULO = 'Continuación D — La autonomía y sus límites: de 1537 a 1544'
CLAVE = 'Continuación D —'
INDICADORES = [
    'Distingue lo que la Real Provisión de 1537 autorizaba y lo que no autorizaba.',
    'Argumenta una posición sobre la deposición de Cabeza de Vaca con datos y con la norma de 1537.',
    'Compara las instituciones coloniales y la elección de 1537 con instituciones y elecciones actuales.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H3'], C.TEMAS['H3d'] + ' ' + C.TEMAS['H3e'], INDICADORES),
    ('h2', 'Leer una norma por partes'),
    ('p', 'En la Clase 10 leíste dos fragmentos de la Real Provisión de 1537. Una norma se entiende mejor si se lee por partes y '
          'se pregunta, para cada parte, qué permite y qué no permite. El cuadro resume, con palabras actuales, las partes de la '
          'provisión que estudiaste.'),
    ('tabla', ['Parte de la norma (síntesis)', 'Qué quiere decir'],
     [['Si Mendoza no dejó lugarteniente, o si este murió sin nombrar a otro…', 'Condición: solo vale cuando falta la autoridad.'],
      ['…los conquistadores y pobladores se reúnan…', 'Quiénes eligen: los españoles de la provincia.'],
      ['…y elijan a la persona que según Dios y sus conciencias pareciere más suficiente…', 'Criterio: la persona más capaz.'],
      ['…por Gobernador en nuestro Nombre…', 'Límite: el elegido gobierna en nombre del rey.']],
     [5.6, 4.4]),
    ('h2', 'El caso de 1544: la deposición de Cabeza de Vaca'),
    ('p', 'Álvar Núñez Cabeza de Vaca llegó a Asunción en 1542 con el título de adelantado, es decir, nombrado directamente por el '
          'rey. Quiso limitar las rancheadas y el servicio que los españoles exigían a los guaraníes, y controlar a los oficiales '
          'reales. En 1544, un grupo de oficiales y vecinos lo apresó, lo depuso y lo envió a España. Irala volvió a gobernar.'),
    ('p', 'Las dos partes contaron los hechos de manera distinta. Quienes lo depusieron lo acusaban de gobernar de manera '
          'arbitraria y de no respetar a los oficiales del rey. Cabeza de Vaca, en los Comentarios publicados en 1555 con la ayuda '
          'de su secretario, sostuvo que lo depusieron porque había querido frenar los abusos contra los indígenas.'),
    ('caja', 'concepto', 'Concepto clave — ',
     'Un hecho histórico puede tener varias versiones. Para opinar con fundamento hay que preguntarse quién cuenta cada versión, '
     'qué interés tenía y qué dice la norma vigente en ese momento. En 1544, la Real Provisión no autorizaba a destituir a un '
     'gobernador nombrado por el rey: solo permitía elegir uno cuando faltaba.'),

    ('h2', 'Consignas del taller'),
    ('p', 'Trabajá en grupos de cuatro. Usá la Clase 10 (fuente, cuadro «Elegir en 1537 y elegir hoy» y Figura 10.2) y este taller.'),
    ('consigna', 'Consignas del taller:'),
    ('item', '1. Completá el cuadro con lo que la Real Provisión autorizaba y lo que no autorizaba. Escribí al menos tres filas.'),
    ('cuadro', ['La Real Provisión autorizaba…', 'La Real Provisión no autorizaba…'], ['', '', ''], [5.0, 5.0], 1.0),
    ('item', '2. Completá el cuadro de las instituciones coloniales.'),
    ('cuadro', ['Institución', '¿Quiénes la integraban?', '¿Qué función tenía?', '¿Gobernaba?'],
     ['Cabildo', 'Obispado', 'Encomienda'], [2.4, 3.0, 3.4, 1.2], 1.1),
    ('item', '3. Debate guiado. ¿Aplicaron los vecinos de Asunción la Real Provisión cuando depusieron a Cabeza de Vaca en 1544? '
             'Anotá dos argumentos de tu grupo y uno del grupo que pensó distinto.', 6),
    ('item', '4. Elegí una institución actual que cumpla una función parecida a la del Cabildo (por ejemplo, la municipalidad o la '
             'junta municipal). Escribí una semejanza y una diferencia.', 3),
    ('item', '5. Escribí un texto de 6 a 8 líneas que compare la elección prevista en 1537 con una elección actual en el Paraguay. '
             'Se tendrá en cuenta: dos diferencias con datos (2 puntos), una semejanza (1 punto) y una conclusión sobre los límites '
             'de la autonomía de 1537 (1 punto).', 8),
    ('h3', 'Autoevaluación del taller'),
    ('tabla', ['Criterio', 'Lo logré', 'En proceso', 'Todavía no'],
     [['Distinguí lo que la norma autorizaba y lo que no.', '', '', ''],
      ['Diferencié el Cabildo, el Obispado y la encomienda.', '', '', ''],
      ['Di argumentos con datos y escuché los de otros.', '', '', ''],
      ['Comparé la elección de 1537 con una actual.', '', '', '']],
     [5.5, 1.5, 1.5, 1.5]),
]

PLAN = {
    'material': 'Tomo: Continuación D; Clase 10 (fuente, cuadro comparativo y Figura 10.2)',
    'tema': C.TEMAS['H3d'] + ' ' + C.TEMAS['H3e'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes lean la Real Provisión por partes, reconozcan sus límites, argumenten sobre el caso de 1544 '
                 'y comparen instituciones y elecciones coloniales con las actuales.',
    'funciones': {
        'Esenciales': 'En clase: consignas 1, 2, 3 y 5 del taller.',
        'Consolidación': 'La consigna 4 y la autoevaluación del taller (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 17).',
        'Complementarias o domiciliarias': 'Repasar las Clases 6 a 10 y las Continuaciones C y D para la Evaluación de la Unidad 3.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 10. Pregunta: «¿Una norma puede usarse para algo que no dice?».',
             'Responden con ejemplos de la escuela.', 'Ideas en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–22', 'Lectura por partes del cuadro de la Real Provisión.',
             'Explican con sus palabras cada parte.', 'Lectura comentada.'),
            ('22–40', 'Acompaña el cuadro «autorizaba / no autorizaba».',
             'Resuelven la consigna 1 en grupos.', 'Consigna 1 (esencial).'),
            ('40–55', 'Repasa la Figura 10.2 y acompaña el cuadro de instituciones.',
             'Resuelven la consigna 2.', 'Consigna 2 (esencial).'),
            ('55–80', 'Lectura del caso de 1544 y del Concepto clave. Coordina el debate: cada grupo expone en dos minutos y escucha a otro.',
             'Debaten y anotan argumentos (consigna 3).', 'Consigna 3 (esencial).'),
            ('80–100', 'Lee los criterios de la consigna 5 y acompaña la escritura.',
             'Escriben el texto comparativo.', 'Consigna 5 (esencial).'),
        ]),
        ('Cierre', [
            ('100–112', 'Puesta en común: dos textos leídos en voz alta y comentados con los criterios.',
             'Comparan y corrigen.', 'Textos revisados.'),
            ('112–120', 'Explica la autoevaluación, recuerda que el próximo encuentro es la Evaluación de la Unidad 3 y qué temas entran.',
             'Completan la autoevaluación.', 'Autoevaluación.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en el cuadro de la consigna 1: la primera fila resuelta en la pizarra como modelo.',
        'Apoyo en el debate: tarjetas con frases de inicio («Creo que sí porque…», «Creo que no porque la norma dice…»).',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: averiguar qué fue la Revolución de los Comuneros del Paraguay (siglo XVIII) y por qué se invocó la Real Provisión.',
    ],
    'evaluacion': {
        'tipo': 'Formativa, con producto.',
        'procedimientos': 'Lectura segmentada; cuadros; debate guiado; texto comparativo.',
        'instrumentos': 'Cuadros de las consignas 1 y 2; registro del debate; consigna 5 con los criterios de su consigna.',
        'criterios': ['Distingue lo que la norma autorizaba y lo que no.',
                      'Argumenta con datos y con la norma, y considera la posición contraria.',
                      'Compara con dos diferencias y una semejanza.'],
    },
    'precisiones': [
        'El debate no tiene una única respuesta correcta: se evalúa que los argumentos usen datos y la norma de 1537.',
        'Los Comentarios de Cabeza de Vaca son una fuente parcial, escrita en su defensa; tratarlos como una versión, no como la verdad.',
    ],
    'tarea': 'Terminar la consigna 4 y la autoevaluación si quedaron pendientes. Repasar las Clases 6 a 10 y las Continuaciones C y D para la Evaluación de la Unidad 3.',
}

SOL = {
    'bloques': [
        ('Consignas del taller', [
            ('1', 'Autorizaba: elegir gobernador cuando faltaba la autoridad; que eligieran los conquistadores y pobladores; elegir a la '
                  'persona más capaz; que el elegido gobernara en nombre del rey. No autorizaba: elegir cuando había gobernador '
                  'nombrado por el rey; destituir a un gobernador; que votaran indígenas o mujeres; gobernar con independencia del rey; '
                  'elecciones periódicas.', 'Al menos tres filas coherentes con la síntesis de la norma.'),
            ('2', 'Cabildo: alcaldes y regidores; justicia y gobierno de la ciudad; sí. Obispado: obispo y sacerdotes; vida religiosa; no '
                  'gobernaba la ciudad. Encomienda: encomendero e indígenas encomendados; asignar trabajo o tributo indígena a un '
                  'español; no.', 'Una casilla por institución y columna; se aceptan expresiones equivalentes.'),
            ('3', 'Respuesta abierta. Argumentos posibles por el «no»: Cabeza de Vaca era un gobernador nombrado por el rey, no faltaba la '
                  'autoridad; la norma no autorizaba destituir. Por el «sí»: los vecinos se sentían con derecho a decidir sobre su '
                  'gobierno; Irala, que gobernó después, había sido reconocido antes por los conquistadores.',
             'Dos argumentos propios con datos o con la norma y uno contrario registrado con fidelidad.'),
            ('4', 'Ejemplo con la municipalidad: semejanza, se ocupa de asuntos de la ciudad (limpieza, obras, mercados); diferencia, hoy '
                  'sus autoridades se eligen por voto de la ciudadanía en elecciones periódicas.', 'Una semejanza y una diferencia correctas.'),
            ('5', 'Ejemplo: «En 1537 solo podían elegir los conquistadores y pobladores españoles, y solo cuando faltaba el gobernador; hoy '
                  'votan todas las ciudadanas y los ciudadanos desde los 18 años, en fechas fijas. En ambos casos se elige a quien va a '
                  'gobernar. Pero en 1537 el elegido gobernaba en nombre del rey y de manera provisional: era una autonomía limitada, '
                  'no una democracia.»',
             'Criterio anunciado en la consigna: dos diferencias con datos (2 puntos), una semejanza (1 punto) y una conclusión sobre '
             'los límites de la autonomía de 1537 (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Cabeza de Vaca: medidas para limitar las rancheadas; deposición en 1544; Comentarios publicados en 1555 con su secretario (Pero Hernández)',
     'Datos habituales de la bibliografía; cotejar.'),
    ('Síntesis de las partes de la Real Provisión', 'Paráfrasis editorial basada en los fragmentos de la Clase 10 (transcripción de Rivarola Paoli); no es cita.'),
]
