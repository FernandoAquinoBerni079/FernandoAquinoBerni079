"""Encuentro 2 — Clase 2: Los primeros pobladores del actual Paraguay (H1; temas H1a y H1b)."""
import curriculo as C

TITULO = 'Clase 2 — Los primeros pobladores del actual Paraguay'
CLAVE = 'Clase 2 —'
INDICADORES = [
    'Explica qué fue la prehistoria y por qué se conoce sobre todo por la arqueología.',
    'Diferencia las sociedades cazadoras-recolectoras de las formaciones tribales.',
    'Ubica en una línea de tiempo la presencia de los primeros grupos humanos en la región, con fechas aproximadas.',
    'Describe la diversidad de pueblos de las regiones Oriental y Occidental y sus formas de organización.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H1'], C.TEMAS['H1a'] + ' ' + C.TEMAS['H1b'], INDICADORES),

    ('h2', 'La prehistoria y cómo se conoce'),
    ('p', 'Se llama prehistoria al período de la vida humana anterior a la escritura. Como esos pueblos no dejaron textos, lo '
          'que sabemos de ellos proviene sobre todo de la arqueología, la ciencia que estudia los restos materiales del pasado: '
          'herramientas de piedra, restos de fogones, huesos de animales cazados, semillas, cerámica y sepulturas. Para conocer '
          'la antigüedad de un resto, los arqueólogos usan métodos de laboratorio, como el del carbono 14.'),
    ('p', 'En América se usan también las palabras «prehispánico» o «precolombino» para referirse al tiempo anterior a la llegada '
          'de los europeos, porque muchos pueblos americanos vivieron sin escritura hasta el siglo XVI y algunos, como los mayas, '
          'sí tuvieron escritura propia (Clase 5).'),

    ('h2', 'Los primeros grupos humanos de la región'),
    ('p', 'Los primeros habitantes del territorio que hoy es el Paraguay llegaron hace miles de años, como parte del lento '
          'poblamiento de América que vas a estudiar en la Clase 4. En zonas vecinas de la cuenca del Paraná, como la provincia '
          'argentina de Misiones y el sur del Brasil, los arqueólogos fecharon herramientas de cazadores-recolectores de unos '
          '8.000 años de antigüedad o más. En el este del Paraguay aparecen herramientas del mismo tipo, pero los sitios '
          'paraguayos fueron poco excavados y fechados: todavía hay mucho por investigar (Figura 2.1).'),
    ('fig', 'fig_2_1_linea_prehistoria.png', 'Figura 2.1 — Línea de tiempo de la prehistoria regional (fechas aproximadas).', 16.0),

    ('h2', 'Las sociedades cazadoras-recolectoras'),
    ('p', 'Durante la mayor parte de la prehistoria, los grupos humanos vivieron de la caza, la pesca y la recolección de frutos, '
          'raíces, miel y huevos. Eran grupos pequeños, de unas pocas familias emparentadas, que se trasladaban según las estaciones '
          'y la disponibilidad de alimentos: por eso se dice que eran nómadas o seminómadas.'),
    ('lista', ['Organización política: no había gobierno permanente. Las decisiones se tomaban en grupo y tenían más influencia '
               'las personas con experiencia o prestigio.',
               'Organización social: el parentesco unía al grupo. El trabajo se repartía según la edad y el sexo.',
               'Organización económica: lo obtenido se compartía; fabricaban herramientas de piedra (puntas de proyectil, '
               'raspadores), de hueso y de madera.',
               'Creencias: la naturaleza, los animales y los antepasados tenían un lugar importante en sus creencias.']),

    ('h2', 'Las formaciones tribales'),
    ('p', 'Con el tiempo, muchos grupos aprendieron a cultivar plantas. La agricultura permitió vivir más tiempo en un mismo lugar, '
          'formar aldeas y almacenar alimentos, y trajo nuevas técnicas, como la cerámica para cocinar y guardar. Así surgieron '
          'las formaciones o sociedades tribales: comunidades más grandes, organizadas por el parentesco, con aldeas y chacras.'),
    ('p', 'En la región, los agricultores ceramistas de lengua tupí-guaraní se extendieron por la cuenca del Paraná y del Paraguay '
          'hace unos 2.000 años. Cultivaban maíz y mandioca en claros abiertos en el bosque y vivían en aldeas. A ellos está '
          'dedicada la Clase 3.'),
    ('tabla', ['Rasgo', 'Sociedad cazadora-recolectora', 'Formación tribal'],
     [['Alimentación', 'Caza, pesca y recolección.', 'Agricultura, junto con caza, pesca y recolección.'],
      ['Vivienda', 'Campamentos que se trasladan.', 'Aldeas más estables.'],
      ['Organización', 'Pocas familias; decisiones en grupo.', 'Varias familias emparentadas; líderes con prestigio.'],
      ['Técnicas', 'Herramientas de piedra, hueso y madera.', 'Además, cerámica y herramientas de cultivo.']],
     [2.0, 4.0, 4.0]),

    ('h2', 'Pueblos diversos en las dos regiones'),
    ('p', 'El río Paraguay divide el país en dos regiones naturales muy distintas (Figura 2.2). La Región Oriental tiene más '
          'lluvias y, antes de la deforestación, grandes bosques. La Región Occidental o Chaco es una gran llanura, más seca '
          'hacia el oeste, con ríos de caudal variable, como el Pilcomayo.'),
    ('fig', 'fig_2_2_regiones.png', 'Figura 2.2 — Las dos regiones naturales del Paraguay.', 11.0),
    ('p', 'Sería un error pensar que en la Región Oriental vivían solo agricultores y en el Chaco solo cazadores. En la Región '
          'Oriental, junto a los agricultores guaraníes, vivían pueblos cazadores-recolectores, como los aché, que se movían por '
          'los bosques. En el Chaco, muchos pueblos combinaban la caza, la pesca y la recolección con cultivos en las orillas '
          'de los ríos y se trasladaban según las estaciones de lluvia y de seca.'),
    ('p', 'Esa diversidad sigue viva. Los pueblos indígenas actuales se agrupan en familias lingüísticas: conjuntos de pueblos '
          'cuyas lenguas tienen un origen común. Saber cómo viven hoy no prueba por sí solo cómo vivían sus antepasados hace '
          'miles de años, pero muestra que el Paraguay fue y es un país de muchos pueblos.'),
    ('caja', 'concepto', 'Concepto clave — ',
     'Una familia lingüística reúne lenguas emparentadas, que provienen de una lengua más antigua común, como el castellano, '
     'el portugués y el italiano provienen del latín. Hablar lenguas de la misma familia no significa ser el mismo pueblo.'),

    ('fuente', 'Fuente estadística · Pueblos indígenas del Paraguay según el III Censo Nacional de Población y Viviendas para '
               'Pueblos Indígenas (Dirección General de Estadística, Encuestas y Censos, 2012)',
     ['Guaraní: Aché, Avá Guaraní, Mbya Guaraní, Paĩ Tavyterã, Guaraní Ñandéva, Guaraní Occidental.',
      'Lengua Maskoy: Enlhet Norte, Enxet Sur, Sanapaná, Angaité, Toba Maskoy, Guaná.',
      'Mataco Mataguayo: Nivaclé, Maká, Manjui.',
      'Zamuco: Ayoreo, Ybytoso, Tomárãho.',
      'Guaicurú: Qom.'],
     'Cada renglón empieza con el nombre de la familia lingüística; después vienen los pueblos que la forman.',
     ['¿Cuántas familias lingüísticas y cuántos pueblos registra el censo de 2012?',
      '¿Qué familia agrupa más pueblos? Nombrá dos de ellos.',
      '¿Por qué esta fuente sirve para conocer el presente, pero no alcanza para saber cómo vivían estos pueblos hace miles de años?']),
    ('renglones', 6),

    ('ubicate', 'Ubicate  ·  Línea de tiempo y mapa (Figuras 2.1 y 2.2)',
     '1) En la Figura 2.1, ¿cuántos años pasaron, aproximadamente, entre los primeros cazadores-recolectores fechados en la región '
     'y la llegada de los agricultores tupí-guaraníes? 2) En la Figura 2.2, ¿qué río separa las dos regiones y qué río marca el '
     'límite sudoeste del Chaco con la Argentina?'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. Las sociedades cazadoras-recolectoras…'),
    ('opc', ['vivían en ciudades con murallas', 'se trasladaban según la disponibilidad de animales y frutos',
             'producían todo su alimento con la agricultura', 'tenían reyes y ejércitos permanentes']),
    ('item', '2. Una formación tribal se caracteriza por…'),
    ('opc', ['la agricultura, las aldeas y los lazos de parentesco', 'la escritura y el comercio con monedas',
             'la vida en grandes imperios con capital', 'el nomadismo sin ningún tipo de cultivo']),
    ('item', '3. El río que separa la Región Oriental de la Región Occidental es el…'),
    ('opc', ['Paraná', 'Pilcomayo', 'Paraguay', 'Tebicuary']),
    ('item', '4. Según el censo de 2012, los pueblos indígenas del Paraguay se agrupan en…'),
    ('opc', ['dos familias lingüísticas', 'tres familias lingüísticas', 'diecinueve familias lingüísticas', 'cinco familias lingüísticas']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. El período de la vida humana anterior a la escritura se llama ________.'),
    ('item', '6. La ciencia que estudia los restos materiales del pasado es la ________.'),
    ('item', '7. Los ayoreo pertenecen a la familia lingüística ________.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) En la Región Oriental vivieron solo pueblos agricultores.'),
    ('item', '9. (....) Muchos pueblos del Chaco combinaban la caza y la pesca con cultivos en las orillas de los ríos.'),
    ('item', '10. (....) Los pueblos indígenas del Paraguay desaparecieron con la llegada de los europeos.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. Completá el cuadro con una característica de cada sociedad.'),
    ('cuadro', ['Criterio', 'Sociedad cazadora-recolectora', 'Formación tribal'], ['Alimentación', 'Vivienda', 'Organización'],
     [2.4, 3.8, 3.8]),
    ('item', '12. ¿Por qué no es correcto decir que en la Región Oriental vivían solo agricultores y en el Chaco solo cazadores? '
             'Se tendrá en cuenta: un ejemplo de la Región Oriental (1 punto), un ejemplo del Chaco (1 punto) y una conclusión '
             'clara (1 punto).', 5),
]

PLAN = {
    'material': 'Tomo: Clase 2 (Figuras 2.1 y 2.2); si es posible, imágenes de puntas de piedra de un museo o de un libro',
    'tema': C.TEMAS['H1a'] + ' ' + C.TEMAS['H1b'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes reconozcan cómo se conoce la prehistoria, diferencien cazadores-recolectores de '
                 'formaciones tribales y valoren la diversidad de pueblos del territorio.',
    'funciones': {
        'Esenciales': 'En clase: fuente (preguntas 1 a 3); Ubicate; actividades 1, 2, 3, 8, 11 y 12.',
        'Consolidación': 'Actividades 4, 5, 6 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 3).',
        'Complementarias o domiciliarias': 'Actividades 7 y 10.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa en dos minutos la consolidación de la Clase 1. Pregunta: «¿Cómo podemos saber cómo vivían personas que no escribieron?».',
             'Proponen ideas (objetos, restos, dibujos).', 'Ideas en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–25', 'Lectura de «La prehistoria y cómo se conoce» y «Los primeros grupos humanos», con la Figura 2.1. Aclara que las fechas son aproximadas y regionales.',
             'Resuelven la primera parte del «Ubicate».', 'Ubicate, parte 1 (esencial).'),
            ('25–45', 'Explica las sociedades cazadoras-recolectoras y las formaciones tribales con el cuadro.',
             'Resuelven las actividades 1 y 2 y, en parejas, la actividad 11.', 'Actividades 1, 2 y 11 (esenciales).'),
            ('45–60', 'Lectura de «Pueblos diversos en las dos regiones» con la Figura 2.2.',
             'Resuelven la segunda parte del «Ubicate» y las actividades 3 y 8.', 'Ubicate, parte 2; actividades 3 y 8 (esenciales).'),
            ('60–78', 'Presenta la fuente estadística y el Concepto clave de familia lingüística.',
             'Responden las preguntas 1 a 3 de la fuente.', 'Fuente (esencial).'),
            ('78–98', 'Acompaña la escritura de la actividad 12 y lee sus criterios.',
             'Escriben la actividad 12; quien termina sigue con las actividades 4, 5, 6 y 9.', 'Actividad 12 (esencial); consolidación.'),
        ]),
        ('Cierre', [
            ('98–110', 'Puesta en común de la actividad 12: dos estudiantes leen su respuesta.',
             'Comparan ejemplos y corrigen.', 'Respuesta revisada.'),
            ('110–120', 'Síntesis: «diversidad de pueblos y de formas de vida». Asigna la tarea.',
             'Anotan la tarea.', 'Síntesis oral.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en la lectura: el docente lee la fuente en voz alta y subraya en la pizarra el nombre de cada familia.',
        'Apoyo en la escritura de la actividad 12: oración inicial «No es correcto porque en la Región Oriental…».',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: averiguar qué pueblo indígena vive más cerca de su localidad y a qué familia lingüística pertenece.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Lectura de línea de tiempo y de mapa; análisis de fuente estadística; cuadro comparativo.',
        'instrumentos': 'Lista de cotejo con los cuatro indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Explica que la prehistoria se conoce por la arqueología.',
                      'Diferencia cazadores-recolectores de formaciones tribales en al menos dos criterios.',
                      'Usa fechas aproximadas y no las presenta como exactas.',
                      'Reconoce la diversidad de pueblos en las dos regiones sin estereotipos.'],
    },
    'precisiones': [
        'Las fechas regionales son aproximadas y provienen sobre todo de sitios de Misiones y del sur del Brasil; los sitios paraguayos están poco fechados. No conviene dar cifras más precisas.',
        'Evitar expresiones como «pueblos primitivos» o «resistentes al clima duro»: describen con prejuicio. Los pueblos actuales son contemporáneos, no restos del pasado.',
    ],
    'tarea': 'Actividades 7 y 10 de la Clase 2.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente', [
            ('F1', 'Cinco familias lingüísticas y diecinueve pueblos.', ''),
            ('F2', 'La familia guaraní y la Lengua Maskoy, con seis pueblos cada una. Ejemplos: Aché y Mbya Guaraní; Enxet Sur y Sanapaná.',
             'Se acepta cualquiera de las dos familias si nombra dos pueblos de ella.'),
            ('F3', 'Porque el censo describe a los pueblos en 2012; para saber cómo vivían hace miles de años hacen falta otras fuentes, como las arqueológicas.',
             'Debe distinguir la época de la fuente de la época que se quiere estudiar.'),
        ]),
        ('Ubicate (Figuras 2.1 y 2.2)', [
            ('U', '1) Unos 6.000 años (de hace unos 8.000 a hace unos 2.000 años). 2) El río Paraguay separa las regiones; el '
                  'Pilcomayo marca el límite sudoeste del Chaco con la Argentina.', 'Se aceptan entre 5.000 y 7.000 años si aclara que es aproximado.'),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'b) se trasladaban según la disponibilidad de animales y frutos', ''),
            ('2', 'a) la agricultura, las aldeas y los lazos de parentesco', ''),
            ('3', 'c) Paraguay', ''),
            ('4', 'd) cinco familias lingüísticas', ''),
        ]),
        ('Completá los espacios', [
            ('5', 'prehistoria', ''),
            ('6', 'arqueología', ''),
            ('7', 'zamuco', ''),
        ]),
        ('Verdadero o falso', [
            ('8', 'Falso: también vivían cazadores-recolectores, como los aché.', 'Justificación obligatoria.'),
            ('9', 'Verdadero.', ''),
            ('10', 'Falso: hoy viven en el Paraguay diecinueve pueblos indígenas, según el censo de 2012.', 'Justificación obligatoria.'),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'Alimentación: caza, pesca y recolección / agricultura, junto con caza y pesca. Vivienda: campamentos que se trasladan / '
                   'aldeas más estables. Organización: pocas familias y decisiones en grupo / varias familias emparentadas con líderes de prestigio.',
             'Una característica correcta en cada casilla.'),
            ('12', 'Ejemplo: «No es correcto porque en la Región Oriental, además de los agricultores guaraníes, vivían cazadores-recolectores '
                   'como los aché, y en el Chaco muchos pueblos cultivaban en las orillas de los ríos además de cazar y pescar. Por eso '
                   'las formas de vida eran variadas en las dos regiones».',
             'Criterio anunciado en la consigna: un ejemplo de la Región Oriental (1 punto), un ejemplo del Chaco (1 punto) y una conclusión clara (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Herramientas de cazadores-recolectores de unos 8.000 años en Misiones y el sur del Brasil',
     'Síntesis arqueológicas regionales (tradiciones Umbú y Humaitá/Altoparanaense; Itapiranga, Santa Catarina, 8.640 AP; Eldorado, Misiones). Cotejar con bibliografía arqueológica paraguaya.'),
    ('Expansión de agricultores tupí-guaraníes hace unos 2.000 años', 'Dato habitual en la arqueología regional; cotejar.'),
    ('Censo indígena 2012: 19 pueblos y 5 familias', 'Lista coincidente en fuentes secundarias (UNI, prensa). Cotejar con la publicación de la DGEEC (hoy INE).'),
]
