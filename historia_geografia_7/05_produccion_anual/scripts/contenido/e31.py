"""Encuentro 31 — Clase 19: El clima de Paraguay y de América (G3; temas G3a, G3b y G3c).

Condición A10/N03 del dictamen: los primeros 20 minutos ordinarios son la
devolución de la Evaluación de la Unidad 5 y los 100 restantes desarrollan G3
completo. Ningún estudiante rinde la prueba mientras se revelan claves: el
apoyo excepcional se completa antes de este encuentro y, si alguien no pudo
rendir, lo hace después con una versión alternativa equivalente.
"""
import curriculo as C

TITULO = 'Clase 19 — El clima de Paraguay y de América'
CLAVE = 'Clase 19 —'
INDICADORES = [
    'Distingue los elementos del clima de los factores que lo modifican.',
    'Describe los grandes tipos de clima de América y las características climáticas del Paraguay.',
    'Explica influencias del clima en actividades humanas del Paraguay, junto con otros factores.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['G3'], C.TEMAS['G3a'] + ' ' + C.TEMAS['G3b'] + ' ' + C.TEMAS['G3c'], INDICADORES),

    ('h2', 'Tiempo y clima'),
    ('p', 'El tiempo atmosférico es el estado de la atmósfera en un lugar y un momento: «hoy llueve y hace 18 °C». El clima es el '
          'conjunto de condiciones que se repiten en un lugar a lo largo de muchos años, por lo menos treinta: «en Asunción los '
          'veranos son calurosos y húmedos». El tiempo cambia de un día a otro; el clima describe lo habitual.'),

    ('h2', 'Elementos y factores del clima'),
    ('p', 'Los elementos del clima son lo que se mide: la temperatura, las precipitaciones, la humedad, la presión atmosférica y los '
          'vientos. Los factores son las condiciones que modifican esos elementos: la latitud, la altitud, la distancia al mar, el '
          'relieve y las corrientes marinas.'),
    ('fig', 'fig_19_1_clima.png', 'Figura 19.1 — Elementos y factores del clima.', 15.0),
    ('caja', 'ejemplo', 'Ejemplo — ',
     'Quito, en el Ecuador, está casi sobre la línea del Ecuador, pero a unos 2.800 metros de altura: por eso su temperatura es '
     'templada todo el año. La altitud modifica lo que produciría la latitud.'),

    ('h2', 'Los tipos de clima de América'),
    ('p', 'Como América se extiende de norte a sur, tiene casi todos los climas de la Tierra. Cerca del Ecuador predomina el clima '
          'ecuatorial, cálido y muy lluvioso todo el año, como en la Amazonía. A los costados aparece el clima tropical, cálido con '
          'una estación seca y otra lluviosa. Más al sur y más al norte de los trópicos están los climas subtropicales y templados, '
          'con estaciones marcadas. Hacia los polos, los climas frío y polar. Hay climas áridos y desérticos donde llueve muy poco, '
          'como el desierto de Atacama, en Chile, y el norte de México. En los Andes, el clima de montaña cambia con la altura.'),
    ('fig', 'fig_19_2_climas_america.png', 'Figura 19.2 — Grandes tipos de clima de América (esquema simplificado).', 11.0),

    ('h2', 'El clima del Paraguay'),
    ('p', 'El Paraguay tiene un clima subtropical: veranos largos y calurosos, con temperaturas que en el Chaco pueden superar los '
          '40 °C, e inviernos cortos y suaves, con algunas heladas. Está atravesado por el trópico de Capricornio y no tiene mar ni '
          'montañas altas que modifiquen mucho su clima: por eso los vientos tienen gran importancia. El viento norte trae aire '
          'cálido y húmedo; el viento sur, aire frío y seco, y produce bajadas bruscas de temperatura.'),
    ('p', 'Las lluvias disminuyen de este a oeste: en el este de la Región Oriental caen unos 1.800 milímetros al año, y en el '
          'noroeste del Chaco, unos 600 (promedios del período 1971-2000). Por eso la Región Oriental es más húmeda y el Chaco, más seco. Algunos años, el fenómeno de '
          'El Niño produce lluvias abundantes e inundaciones, y el de La Niña, sequías.'),
    ('fig', 'fig_19_3_lluvias_py.png', 'Figura 19.3 — Las lluvias en el Paraguay aumentan hacia el este (valores aproximados).', 11.0),
    ('caja', 'concepto', 'Concepto clave — ',
     'Clima: condiciones atmosféricas habituales de un lugar a lo largo de muchos años. Elementos del clima: lo que se mide '
     '(temperatura, lluvias, humedad, presión, vientos). Factores del clima: lo que modifica esos elementos (latitud, altitud, '
     'distancia al mar, relieve, corrientes marinas).'),

    ('h2', 'El clima y las actividades humanas'),
    ('p', 'El clima influye en las actividades humanas, junto con otros factores como los suelos, la tecnología y los mercados:'),
    ('lista', ['Agricultura: el calor y las lluvias de la Región Oriental permiten dos cosechas al año (por ejemplo, soja en verano y '
               'trigo en invierno); una sequía puede reducir mucho la producción.',
               'Ganadería: el Chaco, más seco, se dedica sobre todo a la ganadería, con pasturas adaptadas al calor.',
               'Transporte: en los años secos bajan los ríos y las barcazas de la Hidrovía deben salir con menos carga.',
               'Salud y vida diaria: el calor y la humedad del verano favorecen al mosquito que transmite el dengue; la ropa, las '
               'viviendas y los horarios se adaptan al calor.']),
    ('caja', 'paraguay', 'En Paraguay — ',
     'La Dirección de Meteorología e Hidrología registra todos los días la temperatura, las lluvias y los vientos en estaciones de '
     'todo el país. Con esos datos, a lo largo de muchos años, se describe el clima.'),

    ('fuente', 'Fuente cartográfica · Figura 19.3 (esquema de la editorial con valores aproximados)',
     ['Leé el mapa de la Figura 19.3: la flecha, los valores de lluvia anual y la ubicación de las dos regiones.'],
     '',
     ['¿En qué región llueve más? ¿Cuántos milímetros por año, aproximadamente?',
      '¿Qué diferencia de lluvia hay entre el este y el noroeste del país?',
      'El mapa dice que los valores son «redondeados y varían de un año a otro». ¿Por qué el clima se describe con datos de muchos años?']),
    ('renglones', 5),
    ('ubicate', 'Ubicate  ·  Esquema de América (Figura 19.2)',
     'En la Figura 19.2, ¿qué tipo de clima tiene el Paraguay? ¿Qué clima hay en la Amazonía y cuál en la Patagonia? ¿Por qué el '
     'clima cambia de norte a sur?'),
    ('renglones', 3),

    ('h3', 'Actividades de aplicación'),
    ('consigna', 'Marcá la opción correcta:'),
    ('item', '1. Un elemento del clima es…'),
    ('opc', ['la temperatura', 'la latitud', 'la altitud', 'la distancia al mar']),
    ('item', '2. «Hoy llueve y hace 18 °C» describe…'),
    ('opc', ['el clima', 'un factor del clima', 'el tiempo atmosférico', 'una corriente marina']),
    ('item', '3. El clima del Paraguay es…'),
    ('opc', ['polar', 'de montaña', 'desértico', 'subtropical']),
    ('item', '4. En el Paraguay, las lluvias…'),
    ('opc', ['aumentan hacia el oeste', 'aumentan hacia el este', 'son iguales en todo el país', 'solo caen en invierno']),
    ('consigna', 'Completá los espacios:'),
    ('item', '5. El viento ________ trae aire frío y seco al Paraguay.'),
    ('item', '6. Cuanto mayor es la ________, más baja es la temperatura.'),
    ('item', '7. El clima cálido y muy lluvioso todo el año de la Amazonía se llama ________.'),
    ('consigna', 'Verdadero o falso (justificá las falsas):'),
    ('item', '8. (....) El clima se describe con datos de un solo día.'),
    ('item', '9. (....) El Chaco es más seco que la Región Oriental.'),
    ('item', '10. (....) El fenómeno de La Niña suele producir sequías en el Paraguay.'),
    ('consigna', 'Respondé y fundamentá:'),
    ('item', '11. Explicá con un ejemplo la diferencia entre un elemento y un factor del clima.', 4),
    ('item', '12. Escribí un texto de 6 a 8 líneas sobre cómo influye el clima en una actividad del Paraguay. Se tendrá en cuenta: '
             'la característica del clima (1 punto), la actividad y cómo la afecta (1 punto), otro factor que también influye '
             '(1 punto) y un texto ordenado (1 punto).', 8),
]

PLAN = {
    'material': 'La Evaluación de la Unidad 5 corregida (para la devolución); tomo: Clase 19 (Figuras 19.1, 19.2 y 19.3); termómetro o pronóstico del día',
    'tema': C.TEMAS['G3a'] + ' ' + C.TEMAS['G3b'] + ' ' + C.TEMAS['G3c'],
    'indicadores': INDICADORES,
    'proposito': 'Devolver la Evaluación de la Unidad 5 en los primeros 20 minutos y desarrollar en los 100 restantes los elementos, '
                 'factores y tipos de clima de América y del Paraguay y su influencia en las actividades humanas.',
    'funciones': {
        'Esenciales': 'En clase: Ubicate; fuente (preguntas 1 a 3); actividades 1, 2, 3, 4 y 11.',
        'Consolidación': 'Actividades 5, 6, 8 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 32).',
        'Complementarias o domiciliarias': 'Actividades 7, 10 y 12.',
    },
    'secuencia': [
        ('Inicio', [
            ('0–20', 'Devolución de la Evaluación de la Unidad 5: entrega las pruebas corregidas, explica las claves y los criterios de la Parte F y comenta los errores más frecuentes. Solo se hace si todas las pruebas, incluidas las de apoyo excepcional, ya están entregadas (ver «Atención a la diversidad»).',
             'Revisan su prueba y anotan en qué deben mejorar.', 'Devolución de la evaluación.'),
        ]),
        ('Desarrollo', [
            ('20–32', 'Pregunta con el pronóstico del día: «¿Esto es el tiempo o el clima?». Lectura de «Tiempo y clima».',
             'Distinguen tiempo y clima con ejemplos; resuelven la actividad 2.', 'Actividad 2 (esencial).'),
            ('32–50', 'Lectura de «Elementos y factores del clima» con la Figura 19.1 y el Ejemplo de Quito.',
             'Resuelven las actividades 1 y 11.', 'Actividades 1 y 11 (esenciales).'),
            ('50–64', 'Lectura de «Los tipos de clima de América» con la Figura 19.2.',
             'Resuelven el «Ubicate».', 'Ubicate (esencial).'),
            ('64–84', 'Lectura de «El clima del Paraguay» con la Figura 19.3 y el Concepto clave.',
             'Responden las preguntas 1 a 3 de la fuente y las actividades 3 y 4.', 'Fuente y actividades 3 y 4 (esenciales).'),
            ('84–100', 'Lectura de «El clima y las actividades humanas»: destaca que el clima influye junto con otros factores. Acompaña la consolidación.',
             'Resuelven las actividades 5, 6, 8 y 9.', 'Actividades de consolidación.'),
        ]),
        ('Cierre', [
            ('100–120', 'Puesta en común de la actividad 11 y de la pregunta 3 de la fuente. Lee los criterios de la actividad 12 y asigna la tarea.',
             'Corrigen con otro color.', 'Actividad 11 revisada.'),
        ]),
    ],
    'diversidad': [
        'Procedimiento para quien todavía no rindió la Evaluación U5: el apoyo excepcional se completa antes de este encuentro, en un horario acordado con la dirección. Si un estudiante estuvo ausente o no pudo completarlo, no participa de la devolución: durante esos 20 minutos lee la Clase 19 en otro lugar del aula o de la escuela, y rinde después una versión alternativa equivalente (mismos criterios y matriz, otros ítems). Nadie rinde la prueba mientras se revelan claves.',
        'Apoyo con material concreto: un termómetro y un pluviómetro casero (una botella con una regla) para mostrar cómo se miden dos elementos.',
        'Apoyo en la actividad 11: cuadro de dos columnas en la pizarra («elemento» / «factor») con un ejemplo resuelto.',
        'Desafío: registrar durante una semana la temperatura máxima y la lluvia de la localidad y comparar con lo que dice el tomo.',
    ],
    'evaluacion': {
        'tipo': 'Formativa.',
        'procedimientos': 'Lectura de esquemas y mapas; análisis de fuente cartográfica; respuesta breve.',
        'instrumentos': 'Lista de cotejo con los tres indicadores; actividad 12 con los criterios de su consigna.',
        'criterios': ['Distingue elementos y factores del clima con ejemplos.',
                      'Describe los climas de América y el clima del Paraguay.',
                      'Relaciona el clima con una actividad, junto con otro factor.'],
    },
    'precisiones': [
        'Condición A10/N03: 0 a 20, devolución de la U5; 20 a 120, G3 completo (100 minutos efectivos).',
        'Los valores de lluvia (unos 600 y unos 1.800 mm al año) son promedios aproximados de las normales 1971-2000: Grassi (2020), Estado del Clima Paraguay 2019, MADES-STP, p. 20 impresa (PDF 22), fig. 7. Un año seco puede quedar muy por debajo: no es la normal.',
        'Evitar el determinismo: el clima influye junto con los suelos, la tecnología y los mercados.',
    ],
    'tarea': 'Actividades 7, 10 y 12 de la Clase 19.',
}

SOL = {
    'bloques': [
        ('Trabajá con la fuente (cartográfica)', [
            ('F1', 'En el este de la Región Oriental: unos 1.800 mm al año.', ''),
            ('F2', 'Unos 1.200 mm: de unos 1.800 mm en el este a unos 600 mm en el noroeste del Chaco (normales 1971-2000).', 'Se acepta «mucho más al este» con los dos valores.'),
            ('F3', 'Porque el tiempo cambia de un día y de un año a otro; solo con datos de muchos años se conoce lo habitual.', ''),
        ]),
        ('Ubicate (Figura 19.2)', [
            ('U', 'Subtropical. Amazonía: ecuatorial; Patagonia: templado frío. Porque América se extiende de norte a sur y cambia la '
                  'latitud (también influyen la altitud y el mar).', ''),
        ]),
        ('Marcá la opción correcta', [
            ('1', 'a) la temperatura', ''),
            ('2', 'c) el tiempo atmosférico', ''),
            ('3', 'd) subtropical', ''),
            ('4', 'b) aumentan hacia el este', ''),
        ]),
        ('Completá los espacios', [
            ('5', 'sur', ''),
            ('6', 'altitud (altura)', ''),
            ('7', 'ecuatorial', ''),
        ]),
        ('Verdadero o falso', [
            ('8', 'Falso: se describe con datos de muchos años; un día es el tiempo atmosférico.', 'Justificación obligatoria.'),
            ('9', 'Verdadero.', ''),
            ('10', 'Verdadero.', ''),
        ]),
        ('Respondé y fundamentá', [
            ('11', 'Un elemento es lo que se mide, como la temperatura; un factor es lo que la modifica, como la altitud: en Quito, a '
                   'gran altura, la temperatura es templada aunque esté sobre el Ecuador.', 'Un ejemplo de cada uno relacionado.'),
            ('12', 'Ejemplo: «En la Región Oriental el clima es cálido y llueve bastante, lo que permite cosechar soja en verano y trigo '
                   'en invierno. Cuando hay sequía, la cosecha baja. Pero también influyen los suelos fértiles, las máquinas y los '
                   'precios en los mercados.»',
             'Criterio anunciado en la consigna: la característica del clima (1 punto), la actividad y cómo la afecta (1 punto), '
             'otro factor que también influye (1 punto) y un texto ordenado (1 punto).'),
        ]),
    ],
}

VERIFICACION = [
    ('Lluvias anuales: unos 1.800 mm en el este y unos 600 mm en el noroeste del Chaco', 'Normales 1971-2000, aprox. 600-1.800 mm: Grassi (2020), Estado del Clima Paraguay 2019, MADES-STP, p. 20 (PDF p. 22), figura 7.'),
    ('Temperaturas del Chaco superiores a 40 °C; heladas ocasionales', 'Datos habituales; cotejar con la DMH.'),
    ('Quito a unos 2.800 m', 'Dato habitual; cotejar.'),
    ('El Niño (lluvias e inundaciones) y La Niña (sequías) en el Paraguay', 'Relación habitual en la bibliografía; cotejar.'),
    ('Mapas de las Figuras 19.2 y 19.3', 'Esquemas de la editorial, no mapas climáticos medidos.'),
]
