# -*- coding: utf-8 -*-
"""Capítulo 2 — «Investigar antes de diseñar» (Work §6: secciones 2.1 a 2.4; encuentros 3 y 4).
Se construye según fase2_pilotos/A1_candidato_capitulo2/integracion/PLAN_INTEGRACION_CAPITULO_2.md.
Los registros del dossier (E1 a E5, O1, D1, D2) y las necesidades N-01… se leen de caso/dossier.py.
INTEGRACION documenta el destino de cada elemento del candidato; build/verificar.py comprueba que los
elementos «Conservar» estén en el capítulo con el mismo texto."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'caso'))
import dossier as D
import mbokaja as MB

NUM = 2
UNIDAD = 'Unidad I — Comprender el problema y su contexto'
CAPITULO = 'Capítulo 2'
TITULO = 'Investigar antes de diseñar'
ENCUENTROS = (3, 4)
SECCIONES = ['2.1 Entrevistar para comprender tareas y problemas',
             '2.2 Observar un proceso y analizar documentos',
             '2.3 Contrastar fuentes, contradicciones y necesidades no expresadas',
             '2.4 Registrar evidencia con respeto por las personas y sus datos']
PRACTICA_WORK = 'dossier de relevamiento con roles de bibliotecario, lector y dirección'

ROTULO_CAPACIDAD = 'Capacidad propuesta para el programa institucional (C2; no es una capacidad oficial del MEC)'
CAPACIDAD = 'C2. Obtiene y contrasta información sobre necesidades de usuarios.'
TEMA = ('Relevamiento de información: necesidad y solución. Entrevista: preparación, guion y tipos de preguntas. '
        'Observación y análisis de documentos. Contraste de fuentes, contradicciones y necesidades no expresadas. '
        'Registro numerado; hechos, opiniones y supuestos. Autorización, anonimización y resguardo de los datos.')
INDICADORES = [
    'Prepara una entrevista con objetivo y guion de preguntas abiertas, sin preguntas inductoras, dobles ni técnicas.',
    'Elige la técnica de relevamiento (entrevista, observación, análisis de documentos) según lo que necesita averiguar.',
    'Registra la evidencia numerada y separa hechos, opiniones y supuestos.',
    'Contrasta dos fuentes o dos roles, registra las contradicciones y detecta necesidades no expresadas.',
    'Resguarda la información: pide autorización, anonimiza y limita el uso de los datos.',
]
TIEMPO = 'Dos encuentros de 5 HC (3 y 4 de la secuencia anual). Las 5 HC pueden repartirse en varios bloques semanales.'

APERTURA = [
    'En el Capítulo 1 armaste una ficha de problema con muchas filas marcadas «a verificar». Este capítulo es el '
    'de la verificación: vas a preguntar, mirar y leer, y vas a anotar lo que encuentres de modo que cualquiera '
    'pueda rastrear de dónde salió cada dato.',
    'Al terminar, el caso de Arapoty tiene un dossier de relevamiento: cinco entrevistas, una observación y dos '
    'documentos, con sus líneas numeradas, y una lista de necesidades con sus fuentes. Ese dossier es la base de '
    'todo lo que sigue. En el Capítulo 4, cada requisito va a citar la línea exacta que lo respalda.',
]
ARTICULACION = [
    'Con el Capítulo 1: el mapa de interesados (1.3) decide a quién entrevistar primero y con qué técnica.',
    'Con el Capítulo 4: la lista de necesidades N-01 a N-13 con que cierra este capítulo es el punto de partida de '
    'los requisitos. Acá todavía no se escriben requisitos.',
    'Con Castellano y Lengua Guaraní: preguntar con claridad, escuchar y registrar con fidelidad lo que otra '
    'persona dijo.',
]

# ------------------------------------------------------------------ encuentro 3
E3_TITULO = 'Encuentro 3 — Preparar el relevamiento'

# S41 del candidato, adaptado: sin requisitos (pasan al Capítulo 4).
S21 = ('2.1 Entrevistar para comprender tareas y problemas', [
    'Relevar (también se dice elicitar) es obtener, junto con los interesados, la información sobre su trabajo y '
    'sus necesidades. La palabra «elicitar» viene del inglés «elicit», que significa hacer salir algo que está '
    'escondido. Y eso es lo que pasa: casi nadie llega con sus necesidades ordenadas. La gente cuenta lo que le '
    'molesta, lo que hace todos los días y, muchas veces, la solución que se imagina.',
    'Por eso el analista distingue dos cosas que en una conversación aparecen mezcladas. La necesidad es lo que la '
    'persona tiene que lograr. La solución es una forma concreta de lograrlo. Si se salta directo a la solución, '
    'se pierde la necesidad, y con ella la posibilidad de encontrar una solución mejor o más barata. Un recordatorio '
    'del Capítulo 1: antes de relevar, el mapa de interesados indica a quién conviene escuchar de cerca.',
    'La entrevista es la técnica central de este encuentro, porque permite entender a fondo el trabajo de una '
    'persona clave. Pero una entrevista mal preparada produce datos malos, y a veces datos falsos, como vas a ver en '
    'el registro E1.',
])

TABLA_21 = (['Lo que dice el interesado (con su fuente)', 'Necesidad', 'Solución que aparece', 'Qué hace el analista'],
            [['«A veces tardo media hora.» (E1-L4), buscando quién llevó un libro', 'Saber rápido quién tiene cada libro', 'Ninguna todavía', 'Anota la necesidad con su fuente'],
             ['«¿No le parece que conviene una aplicación para el celular?» «Si usted dice… sí, capaz.» (E1-L11, E1-L12)', 'No se sabe: la sugirió el analista', 'Una aplicación para el celular', 'No la usa como dato; vuelve a preguntar sin inducir'],
             ['«Lo hago contando a mano y me lleva una tarde.» (E1-L8), sobre el informe mensual', 'Entregar el informe mensual sin perder una tarde', 'Ninguna todavía', 'Anota la necesidad y averigua quién usa el informe']])

CONCEPTO_RELEVAR = ('Relevamiento', [
    'Relevar es obtener, registrar y confirmar con los interesados la información sobre su trabajo y sus '
    'necesidades. Su producto no es el sistema ni su diseño, sino un dossier: registros con las líneas numeradas, '
    'hallazgos y una lista de necesidades, cada una con la fuente de donde salió.'])

# S44 del candidato, conservado.
S44_TITULO = 'Preparar y conducir una entrevista'
S44 = [
    'Una entrevista se prepara. Antes de ir, el analista escribe el objetivo (qué quiere averiguar), averigua lo que '
    'ya se sabe y arma un guion: una lista ordenada de preguntas que va de lo general a lo particular. El guion no '
    'se lee como un examen; es una guía para no olvidar nada.',
    'Las preguntas abiertas («¿Cómo es un día normal en la biblioteca?») invitan a contar y descubren cosas que el '
    'analista no imaginaba. Las cerradas («¿Cuántos préstamos hay por día?») precisan datos. Se empieza con abiertas '
    'y se cierra con cerradas. Hay tres tipos de preguntas que se evitan: la inductora, que sugiere la respuesta; la '
    'doble, que pregunta dos cosas a la vez; y la técnica, que usa palabras que el interesado no conoce.',
    'Durante la entrevista, el analista escucha más de lo que habla, pide ejemplos concretos («¿Me cuenta la última '
    'vez que pasó?») y toma notas. Al terminar, resume lo que entendió y pregunta si falta algo. El mismo día pasa en '
    'limpio las notas, porque al día siguiente ya se olvidan detalles.',
]

TABLA_PREGUNTAS = (['Pregunta a evitar', 'Problema', 'Versión mejorada'],
                   [['¿No le parece que lo mejor sería una app?', 'Inductora: sugiere la respuesta.', '¿Cómo le gustaría consultar si un libro está disponible?'],
                    ['¿Cuántos libros presta y cuántos se pierden?', 'Doble: pregunta dos cosas.', 'Dos preguntas separadas.'],
                    ['¿Necesita un CRUD con base relacional?', 'Técnica: usa jerga.', '¿Qué datos anota hoy cuando presta un libro?'],
                    ['¿El sistema actual funciona mal, no?', 'Inductora y negativa.', '¿Qué le resulta más difícil del sistema actual?']])

# EJ2 del candidato, conservado (renumerado como Ejemplo resuelto 2.1).
EJ21 = ('Ejemplo resuelto 2.1: el guion de la entrevista a la bibliotecaria', [
    'Objetivo: entender cómo se registran hoy los préstamos y cuáles son los problemas más costosos para la bibliotecaria.',
    'Apertura: presentarse, explicar el objetivo, pedir permiso para tomar notas y anunciar la duración aproximada.',
    'Preguntas abiertas:\n1. ¿Cómo es un día normal en la biblioteca?\n2. ¿Qué pasa cuando un libro no vuelve?\n3. ¿Qué le pide la dirección y cómo lo prepara?',
    'Preguntas para precisar:\n4. ¿Cómo sabe hoy si un libro está disponible?\n5. ¿Cuántos préstamos hay en un día de mucho movimiento?\n6. ¿Cuánto tarda en preparar el informe mensual?',
    'Cierre:\n7. Si pudiera cambiar una sola cosa, ¿cuál sería?\n8. ¿Hay algo que no le pregunté y que debería saber?',
    'Por qué está bien armado: empieza con preguntas abiertas, después precisa con cerradas y cierra dejando lugar a lo inesperado (pregunta 8). Ninguna pregunta sugiere la respuesta ni nombra una tecnología.',
])

LEAD_E1 = ('El registro E1 es lo que quedó de esa entrevista. Leelo con atención: el analista siguió buena parte del guion, '
           'pero al final agregó una pregunta que no estaba (E1-L11). En la sección 2.4 vas a ver qué consecuencia tuvo.')

# EN_PARAGUAY del candidato, conservado.
EN_PARAGUAY = ('Entrevistar en el idioma del interesado', [
    'La Constitución Nacional (art. 140) establece que el Paraguay es un país pluricultural y bilingüe, y que el '
    'castellano y el guaraní son idiomas oficiales. En una entrevista real, el interesado puede explicarse mejor en '
    'guaraní o en jopara. El analista no lo corrige: le permite hablar como se expresa mejor, anota la frase tal '
    'como se dijo y, al lado, su traducción. Así, quien lea después el registro puede volver a la expresión original '
    'si la traducción genera dudas.'])

RESGUARDO_PREVIO = ('Antes de relevar: criterios para resguardar la información', [
    '1. Pedir autorización: explicar para qué se hace la entrevista o la observación, quién va a leer las notas y '
    'que la persona puede no responder o terminar cuando quiera.',
    '2. No grabar audio ni sacar fotos de personas sin permiso expreso. En una observación, no anotar nombres.',
    '3. Acordar dónde se guardan las notas y quién puede leerlas: solo el equipo y el docente.',
    '4. Usar los datos solo para el proyecto. Lo que no se necesita, no se anota.',
    'La sección 2.4 desarrolla estos criterios. Tu equipo los escribe antes del relevamiento: es parte de la '
    'evidencia del Encuentro 3.',
])

# S43 del candidato, dividido: la entrevista quedó en 2.1; la observación y los documentos van acá.
S22 = ('2.2 Observar un proceso y analizar documentos', [
    'No hay una técnica que sirva para todo. La entrevista profundiza con pocas personas; el cuestionario llega a '
    'muchas, pero con preguntas cerradas; la observación muestra lo que la gente hace, que no siempre coincide con lo '
    'que dice. Un buen analista combina al menos dos técnicas y compara lo que encuentra con cada una.',
    'Observar un proceso es mirarlo mientras ocurre, sin intervenir. Se elige un momento representativo (para la '
    'biblioteca, el primer recreo, que la bibliotecaria señaló como el más difícil en E1-L2), se avisa y se pide '
    'autorización a quien trabaja, y se anotan hechos que se puedan contar: cuántas personas, cuánto tiempo, qué pasó. '
    'Las impresiones («había caos») no sirven; los conteos («14 estudiantes en fila») sí. Quien observa no anota '
    'nombres y trata de no cambiar lo que observa: si la bibliotecaria trabaja distinto porque la miran, el registro '
    'pierde valor.',
    'Analizar documentos es leer lo que la organización ya escribió: reglamentos, formularios, informes, carteles. '
    'Los documentos muestran reglas que nadie menciona en una entrevista porque las da por sabidas, y cifras que '
    'se pueden comprobar. Pero hay que leerlos con tres preguntas: ¿está vigente?, ¿quién lo escribió y para '
    'qué?, ¿se cumple en la práctica? Un reglamento que nadie aplica es un dato, pero de otro tipo.',
    'El documento también sugiere preguntas para la próxima entrevista. Si el reglamento dice que se anota el título '
    'y la bibliotecaria dice que no sabe a qué préstamo corresponde un libro devuelto, hay una pista: el cuaderno no '
    'distingue un ejemplar de otro del mismo título.',
])

# TABLA_TECNICAS del candidato, conservada.
TABLA_TECNICAS = (['Técnica', 'Sirve para…', 'Cuidado con…', 'En la biblioteca'],
                  [['Entrevista', 'Entender a fondo el trabajo y los problemas de una persona clave.', 'Preguntas inductoras; no tomar notas.', 'Entrevista a la bibliotecaria.'],
                   ['Observación directa', 'Ver cómo se trabaja de verdad, con tiempos y dificultades.', 'Molestar o cambiar la conducta del observado.', 'Mirar la atención en el primer recreo.'],
                   ['Cuestionario', 'Conocer la opinión de muchas personas en poco tiempo.', 'Preguntas confusas; muestras chicas.', 'Encuesta breve a estudiantes de todos los cursos.'],
                   ['Análisis de documentos', 'Conocer reglas, formularios e informes que ya existen.', 'Documentos viejos que ya no se aplican.', 'Reglamento de la biblioteca e informe mensual a la dirección.'],
                   ['Taller grupal', 'Reunir a varios interesados para generar ideas o acordar.', 'Que hable solo el que tiene más autoridad.', 'Reunión con delegados de curso y la bibliotecaria.']])

LEAD_FIG21 = ('Seguí las flechas: el relevamiento avanza en cinco pasos, pero no es una línea recta. La flecha punteada '
              'muestra que, si al confirmar el interesado corrige algo, se vuelve a obtener información.')
EPI_FIG21 = 'Figura 2.1 — El proceso de relevamiento y su retorno.'

EJ22 = ('Ejemplo resuelto 2.2: analizar el reglamento y el informe mensual', [
    'Consigna: leer los documentos D1 y D2, anotar qué muestra cada fragmento que importa para el problema y qué '
    'pregunta deja para la próxima entrevista.',
    'Paso 1. Ubicar cada documento: D1 es el reglamento vigente, aprobado por la dirección; D2 es el informe de '
    'marzo, escrito a mano por la bibliotecaria. El primero dice cómo deberían ser las cosas; el segundo, cómo '
    'salieron un mes.',
    'Paso 2. Leer fragmento por fragmento y anotar lo que muestra (Tabla 2.4). Las cifras se comprueban: los '
    'renglones D2-1 a D2-8 suman %d, y el total escrito es %d.' % (D.D2_SUMA_RENGLONES, D.D2_TOTAL_ESCRITO),
    'Paso 3. Convertir cada hallazgo en una pregunta. Así se preparó la segunda entrevista a la bibliotecaria (E4): '
    'su primera y su última pregunta salen de estos documentos (E4-L1 y E4-L11).',
])

TABLA_24 = (['Fragmento', 'Qué dice', 'Qué muestra o qué falta', 'Pregunta para la entrevista'],
            [['D1-A4', 'Se anota el lector, el curso, el título y la fecha', 'No se anota qué ejemplar sale; con varios ejemplares de un título, no se puede saber cuál volvió', '¿Cómo encuentra el préstamo cuando le devuelven un libro?'],
             ['D1-A3', 'Plazo de una semana; los docentes pueden pedir más con autorización', 'Hay una excepción prevista para docentes', '¿Cuántas veces se pide esa excepción y quién la autoriza?'],
             ['D2-8', '6 préstamos sin curso anotado', 'D1-A4 pide anotar el curso; en la práctica no siempre se hace', '¿Por qué algunos préstamos quedan sin curso?'],
             ['D2-9', 'Total: %d' % D.D2_TOTAL_ESCRITO, 'Los renglones suman %d: el informe tiene un error de suma' % D.D2_SUMA_RENGLONES, '¿Cómo arma el informe?']])

ACT_E3 = [
    ('Ejercitá', [
        'Clasificá cada frase como necesidad, solución o hecho:\n'
        '(a) «Tengo que saber qué libros están atrasados.»\n'
        '(b) «Quiero un lector de código de barras.»\n'
        '(c) «Los préstamos se anotan en un cuaderno.»\n'
        '(d) «Necesito que los chicos no hagan fila en el recreo.»\n'
        '(e) «Hagan una página con fondo verde.»\n'
        '(f) «En el primer recreo se llena la biblioteca.»',
        'Marcá si cada pregunta es abierta, cerrada o inductora:\n'
        '(a) ¿Cuántas computadoras tiene la biblioteca?\n'
        '(b) ¿Cómo organiza los libros en los estantes?\n'
        '(c) ¿Verdad que sería mejor que todo esté en la computadora?\n'
        '(d) ¿En qué horario hay más estudiantes?\n'
        '(e) ¿Qué hace cuando un estudiante no devuelve un libro?',
    ]),
    ('Resolvé', [
        'Escribí un guion de seis preguntas para entrevistar a un estudiante de 1.º que usa poco la biblioteca. '
        'Empezá con abiertas, terminá con cerradas y no nombres ninguna tecnología.',
        'Escribí los criterios de tu equipo para resguardar la información de una observación en la biblioteca: a '
        'quién se pide autorización, qué no se anota, dónde se guardan las notas, quién las lee y cuándo se descartan.',
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

# ------------------------------------------------------------------ encuentro 4
E4_TITULO = 'Encuentro 4 — Contrastar y registrar con cuidado'

S23 = ('2.3 Contrastar fuentes, contradicciones y necesidades no expresadas', [
    'Ninguna fuente alcanza sola. La bibliotecaria dice que en el recreo «anoto apurada y después no entiendo mi '
    'letra» (E1-L2); la observación cuenta 14 estudiantes en fila y 9 préstamos en un recreo (O1-1, O1-2); y en '
    'la segunda entrevista ella cuenta que, con apuro, anotó el mismo libro a dos chicos (E4-L4). Tres fuentes '
    'distintas apuntan a lo mismo. Cuando las fuentes coinciden, el hallazgo se fortalece. Comparar fuentes sobre '
    'una misma cuestión se llama contrastar o triangular.',
    'Cuando las fuentes no coinciden, la diferencia también es información. Hay tres clases de contradicción '
    'frecuentes. Entre personas: la docente necesita los libros «Tres semanas, como mínimo» (E2-L8), y el '
    'reglamento fija una semana (D1-A3). Entre lo que se escribe y lo que se hace: el reglamento pide anotar el curso '
    '(D1-A4), y seis préstamos de marzo no lo tienen (D2-8). Entre cifras: los renglones del informe no suman el '
    'total escrito (D2-9).',
    'Un conflicto aparece cuando dos interesados piden cosas incompatibles. El analista no decide quién gana: '
    'registra las dos posiciones, busca la necesidad que hay detrás de cada una y lleva el conflicto a quien tiene '
    'autoridad para resolverlo, con opciones. En el caso, la directora lo dice con claridad: el reglamento se puede '
    'revisar «si la bibliotecaria y los docentes proponen un cambio» (E5-L8).',
    'Por último, hay necesidades que nadie dice. Aparecen en la observación o en los documentos, pero no en las '
    'entrevistas, porque las personas no las ven o las dan por sabidas. Son las necesidades no expresadas, y '
    'suelen ser las que más sorprenden al final de un proyecto si nadie las buscó.',
])

LEAD_FIG22 = ('Observá la figura: tres fuentes de distinto tipo (lo que se dice, lo que se ve y lo que se cuenta después) '
              'sostienen un mismo hallazgo. Si una sola fuente lo dijera, el hallazgo sería más débil.')
EPI_FIG22 = 'Figura 2.2 — Contraste de fuentes: tres registros del dossier sostienen el mismo hallazgo.'

# EJ5 del candidato, adaptado: la situación hipotética se reemplaza por una contradicción real del dossier.
EJ23 = ('Ejemplo resuelto 2.3: una contradicción sobre el plazo de préstamo', [
    'Situación: la docente de Castellano necesita unos treinta ejemplares de una novela durante tres semanas (E2-L2, '
    'E2-L8); el reglamento fija una semana de plazo (D1-A3).',
    'Paso 1. Registrar las dos posiciones, cada una con su fuente: E2-L8 frente a D1-A3.',
    'Paso 2. Buscar la necesidad detrás de cada una. Docente: que todo el curso lea la misma novela sin atrasarse '
    '(E2-L6). Reglamento y bibliotecaria: que los libros circulen y vuelvan.',
    'Paso 3. Revisar si el propio documento prevé una salida. D1-A3 permite a los docentes «un plazo mayor con '
    'autorización de la dirección»: la contradicción no es total, pero falta saber cómo se pide y quién lleva la '
    'cuenta de esos libros.',
    'Paso 4. Proponer opciones sin elegir: (a) plazo de tres semanas solo para lotes del plan lector, autorizado por '
    'la dirección; (b) una semana con renovaciones; (c) préstamo del lote a la docente, que responde por los '
    'ejemplares.',
    'Paso 5. Elevar a la directora, que tiene la autoridad (E5-L8), con las tres opciones. La necesidad queda en la '
    'lista como N-12, con el estado «En conflicto con el plazo del reglamento».',
])

EJ24 = ('Ejemplo resuelto 2.4: buscar necesidades no expresadas', [
    'Consigna: revisar la observación y los documentos y anotar lo que muestran y nadie dijo en las entrevistas.',
    'O1-3: cinco de catorce estudiantes se fueron sin libro. Nadie mencionó a los lectores que abandonan la fila: '
    'es una demanda que hoy no queda registrada. Pregunta para la dirección: ¿le serviría saber cuántos pedidos no '
    'se atienden?',
    'D2-8: seis préstamos sin curso. La directora pide los préstamos por curso (E5-L2), pero el informe no puede ser '
    'exacto si el curso no se anota siempre. Necesidad implícita: que el curso del lector quede registrado en cada '
    'préstamo.',
    'D2-9: el total escrito no coincide con la suma. Nadie dijo «el informe tiene errores»; la bibliotecaria lo '
    'confirmó recién cuando se le preguntó (E4-L12). Esto se suma a la necesidad N-06: obtener el informe sin '
    'errores de suma.',
    'Cada necesidad no expresada se confirma después con el interesado. Si él no la reconoce como propia, se '
    'registra igual, como hallazgo del equipo, con su fuente.',
])

# S45 del candidato, adaptado a las categorías de Work: hechos, opiniones y supuestos.
S24 = ('2.4 Registrar evidencia con respeto por las personas y sus datos', [
    'El registro es el documento que queda de cada entrevista, observación o documento. Se numeran las líneas para '
    'poder citarlas: «E1-L4» significa entrevista 1, línea 4; «O1-3», observación 1, renglón 3; «D1-A4», '
    'documento 1, artículo 4. Junto al registro se anotan la fecha aproximada, el lugar, la duración y qué autorizó '
    'la persona.',
    'Después, cada frase importante se clasifica de dos maneras. Por su naturaleza: un hecho se puede comprobar (lo '
    'que pasó, lo que se hace, una cifra contada); una opinión expresa lo que una persona piensa o desea, y vale '
    'como dato de lo que esa persona piensa, no de cómo son las cosas; un supuesto es algo que alguien da por cierto '
    'sin evidencia, como una estimación que nadie verificó. Por su contenido: describe el proceso, señala un '
    'problema, expresa una necesidad o propone una solución.',
    'Las propuestas no se descartan, pero tampoco se copian como necesidades: se pregunta qué necesidad hay detrás. '
    'Y si una propuesta apareció porque el analista la sugirió, no vale como dato: es un error de la entrevista, y '
    'se vuelve a preguntar de otra manera. Eso pasó en E1-L11 y E1-L12.',
])

# EJ3 del candidato, adaptado: hallazgos con las categorías de Work.
EJ25 = ('Ejemplo resuelto 2.5: del registro a los hallazgos', [
    'Consigna: leer el registro E1, extraer los hallazgos y clasificarlos. Cada hallazgo lleva un código (H1, H2…) y '
    'la línea de donde sale.',
    'Cómo se hizo: se leyó cada respuesta de Mirta y se subrayaron las frases que describen el proceso, señalan un '
    'problema, expresan una necesidad o proponen una solución. Después se marcó si cada una es un hecho, una opinión '
    'o un supuesto. Las cifras se anotan tal como se dijeron, marcadas «a verificar», porque son estimaciones de la '
    'entrevistada.',
])

# TABLA_HALLAZGOS del candidato, adaptada: columna nueva «Naturaleza».
TABLA_HALLAZGOS = (['Cód.', 'Fuente', 'Hallazgo', 'Naturaleza', 'Contenido'],
                   [['H1', 'E1-L2', 'Los préstamos se anotan a mano en un cuaderno.', 'Hecho', 'Proceso'],
                    ['H2', 'E1-L2', 'Con fila, la letra queda ilegible y después no se entiende.', 'Hecho relatado; lo confirma O1', 'Problema'],
                    ['H3', 'E1-L4', 'Encontrar quién tiene un libro puede llevar media hora.', 'Hecho relatado; la cifra, a verificar', 'Problema'],
                    ['H4', 'E1-L4', 'Faltan unos 40 libros por año y no se sabe quién los tiene.', 'Supuesto: estimación, a verificar con el inventario', 'Problema'],
                    ['H5', 'E1-L6', 'No se distingue un libro prestado de uno mal ubicado o perdido.', 'Hecho', 'Problema'],
                    ['H6', 'E1-L8', 'La dirección pide un informe mensual de préstamos por curso; hoy lleva una tarde.', 'Hecho', 'Problema'],
                    ['H7', 'E1-L10', 'Saber al instante quién tiene cada libro.', 'Opinión: deseo de la bibliotecaria', 'Necesidad'],
                    ['H8', 'E1-L10', 'Que el sistema sea «fácil» para alguien que no es de computadoras.', 'Opinión ambigua: hay que precisar «fácil»', 'Necesidad'],
                    ['H9', 'E1-L11, E1-L12', 'Aplicación para el celular: la sugirió el analista.', 'No vale como dato', 'Propuesta inducida']])

RESGUARDO_TITULO = 'Autorización, anonimización y resguardo'
RESGUARDO = [
    'Relevar es entrar en el trabajo de otras personas, y eso exige cuidado. La autorización se pide antes, no '
    'después: se explica para qué es la entrevista, quién va a leer las notas y que la persona puede no responder. '
    'En el dossier queda escrito qué autorizó cada una; por ejemplo, la directora pidió revisar su registro antes de '
    'que se use (contexto de E5), y en la observación no se anotaron nombres (contexto de O1).',
    'Anonimizar es quitar del registro lo que permite identificar a una persona que no necesita ser identificada. '
    'En el caso del libro, todos los nombres son inventados. En un relevamiento real, sobre todo con menores de '
    'edad, el nombre del estudiante se reemplaza por un código («Lector 1»), y se quitan los datos que lo delatan '
    'aunque no lleven nombre, como «el único delegado de 2.º». Los registros reales no se publican ni se comparten '
    'fuera del equipo y del docente.',
    'Resguardar es decidir dónde se guardan las notas, quién puede leerlas y cuándo se descartan. Lo que no se '
    'necesita para el proyecto no se anota. Y el prototipo que el curso construya va a usar datos inventados, nunca '
    'los datos reales de los lectores.',
]
TABLA_26 = (['Principio', 'Qué hace el equipo', 'Cómo se ve en el dossier del caso'],
            [['Autorización', 'Explica el objetivo y pide permiso antes de relevar', 'Cada registro dice qué autorizó la persona'],
             ['Mínimo necesario', 'Anota solo lo que el proyecto necesita', 'La observación O1 cuenta personas; no las nombra'],
             ['Anonimización', 'Reemplaza nombres reales por códigos y quita datos que identifican', 'Nombres ficticios; en un caso real, «Lector 1»'],
             ['Resguardo', 'Guarda las notas donde solo el equipo y el docente las leen', 'El dossier no se publica'],
             ['Confirmación', 'Devuelve el registro a la persona para que lo corrija', 'La directora revisa su registro E5']])

# S48 del candidato, adaptado: confirmar con el interesado.
CONFIRMAR = ('Confirmar con el interesado', [
    'El último paso es la devolución: se le muestra al interesado la lista de hallazgos y necesidades, y se le '
    'pregunta si eso es lo que quiso decir. Puede ser una reunión corta o una hoja que lee y firma. Si corrige algo, '
    'se vuelve a obtener información (la flecha punteada de la Figura 2.1). Confirmar evita el error más caro del '
    'desarrollo de sistemas: construir algo que nadie pidió.'])

NECESIDADES_INTRO = ('El dossier cierra con la lista de necesidades. Cada una tiene un código que no se reutiliza, sus '
                     'fuentes y su estado. Es el punto de partida del Capítulo 4: allí, por ejemplo, N-02 se convierte '
                     'en una regla, un requisito y una prueba.')

ACT_E4 = [
    ('Ejercitá', [
        'Indicá si cada fragmento es un hecho, una opinión o un supuesto, y justificá en una línea:\n'
        '(a) «Ella cuenta los ejemplares en el estante y a veces faltan cinco o seis.» (E2-L4)\n'
        '(b) «Ah, y el sistema tiene que ser rápido.» (E2-L11)\n'
        '(c) «A fin de año faltan unos cuarenta libros» (E1-L4)\n'
        '(d) «Al tocar el timbre de salida al recreo había 14 estudiantes en fila.» (O1-1)\n'
        '(e) «Me gustaría saber antes de venir si lo hay.» (E3-L3)\n'
        '(f) «La biblioteca atiende de lunes a viernes, de 7:00 a 12:30.» (D1-A1)',
    ]),
    ('Resolvé', [
        'Escribí la hoja de confirmación para Mirta: un título, las necesidades N-01, N-02, N-04, N-05 y N-06 con '
        'palabras que ella entienda, y dos preguntas para cerrar las dudas pendientes.',
        'Registrá la contradicción entre D1-A4 y D2-8 con el formato del Ejemplo resuelto 2.3: las dos posiciones con '
        'su fuente, la necesidad detrás de cada una y la pregunta que harías.',
    ]),
    ('Pensá y decidí', [
        'La directora dice: «No hay presupuesto para comprar programas ni para pagar un servicio en internet.» (E5-L4). '
        'Un lector pide: «Me gustaría saber antes de venir si lo hay.» (E3-L3). ¿Hay conflicto entre las dos '
        'posiciones? Explicá la necesidad de cada uno y qué le preguntarías al encargado de informática, a quien '
        'todavía nadie entrevistó.',
    ]),
    ('Desafío', [
        'Reescribí la pregunta E1-L11 para que no sea inductora. Después explicá qué perdió el analista al preguntar '
        'como preguntó.',
    ]),
]

# ------------------------------------------------------------------ práctica
PRACTICA_TITULO = 'Práctica 2 — Dossier de relevamiento con roles'
PRACTICA_INTRO = [
    'Vas a relevar la biblioteca de la Escuela Básica Mbokaja, la misma de la Práctica 1, con una simulación. En '
    'cada grupo, tres compañeros hacen los papeles del encargado de la biblioteca, de una lectora y de la dirección, '
    'con una tarjeta que les da tu docente. Los demás son analistas: preparan el guion, entrevistan y registran. Los '
    'que hacen un papel responden solo con lo que dice su tarjeta; lo que no está, no lo saben. Algunos datos '
    'aparecen únicamente si la pregunta está bien hecha.',
    'Además de las entrevistas, los analistas cuentan con un documento: las normas de la biblioteca. Numerá tus '
    'registros como en el dossier del caso (R1-L1, R1-L2…) y anotá qué autorizó cada persona.',
]
NIVELES = [
    ('Nivel 1 — Guiado', [
        'Prepará un guion de cinco preguntas para el encargado: tres abiertas y dos cerradas, sin preguntas '
        'inductoras. Incluí una sobre cómo se presta a los docentes.',
        'Hacé la entrevista y registrá al menos ocho líneas numeradas. Clasificá seis de ellas como hecho, opinión o '
        'supuesto.',
        'Encontrá una contradicción entre lo que dijo el encargado y una de las normas (M-N1 a M-N5). Anotá las dos '
        'fuentes.',
    ]),
    ('Nivel 2 — Intermedio', [
        'Entrevistá al encargado y a la lectora, y analizá las normas. Armá la tabla de hallazgos (código, fuente, '
        'hallazgo, naturaleza, contenido) con al menos ocho hallazgos de dos fuentes distintas.',
        'Registrá dos contradicciones, cada una con sus dos fuentes y la necesidad detrás de cada posición.',
        'Cerrá el dossier con una lista de cuatro a seis necesidades de Mbokaja, cada una con su código y sus fuentes.',
    ]),
    ('Nivel 3 — Ampliación', [
        'Entrevistá a la lectora y a la dirección, y contrastá sus posiciones: ¿qué necesita cada una y en qué '
        'chocan?',
        'Anotá una necesidad no expresada: algo que muestra el relevamiento y que nadie pidió. Indicá de qué fuentes '
        'sale.',
        'Proponé dos opciones para el conflicto principal, con una ventaja y una desventaja de cada una, sin elegir, e '
        'indicá quién debería decidir. Por último, anonimizá tu dossier: reemplazá los nombres por códigos y quitá '
        'cualquier dato que permita identificar a la lectora.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: cada línea del registro tiene su código; cada hallazgo y cada necesidad citan '
                    'una fuente que existe; las contradicciones muestran las dos fuentes; ninguna propuesta quedó '
                    'como necesidad; los registros dicen qué autorizó cada persona y no tienen datos innecesarios.')

REPASO = ('Para repasar', [
    'Relevar es obtener, registrar y confirmar necesidades con los interesados, no preguntar «¿qué quiere?».',
    'Se combinan técnicas: la entrevista profundiza, la observación muestra lo que realmente pasa y los documentos dicen cómo deberían ser las cosas.',
    'Cada línea del registro tiene un código y cada hallazgo, su fuente. Se separan hechos, opiniones y supuestos.',
    'Las contradicciones se registran con sus dos fuentes y se elevan con opciones a quien decide; las necesidades no expresadas se buscan en la observación y en los documentos.',
    'Se pide autorización, se anota solo lo necesario, se anonimiza y se resguarda.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, este capítulo conserva sus dos encuentros sin fusión: el relevamiento es la '
    'base de todo el proyecto.',
    'Si aun así se pierde uno, no se omiten: el Ejemplo resuelto 2.1 (guion), los criterios de resguardo, el Ejemplo '
    'resuelto 2.3 (contradicción) y la Práctica 2 en el Nivel 1 o el Nivel 2. Pasan a lectura domiciliaria: el '
    'Ejemplo resuelto 2.4, la Tabla 2.3 y las actividades «Pensá y decidí» y «Desafío».',
])

# ------------------------------------------------------------------ evaluación (EVAL_ITEMS del candidato, adaptado)
EVAL_ID = 'ADS3-L1-C2-i'   # semilla elegida para repartir las claves entre a, b y c
EVAL_TITULO = 'Evaluación del Capítulo 2'
EVAL_TEXTO_BASE = ('Texto base — Préstamo de microscopios (situación de evaluación, ficticia)', [
    'T1-L1 Encargada del laboratorio: Prestamos los microscopios solo para usarlos dentro del laboratorio, nunca para llevarlos al aula.',
    'T1-L2 Encargada del laboratorio: Creo que los docentes de 7.º los usan poco porque no saben cómo pedirlos.',
    'T1-L3 Encargada del laboratorio: El mes pasado se rompió uno, y no sé quién lo tenía porque ese día no anoté.',
    'T1-L4 Encargada del laboratorio: Para mí, habría que comprar microscopios digitales.',
    'T2-1 Norma del laboratorio: Los docentes pueden retirar materiales para usarlos en el aula, firmando la planilla de salida.',
    'T2-2 Norma del laboratorio: Cada salida de material se anota con la fecha, el docente y el material.',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(': ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', '¿Qué es relevar información en un proyecto de sistemas?',
     ['Obtener, registrar y confirmar con los interesados la información sobre su trabajo y sus necesidades.',
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
    ('mc', 'En el texto base, T1-L2 es…',
     ['un supuesto: la encargada da por cierta una causa que nadie comprobó.',
      'un hecho observado.',
      'una norma del laboratorio.',
      'una necesidad no expresada.']),
    ('vf', 'Una propuesta de solución del interesado («quiero una app») es una necesidad y se copia tal cual en el dossier.',
     False, 'Falso. Es una propuesta: se pregunta qué necesidad hay detrás y recién de ahí sale la necesidad.'),
    ('vf', 'Cada hallazgo del dossier debe indicar de qué entrevista, observación o documento salió.',
     True, 'Verdadero. Es la trazabilidad, que permite discutir y confirmar cada hallazgo.'),
    ('vf', 'Cuando dos interesados piden cosas incompatibles, el analista elige la mejor y descarta la otra.',
     False, 'Falso. El analista registra ambas posiciones, busca las necesidades y eleva el conflicto con opciones a quien decide.'),
    ('ab', 'Clasificá T1-L1, T1-L3 y T1-L4 como hecho, opinión o supuesto, y señalá cuál de ellas es una propuesta de '
           'solución. Justificá cada respuesta.',
     'T1-L1: hecho (describe cómo se presta; se puede comprobar). T1-L3: hecho (se rompió uno y no se anotó). T1-L4: '
     'opinión que contiene una propuesta de solución (comprar microscopios digitales); se registra y se pregunta qué '
     'necesidad hay detrás. Un punto por cada clasificación justificada y uno por identificar la propuesta.', 4),
    ('ab', 'Con el texto base: registrá una contradicción entre lo que dice la encargada y las normas, con sus dos '
           'fuentes, y anotá una necesidad que nadie expresó. ¿A quién elevarías la contradicción?',
     'Contradicción: T1-L1 (solo dentro del laboratorio) frente a T2-1 (los docentes pueden retirar materiales para el '
     'aula). También vale T1-L3 frente a T2-2 (no se anotó una salida). Necesidad no expresada: saber en todo momento '
     'quién tiene cada microscopio (sale de T1-L3 y T2-2). Se eleva a la dirección o a quien aprobó las normas, con '
     'opciones. Un punto por cada fuente citada, uno por la necesidad y uno por indicar a quién se eleva.', 4),
]
EVAL_PUNTAJE = 'Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno).'

# ------------------------------------------------------------------ integración del candidato
# (elemento del candidato, destino, acción). Se reproduce en la guía y en el informe del lote.
INTEGRACION = [
    ('S41', '2.1', 'Adaptar'), ('TABLA_NRS', '2.1 (Tabla 2.1)', 'Adaptar'), ('CONCEPTO_ELICITAR', '2.1', 'Adaptar'),
    ('S42', 'Capítulo 1 (1.3)', 'Trasladar'), ('EJ1', 'Capítulo 1 (Ejemplo resuelto 1.3)', 'Trasladar'),
    ('TABLA_EJ1', 'Capítulo 1 (Tabla 1.4)', 'Trasladar'), ('S43', '2.1 y 2.2', 'Dividir'),
    ('TABLA_TECNICAS', '2.2 (Tabla 2.3)', 'Conservar'), ('EN_PARAGUAY', '2.1', 'Conservar'), ('S44', '2.1', 'Conservar'),
    ('TABLA_PREGUNTAS', '2.1 (Tabla 2.2)', 'Conservar'), ('EJ2', '2.1 (Ejemplo resuelto 2.1)', 'Conservar'),
    ('S45', '2.4', 'Adaptar'), ('TRANSCRIPCION_E1', '2.1 (registro E1)', 'Conservar'),
    ('EJ3', '2.4 (Ejemplo resuelto 2.5)', 'Adaptar'), ('TABLA_HALLAZGOS', '2.4 (Tabla 2.5)', 'Adaptar'),
    ('S46', 'Capítulo 4', 'Retirar'), ('CONCEPTO_RC', 'Capítulo 4', 'Retirar'), ('EJ4', 'Capítulo 4', 'Retirar'),
    ('TABLA_RC', 'Capítulo 4', 'Retirar'), ('S47', '2.3', 'Adaptar'), ('EJ5', '2.3 (Ejemplo resuelto 2.3)', 'Adaptar'),
    ('S48', '2.4', 'Adaptar'), ('TRANSCRIPCION_E2', '2.3 (registro E2)', 'Conservar'),
    ('OBSERVACION_O1', '2.2 (registro O1)', 'Conservar'), ('ACT_E7', 'Actividades del Encuentro 3', 'Adaptar'),
    ('ACT_E8', 'Actividades del Encuentro 4', 'Adaptar'), ('NIVELES', 'Práctica 2', 'Adaptar'),
    ('EVAL_ITEMS', 'Evaluación del Capítulo 2', 'Adaptar'), ('CALENDARIO_REDUCIDO', 'Capítulo 2', 'Adaptar'),
    ('REPASO', 'Capítulo 2', 'Adaptar'),
]
