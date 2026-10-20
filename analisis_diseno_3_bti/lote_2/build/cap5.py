# -*- coding: utf-8 -*-
"""Capítulo 5 — «Procesos, contexto y casos de uso» (Work §6: secciones 5.1 a 5.4 y práctica; encuentros 9 y 10).

Notaciones de `lote_2_plan/NOTACIONES_CAPITULO_5.md` (aprobadas): diagrama de actividades UML con particiones (5.1),
diagrama de contexto (5.2) y diagrama de casos de uso UML (5.3 y 5.4); los escenarios y los flujos alternativos van en
una plantilla de texto. Los modelos del caso están en caso/modelos.py y las figuras se dibujan desde ahí.
Modela procesos e interacciones, no tablas ni datos (no duplica Algorítmica 3.º; sin diagramas entidad-relación).
La Práctica 5 usa el caso de transferencia Mbokaja con situaciones que no aparecen en los ejemplos (Work §7.4)."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'caso'))
import requisitos as R
import modelos as MO
import mbokaja_u2 as MB
D = R.D

NUM = 5
UNIDAD = 'Unidad II — Especificar qué debe resolver el sistema'
CAPITULO = 'Capítulo 5'
TITULO = 'Procesos, contexto y casos de uso'
ENCUENTROS = (9, 10)
SECCIONES = ['5.1 Proceso actual y proceso propuesto',
             '5.2 Diagrama de contexto y límites de intercambio de información',
             '5.3 Actores, casos de uso y escenarios principales',
             '5.4 Excepciones, decisiones y flujos alternativos']
PRACTICA_WORK = 'modelar préstamo y devolución con situaciones problemáticas nuevas'

ROTULO_CAPACIDAD = ('Capacidades propuestas para el programa institucional (C4 y C3; no son capacidades oficiales '
                    'del MEC)')
CAPACIDAD = ('C4. Modela procesos e interacciones del sistema.\n'
             'C3. Especifica y prioriza requisitos verificables.')
TEMA = ('Proceso actual y proceso propuesto con diagramas de actividades con carriles. Diagrama de contexto: sistema, '
        'entidades externas y flujos de información. Actores, casos de uso, escenarios principales, excepciones y '
        'flujos alternativos. Coherencia entre los modelos y el catálogo de requisitos.')
INDICADORES = [
    'Representa el proceso actual y el proceso propuesto con un diagrama de actividades con carriles, y señala qué problema del dossier resuelve cada cambio.',
    'Delimita el sistema con un diagrama de contexto: entidades externas y la información que entra y sale.',
    'Identifica actores como roles y desarrolla tres casos de uso prioritarios con su escenario principal.',
    'Describe al menos un flujo alternativo por caso de uso, con su punto de decisión y su resultado.',
    'Mantiene la coherencia entre los modelos y el catálogo: cada requisito citado existe y cada notación se usa sola.',
]
TIEMPO = ('Dos encuentros de 5 HC (9 y 10 de la secuencia anual). Las 5 HC pueden repartirse en varios bloques '
          'semanales.')

APERTURA = [
    'Con el catálogo del Capítulo 4 sabés qué tiene que hacer el sistema. Falta ver cómo encaja en el trabajo de las '
    'personas: quién hace cada paso, qué decide el sistema y qué pasa cuando algo sale distinto de lo previsto.',
    'En este capítulo dibujás tres modelos: el proceso de préstamo antes y después del sistema, el contexto con la '
    'información que entra y sale, y los casos de uso con sus escenarios. Cada modelo usa una sola notación, y cada '
    'paso del sistema cita el requisito que lo justifica. Un buen modelo no es un adorno: sirve para explicar y para '
    'descubrir lo que falta.',
]
ARTICULACION = [
    'Con el Capítulo 4: cada acción del sistema, cada caso de uso y cada flujo alternativo citan requisitos del '
    'catálogo (RF-01 a RF-10, RNF-01 a RNF-03, RS-01 y RS-02). Si un modelo necesita algo que el catálogo no tiene, se '
    'anota como requisito nuevo «a confirmar».',
    'Con Dibujo Técnico de 1.º: de ahí vienen la legibilidad, el trazo y las convenciones de un diagrama. Acá se aprende '
    'qué significa cada símbolo.',
    'Con Algorítmica 3.º: allí se trabajan los datos, las claves y las tablas de una biblioteca. Acá no se diseñan '
    'tablas ni se dibujan diagramas de datos: se modelan procesos e interacciones. Los datos se diseñan en el '
    'Capítulo 7.',
]

# ------------------------------------------------------------------ encuentro 9
E9_TITULO = 'Encuentro 9 — Proceso actual y proceso propuesto'

S51 = ('5.1 Proceso actual y proceso propuesto', [
    'Un proceso es una serie de tareas que se hacen en orden para lograr algo: prestar un libro, devolverlo. Antes de '
    'proponer cómo debería funcionar, hay que dibujar cómo funciona hoy. El proceso actual muestra dónde están los '
    'problemas que encontró el relevamiento. El proceso propuesto muestra qué cambia con el sistema, quién hace cada '
    'paso y qué decisiones pasan a tomarse de otra manera.',
    'Para dibujar los dos procesos se usa el diagrama de actividades de UML con particiones, también llamadas carriles. '
    'UML es un lenguaje de modelado muy usado en el desarrollo de software. Cada carril es una columna con el nombre de '
    'un participante: todo lo que está en su columna lo hace él. Así se ve de un vistazo quién es responsable de cada '
    'acción y dónde la tarea pasa de una persona a otra.',
    'La Figura 2.1 del Capítulo 2 era un esquema didáctico del trabajo del equipo y no usaba UML. Desde acá, los procesos '
    'del sistema se representan con esta notación, y solo con ella.',
])

LEYENDA_ACTIVIDAD = 'Tabla 5.1 — Símbolos del diagrama de actividades'
NOTA_LEYENDA_ACTIVIDAD = ('Fuera del núcleo del libro quedan otros símbolos de este diagrama (barras de bifurcación y '
                          'unión, nodo final de flujo, objetos): el préstamo y la devolución no los necesitan.')

LEAD_FIG51 = ('Observá la Figura 5.1: el proceso actual de préstamo y devolución en siete acciones, con dos carriles. '
              'Los números (1), (2) y (3) marcan los pasos donde aparecen los problemas del dossier (Tabla 5.2).')
EPI_FIG51 = 'Figura 5.1 — Proceso actual de préstamo y devolución en la biblioteca (diagrama de actividades, caso ficticio).'

TABLA_52_ROTULO = 'Tabla 5.2 — Problemas del dossier en el proceso actual'
TABLA_52 = (['Marca', 'Paso', 'Problema', 'Fuentes'],
            [[m, p, t, ', '.join(f)] for m, p, t, f in MO.PROBLEMAS_ACTUAL])

EJ51 = ('Ejemplo resuelto 5.1: del relato al proceso actual', [
    'Consigna: dibujar el proceso actual de préstamo y devolución a partir del dossier y marcar sus problemas.',
    'Paso 1. Elegir los participantes. En el préstamo de hoy intervienen el lector y la bibliotecaria: dos carriles. '
    'La dirección no participa del préstamo, aunque reciba el informe.',
    'Paso 2. Ordenar las acciones con verbo en infinitivo y objeto. El reglamento dice qué se anota (D1-A4) y la '
    'bibliotecaria contó cómo busca un préstamo al devolverse un libro (E4-L2). Quedan siete acciones.',
    'Paso 3. Ubicar las decisiones. Hay una sola en el préstamo de hoy: ¿el libro está en el estante? Cada salida lleva '
    'su guarda: «[está en el estante]» y «[no está]». Si no está, el proceso termina en un segundo nodo final.',
    'Paso 4. Marcar los problemas. Junto a cada acción con un problema se anota un número, y la Tabla 5.2 dice cuál es '
    'y de qué fuente sale. El diagrama no lleva símbolos ajenos a la notación: las explicaciones van en la tabla.',
    'Paso 5. Revisar con la lista de reglas: un nodo inicial, al menos un nodo final, todas las salidas de la decisión '
    'con guarda y cada acción en un carril.',
])

LEAD_FIG52 = ('Ahora comparalo con la Figura 5.2. Aparece un tercer carril, «Sistema», y las comprobaciones que antes '
              'nadie hacía pasan a ese carril. Cada acción del sistema cita el requisito del catálogo que la justifica.')
EPI_FIG52 = 'Figura 5.2 — Proceso propuesto de préstamo, con el carril del sistema (diagrama de actividades).'

TABLA_53_ROTULO = 'Tabla 5.3 — Qué cambia del proceso actual al proceso propuesto'
TABLA_53 = (['Paso', 'Hoy', 'Con el sistema', 'Decisión y efecto'],
            [list(x) for x in MO.CAMBIOS_PROCESO])

EJ52 = ('Ejemplo resuelto 5.2: justificar el proceso propuesto', [
    'Consigna: explicar por qué cada comprobación del sistema está donde está.',
    'La comprobación del lector va antes que la del ejemplar: si el lector está inactivo (RN-04) o ya tiene el máximo '
    'vigente (RN-02), no hace falta revisar el ejemplar. Es una decisión del equipo; el orden inverso también cumple '
    'las reglas, pero obliga a buscar el ejemplar en vano.',
    'Las dos salidas de rechazo se juntan en un rombo de fusión antes de «Mostrar el motivo del rechazo»: el sistema '
    'hace lo mismo en los dos casos, aunque el motivo sea distinto. El rombo de fusión no lleva guardas, porque no '
    'decide nada.',
    'La bibliotecaria sigue en el proceso. El sistema no reemplaza a la persona: decide si las reglas se cumplen, y '
    'ella explica el resultado al lector. Por eso el rechazo termina en su carril.',
    'Lo que el diagrama no muestra: cómo se ve la pantalla, qué tablas hay o cómo se programa la comprobación. Eso se '
    'decide en la Unidad III.',
])

S52 = ('5.2 Diagrama de contexto y límites de intercambio de información', [
    'El diagrama de contexto muestra el sistema entero como una sola figura, rodeado de las entidades externas con las '
    'que intercambia información. No muestra los pasos internos: muestra qué entra, qué sale y con quién. Sirve para '
    'acordar el límite del sistema antes de detallarlo, y para descubrir información que nadie había nombrado.',
    'Una entidad externa es una persona, un rol u otro sistema que da información al sistema o la recibe, y queda fuera '
    'de su límite. Cada flecha es un flujo de información en un solo sentido, rotulado con un sustantivo: «informe '
    'mensual por curso», no «pedir el informe». Si una persona no da ni recibe información del sistema, no va en el '
    'diagrama, aunque sea importante para el proyecto.',
    'Una entidad externa del diagrama de contexto y un actor de los casos de uso (5.3) pueden ser la misma persona. La '
    'diferencia está en lo que muestra cada diagrama: el de contexto, qué información intercambia; el de casos de uso, '
    'para qué usa el sistema.',
])
LEYENDA_CONTEXTO = 'Tabla 5.4 — Símbolos del diagrama de contexto'

LEAD_FIG53 = ('En la Figura 5.3 el sistema es el círculo del centro. Las tres entidades externas son las que dan o '
              'reciben información de préstamos; cada flujo tiene su fuente en el dossier (Tabla 5.5).')
EPI_FIG53 = 'Figura 5.3 — Diagrama de contexto del sistema de préstamos de la biblioteca (caso ficticio).'
TABLA_55_ROTULO = 'Tabla 5.5 — Flujos de información del contexto y su fuente'
TABLA_55 = (['Desde', 'Hacia', 'Flujo de información', 'Fuente'],
            [[o, d, r, ', '.join(f)] for o, d, r, f in MO.CONTEXTO['flujos']])

EJ53 = ('Ejemplo resuelto 5.3: qué queda adentro y qué queda afuera', [
    'Consigna: decidir qué entidades externas van en el diagrama de contexto y justificar las que quedan afuera.',
    'Bibliotecaria, lector y dirección van en el diagrama: los tres dan o reciben información de préstamos (Tabla 5.5).',
    'El encargado de informática no va, aunque sea un interesado con influencia: instala la computadora (E4-L10), pero '
    'no da ni recibe datos de préstamos. Si más adelante administrara cuentas de usuario, habría que agregarlo.',
    'La inscripción de estudiantes tampoco: en el núcleo, la bibliotecaria carga los lectores. Un flujo automático con '
    'la secretaría sería una extensión.',
    'La compra de libros, las familias, el catálogo nacional y las notificaciones externas quedan fuera del núcleo del '
    'proyecto (Capítulo 3, Tabla 3.6). No se dibujan.',
])

ACT_E9 = [
    ('Ejercitá', [
        'Indicá qué símbolo del diagrama de actividades usarías para cada cosa y cómo la escribirías:\n'
        '(a) el lector entrega el libro en el mostrador;\n'
        '(b) el préstamo puede seguir o rechazarse según el lector esté activo;\n'
        '(c) el punto donde empieza el préstamo;\n'
        '(d) la columna de todo lo que hace el sistema.',
        'Estos rótulos de flujo de un diagrama de contexto tienen problemas. Corregilos:\n'
        '(a) «pedir el informe»; (b) «datos»; (c) «la bibliotecaria registra»; (d) «préstamos y lectores y vencidos».',
    ]),
    ('Resolvé', [
        'Dibujá el proceso propuesto de devolución con tres carriles (lector, bibliotecaria y sistema). Usá RF-03 y RF-08 '
        'y tené en cuenta el caso de un ejemplar que llega sin préstamo activo.',
        'Releé el registro E2 del Capítulo 2. Proponé si la docente del plan lector debería ser una entidad externa del '
        'diagrama de contexto y con qué flujos. Justificá con la fuente.',
    ]),
    ('Pensá y decidí', [
        'En la Figura 5.2, ¿qué pasaría si la comprobación del ejemplar estuviera en el carril de la bibliotecaria y no en '
        'el del sistema? Explicá qué problema del proceso actual volvería a aparecer.',
    ]),
    ('Desafío', [
        'Un compañero dibujó el diagrama de contexto con una figura de persona para el lector y una elipse para el sistema. '
        'Explicale qué está mezclando y cómo corregirlo, sin rehacer el diagrama entero.',
    ]),
]

# ------------------------------------------------------------------ encuentro 10
E10_TITULO = 'Encuentro 10 — Casos de uso y excepciones'

S53 = ('5.3 Actores, casos de uso y escenarios principales', [
    'Un actor es un rol que usa el sistema: «Bibliotecaria», «Lector». No es una persona concreta: si mañana la '
    'bibliotecaria tiene un reemplazo, el actor es el mismo. Un caso de uso es un objetivo que el actor logra con el '
    'sistema, escrito con verbo y objeto: «Registrar préstamo». No es un paso suelto («Escribir el código») ni una '
    'pantalla.',
    'El diagrama de casos de uso muestra, dentro del límite del sistema, los casos de uso, y afuera, los actores. Una '
    'línea sin flecha une a cada actor con los casos de uso en los que participa. El diagrama dice quién usa el sistema '
    'y para qué; el cómo va en la plantilla de cada caso de uso.',
    'La plantilla tiene cinco campos: el actor, la precondición (lo que tiene que ser cierto antes de empezar), el '
    'escenario principal en pasos numerados, los flujos alternativos y los requisitos que cubre. El escenario principal '
    'cuenta el camino en el que todo sale bien. Cada paso dice quién hace qué: el actor o el sistema.',
])
LEYENDA_CU = 'Tabla 5.6 — Símbolos del diagrama de casos de uso'

LEAD_FIG54 = ('La Figura 5.4 tiene cinco casos de uso. Los tres primeros son los prioritarios del proyecto y se '
              'desarrollan con su plantilla; los otros dos quedan nombrados y se completan en el Capítulo 6.')
EPI_FIG54 = 'Figura 5.4 — Diagrama de casos de uso del sistema de préstamos (caso ficticio).'

EJ54 = ('Ejemplo resuelto 5.4: actor o persona, caso de uso o paso', [
    'Consigna: revisar una primera versión del diagrama que incluía a «Mirta», a «Iván», un caso «Escribir el código del '
    'ejemplar» y una flecha de «Registrar préstamo» hacia el lector.',
    '«Mirta» y «Iván» son personas: se reemplazan por los roles «Bibliotecaria» y «Lector».',
    '«Escribir el código del ejemplar» es un paso del escenario de «Registrar préstamo», no un objetivo: se borra del '
    'diagrama y queda como paso 3 de la plantilla.',
    'La asociación no lleva flecha, y el lector no participa de «Registrar préstamo»: no usa el sistema para eso, lo '
    'hace la bibliotecaria (E4-L8). La línea se borra. El lector sí participa de «Consultar disponibilidad».',
])

S54 = ('5.4 Excepciones, decisiones y flujos alternativos', [
    'Un flujo alternativo describe qué pasa cuando algo sale distinto del escenario principal: el ejemplar ya está '
    'prestado, el lector está inactivo, el código no existe. Se numera desde el paso donde se desvía, con una letra: '
    '«5a» se desvía en el paso 5, y si hay dos desvíos en el mismo paso son «4a» y «4b». Cada flujo dice cuál es la '
    'condición, qué hace el sistema y cómo termina: vuelve a un paso o termina el caso de uso.',
    'Los flujos alternativos son donde más fallan los sistemas, porque nadie los pensó. Cada uno corresponde a una '
    'decisión del proceso propuesto (un rombo de la Figura 5.2) y casi siempre a un requisito de rechazo del catálogo. '
    'Si un flujo alternativo necesita un requisito que el catálogo no tiene, encontraste una omisión: se anota como '
    'requisito nuevo «a confirmar» y se consulta.',
])

EJ55 = ('Ejemplo resuelto 5.5: del rombo al flujo alternativo', [
    'Consigna: escribir los flujos alternativos de «Registrar préstamo» a partir de las decisiones de la Figura 5.2.',
    'El primer rombo decide si el lector está habilitado. Son dos condiciones distintas, con requisitos distintos: '
    'lector inactivo (RF-06) y lector con el máximo vigente (RF-05). Las dos se desvían en el paso 4: flujos 4a y 4b.',
    'El segundo rombo decide si el ejemplar está disponible. Si ya tiene un préstamo activo, se desvía en el paso 5: '
    'flujo 5a (RF-04). Es el flujo que protege la regla RN-01, la de la cadena de trazabilidad de la Figura 4.2.',
    'Los tres terminan igual: el sistema muestra el motivo y no crea ningún préstamo. Por eso, en la Figura 5.2, las '
    'salidas de rechazo se juntan en un rombo de fusión.',
])

ACT_E10 = [
    ('Ejercitá', [
        'Indicá si cada uno es un actor, un caso de uso, un paso o nada de eso, y corregí lo que haga falta:\n'
        '(a) «Prof. Estela Duarte»; (b) «Consultar disponibilidad»; (c) «Hacer clic en Guardar»; (d) «Dirección»; '
        '(e) «Base de datos»; (f) «Inactivar lector o ejemplar».',
    ]),
    ('Resolvé', [
        'Escribí la plantilla de CU-05 «Inactivar lector o ejemplar» (Figura 5.4): actor, precondición, escenario principal '
        'y requisitos que cubre (RF-10 y RN-06).',
        'Agregá a CU-05 un flujo alternativo para un lector que todavía tiene un préstamo activo. Decidí qué debería hacer '
        'el sistema y explicá por qué esa decisión no la puede tomar el equipo solo.',
    ]),
    ('Pensá y decidí', [
        'En CU-02, flujo 2a, la bibliotecaria aparta un ejemplar que llega sin préstamo activo. ¿Hace falta un requisito '
        'nuevo para registrar esa situación? Si te parece que sí, redactalo con el próximo identificador libre y marcalo '
        '«a confirmar».',
    ]),
    ('Desafío', [
        'Revisá la coherencia entre la Figura 5.2 y la plantilla de CU-01: ¿cada rombo tiene su flujo alternativo, y cada '
        'flujo alternativo, su rombo? Anotá cualquier diferencia que encuentres.',
    ]),
]

# ------------------------------------------------------------------ práctica
PRACTICA_TITULO = 'Práctica 5 — Modelar préstamo y devolución en otra biblioteca'
PRACTICA_INTRO = [
    'Volvés a la Escuela Básica Mbokaja, la de las Prácticas 1 a 3. Hay un dato nuevo que cambia la situación: la '
    'biblioteca va a tener una computadora. El encargado te contó cómo presta hoy, y aparecieron dos situaciones que no '
    'están en ningún ejemplo del capítulo. Los requisitos de la tabla ya se acordaron con la escuela.',
]
DATO_NUEVO_TITULO = 'Dato nuevo para decidir (Escuela Básica Mbokaja, caso de práctica, ficticio)'

NIVELES = [
    ('Nivel 1 — Guiado', [
        'Dibujá el proceso actual de préstamo y devolución de Mbokaja (MP-1 a MP-6) como diagrama de actividades con dos '
        'carriles, «Lector» y «Encargado». Entre cinco y siete acciones, una decisión con sus guardas y los nodos inicial '
        'y final.',
        'Marcá con (1) el paso donde nace el problema de V-11 (fichas sin devolución anotada) y con (2) el paso donde se '
        'pierde el préstamo de un docente (MN-01). Explicá cada marca en una línea, con su fuente.',
        'Completá la plantilla del proceso propuesto: «Con el sistema, el paso MP-3 lo hace ________ y se apoya en '
        '________ (MR-__)».',
    ]),
    ('Nivel 2 — Intermedio', [
        'Dibujá el proceso propuesto de devolución con tres carriles: lector, encargado y sistema. Cada acción del sistema '
        'cita su requisito MR.',
        'Escribí el caso de uso «Registrar devolución» con su plantilla completa y un flujo alternativo para MS-1. Si el '
        'flujo necesita un requisito que la tabla no tiene, redactalo como MR-09 «a confirmar».',
    ]),
    ('Nivel 3 — Ampliación', [
        'Escribí el caso de uso «Registrar préstamo» con un flujo alternativo para MS-2. El sistema no puede abrir la '
        'biblioteca a la mañana: explicá qué decisión hace falta, quién la toma y qué opciones le presentarías, sin decidir '
        'por él.',
        'Dibujá el diagrama de contexto del sistema de Mbokaja. Justificá cada entidad externa y cada flujo con una fuente '
        'V, M o MN.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: cada diagrama usa una sola notación; toda acción está en un carril; toda salida '
                    'de una decisión tiene guarda; los actores son roles; cada caso de uso cita requisitos MR que '
                    'existen, y cada flujo alternativo se numera desde su paso y dice cómo termina.')

REPASO = ('Para repasar', [
    'El proceso actual muestra dónde están los problemas; el proceso propuesto, qué cambia, quién lo hace y qué decide el sistema.',
    'En el diagrama de actividades, cada carril es un responsable, cada acción lleva verbo y objeto, y cada salida de una decisión lleva su guarda.',
    'El diagrama de contexto muestra el sistema como un todo, las entidades externas y los flujos de información, rotulados con sustantivos.',
    'Un actor es un rol; un caso de uso es un objetivo del actor. El escenario principal cuenta el camino en el que todo sale bien.',
    'Un flujo alternativo se numera desde su paso, dice qué hace el sistema y cómo termina. Si necesita un requisito que no existe, encontraste una omisión.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, los Encuentros 9 y 10 se unen en uno. Se conserva el proceso actual en versión '
    'simplificada: la Figura 5.1, de 5 a 7 pasos del préstamo y la devolución con los problemas del dossier marcados '
    '(aprox. 1 HC).',
    'En ese encuentro no se omiten: el proceso propuesto (Figura 5.2), los tres casos de uso prioritarios con un flujo '
    'alternativo cada uno y la Práctica 5 en el Nivel 1. Pasan a lectura domiciliaria: el diagrama de contexto (5.2, '
    'con el Ejemplo resuelto 5.3) y las actividades «Pensá y decidí» y «Desafío».',
])

# ------------------------------------------------------------------ evaluación
EVAL_ID = 'ADS3-L2-C5-c'   # semilla elegida para repartir las claves entre a, b y c
EVAL_TITULO = 'Evaluación del Capítulo 5'
EVAL_TEXTO_BASE = ('Texto base — Préstamo de proyectores del colegio (situación de evaluación, ficticia)', [
    'Q-1 El colegio tiene tres proyectores, guardados en la secretaría.',
    'Q-2 El docente pide uno a la secretaria, que anota en una hoja el nombre del docente y la hora.',
    'Q-3 Si los tres están prestados, la secretaria le avisa que no hay.',
    'Q-4 Al devolverlo, la secretaria revisa que funcione y que tenga el cable.',
    'Q-5 Si falta el cable, la secretaria lo anota en la hoja y avisa a la dirección.',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', '¿Qué símbolo del diagrama de actividades divide el camino según una condición?',
     ['Un rombo con una guarda entre corchetes en cada salida.',
      'Una elipse con el nombre de la condición.',
      'Una flecha rotulada con un sustantivo.',
      'Un rectángulo con el nombre del participante.']),
    ('mc', '¿Cuál de estos rótulos de flujo de un diagrama de contexto está bien escrito?',
     ['pedido de proyector',
      'pedir un proyector',
      'el docente pide',
      'revisar el cable']),
    ('mc', '¿Cuál de estos es un caso de uso bien nombrado?',
     ['Registrar préstamo de proyector',
      'Escribir el código en el formulario',
      'Secretaria',
      'Hoja de préstamos']),
    ('mc', 'En un diagrama de casos de uso, la línea sin flecha entre un actor y un caso significa que…',
     ['el actor participa en ese caso de uso.',
      'los datos van del actor al sistema.',
      'el caso de uso termina en el actor.',
      'el actor queda dentro del límite del sistema.']),
    ('vf', 'El diagrama de contexto muestra los pasos internos del proceso.',
     False, 'Falso. Muestra el sistema como un todo, las entidades externas y la información que entra y sale.'),
    ('vf', 'Un actor es un rol, como «Docente», y no una persona concreta.',
     True, 'Verdadero. Si cambia la persona, el actor sigue siendo el mismo.'),
    ('vf', 'Un flujo alternativo se numera desde el paso en que se desvía; por ejemplo, «3a».',
     True, 'Verdadero. El número dice dónde se desvía y la letra distingue los desvíos de un mismo paso.'),
    ('ab', 'Describí el proceso actual como diagrama de actividades: carriles, acciones en orden, la decisión con sus '
           'guardas y los nodos inicial y final.',
     'Carriles: Docente y Secretaria. Acciones: pedir un proyector (docente); comprobar si hay uno disponible '
     '(secretaria); decisión con guardas [hay disponible] y [no hay] (Q-3); anotar nombre y hora (Q-2) y entregar; '
     'usar y devolver (docente); revisar funcionamiento y cable (Q-4). Puede agregarse una segunda decisión [falta el '
     'cable] que lleva a anotar la falta y avisar a la dirección (Q-5). Nodo inicial único; uno o más nodos finales.', 4),
    ('ab', 'Escribí el caso de uso «Registrar devolución de proyector»: actor, escenario numerado y un flujo alternativo para Q-5.',
     'Actor: Secretaria. Escenario: 1. La secretaria indica el proyector devuelto. 2. El sistema muestra el préstamo '
     'activo de ese proyector. 3. La secretaria confirma que funciona y tiene el cable. 4. El sistema cierra el préstamo '
     'y el proyector queda disponible. Flujo alternativo 3a: falta el cable; la secretaria lo indica, el sistema cierra '
     'el préstamo con la observación y deja el aviso para la dirección (Q-5). Se acepta otra redacción coherente.', 4),
]
EVAL_PUNTAJE = ('Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno). '
                'Es opcional: puede reemplazarse por la evidencia de la Práctica 5.')
