"""Encuentro 32 — Clase 20: Regiones naturales de Paraguay y América; cambios en el uso de la tierra (G4; temas G4a, G4b y G4d).

Las ubicaciones de las regiones y ecosistemas son esquemas de la editorial y
se declaran así; los límites oficiales de las ecorregiones del Paraguay deben
consultarse en el MADES. No se dan cifras de deforestación que no puedan
cotejarse en esta edición.
"""
import curriculo as C

TITULO = 'Clase 20 — Regiones naturales de Paraguay y América'
CLAVE = 'Clase 20 —'
INDICADORES = [
    'Describe las principales regiones naturales de América.',
    'Diferencia los grandes ecosistemas de la Región Oriental y de la Región Occidental del Paraguay.',
    'Explica cambios y costos socioambientales del uso de la tierra.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['G4'], C.TEMAS['G4a'] + ' ' + C.TEMAS['G4b'] + ' ' + C.TEMAS['G4d'], INDICADORES),

    ('h2', 'Qué es una región natural'),
    ('p', 'Una región natural es un territorio con características físicas parecidas: un mismo tipo de clima, de relieve, de suelos, '
          'de vegetación y de fauna. Las regiones naturales no tienen límites exactos: pasan gradualmente de una a otra. Cuando se '
          'estudian los seres vivos y su ambiente juntos, se habla de ecosistemas o de ecorregiones.'),

    ('h2', 'Las regiones naturales de América'),
    ('p', 'El clima, el relieve y los suelos que estudiaste en las Clases 17 y 19 explican la gran variedad de regiones naturales de '
          'América:'),
    ('lista', ['Selva tropical: en la Amazonía, cálida y lluviosa todo el año, con la mayor diversidad de plantas y animales del planeta.',
               'Sabanas: pastizales con árboles dispersos y una estación seca, como el Cerrado del Brasil.',
               'Gran Chaco: llanura con bosques secos, sabanas y humedales, compartida por el Paraguay, Bolivia y la Argentina.',
               'Praderas y pampas: llanuras de pastos en zonas templadas, muy usadas para cultivos y ganado.',
               'Desiertos y estepas: muy pocas lluvias y vegetación escasa, como Atacama y la Patagonia.',
               'Bosques templados y de coníferas (taiga) y tundra, en América del Norte, de sur a norte.',
               'Alta montaña: en los Andes, la vegetación cambia con la altura.']),
    ('fig', 'fig_20_1_regiones_america.png', 'Figura 20.1 — Grandes regiones naturales de América (esquema simplificado).', 11.0),

    ('h2', 'Las regiones naturales del Paraguay'),
    ('p', 'El río Paraguay separa dos grandes regiones con ambientes distintos. En la Región Occidental o Chaco se distinguen el '
          'Chaco Seco, al oeste, con bosques bajos y espinosos, cactus y pocas lluvias; el Chaco Húmedo, cerca del río Paraguay, con '
          'palmares, esteros y pastizales que se inundan; y el Pantanal, en el norte, uno de los humedales más grandes del mundo.'),
    ('p', 'La Región Oriental es más húmeda. En el este estaba cubierta por el Bosque Atlántico del Alto Paraná, una selva alta y muy '
          'diversa; en el norte, por el Cerrado, con sabanas y bosques; y en el sur, en Ñeembucú, predominan los humedales y esteros. '
          'El Ministerio del Ambiente y Desarrollo Sostenible (MADES) reconoce oficialmente varias ecorregiones; el mapa de la '
          'Figura 20.2 muestra solo su ubicación aproximada.'),
    ('fig', 'fig_20_2_ecosistemas_py.png', 'Figura 20.2 — Grandes ecosistemas del Paraguay (ubicación aproximada).', 12.0),
    ('tabla', ['', 'Región Occidental (Chaco)', 'Región Oriental'],
     [['Clima', 'Más seco y caluroso', 'Más húmedo'],
      ['Vegetación', 'Bosques secos, palmares, pastizales y humedales', 'Selva del Alto Paraná, Cerrado y humedales'],
      ['Actividades principales', 'Ganadería', 'Agricultura, ganadería y ciudades']],
     [2.6, 3.7, 3.7]),
    ('caja', 'concepto', 'Concepto clave — ',
     'Región natural: territorio con clima, relieve, suelos, vegetación y fauna parecidos. Ecosistema: conjunto de seres vivos y '
     'el ambiente en el que viven, con sus relaciones. Biodiversidad: variedad de seres vivos de un lugar.'),

    ('h2', 'Cambios y costos del uso de la tierra'),
    ('p', 'Para cultivar y criar ganado, las personas transforman las regiones naturales. Esos cambios traen beneficios —alimentos, '
          'trabajo, exportaciones— y también costos socioambientales, es decir, perjuicios para el ambiente y para las personas:'),
    ('lista', ['Deforestación: en la Región Oriental se perdió la mayor parte del Bosque Atlántico durante el siglo XX, y en las últimas '
               'décadas el desmonte avanzó en el Chaco.',
               'Pérdida de biodiversidad: al desaparecer el bosque, desaparecen el hábitat de muchas especies y plantas medicinales.',
               'Erosión y pérdida de suelos fértiles, y menos agua en arroyos y nacientes.',
               'Contaminación por el uso inadecuado de agroquímicos.',
               'Costos sociales: comunidades indígenas y campesinas que pierden los montes de los que obtenían alimentos, medicinas y '
               'materiales, y conflictos por la tierra.']),
    ('caja', 'paraguay', 'En Paraguay — ',
     'Para frenar la deforestación en la Región Oriental, una ley prohibió en 2004 transformar bosques en tierras de cultivo o de '
     'pastoreo, y desde entonces fue prorrogada. En la Clase 21 vas a estudiar las leyes y las instituciones ambientales.'),

    ('fuente', 'Fuente cartográfica · Figura 20.2 (esquema de la editorial con datos de Natural Earth)',
     ['Leé el mapa de la Figura 20.2: la ubicación de cada ecosistema respecto de los ríos y de las dos regiones.'],
     '',
     ['¿Qué ecosistemas están en la Región Occidental y cuáles en la Región Oriental?',
      '¿Qué ecosistema está cerca del río Paraná, en el este? ¿Y en el norte del Chaco, junto al río Paraguay?',
      'El mapa aclara que no reproduce los límites oficiales. ¿Dónde buscarías el mapa oficial de ecorregiones?']),
    ('renglones', 5),
    ('ubicate', 'Ubicate  ·  Esquema de América (Figura 20.1)',
     'En la Figura 20.1, ¿qué región natural ocupa la Amazonía? ¿Cuáles están al sur del Paraguay? ¿En qué región natural de América '
     'está el Chaco paraguayo?'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. Una región natural es…'),
    ('opc', ['un departamento del país', 'una ciudad con muchos parques', 'un territorio con clima, relieve y vegetación parecidos',
             'una zona protegida por ley']),
    ('item', '2. El ecosistema de selva alta y muy diversa del este de la Región Oriental es…'),
    ('opc', ['el Bosque Atlántico del Alto Paraná', 'el Chaco Seco', 'el Pantanal', 'la estepa patagónica']),
    ('item', '3. El Chaco Seco se caracteriza por…'),
    ('opc', ['selvas lluviosas todo el año', 'bosques bajos y espinosos, cactus y pocas lluvias', 'glaciares y tundra',
             'esteros que cubren todo el territorio']),
    ('item', '4. Un costo socioambiental de la deforestación es…'),
    ('opc', ['el aumento de la biodiversidad', 'la mejora de los suelos', 'el aumento del agua de las nacientes',
             'la pérdida del hábitat de muchas especies']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. La variedad de seres vivos de un lugar se llama ________.'),
    ('item', '6. El gran humedal del norte del Chaco, compartido con el Brasil y Bolivia, es el ________.'),
    ('item', '7. Las sabanas con árboles dispersos del Brasil central se llaman ________.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) Las regiones naturales tienen límites exactos.'),
    ('item', '9. (....) En el Chaco, la actividad principal es la ganadería.'),
    ('item', '10. (....) El uso de la tierra solo trae beneficios.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. Compará la Región Occidental y la Región Oriental del Paraguay: clima, vegetación y actividades.', 4),
    ('item', '12. Escribí un texto de 6 a 8 líneas sobre los cambios que produce el uso de la tierra en el Paraguay. Se tendrá en '
             'cuenta: un beneficio (1 punto), dos costos socioambientales (2 puntos) y un texto ordenado (1 punto).', 8),
]

PLAN = {
    'material': 'Tomo: Clase 20 (Figuras 20.1 y 20.2); imágenes de ecosistemas paraguayos si la escuela las tiene',
    'tema': C.TEMAS['G4a'] + ' ' + C.TEMAS['G4b'] + ' ' + C.TEMAS['G4d'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes describan las regiones naturales de América y del Paraguay y analicen beneficios y costos '
                 'socioambientales del uso de la tierra.',
    'funciones': {
        'Esenciales': 'En clase: Ubicate; fuente (preguntas 1 a 3); actividades 1, 2, 3, 4 y 11.',
        'Consolidación': 'Actividades 5, 6, 8 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 33).',
        'Complementarias o domiciliarias': 'Actividades 7, 10 y 12.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 19. Pregunta: «¿Qué plantas y animales hay cerca de tu casa? ¿Siempre estuvieron allí?».',
             'Nombran plantas y animales del lugar.', 'Lista en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–20', 'Lectura de «Qué es una región natural» y del Concepto clave.', 'Resuelven la actividad 1.', 'Actividad 1 (esencial).'),
            ('20–38', 'Lectura de «Las regiones naturales de América» con la Figura 20.1.',
             'Resuelven el «Ubicate».', 'Ubicate (esencial).'),
            ('38–62', 'Lectura de «Las regiones naturales del Paraguay» con la Figura 20.2 y el cuadro comparativo.',
             'Responden las preguntas 1 a 3 de la fuente y las actividades 2, 3 y 11.', 'Fuente y actividades 2, 3 y 11 (esenciales).'),
            ('62–82', 'Lectura de «Cambios y costos del uso de la tierra» y de la caja «En Paraguay». Organiza una lista en dos columnas: beneficios y costos.',
             'Completan la lista y resuelven la actividad 4.', 'Lista de beneficios y costos; actividad 4 (esencial).'),
            ('82–100', 'Acompaña; quien termina antes sigue con la consolidación.', 'Resuelven las actividades 5, 6, 8 y 9.',
             'Actividades de consolidación.'),
        ]),
        ('Cierre', [
            ('100–120', 'Puesta en común de la actividad 11 y de la lista de beneficios y costos. Lee los criterios de la actividad 12 y asigna la tarea.',
             'Corrigen con otro color.', 'Actividad 11 revisada.'),
        ]),
    ],
    'diversidad': [
        'Apoyo visual: imágenes del Chaco Seco, del Pantanal y del Bosque Atlántico para comparar.',
        'Apoyo en la actividad 11: cuadro de la clase como modelo, para completar con palabras propias.',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: averiguar qué área silvestre protegida está más cerca de la localidad y qué ecosistema protege.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Lectura de esquemas y mapas; análisis de fuente cartográfica; cuadro comparativo; respuesta breve.',
        'instrumentos': 'Lista de cotejo con los tres indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Describe regiones naturales de América.',
                      'Diferencia los ecosistemas de las dos regiones del Paraguay.',
                      'Explica beneficios y costos socioambientales del uso de la tierra.'],
    },
    'precisiones': [
        'Las Figuras 20.1 y 20.2 son esquemas de ubicación; los límites oficiales de las ecorregiones están en el mapa del MADES.',
        'No se dan porcentajes de deforestación: si se usan, deben tomarse de una fuente oficial con fecha (INFONA, MADES).',
        'Tratar los costos sociales con respeto por las comunidades indígenas y campesinas afectadas.',
    ],
    'tarea': 'Actividades 7, 10 y 12 de la Clase 20.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente (cartográfica)', [
            ('F1', 'Región Occidental: Chaco Seco, Chaco Húmedo y Pantanal. Región Oriental: Bosque Atlántico del Alto Paraná, Cerrado y '
                   'humedales del Ñeembucú.', 'El Cerrado también llega al Chaco; se acepta si lo justifica.'),
            ('F2', 'El Bosque Atlántico del Alto Paraná; en el norte del Chaco, el Pantanal.', ''),
            ('F3', 'En el Ministerio del Ambiente y Desarrollo Sostenible (MADES).', ''),
        ]),
        ('Ubicate (Figura 20.1)', [
            ('U', 'La selva tropical. Al sur del Paraguay: la pampa y la estepa patagónica. El Chaco paraguayo está en la región del '
                  'Gran Chaco.', ''),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'c) un territorio con clima, relieve y vegetación parecidos', ''),
            ('2', 'a) el Bosque Atlántico del Alto Paraná', ''),
            ('3', 'b) bosques bajos y espinosos, cactus y pocas lluvias', ''),
            ('4', 'd) la pérdida del hábitat de muchas especies', ''),
        ]),
        ('Completá los espacios', [
            ('5', 'biodiversidad', ''),
            ('6', 'Pantanal', ''),
            ('7', 'Cerrado', ''),
        ]),
        ('Verdadero o falso', [
            ('8', 'Falso: pasan gradualmente de una a otra.', 'Justificación obligatoria.'),
            ('9', 'Verdadero.', ''),
            ('10', 'Falso: trae beneficios y también costos socioambientales.', 'Justificación obligatoria.'),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'Occidental: más seca y calurosa; bosques secos, palmares, pastizales y humedales; ganadería. Oriental: más húmeda; '
                   'selva del Alto Paraná, Cerrado y humedales; agricultura, ganadería y ciudades.', 'Las tres características para ambas regiones.'),
            ('12', 'Ejemplo: «El uso de la tierra para cultivos y ganado da alimentos, trabajo y exportaciones. Pero la deforestación hizo '
                   'perder la mayor parte del Bosque Atlántico y avanza en el Chaco: se pierde el hábitat de muchas especies y los suelos '
                   'se erosionan. Además, comunidades indígenas pierden los montes de los que vivían.»',
             'Criterio anunciado en la consigna: un beneficio (1 punto), dos costos socioambientales (2 puntos) y un texto ordenado (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Ecosistemas del Paraguay (Chaco Seco, Chaco Húmedo, Pantanal, Cerrado, Bosque Atlántico del Alto Paraná, humedales del Ñeembucú)',
     'Denominaciones habituales; el MADES tiene una clasificación oficial de ecorregiones que debe cotejarse.'),
    ('Pérdida de la mayor parte del Bosque Atlántico en el siglo XX; avance del desmonte en el Chaco', 'Afirmación cualitativa habitual; cotejar con INFONA o MADES antes de agregar cifras.'),
    ('Ley de 2004 que prohíbe la conversión de bosques en la Región Oriental (Ley 2524/2004) y sus prórrogas', 'Cotejar en la BACN.'),
    ('Figuras 20.1 y 20.2', 'Esquemas de la editorial.'),
]
