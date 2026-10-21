# -*- coding: utf-8 -*-
"""Capítulo 9 — «Arquitectura y revisión del diseño» (Work §6: secciones 9.1 a 9.4 y evaluación integradora de la
primera etapa con H3; encuentros 17 y 18).

Decisiones de Fernando (20-oct-2026): tres capas (presentación, reglas de negocio y persistencia); contratos con
entradas, precondiciones, resultados, errores y requisitos; HTML/CSS, PHP y SQLite como ejemplo técnico provisional,
no obligatorio ni aprobado para todos los colegios; funcionamiento local y sin servicios pagos obligatorios; sin la
matriz de selección tecnológica de Algorítmica 3.º. La Práctica 9 es un complemento editorial al índice de Work, breve,
ubicada en el Encuentro 17 o como actividad complementaria, sin desplazar el H3. Capacidades de Work §5.2: C5 y C6
(Encuentro 17) y C1 a C7 (Encuentro 18, H3)."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'caso'))
import diseno as X
import mbokaja_u3 as MB
R, D, MO = X.R, X.D, X.MO

NUM = 9
UNIDAD = 'Unidad III — Diseñar una solución coherente'
CAPITULO = 'Capítulo 9'
TITULO = 'Arquitectura y revisión del diseño'
ENCUENTROS = (17, 18)
SECCIONES = ['9.1 Presentación, reglas de negocio y persistencia',
             '9.2 Responsabilidades, entradas, salidas y contratos de operaciones',
             '9.3 Entorno, dependencias y decisiones técnicas justificadas',
             '9.4 Coherencia entre requisitos, datos e interfaces']
REVISION_WORK = 'Evaluación integradora de la primera etapa: defensa y corrección del dossier; H3'
PRACTICA_WORK = 'complemento editorial: contrato de devolución, libro dañado, reposición y mantenimiento del entorno'

ROTULO_CAPACIDAD = ('Capacidades propuestas para el programa institucional (C5 y C6; en el H3, C1 a C7; no son '
                    'capacidades oficiales del MEC)')
CAPACIDAD = ('C5. Justifica el modelo de información y sus reglas de integridad.\n'
             'C6. Diseña la interacción y la arquitectura del prototipo.\n'
             'En el H3 se evalúan juntas C1 a C7.')
TEMA = ('Separación entre presentación, reglas de negocio y persistencia. Responsabilidades y contratos de operaciones: '
        'entradas, precondiciones, resultados y errores. Entorno, dependencias y registro de decisiones técnicas. Matriz de '
        'coherencia entre requisitos, datos, interfaces y operaciones. Evaluación integradora de la primera etapa (H3).')
INDICADORES = [
    'Identifica qué hace la presentación, qué deciden las reglas de negocio y qué guarda la persistencia, y ubica cada regla del caso.',
    'Escribe el contrato de una operación con sus entradas, precondiciones, resultado, errores y requisitos vinculados.',
    'Registra una decisión técnica con su contexto, las condiciones excluyentes, las opciones, la decisión y sus consecuencias.',
    'Comprueba la coherencia entre requisitos, datos, pantallas, operaciones y pruebas, y corrige los huecos.',
    'Defiende el dossier de las Unidades I a III y resuelve individualmente una variante no vista.',
]
TIEMPO = ('Dos encuentros de 5 HC (17 y 18 de la secuencia anual). El Encuentro 18 es la evaluación integradora de la '
          'primera etapa (H3): 4 HC de defensa y 1 HC de corrección del dossier.')

APERTURA = [
    'Ya hay un modelo de datos y bocetos de las pantallas. Falta decidir cómo se organiza el sistema por dentro: qué parte '
    'muestra, qué parte decide y qué parte guarda, y qué promete cada operación. Esa organización es la arquitectura.',
    'Al final del capítulo, el equipo defiende todo lo que hizo en la primera mitad del año, desde el problema hasta la '
    'arquitectura, en la evaluación integradora: el hito H3.',
]
ARTICULACION = [
    'Con los Capítulos 7 y 8: las operaciones leen y guardan los datos del modelo, y sus errores son los mensajes de las '
    'pantallas.',
    'Con Algorítmica 3.º: allí se elige una tecnología con una matriz de decisión con criterios cuantificados. Acá no se '
    'repite: la decisión técnica se registra con sus condiciones excluyentes y sus consecuencias.',
    'Con Laboratorio de 3.º y la Unidad IV: el entorno se instala y se prueba en la Unidad IV; acá solo se decide y se deja '
    'registrado qué hay que verificar.',
]

# ------------------------------------------------------------------ encuentro 17
E17_TITULO = 'Encuentro 17 — Responsabilidades, contratos y entorno'

S91 = ('9.1 Presentación, reglas de negocio y persistencia', [
    'Un sistema se organiza mejor si cada parte tiene una responsabilidad. La presentación muestra las pantallas, recibe lo '
    'que la persona escribe y muestra los mensajes. Las reglas de negocio deciden si una operación se puede hacer: '
    'comprueban permisos, reglas y restricciones. La persistencia guarda y recupera los datos.',
    'Separarlas tiene dos ventajas. Si cambia una pantalla, las reglas no cambian; si cambia una regla, como el máximo de '
    'los docentes, se toca un solo lugar. Y ninguna regla depende de que la pantalla «se porte bien»: aunque alguien '
    'envíe un pedido sin usar la pantalla, las reglas se comprueban igual en el servidor (Work §7.5).',
    'Las restricciones más importantes se protegen dos veces. RI-01 (un solo préstamo activo por ejemplar) la comprueba la '
    'capa de reglas y la protege también la persistencia: si dos pedidos llegan a la vez por el mismo ejemplar, se '
    'registra uno solo. Cómo se programa esa protección se ve en el Capítulo 12.',
])
LEYENDA_CAPAS = 'Tabla 9.1 — Símbolos del esquema de capas'
LEAD_FIG91 = ('La Figura 9.1 muestra las tres capas y las seis operaciones del núcleo. Las flechas van hacia abajo: la '
              'pantalla pide, las reglas deciden y la persistencia guarda.')
EPI_FIG91 = 'Figura 9.1 — Esquema de capas del sistema de préstamos.'
TABLA_92_ROTULO = 'Tabla 9.2 — Dónde vive cada regla del caso'
TABLA_92 = (['Regla o restricción', 'Presentación', 'Reglas de negocio', 'Persistencia'],
            [['RI-01 Un préstamo activo por ejemplar (RN-01)', 'Muestra ME-03', 'La comprueba en OP-01', 'La protege ante pedidos simultáneos'],
             ['RI-02 Máximo según el tipo (RN-02 v1.1)', 'Muestra ME-02 con el máximo', 'Lee el máximo en Parámetro y compara', 'Guarda el parámetro'],
             ['RI-03 Inactivos no reciben préstamos (RN-04)', 'Muestra ME-01', 'La comprueba en OP-01', 'Guarda el estado'],
             ['RI-04 y RI-05 Historial sin borrar (RN-05, RN-06)', 'No ofrece botones para borrar', 'Ninguna operación borra', 'No permite borrar lo que tiene historia'],
             ['RNF-02 Solo la bibliotecaria registra', 'Separa las zonas (Figura 8.1)', 'Comprueba el rol en cada operación', 'Guarda las cuentas y sus roles']])

S92 = ('9.2 Responsabilidades, entradas, salidas y contratos de operaciones', [
    'Una operación es un pedido que la presentación le hace a la capa de reglas: «registrá este préstamo». Su contrato es '
    'la promesa de lo que hace, escrita antes de programarla. Tiene cinco partes: las entradas que recibe, las '
    'precondiciones que tienen que cumplirse, el resultado (lo que devuelve y cómo quedan los datos), los errores que puede '
    'devolver y los requisitos que cumple.',
    'Los contratos salen de lo que ya está hecho. Las entradas son los campos de la pantalla; las precondiciones, los '
    'permisos y las reglas; los errores, los flujos alternativos del caso de uso con sus mensajes; el resultado, las '
    'restricciones del modelo. Si un error no tiene mensaje, o un mensaje no corresponde a ningún error, hay una '
    'incoherencia que corregir.',
])
TABLA_93_ROTULO = 'Tabla 9.3 — Operaciones del núcleo'
TABLA_93 = (['Operación', 'Nombre', 'Entradas', 'Requisitos'], [[o[0], o[1], o[2], ', '.join(o[6])] for o in X.OPERACIONES])
EJ91 = ('Ejemplo resuelto 9.1: el contrato de «registrar préstamo»', [
    'Consigna: escribir el contrato de OP-01 a partir de CU-01, de las restricciones del Capítulo 7 y de los mensajes del '
    'Capítulo 8.',
    'Entradas: los dos campos de PT-05 (código del lector y del ejemplar) y la cuenta que opera.',
    'Precondición: la cuenta es de la bibliotecaria (RNF-02). Si no, error ME-13 (sin permiso), y la operación no hace nada. ME-12 es otro error: usuario o contraseña incorrectos al ingresar.',
    'Errores: uno por cada flujo alternativo de CU-01 (4a, 4b, 5a), con su mensaje (ME-01, ME-02, ME-03), más el ejemplar '
    'inexistente (ME-05).',
    'Resultado: un préstamo nuevo, con la fecha de hoy, el curso si es estudiante (RI-08) y el vencimiento con el plazo '
    'vigente (RI-07). Si dos pedidos llegan a la vez por el mismo ejemplar, se registra uno solo (RI-01).',
    'Requisitos: RF-01, RF-02, RF-04, RF-05, RF-06, RF-11 y RNF-02. Las Tablas 9.3 y 9.4 reúnen las cinco partes de los '
    'contratos de las tres operaciones prioritarias.',
])
TABLA_94_ROTULO = 'Tabla 9.4 — Contratos de las operaciones prioritarias (equipo modelo)'
TABLA_94 = (['Operación', 'Precondición', 'Resultado', 'Errores'],
            [[o + ' ' + X.OPERACION[o][1], X.OPERACION[o][3], X.OPERACION[o][4], '\n'.join(X.OPERACION[o][5])]
             for o in X.PRIORITARIAS])

S93 = ('9.3 Entorno, dependencias y decisiones técnicas justificadas', [
    'El entorno es todo lo que el sistema necesita para funcionar: la computadora, el sistema operativo, el servidor web, '
    'el lenguaje, la base de datos y las bibliotecas que se usan. Cada pieza es una dependencia: si falta o cambia, el '
    'sistema puede dejar de funcionar. Por eso el entorno se decide con cuidado y se deja escrito.',
    'Una decisión técnica se registra con su contexto, las condiciones excluyentes, las opciones, la decisión y sus '
    'consecuencias. Las condiciones excluyentes se revisan primero: una opción que no cumple RS-01 (sin internet) o RS-02 '
    '(sin costo) se descarta, por buena que parezca. No se ponen puntajes: se escriben razones que se puedan discutir.',
    'El registro de la Tabla 9.5 usa como ejemplo la ruta técnica que propone Work: HTML y CSS, PHP y SQLite, en la '
    'computadora de la biblioteca. Es un ejemplo provisional: no es obligatorio, no está aprobado para todos los colegios y '
    'todavía no se probó en equipos escolares reales. La institución puede usar el entorno que ya domine, si cumple las '
    'mismas condiciones.',
])
TABLA_95_ROTULO = 'Tabla 9.5 — Registro de la decisión técnica DT-01 (equipo modelo)'
TABLA_95 = (['Campo', 'Contenido'], [list(x) for x in X.DT01])
EJ92 = ('Ejemplo resuelto 9.2: descartar antes de comparar', [
    'Consigna: aplicar las condiciones excluyentes de DT-01 a una propuesta nueva de un compañero: «usemos una aplicación '
    'web gratis en internet, que no hay que instalar».',
    'RS-01: la computadora de la biblioteca no siempre tiene internet (E4-L10). Sin conexión, la bibliotecaria no podría '
    'prestar en el recreo. La propuesta se descarta por RS-01, sin necesidad de compararla con las demás.',
    'Lo que sí aporta la propuesta: no instalar nada es una ventaja real. Queda anotado como consecuencia de la opción '
    'elegida: hay que instalarla y alguien tiene que saber hacerlo.',
])

ACT_E17 = [
    ('Ejercitá', [
        'Indicá en qué capa va cada responsabilidad:\n'
        '(a) mostrar «0 disponibles por ahora»; (b) comprobar que el lector no esté inactivo; (c) guardar la fecha de '
        'devolución; (d) leer el máximo vigente de los docentes; (e) desactivar el botón mientras se guarda.',
    ]),
    ('Resolvé', [
        'Escribí el contrato completo de OP-06 «inactivar lector o ejemplar», con sus cinco partes. Agregá el error que hace '
        'falta si el lector todavía tiene un préstamo activo y decidí qué mensaje le corresponde.',
        'Revisá la Tabla 9.6: encontrá una fila donde falte algo y proponé cómo completarla.',
    ]),
    ('Pensá y decidí', [
        'Un compañero dice: «si el botón Prestar ya no aparece para quien no es bibliotecaria, no hace falta comprobar el rol '
        'en el servidor». Explicá por qué no alcanza.',
    ]),
    ('Desafío', [
        'Agregá a DT-01 una opción D concreta con el entorno que tu curso usa en Laboratorio, y aplicale las condiciones '
        'excluyentes. ¿Qué tendrías que verificar antes de la Unidad IV?',
    ]),
]

S94 = ('9.4 Coherencia entre requisitos, datos e interfaces', [
    'Al terminar el diseño hay muchas piezas: requisitos, modelo de datos, pantallas, mensajes, operaciones y pruebas '
    'previstas. Son coherentes si cada requisito tiene su respuesta en cada capa y ninguna pieza contradice a otra. La '
    'matriz de coherencia amplía la matriz de trazabilidad del Capítulo 6 con tres columnas: los datos, la interfaz y la '
    'operación.',
    'Un hueco en la matriz es algo que falta: un requisito sin pantalla, una pantalla sin operación, un error sin mensaje. '
    'Un «—» puede ser correcto, si se explica: RS-02 no tiene pantalla porque es una condición del entorno. La matriz se '
    'revisa en equipo antes del H3, y cada corrección se registra con su versión.',
])
TABLA_96_ROTULO = 'Tabla 9.6 — Matriz de coherencia del catálogo v1.1'
TABLA_96 = (['Requisito', 'Datos (Capítulo 7)', 'Interfaz (Capítulo 8)', 'Operación (Capítulo 9)', 'Prueba'],
            [list(f) for f in X.COHERENCIA])
EJ93 = ('Ejemplo resuelto 9.3: el impacto de SC-01 en las tres capas', [
    'Consigna: seguir la solicitud SC-01 (máximo de cinco para los docentes, Capítulo 6) hasta el diseño.',
    'Datos: el lector tiene un tipo (RF-11) y Parámetro guarda maximo_docente = 5. Ninguna tabla nueva.',
    'Interfaz: PT-08 pide el tipo al registrar un lector; ME-02 muestra el máximo de ese tipo.',
    'Reglas: OP-01 lee el máximo del tipo del lector. Su contrato agrega RF-11 a los requisitos.',
    'Pruebas: P-06 se desdobla en P-06a y P-06b, como decidió SC-01.',
    'Conclusión: porque RF-05 decía «máximo vigente» y el máximo está en Parámetro, el cambio no obligó a rediseñar nada; '
    'solo a agregar un dato y un valor.',
])

# ------------------------------------------------------------------ encuentro 18
E18_TITULO = 'Encuentro 18 — Evaluación integradora de la primera etapa'
H3_TITULO = 'Evaluación integradora de la primera etapa — Hito H3: dossier consistente y evidencia individual'
H3_TEXTO = [
    'El H3 es la evaluación intermedia del año. Cada equipo defiende su dossier completo de las Unidades I a III: el problema '
    'y el alcance, el relevamiento, el catálogo de requisitos en su versión vigente, los modelos funcionales, el modelo de '
    'datos con su diccionario, los bocetos con sus estados y la arquitectura con sus contratos y su decisión técnica. La '
    'matriz de coherencia muestra que todo encaja.',
    'Durante la defensa, el docente le propone a cada integrante una variante que no se resolvió antes: un cambio de regla '
    'o de datos. Cada estudiante explica, solo, qué cambia en los datos, en la pantalla y en la operación, y qué se revisa '
    'aunque no cambie. Después de la defensa, el equipo corrige el dossier con lo que se le observó y registra la versión '
    'nueva.',
]
H3_LISTA = ('Antes de presentar: lista de verificación del equipo', [
    '1. ¿El dossier tiene la versión vigente de cada documento, y la bitácora dice qué cambió?',
    '2. ¿El catálogo está en su versión vigente (como mínimo, la v1.1 con SC-01), con fuente, prioridad y criterio?',
    '3. ¿Los modelos del Capítulo 5 citan requisitos que existen?',
    '4. ¿Cada préstamo es de un ejemplar, el historial no se borra y cada campo del diccionario tiene su origen?',
    '5. ¿Los tres recorridos tienen bocetos, estados y mensajes para cada flujo alternativo?',
    '6. ¿Cada operación tiene su contrato y cada error, su mensaje?',
    '7. ¿La decisión técnica cumple RS-01 y RS-02 y dice qué falta verificar?',
    '8. ¿La matriz de coherencia no tiene huecos sin explicar?',
])
H3_EVALUACION = ('Cómo se evalúa el H3', [
    'Se evalúan seis criterios, que cubren las capacidades C1 a C7, con los cuatro niveles de desempeño del H1 y el H2: '
    'Sólido, Logrado, En desarrollo e Inicial. La rúbrica completa está en la guía docente, y tu docente la comparte antes de '
    'la defensa.',
    'Cada criterio combina un 60 % de evidencia del producto del equipo y un 40 % de evidencia individual: la resolución de '
    'tu variante, tu aporte registrado en la bitácora y la observación del docente. La proporción y los niveles son una '
    'propuesta editorial: la institución decide cómo se convierten en calificación.',
    'Si falta una evidencia, se registra como ausente y se acuerda cuándo entregarla; no se confunde con un desempeño de '
    'nivel inicial.',
])
RUBRICA_H3 = [
    ('Problema, relevamiento y alcance', 'C1, C2',
     ['Problema y alcance actualizados con las decisiones del año; cada necesidad rastreable a su fuente; anticipa el efecto de una variante.',
      'Problema, alcance y necesidades con fuentes, vigentes.',
      'Alcance desactualizado o necesidades sin fuente.',
      'Sin problema delimitado ni alcance vigente.'],
     'Ficha de problema, dossier y alcance', 'Explica de dónde sale una decisión de alcance'),
    ('Requisitos y trazabilidad', 'C3',
     ['Catálogo versionado sin ambigüedades, con criterios comprobables, prioridades razonadas y cambios tramitados con impacto.',
      'Catálogo vigente con fuente, prioridad y criterio; cambios registrados.',
      'Requisitos sin criterio o cambios sin registro.',
      'Sin catálogo o con soluciones en lugar de requisitos.'],
     'Catálogo y matriz de trazabilidad', 'Rastrea un requisito de la necesidad a la prueba'),
    ('Modelos funcionales', 'C4',
     ['Procesos, contexto y casos de uso coherentes entre sí y con el catálogo, con flujos alternativos que descubren omisiones.',
      'Procesos, contexto y tres casos de uso con flujos alternativos, cada uno con su notación.',
      'Notaciones mezcladas o casos de uso sin flujos alternativos.',
      'Modelos ausentes o que no corresponden al caso.'],
     'Diagramas y plantillas comentados', 'Explica un flujo alternativo y su requisito'),
    ('Modelo de datos y diccionario', 'C5',
     ['Distingue obra, edición y ejemplar; restricciones que hacen cumplir las reglas; historial y datos derivados justificados; corrige una anomalía.',
      'Préstamo de ejemplar, restricciones de las reglas principales y diccionario con origen.',
      'Préstamo de obra, restricciones incompletas o borrado de historial.',
      'Sin modelo o con un modelo que no representa las reglas.'],
     'Modelo, diccionario y contraejemplos', 'Resuelve en el modelo la variante del docente'),
    ('Interacción y arquitectura', 'C6',
     ['Recorridos, bocetos y estados corregidos con evidencia; contratos completos; decisión técnica con condiciones y consecuencias.',
      'Tres recorridos con estados y mensajes; contratos de las operaciones principales; decisión registrada.',
      'Faltan estados o mensajes, o contratos sin errores.',
      'Sin bocetos ni arquitectura.'],
     'Bocetos, mapa, contratos y DT-01', 'Explica en qué capa cambia la variante'),
    ('Versiones, bitácora y trabajo del equipo', 'C7',
     ['Versiones citadas entre sí, bitácora al día con aportes de todos y correcciones del H3 incorporadas.',
      'Dossier versionado y bitácora con aportes.',
      'Versiones sin registro o bitácora irregular.',
      'Sin versiones ni bitácora.'],
     'Bitácora y versiones del dossier', 'Aporte propio registrado y observación del docente'),
]

ACT_E18 = [
    ('Ejercitá', [
        'Aplicá la lista de verificación del H3 al dossier de tu equipo y anotá, para cada punto que no se cumple, qué falta y '
        'quién lo completa.',
    ]),
    ('Resolvé', [
        'Después de la defensa, registrá en la bitácora las observaciones recibidas, las correcciones hechas y la versión nueva '
        'de cada documento que cambió.',
    ]),
]

# ------------------------------------------------------------------ práctica (complemento editorial)
PRACTICA_TITULO = 'Práctica 9 — Contrato de devolución y entorno para otra biblioteca (complemento editorial)'
PRACTICA_INTRO = [
    'Esta práctica no figura en el índice de Work: es un complemento editorial breve, para el Encuentro 17 o como actividad '
    'complementaria. No reemplaza ni desplaza el H3. Seguís con la Escuela Básica Mbokaja: un libro puede volver dañado (MS-1) '
    'y la norma M-N5 pide reponerlo. La computadora donada no tiene internet (M-F7) y nadie en la escuela sabe instalar '
    'programas (M-F9).',
]
NIVELES = [
    ('Nivel 1 — Guiado', [
        'Completá el contrato de la operación «registrar devolución» de Mbokaja:\n'
        'Entradas: ________. Precondiciones: ________. Resultado: ________.\n'
        'Errores: ________ (incluí el libro dañado). Requisitos: MR-__.',
        'Indicá en qué capa se decide que un libro dañado no se vuelva a prestar y en cuál se guarda que está dañado.',
    ]),
    ('Nivel 2 — Intermedio', [
        'Decidí qué pasa con el préstamo, con el ejemplar dañado y con el ejemplar que lo repone (M-N5). Ningún dato con '
        'historia se borra. Escribí el contrato de una operación nueva, «registrar reposición».',
        'Escribí el mensaje de confirmación de la devolución de un libro dañado, con la regla de 8.3.',
    ]),
    ('Nivel 3 — Ampliación', [
        'Escribí el registro de decisión técnica del entorno de Mbokaja con las condiciones excluyentes (M-F2, M-F3), las '
        'opciones y la decisión. Tené en cuenta M-F9 y M-F4: ¿quién va a mantener el sistema y los respaldos?',
        'Explicá qué consecuencia tiene tu decisión en el trabajo del encargado y qué tendría que verificar el profesor que '
        'viene una vez por mes.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: el contrato tiene sus cinco partes; cada error tiene un mensaje; el libro dañado no '
                    'se borra ni se presta; la reposición conserva el historial; la decisión técnica descarta primero lo que '
                    'no cumple las condiciones excluyentes y dice quién mantiene el entorno.')

REPASO = ('Para repasar', [
    'La presentación muestra, las reglas de negocio deciden y la persistencia guarda. Las reglas se comprueban siempre en el servidor.',
    'El contrato de una operación tiene entradas, precondiciones, resultado, errores y requisitos; cada error tiene su mensaje.',
    'Una decisión técnica se registra con su contexto, las condiciones excluyentes, las opciones, la decisión y las consecuencias.',
    'El entorno de referencia es un ejemplo provisional que hay que verificar en los equipos reales.',
    'La matriz de coherencia muestra si cada requisito tiene respuesta en datos, interfaz, operación y prueba.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, los Encuentros 17 y 18 no cambian: la arquitectura y el H3 se conservan.',
    'Si aun así falta tiempo en el Encuentro 17, no se omiten: el Ejemplo resuelto 9.1 (contrato de préstamo), la Tabla 9.5 '
    'y la Tabla 9.6. Pasan a lectura domiciliaria: el Ejemplo resuelto 9.2 y la Práctica 9.',
])

# ------------------------------------------------------------------ evaluación
EVAL_ID = 'ADS3-L3-C9'
EVAL_TITULO = 'Evaluación del Capítulo 9'
EVAL_TEXTO_BASE = ('Texto base — Préstamo de materiales del laboratorio de ciencias (situación de evaluación, ficticia)', [
    'U-1 El laboratorio de ciencias presta microscopios y kits de experimentos a los docentes.',
    'U-2 Un kit no se puede prestar si le falta alguna pieza.',
    'U-3 Solo la encargada del laboratorio registra los préstamos.',
    'U-4 El laboratorio no tiene internet, y el colegio no paga programas.',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', 'En el texto base, ¿qué capa decide que un kit incompleto no se presta (U-2)?',
     ['Las reglas de negocio.', 'La presentación.', 'La persistencia.', 'Ninguna: lo decide la docente.']),
    ('mc', '¿Qué parte del contrato de una operación es «solo la encargada puede registrar»?',
     ['Una precondición.', 'Una entrada.', 'Un resultado.', 'Un requisito de calidad del entorno.']),
    ('mc', '¿Qué se revisa primero en un registro de decisión técnica?',
     ['Las condiciones excluyentes.', 'La opción más popular.', 'El costo de cada opción.', 'Las preferencias del equipo.']),
    ('mc', 'En una matriz de coherencia, un requisito sin operación muestra…',
     ['algo que falta diseñar.', 'un requisito de calidad.', 'una prueba aprobada.', 'que el requisito es deseable.']),
    ('vf', 'Si el botón se oculta en la pantalla, no hace falta comprobar el permiso en el servidor.',
     False, 'Falso. Las reglas y los permisos se comprueban en el servidor, aunque alguien no use la pantalla.'),
    ('vf', 'El contrato dice qué errores puede devolver una operación.',
     True, 'Verdadero. Cada error tiene su mensaje en la pantalla.'),
    ('vf', 'Para decidir el entorno alcanza con elegir el lenguaje que más le guste al equipo.',
     False, 'Falso. Se descartan primero las opciones que no cumplen las condiciones excluyentes y se escriben las razones.'),
    ('ab', 'Escribí el contrato de la operación «prestar kit»: entradas, precondiciones, resultado, errores y fuentes (U-…).',
     'Entradas: código del kit, docente, cuenta. Precondición: la cuenta es de la encargada (U-3). Resultado: préstamo '
     'registrado y kit no disponible. Errores: kit incompleto (U-2), kit ya prestado, sin permiso (U-3). Un punto por '
     'entradas, uno por la precondición, uno por el resultado y uno por los errores con su fuente.', 4),
    ('ab', 'Escribí un registro de decisión técnica breve para el entorno del laboratorio, a partir de U-4.',
     'Contexto: sin internet ni presupuesto (U-4). Condiciones excluyentes: funcionar sin conexión y sin costo. Opciones: '
     'por ejemplo, aplicación local y planilla. Decisión con su razón y una consecuencia (instalación, respaldo o quién lo '
     'mantiene). Un punto por contexto, uno por las condiciones, uno por las opciones y uno por la decisión con su '
     'consecuencia. No se aceptan puntajes.', 4),
]
EVAL_PUNTAJE = ('Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno). '
                'Es opcional: el instrumento principal del cierre de la etapa es el H3.')
