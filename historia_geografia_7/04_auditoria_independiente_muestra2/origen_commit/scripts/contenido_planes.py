"""Planes de clase de la segunda muestra (15, 28, 29 y 30).

Cada plan corresponde a una sección del tomo de la muestra: la capacidad es
la literal del programa MEC 2014, y las figuras, fichas y números de
actividad son los del tomo. Todas las actividades del tomo se asignan (en
clase o como tarea). Las precisiones para el docente amplían; no corrigen
errores del libro, porque esos errores ya se corrigieron en el tomo.
"""
from contenido_tomo import CAP_G2, CAP_H3

COMUNES = {'disciplina': 'Historia y Geografía', 'duracion': '3 HC (120 minutos)'}

PLANES = [
    {
        'n': 15, 'encuentro': 15,
        'titulo': 'Clase 10 — La Real Provisión de 1537 y las instituciones coloniales',
        'unidad': 'Unidad 3 — El Paraguay y América en el siglo XVI',
        'material': 'Tomo: Clase 10 (Figuras 10.1, 10.2 y 10.3)',
        'capacidad': CAP_H3,
        'tema': 'Ejercicio del derecho a la autonomía (Real Provisión del 12 de septiembre de 1537). Instituciones coloniales: Cabildo (tipos e importancia). Obispado. Encomienda (tipos y características).',
        'indicadores': [
            'Explica en qué situación la Real Provisión de 1537 autorizaba elegir un gobernador y quiénes podían hacerlo.',
            'Diferencia la elección colonial de 1537 de una elección democrática actual.',
            'Reconoce las funciones del gobernador, el Cabildo y el Obispado, y los tipos de encomienda.',
        ],
        'proposito': 'Que los estudiantes lean un documento de época con sus condiciones, entiendan qué autonomía tenían los vecinos de Asunción y cuáles eran sus límites, y distingan las instituciones de gobierno de la encomienda.',
        'secuencia': [
            ('Inicio', [
                ('0–15', 'Plantea un problema: «Si la dirección de la escuela queda vacía y no llega nadie de afuera, ¿quién decide? ¿El grupo puede elegir a alguien? ¿Con qué límites?». Anota las ideas y las vincula con la fundación de Asunción (Clase 8).',
                 'Proponen respuestas y discuten los límites de esa elección.', 'Ideas en la pizarra.'),
            ]),
            ('Desarrollo', [
                ('15–30', 'Lectura guiada de «Una provincia lejana y sin gobernador». Muestra en un mapa de América del Sur la distancia entre Buenos Aires, Asunción y España.',
                 'En parejas escriben en dos líneas cuál era el problema de la provincia en 1537.', 'Problema escrito.'),
                ('30–50', 'Lectura de «Qué decía la Real Provisión». Lee en voz alta los dos fragmentos de «Trabajá con la fuente», explica el vocabulario y destaca las tres condiciones.',
                 'Responden individualmente las preguntas 1 a 3 de la fuente en los renglones del recuadro.', 'Respuestas de la fuente.'),
                ('50–60', 'Presenta «Cómo se usó: Irala y Cabeza de Vaca» con la Figura 10.3.',
                 'Resuelven la consigna «Ubicate» y la actividad 7 (ordenar hechos).', 'Ubicate; actividad 7.'),
                ('60–75', 'Organiza grupos de 4 para analizar el cuadro «Elegir en 1537 y elegir hoy» y lee el Concepto clave sobre autonomía.',
                 'Cada grupo agrega una fila al cuadro («¿Qué pasaba si alguien no estaba de acuerdo?» u otra pregunta) y la comparte.', 'Fila agregada por grupo.'),
                ('75–95', 'Explica las autoridades con la Figura 10.2. Propone leer críticamente la Figura 10.1: ¿qué institución no gobernaba? Desarrolla el Cabildo (tipos), el Obispado y la encomienda (tipos).',
                 'Resuelven las actividades 4, 5, 8, 9 y 10.', 'Actividades 4, 5, 8, 9 y 10.'),
                ('95–105', 'Acompaña la resolución individual.',
                 'Resuelven las actividades 1, 2, 3, 6 y 11 a 14.', 'Actividades 1 a 6 y 11 a 14.'),
            ]),
            ('Cierre', [
                ('105–115', 'Corrección oral con la clave del solucionario; pide la justificación de cada falso.',
                 'Corrigen con otro color.', 'Actividades corregidas.'),
                ('115–120', 'Puesta en común breve de la actividad 15 y asignación de la tarea.',
                 'Responden oralmente y anotan la tarea.', 'Actividad 15; tarea.'),
            ]),
        ],
        'diversidad': [
            'Glosario en la pizarra: capitulación, lugarteniente, veedor, adelantado, cabildo, encomienda, mita, yanacona.',
            'Para quienes leen con dificultad: lectura en voz alta de los fragmentos y preguntas guía con opciones.',
            'Desafío: comparar la elección de 1539 con la deposición de Cabeza de Vaca en 1544 y explicar si las dos se apoyaban en la Real Provisión.',
        ],
        'evaluacion': {
            'tipo': 'Formativa.',
            'procedimientos': 'Análisis de fuente; cuadro comparativo; ordenamiento cronológico.',
            'instrumentos': 'Lista de cotejo; actividades corregidas; párrafo de la actividad 16 (tarea).',
            'criterios': [
                'Nombra las tres condiciones de la Real Provisión: falta de autoridad, electores españoles y gobierno en nombre del rey.',
                'Señala al menos dos diferencias entre la elección de 1537 y una elección actual.',
                'Distingue las instituciones de gobierno (gobernador, Cabildo) de la encomienda y explica sus dos tipos.',
            ],
        },
        'precisiones': [
            'El programa del MEC usa la expresión «Ejercicio del derecho a la autonomía»; el tomo la mantiene y la explica en el Concepto clave. Conviene evitar presentarla como democracia o independencia.',
            'Los dos fragmentos de la Real Provisión vienen de transcripciones distintas y se citan con su ortografía («mas» sin tilde). Es una buena oportunidad para explicar que los documentos antiguos tienen otra ortografía.',
            'La Figura 10.1 es una ilustración de síntesis; su título dice «instituciones que gobernaban», pero la encomienda no gobernaba. El tomo lo aclara en el epígrafe y propone compararla con la Figura 10.2.',
        ],
        'tarea': 'Actividad 16 de la Clase 10 (párrafo de 6 a 8 líneas).',
    },
    {
        'n': 28, 'encuentro': 28,
        'titulo': 'Clase 18 — La hidrografía y la Hidrovía',
        'unidad': 'Unidad 5 — El espacio geográfico: posición, relieve e hidrografía',
        'material': 'Tomo: Clase 18 (Figuras 18.1, 18.2 y 18.3) y Ficha reproducible 18-A',
        'capacidad': CAP_G2,
        'tema': 'Hidrografía de Paraguay y América. Importancia y utilidad de los cauces hídricos. Hidrovía Paraná-Paraguay. Impacto ecológico, social y económico. Potencialidad de los recursos naturales y necesidad de su preservación.',
        'indicadores': [
            'Reconoce los principales ríos, lagos, esteros y acuíferos del Paraguay y su ubicación.',
            'Identifica las grandes cuencas y vertientes de América.',
            'Explica la importancia de los ríos y de la Hidrovía, y la necesidad de preservar el agua.',
        ],
        'proposito': 'Que los estudiantes ubiquen la red hidrográfica del Paraguay dentro de la Cuenca del Plata, la comparen con la de América y relacionen el agua con la energía, el transporte y su cuidado.',
        'secuencia': [
            ('Inicio', [
                ('0–10', 'Pregunta: «¿De dónde viene el agua que sale de la canilla en tu casa?». Anota respuestas (río, pozo, acuífero) y anticipa que el agua también está bajo tierra.',
                 'Responden según su experiencia.', 'Ideas en la pizarra.'),
            ]),
            ('Desarrollo', [
                ('10–25', 'Explica río, afluente, margen, cuenca y vertiente con el Concepto clave y el Ejemplo del Tebicuary; dibuja en la pizarra el camino del agua hasta el Río de la Plata.',
                 'Resuelven las actividades 1, 7, 8 y 9.', 'Actividades 1, 7, 8 y 9.'),
                ('25–45', 'Lectura de «Los grandes ríos del Paraguay» con la Figura 18.2 y el cuadro de los tres ríos. Entrega la Ficha 18-A.',
                 'En parejas resuelven la consigna «Ubicate» en la Ficha 18-A y las actividades 2, 3, 10 y 11.', 'Ficha 18-A completa; actividades 2, 3, 10 y 11.'),
                ('45–60', 'Lectura de «Lagos, esteros, humedales y agua subterránea». Relaciona el Acuífero Patiño con el inicio de la clase.',
                 'Resuelven la actividad 5 y anotan qué humedal o lago conocen o tienen cerca.', 'Actividad 5.'),
                ('60–75', 'Lectura de «Ríos que dan vida y energía» y de «La Hidrovía Paraguay-Paraná» con la Figura 18.1 y la caja Ejemplo.',
                 'Explican oralmente por qué ninguna obra es solo beneficio (Saltos del Guairá).', 'Intercambio oral.'),
                ('75–90', 'Presenta «Los grandes ríos y lagos de América» con la Figura 18.3 y la fuente cartográfica.',
                 'Responden por escrito las preguntas 1 a 3 de la fuente y las actividades 4, 6 y 13.', 'Respuestas de la fuente; actividades 4, 6 y 13.'),
                ('90–100', 'Lectura de «Cuidar el agua» y del Concepto clave sobre recursos renovables.',
                 'Resuelven la actividad 12.', 'Actividad 12.'),
            ]),
            ('Cierre', [
                ('100–112', 'Corrección de las actividades 1 a 13 con la clave del solucionario.',
                 'Corrigen en parejas con otro color.', 'Actividades corregidas.'),
                ('112–120', 'Puesta en común de la actividad 14 y asignación de la tarea; anticipa la Continuación F.',
                 'Comparten tres usos del agua con ejemplos.', 'Actividad 14 (oral).'),
            ]),
        ],
        'diversidad': [
            'Ficha 18-A con los nombres de los ríos escritos al pie para quienes necesitan apoyo en la ubicación.',
            'Desafío: averiguar qué río, lago o acuífero abastece de agua a su localidad y qué institución la distribuye.',
        ],
        'evaluacion': {
            'tipo': 'Formativa.',
            'procedimientos': 'Ubicación en mapa; lectura de fuente cartográfica; actividades.',
            'instrumentos': 'Ficha 18-A; lista de cotejo; actividades corregidas.',
            'criterios': [
                'Ubica los ríos Paraguay, Paraná y Pilcomayo, Asunción e Itaipú, y señala los tramos limítrofes.',
                'Explica por qué los ríos de la vertiente del Pacífico son más cortos en América del Sur.',
                'Propone una medida concreta de cuidado del agua y dice a quién corresponde.',
            ],
        },
        'precisiones': [
            'Los mapas de las Figuras 18.2, 18.3 y de la Ficha 18-A se hicieron con datos de Natural Earth; no muestran todos los afluentes ni los lagos Ypacaraí e Ypoá, que se nombran en el texto. Si se dispone de un atlas escolar, conviene ubicarlos allí.',
            'La Ficha 18-A se usa también en la Evaluación de la Unidad 5: conviene guardar una copia limpia por estudiante.',
        ],
        'tarea': 'Actividad 15 de la Clase 18.',
    },
    {
        'n': 29, 'encuentro': 29,
        'titulo': 'Continuación F — La Hidrovía: beneficios, impactos y decisiones',
        'unidad': 'Unidad 5 — El espacio geográfico: posición, relieve e hidrografía',
        'material': 'Tomo: Continuación F (Figura F.1) y Fichas reproducibles F-A, F-B y F-C',
        'capacidad': CAP_G2,
        'tema': 'Hidrovía Paraná-Paraguay. Impacto ecológico, social y económico. Potencialidad de los recursos naturales y necesidad de su preservación.',
        'indicadores': [
            'Explica por qué la Hidrovía es estratégica para un país sin litoral marítimo.',
            'Distingue impactos económicos, sociales y ecológicos de la navegación y de sus obras.',
            'Propone medidas de prevención y de control fundamentadas.',
        ],
        'proposito': 'Que los estudiantes analicen una decisión desde varios roles y tomen posición con argumentos de las tres dimensiones.',
        'secuencia': [
            ('Inicio', [
                ('0–15', 'Recupera la Clase 18 con la Figura F.1 y pregunta: «Una obra muy útil, ¿puede tener costos? ¿Para quién?».',
                 'Responden con ejemplos.', 'Ideas en la pizarra.'),
            ]),
            ('Desarrollo', [
                ('15–30', 'Lectura de «Una vía natural y regional».',
                 'Subrayan los aspectos que el texto agrega además de «sirve para exportar».', 'Texto subrayado.'),
                ('30–45', 'Explica el cuadro de las tres dimensiones y el Concepto clave de evaluación de impacto ambiental, con un ejemplo distinto del caso (un puerto nuevo).',
                 'Agregan una pregunta propia en cada fila del cuadro.', 'Cuadro ampliado.'),
                ('45–55', 'Organiza grupos de 4, reparte las Fichas F-A y F-B y asigna un rol a cada integrante.',
                 'Leen el caso y anotan qué gana y qué arriesga su rol.', 'Notas por rol.'),
                ('55–85', 'Circula orientando; pide que cada rol fundamente.',
                 'Resuelven las consignas 1 a 3 del taller y completan la matriz de la Ficha F-C.', 'Ficha F-C; consignas 1 a 3.'),
                ('85–100', 'Recuerda la extensión y la estructura de la decisión.',
                 'Escriben la decisión del equipo (consigna 4) en la Ficha F-C.', 'Decisión escrita.'),
            ]),
            ('Cierre', [
                ('100–113', 'Invita a dos equipos con decisiones distintas a exponer y sintetiza.',
                 'Exponen y comparan argumentos.', 'Exposición oral.'),
                ('113–120', 'Explica la autoevaluación del taller.',
                 'Completan la tabla de autoevaluación del tomo.', 'Autoevaluación.'),
            ]),
        ],
        'diversidad': [
            'Tarjetas de rol con dos preguntas guía para quienes necesitan más estructura.',
            'Desafío: comparar el caso con la construcción de Itaipú (Clase 18) y señalar qué impactos se repiten.',
        ],
        'evaluacion': {
            'tipo': 'Formativa, con producto.',
            'procedimientos': 'Análisis de caso con roles; matriz de decisión; decisión escrita.',
            'instrumentos': 'Ficha F-C; autoevaluación del tomo; rúbrica del solucionario.',
            'criterios': [
                'Relaciona la Hidrovía con la mediterraneidad.',
                'Identifica al menos un beneficio o impacto en cada dimensión.',
                'Propone una medida coherente con el impacto que identificó.',
            ],
        },
        'precisiones': [
            'El caso de la Ficha F-A es ficticio y no tiene cifras: se evalúa el razonamiento, no una respuesta única.',
            'No se califica la decisión tomada, sino que esté fundamentada en las tres dimensiones.',
        ],
        'tarea': 'Terminar la decisión del equipo si no se completó en clase.',
    },
    {
        'n': 30, 'encuentro': 30,
        'titulo': 'Evaluación de la Unidad 5 — Posición, relieve e hidrografía',
        'unidad': 'Unidad 5 — El espacio geográfico: posición, relieve e hidrografía',
        'material': 'Tomo: Evaluación de la Unidad 5 y Ficha reproducible 18-A',
        'capacidad': 'Analiza la posición geográfica de Paraguay y América y sus incidencias en las actividades humanas. '
                     'Relaciona las características de las unidades orohidrográficas de Paraguay y América.',
        'tema': 'Evaluación de las Clases 16, 17 y 18 y de la Continuación F.',
        'indicadores': [
            'Ubica el Paraguay, sus países limítrofes y sus principales ríos.',
            'Diferencia la posición absoluta de la relativa.',
            'Identifica grandes ríos de América y su vertiente.',
            'Analiza beneficios e impactos de la Hidrovía.',
            'Explica la influencia de la posición, el relieve y los ríos en las actividades económicas.',
        ],
        'proposito': 'Comprobar los logros de la unidad con una prueba de 70 minutos y devolver una corrección comentada en el mismo encuentro.',
        'secuencia': [
            ('Inicio', [
                ('0–10', 'Explica la estructura (Partes A a F), el puntaje (28 puntos) y el tiempo. Entrega una Ficha 18-A limpia a quien no la tenga.',
                 'Leen toda la prueba y preguntan dudas de consigna.', '—'),
            ]),
            ('Desarrollo', [
                ('10–80', 'Supervisa la resolución individual; solo aclara consignas.',
                 'Resuelven las Partes A a F.', 'Prueba completa.'),
            ]),
            ('Cierre', [
                ('80–105', 'Retira las pruebas y corrige en la pizarra las Partes A, B y D con la clave; muestra en un mapa grande las respuestas de la Parte C.',
                 'Anotan en una hoja aparte los ítems que creen haber respondido mal y por qué.', 'Hoja de autocorrección.'),
                ('105–120', 'Lee dos ejemplos (anónimos o preparados) de respuesta a la Parte F: uno completo y uno parcial, y explica la rúbrica.',
                 'Comparan los ejemplos con su propia respuesta.', 'Reflexión escrita breve.'),
            ]),
        ],
        'diversidad': [
            'Lectura en voz alta de las consignas para quien lo necesite.',
            'Tiempo adicional de 15 minutos para la Parte F a estudiantes con apoyo, o resolución oral con registro del docente.',
        ],
        'evaluacion': {
            'tipo': 'Sumativa de unidad, con devolución formativa.',
            'procedimientos': 'Prueba escrita; ubicación en mapa; lectura de mapa; matriz; respuesta desarrollada.',
            'instrumentos': 'Prueba de la Unidad 5 del tomo; Ficha 18-A; clave y rúbrica del solucionario.',
            'criterios': [
                'Total: 28 puntos (A 6; B 4; C 6; D 3; E 4; F 5). La calificación se obtiene con la escala de la institución.',
                'La Parte F se corrige con la rúbrica del solucionario (posición, relieve, ríos, uso de datos y redacción).',
            ],
        },
        'precisiones': [
            'La prueba evalúa también las Clases 16 y 17 tal como están en el tomo actual; si esas clases se amplían, hay que revisar los ítems 1 a 4, 7, 8 y 10.',
        ],
        'tarea': 'Repasar el ítem con más errores con la clase correspondiente.',
    },
]
