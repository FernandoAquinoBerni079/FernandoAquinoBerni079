# -*- coding: utf-8 -*-
"""Capítulo 4 v2 — «Requisitos que se pueden comprobar» (índice de Work, secciones 4.1 a 4.4).
Todo el texto es original; la institución y las personas son ficticias. Cada fuente citada
(E1-L2, RN-01…) existe en DOSSIER o en REGLAS, y el texto del fragmento respalda lo que se le atribuye:
verificar.py comprueba la existencia y las citas textuales."""

UNIDAD = 'Unidad II — Especificar qué debe resolver el sistema'
CAPITULO = 'Capítulo 4'
TITULO = 'Requisitos que se pueden comprobar'
ENCUENTROS = (7, 8)

ROTULO_CAPACIDAD = 'Capacidad propuesta para el programa institucional (C3; no es una capacidad oficial del MEC)'
CAPACIDAD = 'Especifica y prioriza requisitos verificables.'
TEMA = ('Necesidad, requisito, regla de negocio y solución técnica. Requisitos funcionales, de calidad y '
        'restricciones. Identificación, fuente, prioridad y criterios de aceptación. Ambigüedades '
        'frecuentes y cómo corregirlas.')
INDICADORES = [
    'Distingue necesidad, requisito, regla de negocio y solución técnica en pedidos de usuarios.',
    'Formula requisitos funcionales, de calidad y restricciones, cada uno con identificador y fuente que lo respalda.',
    'Define para cada requisito un criterio de aceptación comprobable y una prioridad justificada.',
    'Detecta ambigüedades frecuentes y reescribe el requisito en forma verificable.',
]
TIEMPO = ('Dos encuentros de 5 HC (7 y 8 de la secuencia anual). Las 5 HC pueden repartirse en varios '
          'bloques semanales.')

APERTURA = [
    'En la Unidad I relevaste la biblioteca: entrevistaste, observaste y registraste lo que cada persona '
    'necesita. Ahora hay que convertir ese material en algo con lo que se pueda construir y, sobre todo, '
    'comprobar: una lista de requisitos.',
    'Un requisito sirve si dentro de unos meses alguien puede tomar el prototipo y decir, sin discutir, '
    '«esto se cumple» o «esto no se cumple». En este capítulo aprendés a escribir requisitos así: con un '
    'identificador, con la fuente que los respalda, con una prioridad y con un criterio de aceptación.',
]
ARTICULACION = [
    'Con el Capítulo 2: los fragmentos del dossier de relevamiento que se usan acá están reproducidos en la '
    'página siguiente. Cada requisito cita el fragmento exacto que lo respalda.',
    'Con Algorítmica y Laboratorio de 3.º: este capítulo no exige programar ni diseñar tablas. Las '
    'soluciones técnicas se nombran solo para aprender a separarlas de los requisitos.',
    'Con el resto del libro: los casos de uso (Capítulo 5), la priorización y los cambios (Capítulo 6) y las '
    'pruebas (Capítulos 14 a 16) parten del catálogo que se arma acá.',
]

# ------------------------------------------------------------------ fuentes del capítulo
# Dossier de relevamiento (Capítulo 2). Caso ficticio: Colegio Técnico Arapoty.
DOSSIER_TITULO = 'Extracto del dossier de relevamiento (Capítulo 2) — caso ficticio'
DOSSIER = [
    ('E1', 'Entrevista a la Lic. Mirta Escobar, bibliotecaria', [
        ('E1-L2', 'Anoto los préstamos en un cuaderno; cuando hay fila, anoto apurada y después no entiendo mi letra.'),
        ('E1-L4', 'Tengo que hojear el cuaderno hacia atrás hasta encontrar quién lo llevó. A veces tardo media hora.'),
        ('E1-L6', 'Voy al estante. Si no está, puede estar prestado, mal ubicado o perdido.'),
        ('E1-L8', 'Un informe a fin de cada mes con cuántos préstamos hubo por curso. Lo hago contando a mano y me lleva una tarde.'),
        ('E1-L10', 'Saber al instante quién tiene cada libro. Y que el sistema sea fácil, porque yo no soy de computadoras.'),
    ]),
    ('E4', 'Segunda entrevista a la bibliotecaria', [
        ('E4-L2', 'De las lecturas obligatorias tenemos varios ejemplares. Cuando me devuelven uno, no sé de cuál préstamo es, porque en el cuaderno solo anoto el título.'),
        ('E4-L4', 'En hora pico me pasó de anotar el mismo libro a dos chicos distintos, y después no sabía cuál de los dos lo tenía.'),
        ('E4-L6', 'A los que ya se fueron del colegio no les presto. Pero siguen en el cuaderno y no los puedo borrar, porque ahí está lo que se llevaron.'),
        ('E4-L8', 'Solo yo, o quien me reemplace, debería anotar préstamos. Los chicos pueden mirar qué hay, pero no tocar los registros.'),
        ('E4-L10', 'Trabajaría en la computadora de la biblioteca, que es vieja y no siempre tiene internet.'),
    ]),
    ('E3', 'Entrevista a Iván Ortellado, delegado de 2.º BTI (lector)', [
        ('E3-L1', 'Vengo a buscar un libro y no sé si está.'),
        ('E3-L3', 'Me gustaría saber antes de venir si lo hay.'),
        ('E3-L4', 'Y que se pueda renovar el préstamo sin traer el libro.'),
    ]),
    ('E5', 'Entrevista a la Lic. Teresa Vega, directora', [
        ('E5-L2', 'Necesito saber cada mes cuántos préstamos hubo por curso, para organizar las horas de biblioteca.'),
        ('E5-L4', 'No hay presupuesto para comprar programas ni para pagar un servicio en internet.'),
        ('E5-L6', 'Los datos de los estudiantes no pueden quedar a la vista de cualquiera.'),
    ]),
]
FUENTES = {cod: txt for _, _, frs in DOSSIER for cod, txt in frs}

REGLAS_TITULO = 'Reglas de préstamo acordadas en clase (supuestos didácticos del proyecto)'
REGLAS_NOTA = ('Son las reglas iniciales del caso, negociadas en clase. No son normas del MEC ni políticas de '
               'una biblioteca real, y pueden cambiar con una solicitud de cambio (Capítulo 6).')
REGLAS = [
    ('RN-01', 'Un ejemplar solo puede tener un préstamo activo.'),
    ('RN-02', 'Cada lector puede tener como máximo dos préstamos activos.'),
    ('RN-03', 'El plazo inicial de préstamo es de siete días.'),
    ('RN-04', 'Los lectores inactivos no reciben nuevos préstamos.'),
    ('RN-05', 'La devolución no elimina el préstamo: queda en el historial.'),
    ('RN-06', 'No se borran lectores ni ejemplares con historial: se inactivan.'),
]
FUENTES.update(dict(REGLAS))

# ------------------------------------------------------------------ encuentro 7
E7_TITULO = 'Encuentro 7 — Requisitos funcionales y reglas de préstamo'

S41 = ('4.1 Necesidad, requisito, regla de negocio y solución técnica', [
    'En el dossier aparecen mezcladas cuatro cosas distintas. La necesidad es lo que una persona tiene que '
    'lograr: «Saber al instante quién tiene cada libro» (E1-L10). La regla de negocio es una política de '
    'la organización, que vale aunque no exista ningún sistema: «Un ejemplar solo puede tener un préstamo '
    'activo» (RN-01). El requisito dice qué debe hacer o cumplir el sistema para atender la necesidad y '
    'hacer respetar la regla. La solución técnica es una forma concreta de construirlo: una pantalla, una '
    'tabla, un lenguaje.',
    'Separarlas importa por dos razones. La primera: una solución técnica escrita como requisito cierra '
    'el camino a otras mejores; si el catálogo dice «una app», ya nadie pregunta si alcanzaba con una '
    'página que funcione en la computadora de la biblioteca. La segunda: la regla cambia por decisión de la '
    'institución, no del programador. Si el requisito dice «el máximo vigente» en lugar de «dos», cuando el '
    'curso acuerde otro máximo el requisito sigue sirviendo.',
])

TABLA_41 = (['Categoría', 'Qué expresa', 'Ejemplo del caso', 'Quién la decide'],
            [['Necesidad', 'Lo que una persona tiene que lograr', '«Saber al instante quién tiene cada libro.» (E1-L10)', 'El interesado'],
             ['Regla de negocio', 'Una política de la organización', 'RN-01: un ejemplar solo puede tener un préstamo activo', 'La institución'],
             ['Requisito', 'Lo que el sistema debe hacer o cumplir, de forma comprobable', 'RF-04: rechazar el préstamo de un ejemplar que ya está prestado', 'Se acuerda con los interesados'],
             ['Solución técnica', 'Una forma de construirlo', 'Un índice único en la tabla de préstamos; un botón «Prestar»', 'El equipo, en la etapa de diseño']])

CONCEPTO_REQ = ('Requisito', [
    'Un requisito es un enunciado de lo que el sistema debe hacer o cumplir, escrito de modo que se pueda '
    'comprobar si se cumple. Tiene identificador, fuente, prioridad y criterio de aceptación. No describe '
    'cómo se construye.'])

EJ1 = ('Ejemplo resuelto 4.1: separar las cuatro categorías', [
    'Consigna: clasificar seis frases del trabajo del equipo y justificar cada clasificación.',
    '(a) «Saber al instante quién tiene cada libro.» (E1-L10). Necesidad: describe lo que la bibliotecaria '
    'quiere lograr, no qué hace el sistema.',
    '(b) «Un ejemplar solo puede tener un préstamo activo.» (RN-01). Regla de negocio: rige aunque los '
    'préstamos se sigan anotando en un cuaderno.',
    '(c) «El sistema debe rechazar el préstamo de un ejemplar que ya tiene un préstamo activo.» Requisito: '
    'dice qué hace el sistema y se puede comprobar intentando prestar dos veces el mismo ejemplar.',
    '(d) «Usar un índice único en la tabla de préstamos.» Solución técnica: es una forma de cumplir (c); '
    'se decide en el diseño (Capítulo 9) y se construye en el Capítulo 12.',
    '(e) «Me gustaría saber antes de venir si lo hay.» (E3-L3). Necesidad del lector.',
    '(f) «Hagamos una app para el celular.» (propuesta de un compañero del equipo). Solución técnica: antes '
    'de anotarla hay que preguntar qué necesidad atiende; en este caso, la de (e).',
])

S42 = ('4.2 Requisitos funcionales, de calidad y restricciones', [
    'Los requisitos funcionales describen lo que el sistema hace: registrar un préstamo, rechazarlo, '
    'mostrar quién tiene un ejemplar. Se comprueban haciendo la operación y mirando el resultado.',
    'Los requisitos de calidad, también llamados no funcionales, describen qué tan bien lo hace: si la '
    'bibliotecaria lo puede usar sin ayuda, si protege los datos personales, si responde en un tiempo '
    'razonable. Son los más difíciles de escribir, porque las personas los expresan con palabras vagas '
    '(«fácil», «seguro»); en 4.4 vas a ver cómo volverlos comprobables.',
    'Las restricciones son condiciones que limitan las soluciones posibles: el presupuesto, el equipo '
    'disponible, la falta de internet. No las elige el equipo; las impone el contexto. Por eso conviene '
    'escribirlas temprano: una restricción descubierta tarde puede invalidar un diseño entero.',
])

LEAD_FIG1 = ('Observá la figura: los tres tipos de requisitos cuelgan del mismo tronco, y cada uno responde '
             'una pregunta distinta. Abajo se recuerda que las reglas de negocio no son requisitos: el '
             'sistema las hace cumplir.')
EPI_FIG1 = 'Figura 4.1 — Tipos de requisitos, con un ejemplo del caso para cada uno.'

TABLA_42 = (['Tipo', 'Pregunta que responde', 'Cómo se comprueba', 'Ejemplo del caso'],
            [['Funcional (RF)', '¿Qué hace el sistema?', 'Se ejecuta la operación y se mira el resultado', 'RF-03: registrar la devolución identificando el ejemplar'],
             ['De calidad (RNF)', '¿Qué tan bien lo hace?', 'Con una medida o una tarea observable', 'RNF-03: la consulta pública no muestra datos personales'],
             ['Restricción (RS)', '¿Qué condición limita la solución?', 'Se verifica en el entorno real', 'RS-02: sin licencias ni servicios pagos']])

EJ2 = ('Ejemplo resuelto 4.2: del dossier al catálogo de requisitos', [
    'Consigna: armar el catálogo inicial de requisitos a partir del dossier y de las reglas RN-01 a RN-06.',
    'Paso 1. Leer cada fragmento y preguntarse qué tendría que hacer o cumplir el sistema para atenderlo.',
    'Paso 2. Escribir cada requisito con la forma «El sistema debe…» (o con el actor como sujeto, en los de '
    'calidad), una sola acción por requisito y ninguna tecnología.',
    'Paso 3. Anotar como fuente solo los fragmentos que de verdad lo respaldan. Si un requisito no tiene '
    'fuente, o es una idea del equipo que hay que consultar, o sobra.',
    'Resultado: el catálogo de la tabla siguiente, con diez requisitos funcionales, tres de calidad y dos '
    'restricciones. Observá que RF-05 dice «el máximo vigente» y no «dos»: si RN-02 cambia, RF-05 no cambia.',
])

# Catálogo del ejemplo: (id, tipo, enunciado, fuentes, prioridad)
CATALOGO = [
    ('RF-01', 'Funcional', 'El sistema debe registrar cada préstamo con el ejemplar, el lector y la fecha de salida.', ['E1-L2', 'E4-L2'], 'Imprescindible'),
    ('RF-02', 'Funcional', 'El sistema debe calcular la fecha de vencimiento de cada préstamo según el plazo vigente.', ['RN-03'], 'Imprescindible'),
    ('RF-03', 'Funcional', 'El sistema debe registrar la devolución identificando el ejemplar devuelto y su préstamo.', ['E4-L2', 'RN-05'], 'Imprescindible'),
    ('RF-04', 'Funcional', 'El sistema debe rechazar el préstamo de un ejemplar que ya tiene un préstamo activo.', ['E4-L4', 'RN-01'], 'Imprescindible'),
    ('RF-05', 'Funcional', 'El sistema debe rechazar un nuevo préstamo a un lector que ya alcanzó el máximo vigente de préstamos activos.', ['RN-02'], 'Imprescindible'),
    ('RF-06', 'Funcional', 'El sistema debe rechazar préstamos a lectores inactivos.', ['E4-L6', 'RN-04'], 'Imprescindible'),
    ('RF-07', 'Funcional', 'El sistema debe permitir a cualquier lector consultar si hay ejemplares disponibles de un título.', ['E3-L1', 'E3-L3', 'E1-L6'], 'Imprescindible'),
    ('RF-08', 'Funcional', 'El sistema debe mostrar a la bibliotecaria qué lector tiene cada ejemplar prestado.', ['E1-L4', 'E1-L10'], 'Imprescindible'),
    ('RF-09', 'Funcional', 'El sistema debe informar la cantidad de préstamos de cada curso en un mes elegido.', ['E1-L8', 'E5-L2'], 'Importante'),
    ('RF-10', 'Funcional', 'El sistema debe permitir inactivar un lector o un ejemplar sin borrar su historial.', ['E4-L6', 'RN-06'], 'Imprescindible'),
    ('RNF-01', 'Calidad: uso', 'La bibliotecaria debe poder registrar un préstamo y una devolución sin ayuda, después de una práctica guiada.', ['E1-L10'], 'Importante'),
    ('RNF-02', 'Calidad: seguridad', 'Solo la bibliotecaria o su reemplazo autorizado deben poder registrar o modificar préstamos.', ['E4-L8'], 'Imprescindible'),
    ('RNF-03', 'Calidad: privacidad', 'La consulta pública no debe mostrar datos personales de los lectores.', ['E5-L6'], 'Imprescindible'),
    ('RS-01', 'Restricción', 'El sistema debe funcionar en la computadora de la biblioteca sin conexión a internet.', ['E4-L10'], 'Imprescindible'),
    ('RS-02', 'Restricción', 'La solución no debe requerir licencias ni servicios pagos.', ['E5-L4'], 'Imprescindible'),
]
POSTERGADOS = [
    ('E3-L4', 'Renovar el préstamo sin traer el libro', 'Deseable', 'El circuito de préstamo y devolución funciona sin esto; exige además una regla nueva de renovación. Se lleva al Capítulo 6.'),
]

ACT_E7 = [
    ('Ejercitá', [
        'Clasificá cada frase como necesidad, regla de negocio, requisito o solución técnica, y justificá en una línea:\n'
        '(a) «Quiero saber qué libros están atrasados.»\n'
        '(b) «Los diccionarios no salen de la biblioteca.»\n'
        '(c) «El sistema debe listar los préstamos activos de un lector.»\n'
        '(d) «Guardar los datos en un archivo SQLite.»\n'
        '(e) «El préstamo dura siete días.»\n'
        '(f) «Poner un botón verde que diga Prestar.»',
    ]),
    ('Resolvé', [
        'Un compañero propuso estos requisitos con sus fuentes. Para cada uno, decidí si la fuente lo respalda '
        'de verdad (releé el fragmento en el dossier) y corregí lo que haga falta:\n'
        '(a) «El sistema debe registrar la devolución identificando el ejemplar.» Fuente: E4-L2.\n'
        '(b) «El sistema debe enviar un aviso al celular del lector cuando se acerque el vencimiento.» Fuente: E3-L3.\n'
        '(c) «El sistema debe impedir que se borre un lector con historial.» Fuente: E4-L6.\n'
        '(d) «El sistema debe permitir reservar libros desde la casa.» Fuente: E1-L4.',
        'Redactá un requisito funcional a partir de E5-L2 y otro a partir de E4-L8. Para el segundo, decidí si '
        'es funcional o de calidad y explicá por qué.',
    ]),
    ('Pensá y decidí', [
        'Iván pidió «que se pueda renovar el préstamo sin traer el libro» (E3-L4). ¿Lo incluirías en el '
        'catálogo? ¿Con qué prioridad? ¿Qué regla de negocio faltaría acordar para poder cumplirlo?',
    ]),
    ('Desafío', [
        'El curso decide que cada lector pueda tener tres préstamos activos. ¿Qué cambia: RN-02, RF-05 o los '
        'dos? Explicá qué ganó el catálogo al escribir RF-05 con «el máximo vigente».',
    ]),
]

# ------------------------------------------------------------------ encuentro 8
E8_TITULO = 'Encuentro 8 — Calidad, restricciones y criterios de aceptación'

S43 = ('4.3 Identificación, fuente, prioridad y criterios de aceptación', [
    'Cada requisito lleva un identificador que no se reutiliza nunca: RF para los funcionales, RNF para '
    'los de calidad, RS para las restricciones y RN para las reglas de negocio. Si un requisito se elimina, '
    'su número queda vacante; así, una prueba o una conversación que mencionó «RF-04» sigue apuntando a lo '
    'mismo.',
    'La fuente es el fragmento del dossier o la regla que respalda el requisito. Tiene que decir de verdad '
    'lo que se le atribuye: si RF-04 cita E4-L4, en E4-L4 tiene que aparecer el problema de prestar el '
    'mismo libro a dos personas. Una fuente que no respalda el requisito es peor que ninguna, porque da una '
    'falsa seguridad.',
    'La prioridad ordena el trabajo. En este libro se usan tres niveles. Imprescindible: sin él no funciona '
    'el circuito de préstamo y devolución, o se viola una regla. Importante: aporta mucho valor, pero el '
    'circuito funciona sin él. Deseable: se hace si sobra tiempo. La prioridad se discute con los '
    'interesados y se revisa en el Capítulo 6.',
    'El criterio de aceptación dice cómo se va a comprobar el requisito. Se escribe con tres partes: '
    '«Dado» (la situación de partida), «cuando» (lo que se hace) y «entonces» (lo que se tiene que '
    'observar). Si no se puede escribir un criterio así, el requisito todavía no es comprobable.',
])

LEAD_FIG2 = ('Seguí la cadena de izquierda a derecha: de la necesidad que dijo la bibliotecaria (E4-L4) a la '
             'regla, el requisito, el criterio de aceptación y, más adelante en el libro, la prueba. Cada '
             'eslabón se puede rastrear hasta el anterior.')
EPI_FIG2 = 'Figura 4.2 — Cadena de trazabilidad de RF-04, desde la necesidad hasta la prueba.'

CONCEPTO_CA = ('Criterio de aceptación', [
    'Es la condición observable que decide si un requisito se cumple. Se escribe «Dado… cuando… entonces…» '
    'y debe poder comprobarlo una persona que no participó del análisis.'])

EJ3 = ('Ejemplo resuelto 4.3: la ficha completa de RF-04', [
    'Identificador: RF-04. Tipo: funcional. Prioridad: imprescindible (sin él se viola RN-01).',
    'Enunciado: El sistema debe rechazar el préstamo de un ejemplar que ya tiene un préstamo activo.',
    'Fuentes: E4-L4 (la bibliotecaria anotó el mismo libro a dos chicos y no supo quién lo tenía) y RN-01.',
    'Criterio de aceptación CA-04: Dado un ejemplar con un préstamo activo, cuando se intenta registrar otro '
    'préstamo de ese ejemplar, entonces el sistema rechaza la operación, muestra el motivo y el ejemplar '
    'sigue teniendo un solo préstamo activo, el original.',
    'Por qué el criterio es comprobable: la situación de partida se puede preparar, la acción se puede '
    'repetir y el resultado se ve en dos lugares (el mensaje y la lista de préstamos activos).',
])

TABLA_43 = (['Id.', 'Criterio de aceptación', 'Prioridad y razón'],
            [['RF-02', 'Dado un préstamo registrado el 2 de marzo con el plazo de RN-03, cuando se consulta su vencimiento, entonces figura el 9 de marzo.', 'Imprescindible: sin vencimiento no hay control de atrasos.'],
             ['RF-07', 'Dado un título con un ejemplar disponible y otro prestado, cuando un lector sin sesión lo consulta, entonces ve «1 disponible» y ningún nombre de lector.', 'Imprescindible: atiende la necesidad del lector (E3-L3).'],
             ['RF-09', 'Dado un mes con préstamos de tres cursos, cuando se pide el informe de ese mes, entonces aparece cada curso con su cantidad y la suma coincide con el total de préstamos del mes.', 'Importante: ahorra una tarde por mes (E1-L8), pero el circuito funciona sin él.'],
             ['RS-01', 'Dada la computadora de la biblioteca desconectada de internet, cuando se registra un préstamo y una devolución, entonces ambas operaciones se completan y quedan guardadas.', 'Imprescindible: es la única computadora disponible (E4-L10).']])

S44 = ('4.4 Ambigüedades frecuentes y cómo corregirlas', [
    'Un requisito es ambiguo cuando dos personas pueden entenderlo distinto, y entonces no hay acuerdo '
    'posible sobre si se cumple. Las ambigüedades se repiten tanto que tienen nombre. La tabla siguiente '
    'reúne las más frecuentes en proyectos escolares, con la pregunta que ayuda a corregir cada una.',
    'Para corregir no se inventan cifras: se le pregunta al interesado y se anota la respuesta como nueva '
    'fuente. Mientras tanto, el requisito puede llevar una cifra propuesta marcada «a confirmar».',
])

TABLA_44 = (['Ambigüedad', 'Ejemplo', 'Pregunta para corregirla', 'Versión corregida'],
            [['Palabra vaga', '«El sistema debe ser fácil.»', '¿Fácil para quién y para hacer qué?', 'RNF-01: la bibliotecaria registra un préstamo y una devolución sin ayuda tras una práctica guiada'],
             ['Cuantificador indefinido', '«Todos pueden ver los préstamos.»', '¿Quiénes son «todos»? ¿Qué ven?', 'RF-08 para la bibliotecaria y RNF-03 para la consulta pública'],
             ['Requisito compuesto', '«Registrar préstamos y generar el informe.»', '¿Se pueden probar por separado?', 'Dos requisitos: RF-01 y RF-09'],
             ['Solución disfrazada', '«Una app con inicio de sesión de Google.»', '¿Qué necesidad atiende?', 'RF-07 y RNF-02, sin tecnología'],
             ['Sujeto ausente', '«Debe poder corregirse un préstamo.»', '¿Quién corrige? ¿Qué se corrige?', 'Hay que consultarlo: choca con RN-05'],
             ['Negación imposible de probar', '«El sistema nunca debe perder datos.»', '¿Qué situación concreta preocupa?', 'Tras cerrar y volver a abrir el sistema, los préstamos siguen registrados']])

EJ4 = ('Ejemplo resuelto 4.4: de «fácil» a un requisito comprobable', [
    'Fragmento: «Y que el sistema sea fácil, porque yo no soy de computadoras.» (E1-L10)',
    'Paso 1. Reconocer la ambigüedad: «fácil» es una palabra vaga.',
    'Paso 2. Preguntar: ¿qué tendría que poder hacer Mirta, y en qué condiciones? Supongamos que responde '
    'que quiere registrar préstamos y devoluciones sola, sin llamar al encargado de informática.',
    'Paso 3. Reescribir: RNF-01. La bibliotecaria debe poder registrar un préstamo y una devolución sin '
    'ayuda, después de una práctica guiada.',
    'Paso 4. Criterio de aceptación: Dada la bibliotecaria después de una práctica guiada de 30 minutos (a '
    'confirmar con ella), cuando registra tres préstamos y dos devoluciones de una lista preparada, '
    'entonces completa las cinco operaciones sin pedir ayuda y sin errores de carga.',
    'Paso 5. Anotar como fuente E1-L10 y, cuando Mirta confirme la duración de la práctica, su respuesta.',
])

REVISION_PARES = ('Lista para la revisión entre pares', [
    '1. ¿Tiene identificador y no repite uno existente?',
    '2. ¿La fuente citada dice de verdad lo que se le atribuye?',
    '3. ¿Expresa una sola cosa?',
    '4. ¿Dice qué hace o cumple el sistema, sin nombrar una tecnología?',
    '5. ¿Tiene un criterio «Dado… cuando… entonces…» que otra persona podría comprobar?',
    '6. ¿Está libre de palabras vagas, cuantificadores indefinidos y negaciones imposibles de probar?',
    '7. ¿Tiene una prioridad con su razón?',
])

ACT_E8 = [
    ('Ejercitá', [
        'Nombrá el tipo de ambigüedad de cada enunciado y reescribilo en forma comprobable:\n'
        '(a) «El sistema debe ser rápido.»\n'
        '(b) «Todos los docentes pueden modificar los préstamos.»\n'
        '(c) «El sistema debe registrar la devolución y avisar al lector.»\n'
        '(d) «El sistema nunca debe prestar mal un libro.»',
    ]),
    ('Resolvé', [
        'Escribí el criterio de aceptación «Dado… cuando… entonces…» de RF-05 y el de RF-06.',
        'Aplicá la lista de revisión entre pares a estos requisitos de otro equipo. Para cada uno, anotá qué '
        'puntos de la lista no cumple:\n'
        '(a) «RF-11 El sistema debe ser intuitivo y registrar préstamos.» Fuente: E1-L10.\n'
        '(b) «RF-12 Usar PHP para que funcione sin internet.» Fuente: E4-L10.\n'
        '(c) «RF-04 El sistema debe listar los préstamos vencidos a una fecha de referencia.» Sin fuente.',
    ]),
    ('Pensá y decidí', [
        'Asigná prioridad (imprescindible, importante o deseable) a: RF-09, la renovación pedida en E3-L4, '
        'RF-04, RNF-01 y RF-07. Justificá cada una con el criterio de 4.3.',
    ]),
    ('Desafío', [
        'Escribí un criterio de aceptación para RNF-03 que una persona ajena al equipo pueda comprobar en '
        'menos de cinco minutos.',
    ]),
]

# ------------------------------------------------------------------ práctica
PRACTICA_TITULO = 'Práctica 4 — Convertir pedidos de usuarios en requisitos verificables'
PRACTICA_INTRO = [
    'La biblioteca abrió un buzón de pedidos durante una semana. Recibió los ocho de abajo. Son datos '
    'nuevos: no aparecen en el dossier ni en los ejemplos del capítulo. Trabajá en el nivel que te indique '
    'tu docente. Los tres niveles usan los mismos pedidos.',
]
BUZON_TITULO = 'Buzón de pedidos de la biblioteca (caso ficticio)'
BUZON = [
    ('B-01', 'Docente de Lengua', 'Quiero ver qué libros tiene prestados cada alumno de mi curso.'),
    ('B-02', 'Auxiliar de la tarde', 'Cuando un libro vuelve roto, quiero anotarlo para que no se preste hasta arreglarlo.'),
    ('B-03', 'Estudiante de 1.º', 'El sistema tiene que avisar rápido si el libro está.'),
    ('B-04', 'Dirección', 'Necesito impresos los préstamos por curso de cada mes.'),
    ('B-05', 'Estudiante de 3.º', 'Hagan una app con inicio de sesión de Google.'),
    ('B-06', 'Bibliotecaria', 'Que no se pueda prestar nada a quien tenga un libro vencido.'),
    ('B-07', 'Encargado de informática', 'Tiene que funcionar en la computadora de la biblioteca aunque se corte internet.'),
    ('B-08', 'Docente de Historia', 'Los datos de los alumnos tienen que estar protegidos, y todos tienen que poder ver todo.'),
]
FUENTES.update({cod: txt for cod, _, txt in BUZON})

NIVELES = [
    ('Nivel 1 — Guiado', [
        'Clasificá cada pedido (B-01 a B-08) como necesidad, requisito funcional, requisito de calidad, '
        'restricción, regla de negocio nueva o solución técnica. Si un pedido mezcla dos cosas, anotá las dos.',
        'Completá estas dos fichas:\n'
        'RF-__ El sistema debe mostrar ________ de un curso elegido. Fuente: ____. Prioridad: ________.\n'
        'Criterio: Dado ________, cuando ________, entonces ________.\n'
        'RS-__ El sistema debe funcionar ________. Fuente: ____.',
    ]),
    ('Nivel 2 — Intermedio', [
        'Redactá un catálogo con cuatro requisitos funcionales, dos de calidad y una restricción que salgan '
        'del buzón. Numeralos a partir de RF-11, RNF-04 y RS-03, porque el catálogo ya usa los anteriores. '
        'Cada uno con fuente, prioridad y criterio de aceptación.',
        'Corregí la ambigüedad de B-03 y la de B-08. Para cada una, escribí la pregunta que le harías a quien '
        'la pidió y una versión comprobable marcada «a confirmar».',
    ]),
    ('Nivel 3 — Ampliación', [
        'B-06 propone una regla nueva. Redactala como RN-07, explicá cómo se relaciona con RN-02 y RN-04, y '
        'escribí el requisito y el criterio de aceptación que la harían cumplir. ¿Quién tiene que aprobarla?',
        'B-02 implica un estado nuevo del ejemplar. Explicá qué cambia en el catálogo (qué requisitos se '
        'agregan o se modifican) sin proponer tablas ni código.',
        'Señalá la contradicción interna de B-08 y la relación con E5-L6. Proponé cómo la resolverías con los '
        'interesados, sin decidir por ellos.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: cada requisito tiene identificador nuevo, una fuente del buzón que lo '
                    'respalda, una sola acción, ninguna tecnología y un criterio «Dado… cuando… entonces…». '
                    'Ningún pedido de solución técnica (B-05) quedó copiado como requisito.')

CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros (Piloto C), este capítulo conserva sus dos encuentros: los requisitos '
    'son una evidencia esencial del proyecto.',
    'Si aun así se pierde un encuentro, no se omiten: el Ejemplo resuelto 4.2 (catálogo), el 4.3 (criterio de '
    'aceptación) y la Práctica 4 en el Nivel 1 o el Nivel 2. Pasan a lectura domiciliaria: la tabla de '
    'ambigüedades de 4.4 y las actividades «Pensá y decidí» y «Desafío».',
])

REPASO = ('Para repasar', [
    'La necesidad la expresa una persona; la regla la fija la institución; el requisito dice qué hace o '
    'cumple el sistema; la solución técnica dice cómo se construye.',
    'Hay requisitos funcionales, de calidad y restricciones.',
    'Cada requisito tiene identificador, fuente que lo respalda, prioridad y criterio de aceptación.',
    'Un criterio «Dado… cuando… entonces…» permite que otra persona compruebe el requisito.',
    'Las ambigüedades se corrigen preguntando al interesado, no inventando cifras.',
])

# ------------------------------------------------------------------ evaluación
EVAL_ID = 'ADS3-C4v2-2'   # semilla del barajado: reparte las claves en a, b, c y d
EVAL_TITULO = 'Evaluación del Capítulo 4'
EVAL_TEXTO_BASE = ('Texto base — Regla nueva propuesta por la bibliotecaria (caso ficticio)', [
    'R-07: «Los diccionarios y atlas se consultan en la biblioteca y no se prestan.»',
    'Fuente de los datos: la biblioteca tiene 4 diccionarios y 2 atlas, marcados en el catálogo como material '
    'de referencia.',
])
EVAL_ITEMS = [
    ('mc', '¿Cuál de estas frases es una regla de negocio?',
     ['Un lector puede tener como máximo dos préstamos activos.',
      'El sistema debe permitir buscar un título.',
      'Los datos se guardan en SQLite.',
      'Saber al instante quién tiene cada libro.']),
    ('mc', '¿Cuál de estos es un requisito de calidad?',
     ['La bibliotecaria debe poder registrar un préstamo sin ayuda, después de una práctica guiada.',
      'El sistema debe registrar la devolución de un préstamo.',
      'Usar un botón verde para confirmar el préstamo.',
      'Un ejemplar solo puede tener un préstamo activo.']),
    ('mc', '¿Cuál de estos criterios de aceptación es comprobable?',
     ['Dado un ejemplar prestado, cuando se intenta prestarlo otra vez, entonces se rechaza y queda un solo préstamo activo.',
      'Los préstamos funcionan bien.',
      'El sistema registra los préstamos de forma rápida y segura.',
      'La bibliotecaria queda conforme con el sistema.']),
    ('mc', '¿Qué problema tiene «El sistema debe registrar préstamos y generar el informe mensual»?',
     ['Es compuesto: une dos requisitos que se comprueban por separado.',
      'Es una regla de negocio.',
      'Nombra una tecnología.',
      'No tiene ningún problema.']),
    ('vf', 'Un requisito sin fuente puede quedar en el catálogo si al equipo le parece útil.',
     False, 'Falso. Sin fuente es una idea del equipo: se consulta con los interesados o se descarta.'),
    ('vf', 'Una restricción limita las soluciones posibles; por ejemplo, no tener presupuesto para servicios pagos.',
     True, 'Verdadero. Es una condición impuesta por el contexto (RS-02, E5-L4).'),
    ('vf', '«Usar un índice único en la base de datos» es un requisito funcional.',
     False, 'Falso. Es una solución técnica para cumplir RF-04; se decide en el diseño.'),
    ('ab', 'Reescribí «Los vencidos tienen que salir bien» como un requisito con identificador y su criterio '
           'de aceptación.',
     'Ejemplo: «RF-13 El sistema debe listar los préstamos activos cuya fecha de vencimiento es anterior a una '
     'fecha de referencia elegida.» Criterio: «Dado un préstamo que vence el 9 de marzo y otro que vence el 12, '
     'cuando se pide la lista con fecha de referencia 10 de marzo, entonces aparece solo el primero.» Se acepta '
     'otra redacción si fija la fecha de referencia y el resultado esperado.', 3),
    ('ab', 'Con el texto base: redactá la regla RN-07, el requisito funcional que la hace cumplir, su criterio '
           'de aceptación y su prioridad justificada. Indicá la fuente de cada uno.',
     'RN-07: el material de referencia (diccionarios y atlas) no se presta. Fuente: R-07. Requisito, por '
     'ejemplo: «RF-14 El sistema debe rechazar el préstamo de un ejemplar marcado como material de '
     'referencia.» Fuente: RN-07. Criterio: «Dado un diccionario marcado como referencia, cuando se intenta '
     'prestarlo, entonces el sistema lo rechaza y muestra el motivo.» Prioridad: imprescindible si la '
     'institución aprueba la regla, porque sin el requisito la regla se viola; importante si se acepta '
     'controlarla a mano. Se valora la justificación, no la etiqueta elegida.', 5),
]
