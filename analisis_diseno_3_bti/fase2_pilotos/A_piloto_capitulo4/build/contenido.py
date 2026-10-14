# -*- coding: utf-8 -*-
"""Contenido del Capítulo 4 (piloto). Todo el texto es original; los nombres de
personas e instituciones son ficticios. Se declara como datos y lo consumen
build_capitulo4.py (libro del estudiante) y build_guia_docente.py (guía)."""

UNIDAD = 'Unidad 2 — Ingeniería de requisitos'
CAPITULO = 'Capítulo 4'
TITULO = 'Elicitación de requisitos: escuchar antes de diseñar'
ENCUENTROS = (7, 8)   # numeración de la estructura de referencia de 36 encuentros

CAPACIDAD = ('Aplica técnicas de elicitación para obtener, registrar y confirmar las necesidades '
             'de los interesados de un sistema de información.')
ROTULO_CAPACIDAD = 'Capacidad institucional (propuesta editorial; no es una capacidad oficial del MEC)'
TEMA = ('Interesados del sistema. Técnicas de elicitación. Entrevista: preparación, preguntas y registro. '
        'Hallazgos y requisitos candidatos. Ambigüedades y conflictos. Confirmación con el interesado.')
INDICADORES = [
    'Identifica a los interesados del sistema de la biblioteca y los ubica en un mapa de interés e influencia.',
    'Elabora un guion de entrevista con preguntas abiertas y cerradas, sin preguntas inductoras.',
    'Registra los hallazgos de una entrevista y los transforma en requisitos candidatos que indican su fuente.',
    'Detecta ambigüedades y conflictos entre interesados y propone cómo tratarlos sin decidir por ellos.',
]
TIEMPO = ('Dos encuentros (7 y 8 de la estructura de referencia). Cada encuentro corresponde a la carga '
          'semanal de la asignatura, 5 HC, que la institución puede organizar en una o más sesiones.')

# ------------------------------------------------------------------ apertura
APERTURA = [
    'En la Unidad 1 conociste la biblioteca del colegio tal como funciona hoy. Ahora empieza el trabajo '
    'central del analista: averiguar qué necesita cada persona que va a usar el sistema, o que se va a ver '
    'afectada por él. Ese trabajo se llama elicitación de requisitos.',
    'En este capítulo no vas a programar ni a diseñar tablas. Vas a preparar y analizar entrevistas, '
    'observar cómo se trabaja y convertir lo que la gente dice en una lista ordenada de requisitos '
    'candidatos. Es la materia prima de todo lo que viene después: si acá se escucha mal, el sistema '
    'resuelve el problema equivocado, por bien programado que esté.',
]

ARTICULACION = [
    'Con Algorítmica 3.º: en esa asignatura la biblioteca aparece como base de datos (tablas, claves, '
    'integridad). Acá trabajamos un paso antes, con las personas: todavía no se decide ninguna tabla.',
    'Con el prototipo integrador: los requisitos candidatos de este capítulo se especifican en el '
    'Capítulo 5, se priorizan en el Capítulo 6 y recién en la Unidad 5 se convierten en código.',
]

CASO = [
    'Durante todo el libro trabajamos con la biblioteca del Colegio Técnico Arapoty, un colegio ficticio. '
    'La atiende la Lic. Mirta Escobar, bibliotecaria. La directora es la Lic. Teresa Vega y el encargado '
    'de informática es el Sr. Ramón Ibarra. Todos los nombres, cifras y diálogos del caso son inventados '
    'para este libro.',
]

# ------------------------------------------------------------------ encuentro 7
E7_TITULO = 'Encuentro 7 — A quién escuchar y cómo preguntar'

S41 = ('4.1 Elicitar no es preguntar «¿qué quiere?»', [
    'Elicitar es obtener, junto con los interesados, las necesidades que un sistema debe atender. La palabra '
    'viene del inglés «elicit», que significa hacer salir algo que está escondido. Y eso es lo que pasa: '
    'casi nadie llega con sus necesidades ordenadas. La gente cuenta lo que le molesta, lo que hace todos '
    'los días y, muchas veces, la solución que se imagina.',
    'Por eso el analista distingue tres cosas que en una conversación aparecen mezcladas. La necesidad es '
    'lo que la persona tiene que lograr. El requisito es lo que el sistema debe hacer o cumplir para que '
    'lo logre. La solución es una forma concreta de construirlo. Si se salta directo a la solución, se '
    'pierde la necesidad, y con ella la posibilidad de encontrar una solución mejor o más barata.',
])

TABLA_NRS = (['Lo que dice el interesado', 'Necesidad', 'Requisito candidato', 'Solución (todavía no se decide)'],
             [['«Pierdo media hora buscando quién se llevó un libro.»',
               'Saber rápido quién tiene cada libro.',
               'El sistema debe mostrar quién tiene un libro prestado a partir de su título.',
               'Una página web, una planilla, una app…'],
              ['«Quiero una app para el celular.»',
               'Hay que preguntar: ¿para qué la quiere?',
               'Ninguno todavía: primero se averigua la necesidad.',
               'La app es una solución propuesta, no un requisito.'],
              ['«A fin de mes cuento a mano los préstamos de cada curso.»',
               'Entregar el informe mensual sin perder una tarde.',
               'El sistema debe generar el informe mensual de préstamos por curso.',
               'Un reporte impreso, un archivo para la dirección…']])

CONCEPTO_ELICITAR = ('Elicitación', [
    'Elicitar es obtener, registrar y confirmar con los interesados las necesidades que el sistema debe '
    'atender. Su producto no es el sistema ni su diseño, sino una lista de requisitos candidatos, cada uno '
    'con la fuente de donde salió.'])

S42 = ('4.2 Los interesados del sistema', [
    'Un interesado es toda persona o grupo que usa el sistema, decide sobre él o se ve afectado por sus '
    'resultados. En la biblioteca no es solo la bibliotecaria: también los estudiantes que piden libros, '
    'los docentes que organizan lecturas, la directora que aprueba el presupuesto y el encargado de '
    'informática que cuida las computadoras.',
    'No todos los interesados pesan igual ni quieren lo mismo. Para ordenarlos se usa un mapa de interés '
    'e influencia: el interés mide cuánto le importa el sistema en su trabajo diario; la influencia, '
    'cuánto puede decidir o bloquear. Según el cuadrante, cambia la forma de trabajar con cada uno.',
])

LEAD_FIG1 = ('Observá la figura: el eje horizontal mide el interés y el vertical la influencia. La '
             'bibliotecaria queda arriba a la derecha porque usa el sistema todos los días y su opinión '
             'decide; las familias quedan abajo a la izquierda porque casi no lo usan ni deciden sobre él.')
EPI_FIG1 = 'Figura 4.1 — Mapa de interés e influencia de los interesados de la biblioteca (Colegio Técnico Arapoty, caso ficticio).'

EJ1 = ('Ejemplo resuelto 4.1: el mapa de interesados de la biblioteca', [
    'Consigna: ubicar a seis interesados en el mapa y decidir cómo trabajar con cada uno. Se puntúa de 0 a '
    '10 el interés y la influencia, con una razón para cada puntaje.',
    'Paso 1. Listar a los interesados: bibliotecaria, estudiantes, docentes, directora, encargado de '
    'informática y familias.',
    'Paso 2. Puntuar con razones (ver la tabla siguiente). El puntaje no es exacto: lo importante es que '
    'cada número tenga una razón que otro compañero pueda discutir.',
    'Paso 3. Leer el cuadrante y decidir la estrategia. Con la bibliotecaria se trabaja de cerca, con '
    'entrevistas y revisiones frecuentes. A la directora se la mantiene satisfecha: se la consulta en las '
    'decisiones que la afectan, como el costo. A estudiantes y docentes se los mantiene informados y se '
    'los consulta con técnicas que llegan a muchos, como un cuestionario. A las familias se las observa.',
])

TABLA_EJ1 = (['Interesado', 'Interés', 'Influencia', 'Razón', 'Estrategia'],
             [['Bibliotecaria', '9', '8', 'Usa el sistema todo el día; nadie lo adopta si ella no lo acepta.', 'Gestionar de cerca'],
              ['Directora', '4', '9', 'No lo usa a diario, pero aprueba gastos y reglas.', 'Mantener satisfecha'],
              ['Encargado de informática', '2,5', '6,5', 'Decide qué se instala en las computadoras.', 'Mantener satisfecho'],
              ['Docentes', '6,5', '3,6', 'Piden lotes de libros para sus cursos.', 'Mantener informados'],
              ['Estudiantes', '8,5', '2,2', 'Son los que más piden libros; individualmente deciden poco.', 'Mantener informados'],
              ['Familias', '2,5', '1,5', 'Se enteran por sus hijos; no usan el sistema.', 'Observar']])

S43 = ('4.3 Técnicas de elicitación', [
    'No hay una técnica que sirva para todo. La entrevista profundiza con pocas personas; el cuestionario '
    'llega a muchas, pero con preguntas cerradas; la observación muestra lo que la gente hace, que no '
    'siempre coincide con lo que dice. Un buen analista combina al menos dos técnicas y compara lo que '
    'encuentra con cada una.',
])

TABLA_TECNICAS = (['Técnica', 'Sirve para…', 'Cuidado con…', 'En la biblioteca'],
                  [['Entrevista', 'Entender a fondo el trabajo y los problemas de una persona clave.', 'Preguntas inductoras; no tomar notas.', 'Entrevista a la bibliotecaria.'],
                   ['Observación directa', 'Ver cómo se trabaja de verdad, con tiempos y dificultades.', 'Molestar o cambiar la conducta del observado.', 'Mirar la atención en el primer recreo.'],
                   ['Cuestionario', 'Conocer la opinión de muchas personas en poco tiempo.', 'Preguntas confusas; muestras chicas.', 'Encuesta breve a estudiantes de todos los cursos.'],
                   ['Análisis de documentos', 'Conocer reglas, formularios e informes que ya existen.', 'Documentos viejos que ya no se aplican.', 'Reglamento de la biblioteca e informe mensual a la dirección.'],
                   ['Taller grupal', 'Reunir a varios interesados para generar ideas o acordar.', 'Que hable solo el que tiene más autoridad.', 'Reunión con delegados de curso y la bibliotecaria.']])

EN_PARAGUAY = ('Entrevistar en el idioma del interesado', [
    'La Constitución Nacional (art. 140) establece que el Paraguay es un país pluricultural y bilingüe, y '
    'que el castellano y el guaraní son idiomas oficiales. En una entrevista real, el interesado puede '
    'explicarse mejor en guaraní o en jopara. El analista no lo corrige: le permite hablar como se expresa '
    'mejor, anota la frase tal como se dijo y, al lado, su traducción. Así, quien lea después el registro '
    'puede volver a la expresión original si la traducción genera dudas.'])

S44 = ('4.4 Preparar y conducir una entrevista', [
    'Una entrevista se prepara. Antes de ir, el analista escribe el objetivo (qué quiere averiguar), '
    'averigua lo que ya se sabe y arma un guion: una lista ordenada de preguntas que va de lo general a lo '
    'particular. El guion no se lee como un examen; es una guía para no olvidar nada.',
    'Las preguntas abiertas («¿Cómo es un día normal en la biblioteca?») invitan a contar y descubren '
    'cosas que el analista no imaginaba. Las cerradas («¿Cuántos préstamos hay por día?») precisan datos. '
    'Se empieza con abiertas y se cierra con cerradas. Hay tres tipos de preguntas que se evitan: la '
    'inductora, que sugiere la respuesta; la doble, que pregunta dos cosas a la vez; y la técnica, que usa '
    'palabras que el interesado no conoce.',
    'Durante la entrevista, el analista escucha más de lo que habla, pide ejemplos concretos («¿Me cuenta '
    'la última vez que pasó?») y toma notas. Al terminar, resume lo que entendió y pregunta si falta algo. '
    'El mismo día pasa en limpio las notas, porque al día siguiente ya se olvidan detalles.',
])

TABLA_PREGUNTAS = (['Pregunta a evitar', 'Problema', 'Versión mejorada'],
                   [['¿No le parece que lo mejor sería una app?', 'Inductora: sugiere la respuesta.', '¿Cómo le gustaría consultar si un libro está disponible?'],
                    ['¿Cuántos libros presta y cuántos se pierden?', 'Doble: pregunta dos cosas.', 'Dos preguntas separadas.'],
                    ['¿Necesita un CRUD con base relacional?', 'Técnica: usa jerga.', '¿Qué datos anota hoy cuando presta un libro?'],
                    ['¿El sistema actual funciona mal, no?', 'Inductora y negativa.', '¿Qué le resulta más difícil del sistema actual?']])

EJ2 = ('Ejemplo resuelto 4.2: el guion de la entrevista a la bibliotecaria', [
    'Objetivo: entender cómo se registran hoy los préstamos y cuáles son los problemas más costosos para '
    'la bibliotecaria.',
    'Apertura: presentarse, explicar el objetivo, pedir permiso para tomar notas y anunciar la duración '
    'aproximada.',
    'Preguntas abiertas:\n1. ¿Cómo es un día normal en la biblioteca?\n2. ¿Qué pasa cuando un libro no vuelve?\n'
    '3. ¿Qué le pide la dirección y cómo lo prepara?',
    'Preguntas para precisar:\n4. ¿Cómo sabe hoy si un libro está disponible?\n5. ¿Cuántos préstamos hay en '
    'un día de mucho movimiento?\n6. ¿Cuánto tarda en preparar el informe mensual?',
    'Cierre:\n7. Si pudiera cambiar una sola cosa, ¿cuál sería?\n8. ¿Hay algo que no le pregunté y que '
    'debería saber?',
    'Por qué está bien armado: empieza con preguntas abiertas, después precisa con cerradas y cierra '
    'dejando lugar a lo inesperado (pregunta 8). Ninguna pregunta sugiere la respuesta ni nombra una '
    'tecnología.',
])

LEAD_FIG2 = ('Seguí las flechas: la elicitación avanza en cinco pasos, pero no es una línea recta. La '
             'flecha punteada muestra que, si al confirmar el interesado corrige algo, se vuelve a obtener '
             'información.')
EPI_FIG2 = 'Figura 4.2 — El proceso de elicitación y su retorno.'

ACT_E7 = [
    ('Ejercitá', [
        'Clasificá cada frase como necesidad, requisito candidato o solución:\n'
        '(a) «Tengo que saber qué libros están atrasados.»\n'
        '(b) «Quiero un lector de código de barras.»\n'
        '(c) «El sistema debe registrar la fecha de devolución de cada préstamo.»\n'
        '(d) «Necesito que los chicos no hagan fila en el recreo.»\n'
        '(e) «Hagan una página con fondo verde.»\n'
        '(f) «El sistema debe listar los préstamos vencidos.»',
        'Marcá si cada pregunta es abierta, cerrada o inductora:\n'
        '(a) ¿Cuántas computadoras tiene la biblioteca?\n'
        '(b) ¿Cómo organiza los libros en los estantes?\n'
        '(c) ¿Verdad que sería mejor que todo esté en la computadora?\n'
        '(d) ¿En qué horario hay más estudiantes?\n'
        '(e) ¿Qué hace cuando un estudiante no devuelve un libro?',
    ]),
    ('Resolvé', [
        'Agregá al mapa de la Figura 4.1 dos interesados que no aparecen. Para cada uno, escribí su puntaje '
        'de interés e influencia con una razón, y la estrategia que corresponde.',
        'Escribí un guion de seis preguntas para entrevistar a un estudiante de 1.º que usa poco la '
        'biblioteca. Empezá con abiertas, terminá con cerradas y no nombres ninguna tecnología.',
    ]),
    ('Pensá y decidí', [
        'Elegí la técnica más adecuada para cada situación y justificá en una línea:\n'
        '(a) Saber cuántos estudiantes de toda la institución leerían más si pudieran reservar.\n'
        '(b) Saber por qué el primer recreo es el momento más difícil.\n'
        '(c) Conocer las reglas de préstamo vigentes.\n'
        '(d) Acordar entre la bibliotecaria y los delegados el horario de atención.',
    ]),
    ('Desafío', [
        'Reescribí estas tres preguntas para que no sean inductoras, dobles ni técnicas:\n'
        '(a) ¿No sería mejor que los estudiantes reserven desde el celular?\n'
        '(b) ¿Qué libros se piden más y en qué meses?\n'
        '(c) ¿Le alcanzaría con un login por usuario?',
    ]),
]

# ------------------------------------------------------------------ encuentro 8
E8_TITULO = 'Encuentro 8 — Del registro al requisito candidato'

S45 = ('4.5 El registro de la entrevista', [
    'El registro es el documento que queda de la entrevista. Se numeran las líneas para poder citarlas: '
    '«E1-L4» significa entrevista 1, línea 4. Después, cada frase importante se clasifica en una de cuatro '
    'categorías. Un hecho describe cómo funcionan las cosas hoy. Un problema es algo que sale mal o cuesta '
    'demasiado. Una necesidad es lo que la persona tiene que lograr. Una propuesta es una solución que el '
    'interesado imagina.',
    'Las propuestas no se descartan, pero tampoco se copian como requisitos: se pregunta qué necesidad hay '
    'detrás. Y si una propuesta apareció porque el analista la sugirió, no vale como dato: es un error de '
    'la entrevista, y se vuelve a preguntar de otra manera.',
])

TRANSCRIPCION_E1 = ('Registro E1 — Entrevista a la Lic. Mirta Escobar, bibliotecaria (caso ficticio)', [
    'L1  Analista: ¿Cómo es un día normal en la biblioteca?',
    'L2  Mirta: Abro a las siete, y en el primer recreo se llena. Anoto los préstamos en un cuaderno; cuando hay fila, anoto apurada y después no entiendo mi letra.',
    'L3  Analista: ¿Qué pasa cuando un libro no vuelve?',
    'L4  Mirta: Tengo que hojear el cuaderno hacia atrás hasta encontrar quién lo llevó. A veces tardo media hora. A fin de año faltan unos cuarenta libros y no sé quién los tiene.',
    'L5  Analista: ¿Cómo sabe hoy si un libro está disponible?',
    'L6  Mirta: Voy al estante. Si no está, puede estar prestado, mal ubicado o perdido.',
    'L7  Analista: ¿Qué le pide la dirección?',
    'L8  Mirta: Un informe a fin de cada mes con cuántos préstamos hubo por curso. Lo hago contando a mano y me lleva una tarde.',
    'L9  Analista: Si pudiera cambiar una sola cosa, ¿cuál sería?',
    'L10 Mirta: Saber al instante quién tiene cada libro. Y que el sistema sea fácil, porque yo no soy de computadoras.',
    'L11 Analista: ¿No le parece que conviene una aplicación para el celular?',
    'L12 Mirta: Si usted dice… sí, capaz.',
])

EJ3 = ('Ejemplo resuelto 4.3: del registro a los hallazgos', [
    'Consigna: leer el registro E1, extraer los hallazgos y clasificarlos. Cada hallazgo lleva un código '
    '(H1, H2…) y la línea de donde sale.',
    'Cómo se hizo: se leyó cada respuesta de Mirta, se subrayaron las frases que describen algo (hecho), '
    'algo que sale mal (problema), algo que hay que lograr (necesidad) o una solución (propuesta). Las '
    'cifras se anotan tal como se dijeron, marcadas «a verificar», porque son estimaciones de la '
    'entrevistada.',
])

TABLA_HALLAZGOS = (['Cód.', 'Fuente', 'Hallazgo', 'Tipo'],
                   [['H1', 'E1-L2', 'Los préstamos se anotan a mano en un cuaderno.', 'Hecho'],
                    ['H2', 'E1-L2', 'Con fila, la letra queda ilegible y después no se entiende.', 'Problema'],
                    ['H3', 'E1-L4', 'Encontrar quién tiene un libro puede llevar media hora.', 'Problema'],
                    ['H4', 'E1-L4', 'Faltan unos 40 libros por año y no se sabe quién los tiene (a verificar con el inventario).', 'Problema'],
                    ['H5', 'E1-L6', 'No se distingue un libro prestado de uno mal ubicado o perdido.', 'Problema'],
                    ['H6', 'E1-L8', 'La dirección pide un informe mensual de préstamos por curso; hoy lleva una tarde.', 'Necesidad'],
                    ['H7', 'E1-L10', 'Saber al instante quién tiene cada libro.', 'Necesidad'],
                    ['H8', 'E1-L10', 'Que el sistema sea «fácil» para alguien que no es de computadoras.', 'Necesidad (ambigua)'],
                    ['H9', 'E1-L11/12', 'Aplicación para el celular: la sugirió el analista.', 'No vale como dato']])

S46 = ('4.6 Redactar requisitos candidatos', [
    'Un requisito candidato es una primera versión de un requisito: todavía no está revisado ni aprobado, '
    'pero ya dice qué debe hacer el sistema y de dónde salió. Se redacta con una forma fija: «El sistema '
    'debe [acción] [objeto] [condición, si la hay]». Lleva un código (RC-01, RC-02…), la lista de '
    'hallazgos que lo originan y un tipo preliminar: funcional, si describe algo que el sistema hace; no '
    'funcional, si describe cómo debe ser (fácil, rápido, seguro).',
    'La trazabilidad, es decir poder seguir cada requisito hasta su fuente, es lo que permite discutirlo '
    'después. Si alguien pregunta «¿quién pidió esto?», la respuesta está en la tabla, no en la memoria '
    'del analista.',
])

CONCEPTO_RC = ('Requisito candidato', [
    'Es una necesidad traducida a lo que el sistema debe hacer o cumplir, con un código, su fuente y un '
    'tipo preliminar. Es candidato porque todavía falta especificarlo (Capítulo 5) y priorizarlo con los '
    'interesados (Capítulo 6).'])

EJ4 = ('Ejemplo resuelto 4.4: de los hallazgos a los requisitos candidatos', [
    'Consigna: redactar los requisitos candidatos que surgen de los hallazgos H1 a H9.',
    'Cómo se hizo: cada problema o necesidad se tradujo en una acción del sistema. H1 es un hecho y no '
    'genera requisito por sí solo, pero da contexto a RC-01. H9 no genera ningún requisito: la app la '
    'sugirió el analista, así que en la próxima entrevista se pregunta «¿cómo le gustaría consultar…?». '
    'H8 genera un requisito no funcional que todavía es ambiguo: se marca para resolver en 4.7.',
])

TABLA_RC = (['Código', 'Requisito candidato', 'Origen', 'Tipo preliminar'],
            [['RC-01', 'El sistema debe registrar cada préstamo con el lector, el libro y la fecha de salida.', 'H1, H2', 'Funcional'],
             ['RC-02', 'El sistema debe mostrar quién tiene un libro prestado a partir de su título.', 'H3, H7', 'Funcional'],
             ['RC-03', 'El sistema debe indicar si cada libro está disponible o prestado.', 'H5', 'Funcional'],
             ['RC-04', 'El sistema debe listar los préstamos que todavía no se devolvieron.', 'H4', 'Funcional'],
             ['RC-05', 'El sistema debe generar el informe mensual de préstamos por curso.', 'H6', 'Funcional'],
             ['RC-06', 'El sistema debe ser fácil de usar para la bibliotecaria (ambiguo: ver 4.7).', 'H8', 'No funcional']])

S47 = ('4.7 Ambigüedades y conflictos', [
    'Un requisito es ambiguo cuando dos personas pueden entenderlo de manera distinta. Las palabras que '
    'suelen delatarlo son «fácil», «rápido», «amigable», «siempre», «todos», «etcétera» y «adecuado». '
    'Para resolver la ambigüedad se le pregunta al interesado qué significa para él, y se busca una '
    'condición que se pueda comprobar: un tiempo, una cantidad, una tarea que alguien puede hacer o no.',
    'Por ejemplo, RC-06 dice «fácil de usar». Si se le pregunta a Mirta, puede responder: «Que yo pueda '
    'registrar un préstamo sola, sin llamar a nadie». Con eso se reescribe: «La bibliotecaria debe poder '
    'registrar un préstamo sin ayuda después de una capacitación de una hora». Ahora se puede comprobar.',
    'Un conflicto aparece cuando dos interesados piden cosas incompatibles. El analista no decide quién '
    'gana: registra las dos posiciones, busca la necesidad que hay detrás de cada una y lleva el conflicto '
    'a quien tiene autoridad para resolverlo, con opciones. La decisión se toma al priorizar (Capítulo 6).',
])

EJ5 = ('Ejemplo resuelto 4.5: un conflicto sobre el plazo de préstamo', [
    'Situación: los delegados de curso piden préstamos de 14 días; la bibliotecaria quiere mantener 7 '
    'días porque «si no, los libros no vuelven».',
    'Paso 1. Registrar las dos posiciones con su fuente (por ejemplo, T1-L3 para el taller con delegados '
    'y E1-L4 para la entrevista a la bibliotecaria).',
    'Paso 2. Buscar la necesidad detrás de cada una. Delegados: terminar de leer novelas largas sin '
    'apuro. Bibliotecaria: que los libros vuelvan y circulen.',
    'Paso 3. Proponer opciones sin elegir: (a) 7 días con una renovación; (b) 14 días solo para novelas '
    'de más de 200 páginas; (c) 7 días y aviso automático de vencimiento.',
    'Paso 4. Elevar a la directora, que tiene la autoridad, con las tres opciones y sus ventajas. El '
    'requisito queda pendiente con la marca «en conflicto».',
])

S48 = ('4.8 Confirmar con el interesado', [
    'El último paso es la devolución: se le muestra al interesado la lista de hallazgos y requisitos '
    'candidatos, y se le pregunta si eso es lo que quiso decir. Puede ser una reunión corta o una hoja '
    'que lee y firma. Si corrige algo, se vuelve a obtener información (la flecha punteada de la Figura '
    '4.2). Confirmar evita el error más caro del desarrollo de sistemas: construir algo que nadie pidió.',
])

ACT_E8 = [
    ('Ejercitá', [
        'Subrayá la palabra ambigua y proponé una versión que se pueda comprobar:\n'
        '(a) «El sistema debe responder rápido.»\n'
        '(b) «Todos los usuarios deben poder entrar.»\n'
        '(c) «El informe debe mostrar los datos adecuados.»\n'
        '(d) «La búsqueda debe ser amigable.»',
    ]),
    ('Resolvé', [
        'En la tabla del Ejemplo resuelto 4.4 falta un requisito candidato que se deduce del registro E1: '
        'cuando un libro vuelve, algo tiene que quedar anotado. Redactalo con código, origen y tipo.',
        'Escribí la hoja de confirmación para Mirta: un título, los seis requisitos candidatos con '
        'palabras que ella entienda y dos preguntas para cerrar las dudas pendientes.',
    ]),
    ('Pensá y decidí', [
        'La directora dice: «No hay presupuesto para comprar computadoras nuevas». Los estudiantes, en el '
        'cuestionario, piden «consultar desde el celular si un libro está». Explicá si hay conflicto, '
        'cuál es la necesidad de cada uno y qué le preguntarías al encargado de informática.',
    ]),
    ('Desafío', [
        'Reescribí la línea L11 del registro E1 para que no sea inductora. Después explicá qué perdió el '
        'analista al preguntar como preguntó.',
    ]),
]

# ------------------------------------------------------------------ práctica diferenciada
PRACTICA_TITULO = 'Práctica 4 — El plan lector: elicitar con una docente'
PRACTICA_INTRO = [
    'Trabajás con un interesado nuevo del caso: la Prof. Estela Duarte, docente de Castellano, que organiza '
    'el plan lector. Tenés su entrevista (registro E2) y una nota de observación en la biblioteca (registro '
    'O1). Elegí el nivel que te indique tu docente o el que te animes a hacer. Los tres niveles trabajan '
    'sobre los mismos registros; cada uno pide un poco más que el anterior.',
]

TRANSCRIPCION_E2 = ('Registro E2 — Entrevista a la Prof. Estela Duarte, docente de Castellano (caso ficticio)', [
    'L1  Analista: ¿Para qué usa la biblioteca con sus cursos?',
    'L2  Estela: Para el plan lector: cada mes todo el curso lee la misma novela. Necesito treinta ejemplares juntos.',
    'L3  Analista: ¿Cómo lo hace hoy?',
    'L4  Estela: Le pido a Mirta con una semana de anticipación. Ella cuenta los ejemplares en el estante y a veces faltan cinco o seis.',
    'L5  Analista: ¿Qué pasa cuando faltan?',
    'L6  Estela: Algunos chicos leen en fotocopias o en el celular, y se atrasan.',
    'L7  Analista: ¿Cuánto tiempo necesita los libros?',
    'L8  Estela: Tres semanas, como mínimo. Y lo ideal sería que nadie más pueda llevar ese título mientras tanto.',
    'L9  Analista: ¿Hay otra cosa que le complique?',
    'L10 Estela: Cuando devuelven, Mirta tiene que contar uno por uno, y siempre aparece alguno que no es de la biblioteca.',
    'L11 Estela: Ah, y el sistema tiene que ser rápido.',
])

OBSERVACION_O1 = ('Registro O1 — Observación en la biblioteca, martes, primer recreo (caso ficticio)', [
    'Al tocar el timbre de salida al recreo había 14 estudiantes en fila.',
    'La bibliotecaria registró 9 préstamos en el cuaderno durante el recreo.',
    '5 estudiantes se fueron sin libro cuando tocó el timbre de entrada.',
    '2 estudiantes pidieron un libro que según la bibliotecaria «tenía que estar», y no estaba en el estante.',
])

NIVELES = [
    ('Nivel 1 — Guiado', [
        'Clasificá cada fragmento como hecho, problema, necesidad o propuesta, y anotá su fuente (E2-L…):\n'
        '(a) «cada mes todo el curso lee la misma novela»\n'
        '(b) «a veces faltan cinco o seis»\n'
        '(c) «Necesito treinta ejemplares juntos»\n'
        '(d) «Algunos chicos leen en fotocopias o en el celular, y se atrasan»\n'
        '(e) «Tres semanas, como mínimo»\n'
        '(f) «que nadie más pueda llevar ese título mientras tanto»\n'
        '(g) «Mirta tiene que contar uno por uno»\n'
        '(h) «el sistema tiene que ser rápido»',
        'Completá estos tres requisitos candidatos:\n'
        'RC-21 El sistema debe permitir que un docente solicite ________ ejemplares de un mismo título para su curso. Origen: ______\n'
        'RC-22 El sistema debe indicar cuántos ejemplares de un título están ________ en una fecha. Origen: ______\n'
        'RC-23 El sistema debe registrar la ________ de cada ejemplar de un lote. Origen: ______',
    ]),
    ('Nivel 2 — Intermedio', [
        'Armá la tabla de hallazgos de E2 y O1 (código, fuente, hallazgo, tipo). Incluí al menos dos '
        'hallazgos de la observación.',
        'Redactá cinco requisitos candidatos con código, origen y tipo preliminar. Al menos uno debe salir '
        'de la observación O1.',
        'Encontrá las dos expresiones ambiguas de E2 y proponé para cada una una versión comprobable y la '
        'pregunta que le harías a la docente para confirmarla.',
    ]),
    ('Nivel 3 — Ampliación', [
        'Detectá el conflicto entre lo que pide la docente (E2-L8) y lo que necesitan los demás lectores '
        'y la bibliotecaria. Describí la necesidad que hay detrás de cada posición.',
        'Proponé dos opciones para tratar el conflicto, con una ventaja y una desventaja de cada una, sin '
        'elegir. Indicá quién debería decidir.',
        'Diseñá un cuestionario de seis preguntas para los estudiantes de los cursos que participan del '
        'plan lector: cuatro cerradas y dos abiertas, ninguna inductora.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: cada hallazgo y cada requisito tiene una fuente que otro compañero '
                    'puede encontrar en los registros; ningún requisito nombra una tecnología; ninguna '
                    'propuesta de la docente quedó copiada como requisito sin buscar la necesidad que la '
                    'origina.')

CALENDARIO_REDUCIDO = ('Si el capítulo se da en un solo encuentro', [
    'Lectura previa en casa: 4.1, 4.2 y 4.3.',
    'Actividad central, que no se omite: el Ejemplo resuelto 4.3 y la Práctica 4 en el Nivel 1 o el '
    'Nivel 2.',
    'Se trabajan en clase en forma breve: 4.4 (con la tabla de preguntas a evitar) y 4.7.',
    'Quedan como lectura domiciliaria: 4.8 y las actividades «Pensá y decidí» y «Desafío» de ambos '
    'encuentros.',
])

REPASO = ('Para repasar', [
    'Elicitar es obtener, registrar y confirmar necesidades con los interesados, no preguntar «¿qué quiere?».',
    'El mapa de interés e influencia ordena a los interesados y define cómo trabajar con cada uno.',
    'Se combinan técnicas: la entrevista profundiza, la observación muestra lo que realmente pasa y el '
    'cuestionario llega a muchos.',
    'Cada hallazgo y cada requisito candidato lleva su fuente.',
    'Las palabras ambiguas se reemplazan por condiciones comprobables; los conflictos se registran y se '
    'elevan, no se deciden a escondidas.',
])

# ------------------------------------------------------------------ evaluación
EVAL_ID = 'ADS3-C4-1'   # semilla del barajado: reparte las claves en a, b, c y d
EVAL_TITULO = 'Evaluación del Capítulo 4'
EVAL_TEXTO_BASE = ('Texto base — Registro E3: entrevista a Iván Ortellado, delegado de 2.º BTI (caso ficticio)', [
    'L1 Iván: Vengo a buscar un libro y no sé si está.',
    'L2 Iván: Pierdo el recreo esperando en la fila para que me digan que está prestado.',
    'L3 Iván: Me gustaría saber antes de venir si lo hay.',
    'L4 Iván: Y que se pueda renovar el préstamo sin traer el libro.',
])
EVAL_ITEMS = [
    ('mc', '¿Qué es elicitar requisitos?',
     ['Obtener, registrar y confirmar con los interesados las necesidades que el sistema debe atender.',
      'Programar las funciones que pide el cliente.',
      'Elegir el lenguaje de programación y la base de datos.',
      'Escribir el manual de usuario del sistema.']),
    ('mc', '¿Cuál de estas preguntas es inductora?',
     ['¿No le parece que lo mejor sería una aplicación para el celular?',
      '¿Cómo registra hoy los préstamos?',
      '¿Cuántos préstamos hay en un día de mucho movimiento?',
      '¿Qué hace cuando un libro no vuelve?']),
    ('mc', '¿Qué técnica conviene para ver cómo se atiende a los estudiantes en el primer recreo?',
     ['La observación directa en la biblioteca durante el recreo.',
      'Un cuestionario a las familias.',
      'El análisis del reglamento de la biblioteca.',
      'Una entrevista a la directora.']),
    ('mc', 'Un interesado con mucha influencia y poco interés diario en el sistema se debe…',
     ['mantener satisfecho, consultándolo en las decisiones que lo afectan.',
      'gestionar de cerca, con entrevistas semanales.',
      'ignorar, porque no usa el sistema.',
      'mantener informado solo al final del proyecto.']),
    ('vf', 'Una propuesta de solución del interesado («quiero una app») es un requisito y se copia tal cual en la lista.',
     False, 'Falso. Es una propuesta: se pregunta qué necesidad hay detrás y recién de ahí sale el requisito.'),
    ('vf', 'Cada requisito candidato debe indicar de qué entrevista, observación o documento salió.',
     True, 'Verdadero. Es la trazabilidad, que permite discutir y confirmar cada requisito.'),
    ('vf', 'Cuando dos interesados piden cosas incompatibles, el analista elige la mejor y descarta la otra.',
     False, 'Falso. El analista registra ambas posiciones, busca las necesidades y eleva el conflicto con opciones a quien decide.'),
    ('ab', 'Reescribí «El sistema tiene que ser rápido» como un requisito que se pueda comprobar.',
     'Toda versión con una condición medible y una situación concreta. Ejemplo: «La búsqueda de un título debe '
     'mostrar el resultado en menos de 3 segundos en las computadoras de la biblioteca». Se acepta otra cifra '
     'si se aclara que hay que confirmarla con el interesado.', 3),
    ('ab', 'Con el registro E3 del texto base: anotá un problema y una necesidad con su fuente (E3-L…), y '
           'redactá un requisito candidato con código, origen y tipo.',
     'Problema: pierde el recreo en la fila para enterarse de que el libro está prestado (E3-L2). Necesidad: '
     'saber si un libro está disponible antes de ir (E3-L3). Requisito candidato, por ejemplo: «RC-30 El '
     'sistema debe permitir consultar la disponibilidad de un título sin acercarse al mostrador. Origen: E3-L1, '
     'E3-L2, E3-L3. Funcional.» También vale un requisito de renovación (E3-L4). No vale nombrar una tecnología '
     '(«una app») como requisito.', 5),
]
