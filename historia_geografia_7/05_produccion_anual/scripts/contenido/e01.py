"""Encuentro 1 — Clase 1: La Historia y la Geografía (clase introductoria).

El programa MEC 2014 no tiene una capacidad específica para esta clase: la
capacidad es una formulación editorial (tipo de vínculo «Formulación
editorial»). Prepara las herramientas que piden todas las capacidades del
año: fuentes, tiempo histórico y lectura de mapas.
"""

TITULO = 'Clase 1 — La Historia y la Geografía: mirar el tiempo y el espacio'
CLAVE = 'Clase 1 —'

CAP_EDITORIAL = ('Reconoce el objeto de estudio de la Historia y de la Geografía y utiliza nociones de tiempo histórico y de '
                 'espacio geográfico para ubicar hechos (formulación editorial: clase introductoria sin capacidad del programa).')
TEMA = ('Objeto de estudio de la Historia y de la Geografía. Las fuentes históricas y sus tipos. El tiempo histórico: '
        'cronología, siglos, años antes y después de Cristo. Herramientas de la Geografía: mapa, puntos cardinales, '
        'escala y leyenda.')
INDICADORES = [
    'Diferencia el objeto de estudio de la Historia y el de la Geografía, y explica por qué se complementan.',
    'Clasifica fuentes según su tipo y distingue fuentes primarias de secundarias.',
    'Ubica años en siglos y en una línea de tiempo, incluidos años antes de Cristo.',
    'Usa los puntos cardinales, la escala y la leyenda para leer un mapa del Paraguay.',
]

# La prueba diagnóstica va en hoja propia, antes de la Unidad 1 y de la Clase 1 (se aplica al inicio del encuentro 1).
DIAGNOSTICA = [
    ('h1', 'Prueba diagnóstica'),
    ('recuadro', 'Prueba diagnóstica · ¿Qué sabés ya? (no lleva nota)',
     ['¿Qué estudia la Historia? Escribilo con tus palabras.',
      '¿En qué siglo estamos? ¿Cómo lo sabés?',
      'Nombrá un objeto, un documento o un relato que te permita saber cómo se vivía antes en tu familia o en tu comunidad.',
      '¿Con qué países limita el Paraguay?',
      '¿Qué río separa la Región Oriental de la Región Occidental o Chaco?'],
     [2, 1, 2, 1, 1]),
]

TOMO = [
    ('h1', TITULO),
    ('ficha', CAP_EDITORIAL, TEMA, INDICADORES),

    ('h2', '¿Qué estudia la Historia?'),
    ('p', 'La Historia es la ciencia que estudia las acciones de las sociedades humanas a lo largo del tiempo: cómo vivían, '
          'cómo se organizaban, qué pensaban, qué conflictos tuvieron y qué cambió o permaneció hasta hoy. No se limita a las '
          'guerras ni a los gobernantes: también estudia el trabajo, la familia, las creencias, la alimentación o la lengua.'),
    ('p', 'La historiadora y el historiador trabajan como investigadores. Hacen preguntas sobre el pasado (¿qué pasó?, ¿por qué?, '
          '¿qué consecuencias tuvo?) y las responden con fuentes, es decir, con las huellas que dejaron las personas. Por eso '
          'la Historia se sigue escribiendo: cuando aparecen nuevas fuentes o se hacen nuevas preguntas, cambia lo que sabemos.'),

    ('h2', '¿Qué estudia la Geografía?'),
    ('p', 'La Geografía estudia el espacio geográfico: la superficie de la Tierra transformada por las sociedades. Analiza el '
          'relieve, el clima, los ríos y la vegetación, pero siempre en relación con las personas que viven allí: dónde se '
          'instalan, qué producen, cómo se trasladan y qué efectos tienen sus actividades sobre el ambiente.'),
    ('p', 'La Geografía responde preguntas como ¿dónde está?, ¿cómo es?, ¿por qué está allí? y ¿cómo se relaciona con otros '
          'lugares? Para eso usa mapas, imágenes, datos estadísticos y observación del terreno.'),
    ('tabla', ['', 'Historia', 'Geografía'],
     [['Qué estudia', 'Las sociedades humanas a lo largo del tiempo.', 'El espacio geográfico: la relación entre la sociedad y la naturaleza.'],
      ['Preguntas clave', '¿Qué pasó? ¿Cuándo? ¿Por qué? ¿Qué cambió?', '¿Dónde está? ¿Cómo es? ¿Por qué allí? ¿Con qué se relaciona?'],
      ['Herramientas', 'Fuentes, líneas de tiempo, periodizaciones.', 'Mapas, escalas, imágenes, datos y estadísticas.']],
     [2.0, 4.0, 4.0]),
    ('caja', 'concepto', 'Concepto clave — ',
     'La Historia y la Geografía se complementan: todo hecho ocurre en un tiempo y en un lugar. Asunción se fundó en 1537 '
     '(tiempo) junto al río Paraguay (lugar), y ese río explica por qué durante siglos fue un puerto importante.'),

    ('h2', 'Las fuentes: huellas del pasado'),
    ('p', 'Una fuente histórica es todo aquello que permite conocer el pasado. Las fuentes se clasifican según su tipo '
          '(Figura 1.1) y según el momento en que se produjeron. Las fuentes primarias se produjeron en la época que se estudia: '
          'una carta de un conquistador, una vasija guaraní o una fotografía. Las fuentes secundarias se elaboraron después, a '
          'partir de otras fuentes: un libro de historia escrito hoy, un documental o este mismo cuadernillo.'),
    ('fig', 'fig_1_1_tipos_fuentes.png', 'Figura 1.1 — Tipos de fuentes históricas, con ejemplos.', 15.0),
    ('p', 'Ninguna fuente dice «toda la verdad». Cada una fue hecha por alguien, en un momento y con un propósito. Por eso, ante '
          'una fuente conviene preguntarse: ¿quién la hizo?, ¿cuándo?, ¿para qué?, ¿qué muestra y qué deja afuera?'),
    ('caja', 'paraguay', 'En Paraguay — ',
     'El Archivo Nacional de Asunción conserva documentos escritos desde el siglo XVI, como actas del Cabildo y expedientes '
     'coloniales. También son fuentes valiosas los relatos de los mayores, transmitidos en guaraní y en castellano: la '
     'historia oral recupera lo que muchas veces no quedó escrito.'),

    ('fuente', 'Fuente escrita · Constitución Nacional del Paraguay (1992), artículo 140, «De los idiomas»',
     ['«El Paraguay es un país pluricultural y bilingüe. Son idiomas oficiales el castellano y el guaraní. La ley establecerá '
      'las modalidades de utilización de uno y otro. Las lenguas indígenas, así como las de otras minorías, forman parte del '
      'patrimonio cultural de la Nación.»'],
     'Vocabulario: pluricultural, que tiene varias culturas; modalidades, formas o maneras.',
     ['¿Qué tipo de fuente es y en qué año se produjo?',
      'Si estudiamos la sociedad paraguaya de 1992, ¿es una fuente primaria o secundaria? ¿Por qué?',
      '¿Qué nos dice este texto sobre el Paraguay? Nombrá dos ideas.']),
    ('renglones', 5),

    ('h2', 'El tiempo histórico'),
    ('p', 'Para ordenar los hechos se usa la cronología: el orden de los acontecimientos según su fecha. Una línea de tiempo '
          'es un dibujo de ese orden, en el que las distancias representan los años (Figura 1.2).'),
    ('p', 'En el Paraguay, como en gran parte del mundo, se usa la era cristiana: los años se cuentan desde el nacimiento de '
          'Jesucristo según el cálculo tradicional. Los años anteriores se escriben con «a. C.» (antes de Cristo) y se cuentan '
          'hacia atrás: el año 500 a. C. es más antiguo que el 100 a. C. Los posteriores llevan «d. C.» (después de Cristo), '
          'aunque normalmente no se escribe. No existe el año 0: del año 1 a. C. se pasa al año 1 d. C.'),
    ('fig', 'fig_1_2_linea_tiempo_era.png', 'Figura 1.2 — La era cristiana en una línea de tiempo.', 16.0),
    ('p', 'Para medir períodos largos se usan la década (10 años), el siglo (100 años) y el milenio (1.000 años). Los siglos se '
          'escriben con números romanos. El siglo I d. C. va del año 1 al 100; el siglo XVI, del 1501 al 1600; el siglo XXI, '
          'del 2001 al 2100.'),
    ('caja', 'ejemplo', 'Ejemplo — ',
     '¿A qué siglo pertenece un año? Si no termina en 00, quitale las dos últimas cifras y sumá uno: 1537 → 15 + 1 = siglo '
     'XVI; 476 → 4 + 1 = siglo V. Si termina en 00, el siglo es el número sin los dos ceros: 1800 → siglo XVIII; 2000 → '
     'siglo XX. Con los años a. C. se hace igual, agregando «a. C.»: 450 a. C. → siglo V a. C.'),
    ('p', 'Además de contar años, los historiadores dividen el pasado en grandes etapas o períodos, cada uno con rasgos '
          'comunes. Para el Paraguay y América es habitual hablar de un período prehispánico (antes de la llegada de los '
          'europeos), de un período colonial (siglos XVI a principios del XIX) y de un período independiente (desde 1811).'),

    ('h2', 'El espacio geográfico y sus herramientas'),
    ('p', 'El mapa es una representación reducida y simplificada de la superficie terrestre sobre un plano. Para leerlo hay que '
          'mirar tres elementos: la orientación, la escala y la leyenda.'),
    ('lista', ['Orientación: los puntos cardinales son norte (N), sur (S), este (E) y oeste (O). En casi todos los mapas el norte '
               'está arriba; la rosa de los vientos lo indica.',
               'Escala: indica cuántas veces se redujo la realidad. La escala gráfica es una barra que muestra cuántos kilómetros '
               'reales equivalen a una distancia en el mapa.',
               'Leyenda o referencias: explica qué significa cada símbolo o color (ríos, límites, ciudades).']),
    ('p', 'Con estas herramientas se puede describir la localización de un lugar. La localización relativa lo ubica respecto de '
          'otros lugares («Concepción está al norte de Asunción»); la localización absoluta usa coordenadas, latitud y '
          'longitud, que vas a estudiar en la Clase 16.'),
    ('fig', 'fig_1_3_mapa_orientacion.png', 'Figura 1.3 — El Paraguay: orientación, escala y leyenda.', 12.0),
    ('ubicate', 'Ubicate  ·  Mapa (Figura 1.3)',
     '¿En qué dirección queda Encarnación respecto de Asunción? Usá la escala gráfica y una regla para estimar la distancia en '
     'línea recta entre las dos ciudades. Explicá cómo hiciste el cálculo.'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. La Historia estudia…'),
    ('opc', ['solo las guerras y los gobernantes', 'los fenómenos naturales sin relación con las personas',
             'las acciones de las sociedades humanas a lo largo del tiempo', 'únicamente los hechos ocurridos en el Paraguay']),
    ('item', '2. Una vasija guaraní de cerámica encontrada en una excavación es una fuente…'),
    ('opc', ['material', 'escrita', 'oral', 'cartográfica']),
    ('item', '3. El año 1811 pertenece al siglo…'),
    ('opc', ['XVII', 'XIX', 'XVIII', 'XX']),
    ('item', '4. Para calcular la distancia real entre dos ciudades en un mapa se usa…'),
    ('opc', ['la rosa de los vientos', 'la leyenda', 'el título', 'la escala']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. Una fuente producida en la misma época que se estudia se llama fuente ________.'),
    ('item', '6. El año 2000 pertenece al siglo ________.'),
    ('item', '7. El punto cardinal opuesto al este es el ________.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) Entre el año 50 a. C. y el año 50 d. C. pasaron exactamente 100 años.'),
    ('item', '9. (....) El relato de una abuela sobre su infancia es una fuente oral.'),
    ('item', '10. (....) La Geografía estudia solo el relieve y los ríos, sin tener en cuenta a las personas.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. Clasificá cada fuente: escribí su tipo y si es primaria o secundaria para estudiar la época en que se produjo.'),
    ('cuadro', ['Fuente', 'Tipo', '¿Primaria o secundaria?'],
     ['a) El artículo 140 de la Constitución (1992).', 'b) Un libro escolar de 2020 sobre la colonia.',
      'c) Una punta de flecha de piedra hallada en el Chaco.', 'd) Un mapa del Paraguay dibujado en el siglo XVIII.',
      'e) Una fotografía de una calle de Asunción en 1930.'],
     [5.0, 2.5, 2.5]),
    ('item', '12. Construí una línea de tiempo con cinco hechos de tu vida o de tu familia. Escribí el año y el siglo de cada uno.', 5),
    ('item', '13. Elegí un hecho de tu comunidad y explicá por qué la Historia y la Geografía se complementan para entenderlo. '
             'Se tendrá en cuenta: un hecho con su fecha (1 punto), el lugar donde ocurrió (1 punto) y una razón por la que el '
             'lugar ayuda a entender el hecho (1 punto).', 5),
]

PLAN = {
    'capacidad': CAP_EDITORIAL,
    'vinculo': 'Formulación editorial: clase introductoria sin capacidad del programa MEC 2014. Prepara herramientas '
               '(fuentes, tiempo histórico, lectura de mapas) que usan todas las capacidades del año.',
    'material': 'Tomo: Clase 1 (Figuras 1.1, 1.2 y 1.3); regla; un objeto o una foto antigua que traiga el docente',
    'tema': TEMA,
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes reconozcan qué estudian la Historia y la Geografía y empiecen a usar sus herramientas '
                 'básicas: fuentes, siglos, línea de tiempo y mapa.',
    'funciones': {
        'Esenciales': 'En clase: prueba diagnóstica; fuente (preguntas 1 a 3); Ubicate; actividades 1, 2, 3, 4, 8 y 11.',
        'Consolidación': 'Actividades 5, 6, 7, 9 y 10 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 2).',
        'Complementarias o domiciliarias': 'Actividades 12 y 13.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–15', 'Presenta la materia y aplica la prueba diagnóstica, sin nota. Recoge las respuestas para conocer al grupo.',
             'Responden la prueba diagnóstica en el tomo.', 'Prueba diagnóstica.'),
        ]),
        ('Desarrollo', [
            ('15–30', 'Lectura guiada de «¿Qué estudia la Historia?» y «¿Qué estudia la Geografía?» con el cuadro y el Concepto clave.',
             'Resuelven la actividad 1 y comentan un ejemplo propio de hecho con tiempo y lugar.', 'Actividad 1 (esencial).'),
            ('30–48', 'Muestra un objeto o una foto antigua y pregunta qué nos dice. Explica tipos de fuentes con la Figura 1.1.',
             'Resuelven la actividad 2 y, en parejas, la actividad 11; comprueban con otra pareja.', 'Actividades 2 y 11 (esenciales).'),
            ('48–60', 'Lee en voz alta el artículo 140 y explica el vocabulario.',
             'Responden las preguntas 1 a 3 de la fuente en los renglones del recuadro.', 'Fuente (esencial).'),
            ('60–80', 'Explica a. C. y d. C., el año 1 y la regla del siglo con la Figura 1.2 y el Ejemplo; resuelve 1800 y 476 en la pizarra.',
             'Resuelven las actividades 3 y 8; explican por qué no existe el año 0.', 'Actividades 3 y 8 (esenciales).'),
            ('80–96', 'Explica orientación, escala y leyenda con la Figura 1.3; muestra cómo medir con la regla sobre la escala gráfica.',
             'Resuelven el «Ubicate» y la actividad 4.', 'Ubicate y actividad 4 (esenciales).'),
            ('96–106', 'Acompaña; quien termina antes sigue con las de consolidación.',
             'Resuelven las actividades 5, 6, 7, 9 y 10.', 'Actividades de consolidación.'),
        ]),
        ('Cierre', [
            ('106–120', 'Retoma los errores frecuentes (siglos de años terminados en 00, fuentes primarias) y asigna la tarea; lee los criterios de la actividad 13.',
             'Corrigen con otro color lo que haga falta y anotan la tarea.', 'Errores frecuentes corregidos.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en el cálculo de siglos: tarjeta en la pizarra con la regla y tres ejemplos resueltos (1537, 1800, 476).',
        'Apoyo en el mapa: el docente marca con el dedo el norte y la escala antes de que el estudiante mida.',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: averiguar el año de fundación de su ciudad o compañía y ubicarlo en un siglo y en la Figura 1.2.',
    ],
    'evaluacion': {
        'tipo': 'Diagnóstica (prueba inicial) y formativa.',
        'procedimientos': 'Prueba diagnóstica; análisis de fuente; clasificación de fuentes; lectura de mapa.',
        'instrumentos': 'Registro de la diagnóstica; lista de cotejo con los cuatro indicadores; actividad 13 con los criterios de su consigna.',
        'criterios': ['Distingue el objeto de estudio de la Historia y el de la Geografía.',
                      'Clasifica correctamente al menos cuatro de las cinco fuentes de la actividad 11.',
                      'Ubica en su siglo años terminados y no terminados en 00.',
                      'Estima una distancia con la escala gráfica e indica una dirección cardinal.'],
    },
    'precisiones': [
        'La diagnóstica no lleva nota: sirve para decidir apoyos. Conviene guardar las respuestas hasta la Evaluación de la Unidad 1.',
        'La clasificación primaria/secundaria depende de qué se estudia: un libro de 2020 es primario para estudiar cómo se enseñaba historia en 2020.',
    ],
    'tarea': 'Actividades 12 y 13 de la Clase 1.',
}

SOL = {
    'bloques': [
        ('Prueba diagnóstica (orientaciones; no lleva nota)', [
            ('D1', 'Se espera una idea cercana a «estudia el pasado de las personas o de las sociedades».', 'Registrar si confunden Historia con cuentos o leyendas.'),
            ('D2', 'Siglo XXI. Para saberlo pueden usar cualquier razonamiento; la regla se enseña en esta clase.', ''),
            ('D3', 'Cualquier objeto, documento, foto o relato familiar.', 'Anticipa la noción de fuente.'),
            ('D4', 'Bolivia, el Brasil y la Argentina.', ''),
            ('D5', 'El río Paraguay.', ''),
        ]),
        ('Trabajá con la fuente', [
            ('F1', 'Fuente escrita (un texto legal). Se produjo en 1992.', ''),
            ('F2', 'Primaria, porque se produjo en 1992, la misma época que se estudia.', 'Debe justificar con la fecha.'),
            ('F3', 'Por ejemplo: el Paraguay tiene varias culturas; tiene dos idiomas oficiales, el castellano y el guaraní; las lenguas indígenas son patrimonio del país.',
             'Dos ideas tomadas del texto.'),
        ]),
        ('Ubicate (Figura 1.3)', [
            ('U', 'Encarnación queda al sudeste (SE) de Asunción. Distancia en línea recta: alrededor de 290 km.',
             'Se aceptan entre 250 y 330 km si explica que comparó la distancia medida con la barra de escala. «Sur» o «este» solos son respuestas parciales.'),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'c) las acciones de las sociedades humanas a lo largo del tiempo', ''),
            ('2', 'a) material', ''),
            ('3', 'b) XIX', '1811 → 18 + 1 = XIX.'),
            ('4', 'd) la escala', ''),
        ]),
        ('Completá los espacios', [
            ('5', 'primaria', ''),
            ('6', 'XX', 'Termina en 00: el siglo es el número sin los ceros.'),
            ('7', 'oeste', ''),
        ]),
        ('Verdadero o falso', [
            ('8', 'Falso: pasaron 99 años, porque no existe el año 0 (del 1 a. C. se pasa al 1 d. C.).', 'Justificación obligatoria.'),
            ('9', 'Verdadero.', ''),
            ('10', 'Falso: la Geografía estudia el espacio en relación con las sociedades que viven en él.', 'Justificación obligatoria.'),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'a) Escrita, primaria. b) Escrita, secundaria (estudia la colonia desde hoy). c) Material, primaria. '
                   'd) Cartográfica, primaria. e) Iconográfica, primaria.',
             'Un punto por fila completa. Si el estudiante explica que el libro b) es primario para estudiar la enseñanza en 2020, también es correcto.'),
            ('12', 'Respuesta personal. Ejemplo: 2013, nacimiento, siglo XXI; 2019, ingreso a la escuela, siglo XXI.',
             'Fechas ordenadas, distancias aproximadamente proporcionales y siglo correcto en cada hecho.'),
            ('13', 'Ejemplo: «La fiesta patronal de mi compañía se hace desde 1950 (fecha) junto a la capilla del cruce de caminos '
                   '(lugar); como el cruce es el punto de encuentro de varias compañías, allí se juntaba la gente (razón)».',
             'Criterio anunciado en la consigna: un hecho con su fecha (1 punto), el lugar donde ocurrió (1 punto) y una razón por la que el lugar ayuda a entender el hecho (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Constitución de 1992, art. 140', 'Texto coincidente en varias reproducciones (camara.leg.br, Université Laval). Cotejar con la edición oficial (BACN).'),
    ('Archivo Nacional de Asunción: documentos desde el siglo XVI', 'Dato institucional difundido; cotejar con la página del Archivo.'),
    ('Distancia Asunción-Encarnación ≈ 290 km en línea recta', 'Cálculo propio con coordenadas aproximadas (57,63° O 25,28° S; 55,87° O 27,33° S).'),
]
