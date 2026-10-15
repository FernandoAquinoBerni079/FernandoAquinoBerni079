"""Encuentro 26 — Clase 16: La posición geográfica del Paraguay y de América (G1; temas G1a, G1b y G1c).

Corrige el maestro: trata la posición de América (océanos, hemisferios,
división, paralelos y meridianos); da la posición absoluta con latitud y
longitud; describe los límites con la fórmula completa; agrega el Laudo Hayes
(1878); evita la causalidad valorativa («por eso mantiene buenas relaciones»).
Plan 26: los primeros 20 minutos son la devolución de la Evaluación de la
Unidad 4 (condición A10).
"""
import curriculo as C

TITULO = 'Clase 16 — La posición geográfica del Paraguay y de América'
CLAVE = 'Clase 16 —'
INDICADORES = [
    'Describe la ubicación, los límites y la extensión del Paraguay y de América.',
    'Diferencia la posición absoluta (coordenadas) de la posición relativa.',
    'Relaciona la posición geográfica del Paraguay con actividades de su población.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['G1'], C.TEMAS['G1a'] + ' ' + C.TEMAS['G1b'] + ' ' + C.TEMAS['G1c'], INDICADORES),

    ('h2', 'Paralelos, meridianos y coordenadas'),
    ('p', 'Para ubicar un lugar en la Tierra se usan líneas imaginarias. Los paralelos son círculos que rodean la Tierra de este a '
          'oeste; el principal es el Ecuador (0°), que la divide en hemisferio norte y hemisferio sur. Los meridianos van de polo a '
          'polo; el principal es el meridiano de Greenwich (0°), que la divide en hemisferio oriental y hemisferio occidental.'),
    ('p', 'La latitud es la distancia en grados de un lugar al Ecuador (norte o sur); la longitud, la distancia en grados al '
          'meridiano de Greenwich (este u oeste). Con las dos coordenadas se indica la posición absoluta de un lugar. Otros '
          'paralelos importantes son los trópicos de Cáncer y de Capricornio (unos 23° 26\') y los círculos polares.'),

    ('h2', 'La posición de América'),
    ('p', 'América es un continente del hemisferio occidental que se extiende de norte a sur, desde el océano Glacial Ártico hasta '
          'el cabo de Hornos, cerca de la Antártida. Está entre el océano Atlántico, al este, y el océano Pacífico, al oeste. Es '
          'atravesada por el Ecuador y por los dos trópicos, por eso tiene todos los climas de la Tierra. Su superficie es de unos '
          '42 millones de kilómetros cuadrados.'),
    ('p', 'Se divide en América del Norte, América Central —un istmo, es decir, una franja angosta de tierra, y las islas del '
          'Caribe— y América del Sur. También se habla de América Latina para referirse a los países donde se hablan lenguas '
          'derivadas del latín, como el castellano, el portugués y el francés.'),
    ('h2', 'La posición absoluta del Paraguay'),
    ('p', 'El Paraguay está en el centro de América del Sur, en los hemisferios sur y occidental. Se ubica aproximadamente entre '
          'los 19° 18\' y los 27° 36\' de latitud sur, y entre los 54° 19\' y los 62° 38\' de longitud oeste. El trópico de '
          'Capricornio lo atraviesa por el centro, cerca de la ciudad de Concepción y del Chaco central. Su superficie es de '
          '406.752 kilómetros cuadrados y se organiza en 17 departamentos y la capital, Asunción.'),

    ('fig', 'fig_16_1_america.png', 'Figura 16.1 — América: paralelos principales y ubicación del Paraguay.', 11.0),

    ('h2', 'Límites y posición relativa'),
    ('tabla', ['Punto cardinal', 'Países limítrofes', 'Ríos que marcan parte del límite'],
     [['Norte', 'Bolivia y Brasil', 'río Apa y río Paraguay (con Brasil); río Negro u Otuquis (con Bolivia, aprox. 38 km)'],
      ['Este', 'Brasil y Argentina', 'río Paraná'],
      ['Sur', 'Argentina', 'ríos Paraguay y Paraná'],
      ['Oeste', 'Argentina y Bolivia', 'río Pilcomayo (con la Argentina)']],
     [2.2, 3.6, 4.2]),
    ('p', 'La posición relativa describe un lugar en relación con otros: el Paraguay es un país mediterráneo, sin costa marítima, '
          'rodeado por la Argentina, el Brasil y Bolivia, y unido al océano Atlántico por los ríos Paraguay y Paraná.'),
    ('p', 'Sus límites actuales se fijaron después de dos guerras, por tratados y por un arbitraje: el tratado con el Brasil (1872), '
          'el tratado con la Argentina (1876), el Laudo Hayes (1878), que reconoció al Paraguay el Chaco entre los ríos Verde y '
          'Pilcomayo, y el tratado de paz con Bolivia (1938), después de la Guerra del Chaco.'),
    ('fig', 'fig_16_2_paraguay_posicion.png', 'Figura 16.2 — Posición absoluta y límites del Paraguay (mapa aproximado).', 12.0),
    ('caja', 'concepto', 'Concepto clave — ',
     'Posición absoluta: ubicación exacta con latitud y longitud. Posición relativa: ubicación respecto de otros lugares '
     '(países vecinos, ríos, océanos). Mediterráneo: aquí significa «en medio de las tierras», sin costa marítima; es la misma '
     'palabra que da nombre al mar Mediterráneo, rodeado de tierras.'),

    ('h2', 'Posición y actividades de la población'),
    ('p', 'La posición influye en la vida de la población, junto con otros factores como el clima, los suelos, la tecnología y las '
          'decisiones de las personas. Por estar en una zona subtropical, con lluvias y temperaturas cálidas, el Paraguay tiene '
          'buenas condiciones para la agricultura y la ganadería. Por ser mediterráneo, depende de los ríos y de los puertos de los '
          'países vecinos para su comercio exterior: necesita acuerdos de libre navegación y de uso de puertos. Su ubicación central '
          'en América del Sur también lo convierte en un lugar de paso entre países.'),
    ('caja', 'paraguay', 'En Paraguay — ',
     'La Hidrovía Paraguay-Paraná es la principal vía del comercio exterior: por ella salen la soja, la carne y otros productos y '
     'entran combustibles e insumos. La vas a estudiar en la Clase 18.'),

    ('fuente', 'Fuente cartográfica · Figura 16.2 (elaboración de la editorial con datos de Natural Earth)',
     ['Leé el mapa de la Figura 16.2: sus coordenadas, los puntos extremos, los ríos y los países vecinos.'],
     '',
     ['¿Entre qué paralelos se ubica el Paraguay? ¿Y entre qué meridianos?',
      '¿Qué paralelo importante atraviesa el país? ¿Qué te dice eso sobre su clima?',
      'El mapa dice que es «aproximado» y que las coordenadas deben cotejarse con el IGM o el INE. ¿Por qué es importante que un '
      'mapa indique su fuente?']),
    ('renglones', 5),
    ('ubicate', 'Ubicate  ·  Mapas (Figuras 16.1 y 16.2)',
     'En la Figura 16.1, ¿qué océanos rodean América? ¿En qué hemisferios está el Paraguay? En la Figura 16.2, nombrá un río que '
     'marque el límite con cada país vecino.'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. La posición absoluta de un lugar se indica con…'),
    ('opc', ['la latitud y la longitud', 'los países vecinos', 'la distancia al mar', 'el nombre de la capital']),
    ('item', '2. El Paraguay está en los hemisferios…'),
    ('opc', ['norte y oriental', 'norte y occidental', 'sur y oriental', 'sur y occidental']),
    ('item', '3. El Laudo Hayes (1878)…'),
    ('opc', ['fijó el límite con el Brasil', 'puso fin a la Guerra del Chaco', 'reconoció al Paraguay el Chaco entre los ríos Verde y Pilcomayo',
             'creó los 17 departamentos']),
    ('item', '4. Por ser un país mediterráneo, el Paraguay…'),
    ('opc', ['tiene costas sobre el océano Atlántico', 'necesita acuerdos de navegación y uso de puertos con sus vecinos',
             'no tiene ríos navegables', 'no puede comerciar con otros países']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. El paralelo de 0° se llama ________.'),
    ('item', '6. El trópico de ________ atraviesa el Paraguay.'),
    ('item', '7. Al norte, el río ________ marca parte del límite con el Brasil.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) América está entre el océano Atlántico y el océano Pacífico.'),
    ('item', '9. (....) El Paraguay limita al oeste solo con Bolivia.'),
    ('item', '10. (....) La posición relativa describe un lugar en relación con otros lugares.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. Describí la posición absoluta y la posición relativa del Paraguay.', 4),
    ('item', '12. Escribí un texto de 6 a 8 líneas sobre cómo influye la posición del Paraguay en las actividades de su población. '
             'Se tendrá en cuenta: un efecto de la latitud (1 punto), un efecto de la mediterraneidad (1 punto), otro factor que '
             'también influye (1 punto) y un texto ordenado (1 punto).', 8),
]

PLAN = {
    'material': 'La Evaluación de la Unidad 4 corregida (para la devolución); tomo: Clase 16 (Figuras 16.1 y 16.2); planisferio o globo terráqueo',
    'tema': C.TEMAS['G1a'] + ' ' + C.TEMAS['G1b'] + ' ' + C.TEMAS['G1c'],
    'indicadores': INDICADORES,
    'proposito': 'Devolver la Evaluación de la Unidad 4 y que los estudiantes describan la posición absoluta y relativa del Paraguay '
                 'y de América y la relacionen con las actividades de la población.',
    'funciones': {
        'Esenciales': 'En clase: Ubicate; fuente (preguntas 1 a 3); actividades 1, 2, 4 y 11.',
        'Consolidación': 'Actividades 3, 5, 8 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 27).',
        'Complementarias o domiciliarias': 'Actividades 6, 7, 10 y 12.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–20', 'Devolución de la Evaluación de la Unidad 4: entrega las pruebas corregidas, explica las claves y los criterios de la Parte E y comenta los errores más frecuentes. Se hace solo si todas las pruebas, incluidas las de apoyo excepcional, ya están entregadas.',
             'Revisan su prueba y anotan en qué deben mejorar.', 'Devolución de la evaluación.'),
            ('20–25', 'Pregunta: «¿Cómo le explicarías a alguien de otro continente dónde queda el Paraguay?».',
             'Proponen descripciones.', 'Ideas en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('25–42', 'Lectura de «Paralelos, meridianos y coordenadas» con el globo o el planisferio.',
             'Señalan el Ecuador, Greenwich y los trópicos; resuelven la actividad 1.', 'Actividad 1 (esencial).'),
            ('42–58', 'Lectura de «La posición de América» con la Figura 16.1.',
             'Resuelven el «Ubicate» y la actividad 2.', 'Ubicate y actividad 2 (esenciales).'),
            ('58–78', 'Lectura de «La posición absoluta del Paraguay» y de «Límites y posición relativa» con la Figura 16.2.',
             'Responden las preguntas 1 a 3 de la fuente y la actividad 11.', 'Fuente y actividad 11 (esenciales).'),
            ('78–88', 'Lectura de «Posición y actividades de la población»; destaca que la posición influye junto con otros factores.',
             'Resuelven la actividad 4.', 'Actividad 4 (esencial).'),
            ('88–106', 'Acompaña; quien termina antes sigue con la consolidación.', 'Resuelven las actividades 3, 5, 8 y 9.',
             'Actividades de consolidación.'),
        ]),
        ('Cierre', [
            ('106–120', 'Puesta en común de la actividad 11. Lee los criterios de la actividad 12 y asigna la tarea.',
             'Corrigen con otro color.', 'Actividad 11 revisada.'),
        ]),
    ],
    'diversidad': [
        'Si alguna prueba de apoyo excepcional de la Unidad 4 todavía no fue entregada, la devolución con claves se posterga para el encuentro 27 y estos 20 minutos se usan para la lectura guiada; nadie recibe respuestas mientras alguien siga rindiendo.',
        'Apoyo con material concreto: una naranja o una pelota con el Ecuador y un meridiano dibujados para mostrar latitud y longitud.',
        'Apoyo en la actividad 11: cuadro de dos columnas en la pizarra («absoluta» / «relativa»).',
        'Desafío: buscar las coordenadas de la escuela con un mapa digital y compararlas con las del Paraguay.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Lectura de mapas; análisis de fuente cartográfica; respuesta breve.',
        'instrumentos': 'Lista de cotejo con los tres indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Describe ubicación, límites y extensión del Paraguay y de América.',
                      'Diferencia posición absoluta y relativa.',
                      'Relaciona la posición con actividades, junto con otros factores.'],
    },
    'precisiones': [
        'La posición absoluta exige latitud y longitud; no basta con la latitud.',
        'Evitar el determinismo: la posición influye junto con otros factores (clima, suelos, tecnología, decisiones humanas).',
        'Primeros 20 minutos: devolución de la Evaluación de la Unidad 4, reservada por la condición A10.',
    ],
    'tarea': 'Actividades 6, 7, 10 y 12 de la Clase 16.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente (cartográfica)', [
            ('F1', 'Entre los paralelos de 19° 18\' y 27° 36\' de latitud sur, y entre los meridianos de 54° 19\' y 62° 38\' de longitud oeste.',
             'Se aceptan valores aproximados (19° a 28° S; 54° a 63° O).'),
            ('F2', 'El trópico de Capricornio. El país está en la zona subtropical: es cálido, con veranos calurosos.', ''),
            ('F3', 'Porque permite saber de dónde salieron los datos, qué tan precisos son y dónde comprobarlos.', ''),
        ]),
        ('Ubicate (Figuras 16.1 y 16.2)', [
            ('U', 'Los océanos Atlántico, Pacífico y Glacial Ártico. El Paraguay está en los hemisferios sur y occidental. Ríos: Apa o '
                  'Paraguay o Apa con Brasil; Paraná o Pilcomayo con Argentina; Negro u Otuquis con Bolivia, cuyo límite es mayormente terrestre (unos 38 km fluviales).',
             'Un río por país: para Bolivia, Negro u Otuquis; aceptar la explicación de que la mayor parte del límite boliviano es seco, si identifica el tramo fluvial.'),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'a) la latitud y la longitud', ''),
            ('2', 'd) sur y occidental', ''),
            ('3', 'c) reconoció al Paraguay el Chaco entre los ríos Verde y Pilcomayo', ''),
            ('4', 'b) necesita acuerdos de navegación y uso de puertos con sus vecinos', ''),
        ]),
        ('Completá los espacios', [
            ('5', 'Ecuador', ''),
            ('6', 'Capricornio', ''),
            ('7', 'Apa', 'Se acepta «Paraguay».'),
        ]),
        ('Verdadero o falso', [
            ('8', 'Verdadero.', ''),
            ('9', 'Falso: al oeste limita con la Argentina y con Bolivia.', 'Justificación obligatoria.'),
            ('10', 'Verdadero.', ''),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'Absoluta: entre 19° 18\' y 27° 36\' de latitud sur y entre 54° 19\' y 62° 38\' de longitud oeste. Relativa: en el '
                   'centro de América del Sur, sin costa marítima, entre la Argentina, el Brasil y Bolivia, unido al Atlántico por los '
                   'ríos Paraguay y Paraná.', 'Las dos posiciones; se aceptan coordenadas aproximadas.'),
            ('12', 'Ejemplo: «Por estar cerca del trópico de Capricornio, el Paraguay tiene un clima cálido y lluvias que favorecen la '
                   'agricultura y la ganadería. Por ser mediterráneo, su comercio exterior depende de la Hidrovía y de los puertos de los '
                   'vecinos. Pero también influyen los suelos, la tecnología y las decisiones de las personas.»',
             'Criterio anunciado en la consigna: un efecto de la latitud (1 punto), un efecto de la mediterraneidad (1 punto), otro '
             'factor que también influye (1 punto) y un texto ordenado (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Coordenadas extremas (19° 18\' S; 27° 36\' S; 54° 19\' O; 62° 38\' O) y superficie de 406.752 km²', 'Datos de la bibliografía escolar; cotejar con el IGM o el INE.'),
    ('17 departamentos y la capital', 'Organización territorial vigente; cotejar.'),
    ('Superficie de América (unos 42 millones de km²)', 'Dato aproximado habitual; cotejar.'),
    ('Tratados de límites: Brasil 1872, Argentina 1876, Laudo Hayes 1878, Bolivia 1938', 'Fechas habituales; cotejar.'),
    ('Ríos limítrofes y puntos extremos de la Figura 16.2', 'Mapa aproximado; Natural Earth no trae el río Apa.'),
]
