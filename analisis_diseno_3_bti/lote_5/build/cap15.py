# -*- coding: utf-8 -*-
"""Capítulo 15 — «Probar el sistema completo con usuarios» (Work §6: secciones 15.1 a 15.4 y práctica «revisión cruzada
entre equipos con datos reservados para evaluación»; encuentros 29 y 30).

Decisión 4 de Fernando: dos sesiones de uso con compañeros que representan roles distintos, con tareas nuevas y
observaciones registradas, sobre el sistema funcionando (no los bocetos del Capítulo 8); una persona de la biblioteca
real solo con autorización institucional, datos ficticios y resguardo de la privacidad. Decisión 2: el conjunto
reservado DR es exclusivo del docente y no se publica; el libro trae solo el procedimiento y la plantilla.
Permisos, persistencia y restauración se ejecutaron de verdad (build/reproducir.py). Capacidades de Work §5.2:
C8, C9 y C10 (Encuentro 29) y C3, C6 y C9 (Encuentro 30)."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'caso'))
import verificacion as V
C4, X = V.C4, V.X

NUM = 15
UNIDAD = 'Unidad V — Verificar, validar y mejorar'
CAPITULO = 'Capítulo 15'
TITULO = 'Probar el sistema completo con usuarios'
ENCUENTROS = (29, 30)
SECCIONES = ['15.1 Pruebas de integración y persistencia',
             '15.2 Permisos, recuperación de datos y manejo de errores',
             '15.3 Sesiones de uso y observación de dificultades',
             '15.4 Aceptación por criterios acordados y prioridad de correcciones']
PRACTICA_WORK = 'revisión cruzada entre equipos con datos reservados para evaluación'

ROTULO_CAPACIDAD = ('Capacidades propuestas para el programa institucional (C8 a C10 en el Encuentro 29; C3, C6 y C9 en '
                    'el Encuentro 30; no son capacidades oficiales del MEC)')
CAPACIDAD = ('C3. Especifica y prioriza requisitos verificables.\n'
             'C6. Diseña la interacción y la arquitectura del prototipo.\n'
             'C8. Integra un prototipo funcional con persistencia.\n'
             'C9. Verifica y mejora la solución a partir de evidencia.\n'
             'C10. Documenta, entrega y defiende el prototipo.')
TEMA = ('Pruebas del circuito completo, de la persistencia entre ejecuciones y de la restauración de un respaldo. Permisos '
        'con las tres cuentas y manejo de errores. Sesiones de uso con compañeros en roles, con tareas nuevas y '
        'observaciones registradas. Aceptación por los criterios del catálogo y prioridad de las correcciones.')
INDICADORES = [
    'Prueba el circuito completo y la persistencia entre ejecuciones, con la consulta del estado final.',
    'Ejecuta todas las operaciones con las tres cuentas y comprueba que cada rechazo sea ME-13 sin cambiar datos.',
    'Restaura un respaldo y comprueba que el estado es el del respaldo y que quedó la copia previa.',
    'Conduce o registra una sesión de uso con tareas nuevas, anotando lo que la persona hace y no opiniones.',
    'Marca cada criterio de aceptación con su evidencia y prioriza las correcciones dentro del alcance.',
]
TIEMPO = ('Dos encuentros de 5 HC (29 y 30 de la secuencia anual). Encuentro 29: 5 HC de verificación. Encuentro 30: 1 HC '
          'de análisis (repriorizar con lo observado) y 4 de verificación.')

APERTURA = [
    'Cada operación pasó sus casos. Falta probar el sistema entero: que las partes funcionen juntas, que los datos sigan '
    'ahí después de cerrar, que un respaldo se pueda recuperar y que cada cuenta vea solo lo suyo.',
    'Y falta lo más difícil: ver a otras personas usarlo. Una persona que no construyó el sistema encuentra en cinco minutos '
    'lo que el equipo no vio en cinco semanas. Con esas observaciones y los criterios del catálogo se decide qué está '
    'aceptado y qué se corrige primero.',
]
ARTICULACION = [
    'Con el Capítulo 8: allí se observó el uso de bocetos de papel. Ahora se observa el sistema funcionando, con tareas '
    'nuevas: no es la misma actividad.',
    'Con el Capítulo 11: la Tabla 11.3 (qué responde cada operación según la cuenta) se ejecuta completa.',
    'Con la Unidad VI: acá se prueba la restauración del propio equipo; la instalación por otro equipo es del Capítulo 17.',
]

AVISO_ENTORNO = C4.AVISO_ENTORNO

# ------------------------------------------------------------------ encuentro 29
E29_TITULO = 'Encuentro 29 — Integración, permisos, persistencia y restauración'

S151 = ('15.1 Pruebas de integración y persistencia', [
    'Una prueba de integración recorre varias operaciones en el orden en que las usa la biblioteca: se da de alta un '
    'ejemplar, se presta, se intenta prestar otra vez, se devuelve y se ve en el informe. Cada paso usa lo que dejó el '
    'anterior. Es el recorrido E-6a de la ficha de entorno, ahora con los datos DP.',
    'La persistencia se prueba entre dos ejecuciones: un proceso registra un préstamo y termina; otro, que no sabe nada del '
    'primero, abre la base y lo busca. Si el préstamo está, se guardó en el archivo y no solo en la memoria del programa '
    '(Tabla 15.1).',
    'Lo que no se puede probar en el entorno de construcción queda pendiente, con su motivo: P-13, sin internet en la '
    'computadora del colegio, se hace allí.',
])
TABLA_151_ROTULO = 'Tabla 15.1 — Integración, persistencia y restauración del prototipo del equipo modelo'


def tabla_151():
    r = V.resumen()
    i = r['integracion']['v1_lote4']
    http = C4.resultados_pruebas()['referencia_docente']['prueba_http.sh']['resultado'].replace('Resultado: ', '')
    bien = lambda b: 'Comprobado' if b else 'No coincide'
    return (['Prueba', 'Cómo', 'Resultado', 'Condición'],
            [['Recorrido E-6a', 'prueba_http.sh: consulta, ingreso, alta, préstamo, doble préstamo, devolución, informe', http, 'Comprobado'],
             ['Persistencia', 'Un proceso registra un préstamo; otro proceso lo busca', 'Está' if i['persistencia'] else 'No está', bien(i['persistencia'])],
             ['Permisos (Tabla 15.2)', 'Cada operación con las tres cuentas', i['permisos'].replace('Resultado: ', ''), bien(i['permisos_ok'])],
             ['Restauración (E-11, E-12)', 'Respaldo, un préstamo nuevo, restauración, búsqueda del préstamo',
              'El estado es el del respaldo; quedó la copia previa' if i['restauracion'] else 'No coincide', bien(i['restauracion'])],
             ['Sin internet (P-13)', 'Desconectar la red en la computadora del colegio', '—', 'Pendiente']])


NOTA_151 = 'Entorno: %s. En la computadora del colegio, estas pruebas siguen pendientes hasta hacerlas allí.'

S152 = ('15.2 Permisos, recuperación de datos y manejo de errores', [
    'La Tabla 11.3 decía qué tenía que responder cada operación según la cuenta. Ahora se ejecuta completa: cada operación '
    'con la cuenta de la bibliotecaria, la de dirección y sin sesión (Tabla 15.2). Cada rechazo tiene que ser ME-13 y no '
    'cambiar ningún dato; la consulta pública no pide sesión y no muestra lectores.',
    'Recuperar datos es restaurar un respaldo. La prueba tiene cuatro pasos: respaldar, hacer un cambio, restaurar y '
    'comprobar que el cambio ya no está, porque el estado es el del respaldo. La restauración de la base del proyecto '
    'pide confirmación y guarda antes una copia de la base actual: también se comprueba que esa copia exista.',
    'Los fallos previsibles de la Tabla 12.3 (base ocupada, formulario vencido, fecha imposible) se vuelven a ejecutar con '
    'DP: un error tiene que decir qué pasó y no dejar datos a medias.',
])
TABLA_152_ROTULO = 'Tabla 15.2 — Permisos ejecutados con las tres cuentas (prototipo del equipo modelo, datos DP)'


def tabla_152():
    return (['Operación', 'Sin sesión', 'Bibliotecaria', 'Dirección'], V.filas_permisos('v1_lote4'))


EJ151 = ('Ejemplo resuelto 15.1: restaurar y comprobar', [
    'Consigna: demostrar que un respaldo se puede recuperar, en una copia descartable con DP.',
    '1. php respaldar.php: el respaldo queda en datos/respaldos/. 2. Se registra un préstamo nuevo de EJ-1008 a LE-1005. '
    '3. php restaurar.php con el respaldo: valida el archivo, muestra qué contiene y pide escribir RESTAURAR.',
    '4. Se busca el préstamo de EJ-1008: ya no está, porque el respaldo es anterior. Y en datos/respaldos/ quedó la copia '
    '«antes_de_restaurar», por si había que volver atrás.',
    'Se registra con el entorno. Que la restauración funcione en la computadora del colegio (E-12) es otra prueba, pendiente '
    'hasta hacerla allí.',
])
ACT_E29 = [
    ('Ejercitá', [
        'Ordená los pasos de la prueba de restauración y decí qué se comprueba en cada uno:\n'
        'restaurar · respaldar · buscar el préstamo · registrar un préstamo nuevo.',
    ]),
    ('Resolvé', [
        'En una copia descartable con DP, ejecutá la Tabla 15.2 completa con tu prototipo y anotá el resultado de cada fila.',
        'Hacé la prueba de persistencia y la de restauración, y registrá las dos con su entorno y su condición.',
    ]),
    ('Pensá y decidí', [
        'La restauración funcionó en la notebook de un integrante. ¿Se puede marcar E-12 como comprobada para el laboratorio? '
        'Explicá qué registrás.',
    ]),
]

# ------------------------------------------------------------------ encuentro 30
E30_TITULO = 'Encuentro 30 — Sesiones de uso y aceptación'

S153 = ('15.3 Sesiones de uso y observación de dificultades', [
    'En una sesión de uso, una persona que no construyó el sistema hace tareas reales con él, y el equipo observa. Se hacen '
    'dos sesiones, con compañeros que representan roles distintos: por ejemplo, la bibliotecaria y la dirección. Las tareas '
    'son nuevas: no las del recorrido de prueba, sino otras que la persona no ensayó.',
    'Quien observa anota lo que la persona hace, dónde se detiene y qué pregunta. No ayuda ni explica: si ayuda, ya no se '
    'sabe si el sistema se entiende solo (RNF-01, P-14). Las opiniones («está lindo») se anotan aparte; lo que cuenta es lo '
    'observado (Tabla 15.3).',
    'No es la sesión del Capítulo 8: allí se observaba un boceto de papel; ahora, el sistema funcionando, con sus mensajes y '
    'sus datos.',
])
SESIONES_ROTULO = 'Tabla 15.3 — Sesiones de uso del equipo modelo (simulación del libro, con compañeros en roles)'
SESIONES = (['Sesión', 'Rol', 'Tarea nueva', 'Lo que hizo', 'Dificultad', 'Req.'], [list(s) for s in V.SESIONES])
PERSONA_REAL = ('Si participa alguien de la biblioteca real', [
    'Solo con autorización de la institución y con datos ficticios: la persona usa la copia descartable, nunca una base con '
    'datos de lectores reales.',
    'No se graban ni se fotografían caras ni pantallas con datos personales. Lo que se anota es lo que hizo con el sistema, '
    'sin su nombre.',
    'Si la institución no lo autoriza, las dos sesiones se hacen con compañeros en roles: es la forma prevista.',
])

S154 = ('15.4 Aceptación por criterios acordados y prioridad de correcciones', [
    'Aceptar es marcar cada criterio del catálogo con su evidencia: aceptado, no aceptado o pendiente (Tabla 15.4). Un '
    'criterio está aceptado si todos sus casos dieron lo esperado; si alguno no coincide, no está aceptado; si falta la '
    'prueba, está pendiente. La tabla del equipo modelo se arma con los resultados reales de la Tabla 14.6.',
    'Después se priorizan las correcciones (Tabla 15.5): primero lo que impide un criterio imprescindible o lo que pasa '
    'seguido; después lo que molesta pero no impide. Lo que no entra en el tiempo de la unidad queda como límite conocido '
    'de la versión candidata. Y lo que no es un defecto, sino un pedido nuevo, va por una solicitud de cambio.',
])
TABLA_154_ROTULO = 'Tabla 15.4 — Acta de aceptación del equipo modelo (resultados en el entorno de construcción)'


def tabla_154():
    return (['Req.', 'Requisito (resumido)', 'Evidencia', 'Estado'], [list(a) for a in V.acta('v1_lote4')])


TABLA_155_ROTULO = 'Tabla 15.5 — Prioridad de las correcciones (equipo modelo)'
TABLA_155 = (['Incidencia', 'Gravedad', 'Frecuencia', 'Req.', 'Decisión'], [list(p) for p in V.PRIORIDADES])
EJ152 = ('Ejemplo resuelto 15.2: de una observación a una solicitud de cambio', [
    'Consigna: en la sesión S2, la dirección vio un mes con «Total 0» y preguntó si el sistema había fallado. ¿Qué se hace?',
    'Se revisa el criterio: RF-09 pide el informe por curso, y C-19 dio lo que dice el contrato. No es un defecto.',
    'Pero la observación es real: el mensaje no ayuda. Se registra como pedido de mejora y la dirección lo tramita como '
    'solicitud de cambio, SC-02 (Capítulo 16).',
    'IN-02, en cambio, sí impide un criterio (RNF-01: la bibliotecaria tiene que poder registrar sin ayuda) y aparece cada '
    'vez que hay un error: es la primera corrección.',
])
ACT_E30 = [
    ('Ejercitá', [
        'Clasificá cada anotación como observación u opinión:\n(a) «tardó en encontrar Devolver»; (b) «el sistema es lindo»; '
        '(c) «escribió el código dos veces»; (d) «yo lo haría en azul».',
    ]),
    ('Resolvé', [
        'Hacé las dos sesiones de uso con dos compañeros en roles distintos y tareas nuevas, y registralas como la Tabla 15.3.',
        'Armá el acta de aceptación de tu equipo como la Tabla 15.4, con tus resultados, y la tabla de prioridades.',
    ]),
    ('Pensá y decidí', [
        'Un criterio imprescindible quedó pendiente porque no hubo tiempo de probarlo. ¿Se puede entregar la versión candidata '
        'con ese criterio como aceptado? Explicá.',
    ]),
]

# ------------------------------------------------------------------ práctica
PRACTICA_TITULO = 'Práctica 15 — Revisión cruzada entre equipos con datos reservados'
PRACTICA_INTRO = [
    'Cada equipo prueba el prototipo de otro equipo. Los datos son reservados: los entrega el docente en el momento, en una '
    'copia descartable que prepara con el cargador. Nadie los conoce antes, así que nadie puede preparar su sistema para '
    'ellos: es la evaluación con datos independientes que pide Work.',
    'El equipo revisor entrega un reporte con la plantilla de la Tabla 15.6 y no corrige nada del otro equipo: reporta. Todo '
    'se hace en la copia descartable; ningún dato personal real.',
]
PLANTILLA_ROTULO = 'Tabla 15.6 — Plantilla del reporte de la revisión cruzada'
PLANTILLA = (['Campo', 'Qué se escribe'],
             [['Equipo revisado y versión', 'Nombre del equipo y versión de su prototipo'],
              ['Copia y huella', 'Carpeta de la copia y la huella que informó el cargador'],
              ['Caso', 'Identificador, requisito, clase y entradas'],
              ['Esperado y obtenido', 'Lo que tenía que pasar y lo que pasó, con el mensaje exacto'],
              ['Condición', 'Comprobado, reproducido, simulado o pendiente'],
              ['Defecto (si hay)', 'Pasos, gravedad y requisito afectado'],
              ['Entorno', 'Computadora, sistema, versiones']])
NIVELES = [
    ('Nivel 1 — Guiado', [
        'Ejecutá sobre el prototipo del otro equipo los casos que te entrega el docente y completá la Tabla 15.6 para cada uno.',
        'Marcá cuáles coinciden y cuáles no, y reproducí dos veces cada uno que no coincida.',
    ]),
    ('Nivel 2 — Intermedio', [
        'Con los datos reservados, diseñá tres casos propios de límite o de rechazo que el docente no te dio, ejecutalos y '
        'registralos.',
        'Escribí un reporte de defecto completo para cada caso que no coincida, con su gravedad.',
    ]),
    ('Nivel 3 — Ampliación', [
        'Recibí el reporte que el otro equipo hizo de tu prototipo. Priorizá sus defectos con el criterio de la Tabla 15.5 y '
        'justificá la prioridad de cada uno.',
        'Decidí cuáles corregís en el Capítulo 16 y cuáles quedan como límites conocidos, y por qué.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: la copia se preparó con el cargador y la huella quedó anotada; cada caso tiene '
                    'esperado, obtenido, entorno y condición; los defectos se reproducen antes de reportarse; el revisor '
                    'reporta y no corrige; ningún dato reservado se copia fuera de la sesión.')

REPASO = ('Para repasar', [
    'La integración prueba el circuito completo; la persistencia, que los datos siguen en otra ejecución.',
    'Cada operación se prueba con las tres cuentas: un rechazo es ME-13 y no cambia datos.',
    'Restaurar se prueba con un cambio después del respaldo: después de restaurar, el cambio ya no está.',
    'En una sesión de uso se anota lo que la persona hace; el observador no ayuda.',
    'Un criterio se acepta con evidencia; lo que no se probó queda pendiente, y lo que es un pedido nuevo va por solicitud de cambio.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, los Encuentros 29 y 30 pasan a ser el 22 y el 23, sin cambios.',
    'No se reduce lo esencial: permisos, persistencia y restauración (condiciones mínimas de Work §4.3), las dos sesiones de '
    'uso y el acta de aceptación. Pasan a lectura domiciliaria el Ejemplo resuelto 15.2 y el nivel 3 de la Práctica 15.',
])

# ------------------------------------------------------------------ evaluación
EVAL_ID = 'ADS3-L5-C15'
EVAL_TITULO = 'Evaluación del Capítulo 15'
EVAL_TEXTO_BASE = ('Texto base — Reserva de espacios escolares (situación de evaluación, ficticia)', [
    'EE-1 El salón de actos y el laboratorio se reservan por franjas de una hora.',
    'EE-2 Dos reservas del mismo espacio no pueden superponerse.',
    'EE-3 La secretaría reserva; los docentes consultan las franjas libres.',
    'EE-4 Cada viernes se hace un respaldo de las reservas.',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', '¿Cómo se prueba que las reservas persisten?',
     ['Un proceso registra una reserva y otro, después, la busca.', 'Se mira la pantalla después de reservar.',
      'Se reserva dos veces.', 'Se pregunta a la secretaría.']),
    ('mc', 'Un docente intenta reservar el salón (EE-3). ¿Qué tiene que pasar?',
     ['Un rechazo por permiso, sin cambiar datos.', 'Se registra la reserva.', 'Un error de contraseña.',
      'Se reserva a nombre de la secretaría.']),
    ('mc', 'Para probar el respaldo de EE-4, después de respaldar, ¿qué se hace?',
     ['Un cambio, la restauración y la comprobación de que el cambio ya no está.', 'Nada: si el archivo existe, alcanza.',
      'Borrar la base.', 'Restaurar sin hacer ningún cambio.']),
    ('mc', 'En una sesión de uso, la persona no encuentra cómo cancelar una reserva. ¿Qué hace el observador?',
     ['Anota dónde se detuvo y qué buscó, sin ayudar.', 'Le muestra el botón.', 'Termina la sesión.', 'Cambia la tarea.']),
    ('vf', 'Las sesiones de uso del sistema funcionando son la misma actividad que la revisión de bocetos en papel.',
     False, 'Falso. Ahora se prueba el sistema funcionando, con tareas nuevas.'),
    ('vf', 'Un criterio de aceptación sin prueba ejecutada se marca como pendiente.',
     True, 'Verdadero. No se da por aceptado.'),
    ('vf', 'En una revisión cruzada, el equipo revisor corrige los defectos que encuentra en el otro prototipo.',
     False, 'Falso. Reporta; corrige el equipo dueño del prototipo.'),
    ('ab', 'Escribí la prueba de EE-2 como prueba de integración: los pasos, el esperado y la consulta del estado final.',
     'Reservar una franja; intentar otra reserva superpuesta del mismo espacio; esperado: rechazo con mensaje; consulta: '
     'una sola reserva en esa franja. Un punto por cada parte.', 4),
    ('ab', 'Redactá dos observaciones y una opinión posibles de una sesión de uso de la secretaría, y decí qué harías con cada una.',
     'Observaciones: lo que hizo y dónde se detuvo (1 punto cada una, con su requisito). Opinión: se anota aparte y no decide '
     '(1 punto). Qué se hace: corrección priorizada o solicitud de cambio (1 punto).', 4),
]
EVAL_PUNTAJE = 'Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno).'
