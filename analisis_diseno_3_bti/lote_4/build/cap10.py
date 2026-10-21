# -*- coding: utf-8 -*-
"""Capítulo 10 — «Del diseño a la primera operación funcional» (Work §6: secciones 10.1 a 10.4 y práctica «demostrar
una operación y vincularla con su requisito y prueba»; encuentros 19 y 20).

Decisiones de Fernando (21-oct-2026): el capítulo se construye sin acta de campo, con la advertencia expresa de que el
entorno no se probó en la institución (decisión 1); la base de proyecto parte del Piloto B v2.3 adaptado al diseño
del lote 3 v1.1, en dos distribuciones (decisión 2); la primera operación es el alta mínima de un ejemplar físico
asociado a una obra y edición precargadas, documentada como operación auxiliar OA-01 relacionada con PT-08, con su
contrato y su prueba PA-01, sin atribuirla a ningún contrato existente (decisión 3); fragmentos breves y explicados,
leídos del proyecto (decisión 4). Capacidades de Work §5.2: C7 y C8 (Encuentro 19) y C6, C8 y C9 (Encuentro 20)."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'caso'))
import construccion as C
import mbokaja_u4 as MB
X = C.X

NUM = 10
UNIDAD = 'Unidad IV — Construir el prototipo por incrementos'
CAPITULO = 'Capítulo 10'
TITULO = 'Del diseño a la primera operación funcional'
ENCUENTROS = (19, 20)
SECCIONES = ['10.1 Preparación del entorno y estructura del proyecto',
             '10.2 Versiones, bitácora y conjunto inicial de datos ficticios',
             '10.3 Una operación completa: formulario, procesamiento y almacenamiento',
             '10.4 Validación, consulta parametrizada y evidencia de persistencia']
PRACTICA_WORK = 'demostrar una operación y vincularla con su requisito y prueba'

ROTULO_CAPACIDAD = ('Capacidades propuestas para el programa institucional (C7 y C8 en el Encuentro 19; C6, C8 y C9 '
                    'en el Encuentro 20; no son capacidades oficiales del MEC)')
CAPACIDAD = ('C6. Diseña la interacción y la arquitectura del prototipo.\n'
             'C7. Organiza y registra el trabajo colaborativo.\n'
             'C8. Integra un prototipo funcional con persistencia.\n'
             'C9. Verifica y mejora la solución a partir de evidencia.')
TEMA = ('Ficha de entorno y estructura de la base de proyecto por capas. Primera versión identificable, bitácora y datos '
        'ficticios iniciales. Una operación de punta a punta (alta de un ejemplar): formulario, procesamiento en el '
        'servidor y almacenamiento. Validación en el servidor, consulta parametrizada y evidencia de persistencia.')
INDICADORES = [
    'Completa la ficha de entorno de su equipo con lo que se comprobó y lo que queda pendiente, sin dar por probado lo que no se probó.',
    'Ubica cada archivo de la base en su capa y explica qué trae la base y qué construye el equipo.',
    'Registra la primera versión del prototipo en la bitácora, con los datos ficticios con que se instaló.',
    'Construye el alta de un ejemplar desde el formulario hasta la base, con validación en el servidor y consultas parametrizadas.',
    'Demuestra que el dato sigue después de cerrar y volver a abrir la base, y vincula la operación con su requisito, su contrato y su prueba.',
]
TIEMPO = ('Dos encuentros de 5 HC (19 y 20 de la secuencia anual). Encuentro 19: 3 HC de práctica y 2 de gestión del '
          'trabajo (versiones y bitácora). Encuentro 20: 1 HC de diseño, 3 de práctica y 1 de verificación.')

APERTURA = [
    'Hasta acá el equipo diseñó: requisitos, modelos, datos, pantallas, contratos. Desde este capítulo construye. No '
    'empieza de cero: recibe una base de proyecto que ya resuelve la configuración, la conexión con la base de datos, el '
    'ingreso del personal y la comprobación de permisos. Lo que construye el equipo son las operaciones, con sus reglas y '
    'sus pruebas.',
    'La primera operación es pequeña a propósito: dar de alta un ejemplar físico de una edición que ya está cargada. Es '
    'chica, pero recorre todo el sistema: una pantalla, una regla que se comprueba en el servidor y un dato que se guarda y '
    'sigue ahí al día siguiente.',
]
ARTICULACION = [
    'Con el Capítulo 9: la operación respeta las tres capas (Figura 9.1) y tiene un contrato con las mismas cinco partes '
    'que OP-01 a OP-06.',
    'Con Laboratorio de 2.º y 3.º: formularios, GET y POST, conexión a una base de datos y SQL ya se trabajaron allí. Este '
    'capítulo no repite esos temas: los usa para cumplir un requisito y comprobarlo.',
    'Con Laboratorio de 3.º (acuerdo de Work §3): antes del Encuentro 19, Laboratorio confirma el lenguaje, la conexión y '
    'el entorno. Si todavía no se llegó a esos puntos, la base de proyecto los trae resueltos para revisar.',
]

AVISO_ENTORNO = C.AVISO_ENTORNO

# ------------------------------------------------------------------ encuentro 19
E19_TITULO = 'Encuentro 19 — Entorno, estructura, versiones y datos'

S101 = ('10.1 Preparación del entorno y estructura del proyecto', [
    'El entorno es todo lo que el prototipo necesita para funcionar (Capítulo 9, Tabla 9.5). Antes de programar se '
    'comprueba que esté y que funcione en las computadoras donde se va a trabajar. Esa comprobación se anota en la ficha '
    'de entorno: qué se probó, cómo, con qué resultado y qué quedó pendiente. Tu docente completa antes la ficha completa '
    'con el responsable técnico; el equipo hace la versión breve de la Tabla 10.1 en su computadora.',
    'La base de proyecto se reparte en carpetas, y cada carpeta pertenece a una capa (Figura 10.1). En public/ están las '
    'páginas: la presentación. En src/reglas.php están las operaciones: las reglas de negocio. En src/db.php y '
    'src/esquema.sql están la conexión y las tablas con sus restricciones: la persistencia. En datos/ queda el archivo de '
    'la base, que no se copia ni se borra a mano.',
    'La base del estudiante trae preparado lo que no es parte de las actividades: la conexión, el esquema, el ingreso del '
    'personal, la comprobación de permisos por zona, los mensajes de la Tabla 8.6, la instalación, el respaldo y la '
    'restauración. Cada operación del sistema tiene su contrato escrito en src/reglas.php y responde «PENDIENTE» hasta que '
    'el equipo la construye, sin cambiar ningún dato.',
])
FICHA_ROTULO = 'Tabla 10.1 — Ficha de entorno del equipo (versión breve; la completa está en la guía docente)'
FICHA = (['Código', 'Qué se comprueba', 'Cómo', 'Qué anotás'],
         [[f[0], f[1], f[2], f[3]] for f in C.FICHA_ENTORNO if f[0] in C.FICHA_LIBRO])
LEAD_FIG101 = ('La Figura 10.1 muestra la estructura de carpetas de la base y la capa a la que pertenece cada parte. '
               'Usa los nombres de capa de la Figura 9.1.')
EPI_FIG101 = 'Figura 10.1 — Estructura de la base de proyecto y capa de cada carpeta.'
TABLA_102_ROTULO = 'Tabla 10.2 — Qué trae la base y qué construye tu equipo'
TABLA_102 = (['Parte', 'La trae la base', 'La construye el equipo', 'Capítulo'],
             [['Conexión, esquema y restricciones', 'Sí (src/db.php, src/esquema.sql)', 'La revisa y la explica', '10'],
              ['Ingreso y permisos por zona', 'Sí (src/auth.php: ME-12 y ME-13)', 'Lo prueba (P-11)', '10 y 11'],
              ['Alta de un ejemplar (OA-01)', 'El formulario y el contrato', 'La operación y su prueba', '10'],
              ['Obras, ediciones, lectores y baja lógica', 'Los contratos', 'Operaciones, formularios y pruebas', '11'],
              ['Préstamo y devolución', 'Los contratos', 'Operaciones, pantallas y pruebas', '12'],
              ['Consultas e informe', 'Los contratos', 'Operaciones, pantallas y pruebas', '13'],
              ['Instalación, respaldo y restauración', 'Sí', 'Los usa y anota el resultado (E-11, E-12)', '10']])
FICHA_RECUPERACION = ('Ficha de recuperación: lo que ya sabés de Laboratorio', [
    'Formulario: campos con nombre que el navegador envía al servidor. Con POST, los datos van en el pedido y no en la '
    'dirección. Repaso: Laboratorio de 1.º (formularios) y de 2.º (GET y POST).',
    'Conexión a una base de datos y sentencias SQL para insertar y consultar. Repaso: Laboratorio de 3.º.',
    'Lo nuevo de esta unidad no es la sintaxis: es que cada línea que se programa cumpla un requisito o un contrato y que '
    'una prueba lo demuestre.',
])
EJ101 = ('Ejemplo resuelto 10.1: instalar sin borrar nada', [
    'Consigna: instalar la base de ejemplo en una computadora donde un compañero ya había instalado y cargado datos.',
    'El equipo ejecuta php instalar.php. El instalador encuentra una base en datos/ y responde «Ya existe una base… No se '
    'modificó nada». Una instalación de prueba nunca borra una base existente.',
    'Si de verdad hay que empezar de cero, se usa php instalar.php --reiniciar con el servidor detenido: pide escribir '
    'REINICIAR y, antes de cambiar nada, guarda un respaldo verificado en datos/respaldos/.',
    'Las cuentas bibliotecaria1 y direccion1 son de demostración. Si no se elige una clave, el instalador genera una al '
    'azar y la muestra una sola vez. Esas claves se reemplazan antes de usar el sistema con datos que no sean ficticios.',
])

S102 = ('10.2 Versiones, bitácora y conjunto inicial de datos ficticios', [
    'El prototipo tiene versiones, como el catálogo de requisitos. La versión 0.1 es la base instalada, con la ficha de '
    'entorno completada. Cada incremento que funciona y pasa su prueba es una versión nueva: 0.2 con el alta de un '
    'ejemplar, 0.3 con el catálogo y los lectores, y así. La bitácora dice qué cambió, quién lo hizo y con qué prueba se '
    'comprobó (C7).',
    'Los datos iniciales son ficticios, como en toda la colección: ningún lector es una persona real y los nombres son '
    'descripciones («Estudiante A (ficticio)»). Están elegidos para que cada regla se pueda probar: hay un ejemplar '
    'inactivo (EJ-0459), un lector inactivo (LE-0125), una obra con dos ediciones (OB-0031) y lectores de los dos tipos '
    '(Tabla 10.3).',
])
TABLA_103_ROTULO = 'Tabla 10.3 — Datos ficticios iniciales de la base (src/datos_ejemplo.php)'
_ED = {e[0]: e for e in C.DATOS_INICIALES['ediciones']}
_OB = {o[0]: o for o in C.DATOS_INICIALES['obras']}
TABLA_103 = (['Ejemplar', 'Edición', 'Obra', 'Estado'],
             [[e[0], '%s (%s)' % (e[1], _ED[e[1]][2]), '%s %s' % (_ED[e[1]][1], _OB[_ED[e[1]][1]][1]),
               'activo' if e[2] == '1' else 'inactivo'] for e in C.DATOS_INICIALES['ejemplares']])
TABLA_104_ROTULO = 'Tabla 10.4 — Lectores ficticios iniciales'
TABLA_104 = (['Código', 'Descripción', 'Tipo', 'Curso', 'Estado'],
             [[l[0], l[1], l[2], '—' if l[3] == 'null' else l[3], 'activo' if l[4] == '1' else 'inactivo']
              for l in C.DATOS_INICIALES['lectores']])
BITACORA_ROTULO = 'Tabla 10.5 — Registro de la versión 0.1 en la bitácora (equipo modelo, ficticio)'
BITACORA = (['Campo', 'Contenido'],
            [['Versión', '0.1 del prototipo (base del estudiante instalada)'],
             ['Fecha y encuentro', 'Encuentro 19'],
             ['Qué se hizo', 'Instalación con php instalar.php; cuentas de demostración con claves nuevas anotadas por la docente'],
             ['Comprobaciones', 'E-5: entorno correcto. E-6b: 15 de 15 correctas. E-11: respaldo creado'],
             ['Pendiente', 'E-1, E-7 y E-12 en la computadora del laboratorio: no se pudieron hacer en este encuentro'],
             ['Responsables', 'Integrantes 1 y 2 (instalación); integrante 3 (ficha); integrante 4 (bitácora)']])
EJ102 = ('Ejemplo resuelto 10.2: lo que se anota y lo que no se anota', [
    'Consigna: decidir qué va a la bitácora del Encuentro 19 cuando E-7 (cuenta sin permisos de administrador) no se pudo '
    'probar porque la sala tenía una sola cuenta.',
    'Se anota «E-7 pendiente: la sala no tiene cuenta de estudiante; se prueba el día que el responsable técnico la '
    'cree». No se anota «funciona» ni se deja la fila vacía.',
    'Razón: una ficha de entorno sirve si dice la verdad. Un resultado que no se obtuvo no se inventa; lo que falta '
    'comprobar queda a la vista, con quién y cuándo lo comprueba.',
])

ACT_E19 = [
    ('Ejercitá', [
        'Ubicá cada archivo en su capa: public/lectores.php, src/reglas.php, src/esquema.sql, src/db.php, '
        'public/_plantilla.php, datos/biblioteca.sqlite.',
    ]),
    ('Resolvé', [
        'Completá la Tabla 10.1 en la computadora de tu equipo. En cada fila, escribí el resultado o «pendiente» con el '
        'motivo.',
        'Registrá la versión 0.1 de tu prototipo en la bitácora, con el formato de la Tabla 10.5.',
    ]),
    ('Pensá y decidí', [
        'Un compañero propone borrar a mano datos/biblioteca.sqlite para «empezar limpio». Explicá qué riesgo tiene y qué '
        'se hace en su lugar.',
    ]),
]

# ------------------------------------------------------------------ encuentro 20
E20_TITULO = 'Encuentro 20 — Una operación de punta a punta'

S103 = ('10.3 Una operación completa: formulario, procesamiento y almacenamiento', [
    'La bibliotecaria recibe un libro nuevo de una obra que ya está en el catálogo y le pega la etiqueta EJ-0800. Para '
    'que se pueda prestar, hay que darlo de alta: registrar el ejemplar físico en su edición. Esa es la operación OA-01. '
    'No figura en las Tablas 9.3 y 9.4, que tienen las seis operaciones del núcleo: es una operación auxiliar de la '
    'pantalla PT-08, que la Unidad IV agrega con su propio contrato y su propia prueba (PA-01).',
    'Una operación recorre las tres capas (Figura 10.2). La presentación muestra el formulario y envía el pedido (Código '
    '10.1). La página recibe el pedido, comprueba la zona y la ficha del formulario, llama a la operación y guarda el '
    'resultado para mostrarlo (Código 10.2). La operación decide (Códigos 10.3 y 10.4): comprueba el permiso, limpia y '
    'valida las entradas, busca la edición y guarda el ejemplar. La persistencia guarda el dato y protege que el código '
    'no se repita.',
    'Cada fragmento de código de este libro está leído del proyecto, no copiado a mano, y lleva su ficha: el archivo, el '
    'propósito, el requisito o contrato que cumple, las entradas, el resultado y la prueba que lo comprueba.',
])
LEAD_FIG102 = ('La Figura 10.2 sigue el pedido del alta de EJ-0800 por las tres capas, con la notación de la Tabla 9.1. '
               'El mensaje que ve la bibliotecaria vuelve por el mismo camino.')
EPI_FIG102 = 'Figura 10.2 — Recorrido del alta de un ejemplar (OA-01) por las tres capas.'
CODIGOS_E20 = ['Código 10.1', 'Código 10.2', 'Código 10.3', 'Código 10.4']
EXPLICA = {
    'Código 10.1': 'El formulario no decide nada: solo pide los dos códigos. formulario_inicio() agrega la ficha CSRF '
                   'que identifica el formulario y desactiva el botón mientras se guarda (ME-11).',
    'Código 10.2': 'La página es la parte de la presentación que habla con el servidor: si la ficha del formulario no '
                   'corresponde, no llama a la operación (MV-12); si corresponde, llama a alta_ejemplar() y, después, '
                   'redirige, para que recargar la página no vuelva a enviar el pedido.',
    'Código 10.3': 'Lo primero es el permiso (ME-13): sin él, no se hace nada más. Después se limpian las entradas y se '
                   'valida el formato del código. Cada error devuelve su mensaje y sale sin tocar la base.',
    'Código 10.4': 'La edición se busca y el ejemplar se guarda con consultas parametrizadas: los signos «?» reciben los '
                   'datos por separado. Si la base rechaza el código porque ya existe, la operación responde MA-02.',
}
EJ103 = ('Ejemplo resuelto 10.3: el alta de EJ-0800, paso a paso', [
    'Consigna: seguir el pedido de la bibliotecaria (código EJ-0800, edición ED-0060) y escribir qué responde el sistema '
    'en cada caso de PA-01.',
    'Con la cuenta bibliotecaria1: «%s» El ejemplar queda activo y la consulta pública de «El arroyo y la escuela» pasa '
    'a contar un disponible más.' % C.con_datos('MA-01', 'EJ-0800', 'ED-0060'),
    'El mismo código otra vez: «%s» No se guarda nada.' % C.con_datos('MA-02', 'EJ-0800'),
    'La etiqueta escrita EJ800: «%s»' % C.con_datos('MV-02', 'EJ800', 'EJ- y cuatro cifras'),
    'Una edición que no existe, ED-0999: «%s»' % C.con_datos('MA-03', 'ED-0999'),
    'Con la cuenta direccion1: «%s» La dirección consulta, pero no da de alta ejemplares.' % C.MENSAJES_PHP['ME-13'],
])

S104 = ('10.4 Validación, consulta parametrizada y evidencia de persistencia', [
    'La validación del navegador ayuda, pero no protege: cualquiera puede enviar un pedido sin usar la pantalla. Por eso '
    'cada entrada se valida otra vez en el servidor, en la operación, antes de tocar la base (Work §7.5). Una validación '
    'tiene su mensaje (MV-01 a MV-12) y no deja datos a medias.',
    'Una consulta parametrizada separa la sentencia de los datos. Si alguien escribe en el campo de la edición un texto '
    'con comillas, como ED-0060\' OR \'1\'=\'1, la base lo recibe como un código que no existe y la operación responde '
    'MA-03. El texto nunca se mezcla con la sentencia, así que no puede cambiarla.',
    'La persistencia se demuestra, no se supone: se da de alta el ejemplar, se cierra la conexión, se abre otra (como al '
    'reiniciar el sistema) y se busca el dato. El Código 10.5 hace eso en la prueba PA-01. La Tabla 10.6 muestra el '
    'resultado de esa prueba y dónde corrió.',
])
CODIGOS_S104 = ['Código 10.5']
EXPLICA['Código 10.5'] = ('La prueba abre la base con una conexión nueva, que no sabe nada de la anterior. Si el '
                          'ejemplar está, se guardó en el archivo y no solo en la memoria del programa.')
TABLA_106_ROTULO = 'Tabla 10.6 — PA-01: resultado de la prueba en el entorno de construcción'
EJ104 = ('Ejemplo resuelto 10.4: demostrar una operación y vincularla con su requisito y prueba', [
    'Consigna: preparar la demostración de OA-01 para otro equipo (es la práctica que pide Work para este capítulo).',
    'Requisito: RF-07 (el catálogo distingue el ejemplar físico) y RF-10 (los ejemplares tienen estado). Contrato: OA-01, '
    'con sus cinco partes. Prueba: PA-01, con cinco casos.',
    'Demostración: dar de alta EJ-0801 en ED-0070, intentar EJ-0801 otra vez (MA-02), detener el servidor, volver a '
    'iniciarlo y buscar «Atlas» en la consulta pública: el atlas pasa de 1 a 2 ejemplares.',
    'Registro: en la bitácora, versión 0.2, con el resultado de PA-01 y el entorno en que se ejecutó.',
])

ACT_E20 = [
    ('Ejercitá', [
        'En el Código 10.3, señalá la línea que cumple la precondición del contrato OA-01 y la que cumple el error MV-02.',
    ]),
    ('Resolvé', [
        'Construí alta_ejemplar() en la base de tu equipo siguiendo los cinco pasos del comentario de src/reglas.php. '
        'Ejecutá php pruebas/prueba_mis_operaciones.php y anotá cuántos casos de PA-01 quedan correctos.',
        'Hacé la demostración del Ejemplo resuelto 10.4 con un código distinto y registrá la versión 0.2.',
    ]),
    ('Pensá y decidí', [
        'Un compañero dice: «el campo ya tiene placeholder EJ-0000, nadie va a escribir mal el código». Explicá por qué la '
        'validación tiene que estar igual en el servidor.',
    ]),
    ('Desafío', [
        'Escribí un caso más para PA-01 con una entrada que todavía no se prueba y decidí qué mensaje debería responder.',
    ]),
]

# ------------------------------------------------------------------ práctica
PRACTICA_TITULO = 'Práctica 10 — Demostrar una operación en la computadora de Mbokaja'
PRACTICA_INTRO = [
    'Seguís con la Escuela Básica Mbokaja, que ya tiene la computadora donada sin internet (M-F7). El profesor del colegio '
    'vecino dejó instalado un sistema de prueba con una copia de la base del curso (M-F10). En la escuela nadie sabe '
    'instalar programas (M-F9), y los libros tienen etiquetas propias (M-F11).',
    'Los niveles 1 y 2 se hacen en una copia de práctica de la base de tu equipo, instalada en otra carpeta: el sistema '
    'de prueba de Mbokaja es una copia como esa. El nivel 3 se resuelve en papel.',
]
NIVELES = [
    ('Nivel 1 — Guiado', [
        'Demostrá el alta de un ejemplar en la copia de la base: EJ-0900 en la edición ED-0070. Cerrá y volvé a abrir el '
        'sistema, y mostrá que sigue.',
        'Completá la ficha de la demostración:\n'
        'Operación: ________. Requisito de Arapoty: RF-__. Necesidad de Mbokaja que atiende: MR-__.\n'
        'Contrato: ________. Prueba: PA-__. Resultado obtenido: ________.',
    ]),
    ('Nivel 2 — Intermedio', [
        'El alta no valida el formato del código de la edición: «ED60» llega hasta la consulta y responde MA-03. Agregá en '
        'la operación la validación que falta (MV-02, «ED- y cuatro cifras») y mostrá el rechazo antes de tocar la base.',
        'Agregá un caso a PA-01 para esa validación y escribí el resultado esperado y el obtenido.',
    ]),
    ('Nivel 3 — Ampliación', [
        'Las etiquetas de Mbokaja son MB- y tres cifras (M-F11), y el sistema de prueba espera EJ- y cuatro. Decidí si se '
        'cambian las etiquetas o el sistema, y qué partes cambiarían en cada caso (validación, restricción de la base, '
        'pruebas).',
        'Escribí la ficha de entorno de Mbokaja (E-1, E-2, E-5, E-10, E-11 y E-12): qué se comprueba, quién lo hace (M-F9) '
        'y cada cuánto se respalda, teniendo en cuenta que el profesor vecino viene una vez por mes.',
    ]),
]
PRACTICA_CONTROL = ('Punto de control: la demostración muestra el dato después de reiniciar; la ficha vincula operación, '
                    'requisito, contrato y prueba; la validación nueva rechaza en el servidor y sin cambiar datos; la ficha '
                    'de entorno dice qué se comprobó y qué queda pendiente, sin inventar resultados.')

REPASO = ('Para repasar', [
    'La base de proyecto resuelve la configuración y la conexión; el equipo construye las operaciones, con sus reglas y sus pruebas.',
    'La ficha de entorno registra lo que se comprobó y lo que queda pendiente. Lo que no se probó no se da por probado.',
    'Una operación recorre las tres capas: el formulario pide, la operación decide y la base guarda.',
    'Cada entrada se valida en el servidor, y las consultas son parametrizadas.',
    'La persistencia se demuestra: el dato sigue al abrir la base con otra conexión.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, los Encuentros 19 y 20 se reúnen en el Encuentro 15: «El docente entrega el '
    'entorno, la conexión y el inicio de sesión listos (base explicada, Work §7.5); el equipo hace la primera operación.»',
    'No se omiten: la Tabla 10.1 (al menos E-5 y E-6b), el alta de un ejemplar con PA-01 y la evidencia de persistencia. '
    'Pasan a lectura domiciliaria: el Ejemplo resuelto 10.2 y el nivel 3 de la Práctica 10.',
])

# ------------------------------------------------------------------ evaluación
EVAL_ID = 'ADS3-L4-C10'
EVAL_TITULO = 'Evaluación del Capítulo 10'
EVAL_TEXTO_BASE = ('Texto base — Depósito de materiales de Educación Física (situación de evaluación, ficticia)', [
    'EF-1 El depósito presta pelotas, redes y conos a los docentes de Educación Física.',
    'EF-2 Cada material tiene una etiqueta con DEP- y tres cifras.',
    'EF-3 Solo el encargado del depósito da de alta los materiales nuevos.',
    'EF-4 La computadora del depósito no tiene internet.',
])
EVAL_FUENTES = {l.split(' ', 1)[0]: l.split(' ', 1)[1] for l in EVAL_TEXTO_BASE[1]}
EVAL_ITEMS = [
    ('mc', 'En un sistema para el depósito, ¿en qué capa se comprueba que la etiqueta tenga DEP- y tres cifras (EF-2)?',
     ['En las reglas de negocio, en el servidor.', 'Solo en el formulario del navegador.', 'En la carpeta de datos.',
      'En la bitácora del equipo.']),
    ('mc', '¿Qué demuestra la evidencia de persistencia?',
     ['Que el dato sigue al abrir la base con otra conexión.', 'Que el formulario se ve bien.',
      'Que la operación es rápida.', 'Que el código no tiene errores de escritura.']),
    ('mc', 'Para empezar de cero en una computadora que ya tiene una base instalada, ¿qué se hace?',
     ['Reiniciar con el instalador, que pide confirmación y guarda antes un respaldo verificado.',
      'Borrar a mano el archivo de la base.', 'Instalar encima: el instalador la reemplaza sin avisar.',
      'Copiar otra base con el servidor encendido.']),
    ('mc', 'Una consulta parametrizada sirve para…',
     ['que lo que escribe la persona no pueda cambiar la sentencia.', 'que la consulta tarde menos.',
      'no tener que validar las entradas.', 'mostrar los mensajes de error.']),
    ('vf', 'Si un paso de la ficha de entorno no se pudo comprobar, se anota como pendiente con el motivo.',
     True, 'Verdadero. Un resultado que no se obtuvo no se inventa.'),
    ('vf', 'La base de proyecto trae resueltas todas las operaciones del sistema.',
     False, 'Falso. Trae la conexión, el ingreso y los permisos; las operaciones las construye el equipo.'),
    ('vf', 'Si el encargado del depósito no inició sesión, el alta de un material tiene que responder un error de permiso '
           'sin guardar nada.',
     True, 'Verdadero. El permiso se comprueba primero, en el servidor (EF-3).'),
    ('ab', 'Escribí el contrato de la operación «dar de alta un material» del depósito: entradas, precondición, resultado, '
           'errores y fuentes (EF-…).',
     'Entradas: etiqueta, tipo de material, cuenta. Precondición: la cuenta es del encargado (EF-3). Resultado: material '
     'nuevo, activo. Errores: falta un dato, etiqueta con otro formato (EF-2), etiqueta repetida, sin permiso. Un punto '
     'por entradas, uno por la precondición, uno por el resultado y uno por los errores con su fuente.', 4),
    ('ab', 'Describí cómo demostrarías que el alta de un material funciona y que el dato persiste, y qué anotarías en la '
           'bitácora.',
     'Alta de un material con datos ficticios; rechazo de una etiqueta repetida o mal escrita; cerrar el sistema y '
     'volver a abrirlo (o abrir otra conexión) y encontrar el material; bitácora con versión, prueba, resultado obtenido '
     'y entorno. Un punto por cada parte.', 4),
]
EVAL_PUNTAJE = 'Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítems 8 y 9: 4 puntos cada uno).'
