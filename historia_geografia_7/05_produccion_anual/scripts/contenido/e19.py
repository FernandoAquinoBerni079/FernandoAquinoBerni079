"""Encuentro 19 — Clase 11: La división de la provincia (1617) y la mediterraneidad (H5; tema H5a).

Corrige el maestro: la mediterraneidad es una condición geográfica; la
división de 1617 (causa político-administrativa) la convirtió en dependencia
política y comercial. Agrega a Hernandarias, las ciudades de cada gobernación
y el paso obligado por Santa Fe y Buenos Aires. Sustituye el «testimonio de un
vecino» inventado por una fuente secundaria declarada.
Plan 19: los primeros 20 minutos son la devolución de la Evaluación
Integradora de la 1.ª etapa (condición A10).
"""
import curriculo as C

TITULO = 'Clase 11 — La división de la provincia (1617) y la mediterraneidad'
CLAVE = 'Clase 11 —'
INDICADORES = [
    'Explica las causas de la división de la provincia en 1617.',
    'Distingue la mediterraneidad, condición geográfica, de la dependencia que produjo la división.',
    'Describe consecuencias de la división para la economía y la vida de la provincia del Paraguay.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H5'], C.TEMAS['H5a'], INDICADORES),

    ('h2', 'Una provincia enorme'),
    ('p', 'A comienzos del siglo XVII, la provincia del Paraguay —también llamada del Río de la Plata— era enorme. Desde Asunción '
          'se gobernaban ciudades fundadas por expediciones salidas de ella: Buenos Aires, Santa Fe, Corrientes, Concepción del '
          'Bermejo, Villa Rica del Espíritu Santo, Ciudad Real del Guairá y Santiago de Jerez. Entre una ciudad y otra había '
          'cientos de kilómetros de ríos, selvas y llanuras, y los viajes duraban semanas.'),
    ('p', 'El gobernador Hernando Arias de Saavedra, conocido como Hernandarias, nacido en Asunción en 1561, fue el primer '
          'gobernador criollo, es decir, nacido en América. Gobernó la provincia varias veces entre fines del siglo XVI y 1618. '
          'Conocía bien las dificultades de gobernar un territorio tan grande y propuso al rey dividirlo.'),

    ('h2', 'La división de 1617: causas'),
    ('p', 'En 1617, el rey Felipe III dividió la provincia en dos gobernaciones. Las causas fueron varias:'),
    ('lista', ['la enorme extensión, que hacía casi imposible gobernar y defender todas las ciudades desde un solo lugar;',
               'el crecimiento de Buenos Aires, que por su puerto se había vuelto importante y pedía gobierno propio;',
               'la propuesta de Hernandarias, que conocía el territorio y sus problemas.']),
    ('tabla', ['Gobernación del Paraguay o del Guairá (capital: Asunción)', 'Gobernación del Río de la Plata (capital: Buenos Aires)'],
     [['Asunción, Villa Rica del Espíritu Santo, Ciudad Real del Guairá, Santiago de Jerez',
       'Buenos Aires, Santa Fe, Corrientes, Concepción del Bermejo']],
     [5.0, 5.0]),
    ('fig', 'fig_11_1_division_1617.png', 'Figura 11.1 — Ciudades de las dos gobernaciones después de la división de 1617 (posiciones aproximadas).', 12.0),

    ('h2', 'Mediterraneidad y dependencia'),
    ('p', 'Asunción siempre estuvo lejos del mar: está a más de mil kilómetros de la desembocadura del Río de la Plata. Esa '
          'condición geográfica se llama mediterraneidad. La división de 1617 no cambió la geografía, pero sí cambió quién '
          'controlaba la salida al mar: el puerto de Buenos Aires quedó en manos de otra gobernación.'),
    ('p', 'Desde entonces, todo lo que el Paraguay vendía o compraba afuera bajaba por los ríos Paraguay y Paraná y debía pasar '
          'por Santa Fe y por Buenos Aires, donde se pagaban derechos e impuestos. Además, el comercio por Buenos Aires estaba muy '
          'limitado por la Corona: en 1622 se creó una aduana en Córdoba para controlar el paso de mercaderías entre el puerto y el '
          'Perú. Para los productores paraguayos, cada pago y cada demora hacían más caros sus productos.'),
    ('caja', 'concepto', 'Concepto clave — ',
     'Mediterraneidad: situación de un territorio sin costa marítima, rodeado de tierras. Es una condición geográfica. '
     'Dependencia: situación de quien necesita de otro para comerciar o decidir. La división de 1617 transformó la '
     'mediterraneidad del Paraguay en dependencia política y comercial de Buenos Aires.'),

    ('h2', 'Las secuelas de la mediterraneidad'),
    ('p', 'Las consecuencias se sintieron durante siglos: la provincia quedó más aislada y más pobre; sus productos, sobre todo la '
          'yerba mate, llegaban caros a los mercados; creció el contrabando para evitar los impuestos, y la defensa de las ciudades '
          'del este quedó más débil frente a los bandeirantes, como vas a ver en la Continuación E.'),
    ('caja', 'paraguay', 'En Paraguay — ',
     'Hoy el Paraguay sigue siendo un país mediterráneo. Por eso necesita acuerdos de libre navegación por los ríos y de uso de '
     'puertos en los países vecinos. La Hidrovía Paraguay-Paraná, que vas a estudiar en la Unidad 5, es la vía principal de su '
     'comercio exterior.'),

    ('fuente', 'Fuente secundaria · Las dos gobernaciones y sus ciudades (síntesis de la bibliografía histórica)',
     ['Gobernación del Paraguay o del Guairá: Asunción, Villa Rica del Espíritu Santo, Ciudad Real del Guairá y Santiago de Jerez. '
      'Gobernación del Río de la Plata: Buenos Aires, Santa Fe, Corrientes y Concepción del Bermejo.'],
     '',
     ['¿Cuál de las dos gobernaciones tenía el puerto sobre el Río de la Plata?',
      '¿Por qué ciudades debía pasar un barco que llevaba yerba de Asunción al mar? Usá la Figura 11.1.',
      'Esta lista no es un documento de 1617: es una síntesis hecha por historiadores. ¿Qué tipo de documento de la época '
      'buscarías para comprobarla?']),
    ('renglones', 5),
    ('ubicate', 'Ubicate  ·  Mapa (Figura 11.1)',
     'Seguí con el dedo la salida fluvial de Asunción al mar. ¿Por qué ríos navegaba un barco? ¿Qué ciudades de la otra '
     'gobernación encontraba en el camino?'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. Hernandarias fue importante porque…'),
    ('opc', ['fundó Asunción en 1537', 'fue el primer gobernador criollo y propuso la división de la provincia',
             'llegó desde España con la Real Provisión', 'encabezó el éxodo del Guairá']),
    ('item', '2. Después de 1617, Buenos Aires quedó como capital de…'),
    ('opc', ['la gobernación del Río de la Plata', 'la gobernación del Paraguay', 'el Virreinato del Perú', 'la Audiencia de Charcas']),
    ('item', '3. La mediterraneidad del Paraguay es…'),
    ('opc', ['una consecuencia de la división de 1617', 'un tratado con Buenos Aires', 'la falta de ríos navegables',
             'una condición geográfica: no tener costa marítima']),
    ('item', '4. Una consecuencia de la división fue que…'),
    ('opc', ['el Paraguay obtuvo un puerto propio sobre el mar', 'Asunción pasó a depender de Santa Fe y Buenos Aires para su comercio',
             'se suprimió el comercio de la yerba', 'Buenos Aires pasó a depender de Asunción']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. La provincia fue dividida en el año ________ por el rey Felipe III.'),
    ('item', '6. En 1622 se creó una aduana en la ciudad de ________ para controlar el comercio entre Buenos Aires y el Perú.'),
    ('item', '7. Santiago de Jerez y Ciudad Real del Guairá quedaron en la gobernación del ________.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) La división de 1617 alejó a Asunción del mar.'),
    ('item', '9. (....) Corrientes y Santa Fe quedaron en la gobernación del Río de la Plata.'),
    ('item', '10. (....) El contrabando creció para evitar los impuestos y controles.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. ¿Por qué se dice que la división convirtió la mediterraneidad en dependencia? Explicalo con tus palabras.', 4),
    ('item', '12. Escribí un texto de 6 a 8 líneas sobre la división de 1617. Se tendrá en cuenta: dos causas (2 puntos), una '
             'consecuencia para el Paraguay (1 punto) y la distinción entre mediterraneidad y dependencia (1 punto).', 8),
]

PLAN = {
    'material': 'La Evaluación Integradora de la 1.ª etapa corregida (para la devolución); tomo: Clase 11 (Figura 11.1); mapa de América del Sur',
    'tema': C.TEMAS['H5a'],
    'indicadores': INDICADORES,
    'proposito': 'Devolver la Evaluación Integradora de la 1.ª etapa y que los estudiantes expliquen la división de 1617 '
                 'distinguiendo la condición geográfica de la dependencia política y comercial.',
    'funciones': {
        'Esenciales': 'En clase: Ubicate; fuente (preguntas 1 a 3); actividades 1, 3, 4 y 11.',
        'Consolidación': 'Actividades 2, 5, 8 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 20).',
        'Complementarias o domiciliarias': 'Actividades 6, 7, 10 y 12.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–20', 'Devolución de la Evaluación Integradora de la 1.ª etapa: entrega las pruebas corregidas, explica las claves y los criterios de la Parte E y comenta los errores más frecuentes. Se hace solo si todas las pruebas, incluidas las de apoyo excepcional, ya están entregadas.',
             'Revisan su prueba y anotan en qué unidad deben mejorar.', 'Devolución de la evaluación.'),
            ('20–27', 'Pregunta: «¿Qué pasaría si para vender lo que producís tuvieras que pasar siempre por la casa de un vecino que cobra peaje?».',
             'Proponen ideas.', 'Ideas en la pizarra.'),
        ]),
        ('Desarrollo', [
            ('27–45', 'Lectura de «Una provincia enorme» y de «La división de 1617: causas», con el cuadro y la Figura 11.1.',
             'Resuelven el «Ubicate» y la actividad 1.', 'Ubicate y actividad 1 (esenciales).'),
            ('45–65', 'Lectura de «Mediterraneidad y dependencia» y del Concepto clave. Corrige el error frecuente: la división no alejó a Asunción del mar.',
             'Resuelven las actividades 3, 4 y 11.', 'Actividades 3, 4 y 11 (esenciales).'),
            ('65–82', 'Presenta la fuente y aclara que es una síntesis de historiadores, no un documento de 1617.',
             'Responden las preguntas 1 a 3 de la fuente.', 'Fuente (esencial).'),
            ('82–100', 'Lectura de «Las secuelas de la mediterraneidad» y de la caja «En Paraguay». Acompaña la consolidación.',
             'Resuelven las actividades 2, 5, 8 y 9.', 'Actividades de consolidación.'),
        ]),
        ('Cierre', [
            ('100–120', 'Puesta en común de la actividad 11 y de la pregunta 3 de la fuente. Lee los criterios de la actividad 12 y asigna la tarea.',
             'Corrigen con otro color.', 'Actividad 11 revisada.'),
        ]),
    ],
    'diversidad': [
        'Si alguna prueba de apoyo excepcional de la integradora todavía no fue entregada, la devolución con claves se posterga para el encuentro 20 y estos 20 minutos se usan para la lectura guiada de la clase; nadie recibe respuestas mientras alguien siga rindiendo.',
        'Apoyo en el mapa: el docente marca con tiza la salida fluvial y las ciudades de cada gobernación con dos colores.',
        'Apoyo en la actividad 11: comienzo dado «Antes de 1617, Asunción ya estaba lejos del mar, pero…».',
        'Desafío: averiguar qué es un «depósito franco» y para qué le sirve hoy al Paraguay.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Lectura de mapa; análisis de fuente secundaria; respuesta breve.',
        'instrumentos': 'Lista de cotejo con los tres indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Nombra dos causas de la división.',
                      'Distingue mediterraneidad y dependencia.',
                      'Da una consecuencia de la división para el Paraguay.'],
    },
    'precisiones': [
        'Error frecuente que hay que corregir: «la división dejó a Asunción sin salida al mar». Asunción ya era mediterránea; la división cambió quién controlaba el puerto.',
        'La fecha de la cédula de división es 1617; la separación efectiva de los gobiernos se completó en los años siguientes.',
        'Primeros 20 minutos: devolución de la integradora, reservada por la condición A10.',
    ],
    'tarea': 'Actividades 6, 7, 10 y 12 de la Clase 11.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente', [
            ('F1', 'La gobernación del Río de la Plata, con Buenos Aires.', ''),
            ('F2', 'Por Corrientes, Santa Fe y Buenos Aires, todas de la otra gobernación.', 'Basta con Santa Fe y Buenos Aires.'),
            ('F3', 'Un documento de época: la cédula real de 1617, cartas del Cabildo de Asunción o informes de gobernadores.',
             'Se acepta cualquier documento producido en la época.'),
        ]),
        ('Ubicate (Figura 11.1)', [
            ('U', 'Por el río Paraguay y luego por el Paraná. Encontraba Corrientes, Santa Fe y, al final, Buenos Aires.', ''),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'b) fue el primer gobernador criollo y propuso la división de la provincia', ''),
            ('2', 'a) la gobernación del Río de la Plata', ''),
            ('3', 'd) una condición geográfica: no tener costa marítima', ''),
            ('4', 'b) Asunción pasó a depender de Santa Fe y Buenos Aires para su comercio', ''),
        ]),
        ('Completá los espacios', [
            ('5', '1617', ''),
            ('6', 'Córdoba', ''),
            ('7', 'Paraguay (o del Guairá)', ''),
        ]),
        ('Verdadero o falso', [
            ('8', 'Falso: Asunción siempre estuvo lejos del mar; la división cambió quién controlaba el puerto de Buenos Aires.', 'Justificación obligatoria.'),
            ('9', 'Verdadero.', ''),
            ('10', 'Verdadero.', ''),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'Porque el Paraguay ya no tenía costa (mediterraneidad), pero hasta 1617 Buenos Aires era parte de la misma provincia. '
                   'Después de la división, el puerto quedó en manos de otra gobernación y el Paraguay tuvo que pagar y pedir permiso '
                   'para comerciar: pasó a depender de Buenos Aires.', 'Debe distinguir la condición geográfica de la situación política.'),
            ('12', 'Ejemplo: «En 1617 el rey dividió la provincia porque era enorme y difícil de gobernar y porque Buenos Aires había '
                   'crecido gracias a su puerto. Hernandarias lo había propuesto. El Paraguay ya era mediterráneo, pero desde entonces '
                   'dependió de Buenos Aires: sus productos pagaban impuestos en Santa Fe y Buenos Aires y llegaban caros.»',
             'Criterio anunciado en la consigna: dos causas (2 puntos), una consecuencia para el Paraguay (1 punto) y la distinción '
             'entre mediterraneidad y dependencia (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Hernandarias: nacimiento en Asunción (1561), primer gobernador criollo, gobiernos entre 1592 y 1618 y su propuesta de división',
     'Bibliografía habitual; cotejar años de cada gobierno.'),
    ('División de 1617 (cédula de Felipe III) y ciudades de cada gobernación', 'Cotejar fecha exacta de la cédula y la nómina de ciudades.'),
    ('Aduana de Córdoba (1622)', 'Dato de manual; cotejar.'),
    ('«Más de mil kilómetros» de Asunción a la desembocadura del Río de la Plata', 'Distancia aproximada por río; cotejar.'),
    ('Posiciones de Villa Rica, Ciudad Real, Santiago de Jerez, Concepción del Bermejo y Santa Fe (sitio de Cayastá) en la Figura 11.1',
     'Posiciones aproximadas de la editorial.'),
]
