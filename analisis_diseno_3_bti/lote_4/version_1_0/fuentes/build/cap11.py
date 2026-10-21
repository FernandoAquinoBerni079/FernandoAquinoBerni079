# -*- coding: utf-8 -*-
"""Capítulo 11 — «Catálogo, ejemplares y lectores» (Work §6: secciones 11.1 a 11.4 y práctica «registrar un lote
distinto del ejemplo y resolver entradas inválidas»; encuentros 21 y 22).

Implementa el Incremento 2 de la Tabla 6.3 con el diseño del lote 3 v1.1 sin cambios: zonas de la Figura 8.1, ME-12
solo en el ingreso y ME-13 para la falta de permiso, OP-06 con baja lógica (RI-05). Las altas y correcciones del
catálogo y de los lectores son operaciones auxiliares de PT-08 (OA-02 a OA-05), con contrato y prueba propios: no se
atribuyen a ningún contrato del Capítulo 9. Work §5.2: «Alta, consulta y edición con reglas de validación» (21) y
«Validación en servidor; rechazo de acceso indebido» (22). Capacidades: C5 y C8 (21); C6 y C8 (22).
El libro no publica resueltas las operaciones de los lectores (OA-03, OA-04): la validación de referencia
(validar_lector) está solo en la guía docente."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'caso'))
import construccion as C
import mbokaja_u4 as MB
X = C.X

NUM = 11
UNIDAD = 'Unidad IV — Construir el prototipo por incrementos'
CAPITULO = 'Capítulo 11'
TITULO = 'Catálogo, ejemplares y lectores'
ENCUENTROS = (21, 22)
SECCIONES = ['11.1 Implementación de tareas priorizadas a partir de los bocetos',
             '11.2 Datos obligatorios, códigos, duplicados y mensajes útiles',
             '11.3 Permisos mínimos y comprobaciones del servidor',
             '11.4 Edición y baja lógica sin pérdida de historial']
PRACTICA_WORK = 'registrar un lote distinto del ejemplo y resolver entradas inválidas'

ROTULO_CAPACIDAD = ('Capacidades propuestas para el programa institucional (C5 y C8 en el Encuentro 21; C6 y C8 en el '
                    'Encuentro 22; no son capacidades oficiales del MEC)')
CAPACIDAD = ('C5. Justifica el modelo de información y sus reglas de integridad.\n'
             'C6. Diseña la interacción y la arquitectura del prototipo.\n'
             'C8. Integra un prototipo funcional con persistencia.')
TEMA = ('Tareas del incremento de catálogo y lectores, ordenadas desde los bocetos. Del diccionario de datos a las '
        'validaciones: datos obligatorios, formato de los códigos, duplicados y mensajes. Permisos por zona comprobados '
        'en el servidor (ME-13) y error de ingreso (ME-12). Corrección de datos y baja lógica sin pérdida de historial.')
INDICADORES = [
    'Ordena las tareas del incremento a partir de los bocetos de PT-08 y de sus dependencias.',
    'Lleva cada regla del diccionario a una validación del servidor y a una restricción de la base, con su mensaje.',
    'Construye el alta y la corrección de obras, ediciones y lectores, y rechaza los códigos repetidos sin cambiar datos.',
    'Comprueba en el servidor el permiso de cada pantalla y operación, y demuestra el rechazo de un acceso indebido.',
    'Corrige datos y da de baja lectores y ejemplares sin borrar nada ni alterar el historial.',
]
TIEMPO = ('Dos encuentros de 5 HC (21 y 22 de la secuencia anual), cada uno con 1 HC de diseño, 3 de práctica y 1 de '
          'verificación.')

APERTURA = [
    'Con el alta de un ejemplar funcionando, el equipo tiene la versión 0.2. Ahora completa el catálogo y los lectores: es '
    'el Incremento 2 de la Tabla 6.3. Al terminar, la bibliotecaria puede cargar obras, ediciones, ejemplares y lectores, '
    'corregirlos y darlos de baja.',
    'Son operaciones simples, pero acá se decide si los datos del sistema son confiables. Un código repetido, un estudiante '
    'sin curso o un lector borrado con su historial rompen después los préstamos y el informe. Las reglas del Capítulo 7 '
    'se hacen cumplir en el servidor y en la base, no solo en la pantalla.',
]
ARTICULACION = [
    'Con el Capítulo 7: el diccionario de datos (Tabla 7.5) y las restricciones RI-03, RI-05 y RI-06 se convierten en '
    'validaciones y restricciones.',
    'Con el Capítulo 8: el boceto de PT-08, la regla de los mensajes y las zonas por rol de la Figura 8.1.',
    'Con Laboratorio de 3.º: las altas y modificaciones con SQL ya se practicaron allí. Acá importa que cada una cumpla su '
    'contrato y su prueba.',
]

AVISO_ENTORNO = C.AVISO_ENTORNO

# ------------------------------------------------------------------ encuentro 21
E21_TITULO = 'Encuentro 21 — Catálogo: obras, ediciones y ejemplares'

S111 = ('11.1 Implementación de tareas priorizadas a partir de los bocetos', [
    'El orden de construcción sale de lo que ya se decidió. La Tabla 6.3 pone el catálogo y los lectores en el '
    'Incremento 2, después de la base y antes del préstamo: sin ejemplares ni lectores no hay nada que prestar. Dentro '
    'del incremento, cada tarea es una parte del boceto de PT-08 con su operación, su requisito y su prueba (Tabla 11.1).',
    'Se empieza por lo que otras tareas necesitan. Una edición necesita su obra, y un ejemplar necesita su edición: por eso '
    'el alta de obra y edición (OA-02) va antes que cualquier carga de ejemplares. La corrección de una obra (OA-05) no '
    'depende de nada más y la puede hacer otro integrante a la vez.',
])
TABLA_111_ROTULO = 'Tabla 11.1 — Tareas de la Unidad IV, con su operación, requisito y prueba'
TABLA_111 = (['Enc.', 'Tarea', 'Operación', 'Pantalla', 'Requisitos', 'Pruebas'],
             [[str(t[0]), t[1], t[2], t[3], ', '.join(t[4]), ', '.join(t[5])] for t in C.TAREAS])
CONTRATOS_E21 = ['OA-02', 'OA-05']

S112 = ('11.2 Datos obligatorios, códigos, duplicados y mensajes útiles', [
    'El diccionario de datos del Capítulo 7 dice, para cada dato, si es obligatorio y cómo es. Cada una de esas reglas se '
    'comprueba dos veces: la operación la valida en el servidor y responde un mensaje útil, y la base la protege con una '
    'restricción, por si alguna vez un dato llega sin pasar por la operación (Tabla 11.2).',
    'Un código repetido no se corrige: se rechaza. Cada libro físico tiene su código, y un código que ya se usó no se '
    'vuelve a usar aunque el ejemplar esté dado de baja, porque el historial lo nombra. La base tiene el código como '
    'único; la operación traduce ese rechazo en el mensaje MA-02 o MA-05.',
    'Los mensajes siguen la regla del Capítulo 8: «%s» MV-02, por ejemplo, dice qué código no tiene el formato esperado, '
    'cuál es el formato y dónde revisarlo.' % X.REGLA_MENSAJE,
])
TABLA_112_ROTULO = 'Tabla 11.2 — Del diccionario a la validación y a la restricción de la base'
TABLA_112 = (['Dato (Tabla 7.5)', 'Regla', 'Operación (servidor)', 'Base de datos'],
             [['Código de obra, edición, ejemplar y lector', 'OB-, ED-, EJ- o LE- y cuatro cifras', 'MV-02', 'CHECK con el formato'],
              ['Código de cualquier dato', 'Único; no se reutiliza', 'MA-02 (ejemplar), MA-05 (los demás)', 'UNIQUE'],
              ['Título y autor de la obra; nombre del lector', 'Obligatorios', 'MV-01', 'CHECK: no vacío'],
              ['Edición del ejemplar', 'Tiene que existir', 'MA-03', 'Clave foránea'],
              ['Tipo de lector (RF-11)', 'Estudiante o docente', 'MV-01', 'CHECK con los dos valores'],
              ['Curso (RI-06)', 'Obligatorio para estudiantes; vacío para docentes', 'MV-03 y MV-04', 'CHECK que combina tipo y curso']])
EJ111 = ('Ejemplo resuelto 11.1: una obra con dos ediciones', [
    'Consigna: la biblioteca recibe «Cuentos del arroyo Arapoty» de otra editorial, de 2023. ¿Se registra una obra nueva?',
    'No. La obra ya existe (OB-0031); lo nuevo es la edición. Con OA-02 se registra la edición ED-0052 en la obra '
    'OB-0031, sin escribir de nuevo el título ni el autor. Después, cada libro físico se da de alta con OA-01 en ED-0052.',
    'Si se registrara como obra nueva, la consulta pública mostraría dos títulos iguales, y el informe no podría decir '
    'cuánto se lee esa obra. Es la distinción entre obra, edición y ejemplar del Capítulo 7, ahora en una operación.',
])
EJ112 = ('Ejemplo resuelto 11.2: un mensaje que no ayuda y uno que sí', [
    'Consigna: comparar dos respuestas posibles al intentar registrar la edición ED-0045, que ya existe.',
    'Respuesta A: «Error: UNIQUE constraint failed: ediciones.codigo». Dice qué pasó en la base, pero no en palabras de '
    'la bibliotecaria, ni qué puede hacer.',
    'Respuesta B, la del sistema: «%s» Dice qué pasó, por qué (los códigos no se reutilizan) y qué hacer.'
    % C.con_datos('MA-05', 'ED-0045'),
])
ACT_E21 = [
    ('Ejercitá', [
        'Para cada entrada, escribí qué mensaje debería responder el alta de una obra con su edición:\n'
        '(a) código de obra OB-31; (b) título vacío; (c) la edición ED-0060, que ya existe; (d) todo correcto.',
    ]),
    ('Resolvé', [
        'Construí OA-02 y OA-05 en la base de tu equipo, según sus contratos. Agregá a PT-08 los formularios que faltan y '
        'ejecutá las pruebas PA-02 y PA-05.',
        'Completá en tu bitácora la fila de la Tabla 11.1 de cada tarea terminada, con el resultado de su prueba.',
    ]),
    ('Pensá y decidí', [
        'Un compañero propone que, si el código ya existe, el sistema le sume uno y lo guarde igual. Explicá qué problema '
        'traería con las etiquetas pegadas en los libros.',
    ]),
]

# ------------------------------------------------------------------ encuentro 22
E22_TITULO = 'Encuentro 22 — Lectores, permisos y baja lógica'

S113 = ('11.3 Permisos mínimos y comprobaciones del servidor', [
    'Cada pantalla pertenece a una zona de la Figura 8.1, y cada zona admite ciertos roles: la zona pública, cualquiera; '
    'la zona de la bibliotecaria, solo esa cuenta; la zona compartida de PT-09, la bibliotecaria o la dirección. La base '
    'trae esa comprobación resuelta: cada página llama a exigir_zona() antes de mostrar nada (Código 11.1).',
    'Que la pantalla no muestre un botón no protege nada: alguien puede enviar el pedido igual. Por eso cada operación '
    'comprueba de nuevo el rol, como primera línea, con sin_permiso() (Código 11.2). Si la cuenta no tiene permiso, la '
    'respuesta es ME-13 y no cambia ningún dato.',
    'ME-12 y ME-13 no se confunden. ME-12 aparece solo al ingresar, cuando el usuario o la contraseña no coinciden, y no '
    'dice cuál de los dos falló. ME-13 aparece cuando una cuenta que ingresó bien pide algo que no le corresponde.',
])
CODIGOS_S113 = ['Código 11.1', 'Código 11.2']
EXPLICA = {
    'Código 11.1': 'La zona de cada página se escribe una vez, al principio. Si la cuenta de la sesión no tiene uno de '
                   'los roles de la zona, la página responde 403 con ME-13 y termina: no llega a ninguna operación.',
    'Código 11.2': 'Cada operación protegida empieza con esta llamada y la lista de roles de su contrato. Es la misma '
                   'comprobación que hace la página, repetida a propósito en la capa de reglas.',
}
TABLA_113_ROTULO = 'Tabla 11.3 — Qué responde cada operación según la cuenta (P-11)'
_ROL = {'bibliotecaria': 'bibliotecaria', 'dirección': 'direccion'}
TABLA_113 = (['Operación', 'Sin sesión', 'Bibliotecaria', 'Dirección'],
             [['%s %s' % (o, X.OPERACION[o][1])] +
              ['Permitida' if not X.ROLES_OP[o] else ('Permitida' if r in X.ROLES_OP[o] else 'ME-13')
               for r in (None, 'bibliotecaria', 'dirección')] for o in sorted(X.ROLES_OP)] +
             [['%s %s' % (a[0], a[1]), 'ME-13', 'Permitida', 'ME-13'] for a in C.AUXILIARES])
EJ113 = ('Ejemplo resuelto 11.3: demostrar el rechazo de un acceso indebido', [
    'Consigna: mostrar que la dirección no puede inactivar un ejemplar, aunque conozca la dirección de la página.',
    'Con la cuenta direccion1, se escribe a mano lectores.php en el navegador. Respuesta: ME-13, «%s»' % C.MENSAJES_PHP['ME-13'],
    'Se envía el formulario de inactivar desde una copia de la página, sin pasar por el menú. La operación responde ME-13 '
    'y el ejemplar sigue activo: la consulta pública lo sigue contando.',
    'Prueba: P-11, con las tres cuentas de la Tabla 11.3. Se anota el resultado de cada fila, no solo «funciona».',
])

S114 = ('11.4 Edición y baja lógica sin pérdida de historial', [
    'Corregir un dato es normal: un título mal escrito, un nombre con un error, un estudiante que cambió de curso. Lo que '
    'no se puede es que la corrección cambie el pasado. Por eso cada corrección dice qué se puede cambiar y qué no '
    '(Tabla 11.4), y la base protege lo que no se puede cambiar.',
    'Un lector o un ejemplar con historia no se borra: se da de baja, que en el sistema es quedar inactivo (RI-05). La '
    'operación OP-06 solo cambia el estado (Código 11.3). El lector inactivo no recibe préstamos nuevos (ME-01), el '
    'ejemplar inactivo no se presta, y su historial queda igual. Además, la base no deja borrar a quien tiene historial ni '
    'cambiar el código de un ejemplar con préstamos (Código 11.4).',
    'El curso de un estudiante se puede corregir con OA-04, pero los préstamos que ya hizo conservan el curso que tenía '
    'ese día (RI-08). Así el informe de un mes pasado no cambia aunque el estudiante pase de curso.',
])
CODIGOS_S114 = ['Código 11.3', 'Código 11.4']
EXPLICA['Código 11.3'] = ('La baja es un UPDATE del estado, nunca un DELETE. La condición activo = 1 hace que inactivar '
                          'dos veces no cambie nada: la operación responde MV-07.')
EXPLICA['Código 11.4'] = ('Si alguien intenta cambiar el código de un ejemplar que tiene préstamos, la base lo rechaza '
                          'aunque la orden no venga de ninguna operación del sistema.')
TABLA_114_ROTULO = 'Tabla 11.4 — Qué se puede corregir y qué no'
TABLA_114 = (['Dato', '¿Se corrige?', 'Cómo', 'Por qué'],
             [['Título y autor de una obra', 'Sí', 'OA-05 (MA-09)', 'Las ediciones, los ejemplares y el historial no cambian'],
              ['Nombre y curso de un lector', 'Sí', 'OA-04 (MA-07)', 'Los préstamos anteriores conservan su curso (RI-08)'],
              ['Tipo de lector', 'No', '—', 'Cambiaría el máximo de préstamos ya contados (RI-02)'],
              ['Código de un ejemplar o de un lector', 'No, si tiene historial', '—', 'El historial lo nombra (RI-05)'],
              ['Lector o ejemplar que ya no se usa', 'Se da de baja', 'OP-06 (MA-08)', 'Nada se borra (RI-05, RN-06)'],
              ['Un préstamo', 'No', '—', 'Sus datos son historial (RI-04); solo se completa la devolución']])
EJ114 = ('Ejemplo resuelto 11.4: dar de baja sin borrar', [
    'Consigna: el estudiante LE-0124 dejó el colegio. Darlo de baja y comprobar que nada se perdió.',
    'Con OP-06: «%s»' % C.con_datos('MA-08', 'Lector', 'LE-0124'),
    'En el Encuentro 22 se comprueba: LE-0124 sigue en la base, inactivo; inactivarlo otra vez responde MV-07 sin cambiar '
    'nada; y la base rechaza borrarlo si tiene historial (prueba de garantías de la base).',
    'La parte de P-10 que necesita préstamos (el historial queda igual y un préstamo nuevo responde ME-01) se completa en '
    'el Encuentro 24, cuando el préstamo y la devolución ya funcionan. Hasta entonces queda anotada como pendiente.',
])
ACT_E22 = [
    ('Ejercitá', [
        'Escribí qué mensaje (ME-12, ME-13 u otro) corresponde a cada caso:\n'
        '(a) contraseña equivocada; (b) la dirección intenta registrar un préstamo; (c) sin sesión, se pide el informe; '
        '(d) la bibliotecaria pide el informe.',
    ]),
    ('Resolvé', [
        'Construí OA-03, OA-04 y OP-06 en la base de tu equipo. Para las validaciones del lector, partí de la Tabla 11.2 y '
        'de los mensajes MV-01 a MV-04. Ejecutá PA-03, PA-04, P-10 y P-11 y anotá sus resultados.',
        'Hacé la demostración del Ejemplo resuelto 11.3 con otra operación de la Tabla 11.3.',
    ]),
    ('Pensá y decidí', [
        'La bibliotecaria pide un botón «Borrar lector» para los que egresan. Explicá qué le ofrecés en su lugar y por qué.',
    ]),
    ('Desafío', [
        'Proponé una prueba que demuestre que corregir el curso de un estudiante no cambia el informe de un mes anterior.',
    ]),
]

# ------------------------------------------------------------------ práctica
PRACTICA_TITULO = 'Práctica 11 — Un lote de libros donados y lectores con datos incompletos'
PRACTICA_INTRO = [
    'En Mbokaja llegó un lote de libros donados, cargado en una planilla por un voluntario. También hay lectores nuevos '
    'para registrar. Para esta práctica, el sistema de prueba de Mbokaja ya acepta las etiquetas MB- y tres cifras (M-F11): '
    'el profesor vecino adaptó la validación y la restricción de la base. Los datos tienen errores que hay que resolver '
    'antes de cargarlos, o que el sistema tiene que rechazar.',
]
NIVELES = [
    ('Nivel 1 — Guiado', [
        'Para cada fila del lote (MD-01 a MD-06), decidí: se registra tal cual, se corrige antes de registrar, o el sistema '
        'la rechaza. Escribí el mensaje que esperás en cada rechazo.',
        'Para cada lector (ML-1 a ML-3), escribí si se registra y, si no, qué mensaje responde y qué dato hay que pedir.',
    ]),
    ('Nivel 2 — Intermedio', [
        'MD-01, MD-02 y MD-04 parecen la misma obra. Decidí cuántas obras, ediciones y ejemplares hay que registrar, con '
        'qué operaciones y en qué orden, y qué hacés con el título mal escrito.',
        'Registrá el lote corregido en la copia de la base y comprobá con la consulta pública cuántos disponibles hay de '
        'cada título. Anotá esperado y obtenido.',
    ]),
    ('Nivel 3 — Ampliación', [
        'Los voluntarios de 9.º ayudan los miércoles con el encargado presente (MS-5). Decidí qué pueden hacer en el sistema '
        'y cómo se comprueba en el servidor. Tené en cuenta que son menores de edad y que no tienen que ver datos de otros '
        'estudiantes (MN-05).',
        'Escribí la prueba que demuestra tu decisión, con la cuenta, la operación y el mensaje esperado.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: ningún código repetido se registra; el título mal escrito no crea una obra nueva; '
                    'el estudiante sin curso y el docente con curso se rechazan con su mensaje; los voluntarios no '
                    'comparten la cuenta del encargado ni ven datos de lectores; cada decisión tiene su prueba.')

REPASO = ('Para repasar', [
    'Las tareas del incremento se ordenan por dependencias: primero lo que las demás necesitan.',
    'Cada regla del diccionario se valida en el servidor, con su mensaje, y se protege en la base con una restricción.',
    'Un código repetido se rechaza y no se reutiliza.',
    'Cada pantalla y cada operación comprueban el rol en el servidor: ME-13 sin cambiar datos. ME-12 es solo del ingreso.',
    'Corregir no cambia el pasado, y dar de baja no borra: el historial se conserva.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, los Encuentros 21 y 22 se reúnen en el Encuentro 16: «Lectores por carga '
    'inicial; los permisos mínimos vienen en la base y el equipo los prueba.»',
    'No se omiten: OA-02, OP-06 con P-10 y la prueba de permisos P-11 con la Tabla 11.3. Los lectores se usan como vienen '
    'en los datos iniciales; OA-03, OA-04 y OA-05 pasan a actividad complementaria.',
])

# ------------------------------------------------------------------ evaluación
EVAL_ID = 'ADS3-L4-C11'
EVAL_TITULO = 'Evaluación del Capítulo 11'
EVAL_TEXTO_BASE = ('Texto base — Sala de audiovisuales (situación de evaluación, ficticia)', [
    'AV-1 La sala presta proyectores y parlantes; cada equipo tiene un código PRY- y dos cifras.',
    'AV-2 Solo la coordinadora registra, corrige y da de baja los equipos.',
    'AV-3 Un proyector que se rompe no se presta más, pero sus préstamos anteriores se conservan.',
    'AV-4 Los docentes solo consultan qué equipos están disponibles.',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', 'Un docente que ingresó bien pide dar de baja un proyector. ¿Qué responde el sistema (AV-2, AV-4)?',
     ['Un error de permiso, sin cambiar datos.', 'Un error de usuario o contraseña.', 'Da de baja el proyector.',
      'Nada: el botón no aparece, así que no hace falta responder.']),
    ('mc', '¿Qué se hace con el proyector roto de AV-3?',
     ['Se marca inactivo y se conserva su historial.', 'Se borra con sus préstamos.', 'Se le cambia el código.',
      'Se borra solo el proyector y se dejan los préstamos.']),
    ('mc', '¿Dónde se protege que dos equipos no tengan el mismo código?',
     ['En la operación, con un mensaje, y en la base, con una restricción de unicidad.', 'Solo en el formulario.',
      'Solo en la bitácora.', 'En ningún lado: lo controla la coordinadora a mano.']),
    ('mc', 'El código «PRY-7» no cumple AV-1. ¿Qué mensaje es útil?',
     ['«El código PRY-7 no tiene el formato esperado (PRY- y dos cifras). Revisá la etiqueta.»', '«Error 500.»',
      '«Dato inválido.»', '«CHECK constraint failed.»']),
    ('vf', 'Ocultar el botón «Dar de baja» a los docentes alcanza para proteger la operación.',
     False, 'Falso. Cualquiera puede enviar el pedido; la operación comprueba el rol en el servidor.'),
    ('vf', 'Corregir el nombre de un equipo no tiene que cambiar sus préstamos anteriores.',
     True, 'Verdadero. Corregir no cambia el historial.'),
    ('vf', 'Si un código ya se usó en un equipo dado de baja, se puede reutilizar en uno nuevo.',
     False, 'Falso. El historial nombra ese código: no se reutiliza.'),
    ('ab', 'Armá una tabla con tres reglas de los datos de la sala (AV-…), la validación del servidor con su mensaje y la '
           'restricción de la base que corresponde a cada una.',
     'Por ejemplo: formato PRY- y dos cifras (AV-1): mensaje de formato y CHECK; código único: mensaje de código usado y '
     'UNIQUE; equipo inactivo no se presta (AV-3): rechazo en el préstamo y estado en la base. Un punto por cada regla '
     'completa y uno por citar las fuentes.', 4),
    ('ab', 'Diseñá la prueba que demuestra que un docente no puede dar de baja un equipo: cuenta, pedido, resultado '
           'esperado y qué comprobás en los datos.',
     'Cuenta de docente con sesión; pedido de baja enviado aunque no haya botón; error de permiso; el equipo sigue activo '
     'y su historial no cambió. Un punto por cada parte.', 4),
]
EVAL_PUNTAJE = 'Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno).'
