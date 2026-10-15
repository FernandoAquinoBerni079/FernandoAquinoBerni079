"""Encuentro 30 — Evaluación de la Unidad 5 (asociación curricular: G1 y G2).

Base: Evaluación U5 de la muestra 3 (commit 841f5bc9). Cambios: ítem 7
reemplazado (el tomo no enseña que Bolivia sea mediterránea); mapas propios
de la prueba con clave gráfica; autoevaluación al terminar; matriz
ítem-capacidad-puntaje; apoyo excepcional antes del encuentro 31 (A10).
"""

TITULO = 'Evaluación de la Unidad 5 — Posición, relieve e hidrografía'
CLAVE = 'EVALUACIÓN DE LA UNIDAD 5'

TOMO = [('banda', 'EVALUACIÓN DE LA UNIDAD 5', 'El espacio geográfico: posición, relieve e hidrografía'),
 ('datos',),
 ('p',
  'Tiempo: 70 minutos. Puntaje total: 28 puntos. Todo lo que necesitás está en esta prueba, incluido el mapa de la Parte C.'),
 ('consigna', 'Parte A — Marcá la opción correcta (1 punto cada una).'),
 ('item', '1. El Paraguay limita con…'),
 ('opc',
  ['Bolivia, el Brasil y la Argentina',
   'Bolivia, Chile y la Argentina',
   'el Brasil, el Uruguay y la Argentina',
   'el Perú, Bolivia y el Brasil']),
 ('item', '2. «En el centro de América del Sur» es un ejemplo de posición…'),
 ('opc', ['absoluta', 'relativa', 'climática', 'política']),
 ('item', '3. La parte de la geografía que estudia las formas del relieve es la…'),
 ('opc', ['hidrografía', 'climatología', 'orografía', 'demografía']),
 ('item', '4. Las mayores alturas del Paraguay se encuentran en…'),
 ('opc', ['el Chaco central', 'el Bajo Chaco', 'la desembocadura del Pilcomayo', 'la Región Oriental']),
 ('item', '5. El río que nace en los Andes de Bolivia y es límite con la Argentina en el Chaco es el…'),
 ('opc', ['Paraná', 'Pilcomayo', 'Apa', 'Tebicuary']),
 ('item', '6. Una evaluación de impacto ambiental se hace…'),
 ('opc',
  ['antes de una obra, para prever y reducir sus efectos',
   'solo después de un accidente',
   'para calcular el precio del flete',
   'para fijar los límites del país']),
 ('consigna',
  'Parte B — Verdadero o falso. Justificá las falsas (1 punto cada una: si es verdadera, 1 punto por marcarla bien; si es falsa, '
  '0,5 por marcarla y 0,5 por la justificación).'),
 ('item', '7. (....) El trópico de Capricornio atraviesa el Paraguay.'),
 ('item', '8. (....) La posición absoluta del Paraguay se expresa solo con su latitud.'),
 ('item', '9. (....) En parte de su recorrido, el río Paraguay es límite con el Brasil.'),
 ('item', '10. (....) El relieve llano explica por sí solo toda la producción agrícola del Paraguay.'),
 ('consigna', 'Parte C — Mapa (6 puntos: 1 por cada elemento bien ubicado y nombrado, y 1 por los tres países).'),
 ('item',
  '11. En este mapa mudo, marcá y nombrá el río Paraguay, el río Paraná, el río Pilcomayo, Asunción y la represa de Itaipú. '
  'Escribí los nombres de los tres países limítrofes en el lugar correcto.'),
 ('fig',
  'eval_u5_mapa_mudo.png',
  'Mapa mudo para la Parte C. Elaboración propia con datos de Natural Earth (dominio público).',
  12.0),
 ('consigna', 'Parte D — Fuente cartográfica (3 puntos: 1 por fila; 0,5 por el nombre del río y 0,5 por la vertiente).'),
 ('fig',
  'eval_u5_rios_numerados.png',
  'Mapa para la Parte D. Elaboración propia con datos de Natural Earth (dominio público).',
  9.5),
 ('item', '12. Escribí el nombre de los ríos 1, 2 y 3 del mapa y la vertiente (océano) hacia la que corre cada uno.'),
 ('cuadro', ['N.º', 'Nombre del río', 'Vertiente'], ['1', '2', '3'], [1.2, 4.4, 4.4]),
 ('consigna', 'Parte E — La Hidrovía (4 puntos: 1 por cada casilla con un ejemplo correcto).'),
 ('item', '13. Completá la matriz con un ejemplo en cada casilla.'),
 ('cuadro',
  ['Beneficio económico', 'Impacto social', 'Impacto ecológico', 'Medida para reducir un impacto'],
  [''],
  [2.5, 2.5, 2.5, 2.5]),
 ('consigna', 'Parte F — Desarrollo (5 puntos).'),
 ('item',
  '14. Explicá cómo influyen la posición (ser un país mediterráneo), el relieve y los ríos en las actividades económicas del '
  'Paraguay. Escribí entre 8 y 10 líneas. Se tendrá en cuenta (1 punto cada uno): la posición, el relieve junto con otro factor, '
  'los ríos, un dato concreto de cada clase de la unidad y un texto ordenado.',
  10),
 ('h3', 'Al terminar la prueba: autoevaluación de la unidad'),
 ('p', 'Completala cuando termines la prueba, antes de entregarla. No lleva nota: sirve para saber qué repasar.'),
 ('tabla',
  ['Puedo…', 'Sí', 'Con ayuda', 'Todavía no'],
  [['Describir la posición absoluta y relativa del Paraguay.', '', '', ''],
   ['Describir el relieve del Paraguay y de América.', '', '', ''],
   ['Ubicar los grandes ríos del Paraguay y de América.', '', '', ''],
   ['Analizar beneficios e impactos de la Hidrovía.', '', '', '']],
  [5.5, 1.5, 1.5, 1.5]),
 ('p', 'La parte de la prueba que me resultó más difícil fue… y la voy a repasar así:'),
 ('renglones', 3)]

PLAN = {'material': 'Tomo: Evaluación de la Unidad 5 (incluye el mapa mudo de la Parte C y el mapa de la Parte D)',
 'tema': 'Evaluación de las Clases 16, 17 y 18 y de la Continuación F.',
 'indicadores': ['Ubica el Paraguay, sus países limítrofes y sus principales ríos.',
                 'Diferencia la posición absoluta de la relativa.',
                 'Identifica grandes ríos de América y su vertiente.',
                 'Analiza beneficios e impactos de la Hidrovía.',
                 'Explica la influencia de la posición, el relieve y los ríos en las actividades económicas.'],
 'proposito': 'Comprobar los logros de la unidad con una prueba de 70 minutos, en condiciones iguales para todos, y devolver la '
              'corrección comentada en el encuentro siguiente.',
 'funciones': {'Material que recibe cada estudiante': 'La prueba del tomo (fotocopiada o en el cuadernillo), que ya incluye los '
                                                      'dos mapas. No se usa ninguna otra ficha.',
               'Criterios de puntaje': 'Figuran en cada parte de la prueba: A 6, B 4, C 6, D 3, E 4 y F 5 (total 28).',
               'Devolución': 'Con claves y criterios, en los primeros 20 minutos del encuentro 31, cuando todas las pruebas '
                             'están entregadas.'},
 'secuencia': [('Inicio',
                [('0–10',
                  'Explica la estructura (Partes A a F), el puntaje de cada parte y el tiempo. Lee en voz alta los criterios de '
                  'la Parte F.',
                  'Leen toda la prueba y preguntan dudas de consigna.',
                  '—')]),
               ('Desarrollo',
                [('10–80',
                  'Supervisa la resolución individual; solo aclara consignas.',
                  'Resuelven las Partes A a F.',
                  'Prueba.'),
                 ('80–95',
                  'Tiempo adicional supervisado para quienes lo necesitan (hasta 15 minutos). Los demás completan la '
                  'autoevaluación, entregan y pasan a la actividad sin claves.',
                  'Quienes tienen tiempo adicional siguen la prueba; el resto trabaja en la actividad sin claves.',
                  'Entrega de todas las pruebas.')]),
               ('Cierre',
                [('95–120',
                  'Con todas las pruebas entregadas, propone una actividad sin claves: cada estudiante escribe qué parte le '
                  'resultó más difícil y qué clase va a repasar. No se corrige ni se comentan respuestas.',
                  'Completan la reflexión y la entregan.',
                  'Reflexión escrita (no lleva nota).')])],
 'diversidad': ['Tiempo adicional de hasta 15 minutos (80 a 95), supervisado y sin corrección simultánea: nadie recibe '
                'respuestas antes de que terminen todos.',
                'Lectura en voz alta de las consignas para quien lo necesite, sin explicar contenidos.',
                'Si un estudiante necesita más de 15 minutos adicionales, completa la prueba antes del encuentro 31 en un '
                'horario de apoyo acordado con la dirección, bajo supervisión y con la prueba custodiada por el docente. No la '
                'completa al comienzo del encuentro 31: allí se hace la devolución con claves (condición A10).'],
 'evaluacion': {'tipo': 'Sumativa de unidad; devolución formativa en el encuentro 31.',
                'procedimientos': 'Prueba escrita; ubicación en mapa; lectura de mapa; matriz; respuesta desarrollada.',
                'instrumentos': 'Prueba de la Unidad 5 del tomo; claves, criterios, clave gráfica y matriz '
                                'ítem-capacidad-puntaje del solucionario.',
                'criterios': ['Total: 28 puntos (A 6; B 4; C 6; D 3; E 4; F 5). La calificación se obtiene con la escala de la '
                              'institución.',
                              'La Parte F se corrige con los cinco criterios impresos en la consigna (1 punto cada uno).']},
 'precisiones': ['La prueba evalúa las Clases 16, 17 y 18 y la Continuación F tal como están en el tomo de producción; el ítem 7 '
                 'se reemplazó porque el tomo no trata la condición mediterránea de Bolivia.',
                 'Primeros 20 minutos del encuentro 31: devolución con claves y criterios, cuando todas las pruebas, incluidas '
                 'las de apoyo excepcional, ya están entregadas. El Plan 31 reserva ese tiempo.'],
 'tarea': 'Repasar la clase que cada estudiante anotó en su reflexión.'}

SOL = {'puntaje': 28,
 'bloques': [('Parte A — 1 punto cada una',
              [('1', 'a) Bolivia, el Brasil y la Argentina', ''),
               ('2', 'b) relativa', ''),
               ('3', 'c) orografía', ''),
               ('4', 'd) la Región Oriental', ''),
               ('5', 'b) Pilcomayo', ''),
               ('6', 'a) antes de una obra, para prever y reducir sus efectos', '')]),
             ('Parte B — 1 punto cada una',
              [('7',
                'Verdadero.',
                'Criterio anunciado en la Parte B: si es verdadera, 1 punto por marcarla bien; si es falsa, 0,5 por marcarla y '
                '0,5 por la justificación.'),
               ('8', 'Falso: se expresa con la latitud y la longitud.', ''),
               ('9', 'Verdadero.', ''),
               ('10', 'Falso: también influyen el suelo, el clima, la tecnología y los mercados.', '')]),
             ('Parte C — 6 puntos',
              [('11',
                'Río Paraguay, río Paraná, río Pilcomayo, Asunción e Itaipú bien ubicados (1 punto cada uno); los tres países '
                'limítrofes en su lugar (1 punto en total).',
                'Criterio anunciado en la Parte C: 1 por cada elemento bien ubicado y nombrado, y 1 por los tres países. Se '
                'corrige sobre el mapa mudo impreso en la prueba. Parcial: 0,5 si el elemento está bien ubicado pero sin nombre '
                'o mal nombrado; países, 0,5 si ubica dos de los tres. Tolerancias como en el «Ubicate» de la Clase 18.')]),
             ('Parte D — 3 puntos',
              [('12',
                '1: Amazonas, vertiente del Atlántico. 2: Mississippi, vertiente del Atlántico (golfo de México). 3: Paraná, '
                'vertiente del Atlántico (por el Río de la Plata).',
                'Criterio anunciado en la Parte D: 1 por fila; 0,5 por el nombre del río y 0,5 por la vertiente. La vertiente '
                'correcta suma 0,5 aunque el nombre falte.')]),
             ('Parte E — 4 puntos',
              [('13',
                'Ejemplo: económico, exportar a menor costo; social, empleo en los puertos o afectación de la pesca; ecológico, '
                'cambios en los humedales o en la calidad del agua; medida, evaluación de impacto ambiental y control del agua.',
                'Criterio anunciado en la Parte E: 1 por cada casilla con un ejemplo correcto.')]),
             ('Parte F — 5 puntos',
              [('14',
                'Ejemplo completo: «El Paraguay es un país mediterráneo: para exportar depende de los ríos y de puertos de otros '
                'países, por eso la Hidrovía es tan importante (Clase 16). En la Región Oriental el relieve es bajo y ondulado, '
                'y junto con suelos fértiles y lluvias suficientes permite la agricultura mecanizada; en el Chaco, la llanura y '
                'el clima más seco favorecen la ganadería (Clase 17). Los ríos dan transporte, agua y energía: Itaipú y Yacyretá '
                'producen electricidad (Clase 18). Por eso posición, relieve y ríos influyen juntos en la economía.» Puntaje '
                'parcial: cada criterio vale 1 o 0; el del relieve exige nombrar al menos otro factor (suelo, clima, tecnología '
                'o mercados), como dice la consigna.',
                'Criterio anunciado en la consigna (1 punto cada uno): la posición, el relieve junto con otro factor, los ríos, '
                'un dato concreto de cada clase de la unidad y un texto ordenado.')])],
 'mapas': [('eval_u5_mapa_clave.png',
            12.0,
            'Clave gráfica de la Parte C (Figura 18.1 del tomo). Los tramos limítrofes del río Paraguay son: con el Brasil, '
            'desde Bahía Negra hasta la desembocadura del Apa (triángulo); con la Argentina, desde la desembocadura del '
            'Pilcomayo, frente a Asunción, hasta la confluencia con el Paraná. Tolerancia: 1 cm en el mapa impreso.')],
 'matriz': [('1, 2, 7 y 8', 'G1', 'Límites, posición relativa y absoluta, trópico de Capricornio.', 4),
            ('3, 4 y 10', 'G2', 'Orografía y relieve del Paraguay; relieve y otros factores.', 3),
            ('5, 6 y 9', 'G2', 'Ríos del Paraguay; evaluación de impacto ambiental.', 3),
            ('11', 'G1, G2', 'Ubicación de ríos, Asunción, Itaipú y países limítrofes.', 6),
            ('12', 'G2', 'Grandes ríos de América y sus vertientes.', 3),
            ('13', 'G2', 'Beneficios e impactos de la Hidrovía.', 4),
            ('14', 'G1, G2', 'Posición, relieve y ríos en las actividades económicas.', 5)]}

VERIFICACION = []
