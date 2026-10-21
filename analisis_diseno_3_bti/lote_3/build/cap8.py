# -*- coding: utf-8 -*-
"""Capítulo 8 — «Diseñar para las tareas de las personas» (Work §6: secciones 8.1 a 8.4 y práctica; encuentros 15 y 16).

Notaciones aprobadas por Fernando (20-oct-2026): mapa de navegación (pantallas con su código, flechas rotuladas con la
acción, punto de inicio y zonas por rol) y boceto de baja fidelidad. El capítulo distingue expresamente el mapa de los
diagramas del Capítulo 5. Los recorridos salen de las plantillas de CU-01 a CU-03 y cada flujo alternativo tiene su
mensaje (caso/diseno.py). La Práctica 8 usa Mbokaja: el voluntario de 9.º es menor de edad y sirve para decidir
permisos mínimos, supervisión y privacidad; no se supone que tenga acceso a datos personales ni a funciones
administrativas. Capacidades de Work §5.2: C6 (Encuentro 15) y C6 y C9 (Encuentro 16)."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'caso'))
import diseno as X
import mbokaja_u3 as MB
R, D, MO = X.R, X.D, X.MO

NUM = 8
UNIDAD = 'Unidad III — Diseñar una solución coherente'
CAPITULO = 'Capítulo 8'
TITULO = 'Diseñar para las tareas de las personas'
ENCUENTROS = (15, 16)
SECCIONES = ['8.1 Recorridos de usuario y organización de pantallas',
             '8.2 Bocetos y prototipo de baja fidelidad',
             '8.3 Estados vacío, carga, error y confirmación',
             '8.4 Etiquetas, navegación por teclado y lectura comprensible']
PRACTICA_WORK = 'observar el uso del boceto y modificarlo con evidencia'

ROTULO_CAPACIDAD = ('Capacidades propuestas para el programa institucional (C6 y C9; no son capacidades oficiales del '
                    'MEC)')
CAPACIDAD = ('C6. Diseña la interacción y la arquitectura del prototipo.\n'
             'C9. Verifica y mejora la solución a partir de evidencia.')
TEMA = ('Recorridos de usuario a partir de los casos de uso. Organización de pantallas y mapa de navegación con zonas por '
        'rol. Bocetos y prototipo de baja fidelidad. Estados vacío, carga, error y confirmación, y mensajes útiles. '
        'Etiquetas, navegación por teclado y lectura comprensible. Revisión con usuarios simulados.')
INDICADORES = [
    'Traza tres recorridos completos a partir de los casos de uso prioritarios y organiza las pantallas en un mapa de navegación con zonas por rol.',
    'Dibuja bocetos de baja fidelidad que muestran qué va en cada pantalla y qué requisito lo pide.',
    'Muestra los estados vacío, carga, error y confirmación, con mensajes que dicen qué pasó, por qué y qué hacer.',
    'Aplica una lista de accesibilidad: etiquetas visibles, uso con teclado, foco visible y mensajes que no dependen del color.',
    'Observa el uso del boceto con usuarios simulados, registra los problemas con evidencia y corrige el diseño.',
]
TIEMPO = ('Dos encuentros de 5 HC (15 y 16 de la secuencia anual), de diseño; el Encuentro 16 incluye 2 HC de revisión '
          'con usuarios simulados.')

APERTURA = [
    'El sistema puede tener el modelo de datos perfecto y fracasar igual, si la bibliotecaria no encuentra dónde registrar '
    'una devolución en medio del recreo. En este capítulo diseñás la interacción: qué pantallas hay, cómo se pasa de una a '
    'otra, qué se ve en cada una y qué pasa cuando algo sale mal.',
    'Todavía no se programa nada. Se trabaja con bocetos en papel o en cajas grises, que se cambian en minutos. Y se prueban '
    'con personas, porque lo que al equipo le parece claro no siempre lo es para quien va a usarlo.',
]
ARTICULACION = [
    'Con el Capítulo 5: cada recorrido sale de la plantilla de un caso de uso, y cada flujo alternativo se convierte en un '
    'estado de error con su mensaje.',
    'Con el Capítulo 7: las pantallas muestran los datos del modelo; la consulta pública muestra obras y disponibles, nunca '
    'datos de lectores (RNF-03).',
    'Con el Capítulo 9: cada botón dispara una operación cuyo contrato dice qué errores puede devolver.',
]

# ------------------------------------------------------------------ encuentro 15
E15_TITULO = 'Encuentro 15 — Recorridos, pantallas y bocetos'

S81 = ('8.1 Recorridos de usuario y organización de pantallas', [
    'Un recorrido de usuario es la secuencia de pantallas y acciones con la que una persona completa una tarea. Se obtiene '
    'de la plantilla del caso de uso: cada paso del escenario principal dice quién hace qué, y eso se convierte en una '
    'pantalla, un dato que se escribe o un botón que se pulsa. Los tres recorridos de este capítulo son los de los casos de '
    'uso prioritarios: registrar un préstamo, registrar una devolución y consultar la disponibilidad.',
    'Las pantallas se organizan en un mapa de navegación. El mapa muestra todas las pantallas y cómo se pasa de una a otra; '
    'no muestra el contenido de cada una. Las pantallas que puede ver un rol, o un grupo de roles, se agrupan en una zona '
    'con su nombre: así se ve de un vistazo que la consulta pública no lleva a los datos de los lectores (RNF-03) y que solo la '
    'bibliotecaria registra préstamos (RNF-02).',
    'El mapa de navegación no es ninguno de los diagramas del Capítulo 5. No tiene carriles ni decisiones, como el diagrama '
    'de actividades; sus flechas no son flujos de información rotulados con sustantivos, como en el diagrama de contexto; y '
    'sus rectángulos son pantallas, no actores ni casos de uso. Sus flechas se rotulan con la acción que hace la persona: '
    '«Prestar», «Ver informe».',
])
LEYENDA_NAV = 'Tabla 8.1 — Símbolos del mapa de navegación'
TABLA_DIFERENCIAS_ROTULO = 'Tabla 8.2 — El mapa de navegación frente a los diagramas del Capítulo 5'
TABLA_DIFERENCIAS = (['Diagrama', 'Qué muestra', 'Rectángulos', 'Flechas'],
                     [['Mapa de navegación (8.1)', 'Pantallas y cómo se pasa de una a otra', 'Pantallas, con su código', 'Acción del usuario, con verbo'],
                      ['Actividades (5.1)', 'Pasos de un proceso y quién los hace', 'Acciones, en carriles', 'Orden de las acciones; guardas en las decisiones'],
                      ['Contexto (5.2)', 'Información que entra y sale del sistema', 'Entidades externas', 'Flujo de información, con sustantivo'],
                      ['Casos de uso (5.3)', 'Quién usa el sistema y para qué', 'Límite del sistema', 'No tiene: líneas sin flecha']])
LEAD_FIG81 = ('La Figura 8.1 es el mapa de navegación del sistema de la biblioteca. Las zonas punteadas separan lo que '
              've cualquier persona de lo que ven la bibliotecaria y la dirección después de ingresar.')
EPI_FIG81 = 'Figura 8.1 — Mapa de navegación del sistema de préstamos (caso ficticio).'
NOTA_MAPA = X.NOTA_MAPA
TABLA_PANTALLAS_ROTULO = 'Tabla 8.3 — Pantallas, zonas y requisitos'
TABLA_PANTALLAS = (['Pantalla', 'Nombre', 'Zona', 'Qué muestra', 'Requisitos'],
                   [[c, n, z, q, ', '.join(r)] for c, n, z, q, r in X.PANTALLAS])
TABLA_RECORRIDOS_ROTULO = 'Tabla 8.4 — Tres recorridos, paso a paso, desde los casos de uso'
TABLA_RECORRIDOS = (['Caso de uso', 'Paso', 'Pantalla', 'La persona…', 'El sistema…'],
                    [[cu, str(p), pt, a, b] for cu, pasos in X.RECORRIDOS for p, pt, a, b in pasos])

EJ81 = ('Ejemplo resuelto 8.1: del caso de uso CU-01 al recorrido', [
    'Consigna: convertir el escenario principal de «Registrar préstamo» en un recorrido de pantallas.',
    'Paso 1 de la plantilla, «la bibliotecaria indica el lector»: un campo «Código del lector» en PT-05. El paso 2, «el '
    'sistema muestra el lector y sus préstamos activos», va al lado del campo: así la bibliotecaria ve antes de prestar si '
    'el lector ya está en el máximo.',
    'Paso 3, «indica el ejemplar»: un segundo campo en la misma pantalla. No hace falta otra pantalla: menos cambios de '
    'pantalla, menos tiempo en el recreo (E1-L2).',
    'Pasos 4 a 6: el botón «Prestar». Las comprobaciones las hace el sistema; la pantalla solo muestra el resultado.',
    'Paso 7: el mensaje de confirmación con el vencimiento (ME-04). Los flujos 4a, 4b y 5a son los mensajes ME-01, ME-02 y '
    'ME-03 (8.3).',
])

S82 = ('8.2 Bocetos y prototipo de baja fidelidad', [
    'Un boceto de baja fidelidad es un dibujo simple de una pantalla: cajas grises, etiquetas, campos y botones, sin colores '
    'ni logotipos. Sirve para discutir qué va en cada pantalla antes de gastar tiempo en el aspecto. Si un boceto se tira, '
    'se perdieron diez minutos; si se tira una pantalla programada, se pierde un día.',
    'Cada elemento del boceto tiene que poder justificarse con un requisito o un paso de un recorrido. Lo que no se puede '
    'justificar sobra. El prototipo de baja fidelidad es el conjunto de bocetos de un recorrido, en papel, que una persona '
    'puede «usar» señalando con el dedo mientras alguien del equipo cambia la hoja.',
])
LEYENDA_BOC = 'Tabla 8.5 — Símbolos del boceto de baja fidelidad'
LEAD_FIG82 = ('La Figura 8.2 tiene los bocetos de las tres tareas. Fijate que la consulta pública no muestra ningún dato '
              'de lectores y que el préstamo y la devolución tienen siempre una zona para el mensaje.')
EPI_FIG82 = 'Figura 8.2 — Bocetos de baja fidelidad de las tres tareas (caso ficticio).'
EJ82 = ('Ejemplo resuelto 8.2: justificar cada elemento del boceto de la devolución', [
    'Consigna: revisar el boceto de PT-06 y decir qué requisito o paso pide cada elemento.',
    'Campo «Código del ejemplar»: RF-03 y el paso 1 de CU-02. Sin él no se sabe qué préstamo cerrar (E4-L2).',
    'Datos del préstamo con el lector: RF-08 y el paso 2. La bibliotecaria confirma que es el préstamo correcto antes de '
    'cerrarlo.',
    'Botón «Confirmar devolución»: el paso 3. Dice «devolución», la palabra que usa la bibliotecaria, y no «cerrar '
    'transacción».',
    'Zona de mensaje: los flujos 1a y 2a (ME-05 y ME-06) y la confirmación (ME-07).',
    'Un campo «Observaciones» que propuso un compañero no tiene requisito que lo pida: no entra en el núcleo. Si la '
    'bibliotecaria lo pide, se tramita como solicitud de cambio.',
])

ACT_E15 = [
    ('Ejercitá', [
        'Indicá si cada elemento corresponde al mapa de navegación, a un diagrama del Capítulo 5 o a un boceto:\n'
        '(a) una flecha rotulada «Ver préstamos»; (b) una flecha rotulada «informe mensual por curso»; (c) un campo con la '
        'etiqueta «Código del ejemplar»; (d) un marco punteado rotulado «Bibliotecaria»; (e) un carril «Sistema».',
    ]),
    ('Resolvé', [
        'Escribí el recorrido de CU-05 «Inactivar lector o ejemplar» con el formato de la Tabla 8.4: paso, pantalla, lo que '
        'hace la persona y lo que responde el sistema.',
        'Dibujá el boceto de PT-07 «Préstamos activos y vencidos» y justificá cada elemento con un requisito.',
    ]),
    ('Pensá y decidí', [
        'Un compañero propone que la consulta pública muestre «Prestado a: nombre del lector» para que los estudiantes sepan a '
        'quién pedirle el libro. Decidí y justificá con el catálogo.',
    ]),
    ('Desafío', [
        'Agregá al mapa de navegación la pantalla que haría falta para la variante «la dirección también quiere ver los '
        'préstamos vencidos». ¿En qué zona va? ¿Qué transiciones nuevas aparecen?',
    ]),
]

# ------------------------------------------------------------------ encuentro 16
E16_TITULO = 'Encuentro 16 — Estados, mensajes, accesibilidad y revisión con usuarios'

S83 = ('8.3 Estados vacío, carga, error y confirmación', [
    'Una pantalla no tiene un solo aspecto. Antes de que la persona escriba algo está vacía; mientras el sistema busca o '
    'guarda está cargando; si algo sale mal muestra un error; y cuando la operación termina bien, confirma. Diseñar solo '
    'la pantalla «cuando todo sale bien» deja a la persona sin saber qué pasa en los otros casos.',
    'Cada flujo alternativo del Capítulo 5 se convierte en un estado de error, con su mensaje. La regla para escribirlos es '
    'una sola: ' + X.REGLA_MENSAJE[0].lower() + X.REGLA_MENSAJE[1:] + ' Un mensaje como «Error 23» no cumple ninguna de las '
    'tres partes.',
    'El estado de carga también evita errores. Si el botón «Prestar» queda desactivado mientras se guarda, nadie lo pulsa '
    'dos veces. La computadora de la biblioteca es vieja (E4-L10): conviene que la persona vea que el sistema está '
    'trabajando.',
])
LEAD_FIG83 = ('La Figura 8.3 muestra la misma pantalla en sus cuatro estados. El mensaje de error es el del flujo 5a '
              'de CU-01 (ME-03).')
EPI_FIG83 = 'Figura 8.3 — Los cuatro estados de PT-05 «Registrar préstamo» (boceto).'
TABLA_MENSAJES_ROTULO = 'Tabla 8.6 — Mensajes y estados, desde los flujos alternativos'
TABLA_MENSAJES = (['Código', 'Pantalla', 'Estado', 'Cuándo', 'Mensaje'],
                  [[c, p, e, q, t] for c, p, e, q, t, _ in X.MENSAJES])
EJ83 = ('Ejemplo resuelto 8.3: de un flujo alternativo a un mensaje', [
    'Consigna: escribir el mensaje del flujo 4b de CU-01 (el lector ya tiene el máximo).',
    'Primera versión: «Operación no permitida.» No dice qué pasó ni qué hacer.',
    'Segunda versión: «El lector superó el límite.» Dice qué pasó, pero no cuál es el límite ni qué hacer.',
    'Versión final (ME-02): «No se puede prestar: el lector ya tiene 2 préstamos activos, el máximo para estudiantes. Tiene '
    'que devolver uno antes.» Dice qué pasó, por qué y qué hacer. Como el máximo depende del tipo (RN-02 v1.1), el mensaje '
    'muestra el máximo que corresponde a ese lector, leído de Parámetro.',
])

S84 = ('8.4 Etiquetas, navegación por teclado y lectura comprensible', [
    'Una pantalla accesible es la que puede usar la mayor cantidad posible de personas, incluidas las que tienen dificultades '
    'para ver, para usar el ratón o para leer textos largos. En la biblioteca, además, se trabaja apurado y con fila: lo que '
    'ayuda a una persona con dificultades ayuda a todos.',
    'La lista de la Tabla 8.7 reúne lo mínimo que se revisa en cada boceto. No reemplaza una revisión de accesibilidad '
    'completa, pero evita los problemas más frecuentes: campos sin etiqueta, tareas que solo se hacen con el ratón, '
    'mensajes que solo se distinguen por el color y palabras técnicas que la bibliotecaria no usa.',
    'Para revisar un boceto con usuarios simulados, un integrante hace de usuario con una tarjeta de rol, otro conduce la '
    'sesión sin ayudar y un tercero anota lo que observa. Se anota lo que la persona hace, no lo que el equipo cree que '
    'pensó. Cada problema observado lleva su evidencia (qué hizo la persona) y una corrección. RNF-01 da la meta: completar '
    'la tarea sin ayuda.',
])
TABLA_ACC_ROTULO = 'Tabla 8.7 — Lista de accesibilidad para revisar cada boceto'
TABLA_ACC = (['Código', 'Qué se revisa'], [list(a) for a in X.ACCESIBILIDAD])
TABLA_OBS_ROTULO = 'Tabla 8.8 — Registro de la sesión con usuarios simulados (equipo modelo, ficticio)'
TABLA_OBS = (['Tarea', 'Lo que hizo la persona (evidencia)', 'Problema', 'Corrección del boceto'],
             [['Registrar préstamo', 'Escribió el código del ejemplar en el campo del lector.', 'Los dos campos tenían la misma etiqueta corta, «Código».', 'Etiquetas completas: «Código del lector» y «Código del ejemplar» (A-01).'],
              ['Registrar devolución', 'Buscó el botón durante un rato y preguntó: «¿Dónde devuelvo?».', 'El botón decía «Procesar».', '«Confirmar devolución» (A-06).'],
              ['Consultar disponibilidad', 'Usó solo el teclado y no supo en qué campo estaba.', 'El foco no se veía.', 'Foco visible (A-03).'],
              ['Registrar préstamo', 'Leyó el mensaje en rojo, pero no supo qué hacer.', 'El mensaje no decía qué hacer.', 'Mensaje completo (ME-03).']])
EJ84 = ('Ejemplo resuelto 8.4: de la observación a la corrección', [
    'Consigna: usar la Tabla 8.8 para decidir qué cambiar en los bocetos y qué no.',
    'Las cuatro observaciones tienen evidencia: lo que la persona hizo. Por eso se corrigen todas, y cada corrección cita '
    'la regla de la lista de accesibilidad o el mensaje que la resuelve.',
    'Un integrante opinó que «los botones deberían ser verdes». No es una observación de uso: no hay evidencia de que el '
    'color haya causado un problema. Queda para la etapa de diseño visual.',
    'Después de corregir, el equipo vuelve a probar el recorrido con otra persona. La versión corregida de los bocetos '
    'lleva un número nuevo en la bitácora.',
])

ACT_E16 = [
    ('Ejercitá', [
        'Indicá el estado (vacío, carga, error o confirmación) y corregí cada mensaje con la regla de 8.3:\n'
        '(a) «Error.»; (b) «Guardado.»; (c) «No hay datos.»; (d) «Procesando…».',
    ]),
    ('Resolvé', [
        'Escribí los mensajes de PT-08 para dos casos: se intenta inactivar un lector con un préstamo activo, y se inactiva un '
        'ejemplar sin problemas.',
        'Aplicá la lista de la Tabla 8.7 al boceto de PT-05 de la Figura 8.2 y anotá un problema y su corrección, o explicá '
        'por qué cumple cada punto.',
    ]),
    ('Pensá y decidí', [
        'Durante la sesión, la persona que hace de bibliotecaria dice: «yo pondría todo en una sola pantalla». ¿Lo anotás como '
        'observación o como opinión? ¿Qué harías para decidir con evidencia?',
    ]),
    ('Desafío', [
        'Diseñá el estado de PT-02 para cuando la computadora de la biblioteca tarda mucho en responder. ¿Qué ve el lector y '
        'qué no debería poder hacer mientras tanto?',
    ]),
]

# ------------------------------------------------------------------ práctica
PRACTICA_TITULO = 'Práctica 8 — Observar el uso del boceto en otra biblioteca y modificarlo con evidencia'
PRACTICA_INTRO = [
    'En la Escuela Básica Mbokaja se hizo una sesión de uso con un boceto de la pantalla de préstamo. Participaron el '
    'encargado, un voluntario de 9.º y una estudiante del turno mañana. El voluntario es menor de edad y ayuda con el '
    'encargado presente (MS-5): no se puede suponer que tenga acceso a datos personales ni a funciones administrativas. '
    'Si tu curso hizo su propia sesión, usá su registro; si no, usá el de abajo.',
]
NIVELES = [
    ('Nivel 1 — Guiado', [
        'Clasificá cada observación (OBS-1 a OBS-6) según el problema: etiqueta, estado, mensaje, teclado o privacidad. '
        'Indicá qué punto de la Tabla 8.7 no se cumple, si corresponde.',
        'Redibujá el boceto de la pantalla de préstamo de Mbokaja con dos correcciones que salgan de las observaciones. '
        'Anotá al lado de cada una la observación que la justifica.',
    ]),
    ('Nivel 2 — Intermedio', [
        'Escribí los mensajes de error y de confirmación de la pantalla de préstamo de Mbokaja con la regla de 8.3. Uno tiene '
        'que resolver OBS-6.',
        'Diseñá el estado de carga que evita OBS-4 y explicá por qué también hace falta una restricción del modelo (Práctica 7).',
    ]),
    ('Nivel 3 — Ampliación', [
        'OBS-1 muestra un problema de privacidad. Decidí qué puede ver y qué puede hacer el voluntario en el sistema: '
        'permisos mínimos, supervisión del encargado y datos que nunca ve. Justificá con MN-05 y MS-5.',
        'Dibujá el mapa de navegación de Mbokaja con una zona para el encargado y, si lo justificaste, otra más limitada para '
        'los voluntarios.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: cada corrección cita la observación que la justifica; los mensajes dicen qué pasó, '
                    'por qué y qué hacer; el voluntario no ve datos personales ni tiene funciones administrativas; el mapa '
                    'usa solo pantallas, transiciones con verbo, inicio y zonas.')

REPASO = ('Para repasar', [
    'Un recorrido sale de la plantilla del caso de uso: cada paso es una pantalla, un dato o una acción.',
    'El mapa de navegación muestra pantallas y transiciones rotuladas con la acción; las zonas muestran qué ve cada rol.',
    'Un boceto de baja fidelidad se justifica elemento por elemento con requisitos o pasos de un recorrido.',
    'Cada pantalla tiene sus estados: vacío, carga, error y confirmación. Un mensaje dice qué pasó, por qué y qué hacer.',
    'La revisión con usuarios registra lo que la persona hace, con evidencia, y el boceto se corrige y se vuelve a probar.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, los Encuentros 15 y 16 se unen en uno: tres recorridos en baja fidelidad (Figura '
    '8.2) y una sola sesión de revisión entre equipos.',
    'En ese encuentro no se omiten: la Tabla 8.4, los mensajes de la Tabla 8.6 y la lista de la Tabla 8.7. Pasan a lectura '
    'domiciliaria: el Ejemplo resuelto 8.2 y la Práctica 8 en el Nivel 3.',
])

# ------------------------------------------------------------------ evaluación
EVAL_ID = 'ADS3-L3-C8'
EVAL_TITULO = 'Evaluación del Capítulo 8'
EVAL_TEXTO_BASE = ('Texto base — Pedido de constancias en la secretaría (situación de evaluación, ficticia)', [
    'Z-1 Los estudiantes piden constancias de alumno regular en la secretaría.',
    'Z-2 Hoy llenan un papel con su nombre, su curso y para qué la necesitan.',
    'Z-3 La secretaria entrega la constancia al día siguiente.',
    'Z-4 Muchos vuelven antes de tiempo porque no saben si la constancia ya está lista.',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', 'En un mapa de navegación, ¿qué representa una flecha rotulada?',
     ['La acción con la que la persona pasa de una pantalla a otra.',
      'Un dato que entra al sistema.',
      'El orden de los pasos de un proceso.',
      'Que un actor participa en un caso de uso.']),
    ('mc', '¿Cuál de estos mensajes de error está mejor escrito?',
     ['No se puede enviar: falta el curso. Elegilo en la lista.',
      'Error 23.',
      'Datos inválidos.',
      'Algo salió mal.']),
    ('mc', '¿Qué estado muestra una pantalla mientras el sistema guarda los datos?',
     ['Carga.', 'Vacío.', 'Error.', 'Confirmación.']),
    ('mc', '¿Cuál de estas prácticas ayuda a usar la pantalla con el teclado?',
     ['Que Tab siga el orden de la tarea y el foco se vea.',
      'Que los botones sean grandes y verdes.',
      'Que los errores aparezcan en rojo.',
      'Que haya muchas pantallas pequeñas.']),
    ('vf', 'El mapa de navegación lleva flechas rotuladas con sustantivos, igual que el diagrama de contexto.',
     False, 'Falso. Sus flechas llevan la acción, con verbo; las del contexto llevan la información, con sustantivo.'),
    ('vf', 'En una sesión con usuarios simulados se anota lo que la persona hace, no lo que el equipo cree que pensó.',
     True, 'Verdadero. Cada problema necesita su evidencia.'),
    ('vf', 'Un boceto de baja fidelidad tiene que tener los colores definitivos.',
     False, 'Falso. Se usan cajas grises; el aspecto se decide después.'),
    ('ab', 'Con el texto base, escribí el recorrido para pedir una constancia y saber si está lista, y dibujá su mapa de '
           'navegación con al menos tres pantallas.',
     'Recorrido: el estudiante completa el pedido (nombre, curso, motivo) y lo envía; recibe una confirmación; más tarde '
     'consulta el estado y ve «en preparación» o «lista». Mapa: inicio → «Pedir constancia» → «Pedido enviado» → «Estado del '
     'pedido», con flechas rotuladas con verbos; la pantalla de la secretaria en una zona propia. Un punto por el recorrido '
     'completo, uno por las tres pantallas, uno por las flechas con acción y uno por la zona de la secretaria.', 4),
    ('ab', 'Escribí los estados y los mensajes de la pantalla «Estado del pedido» para Z-4: vacío, carga, error y '
           'confirmación.',
     'Vacío: «Escribí tu número de pedido para ver cómo va.» Carga: «Buscando tu pedido…». Error: «No encontramos ese número '
     'de pedido. Revisá el número que te dieron al enviarlo.» Confirmación: «Tu constancia está lista: retirala en la '
     'secretaría a partir de las 8:00.» Un punto por estado con un mensaje que dice qué pasó y qué hacer.', 4),
]
EVAL_PUNTAJE = ('Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno). '
                'Es opcional: puede reemplazarse por la evidencia de la Práctica 8.')
