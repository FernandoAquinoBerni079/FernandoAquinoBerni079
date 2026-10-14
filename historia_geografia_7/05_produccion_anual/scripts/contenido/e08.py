"""Encuentro 8 — Continuación B: mapa y línea de tiempo (H2; temas H2a y H2b).

Corrige el problema del maestro (la consigna pedía una línea de tiempo sin
dar las fechas): el tomo trae el cuadro de datos y las fichas reproducibles
con el mapa mudo y el eje en blanco.
"""
import curriculo as C

TITULO = 'Continuación B — Poblamiento y civilizaciones americanas: mapa y línea de tiempo'
CLAVE = 'Continuación B —'
INDICADORES = [
    'Representa en un mapa histórico las rutas de poblamiento y las áreas de las tres civilizaciones, con leyenda.',
    'Construye una línea de tiempo a escala y explica por qué las civilizaciones no fueron simultáneas.',
    'Compara dos civilizaciones con datos de lugar, tiempo, organización y aportes.',
]

TOMO = [
    ('h1', TITULO),
    ('ficha', C.CAPACIDADES['H2'], C.TEMAS['H2a'] + ' ' + C.TEMAS['H2b'], INDICADORES),
    ('h2', 'Del dato al mapa y a la línea de tiempo'),
    ('p', 'En las Clases 4 y 5 estudiaste cómo se pobló América y cómo eran las civilizaciones maya, mexica e inca. En este '
          'encuentro vas a organizar esa información en dos herramientas: un mapa histórico y una línea de tiempo. Las dos '
          'responden preguntas distintas: el mapa, ¿dónde?; la línea, ¿cuándo?'),
    ('tabla', ['Pasos para un mapa histórico', 'Pasos para una línea de tiempo'],
     [['1. Poné un título que diga qué y cuándo.', '1. Elegí la fecha de inicio y la de fin.'],
      ['2. Ubicá los lugares con ayuda de un mapa del tomo.', '2. Elegí una escala: por ejemplo, 1 cm = 100 años.'],
      ['3. Usá colores o tramas distintos para cada área.', '3. Dibujá los períodos como barras y los hechos como marcas.'],
      ['4. Explicá cada color y símbolo en la leyenda.', '4. Escribí en cada barra qué es y sus fechas.'],
      ['5. Escribí la fuente de la que tomaste los datos.', '5. Revisá que las distancias respeten la escala.']],
     [5.0, 5.0]),
    ('h2', 'Los datos que vas a usar'),
    ('tabla', ['Tema', 'Dónde', 'Cuándo (aproximado)'],
     [['Paso por Beringia', 'Entre Siberia y Alaska', 'Durante la última glaciación, hace más de 15.000 años'],
      ['Monte Verde', 'Sur de Chile', 'Hace unos 14.500 años'],
      ['Mayas: período clásico', 'Sur de México, Guatemala, Belice (ciudad de Tikal)', '250 a 900 d. C.'],
      ['Mayas: período posclásico', 'Norte de Yucatán (Chichén Itzá)', '900 a 1540 d. C.'],
      ['Mexicas', 'Centro de México (Tenochtitlan)', '1325 a 1521 d. C.'],
      ['Incas: imperio', 'Andes, del sur de Colombia al centro de Chile (Cuzco)', '1438 a 1533 d. C.'],
      ['Llegada de Colón', 'Islas del Caribe', '1492 d. C.']],
     [3.0, 4.0, 3.0]),
    ('caja', 'concepto', 'Concepto clave — ',
     'La escala de una línea de tiempo es la relación entre la distancia dibujada y los años. Si los hechos están muy separados, '
     'como el poblamiento (hace miles de años) y las civilizaciones (hace siglos), no entran en la misma escala: se usan dos '
     'líneas o un corte marcado en el eje.'),

    ('h2', 'Consignas del taller'),
    ('p', 'Trabajá en parejas. Usá las fichas reproducibles B-1 y B-2 y las Figuras 4.1, 5.1 y 5.2 de las clases anteriores como guía.'),
    ('consigna', 'Consignas del taller:'),
    ('item', '1. En el mapa mudo de la Ficha B-1: marcá Beringia y Monte Verde y dibujá con flechas una ruta de poblamiento; '
             'pintá con tres colores las áreas aproximadas de mayas, mexicas e incas; escribí Tikal, Tenochtitlan y Cuzco; '
             'completá la leyenda y el título.'),
    ('item', '2. En la línea de tiempo de la Ficha B-2, dibujá una barra para el período clásico maya, otra para los mexicas y '
             'otra para el imperio inca, con los datos del cuadro. Marcá el año 1492.'),
    ('item', '3. ¿Por qué Monte Verde no entra en la línea de la Ficha B-2? Calculá, aproximadamente, cuántos siglos pasaron entre '
             'Monte Verde y la fundación de Tenochtitlan.', 4),
    ('item', '4. Escribí un texto de 6 a 8 líneas que compare dos de las tres civilizaciones. Se tendrá en cuenta: dos '
             'diferencias o semejanzas con datos (2 puntos), la ubicación correcta en el tiempo (1 punto) y la redacción clara '
             '(1 punto).', 8),
    ('h3', 'Autoevaluación del taller'),
    ('tabla', ['Criterio', 'Lo logré', 'En proceso', 'Todavía no'],
     [['Mi mapa tiene título, colores y leyenda.', '', '', ''],
      ['Respeté la escala en la línea de tiempo.', '', '', ''],
      ['Expliqué por qué las civilizaciones no fueron simultáneas.', '', '', ''],
      ['Usé datos para comparar dos civilizaciones.', '', '', '']],
     [5.5, 1.5, 1.5, 1.5]),
]

FICHAS = [
    ('ficha_repro', 'Ficha reproducible B-1 — Mapa mudo de América',
     [('p', 'Título del mapa: ______________________________________________'),
      ('fig', 'ficha_B_mapa_mudo_america.png', 'Mapa mudo para la consigna 1. Elaboración propia con datos de Natural Earth (dominio público); mapa aproximado.', 15.0),
      ('cuadro', ['Leyenda: color o símbolo', 'Qué representa'], ['', '', '', ''], [3.0, 7.0], 0.9)]),
    ('ficha_repro', 'Ficha reproducible B-2 — Línea de tiempo de las civilizaciones',
     [('fig', 'ficha_B_linea_vacia.png', 'Eje para la consigna 2 (1 división = 100 años).', 16.0),
      ('p', 'Cuando termines, escribí debajo qué civilización duró más y cuál fue la más reciente:'),
      ('renglones', 4)]),
]

PLAN = {
    'material': 'Tomo: Continuación B; Fichas reproducibles B-1 y B-2 (una por pareja, preparadas antes del encuentro); lápices de colores y regla',
    'tema': C.TEMAS['H2a'] + ' ' + C.TEMAS['H2b'],
    'indicadores': INDICADORES,
    'proposito': 'Que los estudiantes organicen en un mapa y en una línea de tiempo lo estudiado sobre el poblamiento y las '
                 'civilizaciones, y comparen con datos.',
    'funciones': {
        'Esenciales': 'En clase: consignas 1, 2 y 4 del taller; Fichas B-1 y B-2.',
        'Consolidación': 'En clase: consigna 3 y autoevaluación del taller.',
        'Complementarias o domiciliarias': 'Pasar en limpio el texto comparativo si quedó en borrador (optativo).',
    },
    'secuencia': [
        ('Inicio', [
            ('0–10', 'Revisa la consolidación de la Clase 5. Pregunta: «¿Mayas, mexicas e incas vivieron al mismo tiempo?».',
             'Responden y justifican.', 'Respuestas orales.'),
        ]),
        ('Desarrollo', [
            ('10–20', 'Explica los pasos del mapa y de la línea de tiempo con el cuadro y el Concepto clave de escala.',
             'Leen el cuadro de datos y subrayan lugares y fechas.', 'Datos subrayados.'),
            ('20–50', 'Entrega la Ficha B-1 y modela cómo elegir colores y armar la leyenda.',
             'Resuelven la consigna 1 en parejas.', 'Ficha B-1 (esencial).'),
            ('50–75', 'Entrega la Ficha B-2 y muestra en la pizarra cómo dibujar la barra del clásico maya (250-900).',
             'Resuelven la consigna 2 y la consigna 3.', 'Ficha B-2; consignas 2 y 3.'),
            ('75–98', 'Lee los criterios de la consigna 4 y acompaña la escritura.',
             'Escriben el texto comparativo (consigna 4).', 'Consigna 4 (esencial).'),
        ]),
        ('Cierre', [
            ('98–112', 'Exposición de dos mapas y dos líneas de tiempo; el grupo comprueba escala y leyenda.',
             'Comparan y corrigen.', 'Mapas y líneas revisados.'),
            ('112–120', 'Explica la autoevaluación y recuerda que el próximo encuentro es la Evaluación de la Unidad 2.',
             'Completan la autoevaluación.', 'Autoevaluación.'),
        ]),
    ],
    'diversidad': [
        'Apoyo en el mapa: el docente marca previamente con un punto Tikal, Tenochtitlan y Cuzco en algunas copias de la Ficha B-1.',
        'Apoyo en la línea de tiempo: la barra del clásico maya dibujada como modelo en la pizarra.',
        'Desafío: agregar a la línea la caída de Tenochtitlan (1521) y de los incas (1532-1533) y calcular cuántos años después de 1492 ocurrieron.',
    ],
    'evaluacion': {
        'tipo': 'Formativa, con producto.',
        'procedimientos': 'Mapa histórico; línea de tiempo a escala; texto comparativo.',
        'instrumentos': 'Fichas B-1 y B-2; autoevaluación; consigna 4 con los criterios de su consigna.',
        'criterios': ['El mapa tiene título, áreas diferenciadas, lugares y leyenda.',
                      'La línea de tiempo respeta la escala y las fechas.',
                      'El texto compara con datos y ubica correctamente en el tiempo.'],
    },
    'precisiones': [
        'Las áreas que pintan los estudiantes son aproximadas, como las de la Figura 5.1; no se evalúa precisión de límites.',
        'Las fechas del poblamiento no entran en la misma escala que las civilizaciones: es justamente lo que se trabaja en la consigna 3.',
    ],
    'tarea': 'Repasar las Clases 4 y 5 y la Continuación B para la Evaluación de la Unidad 2.',
}

SOL = {
    'bloques': [
        ('Consignas del taller', [
            ('1', 'Beringia entre Siberia y Alaska; Monte Verde en el sur de Chile; flecha de norte a sur por la costa del Pacífico o '
                  'por el interior. Áreas: mayas en Yucatán, Guatemala y Belice; mexicas en el centro y sur de México; incas a lo '
                  'largo de los Andes. Tikal, Tenochtitlan y Cuzco ubicadas; leyenda con tres colores y símbolos.',
             'Lista de cotejo: título; cinco lugares; tres áreas diferenciadas; leyenda completa. Se compara con la Figura 5.1.'),
            ('2', 'Barras: clásico maya de 250 a 900; mexicas de 1325 a 1521; incas de 1438 a 1533. Marca en 1492.',
             'Cada barra con sus fechas y respetando la escala (1 división = 100 años).'),
            ('3', 'Porque ocurrió hace unos 14.500 años, es decir, hacia el 12.500 a. C., y la línea empieza en el año 0. Entre Monte '
                  'Verde y 1325 pasaron unos 13.800 años: alrededor de 138 siglos.', 'Se aceptan entre 130 y 140 siglos si explica el cálculo.'),
            ('4', 'Ejemplo: «Los mayas vivieron en el sur de México y en Guatemala, y su período clásico fue entre el 250 y el 900. '
                  'Los incas vivieron en los Andes y formaron su imperio desde 1438. Los mayas tenían ciudades-estado independientes; '
                  'los incas, un imperio con un solo soberano. Los dos fueron grandes constructores, pero los mayas escribían y los '
                  'incas usaban quipus.»',
             'Criterio anunciado en la consigna: dos diferencias o semejanzas con datos (2 puntos), la ubicación correcta en el tiempo (1 punto) y la redacción clara (1 punto).'),
        ]),
    ],
}

VERIFICACION = []
