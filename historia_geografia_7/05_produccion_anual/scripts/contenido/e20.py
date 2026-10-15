"""Encuentro 20 — Clase 12: Economía y situación de los indígenas en el siglo XVII (H5; temas H5b y H5c).

Corrige el maestro: agrega las Ordenanzas de Alfaro (1611), el trabajo en los
yerbales, las malocas y la moneda de la tierra; explica que convivían una
economía de subsistencia y un sector exportador; matiza la composición
mestiza (el sector «español» era en gran parte mestizo, y había una numerosa
población indígena en pueblos y reducciones).
"""
import curriculo as C

TITULO = 'Clase 12 — Economía y situación de los indígenas en el siglo XVII'
CLAVE = 'Clase 12 —'
INDICADORES = [
    'Describe la economía de la provincia: subsistencia, yerba mate y moneda de la tierra.',
    'Explica qué establecían las Ordenanzas de Alfaro y por qué se cumplieron poco.',
    'Describe la situación de los indígenas en encomiendas, pueblos y yerbales.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H5'], C.TEMAS['H5b'] + ' ' + C.TEMAS['H5c'], INDICADORES),

    ('h2', 'Una economía para vivir'),
    ('p', 'En el siglo XVII, la mayor parte de la población de la provincia vivía de lo que producía en chacras y estancias: maíz, '
          'mandioca, porotos, batata, algodón para tejer, caña de azúcar y ganado vacuno. Era una economía de subsistencia: se '
          'producía sobre todo para comer y vestirse, y poco se vendía.'),
    ('h2', 'La yerba mate, el «oro verde»'),
    ('p', 'El producto que la provincia vendía afuera era la yerba mate. Crecía en forma natural en los montes del noreste y del '
          'este, en las regiones de Mbaracayú y del Guairá. Grupos de trabajadores indígenas, sobre todo mitayos de las encomiendas, '
          'pasaban meses en los yerbales cortando, secando y cargando la yerba. El trabajo era muy duro y muchos morían por las '
          'enfermedades, el hambre y el maltrato.'),
    ('p', 'La yerba bajaba en barcos hasta Santa Fe y se redistribuía por rutas diferentes: una hacia Buenos Aires y el Atlántico, y otras hacia Córdoba, el Alto Perú (Potosí) y Chile, así como a '
          'otras ciudades. Así, aunque no tenía minas, el Paraguay estaba conectado con la economía de la plata. El tabaco y los '
          'lienzos de algodón eran otros productos de venta.'),
    ('fig', 'fig_12_1_yerba.png', 'Figura 12.1 — Las dos economías de la provincia en el siglo XVII (esquema).', 15.0),
    ('h2', 'Sin monedas: la moneda de la tierra'),
    ('p', 'En la provincia casi no circulaban monedas de metal. Por eso se usaba la «moneda de la tierra»: se pagaba con yerba, '
          'tabaco, lienzo de algodón o ganado, según valores que fijaban las autoridades. Esto muestra la pobreza de la provincia y '
          'su dependencia de los compradores de afuera.'),

    ('h2', 'La sociedad'),
    ('p', 'Los vecinos llamados «españoles» eran en gran parte mestizos, hijos y nietos de las uniones del siglo XVI, y hablaban '
          'guaraní. Junto a ellos vivía una población indígena numerosa: en los pueblos de indios administrados por franciscanos y '
          'sacerdotes, en las reducciones jesuíticas y en las casas y chacras de los encomenderos. Había también pueblos que no '
          'aceptaron el dominio español, sobre todo en el Chaco.'),

    ('h2', 'La situación de los indígenas y las Ordenanzas de Alfaro'),
    ('p', 'Los indígenas encomendados trabajaban en las chacras, en las casas de los encomenderos y en los yerbales. Los abusos '
          'eran tantos que la Corona envió a un visitador, el oidor Francisco de Alfaro. En 1611 dictó las Ordenanzas de Alfaro, '
          'que prohibían el servicio personal (el trabajo obligatorio y sin pago para los encomenderos), mandaban pagar el trabajo, '
          'limitaban la mita y protegían la vida de los indígenas en sus pueblos.'),
    ('p', 'En la práctica, las ordenanzas se cumplieron poco: los encomenderos protestaron, las autoridades estaban lejos y la '
          'economía de la provincia dependía del trabajo indígena. A esto se sumaron las malocas: expediciones de cazadores de '
          'esclavos que llegaban desde São Paulo, en el Brasil, y capturaban a miles de indígenas. Lo vas a estudiar en la '
          'Continuación E.'),
    ('caja', 'concepto', 'Concepto clave — ',
     'Servicio personal: trabajo obligatorio y sin pago que los indígenas encomendados prestaban a su encomendero. '
     'Mita: trabajo por turnos. Las Ordenanzas de Alfaro (1611) prohibieron el servicio personal, pero no lograron terminar con los abusos.'),

    ('fuente', 'Documento de época · Ordenanzas de Alfaro (1611). Versión escolar resumida: no es cita textual.',
     ['Se prohíbe el servicio personal de los indios. Los indios que trabajen para los españoles deben recibir su pago. '
      'Ningún indio puede ser llevado a trabajar lejos de su pueblo contra su voluntad. Los indios deben vivir en sus pueblos, '
      'con sus autoridades, y tener tierras para sus cultivos.'],
     'Vocabulario: ordenanza es una norma dictada por una autoridad; visitador, el funcionario enviado a inspeccionar una región.',
     ['¿Qué problema querían resolver las ordenanzas? Citá una frase de la versión resumida.',
      '¿Quiénes se perjudicaban con estas normas? ¿Por qué?',
      'Si las ordenanzas se cumplieron poco, ¿qué otro tipo de fuente usarías para saber cómo vivían en realidad los indígenas?']),
    ('renglones', 6),
    ('ubicate', 'Ubicate  ·  Esquema (Figura 12.1) y mapa (Figura 11.1)',
     'En la Figura 12.1, ¿dónde estaban los yerbales y por qué ciudades pasaba la yerba hasta los mercados? Buscá esas ciudades en '
     'la Figura 11.1: ¿a qué gobernación pertenecía cada una?'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. El principal producto que la provincia del Paraguay vendía afuera en el siglo XVII era…'),
    ('opc', ['la plata', 'el azúcar', 'la yerba mate', 'el trigo']),
    ('item', '2. La «moneda de la tierra» era…'),
    ('opc', ['el pago con productos como yerba, tabaco o lienzo', 'una moneda de oro acuñada en Asunción', 'el nombre del tributo a la Corona',
             'una moneda de plata traída de Potosí']),
    ('item', '3. Las Ordenanzas de Alfaro (1611)…'),
    ('opc', ['crearon las encomiendas', 'dividieron la provincia en dos gobernaciones', 'autorizaron las malocas',
             'prohibieron el servicio personal de los indígenas']),
    ('item', '4. Las malocas eran…'),
    ('opc', ['pueblos fundados por los franciscanos', 'expediciones que capturaban indígenas para esclavizarlos', 'barcos que llevaban yerba',
             'reuniones del cabildo indígena']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. Los yerbales naturales estaban en las regiones de Mbaracayú y del ________.'),
    ('item', '6. El funcionario que dictó las ordenanzas de 1611 fue Francisco de ________.'),
    ('item', '7. Una economía que produce sobre todo para comer y vestirse se llama economía de ________.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) En la provincia circulaban muchas monedas de metal.'),
    ('item', '9. (....) Muchos vecinos llamados «españoles» eran en realidad mestizos y hablaban guaraní.'),
    ('item', '10. (....) Las Ordenanzas de Alfaro terminaron con todos los abusos contra los indígenas.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. ¿Por qué se dice que el Paraguay estaba conectado con la economía de la plata aunque no tenía minas?', 4),
    ('item', '12. Escribí un párrafo de 6 a 8 líneas sobre la situación de los indígenas en el siglo XVII. Se tendrá en cuenta: dos '
             'lugares donde trabajaban (1 punto), qué establecían las Ordenanzas de Alfaro (1 punto), por qué se cumplieron poco '
             '(1 punto) y un texto ordenado (1 punto).', 8),
]

PLAN = {
    'material': 'Tomo: Clase 12 (Figura 12.1) y Figura 11.1 de la Clase 11',
    'tema': C.TEMAS['H5b'] + ' ' + C.TEMAS['H5c'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes describan la economía de la provincia en el siglo XVII y la situación de los indígenas, '
                 'y expliquen la distancia entre las normas y la práctica.',
    'funciones': {
        'Esenciales': 'En clase: Ubicate; fuente (preguntas 1 a 3); actividades 1, 2, 3, 4 y 11.',
        'Consolidación': 'Actividades 5, 6, 8 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 21).',
        'Complementarias o domiciliarias': 'Actividades 7, 10 y 12.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 11. Pregunta: «Si no hubiera billetes ni monedas, ¿cómo pagarías?».',
             'Proponen ejemplos de trueque.', 'Ideas en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–30', 'Lectura de «Una economía para vivir», «La yerba mate» y «Sin monedas», con la Figura 12.1.',
             'Resuelven el «Ubicate» y las actividades 1 y 2.', 'Ubicate y actividades 1 y 2 (esenciales).'),
            ('30–50', 'Lectura de «La sociedad» y de «La situación de los indígenas». Explica servicio personal y mita con el Concepto clave.',
             'Resuelven las actividades 3 y 4.', 'Actividades 3 y 4 (esenciales).'),
            ('50–70', 'Presenta la versión resumida de las Ordenanzas de Alfaro y aclara que no es cita textual.',
             'Responden las preguntas 1 a 3 de la fuente.', 'Fuente (esencial).'),
            ('70–82', 'Plantea la pregunta de la actividad 11 y la resuelve con el grupo en la pizarra a partir de la Figura 12.1.',
             'Escriben la actividad 11.', 'Actividad 11 (esencial).'),
            ('82–100', 'Acompaña; quien termina antes sigue con la consolidación.', 'Resuelven las actividades 5, 6, 8 y 9.',
             'Actividades de consolidación.'),
        ]),
        ('Cierre', [
            ('100–120', 'Puesta en común de la pregunta 3 de la fuente: norma y realidad no siempre coinciden. Lee los criterios de la actividad 12 y asigna la tarea.',
             'Comentan y corrigen.', 'Fuente revisada.'),
        ]),
    ],
    'diversidad': [
        'Variante si la devolución de la Evaluación Integradora de la 1.ª etapa se posterga a este encuentro: 0 a 20 minutos, devolución con claves (sin revelarlas a quien todavía debe rendir); 20 a 120, la clase en 100 minutos. Se mantienen en clase todas las esenciales (Ubicate; fuente, preguntas 1 a 3; actividades 1, 2, 3, 4 y 11). Las de consolidación (5, 6, 8 y 9) pasan a casa, con revisión breve al abrir el encuentro 21; las complementarias quedan como tarea optativa.',
        'Apoyo en vocabulario: glosario en la pizarra (subsistencia, mitayo, servicio personal, ordenanza, visitador, maloca).',
        'Apoyo en la actividad 11: ramificación dada en la pizarra «yerba → Santa Fe → Buenos Aires / Córdoba y mercados interiores (Potosí y Chile)».',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: averiguar cómo se prepara la yerba hoy y compararlo con el trabajo en los yerbales del siglo XVII.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Lectura de esquema; análisis de fuente; respuesta breve.',
        'instrumentos': 'Lista de cotejo con los tres indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Distingue la economía de subsistencia del comercio de la yerba y explica la moneda de la tierra.',
                      'Explica qué establecían las Ordenanzas de Alfaro.',
                      'Describe la situación de los indígenas sin omitir la distancia entre norma y práctica.'],
    },
    'precisiones': [
        'Error frecuente: pensar que la economía paraguaya producía sobre todo para exportar. Convivían la subsistencia y la venta de yerba.',
        'Las Ordenanzas de Alfaro se presentan en versión escolar resumida; no leerlas como cita textual.',
    ],
    'tarea': 'Actividades 7, 10 y 12 de la Clase 12.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente', [
            ('F1', 'Los abusos del servicio personal: el trabajo obligatorio y sin pago. Frase: «Se prohíbe el servicio personal de los indios».', ''),
            ('F2', 'Los encomenderos, porque perdían trabajo gratuito y tenían que pagar a los indígenas.', ''),
            ('F3', 'Fuentes que muestren la práctica: quejas de caciques, informes de visitadores, juicios, cartas de sacerdotes o cuentas de los yerbales.',
             'Se acepta cualquier fuente que muestre lo que ocurría en realidad.'),
        ]),
        ('Ubicate (Figuras 12.1 y 11.1)', [
            ('U', 'Los yerbales estaban en Mbaracayú y el Guairá. La yerba salía desde Asunción hacia Santa Fe y desde allí se distribuía por rutas diversas hacia Buenos Aires, Córdoba, Potosí, '
                  'Chile y otros mercados. Asunción era de la gobernación del Paraguay; Santa Fe y Buenos Aires, del Río de la Plata.', ''),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'c) la yerba mate', ''),
            ('2', 'a) el pago con productos como yerba, tabaco o lienzo', ''),
            ('3', 'd) prohibieron el servicio personal de los indígenas', ''),
            ('4', 'b) expediciones que capturaban indígenas para esclavizarlos', ''),
        ]),
        ('Completá los espacios', [
            ('5', 'Guairá', ''),
            ('6', 'Alfaro', ''),
            ('7', 'subsistencia', ''),
        ]),
        ('Verdadero o falso', [
            ('8', 'Falso: casi no había monedas de metal; se usaba la moneda de la tierra.', 'Justificación obligatoria.'),
            ('9', 'Verdadero.', ''),
            ('10', 'Falso: se cumplieron poco por la resistencia de los encomenderos y la lejanía de las autoridades.', 'Justificación obligatoria.'),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'Porque vendía yerba mate en Potosí y el Alto Perú, donde se pagaba con la plata de las minas; así la provincia '
                   'participaba de ese circuito aunque no produjera plata.', 'Debe mencionar la yerba y su mercado minero.'),
            ('12', 'Ejemplo: «Los indígenas encomendados trabajaban en las chacras y en los yerbales, donde muchos morían. En 1611 las '
                   'Ordenanzas de Alfaro prohibieron el servicio personal y mandaron pagar el trabajo. Pero se cumplieron poco, porque '
                   'los encomenderos protestaron y las autoridades estaban lejos.»',
             'Criterio anunciado en la consigna: dos lugares donde trabajaban (1 punto), qué establecían las Ordenanzas de Alfaro '
             '(1 punto), por qué se cumplieron poco (1 punto) y un texto ordenado (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Ordenanzas de Alfaro (1611): contenido resumido', 'Versión escolar resumida y declarada como no textual; cotejar con una edición de las ordenanzas.'),
    ('Yerbales de Mbaracayú y del Guairá; trabajo de mitayos y mortalidad', 'Bibliografía habitual; cotejar.'),
    ('Moneda de la tierra (valores fijados por las autoridades)', 'Bibliografía habitual; cotejar.'),
    ('Composición de la sociedad (sector «español» mayormente mestizo)', 'Interpretación habitual; proporciones no cuantificadas.'),
]
