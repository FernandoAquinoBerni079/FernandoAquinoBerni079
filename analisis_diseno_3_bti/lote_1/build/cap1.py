# -*- coding: utf-8 -*-
"""Capítulo 1 — «Un sistema comienza con una necesidad» (Work §6: secciones 1.1 a 1.4; encuentros 1 y 2).
Texto original. Las fuentes citadas (D0-1…) existen en caso/dossier.py; las de la práctica (V-01…), en
caso/mbokaja.py. El mapa de interesados (sección 1.3) se trasladó del candidato del Capítulo 2."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'caso'))
import dossier as D
import mbokaja as MB

NUM = 1
UNIDAD = 'Unidad I — Comprender el problema y su contexto'
CAPITULO = 'Capítulo 1'
TITULO = 'Un sistema comienza con una necesidad'
ENCUENTROS = (1, 2)
SECCIONES = ['1.1 De la dificultad cotidiana al problema de información',
             '1.2 Personas, procesos, datos, recursos y límites del sistema',
             '1.3 Actores e interesados: necesidades diferentes, decisiones compartidas',
             '1.4 Diagnóstico de conocimientos previos y plan de apoyo']
PRACTICA_WORK = 'describir una biblioteca y separar hechos, supuestos y soluciones anticipadas'

ROTULO_CAPACIDAD = ('Capacidades propuestas para el programa institucional (C1 y C7, en parte; no son capacidades '
                    'oficiales del MEC)')
CAPACIDAD = ('C1. Delimita un problema y evalúa la factibilidad de una solución.\n'
             'C7, en parte. Organiza y registra el trabajo colaborativo (acuerdo de trabajo y plan de apoyo).')
TEMA = ('Dificultad, problema de información y solución anticipada. Hechos y supuestos. Personas, procesos, datos, '
        'recursos y límites de un sistema. Actores e interesados; mapa de interés e influencia. Diagnóstico de '
        'conocimientos previos y plan de apoyo.')
INDICADORES = [
    'Distingue una dificultad cotidiana del problema de información que la explica y de una solución anticipada.',
    'Describe un sistema de información con sus personas, procesos, datos, recursos y límites.',
    'Identifica actores e interesados, con sus necesidades y su influencia en las decisiones.',
    'Separa hechos, supuestos y soluciones anticipadas en la descripción de una situación.',
    'Reconoce sus conocimientos previos y acuerda un plan de apoyo y las reglas de trabajo del equipo.',
]
TIEMPO = 'Dos encuentros de 5 HC (1 y 2 de la secuencia anual). Las 5 HC pueden repartirse en varios bloques semanales.'

APERTURA = [
    'Un sistema no empieza con un programa. Empieza cuando alguien tiene una dificultad que se repite: una fila que '
    'no avanza, un libro que nadie sabe quién tiene, una tarde entera contando préstamos. Antes de pensar en '
    'pantallas o en bases de datos, el analista tiene que entender esa dificultad, a quién afecta y qué parte de '
    'ella se puede mejorar con información.',
    'En este capítulo recibís el pedido que da origen al proyecto del año: la dirección del Colegio Técnico Arapoty '
    'le pide al curso que estudie el problema de su biblioteca. Vas a aprender a convertir ese pedido en un problema '
    'bien planteado, a describir el sistema que ya existe y a reconocer a las personas que tienen algo que decir. '
    'También vas a revisar tu punto de partida y a acordar cómo va a trabajar tu equipo.',
]
ARTICULACION = [
    'Con los preliminares: el diagnóstico de entrada, el acuerdo de trabajo y la presentación del caso se usan en '
    'el Encuentro 1.',
    'Con el Capítulo 2: muchas afirmaciones de este capítulo quedan marcadas «a verificar». El relevamiento del '
    'Capítulo 2 las confirma o las corrige.',
    'Con Algorítmica y Laboratorio: en 1.2, «datos» quiere decir qué información usa cada persona. Las tablas y los '
    'campos se diseñan recién en la Unidad III.',
]

# ------------------------------------------------------------------ encuentro 1
E1_TITULO = 'Encuentro 1 — El reto y el sistema que ya existe'

S11 = ('1.1 De la dificultad cotidiana al problema de información', [
    'El proyecto del año empieza con una nota de la dirección. Su primer párrafo dice: «La biblioteca registra los '
    'préstamos en un cuaderno, y cada vez cuesta más saber qué libros hay y quién los tiene.» (D0-1). Es una '
    'dificultad cotidiana: la vive la bibliotecaria cuando busca un libro, el lector cuando no lo encuentra y la '
    'dirección cuando necesita un dato. Pero una dificultad todavía no es un problema planteado.',
    'Lo primero que se ve de una dificultad es su síntoma: la fila, la demora, el enojo. El analista pregunta qué '
    'hay detrás. Hay un problema de información cuando a alguien le falta un dato que necesita, o lo recibe tarde, '
    'o no puede confiar en él, o no le llega a quien tiene que decidir. «No saber quién tiene un libro» es un '
    'problema de información. «No tener libros suficientes» no lo es: ningún registro, por bueno que sea, compra '
    'libros. Delimitar el problema es decir qué parte de la dificultad se puede mejorar con información.',
    'En cualquier relato de una situación aparecen mezcladas tres clases de afirmaciones. Un hecho es algo que se '
    'puede comprobar y tiene una fuente: que la dirección escribió la nota es un hecho. Un supuesto es algo que '
    'creemos sin haberlo comprobado todavía: «hay fila porque los lectores no saben qué libros hay» puede ser '
    'cierto, pero hasta que se observe y se pregunte es un supuesto. Una solución anticipada es una propuesta que '
    'aparece antes de entender el problema: «Algunos docentes sugieren comprar lectores de códigos de barras.» '
    '(D0-4).',
    'Las soluciones anticipadas no se descartan ni se adoptan: se registran, y se pregunta qué problema '
    'resolverían. Un lector de códigos de barras hace más rápido anotar qué libro sale, pero no dice si un libro '
    'está disponible ni produce el informe mensual. Si el equipo la adopta antes de entender el problema, puede '
    'gastar en algo que no ataca la causa.',
])

TABLA_11 = (['Categoría', 'Qué es', 'Ejemplo del caso', 'Qué hace el analista'],
            [['Síntoma', 'Lo que se ve de la dificultad', 'Cuesta saber qué libros hay (D0-1)', 'Pregunta qué hay detrás'],
             ['Problema de información', 'Falta un dato, llega tarde, no es confiable o no llega a quien decide', 'No se sabe con certeza quién tiene cada libro', 'Lo enuncia y lo verifica'],
             ['Problema que no es de información', 'Una falta que ningún registro resuelve', 'Pocos ejemplares de un título muy pedido', 'Lo deja fuera del sistema y lo informa'],
             ['Solución anticipada', 'Una propuesta anterior al análisis', 'Lectores de códigos de barras (D0-4)', 'La registra y pregunta qué resuelve']])

CONCEPTO_PROBLEMA = ('Problema de información', [
    'Situación en la que una persona o un grupo no cuenta con la información que necesita para hacer su tarea o '
    'tomar una decisión: porque no existe, llega tarde, no es confiable o no le llega. Se enuncia sin nombrar una '
    'solución y con la evidencia que lo respalda.'])

EJ11 = ('Ejemplo resuelto 1.1: del pedido de la dirección a la ficha de problema', [
    'Consigna: leer la nota de la dirección (D0, en la presentación del caso), clasificar cada párrafo y armar una '
    'primera ficha de problema.',
    'Paso 1. Clasificar. D0-1 describe una dificultad y la atribuye al cuaderno: es un hecho que la dirección lo '
    'afirma; cuánto cuesta y a quién, todavía hay que averiguarlo. D0-2 y D0-6 son el encargo y su plazo. D0-3 fija '
    'lo mínimo que la dirección espera. D0-4 es una solución anticipada. D0-5 es una condición: cuidar los datos y '
    'contar con la conformidad de la bibliotecaria.',
    'Paso 2. Separar lo que sabemos de lo que suponemos. Sabemos lo que dice la nota. Suponemos, por ejemplo, que la '
    'fila del recreo se debe a que nadie sabe qué hay disponible. Cada supuesto se anota con la marca «a verificar».',
    'Paso 3. Completar la ficha (Tabla 1.2). Cada fila indica su fuente o su estado.',
    'Paso 4. Enunciar el problema en una sola oración, sin nombrar una solución: «En la biblioteca del Colegio '
    'Técnico Arapoty, la bibliotecaria, los lectores y la dirección no cuentan con información confiable y a tiempo '
    'sobre qué ejemplares están disponibles, quién tiene cada uno y cuántos préstamos hubo por curso, porque los '
    'préstamos se registran en un cuaderno.» Fuentes: D0-1 y D0-3. Estado: a verificar en el relevamiento.',
])

TABLA_12 = (['Elemento de la ficha', 'Contenido para el caso', 'Fuente o estado'],
            [['Quién tiene la dificultad', 'La bibliotecaria, los lectores y la dirección', 'D0-1, D0-3'],
             ['Qué información falta o no es confiable', 'Qué ejemplares hay disponibles, quién tiene cada uno, cuántos préstamos hubo por curso', 'D0-1, D0-3'],
             ['En qué situación aparece', 'Al prestar en el recreo, al buscar un libro que no vuelve, al preparar el informe mensual', 'Supuesto: a verificar'],
             ['Qué consecuencia tiene', 'Tiempo perdido y libros que no se sabe quién tiene', 'D0-1; la magnitud, a verificar'],
             ['Qué condiciones pone la institución', 'Una mejora que el colegio pueda sostener, que cuide los datos y que acepte la bibliotecaria', 'D0-2, D0-5'],
             ['Qué soluciones se anticiparon', 'Lectores de códigos de barras: se registra, no se adopta', 'D0-4'],
             ['Qué falta averiguar', 'Cómo se registra hoy, cuántos préstamos hay, qué necesita cada persona', 'Relevamiento (Capítulo 2)']])

S12 = ('1.2 Personas, procesos, datos, recursos y límites del sistema', [
    'Un sistema es un conjunto de elementos que se relacionan para cumplir un propósito. Un sistema de información '
    'es el que reúne, guarda, procesa y entrega información para que una organización funcione. No hace falta una '
    'computadora para que exista: la biblioteca de Arapoty ya tiene uno, formado por la bibliotecaria, el cuaderno, '
    'los estantes y la costumbre de anotar cada préstamo. El proyecto no crea un sistema de la nada; mejora uno que '
    'ya funciona, mal o bien.',
    'Para describirlo se miran cinco elementos. Las personas: quiénes registran, consultan o deciden. Los procesos: '
    'las secuencias de actividades que se repiten, como prestar, devolver, buscar un libro o preparar el informe. '
    'Los datos: en este libro, en esta etapa, significa qué información usa o produce cada persona en cada '
    'proceso; cómo se organiza esa información en tablas se decide recién en la Unidad III. Los recursos: '
    'materiales, equipos, tiempo, dinero y conocimientos disponibles. Los límites: qué queda dentro del sistema '
    'que se estudia y qué queda afuera.',
    'El límite no está dado: lo decide el equipo, con los interesados. Lo que queda afuera forma el entorno, y se '
    'relaciona con el sistema por lo que entra y lo que sale. Si la compra de libros queda afuera, el sistema no la '
    'gestiona, pero puede entregarle información (qué títulos se piden más). Un límite mal puesto produce '
    'proyectos imposibles: si «la biblioteca» incluye compras, inventario, inscripciones y sanciones, el equipo no '
    'termina nunca.',
    'Describir el sistema actual antes de proponer uno nuevo tiene una ventaja práctica: muestra qué funciona y '
    'conviene conservar. El cuaderno, por ejemplo, no necesita electricidad. Esa virtud vuelve a aparecer en el '
    'Capítulo 3, cuando se piensa qué hacer si se corta la luz.',
])

LEAD_FIG11 = ('Observá la figura: en el centro están los procesos del préstamo; alrededor, las personas, los datos y los '
              'recursos que intervienen. La línea punteada es el límite: lo que queda afuera, como la compra de '
              'libros, forma el entorno.')
EPI_FIG11 = 'Figura 1.1 — El sistema de préstamos de la biblioteca de Arapoty, con sus cinco elementos (caso ficticio).'

TABLA_13 = (['Elemento', 'Pregunta que lo identifica', 'En la biblioteca de Arapoty (lo que sabemos hasta ahora)'],
            [['Personas', '¿Quién registra, consulta o decide?', 'Bibliotecaria, lectores (estudiantes y docentes), dirección'],
             ['Procesos', '¿Qué secuencias de actividades se repiten?', 'Prestar, devolver, buscar un libro, preparar el informe mensual'],
             ['Datos', '¿Qué información usa o produce cada persona?', 'Quién llevó qué libro y cuándo; qué libros hay; préstamos por curso'],
             ['Recursos', '¿Con qué se cuenta?', 'El cuaderno, los estantes, el tiempo de la bibliotecaria; el resto, a verificar'],
             ['Límites', '¿Qué queda dentro y qué afuera?', 'Dentro: préstamo, devolución, consulta, informe. Afuera: compra de libros, inscripción de estudiantes']])

CONCEPTO_SISTEMA = ('Sistema de información', [
    'Conjunto de personas, procesos, datos y recursos que reúne, guarda, procesa y entrega información para una '
    'organización, dentro de un límite definido. Puede ser manual, informatizado o mixto.'])

EJ12 = ('Ejemplo resuelto 1.2: describir un proceso del sistema actual', [
    'Consigna: describir el proceso «prestar un libro» con los cinco elementos, marcando qué se sabe y qué se supone.',
    'Personas: el lector que pide y la bibliotecaria que registra (D0-3).',
    'Pasos (supuesto, a verificar con observación): el lector pide un título; la bibliotecaria lo busca en el '
    'estante; si lo encuentra, anota el préstamo en el cuaderno y entrega el libro.',
    'Datos: la bibliotecaria necesita saber quién se lleva el libro y qué libro es; la dirección, después, necesita '
    'contar esos préstamos por curso (D0-3). Qué se anota exactamente en el cuaderno todavía no lo sabemos.',
    'Recursos: el cuaderno (D0-1) y el tiempo de atención. Si hay computadora en la biblioteca, y en qué estado, '
    'queda a verificar.',
    'Límite: el proceso empieza cuando el lector pide y termina cuando se lleva el libro. Lo que pasa después '
    '(devolver, reclamar) son otros procesos del mismo sistema.',
    'Qué aprendimos: la descripción tiene más «a verificar» que certezas. Eso no es un error: es la lista de lo '
    'que el relevamiento del Capítulo 2 tiene que averiguar.',
])

ACT_E1 = [
    ('Ejercitá', [
        'Clasificá cada frase como síntoma, problema de información, problema que no es de información o solución '
        'anticipada. Justificá en una línea:\n'
        '(a) «Los lunes la biblioteca se llena.»\n'
        '(b) «Nadie sabe cuántos diccionarios quedan en buen estado.»\n'
        '(c) «Faltan mesas para leer.»\n'
        '(d) «Pongamos una pantalla con la lista de libros.»\n'
        '(e) «La lista de libros nuevos llega a los docentes un mes después.»\n'
        '(f) «Los libros de cuentos se rompen rápido.»',
        'Leé la descripción y nombrá las personas, los procesos, los datos, los recursos y un límite posible:\n'
        '«En el gimnasio, el profesor de Educación Física presta pelotas y conos a los cursos. Anota en una hoja '
        'el curso, el material y la hora. A fin de mes cuenta el material que falta y avisa a la dirección.»',
    ]),
    ('Resolvé', [
        'Escribí el enunciado del problema, en una oración y sin nombrar soluciones, para esta situación: «La sala '
        'de informática se reserva en una hoja pegada en la puerta. Dos docentes llegaron a la misma hora con sus '
        'cursos, porque uno había anotado con lápiz y alguien lo borró.» Indicá qué parte es hecho y qué parte '
        'tendrías que verificar.',
    ]),
    ('Pensá y decidí', [
        'Los lectores de códigos de barras (D0-4): ¿qué parte del problema mejorarían y qué parte no? ¿Por qué el '
        'equipo no los adopta todavía, aunque los hayan sugerido docentes?',
    ]),
    ('Desafío', [
        '¿La compra de libros nuevos queda dentro o fuera del sistema que va a estudiar el curso? Escribí un '
        'argumento para cada posición y decí qué información cruzaría el límite si queda afuera.',
    ]),
]

# ------------------------------------------------------------------ encuentro 2
E2_TITULO = 'Encuentro 2 — Interesados, punto de partida y práctica'

S13 = ('1.3 Actores e interesados: necesidades diferentes, decisiones compartidas', [
    'Un interesado es toda persona o grupo que usa el sistema, decide sobre él o se ve afectado por sus '
    'resultados. Un actor es un interesado que interactúa directamente con el sistema: lo usa para registrar o '
    'consultar. Todo actor es interesado, pero no todo interesado es actor. En la biblioteca, la bibliotecaria y los '
    'lectores son actores; las familias son interesadas, porque les importa que sus hijos lean, pero no usan el '
    'sistema.',
    'Los interesados no quieren lo mismo. La bibliotecaria quiere que los libros vuelvan; un lector quiere tenerlo '
    'más tiempo; la dirección quiere información de conjunto. Esas diferencias no son un obstáculo: son el material '
    'del análisis. El analista no decide quién tiene razón. Registra cada posición, busca la necesidad que hay '
    'detrás y lleva las opciones a quien tiene autoridad para decidir. La nota de la dirección lo dice a su modo: '
    'la propuesta tiene que «contar con la conformidad de la bibliotecaria» (D0-5).',
    'Para ordenar a los interesados se usa un mapa de interés e influencia. El interés mide cuánto le importa el '
    'sistema en su trabajo diario; la influencia, cuánto puede decidir o bloquear. Cada cuadrante sugiere una forma '
    'de trabajar: gestionar de cerca (mucho interés y mucha influencia), mantener satisfecho (poco interés y mucha '
    'influencia), mantener informado (mucho interés y poca influencia) y observar (poco de ambos).',
    'Los puntajes del mapa son estimaciones del equipo, no mediciones. Sirven para organizar el trabajo y se '
    'revisan después del relevamiento. Lo importante es que cada número tenga una razón que otro compañero pueda '
    'discutir.',
])

LEAD_FIG12 = ('Observá la figura: el eje horizontal mide el interés y el vertical la influencia. La bibliotecaria queda '
              'arriba a la derecha porque usa el sistema todos los días y su opinión decide; las familias quedan abajo '
              'a la izquierda porque casi no lo usan ni deciden sobre él.')
EPI_FIG12 = 'Figura 1.2 — Mapa de interés e influencia de los interesados de la biblioteca (Colegio Técnico Arapoty, caso ficticio).'

EJ13 = ('Ejemplo resuelto 1.3: el mapa de interesados de la biblioteca', [
    'Consigna: ubicar a seis interesados en el mapa y decidir cómo trabajar con cada uno. Se puntúa de 0 a 10 el '
    'interés y la influencia, con una razón para cada puntaje.',
    'Paso 1. Listar a los interesados: bibliotecaria, estudiantes, docentes, directora, encargado de informática y '
    'familias.',
    'Paso 2. Puntuar con razones (Tabla 1.4). El puntaje no es exacto: lo importante es que cada número tenga una '
    'razón que otro compañero pueda discutir.',
    'Paso 3. Leer el cuadrante y decidir la estrategia. Con la bibliotecaria se trabaja de cerca, con entrevistas y '
    'revisiones frecuentes. A la directora se la mantiene satisfecha: se la consulta en las decisiones que la '
    'afectan, como el costo. A estudiantes y docentes se los mantiene informados y se los consulta con técnicas que '
    'llegan a muchos, como un cuestionario. A las familias se las observa.',
])

def _n(x):
    return ('%g' % x).replace('.', ',')

TABLA_14 = (['Interesado', 'Interés', 'Influencia', 'Razón', 'Estrategia'],
            [[a, _n(b), _n(c), d, e] for a, b, c, d, e in D.INTERESADOS])

TABLA_15 = (['Persona o grupo', '¿Es actor?', 'Qué necesitaría (supuesto, a verificar)'],
            [['Bibliotecaria', 'Sí: registra y consulta', 'Registrar rápido y saber quién tiene cada libro'],
             ['Estudiantes y docentes lectores', 'Sí: consultan y retiran', 'Saber qué libros hay antes de ir'],
             ['Directora', 'Recibe información; no opera', 'Préstamos por curso cada mes (D0-3)'],
             ['Encargado de informática', 'No, pero instala y cuida los equipos', 'Que lo que se instale funcione y se pueda mantener'],
             ['Familias', 'No', 'Que sus hijos tengan acceso a los libros']])

S14 = ('1.4 Diagnóstico de conocimientos previos y plan de apoyo', [
    'El proyecto usa saberes de 1.º y 2.º curso: programación y pseudocódigo (Algorítmica), formularios y páginas '
    'web (Laboratorio), organización de datos en planillas y archivos, y comunicación escrita. Otros saberes, como '
    'las bases de datos de 3.º, los vas a aprender al mismo tiempo que avanza este libro: nadie espera que los '
    'domines al empezar.',
    'Por eso el Encuentro 1 empezó con el diagnóstico de entrada de los preliminares. No lleva nota. Sirve para que '
    'vos y tu docente sepan de dónde partís. Leé tus resultados por área (programación, formularios, datos y '
    'comunicación) y marcá cada una como «seguro», «con dudas» o «no lo vi». Tu docente reúne los resultados del '
    'curso en un mapa de apoyos, para saber qué repasar con todos y quién puede ayudar a quién.',
    'Con tus resultados armás un plan de apoyo personal: qué vas a repasar, dónde (la guía de consulta a las '
    'asignaturas previas de los preliminares indica materia y curso), con quién y antes de cuándo. Los plazos no son '
    'arbitrarios: los datos se necesitan desde el Encuentro 13 y la programación desde el Encuentro 19.',
    'El plan de apoyo es también un compromiso con tu equipo. En un proyecto compartido, las diferencias de '
    'formación son un recurso: quien sabe más de formularios puede explicar, y quien escribe mejor puede revisar '
    'los registros. Para que eso funcione, el equipo firma el acuerdo de trabajo de los preliminares, reparte los '
    'roles, que rotan en cada unidad, y anota en la bitácora qué hizo cada integrante. Así cada uno puede mostrar su '
    'aporte, y la evaluación reconoce el trabajo individual además del producto común.',
])

EJ14 = ('Ejemplo resuelto 1.4: el plan de apoyo de Noelia (estudiante ficticia)', [
    'Consigna: leer los resultados del diagnóstico de Noelia (Tabla 1.6) y armar su plan de apoyo.',
    'Paso 1. Ordenar por urgencia. «Datos» está «con dudas» y se necesita desde el Encuentro 13; «formularios» '
    'está «no lo vi» y se necesita desde el Encuentro 19. Programación y comunicación están firmes.',
    'Paso 2. Elegir dónde repasar, con la guía de consulta de los preliminares: datos, en Algorítmica 2.º '
    '(archivos y consultas); formularios, en Laboratorio 1.º y 2.º.',
    'Paso 3. Elegir con quién y cuándo, y qué evidencia va a mostrar (Tabla 1.7). Noelia, a su vez, ofrece ayuda en '
    'lo que domina: revisar la redacción de los registros del equipo.',
])

TABLA_16 = (['Área del diagnóstico', 'Ítems correctos', 'Autoevaluación de Noelia'],
            [['Programación', '3 de 3', 'Seguro'],
             ['Formularios', '0 de 2', 'No lo vi'],
             ['Datos', '1 de 2', 'Con dudas'],
             ['Comunicación', '2 de 2', 'Seguro']])

TABLA_17 = (['Qué repasar', 'Dónde', 'Con quién', 'Antes de', 'Cómo lo voy a mostrar'],
            [['Filtrar y contar datos en una planilla', 'Algorítmica 2.º: archivos y consultas', 'Compañero de apoyo del equipo', 'Encuentro 13', 'Resolver de nuevo el ítem 6 del diagnóstico'],
             ['Controles de un formulario y envío de datos', 'Laboratorio 1.º y 2.º: formularios', 'Docente de Laboratorio', 'Encuentro 19', 'Un formulario de dos campos que envía datos'],
             ['Ofrezco: revisar la redacción de los registros', '—', 'Todo el equipo', 'Capítulo 2', 'Revisión anotada en la bitácora']])

ACT_E2 = [
    ('Ejercitá', [
        'Indicá si cada uno es actor, interesado que no es actor o ninguno de los dos, y por qué:\n'
        '(a) la docente que reemplaza a la bibliotecaria en julio;\n'
        '(b) la familia de un estudiante de 7.º;\n'
        '(c) el encargado de informática;\n'
        '(d) la librería que vende libros al colegio;\n'
        '(e) un estudiante de 9.º que retira libros todas las semanas;\n'
        '(f) la directora, que recibe el informe mensual.',
    ]),
    ('Resolvé', [
        'Agregá al mapa de la Figura 1.2 dos interesados que no aparecen. Para cada uno, escribí su puntaje de '
        'interés e influencia con una razón, y la estrategia que corresponde.',
        'Completá tu propio plan de apoyo con el formato de la Tabla 1.7 y con tus resultados del diagnóstico de '
        'entrada. Incluí al menos una ayuda que vos podés ofrecer al equipo.',
    ]),
    ('Pensá y decidí', [
        'Los estudiantes tienen mucho interés y poca influencia. ¿Qué se pierde si el equipo solo los «mantiene '
        'informados»? Proponé una forma de escucharlos sin que decidan solos sobre las reglas de la biblioteca.',
    ]),
    ('Desafío', [
        'Supongamos que hay que cambiar el plazo de préstamo. Usando el mapa, decí quién debería decidir, a quién '
        'habría que consultar y a quién solo informar. Marcá qué parte de tu respuesta es un supuesto que el '
        'relevamiento tendría que confirmar.',
    ]),
]

# ------------------------------------------------------------------ práctica
PRACTICA_TITULO = 'Práctica 1 — Describir una biblioteca: hechos, supuestos y soluciones anticipadas'
PRACTICA_INTRO = [
    'Un estudiante de 3.º BTI visitó la biblioteca de otra escuela y escribió el relato de abajo. Es un caso de '
    'práctica, con datos distintos de los del Colegio Arapoty: las mismas escuela y personas vuelven en las '
    'Prácticas 2 y 3. Trabajá en el nivel que te indique tu docente. Todos los niveles entregan una ficha de problema '
    'y un mapa de actores: son las evidencias del Encuentro 2.',
]
NIVELES = [
    ('Nivel 1 — Guiado', [
        'Clasificá cada oración del relato (V-01 a V-12) como hecho, supuesto o solución anticipada. Para tres de '
        'los supuestos, escribí qué pregunta harías o qué observarías para verificarlo.',
        'Completá la ficha de problema de la biblioteca Mbokaja:\n'
        'Quién tiene la dificultad: ________. Qué información falta o no es confiable: ________.\n'
        'En qué situación aparece: ________. Qué consecuencia tiene: ________ (fuente: V-__).\n'
        'Qué soluciones se anticiparon: ________ (V-__ y V-__). Qué falta averiguar: ________.',
        'Listá los actores y los interesados que aparecen en el relato e indicá para cada uno si es actor.',
    ]),
    ('Nivel 2 — Intermedio', [
        'Clasificá V-01 a V-12 y justificá cada clasificación en una línea. Señalá qué oración mezcla un hecho con '
        'una cifra que todavía hay que verificar.',
        'Describí el sistema de préstamos de Mbokaja con los cinco elementos (formato de la Tabla 1.3) y proponé un '
        'límite justificado.',
        'Redactá la ficha de problema completa (formato de la Tabla 1.2) y el enunciado del problema en una '
        'oración, sin nombrar soluciones. Armá el mapa de actores e interesados con puntajes y razones.',
    ]),
    ('Nivel 3 — Ampliación', [
        'Con la autorización de tu docente, visitá la biblioteca de tu colegio y escribí un relato de diez '
        'oraciones sin nombres de estudiantes ni datos personales. Separá hechos, supuestos y soluciones '
        'anticipadas.',
        'Redactá la ficha de problema y el mapa de actores de tu biblioteca.',
        'Compará con Mbokaja: escribí dos diferencias que cambien el problema, no solo los nombres, y explicá por '
        'qué lo cambian.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: cada oración del relato tiene una clasificación justificada; la ficha de '
                    'problema distingue lo que se sabe (con su fuente V-xx) de lo que hay que averiguar; el enunciado '
                    'no nombra ninguna solución; el mapa distingue actores de interesados que no son actores.')

REPASO = ('Para repasar', [
    'Una dificultad cotidiana es el síntoma; el problema de información es lo que falta saber, o se sabe tarde o mal.',
    'Hechos, supuestos y soluciones anticipadas se separan; los supuestos se marcan «a verificar».',
    'Un sistema de información tiene personas, procesos, datos, recursos y límites, aunque no tenga computadora.',
    'Todo actor es interesado, pero no todo interesado es actor. El mapa de interés e influencia ordena cómo trabajar con cada uno.',
    'El diagnóstico de entrada no lleva nota: alimenta tu plan de apoyo y el mapa de apoyos del curso.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, este capítulo conserva sus dos encuentros.',
    'Si aun así se pierde uno, no se omiten: el Ejemplo resuelto 1.1 (ficha de problema), el 1.3 (mapa de '
    'interesados) y la Práctica 1 en el Nivel 1 o el Nivel 2. Pasan a lectura domiciliaria: la sección 1.2 con el '
    'Ejemplo resuelto 1.2, y las actividades «Pensá y decidí» y «Desafío».',
])

# ------------------------------------------------------------------ evaluación
EVAL_ID = 'ADS3-L1-C1'
EVAL_TITULO = 'Evaluación del Capítulo 1'
EVAL_TEXTO_BASE = ('Texto base — Préstamo de proyectores (situación de evaluación, ficticia)', [
    'A-1 El colegio tiene tres proyectores que los docentes piden en la secretaría.',
    'A-2 La secretaria anota en una libreta el nombre del docente y la hora, pero no qué proyector se lleva.',
    'A-3 La semana pasada dos docentes reservaron el mismo proyector para la misma hora.',
    'A-4 Un docente propone comprar un cuarto proyector.',
    'A-5 Seguramente los proyectores se piden más en época de exámenes.',
    'A-6 La dirección quiere saber cuántas horas se usa cada proyector, para decidir si se compra otro.',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', '¿Cuál de estas frases describe un problema de información?',
     ['Nadie sabe con certeza qué lector tiene cada libro.',
      'Faltan estantes para ordenar los libros.',
      'Hay que comprar un lector de códigos de barras.',
      'La biblioteca abre a las siete.']),
    ('mc', 'En el texto base, ¿qué es la oración A-5?',
     ['Un supuesto: todavía no se comprobó.',
      'Un hecho observado.',
      'Una solución anticipada.',
      'Un límite del sistema.']),
    ('mc', '¿Cuál de estos interesados es también actor del sistema de préstamos de proyectores?',
     ['La secretaria que anota los préstamos.',
      'La empresa que vendió los proyectores.',
      'Las familias de los estudiantes.',
      'El intendente municipal.']),
    ('mc', 'Un interesado con mucha influencia y poco interés diario en el sistema se debe…',
     ['mantener satisfecho, consultándolo en las decisiones que lo afectan.',
      'gestionar de cerca, con entrevistas semanales.',
      'ignorar, porque no usa el sistema.',
      'mantener informado solo al final del proyecto.']),
    ('vf', 'Un sistema de información necesita una computadora para existir.',
     False, 'Falso. La libreta de la secretaría, la secretaria y sus procesos ya forman un sistema de información manual.'),
    ('vf', 'La propuesta de comprar un cuarto proyector (A-4) es una solución anticipada.',
     True, 'Verdadero. Aparece antes de entender el problema; se registra y se pregunta qué resolvería.'),
    ('vf', 'El diagnóstico de entrada sirve para poner la primera nota del año.',
     False, 'Falso. No lleva nota: sirve para el plan de apoyo de cada estudiante y el mapa de apoyos del curso.'),
    ('ab', 'Con el texto base, completá la ficha de problema: quién tiene la dificultad, qué información falta o no '
           'es confiable, qué consecuencia tiene y qué falta averiguar. Indicá la fuente (A-…) de cada dato.',
     'Quién: los docentes, la secretaria y la dirección (A-1, A-6). Qué información falta: qué proyector se lleva '
     'cada docente y cuándo está libre cada uno (A-2, A-3). Consecuencia: reservas superpuestas (A-3) y decisiones '
     'de compra sin datos de uso (A-6). Qué falta averiguar: cuántos pedidos hay por semana, si A-5 es cierto, cómo '
     'se devuelven. Se valora que no aparezca «comprar otro proyector» como problema.', 4),
    ('ab', 'Enunciá el problema en una oración, sin nombrar una solución, y explicá por qué A-4 no resuelve todo el '
           'problema.',
     'Ejemplo: «En el colegio, los docentes y la dirección no cuentan con información confiable sobre qué '
     'proyector está reservado o prestado en cada momento ni sobre su uso, porque la libreta no registra el '
     'proyector.» A-4 podría reducir la falta de equipos, pero no impide reservas superpuestas ni produce el dato de '
     'uso que pide A-6.', 4),
]
EVAL_PUNTAJE = 'Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno).'
