"""Encuentro 5 — Evaluación de la Unidad 1 (asociación curricular: H1).

Regla de equidad (A10, aplicada a las ocho evaluaciones): nadie recibe claves
mientras alguien sigue rindiendo. La devolución con claves se hace en los
primeros 20 minutos del encuentro siguiente, cuyo plan reserva ese tiempo.
"""

TITULO = 'Evaluación de la Unidad 1 — Cómo mirar el tiempo y el espacio'
CLAVE = 'EVALUACIÓN DE LA UNIDAD 1'
PUNTAJE = 23

TOMO = [
    ('banda', 'EVALUACIÓN DE LA UNIDAD 1', 'Cómo mirar el tiempo y el espacio · Los primeros pobladores y los guaraníes'),
    ('datos',),
    ('p', f'Tiempo: 70 minutos. Puntaje total: {PUNTAJE} puntos. Todo lo que necesitás está en esta prueba, incluido el mapa de la Parte C.'),
    ('consigna', 'Parte A — Marcá la opción correcta (1 punto cada una).'),
    ('item', '1. La arqueología estudia…'),
    ('opc', ['los documentos escritos de los cabildos', 'los restos materiales del pasado', 'las lenguas que se hablan hoy',
             'los mapas antiguos de los navegantes']),
    ('item', '2. Una diferencia entre las sociedades cazadoras-recolectoras y las formaciones tribales es que estas últimas…'),
    ('opc', ['no tenían ningún tipo de organización', 'desconocían el uso del fuego', 'practicaban la agricultura y vivían en aldeas',
             'vivían solo en la Región Occidental']),
    ('item', '3. Los aché eran…'),
    ('opc', ['agricultores del Chaco que vivían en ciudades', 'cazadores-recolectores de los bosques de la Región Oriental',
             'un pueblo de la familia lingüística zamuco', 'los conquistadores que fundaron Asunción']),
    ('item', '4. El tekoha es…'),
    ('opc', ['el territorio donde se vive según el modo de ser guaraní', 'un tipo de vasija de cerámica', 'el líder de la aldea',
             'una danza ritual']),
    ('item', '5. La agricultura de roza consiste en…'),
    ('opc', ['regar los campos con canales', 'usar arados tirados por bueyes', 'cultivar en terrazas en las montañas',
             'cortar y quemar un sector del bosque y cultivarlo algunos años']),
    ('item', '6. Según el censo de 2012, el pueblo qom pertenece a la familia lingüística…'),
    ('opc', ['guaraní', 'zamuco', 'guaicurú', 'mataco mataguayo']),
    ('consigna', 'Parte B — Verdadero o falso. Justificá las falsas (1 punto cada una: si es verdadera, 1 punto por marcarla bien; '
                 'si es falsa, 0,5 por marcarla y 0,5 por la justificación).'),
    ('item', '7. (....) La prehistoria del Paraguay se conoce sobre todo por documentos escritos.'),
    ('item', '8. (....) Las mujeres guaraníes cultivaban las chacras y fabricaban la cerámica.'),
    ('item', '9. (....) El mburuvicha gobernaba por la fuerza, con un ejército permanente.'),
    ('item', '10. (....) Hoy viven en el Paraguay pueblos indígenas de cinco familias lingüísticas.'),
    ('consigna', 'Parte C — Mapa (4 puntos: 1 por cada elemento bien ubicado y nombrado).'),
    ('item', '11. En el mapa: a) escribí «Región Oriental» y «Región Occidental (Chaco)» en su lugar; b) repasá con color el río '
             'que separa las dos regiones y escribí su nombre; c) marcá con una X el río Pilcomayo.'),
    ('fig', 'eval_u1_mapa.png', 'Mapa para la Parte C. Elaboración propia con datos de Natural Earth (dominio público); mapa aproximado.', 9.0),
    ('consigna', 'Parte D — Análisis de fuente (4 puntos: 2 por cada respuesta; 1 por la idea correcta y 1 por usar un dato de la fuente).'),
    ('p', 'Fuente · Nombres actuales de lugares del Paraguay: Ypacaraí, Ypané, Ypoá, Itá, Itauguá, Caaguazú. En guaraní, y significa '
          '«agua»; ita, «piedra»; ka\'a, «hierba» o «monte»; guasu, «grande».'),
    ('item', '12. ¿Qué tienen en común los nombres Ypacaraí, Ypané e Ypoá? ¿Qué muestran sobre la relación de los guaraníes con el agua?', 3),
    ('item', '13. ¿Por qué estos nombres son una prueba del legado guaraní en el Paraguay de hoy?', 3),
    ('consigna', 'Parte E — Desarrollo (5 puntos).'),
    ('item', '14. Explicá cómo se organizaba una aldea guaraní. Escribí entre 6 y 8 líneas. Se tendrá en cuenta (1 punto cada uno): '
             'el parentesco y la casa comunal, la reciprocidad (jopói), la autoridad del mburuvicha, el papel de las mujeres y '
             'un texto ordenado.', 8),
    ('h3', 'Al terminar la prueba: autoevaluación de la unidad'),
    ('p', 'Completala cuando termines la prueba, antes de entregarla. No lleva nota: sirve para saber qué repasar.'),
    ('tabla', ['Puedo…', 'Sí', 'Con ayuda', 'Todavía no'], [['Explicar cómo se conoce la prehistoria.', '', '', ''], ['Diferenciar cazadores-recolectores y formaciones tribales.', '', '', ''], ['Ubicar las dos regiones y sus ríos en un mapa.', '', '', ''], ['Explicar la organización y el legado de los guaraníes.', '', '', '']], [5.5, 1.5, 1.5, 1.5]),
    ('p', 'La parte de la prueba que me resultó más difícil fue… y la voy a repasar así:'),
    ('renglones', 4)
]

PLAN = {
    'material': 'Tomo: Evaluación de la Unidad 1 (fotocopiada o en el cuadernillo; ya incluye el mapa de la Parte C)',
    'tema': 'Evaluación de las Clases 2 y 3 y de la Continuación A. La Clase 1 es introductoria y se evalúa de forma formativa.',
    'indicadores': ['Explica cómo se conoce la prehistoria y diferencia cazadores-recolectores de formaciones tribales.',
                    'Ubica las dos regiones naturales y sus ríos principales.',
                    'Explica la organización, la economía y el legado guaraní.',
                    'Analiza una fuente lingüística y fundamenta con datos.'],
    'proposito': 'Comprobar los logros de la Unidad 1 en condiciones iguales para todos y preparar la devolución del encuentro 6.',
    'funciones': {
        'Material que recibe cada estudiante': 'La prueba del tomo, que ya incluye el mapa. No se usa ninguna otra ficha.',
        'Criterios de puntaje': f'Figuran en cada parte de la prueba: A 6, B 4, C 4, D 4 y E 5 (total {PUNTAJE}).',
        'Devolución': 'Con claves y criterios, en los primeros 20 minutos del encuentro 6, cuando todas las pruebas están entregadas.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Explica la estructura (Partes A a E), el puntaje de cada parte y el tiempo. Lee en voz alta los criterios de la Parte E.',
             'Leen toda la prueba y preguntan dudas de consigna.', '—'),
        ]),
        ('Desarrollo', [
            ('10–80', 'Supervisa la resolución individual; solo aclara consignas.', 'Resuelven las Partes A a E.', 'Prueba.'),
            ('80–95', 'Tiempo adicional supervisado para quienes lo necesitan (hasta 15 minutos). Los demás completan la autoevaluación, entregan y pasan a la lectura sin claves.',
             'Quienes tienen tiempo adicional siguen la prueba; el resto lee en silencio la clase siguiente.', 'Entrega de todas las pruebas.'),
        ]),
        ('Cierre', [
            ('95–120', 'Con todas las pruebas entregadas, propone una actividad sin claves: lectura de anticipación de la Clase 4 y comentario oral sobre qué parte resultó más difícil, sin hablar de respuestas. No se corrige ni se comentan respuestas.',
             'Leen y comentan.', 'Comentario oral (no lleva nota).'),
        ]),
    ],
    'diversidad': [
        'Tiempo adicional de hasta 15 minutos (80 a 95), supervisado y sin corrección simultánea: nadie recibe respuestas antes de que terminen todos.',
        'Si un estudiante necesita más de 15 minutos adicionales, completa la prueba antes del encuentro 6 en un horario de apoyo acordado con la dirección, bajo supervisión y con la prueba custodiada por el docente. La devolución con claves se hace recién cuando esa prueba está entregada.',
        'Lectura en voz alta de las consignas para quien lo necesite, sin explicar contenidos.',
    ],
    'evaluacion': {
        'tipo': 'Sumativa de unidad; devolución formativa en el encuentro 6.',
        'procedimientos': 'Prueba escrita; ubicación en mapa; análisis de fuente; respuesta desarrollada.',
        'instrumentos': 'Prueba de la Unidad 1 del tomo; claves, criterios y matriz ítem-capacidad-puntaje del solucionario.',
        'criterios': [f'Total: {PUNTAJE} puntos (A 6; B 4; C 4; D 4; E 5). La calificación se obtiene con la escala de la institución.',
                      'La Parte E se corrige con los cinco criterios impresos en la consigna.'],
    },
    'precisiones': [
        'La prueba evalúa la capacidad H1 (Clases 2 y 3 y Continuación A). Los contenidos de la Clase 1 se evalúan de forma formativa.',
        'Primeros 20 minutos del encuentro 6: devolución con claves y criterios; el Plan 6 reserva ese tiempo.',
    ],
    'tarea': 'Leer la introducción de la Clase 4 (sin actividades).',
}

SOL = {
    'puntaje': PUNTAJE,
    'bloques': [
        ('Parte A — 1 punto cada una', [
            ('1', 'b) los restos materiales del pasado', ''),
            ('2', 'c) practicaban la agricultura y vivían en aldeas', ''),
            ('3', 'b) cazadores-recolectores de los bosques de la Región Oriental', ''),
            ('4', 'a) el territorio donde se vive según el modo de ser guaraní', ''),
            ('5', 'd) cortar y quemar un sector del bosque y cultivarlo algunos años', ''),
            ('6', 'c) guaicurú', ''),
        ]),
        ('Parte B — 1 punto cada una', [
            ('7', 'Falso: como no hay escritura, se conoce sobre todo por la arqueología.',
             'Criterio anunciado en la Parte B: si es verdadera, 1 punto por marcarla bien; si es falsa, 0,5 por marcarla y 0,5 por la justificación.'),
            ('8', 'Verdadero.', ''),
            ('9', 'Falso: su autoridad se basaba en el prestigio, la generosidad y la palabra.', ''),
            ('10', 'Verdadero.', ''),
        ]),
        ('Parte C — 4 puntos', [
            ('11', 'Región Oriental al este del río Paraguay; Región Occidental (Chaco) al oeste; río Paraguay repasado y nombrado; '
                   'X sobre el Pilcomayo, en el límite sudoeste con la Argentina.',
             'Criterio anunciado en la Parte C: 1 por cada elemento bien ubicado y nombrado. Parcial: 0,5 si el elemento está bien '
             'ubicado pero sin nombre o mal nombrado. Se corrige sobre el mapa impreso en la prueba; ver la clave gráfica.'),
        ]),
        ('Parte D — 4 puntos', [
            ('12', 'Todos empiezan con «y», que significa «agua». Muestran que el agua (ríos, lagos, esteros) era un elemento '
                   'importante del ambiente guaraní y servía para orientarse y nombrar los lugares.',
             'Criterio anunciado en la Parte D: 2 por cada respuesta; 1 por la idea correcta y 1 por usar un dato de la fuente.'),
            ('13', 'Porque son palabras guaraníes que se siguen usando hoy para nombrar ciudades, lagos y ríos del Paraguay: la '
                   'lengua guaraní sigue viva en el territorio.', ''),
        ]),
        ('Parte E — 5 puntos', [
            ('14', 'Ejemplo: «La aldea guaraní estaba formada por varias casas comunales; en cada una vivía una familia extensa unida '
                   'por el parentesco. Los bienes circulaban por la reciprocidad o jopói: quien cazaba o cosechaba mucho compartía, y '
                   'eso le daba prestigio. El mburuvicha no mandaba por la fuerza, sino por su prestigio y generosidad. Las mujeres '
                   'cultivaban las chacras, hacían la cerámica y enseñaban la lengua a los hijos.»',
             'Criterio anunciado en la consigna (1 punto cada uno): el parentesco y la casa comunal, la reciprocidad (jopói), la '
             'autoridad del mburuvicha, el papel de las mujeres y un texto ordenado.'),
        ]),
    ],
    'mapas': [('eval_u1_mapa_clave.png', 9.0, 'Clave gráfica de la Parte C. Tolerancia: se aceptan los rótulos de región dentro '
               'de su región; el río Paraguay debe seguir el cauce central; la X del Pilcomayo, sobre su curso, en el límite sudoeste.')],
    'matriz': [
        ('1 a 6', 'H1', 'Prehistoria, formaciones, pueblos, tekoha, roza y familias lingüísticas (Clases 2 y 3).', 6),
        ('7 a 10', 'H1', 'Fuentes de la prehistoria, papel de las mujeres, autoridad y pueblos actuales.', 4),
        ('11', 'H1', 'Primeros pobladores de las regiones Oriental y Occidental: ubicación de regiones y ríos.', 4),
        ('12 y 13', 'H1', 'Legado e importancia de la lengua guaraní a partir de una fuente (Continuación A).', 4),
        ('14', 'H1', 'Organización guaraní basada en el parentesco y la reciprocidad; papel de las mujeres.', 5),
    ],
}

VERIFICACION = []
