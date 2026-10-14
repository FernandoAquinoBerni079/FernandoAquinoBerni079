"""Contenido de los cinco planes del piloto (1, 28, 29, 30 y 31).

Los campos Capacidad, Tema e Indicadores se copian de la ficha del tomo de cada
encuentro. La secuencia trabaja con el tomo tal como está hoy; cuando el tomo
tiene un error o le falta algo, el plan lo dice en «Precisiones para el
docente» en lugar de inventar contenido para el alumno.
"""

COMUNES = {
    'disciplina': 'Historia y Geografía',
    'grado': '7.º grado — Educación Escolar Básica, Tercer Ciclo',
    'duracion': '3 HC (120 minutos)',
}

PLANES = [
    {
        'n': 1, 'encuentro': 1,
        'titulo': 'Clase 1 — La Historia y la Geografía: mirar el tiempo y el espacio',
        'unidad': 'Unidad 1 — Cómo mirar el tiempo y el espacio',
        'material': 'Tomo: Prueba diagnóstica y Clase 1',
        'capacidad': 'Reconoce el objeto de estudio de la Historia y la Geografía y el uso de fuentes.',
        'tema': 'La Historia mira el tiempo; la Geografía mira el espacio. Fuentes primarias y secundarias.',
        'indicadores': [
            'Diferencia el objeto de estudio de la Historia y de la Geografía.',
            'Distingue una fuente primaria de una secundaria con ejemplos.',
            'Ubica hechos en una línea de tiempo sencilla.',
        ],
        'proposito': 'Que los estudiantes conozcan el cuadernillo, muestren lo que ya saben (sin nota) y empiecen a usar las dos preguntas básicas del área: ¿cuándo? y ¿dónde?',
        'secuencia': [
            ('Inicio', [
                ('0–5', 'Presenta el cuadernillo: muestra una clase completa y las secciones que se repiten («Trabajá con la fuente», «Ubicate», actividades). Acuerda con el grupo cómo se trabaja.',
                 'Hojean la Clase 1 y ubican las secciones nombradas.', '—'),
                ('5–20', 'Entrega la prueba diagnóstica. Aclara que no lleva nota. Circula sin corregir ni dar pistas; retira las hojas al terminar.',
                 'Resuelven individualmente las 6 consignas.', 'Prueba diagnóstica (se usa para planificar apoyos).'),
                ('20–25', 'Escribe en la pizarra «¿Cuándo naciste?» y «¿Dónde vivís?» y anota las respuestas en dos columnas: TIEMPO y ESPACIO.',
                 'Responden en voz alta y deciden en qué columna va cada respuesta.', 'Cuadro de dos columnas en la pizarra.'),
            ]),
            ('Desarrollo', [
                ('25–40', 'Lectura compartida de «¿Para qué sirven la Historia y la Geografía?» y de la Figura 1.1. Pregunta qué interroga cada ciencia.',
                 'En parejas escriben una pregunta histórica y una geográfica sobre su propia ciudad o compañía.', 'Dos preguntas por pareja.'),
                ('40–55', 'Explica el tiempo histórico y la regla del siglo con la caja «Ejemplo». Resuelve en la pizarra 1537, 1811 y 2026, y muestra el caso especial de los años terminados en 00 (ver Precisiones).',
                 'Calculan el siglo de los años que dicta el docente. Resuelven las actividades 3 y 7.', 'Actividades 3 y 7.'),
                ('55–70', 'Lectura de «El espacio geográfico: un producto social» y de la caja «Concepto clave». Organiza grupos de 4.',
                 'Cada grupo nombra tres elementos de su barrio hechos o transformados por las personas y explica por qué no son «solo naturaleza». Resuelven las actividades 4 y 10.', 'Lista del grupo; actividades 4 y 10.'),
                ('70–90', 'Lectura de «Las fuentes» y de la Figura 1.2. Muestra o describe tres objetos (una foto familiar antigua, una boleta actual, el propio cuadernillo) y pregunta si son fuente primaria o secundaria de qué época. Comenta la caja «En Paraguay» (Archivo Nacional de Asunción).',
                 'Clasifican los objetos y justifican según cuándo se creó cada uno. Resuelven las actividades 2, 6 y 9.', 'Actividades 2, 6 y 9.'),
                ('90–100', 'Presenta la cita de Luis Villoro en «Trabajá con la fuente».',
                 'Responden por escrito las preguntas 1 y 2; comparten oralmente la pregunta 3.', 'Respuestas escritas.'),
            ]),
            ('Cierre', [
                ('100–112', 'Explica la consigna «Ubicate · Línea de tiempo» y controla que los hechos vayan del más antiguo (izquierda) al más reciente (derecha).',
                 'Dibujan la línea de tiempo de su vida con cuatro hechos fechados.', 'Línea de tiempo personal.'),
                ('112–118', 'Corrección oral rápida de las actividades 1, 5 y 8.',
                 'Responden y corrigen en el cuadernillo.', 'Actividades 1, 5 y 8.'),
                ('118–120', 'Asigna la tarea y hace una pregunta de cierre: «¿Qué pregunta te hacés vos sobre el pasado?».',
                 'Anotan la tarea: actividades 11 y 12.', 'Tarea.'),
            ]),
        ],
        'diversidad': [
            'Lectura en voz alta de los apartados para quienes leen con dificultad; el docente escribe en la pizarra las palabras clave (siglo, fuente primaria, fuente secundaria, espacio geográfico).',
            'El guaraní puede usarse como lengua de apoyo en la lluvia de ideas y en el trabajo de grupo.',
            'Desafío para quienes terminan antes: ordenar en una línea de tiempo cinco hechos de la historia del Paraguay que ya conozcan.',
        ],
        'evaluacion': {
            'tipo': 'Diagnóstica y formativa.',
            'procedimientos': 'Prueba diagnóstica; observación del trabajo de grupo; revisión de la línea de tiempo.',
            'instrumentos': 'Registro de la prueba diagnóstica (cuadro por alumno con las 6 consignas); lista de cotejo.',
            'criterios': [
                'Distingue el objeto de estudio de la Historia y el de la Geografía con un ejemplo propio.',
                'Clasifica una fuente como primaria o secundaria y justifica según cuándo se creó.',
                'Ordena cuatro hechos con su año de izquierda (más antiguo) a derecha (más reciente).',
            ],
        },
        'precisiones': [
            'La regla «dos primeras cifras + 1» falla con los años terminados en 00: el año 1900 pertenece al siglo XIX, no al XX, y el 2000 al siglo XX. Conviene decirlo al presentar la regla.',
            'Luis Villoro (1922–2014) fue un filósofo e historiador mexicano. La frase del tomo resume ideas de su ensayo «El sentido de la historia», publicado en el libro colectivo «Historia, ¿para qué?» (México, Siglo XXI, 1980). Antes de imprimir, conviene cotejar si el tomo la presenta como cita textual o como paráfrasis.',
            'Las respuestas de la prueba diagnóstica no se califican: sirven para decidir los apoyos de la Unidad 1.',
        ],
        'tarea': 'Actividades 11 y 12 de la Clase 1.',
    },
    {
        'n': 28, 'encuentro': 28,
        'titulo': 'Clase 18 — La hidrografía y la Hidrovía',
        'unidad': 'Unidad 5 — El espacio geográfico: posición, relieve e hidrografía',
        'material': 'Tomo: Clase 18',
        'capacidad': 'Relaciona las características de las unidades orohidrográficas.',
        'tema': 'La hidrografía. La Hidrovía Paraguay-Paraná. Recursos naturales y su preservación.',
        'indicadores': [
            'Reconoce los principales ríos del Paraguay.',
            'Explica la importancia de la Hidrovía.',
            'Valora la preservación de los recursos naturales.',
        ],
        'proposito': 'Que los estudiantes ubiquen los grandes ríos del país, entiendan por qué la Hidrovía es vital para un país sin litoral marítimo y reconozcan que el agua, aunque se renueva, no es inagotable.',
        'secuencia': [
            ('Inicio', [
                ('0–15', 'Dibuja el contorno del Paraguay en la pizarra y pregunta: «Si el Paraguay no tiene mar, ¿por dónde salen la soja y la carne hacia otros continentes?». Recuerda la mediterraneidad (Clases 11 y 16) y anota los ríos que nombra el grupo.',
                 'Proponen respuestas y nombran los ríos que conocen.', 'Lista de ríos en la pizarra.'),
            ]),
            ('Desarrollo', [
                ('15–30', 'Lectura de «El Paraguay, país de ríos» y del cuadro Río / Ubicación. Precisa el recorrido real del río Paraguay (ver Precisiones).',
                 'En el mapa esquemático marcan los ríos Paraguay, Paraná y Pilcomayo y la ciudad de Asunción (consigna «Ubicate»). Marcan con otro color los tramos en que el río Paraguay es límite.', 'Mapa con tres ríos y Asunción.'),
                ('30–45', 'Lectura de «Ríos que dan vida y energía» y de la caja «En Paraguay». Ubica Itaipú y Yacyretá en el mapa de la pizarra.',
                 'En parejas hacen un cuadro de dos columnas: uso del río y ejemplo del Paraguay (agua, pesca, transporte, energía).', 'Cuadro de usos.'),
                ('45–65', 'Presenta la Hidrovía con la Figura 18.1 y la caja «Ejemplo» («autopista de agua»). Organiza grupos de 4.',
                 'Siguen el recorrido de norte a sur, nombran los cinco países que une y responden por escrito las preguntas 1 a 3 de «Trabajá con la fuente».', 'Respuestas de la fuente.'),
                ('65–80', 'Lectura de «Cuidar el agua» y de la caja «Concepto clave»: renovable no quiere decir inagotable. Pregunta quién es responsable de cuidar los ríos.',
                 'Cada grupo propone una medida concreta para cada actor: el Estado, las empresas y las personas.', 'Tres medidas por grupo.'),
                ('80–95', 'Acompaña la resolución individual y atiende consultas.',
                 'Resuelven las actividades 1 a 10.', 'Actividades 1 a 10.'),
            ]),
            ('Cierre', [
                ('95–105', 'Dicta o proyecta la clave de las actividades 1 a 10 y explica las respuestas que más fallaron.',
                 'Corrigen en parejas con otro color.', 'Actividades corregidas.'),
                ('105–117', 'Pide un boleto de salida: «Escribí tres ideas de la clase: un río, un uso del agua y una forma de cuidarla».',
                 'Escriben el boleto y lo entregan.', 'Boleto de salida.'),
                ('117–120', 'Asigna la tarea y anticipa la Continuación F (beneficios e impactos de la Hidrovía).',
                 'Anotan la tarea.', 'Tarea.'),
            ]),
        ],
        'diversidad': [
            'Mapa esquemático con los nombres ya escritos para quienes tienen dificultades de ubicación espacial: solo deben repasar los ríos con color.',
            'Desafío: averiguar a qué país llega por agua la mercadería que sale de un puerto paraguayo cercano y qué otros caminos tiene (rutas y puertos francos de países vecinos).',
        ],
        'evaluacion': {
            'tipo': 'Formativa.',
            'procedimientos': 'Ubicación en el mapa; análisis de la fuente; boleto de salida.',
            'instrumentos': 'Lista de cotejo; actividades corregidas; boleto de salida.',
            'criterios': [
                'Ubica en el mapa los ríos Paraguay, Paraná y Pilcomayo, y Asunción.',
                'Explica la relación entre la Hidrovía y la mediterraneidad.',
                'Propone una medida concreta de cuidado del agua y dice a quién corresponde.',
            ],
        },
        'precisiones': [
            'El río Paraguay recorre el país de norte a sur, pero no siempre por dentro: en el norte, desde Bahía Negra hasta la desembocadura del río Apa, es límite con Brasil, y desde la confluencia con el Pilcomayo (frente a Asunción) hasta el Paraná es límite con Argentina. En todo su recorrido separa la Región Oriental de la Occidental. El tomo dice que «cruza» el país; conviene precisarlo en clase.',
            'Error frecuente: ubicar Itaipú sobre el río Paraguay. Las dos represas binacionales están sobre el río Paraná.',
            'Itaipú produce energía renovable, pero su construcción inundó los Saltos del Guairá y desplazó población: sirve para anticipar la Continuación F (toda obra tiene beneficios e impactos).',
            'Actividad 7: la clave es «renovable», pero un alumno puede escribir «escaso» o «vital». Se acepta si lo fundamenta; la idea que se busca es la del Concepto clave.',
            'El tomo todavía no desarrolla la Cuenca del Plata, los afluentes, los lagos y esteros, el Acuífero Guaraní ni la hidrografía de América (ver el informe de diagnóstico). Mientras no se amplíe, este plan no los da por enseñados.',
        ],
        'tarea': 'Actividades 11 y 12 de la Clase 18.',
    },
    {
        'n': 29, 'encuentro': 29,
        'titulo': 'Continuación F — Posición, ríos e Hidrovía: beneficios e impactos',
        'unidad': 'Unidad 5 — El espacio geográfico: posición, relieve e hidrografía',
        'material': 'Tomo: Continuación F',
        'capacidad': 'Relaciona las características de las unidades orohidrográficas de Paraguay y América y analiza la incidencia de la posición geográfica en las actividades humanas.',
        'tema': 'Hidrovía Paraguay–Paraná: integración, comercio, comunidades ribereñas y posibles impactos ambientales.',
        'indicadores': [
            'Explica por qué la Hidrovía es estratégica para un país sin litoral marítimo.',
            'Distingue impactos económicos, sociales y ecológicos vinculados a la navegación y sus obras.',
            'Propone medidas de gestión que compatibilicen navegación, seguridad y protección de los ecosistemas.',
        ],
        'proposito': 'Que los estudiantes analicen una decisión real de su país desde tres miradas y tomen posición con argumentos, sin suponer que una obra es buena o mala de antemano.',
        'secuencia': [
            ('Inicio', [
                ('0–15', 'Recupera la Clase 18 con el mapa de la Hidrovía. Plantea la pregunta: «Una obra muy útil, ¿puede tener costos? ¿Para quién?».',
                 'Responden oralmente con ejemplos (una ruta nueva, una represa).', 'Ideas en la pizarra.'),
            ]),
            ('Desarrollo', [
                ('15–30', 'Lectura de «Una vía natural y regional». Explica qué son los puertos de ultramar y por qué el comercio exterior depende de ellos.',
                 'Subrayan los aspectos que el texto agrega además de «sirve para exportar»: empleo, puertos, comunidades ribereñas, seguridad, nivel de los ríos, humedales, calidad del agua.', 'Texto subrayado.'),
                ('30–45', 'Lectura de «Tres dimensiones». Modela en la pizarra la matriz con un ejemplo distinto del caso (un puerto nuevo en una ciudad ribereña). Explica qué es una evaluación de impacto ambiental, en una definición breve (ver Precisiones).',
                 'Copian la matriz modelo y agregan un ejemplo propio en cada columna.', 'Matriz modelo.'),
                ('45–90', 'Organiza grupos de 4 y reparte roles: empresa naviera, pescadores y comunidad ribereña, organismo ambiental, autoridad de puertos. Entrega la ficha del caso (ver Precisiones) y circula orientando.',
                 'Cada integrante analiza el caso desde su rol. El grupo responde las consignas 1 a 3 de «Caso para decidir» y completa la matriz Económico / Social / Ecológico.', 'Matriz del grupo.'),
                ('90–105', 'Pide la conclusión individual y recuerda la extensión (6 a 8 líneas).',
                 'Escriben una conclusión fundamentada: qué decidirían y con qué medida preventiva.', 'Conclusión individual.'),
            ]),
            ('Cierre', [
                ('105–117', 'Invita a dos grupos con posiciones distintas a exponer. Sintetiza: un impacto se identifica, se estudia y se gestiona.',
                 'Exponen y comparan las posiciones.', 'Exposición oral.'),
                ('117–120', 'Explica la autoevaluación con la mini-rúbrica del solucionario.',
                 'Marcan su nivel en cada criterio.', 'Autoevaluación.'),
            ]),
        ],
        'diversidad': [
            'Roles con tarjetas de apoyo («¿Qué gana mi grupo? ¿Qué arriesga?») para quienes necesitan una guía más concreta.',
            'Desafío: comparar el caso con otra obra conocida (por ejemplo, Yacyretá) y señalar qué impactos se repiten.',
        ],
        'evaluacion': {
            'tipo': 'Formativa, con producto.',
            'procedimientos': 'Análisis de caso; matriz de decisión; conclusión escrita.',
            'instrumentos': 'Mini-rúbrica de las continuaciones (solucionario); lista de cotejo del trabajo en grupo.',
            'criterios': [
                'Relaciona la Hidrovía con la mediterraneidad.',
                'Identifica al menos un beneficio o un impacto en cada dimensión.',
                'Propone una medida de prevención o mitigación coherente con el impacto que identificó.',
            ],
        },
        'precisiones': [
            'Ficha del caso para el docente (caso didáctico ficticio, sin datos reales): «En un año de aguas bajas, las barcazas deben salir con menos carga en un tramo del río Paraguay. Se propone un dragado de mantenimiento, que consiste en sacar sedimentos del fondo para hacer más profundo el canal. Actores: empresas navieras y exportadores; pescadores y comunidades ribereñas; el Ministerio del Ambiente y Desarrollo Sostenible (MADES); la autoridad de puertos y navegación». Se presenta como caso ficticio; si se quieren usar cifras reales de nivel del río, hay que tomarlas de la Dirección de Meteorología e Hidrología con su fecha.',
            'Evaluación de impacto ambiental, definición breve para este encuentro: estudio que se hace antes de una obra para saber qué efectos puede tener sobre el ambiente y las personas, y cómo evitarlos o reducirlos. La ley que la regula se estudia en la Clase 21.',
            'El indicador 3 pide medidas «de gestión». No se espera un dictamen técnico: alcanza con una medida razonable (monitorear la calidad del agua, consultar a los pescadores, elegir la época del año).',
        ],
        'tarea': 'Terminar la conclusión si no se completó en clase.',
    },
    {
        'n': 30, 'encuentro': 30,
        'titulo': 'Evaluación de la Unidad 5 — Posición, relieve e hidrografía',
        'unidad': 'Unidad 5 — El espacio geográfico: posición, relieve e hidrografía',
        'material': 'Tomo: Evaluación de la Unidad 5',
        'capacidad': 'Integra las capacidades de la Unidad 5 (Clases 16 a 18 y Continuación F).',
        'tema': 'Evaluación de la Unidad 5.',
        'indicadores': [
            'Ubica el Paraguay, sus límites y sus principales ríos.',
            'Diferencia posición absoluta y posición relativa.',
            'Explica la relación entre la mediterraneidad y la Hidrovía.',
            'Explica la influencia del relieve en las actividades humanas, junto con otros factores.',
        ],
        'proposito': 'Comprobar qué lograron los estudiantes en la Unidad 5 y devolverles la corrección en el mismo encuentro, para que sepan qué deben reforzar.',
        'secuencia': [
            ('Inicio', [
                ('0–10', 'Explica la estructura de la prueba (Partes A y B del tomo y Parte C complementaria), el puntaje y el tiempo. No repasa contenidos.',
                 'Leen la prueba completa antes de empezar y preguntan dudas de consigna.', '—'),
            ]),
            ('Desarrollo', [
                ('10–55', 'Supervisa la resolución individual. Solo aclara consignas, no contenidos.',
                 'Resuelven las Partes A y B del tomo (8 ítems, 12 puntos).', 'Prueba del tomo.'),
                ('55–70', 'Entrega la Parte C complementaria (ver Precisiones).',
                 'Resuelven la Parte C: mapa y matriz breve (6 puntos).', 'Parte C.'),
                ('70–75', 'Retira las pruebas.', '—', 'Pruebas para corregir.'),
            ]),
            ('Cierre', [
                ('75–105', 'Corrección colectiva con la clave del solucionario, sin devolver todavía las pruebas: explica cada ítem y los errores esperables.',
                 'Anotan en una hoja aparte lo que creen haber respondido mal y por qué.', 'Hoja de autocorrección.'),
                ('105–120', 'Propone una actividad de refuerzo para el ítem con más dificultades (por ejemplo, posición absoluta y relativa con el mapa).',
                 'Resuelven el refuerzo en parejas.', 'Refuerzo.'),
            ]),
        ],
        'diversidad': [
            'Lectura en voz alta de las consignas para quien lo necesite.',
            'Tiempo adicional en la Parte C para estudiantes con apoyo; pueden resolverla en el encuentro siguiente.',
        ],
        'evaluacion': {
            'tipo': 'Sumativa de unidad, con devolución formativa.',
            'procedimientos': 'Prueba escrita; ubicación en mapa; matriz de impactos.',
            'instrumentos': 'Prueba de la Unidad 5 (tomo) más la Parte C complementaria; clave del solucionario.',
            'criterios': [
                'Total: 18 puntos (Partes A y B: 12; Parte C: 6). La calificación se obtiene con la escala de la institución.',
                'Parte C: 1 punto por cada elemento bien ubicado (4) y 1 punto por cada fila completa de la matriz (2).',
            ],
        },
        'precisiones': [
            'La prueba del tomo tiene 8 ítems y no evalúa la ubicación en el mapa ni las tres dimensiones de impacto, que los indicadores sí piden. Mientras no se amplíe el tomo, el docente agrega la Parte C, que entra en media hoja: «Parte C — 9. En el mapa esquemático del Paraguay, marcá el río Paraguay, el río Paraná, la represa de Itaipú y la ciudad de Asunción (4 puntos). 10. Completá una fila de la matriz Económico / Social / Ecológico para la Hidrovía con un beneficio y otra con un posible impacto (2 puntos)».',
            'El encabezado de la prueba en el tomo dice «posición y relieve», aunque la prueba también evalúa la hidrografía. Conviene corregirlo en el tomo.',
            'Ítem 6: la respuesta es «Paraguay», pero si un alumno aclara que el río es en parte límite con Brasil y con Argentina, la respuesta es igual de correcta (ver la Precisión del Plan 28).',
            'Ítem 8: se espera que el alumno mencione que el relieve llano facilita la agricultura, la ganadería y el transporte, pero también que no lo explica todo (el suelo, el clima y los mercados también influyen).',
        ],
        'tarea': 'Repasar el ítem con más errores con el apartado correspondiente del tomo.',
    },
    {
        'n': 31, 'encuentro': 31,
        'titulo': 'Clase 19 — El clima del Paraguay y de América',
        'unidad': 'Unidad 6 — Clima, regiones naturales y ambiente',
        'material': 'Tomo: Clase 19',
        'capacidad': 'Identifica las características climáticas y su influencia.',
        'tema': 'Elementos y factores del clima. Tipos de clima de América y del Paraguay.',
        'indicadores': [
            'Diferencia elementos y factores del clima.',
            'Reconoce los tipos de clima del Paraguay.',
            'Relaciona el clima con las actividades humanas.',
        ],
        'proposito': 'Que los estudiantes distingan tiempo atmosférico y clima, separen lo que se mide de lo que lo causa y expliquen por qué el Paraguay es más seco hacia el oeste.',
        'secuencia': [
            ('Inicio', [
                ('0–15', 'Pregunta cómo está el tiempo hoy y si esa descripción alcanza para decir cómo es el clima del Paraguay. Anota las respuestas.',
                 'Describen el tiempo del día y discuten la diferencia.', 'Ideas en la pizarra.'),
            ]),
            ('Desarrollo', [
                ('15–30', 'Lectura de «Tiempo atmosférico y clima». Da un par de ejemplos: «hoy llueve en Asunción» (tiempo) y «los veranos son calurosos y húmedos» (clima).',
                 'Resuelven las actividades 1, 5 y 8.', 'Actividades 1, 5 y 8.'),
                ('30–50', 'Lectura de «Elementos y factores» y de la caja «Concepto clave». Agrega la continentalidad como factor (ver Precisiones). Reparte ocho tarjetas o las escribe en la pizarra: temperatura, lluvia, humedad, viento, latitud, altitud, cercanía al agua, continentalidad.',
                 'En parejas clasifican las tarjetas en elementos y factores. Resuelven las actividades 2 y 6.', 'Clasificación; actividades 2 y 6.'),
                ('50–70', 'Lectura de «Los climas del Paraguay» y de la Figura 19.1. Presenta «Trabajá con la fuente» y aclara que la pregunta 2 se responde con el apartado leído, porque la fuente no habla de temperaturas.',
                 'Responden por escrito las tres preguntas de la fuente.', 'Respuestas de la fuente.'),
                ('70–85', 'Explica la consigna «Ubicate» con la corrección indicada en Precisiones.',
                 'Trazan el Trópico de Capricornio y marcan con una flecha y un degradé que las lluvias aumentan de oeste a este. Resuelven las actividades 3, 4, 9 y 10.', 'Mapa; actividades 3, 4, 9 y 10.'),
                ('85–100', 'Lectura de «El clima y la vida diaria» y de la caja «En Paraguay». Organiza grupos de 4.',
                 'Cada grupo completa un cuadro: cómo influye el clima en la ropa, la comida, la vivienda, los cultivos y los fenómenos extremos. Resuelven la actividad 7.', 'Cuadro del grupo; actividad 7.'),
            ]),
            ('Cierre', [
                ('100–112', 'Corrección oral de las actividades 1 a 10, con la clave corregida de la pregunta 3 de la fuente.',
                 'Corrigen con otro color.', 'Actividades corregidas.'),
                ('112–120', 'Boleto de salida: «¿Por qué el Chaco es más seco que la Región Oriental?». Asigna la tarea.',
                 'Responden en dos o tres líneas y anotan la tarea.', 'Boleto de salida.'),
            ]),
        ],
        'diversidad': [
            'Tarjetas con dibujo (termómetro, nube, montaña, mar) para quienes necesitan apoyo visual en la clasificación.',
            'Desafío: buscar en el pronóstico del día la temperatura de una ciudad del Chaco y de una de la Región Oriental y compararlas.',
        ],
        'evaluacion': {
            'tipo': 'Formativa.',
            'procedimientos': 'Clasificación de elementos y factores; análisis de fuente; mapa; boleto de salida.',
            'instrumentos': 'Lista de cotejo; actividades corregidas; boleto de salida.',
            'criterios': [
                'Clasifica correctamente al menos seis de las ocho tarjetas.',
                'Explica que las lluvias aumentan de oeste a este y lo representa en el mapa.',
                'Relaciona el clima con al menos dos aspectos de la vida diaria.',
            ],
        },
        'precisiones': [
            '«Ubicate»: el tomo pide colorear «de un lado del Trópico» la zona húmeda y «del otro» la seca. Es incorrecto: el Trópico de Capricornio cruza el país de este a oeste y atraviesa las dos regiones; el contraste de humedad es de oeste (Chaco, más seco) a este (Región Oriental, más húmeda). Consigna corregida: «Dibujá el Trópico de Capricornio. Después, con una flecha de oeste a este, indicá hacia dónde aumentan las lluvias y coloreá en degradé del Chaco a la Región Oriental». Hay que corregirla en el tomo.',
            'Pregunta 3 de la fuente: el solucionario actual responde «De diciembre a marzo», que no contesta la pregunta. Clave correcta: «Las lluvias aumentan de oeste a este. En la Región Oriental la época de lluvias va de la primavera a parte del otoño; el Chaco depende más de las lluvias del verano y tiene un invierno más seco».',
            'Factores del clima: además de los tres que nombra el tomo, conviene mencionar la continentalidad (el Paraguay está lejos del mar y eso acentúa las diferencias de temperatura entre el verano y el invierno) y los vientos (el viento norte, cálido, y el viento sur, frío).',
            'El tomo afirma que el tereré «nació como respuesta al calor»; su origen no está documentado con certeza. Conviene decir que «se asocia con el calor». Lo que inscribió la UNESCO en 2020 son las prácticas y saberes tradicionales, no las bebidas en sí.',
            'El título y el tema anuncian los tipos de clima de América, pero el tomo no los desarrolla (ver el informe de diagnóstico). Este plan no los da por enseñados.',
        ],
        'tarea': 'Actividades 11 y 12 de la Clase 19.',
    },
]
