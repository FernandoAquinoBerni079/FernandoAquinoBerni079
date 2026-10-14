"""Encuentro 7 — Clase 5: Mayas, aztecas e incas (H2; tema H2b).

Corrige los errores del maestro señalados en el diagnóstico: la chinampa no
flotaba; se agregan fechas, organización social y el problema del nombre
«prehistoria» para sociedades con escritura.
"""
import curriculo as C

TITULO = 'Clase 5 — Mayas, aztecas e incas'
CLAVE = 'Clase 5 —'
INDICADORES = [
    'Ubica en un mapa y en una línea de tiempo a mayas, mexicas (aztecas) e incas.',
    'Describe la organización política y social de cada civilización.',
    'Reconoce aportes culturales de estos pueblos a la humanidad.',
    'Analiza una fuente escrita por un conquistador teniendo en cuenta su punto de vista.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H2'], C.TEMAS['H2b'], INDICADORES),
    ('h2', 'Grandes civilizaciones de la América prehispánica'),
    ('p', 'Mientras en la cuenca del Paraguay vivían aldeas guaraníes, en otras regiones de América se desarrollaron sociedades '
          'con ciudades, templos monumentales, gobernantes poderosos y grandes poblaciones. Las más conocidas son la maya y la '
          'mexica, en Mesoamérica, y la inca, en los Andes (Figura 5.1). No existieron todas al mismo tiempo (Figura 5.2).'),
    ('p', 'El programa llama a esta etapa «prehistoria americana», porque es anterior a la llegada de los europeos y a sus '
          'documentos escritos. Pero los mayas tuvieron escritura propia, y los incas registraban datos con cuerdas anudadas. '
          'Por eso muchos historiadores prefieren hablar de «América prehispánica» o «precolombina».'),
    ('fig', 'fig_5_1_civilizaciones.png', 'Figura 5.1 — Áreas aproximadas de mayas, mexicas e incas (esquema).', 12.0),
    ('fig', 'fig_5_2_cronologia.png', 'Figura 5.2 — Cronología aproximada de las tres civilizaciones.', 16.0),

    ('h2', 'Los mayas'),
    ('p', 'Los mayas vivieron en el sur del actual México (península de Yucatán, Chiapas), Guatemala, Belice y parte de Honduras y '
          'El Salvador. Esa región forma parte de Mesoamérica, el área cultural que abarca el centro y el sur de México y parte de '
          'América Central. Su período de mayor esplendor, llamado clásico, fue entre los años 250 y 900 d. C.'),
    ('p', 'Nunca formaron un imperio unificado: vivían en ciudades-estado independientes, como Tikal, Palenque, Copán o Calakmul, '
          'gobernadas por reyes considerados sagrados, que a menudo guerreaban entre sí. Hacia el 900 muchas ciudades del sur fueron '
          'abandonadas, pero la cultura maya continuó en el norte de Yucatán, en ciudades como Chichén Itzá, y sus descendientes '
          'viven hoy en México y Guatemala y hablan lenguas mayas.'),
    ('lista', ['Escritura: un sistema de signos que representaban palabras y sílabas, grabado en piedra, cerámica y libros de corteza.',
               'Matemática y astronomía: usaron el cero y calendarios muy precisos basados en la observación del Sol, la Luna y Venus.',
               'Arquitectura: pirámides escalonadas con templos en la cima, palacios y juegos de pelota.']),

    ('h2', 'Los mexicas o aztecas'),
    ('p', 'Los mexicas, también llamados aztecas, fundaron hacia 1325 la ciudad de Tenochtitlan en unos islotes del lago de Texcoco, '
          'en el valle de México. En 1428 formaron la Triple Alianza con las ciudades de Texcoco y Tlacopan y dominaron gran parte '
          'del centro y del sur de México. Los pueblos sometidos debían pagarles tributos: maíz, telas, cacao, plumas o trabajo.'),
    ('p', 'El gobernante supremo era el huey tlatoani; Moctezuma II gobernaba cuando llegaron los españoles. La sociedad estaba '
          'jerarquizada: los nobles (pipiltin) ocupaban los cargos de gobierno, los sacerdotes dirigían el culto, los guerreros '
          'ascendían por sus hazañas, los comerciantes (pochteca) recorrían grandes distancias, y la mayoría eran campesinos y '
          'artesanos (macehualtin), organizados en barrios llamados calpulli. Tenochtitlan cayó en 1521 ante Hernán Cortés y sus '
          'numerosos aliados indígenas.'),
    ('caja', 'ejemplo', 'Ejemplo — ',
     'Una chinampa era como un cantero elevado construido dentro de un lago poco profundo: se apilaban capas de barro y de '
     'plantas, y se sujetaban los bordes con estacas y árboles plantados. No flotaba: estaba apoyada en el fondo. Entre las '
     'chinampas quedaban canales por donde circulaban canoas. La técnica es anterior a los mexicas, que la usaron para '
     'alimentar a una ciudad muy poblada.'),

    ('h2', 'Los incas'),
    ('p', 'Los incas tenían su capital en Cuzco, en los Andes del actual Perú. Desde mediados del siglo XV, con el gobernante '
          'Pachacútec, iniciaron una rápida expansión y formaron el Tawantinsuyu, «las cuatro regiones unidas», el imperio más '
          'extenso de la América prehispánica: iba del sur de la actual Colombia al centro de Chile y el noroeste de la Argentina.'),
    ('p', 'El soberano, el Sapa Inca, era considerado hijo del Sol. La base de la sociedad era el ayllu, una comunidad de familias '
          'emparentadas que trabajaban juntas la tierra. Por medio de la mita, las comunidades entregaban turnos de trabajo al '
          'Estado para construir caminos, templos o terrazas de cultivo. El imperio cayó entre 1532 y 1533, cuando Francisco '
          'Pizarro capturó y ejecutó al Inca Atahualpa, en medio de una guerra civil entre dos hermanos que se disputaban el trono.'),
    ('lista', ['Caminos: una red de miles de kilómetros, el Qhapaq Ñan, con puentes colgantes y postas.',
               'Agricultura de montaña: terrazas o andenes, riego y cientos de variedades de papa y de maíz.',
               'Registro con quipus: cuerdas con nudos para llevar cuentas de población, tributos y cosechas.',
               'Lengua general: el quechua, que aún hablan millones de personas en los Andes.']),

    ('fuente', 'Fuente escrita · Hernán Cortés, Segunda carta de relación al emperador Carlos V (1520). Fragmento en versión '
               'modernizada, sobre el mercado de Tenochtitlan.',
     ['«Tiene esta ciudad muchas plazas, donde hay continuo mercado y trato de comprar y vender. Tiene otra plaza tan grande como '
      'dos veces la ciudad de Salamanca, toda cercada de portales alrededor, donde hay cotidianamente arriba de sesenta mil '
      'ánimas comprando y vendiendo.»'],
     'Vocabulario: trato, comercio; Salamanca, ciudad de España; cotidianamente, todos los días; ánimas, personas.',
     ['¿Quién escribió la carta, a quién y en qué año?',
      '¿Qué datos sobre Tenochtitlan aporta el fragmento?',
      '¿Por qué Cortés compara el mercado con Salamanca? ¿Qué le convenía mostrar al emperador?']),
    ('renglones', 6),
    ('ubicate', 'Ubicate  ·  Mapa y cronología (Figuras 5.1 y 5.2)',
     '1) Ubicá Tenochtitlan, Tikal y Cuzco y decí en qué país actual está cada una. 2) Cuando se fundó Tenochtitlan (hacia 1325), '
     '¿ya existía el imperio inca? ¿Y el período clásico maya? Explicá con las fechas.'),
    ('renglones', 4),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. Las ciudades mayas del período clásico…'),
    ('opc', ['formaban un imperio con capital en Cuzco', 'eran ciudades-estado independientes con sus propios reyes',
             'estaban gobernadas por el huey tlatoani', 'fueron fundadas por los españoles']),
    ('item', '2. Tenochtitlan fue fundada hacia 1325…'),
    ('opc', ['en la costa del océano Pacífico', 'en la península de Yucatán', 'en unos islotes del lago de Texcoco',
             'en los Andes del Perú']),
    ('item', '3. La mita incaica era…'),
    ('opc', ['un turno de trabajo que las comunidades daban al Estado', 'un tipo de pirámide escalonada', 'el nombre del Sapa Inca',
             'una moneda de oro']),
    ('item', '4. Una chinampa era…'),
    ('opc', ['una balsa que flotaba con plantas', 'un camino de piedra en los Andes', 'un templo en la cima de una pirámide',
             'un cantero elevado construido con barro y plantas en un lago poco profundo']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. La capital de los incas era ________.'),
    ('item', '6. Los incas registraban cuentas con cuerdas anudadas llamadas ________.'),
    ('item', '7. Los mexicas formaron en 1428 la Triple ________ con Texcoco y Tlacopan.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) Las tres civilizaciones existieron al mismo tiempo durante todo su desarrollo.'),
    ('item', '9. (....) Los mayas usaron el cero en sus cálculos.'),
    ('item', '10. (....) Tenochtitlan cayó en 1521 solo por la fuerza de los soldados españoles.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. Completá el cuadro comparativo.'),
    ('cuadro', ['Criterio', 'Mayas', 'Mexicas', 'Incas'], ['Región', 'Forma de gobierno', 'Un aporte cultural'], [2.2, 2.6, 2.6, 2.6]),
    ('item', '12. ¿Por qué muchos historiadores prefieren hablar de «América prehispánica» en lugar de «prehistoria americana» '
             'para estas civilizaciones? Se tendrá en cuenta: qué significa prehistoria (1 punto), un ejemplo de escritura o '
             'registro (1 punto) y una conclusión (1 punto).', 5),
]

PLAN = {
    'material': 'Tomo: Clase 5 (Figuras 5.1 y 5.2); planisferio o mapa de América',
    'tema': C.TEMAS['H2b'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes ubiquen y comparen tres grandes civilizaciones prehispánicas y reconozcan sus aportes, '
                 'sin confundir sus épocas.',
    'funciones': {
        'Esenciales': 'En clase: Ubicate; fuente (preguntas 1 a 3); actividades 1, 2, 3, 4 y 11.',
        'Consolidación': 'Actividades 5, 6, 8 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 8).',
        'Complementarias o domiciliarias': 'Actividades 7, 10 y 12.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 4. Muestra las Figuras 5.1 y 5.2 y pregunta qué observan.',
             'Describen las áreas y las barras de tiempo.', 'Observaciones orales.'),
        ]),
        ('Desarrollo', [
            ('10–22', 'Lectura de la introducción: explica Mesoamérica, los Andes y el problema del nombre «prehistoria».',
             'Resuelven la primera parte del «Ubicate».', 'Ubicate, parte 1 (esencial).'),
            ('22–40', 'Lectura de «Los mayas» y «Los mexicas o aztecas»; explica la chinampa con el Ejemplo y un dibujo en la pizarra.',
             'Resuelven las actividades 1, 2 y 4.', 'Actividades 1, 2 y 4 (esenciales).'),
            ('40–55', 'Lectura de «Los incas».', 'Resuelven la actividad 3 y la segunda parte del «Ubicate».',
             'Actividad 3; Ubicate, parte 2 (esenciales).'),
            ('55–72', 'Lee el fragmento de Cortés y explica el vocabulario y quién escribe.',
             'Responden las preguntas 1 a 3 de la fuente.', 'Fuente (esencial).'),
            ('72–92', 'Organiza parejas para el cuadro comparativo.',
             'Completan la actividad 11.', 'Actividad 11 (esencial).'),
            ('92–104', 'Acompaña; quien termina sigue con la consolidación.', 'Resuelven las actividades 5, 6, 8 y 9.',
             'Actividades de consolidación.'),
        ]),
        ('Cierre', [
            ('104–120', 'Puesta en común del cuadro comparativo; retoma errores (chinampa, fechas). Lee los criterios de la actividad 12 y asigna la tarea.',
             'Corrigen el cuadro con otro color.', 'Cuadro revisado.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en el cuadro: una fila resuelta como modelo (Región) antes de que completen el resto.',
        'Apoyo en la fuente: el docente lee el fragmento dos veces y los estudiantes subrayan los números.',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: investigar qué es el Qhapaq Ñan y por qué la UNESCO lo declaró Patrimonio Mundial.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Lectura de mapa y de cronología; análisis de fuente; cuadro comparativo.',
        'instrumentos': 'Lista de cotejo con los cuatro indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Ubica las tres civilizaciones en el espacio y en el tiempo sin confundir sus épocas.',
                      'Diferencia ciudades-estado mayas, Triple Alianza mexica e imperio inca.',
                      'Nombra al menos un aporte cultural de cada una.',
                      'Reconoce el punto de vista del conquistador en la fuente.'],
    },
    'precisiones': [
        'La chinampa no flotaba: es un error muy difundido. Se corrige explícitamente.',
        'La caída de Tenochtitlan se explica también por los aliados indígenas de Cortés (tlaxcaltecas y otros) y por las epidemias; se amplía en la Clase 6.',
        'El fragmento de Cortés está en versión modernizada; si se dispone de una edición, conviene mostrar la ortografía original.',
    ],
    'tarea': 'Actividades 7, 10 y 12 de la Clase 5.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente', [
            ('F1', 'Hernán Cortés, conquistador español, al emperador Carlos V, en 1520.', ''),
            ('F2', 'Tenía muchas plazas con mercado permanente; una plaza enorme, rodeada de portales, donde comerciaban más de '
                   'sesenta mil personas por día.', ''),
            ('F3', 'Para que el emperador, que conocía Salamanca, imaginara el tamaño. Le convenía mostrar una ciudad rica y '
                   'grande para destacar el valor de su conquista y conseguir apoyo.', 'Se valora que relacione el propósito con el autor.'),
        ]),
        ('Ubicate (Figuras 5.1 y 5.2)', [
            ('U', '1) Tenochtitlan: México; Tikal: Guatemala; Cuzco: Perú. 2) No, el imperio inca empezó a expandirse hacia 1438. '
                  'El período clásico maya ya había terminado (250-900); en 1325 estaba en curso el posclásico.', ''),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'b) eran ciudades-estado independientes con sus propios reyes', ''),
            ('2', 'c) en unos islotes del lago de Texcoco', ''),
            ('3', 'a) un turno de trabajo que las comunidades daban al Estado', ''),
            ('4', 'd) un cantero elevado construido con barro y plantas en un lago poco profundo', ''),
        ]),
        ('Completá los espacios', [
            ('5', 'Cuzco', ''),
            ('6', 'quipus', ''),
            ('7', 'Alianza', ''),
        ]),
        ('Verdadero o falso', [
            ('8', 'Falso: el clásico maya (250-900) es muy anterior a los mexicas (desde 1325) y a la expansión inca (desde 1438).',
             'Justificación obligatoria.'),
            ('9', 'Verdadero.', ''),
            ('10', 'Falso: Cortés tuvo muchos aliados indígenas y las epidemias debilitaron a la ciudad.', 'Justificación obligatoria.'),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'Región: sur de México y América Central / centro de México / Andes. Gobierno: ciudades-estado con reyes sagrados / '
                   'Triple Alianza con el huey tlatoani y tributos / imperio con el Sapa Inca. Aporte: escritura, cero, calendario / '
                   'chinampas, Tenochtitlan / caminos, terrazas, quipus.', 'Una casilla correcta por criterio y civilización; se aceptan otros aportes.'),
            ('12', 'Ejemplo: «La prehistoria es la etapa anterior a la escritura. Los mayas tenían escritura propia y los incas '
                   'usaban quipus. Por eso es más exacto hablar de América prehispánica, es decir, anterior a la llegada de los españoles.»',
             'Criterio anunciado en la consigna: qué significa prehistoria (1 punto), un ejemplo de escritura o registro (1 punto) y una conclusión (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Fragmento de la Segunda carta de relación de Cortés (1520)', 'Versión modernizada de difusión escolar; cotejar la literalidad con una edición (por ejemplo, Porrúa).'),
    ('Fechas: clásico maya 250-900; Tenochtitlan hacia 1325; Triple Alianza 1428; Pachacútec hacia 1438; caída 1521 y 1532-1533', 'Fechas habituales de la bibliografía; cotejar.'),
    ('Áreas del mapa 5.1', 'Polígonos aproximados de la editorial; no son límites.'),
]
