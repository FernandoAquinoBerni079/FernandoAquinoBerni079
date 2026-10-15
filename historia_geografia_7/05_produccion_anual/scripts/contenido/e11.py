"""Encuentro 11 — Clase 7: El reparto de América y el gobierno colonial (H4; temas H4c y H4d).

Corrige el maestro: opción múltiple con dos respuestas correctas, actividades
que contradecían el concepto de absolutismo, y falta de la Audiencia de
Charcas y de la fecha del Virreinato del Perú (1542).
"""
import curriculo as C

TITULO = 'Clase 7 — El reparto de América y el gobierno colonial'
CLAVE = 'Clase 7 —'
INDICADORES = [
    'Explica cómo se repartieron los territorios americanos España y Portugal y por qué otras potencias no lo aceptaron.',
    'Describe características del colonialismo español y su repercusión en los pueblos indígenas.',
    'Explica qué era el gobierno absolutista y cómo se proyectaba en América a través de sus autoridades.',
    'Ubica al Paraguay dentro del Virreinato del Perú.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H4'], C.TEMAS['H4c'] + ' ' + C.TEMAS['H4d'], INDICADORES),

    ('h2', 'Un mundo repartido en dos'),
    ('p', 'Después del primer viaje de Colón, Castilla y Portugal discutieron a quién pertenecían las nuevas tierras. En 1493 el '
          'papa Alejandro VI dictó unas bulas que trazaban una línea en el Atlántico. Portugal no estuvo conforme y los dos reinos '
          'negociaron directamente: el 7 de junio de 1494 firmaron el Tratado de Tordesillas, que fijó una línea imaginaria de '
          'polo a polo a 370 leguas al oeste de las islas de Cabo Verde. Las tierras al oeste serían de Castilla y las del este, '
          'de Portugal (Figura 7.1). Por eso el Brasil quedó para Portugal.'),
    ('fig', 'fig_7_1_tordesillas.png', 'Figura 7.1 — La línea del Tratado de Tordesillas (1494), esquema aproximado.', 12.0),
    ('p', 'Otros reinos europeos, como Francia e Inglaterra, no aceptaron ese reparto, porque no habían participado. Durante los '
          'siglos XVI y XVII enviaron corsarios a atacar los barcos españoles y fundaron sus propias colonias en América del Norte '
          'y en el Caribe. Lo vas a estudiar en la Clase 15.'),

    ('h2', 'Los reyes absolutos'),
    ('p', 'En el siglo XVI, en los principales reinos de Europa, el rey concentró cada vez más poder: dictaba las leyes, era el '
          'juez supremo, cobraba impuestos, dirigía el ejército y nombraba a todos los funcionarios. Se decía que su poder venía '
          'de Dios y que no debía rendir cuentas a nadie más. A esa forma de gobierno se la llama monarquía absoluta o absolutismo. '
          'Carlos I (rey de 1516 a 1556) y su hijo Felipe II (de 1556 a 1598) gobernaron así un enorme conjunto de territorios en '
          'Europa y en América.'),
    ('caja', 'concepto', 'Concepto clave — ',
     'En una monarquía absoluta el poder no está dividido: el rey dicta las leyes, juzga y gobierna. Hoy, en una república '
     'democrática como el Paraguay, el poder se divide en Legislativo, Ejecutivo y Judicial, y las autoridades son elegidas y '
     'responden ante la ley.'),

    ('h2', 'Cómo se gobernaba América desde España'),
    ('p', 'El rey gobernaba sus territorios americanos desde España con ayuda de dos instituciones: la Casa de Contratación, '
          'creada en Sevilla en 1503, que controlaba el comercio y la navegación con América, y el Consejo de Indias, creado en '
          '1524, que preparaba las leyes para América y proponía al rey los nombramientos.'),
    ('p', 'En América, el rey estaba representado por los virreyes, que gobernaban grandes territorios llamados virreinatos. En el '
          'siglo XVI se crearon dos: el de Nueva España (1535), con capital en México, y el del Perú (1542), con capital en Lima. '
          'Las audiencias eran tribunales de justicia que también controlaban a los gobernantes; para nuestra región, la Audiencia '
          'de Charcas (en la actual Bolivia) se creó en 1559. Las gobernaciones, como la del Río de la Plata y del Paraguay, '
          'estaban a cargo de un gobernador, y cada ciudad tenía su cabildo (Figura 7.2).'),
    ('fig', 'fig_7_2_gobierno.png', 'Figura 7.2 — El gobierno de las colonias españolas en el siglo XVI (esquema simplificado).', 15.0),
    ('caja', 'paraguay', 'En Paraguay — ',
     'El Paraguay formó parte del Virreinato del Perú desde su creación en 1542. Las órdenes del rey llegaban a Asunción después '
     'de meses de viaje, por Lima o por el Atlántico. Esa distancia dio a las autoridades locales y al Cabildo de Asunción mucho '
     'margen para decidir por sí mismos.'),

    ('h2', 'El colonialismo español y los pueblos indígenas'),
    ('p', 'El colonialismo es el dominio de un Estado sobre territorios y pueblos lejanos, que quedan subordinados a sus intereses. '
          'El colonialismo español tuvo algunos rasgos principales: las colonias dependían de la Corona de Castilla; el comercio '
          'era un monopolio, es decir, solo podía hacerse con España, en flotas controladas; la Iglesia acompañó la conquista con '
          'la evangelización; y el trabajo indígena se organizó en beneficio de los colonizadores, con instituciones como la '
          'encomienda y la mita.'),
    ('p', 'Para los pueblos indígenas, la repercusión fue enorme: perdieron tierras, debieron pagar tributos y trabajar para los '
          'españoles, y su población cayó por las epidemias y los abusos. Pero no fueron solo víctimas: muchos resistieron con las '
          'armas o huyendo, y otros se adaptaron para sobrevivir. Los caciques actuaron como intermediarios entre su pueblo y las '
          'autoridades españolas, y en los pueblos de indios se crearon cabildos indígenas. La Corona dictó leyes para protegerlos, '
          'como las Leyes Nuevas de 1542, que a menudo no se cumplieron.'),

    ('fuente', 'Fuente escrita · Tratado de Tordesillas (7 de junio de 1494). Versión escolar resumida (no es cita textual) de la '
               'cláusula principal.',
     ['Los reyes de Castilla y de Portugal acuerdan que se trace en el mar Océano una raya o línea derecha de polo a polo, a '
      'trescientas setenta leguas de las islas de Cabo Verde hacia el poniente. Todo lo hallado o por hallar al oriente de esa '
      'línea será del rey de Portugal, y todo lo que está al occidente, de los reyes de Castilla.'],
     'Vocabulario: poniente u occidente, oeste; oriente, este; legua, medida de distancia de algo más de 5 km.',
     ['¿Quiénes firmaron el tratado y en qué año?',
      '¿Qué tierras correspondían a Portugal y cuáles a Castilla?',
      '¿Quiénes no participaron de este acuerdo, aunque vivían en las tierras repartidas? ¿Qué te dice eso sobre el colonialismo?']),
    ('renglones', 6),
    ('ubicate', 'Ubicate  ·  Mapa (Figura 7.1)',
     'Ubicá la línea de Tordesillas. ¿Qué parte de América del Sur quedó del lado portugués? ¿De qué lado quedó el actual Paraguay?'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. El Tratado de Tordesillas (1494) fue firmado por…'),
    ('opc', ['Castilla y Francia', 'Castilla e Inglaterra', 'Castilla y Portugal', 'Portugal y Holanda']),
    ('item', '2. En una monarquía absoluta…'),
    ('opc', ['el poder se divide en tres poderes independientes', 'el rey concentra el poder de hacer leyes, juzgar y gobernar',
             'los ciudadanos eligen al rey cada cinco años', 'el Cabildo controla al rey']),
    ('item', '3. Desde su creación en 1542, el Paraguay formó parte del Virreinato…'),
    ('opc', ['de Nueva España', 'del Río de la Plata', 'de Nueva Granada', 'del Perú']),
    ('item', '4. La Casa de Contratación de Sevilla se ocupaba de…'),
    ('opc', ['controlar el comercio y la navegación con América', 'juzgar los delitos cometidos en Asunción',
             'elegir a los caciques de los pueblos de indios', 'redactar la Constitución']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. El tribunal de justicia creado en 1559 para nuestra región fue la Audiencia de ________.'),
    ('item', '6. El comercio que solo podía hacerse con España se llamaba ________.'),
    ('item', '7. Los ________ actuaban como intermediarios entre su pueblo y las autoridades españolas.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) Francia e Inglaterra aceptaron el reparto de Tordesillas.'),
    ('item', '9. (....) El Consejo de Indias preparaba las leyes para América y proponía nombramientos al rey.'),
    ('item', '10. (....) Los pueblos indígenas aceptaron sin resistencia el dominio español.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. Ordená de mayor a menor alcance territorial estas autoridades y explicá qué hacía cada una: cabildo, rey, '
             'virrey, gobernador.', 5),
    ('item', '12. Compará el gobierno absolutista del siglo XVI con el gobierno del Paraguay actual. Se tendrá en cuenta: quién '
             'hace las leyes en cada caso (1 punto), cómo se eligen las autoridades (1 punto) y una conclusión (1 punto).', 6),
]

PLAN = {
    'material': 'Tomo: Clase 7 (Figuras 7.1 y 7.2); planisferio',
    'tema': C.TEMAS['H4c'] + ' ' + C.TEMAS['H4d'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes expliquen el reparto de América, el absolutismo y la organización del gobierno colonial, '
                 'y reconozcan sus efectos sobre los pueblos indígenas.',
    'funciones': {
        'Esenciales': 'En clase: fuente (preguntas 1 a 3); Ubicate; actividades 1, 2, 3 y 11.',
        'Consolidación': 'Actividades 4, 5, 8 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 12).',
        'Complementarias o domiciliarias': 'Actividades 6, 7, 10 y 12.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 6. Pregunta: «¿Quién decidió de quién eran las tierras americanas?».',
             'Responden y discuten.', 'Ideas en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–28', 'Lectura de «Un mundo repartido en dos» con la Figura 7.1 y la fuente resumida del tratado.',
             'Resuelven el «Ubicate», la actividad 1 y las preguntas 1 a 3 de la fuente.', 'Ubicate, actividad 1 y fuente (esenciales).'),
            ('28–45', 'Explica el absolutismo con el Concepto clave y lo compara con la división de poderes actual.',
             'Resuelven la actividad 2.', 'Actividad 2 (esencial).'),
            ('45–65', 'Explica las autoridades con la Figura 7.2 y la caja «En Paraguay».',
             'Resuelven las actividades 3 y 11.', 'Actividades 3 y 11 (esenciales).'),
            ('65–85', 'Lectura de «El colonialismo español y los pueblos indígenas».',
             'En parejas anotan dos formas de resistencia o adaptación indígena.', 'Lista de formas de resistencia y adaptación.'),
            ('85–100', 'Acompaña; quien termina antes sigue con la consolidación.', 'Resuelven las actividades 4, 5, 8 y 9.',
             'Actividades de consolidación.'),
        ]),
        ('Cierre', [
            ('100–120', 'Revisa los errores frecuentes (virreinato, audiencia, absolutismo), lee los criterios de la actividad 12 y asigna la tarea.',
             'Corrigen con otro color lo que haga falta.', 'Errores frecuentes corregidos.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en la Figura 7.2: tarjetas con el nombre de cada autoridad para ordenar sobre el banco antes de escribir la actividad 11.',
        'Apoyo en la fuente: el docente dibuja en la pizarra el Atlántico, Cabo Verde y la línea, y marca «oeste» y «este».',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: investigar qué fueron las Leyes Nuevas de 1542 y por qué muchos encomenderos se opusieron.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Lectura de mapa; análisis de fuente; organización jerárquica de autoridades.',
        'instrumentos': 'Lista de cotejo con los cuatro indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Explica el reparto de Tordesillas y su consecuencia para el Brasil.',
                      'Define el absolutismo sin contradecir el Concepto clave.',
                      'Ordena las autoridades y ubica al Paraguay en el Virreinato del Perú.',
                      'Nombra efectos del colonialismo y formas de respuesta indígena.'],
    },
    'precisiones': [
        'El maestro tenía una opción múltiple con dos respuestas posibles (Perú y Río de la Plata): el Virreinato del Río de la Plata se creó recién en 1776, fuera del alcance del año.',
        'La fuente del tratado es una versión resumida, no textual.',
    ],
    'tarea': 'Actividades 6, 7, 10 y 12 de la Clase 7.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente', [
            ('F1', 'Los reyes de Castilla y el rey de Portugal, en 1494.', ''),
            ('F2', 'A Portugal, las tierras al este de la línea (de ahí el Brasil); a Castilla, las del oeste.', ''),
            ('F3', 'Los pueblos indígenas que vivían en América. Muestra que el colonialismo decidía sobre territorios y pueblos sin '
                   'tenerlos en cuenta.', 'Se valora que relacione la ausencia de los pueblos con el concepto de colonialismo.'),
        ]),
        ('Ubicate (Figura 7.1)', [
            ('U', 'Quedó del lado portugués el extremo oriental de América del Sur, parte del actual Brasil. El Paraguay quedó del '
                  'lado castellano, al oeste de la línea.', ''),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'c) Castilla y Portugal', ''),
            ('2', 'b) el rey concentra el poder de hacer leyes, juzgar y gobernar', ''),
            ('3', 'd) del Perú', ''),
            ('4', 'a) controlar el comercio y la navegación con América', ''),
        ]),
        ('Completá los espacios', [
            ('5', 'Charcas', ''),
            ('6', 'monopolio', ''),
            ('7', 'caciques', ''),
        ]),
        ('Verdadero o falso', [
            ('8', 'Falso: no lo aceptaron porque no habían participado; enviaron corsarios y fundaron sus colonias.', 'Justificación obligatoria.'),
            ('9', 'Verdadero.', ''),
            ('10', 'Falso: muchos resistieron con las armas o huyendo, y otros se adaptaron para sobrevivir.', 'Justificación obligatoria.'),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'Rey: gobernaba todos los territorios, dictaba las leyes. Virrey: representaba al rey en un virreinato. Gobernador: '
                   'gobernaba una provincia o gobernación. Cabildo: gobernaba una ciudad.', 'Orden correcto y una función de cada autoridad.'),
            ('12', 'Ejemplo: «En el siglo XVI el rey hacía las leyes, juzgaba y gobernaba; hoy las leyes las hace el Congreso. Antes '
                   'las autoridades eran nombradas por el rey; hoy se eligen con el voto de los ciudadanos. Por eso hoy el poder está '
                   'dividido y controlado, y en el absolutismo no.»',
             'Criterio anunciado en la consigna: quién hace las leyes en cada caso (1 punto), cómo se eligen las autoridades (1 punto) y una conclusión (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Tratado de Tordesillas: 7 de junio de 1494, 370 leguas al oeste de Cabo Verde; bulas de 1493', 'Datos habituales; la fuente es una versión resumida. Cotejar con una edición del tratado.'),
    ('Casa de Contratación 1503; Consejo de Indias 1524; Virreinato de Nueva España 1535 y del Perú 1542; Audiencia de Charcas 1559', 'Fechas habituales; cotejar.'),
    ('Meridiano aproximado de 46° O en la Figura 7.1', 'Valor aproximado de uso escolar; la ubicación se discutió durante siglos.'),
]
