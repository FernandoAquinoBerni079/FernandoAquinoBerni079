"""Encuentro 27 — Clase 17: El relieve del Paraguay y de América (G2; tema G2a).

Corrige el maestro: nombra las serranías del Paraguay (llamadas «cordilleras»)
y el cerro Tres Kandú; matiza el Chaco como llanura con elevaciones aisladas;
amplía el relieve de América (Rocosas, Apalaches, Sierra Madre, Andes,
macizos, mesetas y llanuras); precisa que los Andes son la cordillera
continental más larga; trae un perfil esquemático en lugar de una «recreación
generada por IA»; y explica la influencia del relieve junto con otros factores
(condición del dictamen para las Clases 16 y 17).
"""
import curriculo as C

TITULO = 'Clase 17 — El relieve del Paraguay y de América'
CLAVE = 'Clase 17 —'
INDICADORES = [
    'Describe el relieve de las regiones Oriental y Occidental del Paraguay.',
    'Reconoce las grandes formas de relieve de América y las ubica en un mapa.',
    'Relaciona el relieve con actividades humanas, junto con otros factores.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['G2'], C.TEMAS['G2a'], INDICADORES),

    ('h2', 'Las formas del relieve'),
    ('p', 'El relieve es el conjunto de formas que tiene la superficie terrestre. Las principales son las montañas (elevaciones de '
          'gran altura que forman cordilleras), las mesetas (terrenos altos y bastante planos), las llanuras (terrenos bajos y '
          'planos), las sierras o serranías (elevaciones menores) y los valles (terrenos bajos entre elevaciones). La parte de la '
          'geografía que estudia el relieve se llama orografía.'),

    ('h2', 'El relieve del Paraguay'),
    ('p', 'El Paraguay tiene un relieve bajo: casi todo el territorio está por debajo de los 500 metros sobre el nivel del mar. '
          'El río Paraguay separa dos regiones con relieves distintos.'),
    ('p', 'La Región Occidental o Chaco es una gran llanura que desciende suavemente de noroeste a sureste, hacia el río Paraguay. '
          'En el norte tiene algunas elevaciones aisladas, como el cerro León. Muchos de sus suelos se inundan en la época de lluvias '
          'y se secan en invierno.'),
    ('p', 'La Región Oriental tiene llanuras, colinas y serranías bajas. En el Paraguay se las llama «cordilleras», aunque por su '
          'altura son en realidad serranías: Amambay y Mbaracayú, en el noreste; Caaguazú y San Rafael, en el centro y el sureste; '
          'la cordillera de los Altos, cerca de Asunción; y la serranía de Ybytyruzú, en el Guairá, donde está el cerro Tres Kandú, '
          'el punto más alto del país, con unos 842 metros. Al sur, en Ñeembucú, predominan llanuras bajas con esteros.'),
    ('fig', 'fig_17_2_perfil.png', 'Figura 17.1 — Perfil esquemático del relieve del Paraguay de oeste a este.', 15.0),

    ('h2', 'El relieve de América'),
    ('p', 'América tiene una estructura que se repite de norte a sur: grandes cordilleras jóvenes al oeste, macizos antiguos y '
          'desgastados al este, y extensas llanuras en el centro.'),
    ('lista', ['Al oeste: las montañas Rocosas y la Sierra Madre, en América del Norte, y la cordillera de los Andes, en América del '
               'Sur. Los Andes son la cordillera continental más larga del mundo, con más de 7.000 kilómetros, y allí está el '
               'Aconcagua, el punto más alto de América, con unos 6.960 metros. Entre sus cordones hay altiplanos y volcanes.',
               'Al este: los montes Apalaches, en América del Norte, y los macizos de Guayana y de Brasilia, en América del Sur. Son '
               'formaciones muy antiguas, desgastadas por la erosión. En el sur está la meseta patagónica.',
               'En el centro: las llanuras centrales de América del Norte y, en América del Sur, las llanuras del Orinoco, la '
               'amazónica y la chaco-pampeana, de la que forma parte el Chaco paraguayo.']),
    ('fig', 'fig_17_1_relieve_america.png', 'Figura 17.2 — Grandes formas de relieve de América (esquema simplificado).', 11.0),
    ('caja', 'concepto', 'Concepto clave — ',
     'Cordillera: cadena de montañas altas. Serranía: conjunto de elevaciones de menor altura. Macizo: bloque de relieve antiguo, '
     'desgastado por la erosión. Llanura: terreno bajo y plano. Meseta: terreno alto y relativamente plano.'),

    ('h2', 'El relieve y las actividades humanas'),
    ('p', 'El relieve influye en las actividades humanas, pero nunca solo: actúa junto con el clima, los suelos, el agua, la '
          'tecnología, los mercados y las decisiones de las personas. Las llanuras facilitan la agricultura mecanizada y la '
          'construcción de caminos, pero solo producen bien si hay suelos fértiles, agua suficiente y acceso a mercados: en el Chaco, '
          'por ejemplo, la falta de agua dulce limita la agricultura y favorece la ganadería. En los Andes, los pueblos construyeron '
          'terrazas de cultivo para aprovechar las laderas, y la altura ofrece minerales y paisajes que atraen al turismo.'),
    ('caja', 'paraguay', 'En Paraguay — ',
     'Las serranías de la Región Oriental, como las de los Altos y de Ybytyruzú, atraen al turismo por sus paisajes y sus saltos de '
     'agua; las llanuras del este, con suelos rojos fértiles y lluvias abundantes, son la principal zona agrícola del país.'),

    ('fuente', 'Fuente gráfica · Figura 17.1, perfil esquemático (elaboración de la editorial)',
     ['Leé el perfil de la Figura 17.1 de oeste a este: dónde es más alto y más bajo el terreno y dónde corren los grandes ríos.'],
     '',
     ['¿En qué parte del perfil está el punto más bajo? ¿Qué río corre allí?',
      '¿Cómo cambia la altura del Chaco de oeste a este?',
      'El perfil tiene la escala vertical «muy exagerada». ¿Qué significa eso? ¿Por qué se hace?']),
    ('renglones', 5),
    ('ubicate', 'Ubicate  ·  Esquema de América (Figura 17.2)',
     'Ubicá la cordillera de los Andes, el macizo de Brasilia y la llanura chaco-pampeana. ¿En qué gran forma de relieve está el '
     'Chaco paraguayo?'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. El punto más alto del Paraguay es el cerro…'),
    ('opc', ['León', 'Lambaré', 'Tres Kandú', 'Aconcagua']),
    ('item', '2. Los macizos de Guayana y de Brasilia son…'),
    ('opc', ['cordilleras jóvenes y muy altas', 'formaciones antiguas desgastadas por la erosión', 'llanuras inundables', 'volcanes activos']),
    ('item', '3. La Región Occidental del Paraguay es…'),
    ('opc', ['una zona de altas montañas', 'una meseta volcánica', 'un conjunto de serranías', 'una gran llanura con algunas elevaciones aisladas en el norte']),
    ('item', '4. La cordillera continental más larga del mundo es…'),
    ('opc', ['la cordillera de los Andes', 'la cordillera de los Altos', 'la Sierra Madre', 'los montes Apalaches']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. El punto más alto de América es el ________, en los Andes.'),
    ('item', '6. La parte de la geografía que estudia el relieve se llama ________.'),
    ('item', '7. Las «cordilleras» de la Región Oriental son, por su altura, ________.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) El relieve es el único factor que explica dónde se cultiva en el Paraguay.'),
    ('item', '9. (....) El Chaco desciende suavemente hacia el río Paraguay.'),
    ('item', '10. (....) Las montañas Rocosas están en el este de América del Norte.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. Compará el relieve de la Región Oriental y el de la Región Occidental del Paraguay.', 4),
    ('item', '12. Escribí un texto de 6 a 8 líneas sobre cómo influye el relieve en una actividad humana del Paraguay o de América. '
             'Se tendrá en cuenta: la forma de relieve y su ubicación (1 punto), la actividad relacionada (1 punto), otro factor que '
             'también influye, como el clima, el suelo o el agua (1 punto) y un texto ordenado (1 punto).', 8),
]

PLAN = {
    'material': 'Tomo: Clase 17 (Figuras 17.1 y 17.2); mapa físico de América si la escuela lo tiene',
    'tema': C.TEMAS['G2a'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes describan el relieve del Paraguay y de América y lo relacionen con las actividades humanas '
                 'sin reducirlo a una sola causa.',
    'funciones': {
        'Esenciales': 'En clase: Ubicate; fuente (preguntas 1 a 3); actividades 1, 2, 3, 4 y 11.',
        'Consolidación': 'Actividades 5, 7, 8 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 28).',
        'Complementarias o domiciliarias': 'Actividades 6, 10 y 12.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 16. Pregunta: «¿Alguien subió alguna vez a un cerro del Paraguay? ¿Cómo era?».',
             'Cuentan experiencias.', 'Ideas en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('10–20', 'Lectura de «Las formas del relieve»; dibuja en la pizarra montaña, meseta, llanura y valle.',
             'Copian el dibujo con los nombres.', 'Esquema en el cuaderno.'),
            ('20–42', 'Lectura de «El relieve del Paraguay» con la Figura 17.1.',
             'Responden las preguntas 1 a 3 de la fuente y la actividad 1.', 'Fuente y actividad 1 (esenciales).'),
            ('42–55', 'Plantea la comparación entre las dos regiones.', 'Resuelven las actividades 3 y 11.', 'Actividades 3 y 11 (esenciales).'),
            ('55–72', 'Lectura de «El relieve de América» con la Figura 17.2 y el Concepto clave.',
             'Resuelven el «Ubicate» y las actividades 2 y 4.', 'Ubicate y actividades 2 y 4 (esenciales).'),
            ('72–84', 'Lectura de «El relieve y las actividades humanas»: destaca que el relieve actúa junto con otros factores.',
             'Dan un ejemplo oral de cada factor.', 'Ejemplos orales.'),
            ('84–102', 'Acompaña; quien termina antes sigue con la consolidación.', 'Resuelven las actividades 5, 7, 8 y 9.',
             'Actividades de consolidación.'),
        ]),
        ('Cierre', [
            ('102–120', 'Puesta en común de la actividad 11 y del V/F 8 (relieve y otros factores). Lee los criterios de la actividad 12 y asigna la tarea.',
             'Corrigen con otro color.', 'Actividad 11 revisada.'),
        ]),
    ],
    'diversidad': [
        'Variante si la devolución de la Evaluación de la Unidad 4 se posterga a este encuentro: 0 a 20 minutos, devolución con claves (sin revelarlas a quien todavía debe rendir); 20 a 120, la clase en 100 minutos. Se mantienen en clase todas las esenciales (Ubicate; fuente, preguntas 1 a 3; actividades 1, 2, 3, 4 y 11). Las de consolidación (5, 7, 8 y 9) pasan a casa, con revisión breve al abrir el encuentro 28; las complementarias quedan como tarea optativa.',
        'Apoyo con material concreto: modelar con plastilina o arena una montaña, una meseta, una llanura y un valle.',
        'Apoyo en la actividad 11: cuadro de dos columnas en la pizarra («Oriental» / «Occidental») con las palabras llanura, serranía, cerro, esteros.',
        'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
        'Desafío: averiguar a qué altura está la ciudad donde vivís y ubicarla aproximadamente en el perfil de la Figura 17.1.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Lectura de perfil y de esquema; comparación; respuesta breve.',
        'instrumentos': 'Lista de cotejo con los tres indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Describe el relieve de las dos regiones del Paraguay.',
                      'Reconoce y ubica las grandes formas de relieve de América.',
                      'Relaciona el relieve con actividades junto con otros factores.'],
    },
    'precisiones': [
        'Evitar el determinismo: el relieve influye junto con el clima, el suelo, el agua, la tecnología y los mercados (condición del dictamen).',
        'La Figura 17.1 es un perfil esquemático con alturas aproximadas; la Figura 17.2 no es un mapa topográfico.',
        'Altura del Tres Kandú: unos 842 m según la cifra habitual; puede haber mediciones distintas.',
    ],
    'tarea': 'Actividades 6, 10 y 12 de la Clase 17.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente (gráfica)', [
            ('F1', 'Junto al río Paraguay, en el centro del perfil.', ''),
            ('F2', 'Desciende suavemente de oeste a este, hacia el río Paraguay.', ''),
            ('F3', 'Que las alturas se dibujaron mucho más grandes que las distancias horizontales; se hace para que las diferencias de '
                   'altura, que son pequeñas comparadas con la anchura del país, se puedan ver.', ''),
        ]),
        ('Ubicate (Figura 17.2)', [
            ('U', 'Los Andes al oeste de América del Sur; el macizo de Brasilia al este; la llanura chaco-pampeana en el centro-sur. El '
                  'Chaco paraguayo forma parte de la llanura chaco-pampeana.', ''),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'c) Tres Kandú', ''),
            ('2', 'b) formaciones antiguas desgastadas por la erosión', ''),
            ('3', 'd) una gran llanura con algunas elevaciones aisladas en el norte', ''),
            ('4', 'a) la cordillera de los Andes', ''),
        ]),
        ('Completá los espacios', [
            ('5', 'Aconcagua', ''),
            ('6', 'orografía', ''),
            ('7', 'serranías', ''),
        ]),
        ('Verdadero o falso', [
            ('8', 'Falso: también influyen el clima, los suelos, el agua, la tecnología y los mercados.', 'Justificación obligatoria.'),
            ('9', 'Verdadero.', ''),
            ('10', 'Falso: están en el oeste; en el este están los Apalaches.', 'Justificación obligatoria.'),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'La Región Occidental es una gran llanura que desciende suavemente hacia el río Paraguay, con algunas elevaciones '
                   'aisladas en el norte. La Región Oriental tiene llanuras, colinas y serranías bajas (Amambay, Caaguazú, Ybytyruzú, '
                   'los Altos), con el punto más alto en el cerro Tres Kandú.', 'Una característica de cada región.'),
            ('12', 'Ejemplo: «En las llanuras del este del Paraguay se cultiva soja y maíz con máquinas, porque el terreno es plano. Pero '
                   'esto es posible también porque los suelos son fértiles y llueve bastante; en el Chaco, que también es llano, la falta '
                   'de agua dulce hace que predomine la ganadería.»',
             'Criterio anunciado en la consigna: la forma de relieve y su ubicación (1 punto), la actividad relacionada (1 punto), otro '
             'factor que también influye, como el clima, el suelo o el agua (1 punto) y un texto ordenado (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Cerro Tres Kandú, unos 842 m; cerro León en el Chaco', 'Cifra habitual; cotejar con el IGM.'),
    ('Aconcagua, unos 6.960 m; Andes, más de 7.000 km', 'Cifras habituales (6.961-6.962 m según la fuente); cotejar.'),
    ('Perfil de la Figura 17.1', 'Alturas aproximadas de la editorial; no es un perfil topográfico medido.'),
    ('Esquema de la Figura 17.2', 'Ubicación general de las formas de relieve; no es un mapa topográfico.'),
]
