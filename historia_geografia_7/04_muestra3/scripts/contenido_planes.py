"""Planes de clase de la tercera muestra (15, 28, 29 y 30).

Cambios respecto de la segunda muestra:
- tiempos verosímiles para 7.º grado: cada fase tiene una carga que entra en
  sus minutos, y la suma es exactamente 120;
- las actividades del tomo se clasifican en esenciales (evidencian la
  capacidad y se hacen en clase), de consolidación (en clase si alcanza el
  tiempo; si no, al inicio del encuentro siguiente) y complementarias o
  domiciliarias;
- los criterios de corrección que se usan son los mismos que el tomo comunica
  al estudiante en cada consigna;
- en la evaluación, el tiempo adicional se da bajo supervisión y ninguna
  respuesta se revela antes de que terminen todos; la devolución con claves
  es en el encuentro siguiente.
"""
from contenido_tomo import CAP_G2, CAP_H3

COMUNES = {'disciplina': 'Historia y Geografía', 'duracion': '3 HC (120 minutos)'}

PLANES = [
    {
        'n': 15, 'encuentro': 15,
        'titulo': 'Clase 10 — La Real Provisión de 1537 y las instituciones coloniales',
        'unidad': 'Unidad 3 — El Paraguay y América en el siglo XVI',
        'material': 'Tomo: Clase 10 (Figuras 10.1 y 10.2); planisferio o mapamundi del aula (para la distancia entre España y el Río de la Plata)',
        'capacidad': CAP_H3,
        'vinculo': 'Capacidad literal del programa MEC 2014 (pág. 55). Tema: los del programa para esa capacidad.',
        'tema': 'Ejercicio del derecho a la autonomía (Real Provisión del 12 de septiembre de 1537). Instituciones coloniales: Cabildo (tipos e importancia). Obispado. Encomienda (tipos y características).',
        'indicadores': [
            'Explica en qué situación la Real Provisión de 1537 autorizaba elegir un gobernador y quiénes podían hacerlo.',
            'Diferencia la elección colonial de 1537 de una elección democrática actual.',
            'Reconoce las funciones del gobernador, el Cabildo y el Obispado, y los tipos de encomienda.',
        ],
        'proposito': 'Que lean un documento de época, entiendan qué autonomía tenían los vecinos de Asunción y sus límites, y distingan el gobierno de la encomienda.',
        'funciones': {
            'Esenciales': 'En clase: fuente (preguntas 1 a 3); Ubicate; actividades 1, 2, 3, 4, 7, 13 y 15.',
            'Consolidación': 'Actividades 5, 8, 9 y 10 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 16).',
            'Complementarias o domiciliarias': 'Actividades 6, 11, 12 y 14 (repaso breve), actividad 16 (párrafo) y autoevaluación de la clase.',
        },
        'secuencia': [
            ('Inicio', [
                ('0–10', 'Plantea un problema: «Si la dirección de la escuela queda vacía y no llega nadie de afuera, ¿quién decide? ¿Con qué límites?». Vincula con la fundación de Asunción (Clase 8).',
                 'Proponen respuestas y discuten los límites de esa decisión.', 'Ideas en la pizarra.'),
            ]),
            ('Desarrollo', [
                ('10–25', 'Lectura guiada de «Una provincia lejana y sin gobernador». Muestra en el planisferio la distancia entre España, Buenos Aires y Asunción.',
                 'En parejas escriben en dos líneas cuál era el problema de la provincia en 1537.', 'Problema escrito.'),
                ('25–33', 'Lectura de «Qué decía la Real Provisión» y de «Después de 1537»: destaca las tres condiciones y explica que los historiadores discuten cómo llegó Irala al cargo.',
                 'Subrayan las tres condiciones de la provisión.', 'Texto subrayado.'),
                ('33–47', 'Lee en voz alta los dos fragmentos de «Trabajá con la fuente» y explica el vocabulario.',
                 'Responden individualmente las preguntas 1 a 3 de la fuente, en los renglones del recuadro.', 'Fuente (esencial).'),
                ('47–55', 'Presenta la Figura 10.1 (línea de tiempo).',
                 'Resuelven el «Ubicate» y la actividad 7 (ordenar hechos).', 'Ubicate y actividad 7 (esenciales).'),
                ('55–70', 'Organiza grupos de 4 para analizar el cuadro «Elegir en 1537 y elegir hoy» y lee el Concepto clave sobre autonomía.',
                 'Cada grupo escribe en el cuaderno una fila nueva para el cuadro y resuelve las actividades 1, 2 y 3.', 'Fila agregada; actividades 1 a 3 (esenciales).'),
                ('70–88', 'Explica las autoridades con la Figura 10.2, el Cabildo (tipos), el Obispado y la encomienda (tipos).',
                 'Resuelven las actividades 4 y 13.', 'Actividades 4 y 13 (esenciales).'),
                ('88–100', 'Acompaña la resolución individual; quien termina antes sigue con las de consolidación.',
                 'Resuelven las actividades 5, 8, 9 y 10.', 'Actividades de consolidación.'),
            ]),
            ('Cierre', [
                ('100–112', 'Retoma solo los errores frecuentes de las esenciales, que se comprobaron por parejas al cerrar cada bloque.',
                 'Corrigen con otro color lo que haga falta.', 'Errores frecuentes corregidos.'),
                ('112–120', 'Boleto de salida con la actividad 15. Asigna la tarea y lee los criterios de la actividad 16.',
                 'Escriben la actividad 15 y la entregan.', 'Actividad 15 (esencial).'),
            ]),
        ],
        'diversidad': [
            'Apoyo para la lectura: el docente lee los fragmentos en voz alta y deja un glosario en la pizarra (capitulación, adelantado, cabildo, encomienda, mita, yanacona).',
            'Apoyo en la fuente: las preguntas 1 a 3 pueden responderse eligiendo entre dos opciones escritas en la pizarra (1: al rey / a los vecinos; 2: que fuera el más capaz / que fuera el más rico; 3: por su cuenta / en nombre del rey), con la misma exigencia de citar la frase.',
            'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
            'Desafío: comparar cómo llegó Irala al gobierno en 1539 y en 1544, y por qué los historiadores no coinciden.',
        ],
        'evaluacion': {
            'tipo': 'Formativa.',
            'procedimientos': 'Análisis de fuente; cuadro comparativo; ordenamiento cronológico; boleto de salida.',
            'instrumentos': 'Lista de cotejo con los tres criterios; actividad 16 con los criterios de su consigna.',
            'criterios': [
                'Nombra las tres condiciones de la Real Provisión: falta de autoridad, electores españoles y gobierno en nombre del rey.',
                'Señala al menos dos diferencias entre la elección de 1537 y una elección actual.',
                'Distingue las instituciones de gobierno (gobernador, Cabildo) de la encomienda y explica sus dos tipos.',
            ],
        },
        'precisiones': [
            'El programa del MEC dice «Ejercicio del derecho a la autonomía»; el tomo lo explica en el Concepto clave. No presentarlo como democracia ni como independencia.',
            'Los dos fragmentos vienen de transcripciones distintas, con su ortografía. Sobre 1539, el tomo presenta el debate sin tomar partido: no afirmar que hubo una elección.',
        ],
        'tarea': 'Actividades 6, 11, 12 y 14 (repaso breve) y actividad 16 (párrafo con los criterios de la consigna).',
    },
    {
        'n': 28, 'encuentro': 28,
        'titulo': 'Clase 18 — La hidrografía y la Hidrovía',
        'unidad': 'Unidad 5 — El espacio geográfico: posición, relieve e hidrografía',
        'material': 'Tomo: Clase 18 (Figuras 18.1, 18.2 y 18.3); copias de la Ficha reproducible 18-A preparadas antes del encuentro (algunas con banco de nombres); lápices azul y rojo',
        'capacidad': CAP_G2,
        'vinculo': 'Capacidad literal del programa MEC 2014 (pág. 57). Tema: los del programa para esa capacidad.',
        'tema': 'Hidrografía de Paraguay y América. Importancia y utilidad de los cauces hídricos. Hidrovía Paraná-Paraguay. Impacto ecológico, social y económico. Potencialidad de los recursos naturales y necesidad de su preservación.',
        'indicadores': [
            'Reconoce los principales ríos, lagos, esteros y acuíferos del Paraguay y su ubicación.',
            'Identifica las grandes cuencas y vertientes de América.',
            'Explica la importancia de los ríos y de la Hidrovía, y la necesidad de preservar el agua.',
        ],
        'proposito': 'Que los estudiantes ubiquen la red hidrográfica del Paraguay dentro de la Cuenca del Plata, la comparen con la de América y relacionen el agua con la energía, el transporte y su cuidado.',
        'funciones': {
            'Esenciales': 'En clase: Ubicate (Ficha 18-A); fuente cartográfica (preguntas 1 a 3); actividades 1, 3, 5, 7, 8 y 12; actividad 14 (oral).',
            'Consolidación': 'Actividades 2, 4, 6 y 9 (en clase si alcanza; si no, en casa, con revisión breve al abrir el encuentro 29).',
            'Complementarias o domiciliarias': 'Actividades 10, 11 y 13 (repaso breve) y actividad 15.',
        },
        'secuencia': [
            ('Inicio', [
                ('0–10', 'Pregunta: «¿De dónde viene el agua que sale de la canilla en tu casa?». Anota las respuestas (río, pozo, acuífero).',
                 'Responden según su experiencia.', 'Ideas en la pizarra.'),
            ]),
            ('Desarrollo', [
                ('10–25', 'Explica río, afluente, margen, cuenca y vertiente con el Concepto clave y el Ejemplo del Tebicuary; dibuja en la pizarra el camino del agua hasta el Río de la Plata.',
                 'Resuelven las actividades 1, 7 y 8 y las comprueban con el compañero.', 'Actividades 1, 7 y 8 (esenciales).'),
                ('25–50', 'Lectura de «Los grandes ríos del Paraguay» con la Figura 18.1 y el cuadro de los tres ríos. Modela en la pizarra el primer paso del «Ubicate» (repasar el río Paraguay) y después acompaña. Al final del bloque revisa la ficha con la Figura 18.1 proyectada o dibujada.',
                 'En parejas resuelven el «Ubicate» en la Ficha 18-A y lo revisan con la Figura 18.1.', 'Ficha 18-A revisada (esencial).'),
                ('50–60', 'Lectura de «Lagos, esteros, humedales y agua subterránea»; relaciona el Acuífero Patiño con el inicio.',
                 'Resuelven la actividad 5.', 'Actividad 5 (esencial).'),
                ('60–70', 'Lectura de «Ríos que dan vida y energía» y de «La Hidrovía Paraguay-Paraná» con la Figura 18.2.',
                 'Resuelven la actividad 3 y explican oralmente por qué ninguna obra es solo beneficio.', 'Actividad 3 (esencial).'),
                ('70–90', 'Presenta «Los grandes ríos y lagos de América» con la Figura 18.3 y comprueba en voz alta la primera pregunta de la fuente.',
                 'Responden por escrito las preguntas 1 a 3 de la fuente cartográfica.', 'Fuente cartográfica (esencial).'),
                ('90–100', 'Lectura de «Cuidar el agua» y del Concepto clave sobre recursos renovables.',
                 'Resuelven la actividad 12; quien termina antes sigue con las actividades 2, 4, 6 y 9 (consolidación; si no alcanza el tiempo, se completan en casa).', 'Actividad 12 (esencial); consolidación.'),
            ]),
            ('Cierre', [
                ('100–110', 'Retoma solo los errores más frecuentes de las esenciales (la ficha ya se revisó en su bloque).',
                 'Corrigen con otro color lo que haga falta.', 'Errores frecuentes corregidos.'),
                ('110–120', 'Puesta en común de la actividad 14 y asignación de la tarea.',
                 'Comparten tres usos del agua con ejemplos.', 'Actividad 14 (oral).'),
            ]),
        ],
        'diversidad': [
            'Apoyo espacial: antes de clase, el docente escribe al pie de algunas copias de la Ficha 18-A este banco de nombres: Paraguay, Paraná, Pilcomayo, Asunción, Itaipú, Yacyretá, Bolivia, Brasil, Argentina. El estudiante los copia en su lugar.',
            'Apoyo en la lectura de mapas: el docente señala primero en la Figura 18.1 el río Paraguay y la frontera, y luego el estudiante repite en la ficha.',
            'Ajuste de cantidad: quien necesita más tiempo hace solo las esenciales en clase (ver «Actividades según su función»).',
            'Desafío: averiguar qué río, lago o acuífero abastece de agua a su localidad y qué institución la distribuye.',
        ],
        'evaluacion': {
            'tipo': 'Formativa.',
            'procedimientos': 'Ubicación en mapa; lectura de fuente cartográfica; actividades.',
            'instrumentos': 'Ficha 18-A; lista de cotejo; criterios de las actividades 14 y 15 tal como figuran en sus consignas.',
            'criterios': [
                'Ubica los ríos Paraguay, Paraná y Pilcomayo, Asunción e Itaipú, y señala los tramos limítrofes.',
                'Explica por qué los ríos de la vertiente del Pacífico son más cortos en América del Sur.',
                'Propone una medida concreta de cuidado del agua y dice a quién corresponde.',
            ],
        },
        'precisiones': [
            'Los mapas se hicieron con datos de Natural Earth: no muestran todos los afluentes ni los lagos Ypacaraí e Ypoá, que se nombran en el texto. Si hay un atlas escolar, conviene ubicarlos allí.',
            'La Evaluación de la Unidad 5 trae su propia copia del mapa mudo; la Ficha 18-A se usa en esta clase.',
        ],
        'tarea': 'Actividades 10, 11 y 13 (repaso breve) y actividad 15 de la Clase 18.',
    },
    {
        'n': 29, 'encuentro': 29,
        'titulo': 'Continuación F — La Hidrovía: beneficios, impactos y decisiones',
        'unidad': 'Unidad 5 — El espacio geográfico: posición, relieve e hidrografía',
        'material': 'Tomo: Continuación F y Figura 18.2 de la Clase 18; Fichas reproducibles F-A, F-B (tarjetas para recortar) y F-C, fotocopiadas antes del encuentro',
        'capacidad': CAP_G2,
        'vinculo': 'Capacidad literal del programa MEC 2014 (pág. 57); la continuación profundiza el tema «Hidrovía Paraná-Paraguay. Impacto ecológico, social y económico».',
        'tema': 'Hidrovía Paraná-Paraguay. Impacto ecológico, social y económico. Potencialidad de los recursos naturales y necesidad de su preservación.',
        'indicadores': [
            'Explica por qué la Hidrovía es estratégica para un país sin litoral marítimo.',
            'Distingue impactos económicos, sociales y ecológicos de la navegación y de sus obras.',
            'Propone medidas de prevención y de control fundamentadas.',
        ],
        'proposito': 'Que los estudiantes analicen una decisión desde varios roles y tomen posición con argumentos de las tres dimensiones.',
        'funciones': {
            'Esenciales': 'En clase: consignas 1 a 4 del taller; matriz y decisión del equipo en la Ficha F-C (única decisión que se califica).',
            'Consolidación': 'En clase: autoevaluación del taller.',
            'Complementarias o domiciliarias': 'Desafío de comparación con Itaipú (Clase 18).',
        },
        'secuencia': [
            ('Inicio', [
                ('0–12', 'Recupera la Clase 18 con la Figura 18.2 (y revisa en dos o tres minutos las dudas de consolidación de la Clase 18) y pregunta: «Una obra muy útil, ¿puede tener costos? ¿Para quién?».',
                 'Responden con ejemplos.', 'Ideas en la pizarra.'),
            ]),
            ('Desarrollo', [
                ('12–25', 'Lectura de «Una vía natural y regional».',
                 'Subrayan los aspectos que el texto agrega además de «sirve para exportar».', 'Texto subrayado.'),
                ('25–40', 'Explica el cuadro de las tres dimensiones y el Concepto clave de evaluación de impacto ambiental, con un ejemplo distinto del caso.',
                 'Escriben en el cuaderno una pregunta propia para cada fila del cuadro.', 'Tres preguntas en el cuaderno.'),
                ('40–50', 'Organiza grupos de 4, reparte las Fichas F-A y F-B y asigna los roles. Lee en voz alta los criterios de la consigna 4 y aclara que se califica solo la decisión de la Ficha F-C.',
                 'Leen el caso y completan la tarjeta de su rol (qué gana, qué arriesga, argumento).', 'Tarjetas de rol completas.'),
                ('50–80', 'Circula orientando; pide que cada rol fundamente.',
                 'Resuelven las consignas 1 a 3 y completan la matriz de la Ficha F-C.', 'Consignas 1 a 3 y Ficha F-C (esenciales).'),
                ('80–98', 'Recuerda la extensión y los criterios de la decisión.',
                 'Escriben la decisión del equipo en la Ficha F-C (consigna 4); los renglones del tomo sirven de borrador personal.', 'Consigna 4 en la Ficha F-C (esencial).'),
            ]),
            ('Cierre', [
                ('98–112', 'Invita a dos equipos con decisiones distintas a exponer y sintetiza.',
                 'Exponen y comparan argumentos.', 'Exposición oral.'),
                ('112–120', 'Explica la autoevaluación del taller.',
                 'Completan la autoevaluación del tomo.', 'Autoevaluación.'),
            ]),
        ],
        'diversidad': [
            'Las tarjetas de la Ficha F-B traen impresas dos preguntas guía («¿Qué gana mi grupo?» y «¿Qué arriesga?») y un espacio para el argumento; quien necesita más estructura completa primero esas dos columnas con ayuda del docente.',
            'En la consigna 4, quien lo necesite puede presentar la decisión oralmente al docente, que la registra con los mismos criterios.',
            'Desafío: comparar el caso con la construcción de Itaipú (Clase 18) y señalar qué impactos se repiten.',
        ],
        'evaluacion': {
            'tipo': 'Formativa, con producto.',
            'procedimientos': 'Análisis de caso con roles; matriz de decisión; decisión escrita.',
            'instrumentos': 'Ficha F-C; autoevaluación del tomo; rúbrica de la consigna 4, la misma que el tomo comunica al estudiante.',
            'criterios': [
                'Relación con la mediterraneidad (2 puntos).',
                'Un argumento económico, uno social y uno ecológico (3 puntos).',
                'Una medida coherente con el impacto (2 puntos) y redacción clara (1 punto).',
            ],
        },
        'precisiones': [
            'El caso de la Ficha F-A es ficticio y no tiene cifras: se evalúa el razonamiento, no una respuesta única.',
            'No se califica la decisión tomada, sino que esté fundamentada en las tres dimensiones.',
        ],
        'tarea': 'Desafío optativo: comparar el caso con la construcción de Itaipú (Clase 18). La decisión del equipo se termina en clase.',
    },
    {
        'n': 30, 'encuentro': 30,
        'titulo': 'Evaluación de la Unidad 5 — Posición, relieve e hidrografía',
        'unidad': 'Unidad 5 — El espacio geográfico: posición, relieve e hidrografía',
        'material': 'Tomo: Evaluación de la Unidad 5 (incluye el mapa mudo de la Parte C y el mapa de la Parte D)',
        'capacidad': 'Analiza la posición geográfica de Paraguay y América y sus incidencias en las actividades humanas. '
                     'Relaciona las características de las unidades orohidrográficas de Paraguay y América.',
        'vinculo': 'Asociación curricular: la evaluación integra dos capacidades literales del programa MEC 2014 (pág. 57); no tiene capacidad propia.',
        'tema': 'Evaluación de las Clases 16, 17 y 18 y de la Continuación F.',
        'indicadores': [
            'Ubica el Paraguay, sus países limítrofes y sus principales ríos.',
            'Diferencia la posición absoluta de la relativa.',
            'Identifica grandes ríos de América y su vertiente.',
            'Analiza beneficios e impactos de la Hidrovía.',
            'Explica la influencia de la posición, el relieve y los ríos en las actividades económicas.',
        ],
        'proposito': 'Comprobar los logros de la unidad con una prueba de 70 minutos, en condiciones iguales para todos, y devolver la corrección comentada en el encuentro siguiente.',
        'funciones': {
            'Material que recibe cada estudiante': 'La prueba del tomo (fotocopiada o en el cuadernillo), que ya incluye los dos mapas. No se usa ninguna otra ficha.',
            'Criterios de puntaje': 'Figuran en cada parte de la prueba: A 6, B 4, C 6, D 3, E 4 y F 5 (total 28).',
            'Devolución': 'Con claves y rúbrica, en los primeros 20 minutos del encuentro 31, cuando todos terminaron.',
        },
        'secuencia': [
            ('Inicio', [
                ('0–10', 'Explica la estructura (Partes A a F), el puntaje de cada parte y el tiempo. Lee en voz alta los criterios de la Parte F.',
                 'Leen toda la prueba y preguntan dudas de consigna.', '—'),
            ]),
            ('Desarrollo', [
                ('10–80', 'Supervisa la resolución individual; solo aclara consignas.',
                 'Resuelven las Partes A a F.', 'Prueba.'),
                ('80–95', 'Tiempo adicional supervisado para quienes lo necesitan (hasta 15 minutos). Los demás entregan y pasan a la actividad sin claves.',
                 'Quienes tienen tiempo adicional siguen la prueba; el resto trabaja en la actividad sin claves.', 'Entrega de todas las pruebas.'),
            ]),
            ('Cierre', [
                ('95–120', 'Con todas las pruebas entregadas, propone una actividad sin claves: cada estudiante escribe qué parte le resultó más difícil y qué clase va a repasar. No se corrige ni se comentan respuestas.',
                 'Completan la reflexión y la entregan.', 'Reflexión escrita (no lleva nota).'),
            ]),
        ],
        'diversidad': [
            'Tiempo adicional de hasta 15 minutos (80 a 95), supervisado, sin corrección simultánea: nadie recibe respuestas antes de que terminen todos.',
            'Lectura en voz alta de las consignas para quien lo necesite, sin explicar contenidos.',
            'Si un estudiante necesita más de 15 minutos adicionales, completa la prueba al comienzo del encuentro 31, antes de la devolución.',
        ],
        'evaluacion': {
            'tipo': 'Sumativa de unidad; devolución formativa en el encuentro 31.',
            'procedimientos': 'Prueba escrita; ubicación en mapa; lectura de mapa; matriz; respuesta desarrollada.',
            'instrumentos': 'Prueba de la Unidad 5 del tomo; clave y rúbrica del solucionario, que coinciden con los criterios impresos en la prueba.',
            'criterios': [
                'Total: 28 puntos (A 6; B 4; C 6; D 3; E 4; F 5). La calificación se obtiene con la escala de la institución.',
                'La Parte F se corrige con los cinco criterios impresos en la consigna (1 punto cada uno).',
            ],
        },
        'precisiones': [
            'La prueba evalúa también las Clases 16 y 17 tal como están en el tomo actual; si esas clases se amplían, hay que revisar los ítems 1 a 4, 7, 8 y 10.',
            'Primeros 20 minutos del encuentro 31: devolución con claves y rúbrica y comparación con la reflexión escrita. El Plan 31 debe reservar ese tiempo cuando se rehaga.',
        ],
        'tarea': 'Repasar la clase que cada estudiante anotó en su reflexión.',
    },
]
