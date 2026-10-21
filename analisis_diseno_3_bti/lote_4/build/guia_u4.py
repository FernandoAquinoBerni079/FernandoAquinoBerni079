# -*- coding: utf-8 -*-
"""Guía docente con solucionario del lote 4 (Unidad IV, Capítulos 10 a 13): coordinación con Laboratorio y ficha de
entorno completa (E-1 a E-12, con E-6a y E-6b), protocolo de campo y de concurrencia para Windows, evidencias
equivalentes para otro entorno, las dos distribuciones de la base con su tamaño, secuencia de cada encuentro en HC,
claves de las actividades, prácticas y evaluaciones, listas de cotejo, fragmentos de referencia que el libro no
publica, rúbrica del H4 con evidencias, planilla y banco de variantes, calendario de 28 encuentros, resultados de las
pruebas con su entorno y procedencia de los recursos.
Los datos del caso se leen de caso/construccion.py, caso/mbokaja_u4.py y del proyecto; no se copian."""
import os, filecmp
import oficio as O
H, M, K = O.H, O.M, O.K
import piezas_u4 as Z
import fragmentos as F
import cap10, cap11, cap12, cap13
C, X = Z.C, Z.X
MB = cap10.MB

ANCHO_SEC = [3.2, 2.4, 11.0]

# ---------------------------------------------------------------- antes del Encuentro 19
LABORATORIO = [
    'Antes del Encuentro 19, el docente de Laboratorio confirma el lenguaje, la conexión a la base de datos y el entorno '
    '(acuerdo operativo de Work §3). Si la secuencia de Laboratorio todavía no llegó a esos puntos, se entrega la base del '
    'estudiante explicada: el curso la revisa y la completa, no la escribe desde cero.',
    'Laboratorio trabaja el funcionamiento técnico; este optativo, la justificación y la trazabilidad (Work §3). Por eso el '
    'libro no tiene una unidad de sintaxis PHP ni un manual de SQL: cada fragmento de código está para mostrar qué requisito '
    'o contrato cumple y qué prueba lo demuestra. La evaluación no valora la sintaxis.',
    'Si el diagnóstico muestra que el curso no domina formularios ni programación elemental, Work §7.5 pide apoyo de '
    'Laboratorio y simplificar el alcance: usar la adaptación de 28 encuentros (sección 6) aunque el calendario tenga 36. No '
    'se promete resolver esa brecha con una ficha breve.',
]
ESTADO_CAMPO = [
    'Estado: las pruebas de la base corrieron solo en el entorno de construcción de este material (sección 7). No se probaron '
    'en ninguna computadora escolar ni en Windows. No hay acta de campo. El libro lo dice en cada capítulo.',
    'Antes de usar la base como solución comprobada en un laboratorio escolar, el docente o el responsable técnico hace la '
    'prueba de campo: versión de Windows, cuenta sin permisos de administrador, funcionamiento sin internet, instalación, '
    'persistencia, respaldo y restauración. Lo hace con la ficha de esta sección, en las computadoras donde se va a trabajar.',
    'No se inventan resultados: lo que no se pudo probar se anota como pendiente, con el mensaje exacto si hubo error. Un acta '
    'de campo vale para los equipos probados, no para todos los colegios.',
]
DIFERENCIAS_WINDOWS = (['Diferencia conocida', 'Qué hacer y qué anotar'],
                       [['En el PHP portátil oficial para Windows, pdo_sqlite viene desactivado en el php.ini de ejemplo',
                         'Activar extension=pdo_sqlite (y sqlite3) en php.ini; E-5 lo detecta. Anotar la versión del zip.'],
                        ['El servidor incorporado (php -S) atiende los pedidos de a uno en Windows',
                         'No sirve para probar simultaneidad: usar el protocolo de concurrencia (sección 0.4).'],
                        ['Windows no deja borrar ni reemplazar archivos abiertos',
                         'Detener el servidor antes de reiniciar o restaurar; anotar si respaldar.php y restaurar.php funcionaron.'],
                        ['No existe posix_kill: retirar_marca.php no puede comprobar si el proceso sigue vivo',
                         'La persona comprueba que no quede ningún php.exe abierto antes de retirar una marca de mantenimiento.'],
                        ['Base en un pendrive o una carpeta de red',
                         'No se usa así (E-10): disco local. Retirar el pendrive con el servidor abierto puede dañar la base.']])
ALTERNATIVO = [
    'HTML y CSS, PHP y SQLite son la referencia editorial provisional. La institución puede usar otro entorno que ya domine '
    'en Laboratorio si produce evidencias equivalentes (Work §7.5): las mismas reglas, los mismos contratos y las mismas '
    'pruebas, con los entregables de la tabla siguiente. Los fragmentos de código del libro quedan entonces como ejemplo.',
    'Si ningún entorno funciona en los equipos, se trabaja con una sola computadora preparada por el docente para las '
    'demostraciones y las pruebas, y se reduce el alcance con la adaptación de 28 encuentros. Se registra como limitación.',
    'En los dos casos se anota en la ficha de entorno el camino elegido y su resultado. Ningún camino se declara probado si '
    'no se probó.',
]
PROTOCOLO_REGISTRO = (['Dato', 'Ronda 1', 'Ronda 2', 'Ronda 3'],
                      [['Versión de Windows (edición, versión, 32/64 bits)', '', '', ''],
                       ['Versión de PHP y de SQLite (php verificar_entorno.php)', '', '', ''],
                       ['Ubicación de la base (disco local)', '', '', ''],
                       ['Comando ejecutado (php pruebas/prueba_carrera.php)', '', '', ''],
                       ['Línea «Resultado» y mensajes recibidos', '', '', ''],
                       ['Consulta de control: ejemplares con más de un préstamo activo', '', '', ''],
                       ['Estado (correcto, falla o pendiente con el mensaje exacto)', '', '', '']])

DESCRIPCION = {
    'LEEME.txt': 'Instrucciones de instalación, uso y pruebas',
    'instalar.php': 'Crea la base; nunca borra una existente sin confirmación y respaldo verificado',
    'respaldar.php': 'Respaldo consistente y verificado',
    'restaurar.php': 'Restaura un respaldo verificado, con confirmación y copia previa',
    'retirar_marca.php': 'Retiro seguro de una marca de mantenimiento huérfana',
    'verificar_entorno.php': 'Comprueba versión de PHP, extensiones y escritura (E-5)',
    'src/db.php': 'Conexión, esquema y utilidades de la base',
    'src/esquema.sql': 'Tablas, restricciones, índice único de RI-01 y protección del historial',
    'src/auth.php': 'Sesión, ingreso (ME-12), zonas y permisos (ME-13), ficha CSRF',
    'src/mensajes.php': 'Textos de ME-01 a ME-13, MA y MV',
    'src/reglas.php': 'Operaciones del sistema y auxiliares',
    'src/datos_ejemplo.php': 'Datos ficticios iniciales y cuentas de demostración',
    'src/mantenimiento.php': 'Modo mantenimiento con bloqueo exclusivo',
    'src/respaldo.php': 'Funciones de respaldo verificado',
    'public/_plantilla.php': 'Cabecera, menú por rol, avisos, «Guardando…» y redirección',
    'public/index.php': 'PT-01 y PT-02, consulta pública',
    'public/login.php': 'PT-03, ingreso del personal',
    'public/inicio.php': 'PT-04, inicio de la bibliotecaria',
    'public/salir.php': 'Cierre de sesión',
    'public/lectores.php': 'PT-08, lectores y ejemplares',
    'public/prestamo.php': 'PT-05, registrar préstamo',
    'public/devolucion.php': 'PT-06, registrar devolución',
    'public/activos.php': 'PT-07, préstamos activos y vencidos',
    'public/informe.php': 'PT-09, informe mensual por curso',
    'pruebas/_comun.php': 'Utilidades de las pruebas',
    'pruebas/prueba_contratos.php': 'Contratos OP-01 a OP-06 y OA-01 a OA-05, con persistencia',
    'pruebas/prueba_mis_operaciones.php': 'Operaciones del equipo; PENDIENTE no cuenta como falla',
    'pruebas/prueba_carrera.php': 'Pedidos simultáneos con procesos independientes (P-07, RI-02)',
    'pruebas/_trabajador.php': 'Proceso de la prueba de carrera',
    'pruebas/prueba_garantias.php': 'Restricciones y protección del historial en la base',
    'pruebas/prueba_respaldo.php': 'Respaldo y restauración',
    'pruebas/prueba_mantenimiento.php': 'Modo mantenimiento',
    'pruebas/prueba_marca_huerfana.php': 'Retiro de una marca huérfana',
    'pruebas/_corte.php': 'Proceso que se corta a propósito',
    'pruebas/prueba_http.sh': 'Recorrido E-6a por HTTP (referencia docente)',
    'pruebas/prueba_base.sh': 'Comprobación E-6b de la base del estudiante',
}


def tabla_archivos():
    ref, base = os.path.join(C.PROY, 'referencia_docente'), os.path.join(C.PROY, 'base_estudiante')
    todos = sorted(set(_archivos(ref)) | set(_archivos(base)), key=lambda a: (a.count('/'), a))
    filas = []
    for a in todos:
        en_r, en_b = os.path.exists(os.path.join(ref, a)), os.path.exists(os.path.join(base, a))
        if en_r and en_b:
            estado = 'Igual' if filecmp.cmp(os.path.join(ref, a), os.path.join(base, a), shallow=False) else 'Sin operaciones resueltas'
        else:
            estado = 'Solo en la referencia' if en_r else 'Solo en la base'
        filas.append([a, DESCRIPCION.get(a, ''), estado])
    return (['Archivo', 'Qué hace', 'Base del estudiante'], filas)


def _archivos(raiz):
    out = []
    for d, _, fs in os.walk(raiz):
        for f in fs:
            rel = os.path.relpath(os.path.join(d, f), raiz)
            if not rel.startswith('datos'):
                out.append(rel)
    return out


def tabla_lineas():
    c = C.conteo_lineas()
    filas = [[f, str(a), str(b)] for f, a, b in c['arranque']]
    ta, tb = sum(x[1] for x in c['arranque']), sum(x[2] for x in c['arranque'])
    filas.append(['Total de arranque', str(ta), str(tb)])
    filas += [[f, str(a), str(b)] for f, a, b in c['herramientas']]
    ha, hb = sum(x[1] for x in c['herramientas']), sum(x[2] for x in c['herramientas'])
    filas.append(['Total de herramientas de seguridad y respaldo', str(ha), str(hb)])
    return (['Archivo PHP propio', 'Líneas', 'Líneas de código'], filas), (ta, tb, ha, hb)


def texto_lineas():
    _, (ta, tb, ha, hb) = tabla_lineas()
    return [
        'Fernando pidió que la base quede por debajo de unas 400 líneas de PHP propio de arranque, sin contar datos, pruebas '
        'ni plantillas de texto, y sin quitar validaciones ni medidas de seguridad para cumplir la cifra. Se cuentan las '
        'líneas de cada archivo y, aparte, las líneas de código (sin líneas vacías ni comentarios).',
        'Arranque (conexión, sesión y permisos, operaciones pendientes con sus contratos, páginas e instalador): %d líneas de '
        'código, por debajo de 400. Con comentarios y líneas vacías son %d: los comentarios son los contratos de cada '
        'operación y los pasos que el equipo completa, que forman parte de la explicación de la base.' % (tb, ta),
        'Herramientas heredadas del Piloto B v2.3 (mantenimiento, respaldo, restauración, retiro de marcas y verificación '
        'del entorno): %d líneas, %d de código. Exceden la cifra si se las suma, y no se recortaron: son las garantías de '
        'que una instalación no borra una base, de que un respaldo es consistente y de que una restauración no destruye '
        'datos sin aviso y copia verificada. Los estudiantes las usan, pero no las leen ni las modifican.' % (ha, hb),
        'No se cuentan: src/mensajes.php (textos), src/datos_ejemplo.php (datos), src/esquema.sql (esquema) y pruebas/.',
    ]


def tabla_resultados():
    r = C.resultados_pruebas()
    e = r['entorno']
    filas = []
    for dist, nombre in (('referencia_docente', 'Referencia docente'), ('base_estudiante', 'Base del estudiante')):
        for prueba, v in r[dist].items():
            filas.append([nombre, prueba, v['resultado'].replace('Resultado: ', '') +
                          (' (%d pendientes)' % v['pendientes'] if v['pendientes'] else '')])
    ej = r['reproduccion_ejemplo_capitulo_10']
    filas.append(['Ejemplo del Capítulo 10', 'OA-01 pegada en una copia de la base', ej['resultado'].replace('Resultado: ', '')])
    entorno = '%s; PHP %s; SQLite %s; %s; %s' % (e['sistema'], e['php'], e['sqlite'], e['fecha'], e['tipo'])
    return (['Distribución', 'Prueba', 'Resultado'], filas), entorno


# ---------------------------------------------------------------- capítulo 10
SEC_C10 = [
    ('Encuentro 19 — Entorno, estructura, versiones y datos (5 HC: 3 de práctica y 2 de gestión)', [
        ['Práctica', 'aprox. 3 HC', 'Apertura del capítulo y aviso de entorno. Sección 10.1: instalación de la base del estudiante (php verificar_entorno.php, php instalar.php), Tabla 10.1 en cada equipo (E-5, E-6b con bash pruebas/prueba_base.sh, E-10, E-11), Figura 10.1 y Tabla 10.2. Ejemplo resuelto 10.1. Actividades 1 y 2.'],
        ['Gestión del trabajo', 'aprox. 2 HC', 'Sección 10.2: versión 0.1, bitácora (Tabla 10.5) y datos ficticios (Tablas 10.3 y 10.4). Ejemplo resuelto 10.2. Actividades 3 y 4. Evidencia (Work, encuentro 19): ejecución inicial reproducible y ficha de entorno.'],
    ]),
    ('Encuentro 20 — Una operación de punta a punta (5 HC: 1 de diseño, 3 de práctica y 1 de verificación)', [
        ['Diseño', 'aprox. 1 HC', 'Sección 10.3: el boceto de PT-08, el contrato OA-01 y la Figura 10.2. Lectura de los Códigos 10.1 y 10.2. Actividad 1.'],
        ['Práctica', 'aprox. 3 HC', 'Códigos 10.3 y 10.4 y Ejemplo resuelto 10.3. Cada equipo construye alta_ejemplar() en su base (Actividad 2). Sección 10.4: validación en el servidor y consulta parametrizada.'],
        ['Verificación', 'aprox. 1 HC', 'PA-01 con php pruebas/prueba_mis_operaciones.php, Código 10.5 y Tabla 10.6. Demostración del Ejemplo resuelto 10.4 y versión 0.2 (Actividad 3). Evidencia (Work, encuentro 20): formulario-servidor-base de datos y prueba de persistencia. Práctica 10 en el nivel que indique el docente.'],
    ]),
]
CLAVES_E19 = [
    ['1', 'public/lectores.php y public/_plantilla.php: presentación. src/reglas.php: reglas de negocio. src/esquema.sql y src/db.php: persistencia. datos/biblioteca.sqlite: el archivo de la base (persistencia), que no se edita a mano.', 'Poner reglas.php en la presentación porque lo llama una página.'],
    ['2', 'Respuesta abierta. Cada fila con el resultado obtenido o «pendiente» y el motivo. En una instalación correcta, E-5 informa el entorno correcto y E-6b da 15 de 15 correctas.', 'Escribir «funciona» sin haber ejecutado la comprobación, o dejar filas vacías.'],
    ['3', 'Registro con versión 0.1, fecha, qué se hizo, comprobaciones con su resultado, pendientes y responsables, como la Tabla 10.5.', 'Registro sin pendientes ni responsables.'],
    ['4', 'Se pierden los datos sin respaldo y, si el servidor está abierto, el archivo puede quedar dañado. En su lugar: php instalar.php --reiniciar con el servidor detenido (pide REINICIAR y guarda antes un respaldo verificado) o restaurar un respaldo con php restaurar.php.', 'Decir que no importa porque son datos de prueba.'],
]
CLAVES_E20 = [
    ['1', 'Precondición: la línea if ($r = sin_permiso($cuenta, array(\'bibliotecaria\'))), que devuelve ME-13. MV-02: la comprobación con preg_match del formato EJ- y cuatro cifras y su return.', 'Señalar la línea de MV-01 como la del formato.'],
    ['2', 'Los cinco casos de PA-01 dan CORRECTO; las demás operaciones siguen PENDIENTE. La prueba compara el mensaje y además que la base no cambió en los rechazos.', 'Dar por buena la operación porque «se ve el mensaje», sin correr la prueba.'],
    ['3', 'Demostración con un código distinto, rechazo del repetido, reinicio y consulta pública; versión 0.2 con el resultado de PA-01 y el entorno en que se ejecutó.', 'Demostrar sin reiniciar.'],
    ['4', 'Cualquiera puede enviar el pedido sin usar la pantalla, y el placeholder no valida nada: solo sugiere. La validación del servidor es la que protege los datos (Work §7.5).', 'Confiar en el navegador.'],
    ['5', 'Respuesta abierta. Ejemplos: un código con espacios o en minúsculas («ej-0802 ») se limpia y se acepta (MA-01); el código vacío responde MV-01; una edición con formato inválido hoy llega a la consulta y responde MA-03 (es la validación que falta, Práctica 10, nivel 2).', 'Un caso sin resultado esperado.'],
]
CLAVES_P10 = [
    ['Nivel 1', 'Alta de EJ-0900 en ED-0070: «%s» Después de reiniciar, la consulta de «Atlas» cuenta un ejemplar más. Ficha: OA-01; RF-07 (y RF-10); Mbokaja MR-05 (saber qué libros hay disponibles); contrato OA-01; prueba PA-01; resultado obtenido anotado.' % C.con_datos('MA-01', 'EJ-0900', 'ED-0070')],
    ['Nivel 2', 'Después de limpiar las entradas, una comprobación más: si el código de la edición no tiene ED- y cuatro cifras, resultado(false, \'MV-02\', $codigo_edicion, \'ED- y cuatro cifras\'). Con «ED60» responde «%s» y la base no cambia. Caso nuevo de PA-01 con esperado MV-02 y sin cambios.' % C.con_datos('MV-02', 'ED60', 'ED- y cuatro cifras')],
    ['Nivel 3', 'Cambiar las etiquetas obliga a reetiquetar todos los libros con un encargado que tiene menos horas (M-F4). Adaptar el sistema cambia, juntas, la validación de OA-01 (MV-02 con MB- y tres cifras), la restricción CHECK de ejemplares en src/esquema.sql y los datos y casos de PA-01; si cambia solo una, la otra rechaza. Se acepta cualquiera de las dos con su costo. Ficha de entorno: E-1 relevado en la computadora donada; E-2 sin internet (M-F7); E-5 y E-10 por el profesor vecino en su visita; E-11 respaldo semanal por el encargado con php respaldar.php; E-12 restauración probada por el profesor una vez por mes (M-F9). Lo que no se probó queda pendiente.'],
]
COTEJO_P10 = [
    ['La demostración muestra el dato después de reiniciar.', 'Indicador 5'],
    ['La ficha vincula operación, requisito, contrato y prueba.', 'Indicador 5'],
    ['La validación nueva rechaza en el servidor sin cambiar datos (Nivel 2 o 3).', 'Indicador 4'],
    ['La ficha de entorno dice qué se comprobó y qué queda pendiente, sin inventar resultados (Nivel 3).', 'Indicador 1'],
]
CRIT_C10 = [['8', '4: entradas (1), precondición de EF-3 (1), resultado (1), errores con su fuente EF-2 o EF-3 (1).', 'Un punto por cada parte.'],
            ['9', '4: alta con datos ficticios (1), un rechazo (1), cerrar y volver a abrir y encontrar el dato (1), bitácora con versión, prueba, resultado y entorno (1).', 'Sin el punto de persistencia si no se cierra y vuelve a abrir.']]
ERRORES_C10 = [
    ['Borrar a mano datos/biblioteca.sqlite para empezar de nuevo', 'php instalar.php --reiniciar (con respaldo verificado) o php restaurar.php'],
    ['Anotar en la ficha de entorno un resultado que no se obtuvo', 'Pendiente, con el motivo y quién lo comprueba'],
    ['Validar solo en el formulario', 'Validación en el servidor, en la operación, antes de tocar la base'],
    ['Armar la consulta pegando el texto que escribió la persona', 'Consulta parametrizada con «?»'],
    ['Dar por demostrada la persistencia sin reiniciar', 'Abrir la base con otra conexión, o detener y volver a iniciar el sistema'],
    ['Usar las claves de demostración con datos que no son de prueba', 'Reemplazarlas antes: el instalador las muestra una sola vez'],
]

# ---------------------------------------------------------------- capítulo 11
SEC_C11 = [
    ('Encuentro 21 — Catálogo: obras, ediciones y ejemplares (5 HC: 1 de diseño, 3 de práctica y 1 de verificación)', [
        ['Diseño', 'aprox. 1 HC', 'Sección 11.1 con la Tabla 11.1 y los contratos OA-02 y OA-05. Sección 11.2 con la Tabla 11.2 y el contrato OA-03 (adelanto del Encuentro 22). Actividad 1.'],
        ['Práctica', 'aprox. 3 HC', 'Ejemplos resueltos 11.1 y 11.2. Cada equipo construye OA-02 y OA-05 y sus formularios en PT-08 (Actividad 2).'],
        ['Verificación', 'aprox. 1 HC', 'PA-02 y PA-05; registro de las tareas en la bitácora (Actividad 3). Evidencia (Work, encuentro 21): alta, consulta y edición con reglas de validación. Actividad 4 como plenario.'],
    ]),
    ('Encuentro 22 — Lectores, permisos y baja lógica (5 HC: 1 de diseño, 3 de práctica y 1 de verificación)', [
        ['Diseño', 'aprox. 1 HC', 'Sección 11.3 con los Códigos 11.1 y 11.2 y la Tabla 11.3. Actividad 1.'],
        ['Práctica', 'aprox. 3 HC', 'Sección 11.4 con los contratos OA-04 y OP-06, los Códigos 11.3 y 11.4 y la Tabla 11.4. Cada equipo construye OA-03, OA-04 y OP-06 (Actividad 2). Ejemplo resuelto 11.4.'],
        ['Verificación', 'aprox. 1 HC', 'P-11 con las tres cuentas (Ejemplo resuelto 11.3, Actividad 3) y la parte de P-10 que no necesita préstamos. Evidencia (Work, encuentro 22): validación en el servidor y rechazo de acceso indebido. Práctica 11 en el nivel que indique el docente.'],
    ]),
]
CLAVES_E21 = [
    ['1', '(a) MV-02: «%s» (b) MV-01, si la obra es nueva: el título es obligatorio. (c) MA-05: «%s» (d) MA-04.' % (C.con_datos('MV-02', 'OB-31', 'OB- y cuatro cifras'), C.con_datos('MA-05', 'ED-0060')), 'Responder MA-02 para la edición: MA-02 es solo del ejemplar.'],
    ['2', 'OA-02 y OA-05 según sus contratos; PA-02 y PA-05 correctas. Formularios de PT-08 con formulario_inicio(), para la ficha CSRF y el «Guardando…».', 'Formularios sin ficha CSRF: el servidor los rechaza con MV-12.'],
    ['3', 'Cada fila de la Tabla 11.1 terminada con su prueba y resultado, y la versión del prototipo (0.3 al cerrar el incremento).', 'Marcar tareas terminadas sin prueba.'],
    ['4', 'El código guardado no coincidiría con la etiqueta pegada en el libro: al escanear o escribir la etiqueta, el sistema buscaría otro ejemplar o ninguno, y el error de carga quedaría oculto.', 'Aceptar la idea porque «evita el error».'],
]
CLAVES_E22 = [
    ['1', '(a) ME-12. (b) ME-13. (c) ME-13. (d) Ningún error: OP-05 admite a la bibliotecaria y a la dirección.', 'Usar ME-12 para (b) o (c).'],
    ['2', 'OA-03, OA-04 y OP-06 según sus contratos, con MV-01 a MV-04 para el lector (RI-06). PA-03, PA-04 y P-11 correctas; P-10 parcial (sin préstamos todavía).', 'Validar el curso solo en el formulario.'],
    ['3', 'Por ejemplo, con la cuenta de dirección se envía el alta de un ejemplar: ME-13 y el ejemplar no existe después. Se anota cuenta, operación, mensaje y estado de los datos.', 'Anotar solo el mensaje.'],
    ['4', 'La baja lógica con OP-06: el lector queda inactivo, no recibe préstamos nuevos y su historial se conserva (RI-05, RN-06). Borrarlo perdería sus préstamos y el informe de los meses en que estuvo.', 'Ofrecer el borrado «solo si no tiene préstamos activos».'],
    ['5', 'Un estudiante con un préstamo de marzo registrado en 2.º BTI; se corrige su curso a 3.º BTI con OA-04; el informe de marzo sigue con ese préstamo en 2.º BTI (RI-08). La referencia docente lo comprueba en prueba_contratos.php.', 'Comprobar con el informe del mes actual.'],
]
CLAVES_P11 = [
    ['Nivel 1', 'MD-01: se registra (obra nueva, su edición y el ejemplar MB-201). MD-02: se registra como otro ejemplar de la misma obra y edición (MB-202). MD-03: el sistema la rechaza con MA-02 (MB-202 ya existe): hay que revisar la etiqueta del libro y darle otra. MD-04: se corrige antes: es la misma obra que MD-01; el ejemplar MB-204 va en esa edición. MD-05: falta el autor: MV-01 al registrar la obra; hay que pedir el dato. MD-06: MV-02 por el formato (MB205). ML-1: MV-03, falta el curso (4.º grado). ML-2: MV-04, el docente no lleva curso. ML-3: se registra (MA-06).'],
    ['Nivel 2', '«La laguna de los patos»: una obra, una edición (salvo que las tapas muestren ediciones distintas) y tres ejemplares (MB-201, MB-202 y MB-204), con el título bien escrito. «Canciones del recreo»: una obra, una edición y un ejemplar con una etiqueta nueva. «Mapas de mi país»: MD-05 y MD-06 son probablemente el mismo libro (MB-205 sin autor y MB205 con autor): se revisa el estante y, si es uno, se registra una sola vez con el autor de MD-06. Orden: OA-02 antes que OA-01. Consulta esperada: 3, 1 y 1 disponibles (o 2 si los mapas son dos libros con etiquetas distintas).'],
    ['Nivel 3', 'Los voluntarios no usan la cuenta del encargado. Opción esperada: usan solo la consulta pública, que no pide sesión ni muestra datos de lectores (MN-05, RNF-03), y el encargado registra. Si la escuela quiere que registren, hace falta una solicitud de cambio con un rol nuevo, una zona y su comprobación en el servidor, sin acceso a datos de otros estudiantes. Prueba: con la cuenta del voluntario (si existe), pedir un préstamo o el informe responde ME-13 y no cambia nada.'],
]
COTEJO_P11 = [
    ['Ningún código repetido se registra y cada rechazo tiene su mensaje.', 'Indicadores 2 y 3'],
    ['El título mal escrito no crea una obra nueva (Nivel 2 o 3).', 'Indicador 3'],
    ['El estudiante sin curso y el docente con curso se rechazan.', 'Indicador 2'],
    ['Los voluntarios no comparten la cuenta ni ven datos de lectores, comprobado en el servidor (Nivel 3).', 'Indicador 4'],
]
CRIT_C11 = [['8', '4: una regla completa con su mensaje y su restricción (1 cada una, hasta 3) y las fuentes citadas (1).', 'Sin punto si la regla no tiene restricción en la base.'],
            ['9', '4: cuenta de docente con sesión (1), pedido enviado aunque no haya botón (1), error de permiso (1), datos sin cambios (1).', 'Un punto por cada parte.']]
ERRORES_C11 = [
    ['Usar ME-12 para un permiso que falta', 'ME-12 solo en el ingreso; ME-13 para la falta de permiso'],
    ['Ocultar el botón y no comprobar el rol en la operación', 'sin_permiso() como primera línea de cada operación protegida'],
    ['Registrar como obra nueva otra edición de una obra existente', 'OA-02 con el código de la obra que ya existe'],
    ['Reutilizar el código de un ejemplar dado de baja', 'Los códigos no se reutilizan: el historial los nombra'],
    ['Borrar un lector que egresó', 'OP-06: inactivo, con su historial'],
    ['Cambiar el curso en los préstamos anteriores al corregir un lector', 'Los préstamos guardan el curso al prestar (RI-08)'],
]

# ---------------------------------------------------------------- capítulo 12
SEC_C12 = [
    ('Encuentro 23 — El préstamo y sus protecciones (5 HC: 1 de diseño, 3 de práctica y 1 de verificación)', [
        ['Diseño', 'aprox. 1 HC', 'Sección 12.1 con el contrato de OP-01, la Tabla 12.1 y los Ejemplos resueltos 12.1 y 12.2. Actividad 1.'],
        ['Práctica', 'aprox. 3 HC', 'Sección 12.2 con la Figura 12.1 y los Códigos 12.1 y 12.2. Cada equipo construye comprobar_prestamo(), registrar_prestamo() y PT-05 (Actividad 2).'],
        ['Verificación', 'aprox. 1 HC', 'P-01, P-02, P-05, P-06a, P-06b y P-07; prueba de carrera con procesos independientes (Tabla 12.2 y protocolo de la sección 0.4) y registro del entorno (Actividad 3). Evidencia (Work, encuentro 23): operación coherente ante reenvío o segunda solicitud.'],
    ]),
    ('Encuentro 24 — Devolución, historial y fallos previsibles (5 HC: 1 de diseño, 3 de práctica y 1 de verificación)', [
        ['Diseño', 'aprox. 1 HC', 'Sección 12.3 con el contrato de OP-02, el Código 12.3 y el Ejemplo resuelto 12.3. Actividad 1.'],
        ['Práctica', 'aprox. 3 HC', 'Cada equipo construye registrar_devolucion() y PT-06 (Actividad 2). Sección 12.4 con el Código 12.4 y la Tabla 12.3.'],
        ['Verificación', 'aprox. 1 HC', 'P-03, la parte de P-10 que quedó pendiente y la consulta de control del Ejemplo resuelto 12.4 (Actividad 3). Evidencia (Work, encuentro 24): devolución única, conservación de referencias y pruebas. Práctica 12 en el nivel que indique el docente.'],
    ]),
]
CLAVES_E23 = [
    ['1', 'Orden: permiso, datos, lector existe, lector activo, máximo, ejemplar existe, ejemplar activo, ejemplar sin préstamo activo. (a) ME-01. (b) MV-06. (c) ME-03 con el vencimiento del préstamo vigente.', 'Comprobar el ejemplar antes que el lector: cambia el mensaje que ve la bibliotecaria.'],
    ['2', 'Las comprobaciones de la Tabla 12.1 en ese orden, dentro de la operación atómica del Código 12.1, y PT-05 con formulario_inicio(). Pruebas correctas; la de carrera, con el entorno anotado.', 'Comprobar fuera de la transacción y registrar adentro.'],
    ['3', 'Cada prueba con esperado, obtenido y entorno (sistema, PHP, SQLite). Si la de carrera no se pudo ejecutar, pendiente con el mensaje exacto.', 'Anotar «P-07 correcta» sin el entorno.'],
    ['4', 'Quedaría sin protección todo lo que no pase por la comprobación: un error de programación en el orden o en la consulta, una operación futura que inserte préstamos (por ejemplo, una reposición) o un dato escrito directamente en la base.', 'Responder que «la transacción ya alcanza».'],
]
CLAVES_E24 = [
    ['1', '(a) ME-06; no cambia nada. (b) ME-05. (c) MV-10: la devolución no puede ser anterior a la salida; el préstamo sigue activo.', 'Responder ME-07 en (a).'],
    ['2', 'registrar_devolucion() con su contrato: permiso, ejemplar existente, fecha válida y la sentencia única del Código 12.3, con ME-07 o ME-06 según cuántas filas cambió. P-03 correcta y P-10 completa.', 'Buscar el préstamo con una consulta y cerrarlo con otra: dos pedidos a la vez podrían cerrar dos veces.'],
    ['3', 'La consulta de control no devuelve filas después de las pruebas; se anota con la prueba y el entorno.', 'No anotar el resultado cuando no hay filas.'],
    ['4', 'No se borra: se registra la devolución con la misma fecha y se marca como anulado con su motivo y quién lo anuló. Es un requisito nuevo (por ejemplo, «anular un préstamo cargado por error, conservando el registro»), que se tramita como solicitud de cambio y cambia el contrato de OP-02 o agrega una operación.', 'Proponer un botón que borre el préstamo.'],
    ['5', 'Respuesta abierta. Ejemplos: la sesión venció en medio del préstamo (ME-13, nada cambia); se cerró el navegador antes de ver la respuesta (se comprueba en PT-07 si se registró); se intenta inactivar un ejemplar prestado (decisión de diseño a registrar).', 'Fallo sin prueba.'],
]
CLAVES_P12 = [
    ['Nivel 1', 'El primer pedido reserva la base para escribir (BEGIN IMMEDIATE); el segundo espera. Cuando el primero registra y termina, el segundo comprueba y encuentra MB-104 prestado: ME-03. Si por un error el segundo pasara la comprobación, el índice único rechaza el segundo préstamo activo y la operación responde ME-03 igual. Mensaje: «No se puede prestar: el ejemplar MB-104 ya está prestado y vence el … (siete días después). Elegí otro ejemplar disponible.»'],
    ['Nivel 2', 'Dos o más procesos independientes, cada uno con su conexión (php pruebas/prueba_carrera.php o dos procesos de línea de comandos lanzados a la vez), el mismo ejemplar y lectores distintos, varias rondas. Esperado: un ME-04 y el resto ME-03 por ronda; la consulta de control no devuelve filas. Dos pestañas contra php -S no prueban nada en Windows: el servidor atiende de a un pedido y los pedidos nunca se superponen. Si no se pudo ejecutar: pendiente, con la versión de Windows, PHP y SQLite y el mensaje exacto; no se declara aprobada.'],
    ['Nivel 3', 'Orden: 1) devolución del préstamo (con la nota de daño, contrato de la Práctica 9); 2) baja del ejemplar dañado con OP-06; 3) alta del ejemplar que lo repone con OA-01 y un código nuevo. Lo más seguro es que 2 y 3 sean una sola operación atómica («registrar reposición»). Si son tres y el sistema falla entre 2 y 3, el dañado queda inactivo y falta el nuevo: no se pierde historial y se completa después; lo que nunca puede pasar es que el dañado quede activo y prestable. Se acepta cualquier decisión justificada.'],
]
COTEJO_P12 = [
    ['Se registra un solo préstamo de MB-104 y se explica qué protección actúa.', 'Indicador 2'],
    ['El otro voluntario recibe un mensaje útil.', 'Indicador 1'],
    ['La prueba usa procesos independientes y se anota con su entorno, o como pendiente (Nivel 2 o 3).', 'Indicador 3'],
    ['El libro dañado queda en el historial, inactivo, y el que lo repone es un ejemplar nuevo (Nivel 3).', 'Indicador 4'],
]
CRIT_C12 = [['8', '4: orden correcto (1), fuentes CA-1 y CA-2 (1), mensajes (1), registro final (1).', 'Sin el punto del orden si la calculadora se comprueba antes que el permiso.'],
            ['9', '4: operación atómica bien explicada (2) y restricción única con el caso que cubre (2).', '1 punto por cada protección nombrada sin explicar el caso.']]
ERRORES_C12 = [
    ['Probar la simultaneidad con dos pestañas contra php -S', 'Dos procesos independientes, cada uno con su conexión'],
    ['Comprobar fuera de la transacción y registrar adentro', 'Comprobación y registro entre BEGIN IMMEDIATE y COMMIT'],
    ['Quitar el índice único porque «la operación ya comprueba»', 'Las dos protecciones de RI-01'],
    ['Escribir el máximo en el código', 'Leerlo de Parámetro según el tipo del lector'],
    ['Devolver buscando y cerrando con dos sentencias', 'Una sola sentencia sobre el préstamo activo; ME-06 si no cambió ninguna fila'],
    ['Declarar aprobada una prueba que corrió en otro equipo', 'Vale para el entorno donde corrió; en el del colegio, pendiente'],
]

# ---------------------------------------------------------------- capítulo 13
SEC_C13 = [
    ('Encuentro 25 — Consultas, vencimientos e informe (5 HC: 1 de diseño, 3 de práctica y 1 de verificación)', [
        ['Diseño', 'aprox. 1 HC', 'Sección 13.1 con los contratos de OP-03 y OP-04, el Código 13.1 y el Ejemplo resuelto 13.1. Actividad 1.'],
        ['Práctica', 'aprox. 3 HC', 'Sección 13.2 con la Figura 13.1, el Código 13.2, la Tabla 13.1, el contrato de OP-05 y el Ejemplo resuelto 13.2. Cada equipo construye OP-03, OP-04, OP-05 y PT-02, PT-07 y PT-09 (Actividad 2).'],
        ['Verificación', 'aprox. 1 HC', 'P-04, P-08, P-09 y P-12; permisos de PT-07 y PT-09 (Actividad 3). Evidencia (Work, encuentro 25): reporte correcto con fecha de referencia definida.'],
        ['Complemento (fuera de las 5 HC)', 'aprox. 1 HC', 'Práctica 13, complemento editorial: como tarea o como actividad complementaria. No ocupa tiempo del Encuentro 26 ni reduce las 2 HC de evaluación.'],
    ]),
    ('Encuentro 26 — Integración, demostración y revisión de la Unidad IV, H4 (5 HC: 2 de práctica, 1 de verificación y 2 de evaluación)', [
        ['Integración', 'aprox. 2 HC (práctica)', 'Sección 13.3: recorrido E-6a y P-13 sin internet; revisión con la Tabla 13.2 (Actividades 1 y 2). Ejemplo resuelto 13.3.'],
        ['Demostración', 'aprox. 1 HC (verificación)', 'Sección 13.4: cada equipo demuestra ante otro y registra sus incidencias con la Tabla 13.3 (Actividad 3).'],
        ['Revisión de la unidad (H4)', 'aprox. 2 HC (evaluación)', 'Lista de verificación del H4, revisión con la rúbrica (sección 5) y una variante del banco para cada integrante, resuelta en forma individual. Se completa la planilla. Evidencia (Work, encuentro 26): prototipo completo mínimo y lista de incidencias.'],
    ]),
]
CLAVES_E25 = [
    ['1', 'Con 12/03: los tres en plazo (EJ-0458 vence ese mismo día). Con 22/03: los tres vencidos (12/03, 17/03 y 21/03 son anteriores).', 'Marcar vencido el que vence el mismo día.'],
    ['2', 'OP-03 sin datos de lectores; OP-04 con la fecha de referencia como entrada (MV-08 si es inválida, ME-10 si no hay activos); OP-05 con el total contado de nuevo. P-04, P-08, P-09 y P-12 correctas.', 'Usar la fecha del día dentro de la consulta en lugar de la fecha de referencia.'],
    ['3', 'El informe responde con las dos cuentas (PT-09 está en la zona compartida). PT-07 con la cuenta de dirección responde ME-13.', 'Esperar ME-12 para la dirección en PT-07.'],
    ['4', 'RNF-03: la consulta pública no muestra datos personales, y la mayoría de los lectores son menores de edad. Se puede mostrar «0 disponibles por ahora» sin el nombre de nadie.', 'Aceptarlo porque «es útil».'],
]
CLAVES_P13 = [
    ['Nivel 1', 'Lo que pasó: el viernes 10 están prestados MB-105 y MB-201; MB-104 volvió el miércoles 8 (MI-03). En el sistema, MB-104 sigue con su préstamo activo porque la devolución no se registró: por eso la consulta dice 0 disponibles (MI-05) si el título tiene un solo ejemplar (M-F8). No falla una operación: faltó un registro. Se corrige registrando la devolución con la fecha real (2026-04-08), sin borrar nada, y se anota en la bitácora.'],
    ['Nivel 2', 'MB-104 salió el lunes 6 con plazo de siete días: vence el 13 de abril. Con fecha de referencia 13 de abril no está vencido: vence ese mismo día. Si el sistema lo marca vencido (MI-07), hay una incidencia en OP-04 (compara «vence antes o el mismo día» en lugar de «antes»): PT-07/OP-04, «con referencia 13/04, un préstamo que vence el 13/04 aparece vencido», gravedad media, prueba con un préstamo cuyo vencimiento es igual a la fecha de referencia. Además, después de corregir el nivel 1, MB-104 ya no aparece en la lista.'],
    ['Nivel 3', 'Abril: MI-01 (5.º grado), MI-02 (6.º grado) y MI-04 (Docentes): 3 préstamos, uno por grupo. Coincide con las fichas (MI-06): no hay incidencia, y se anota que coincide. Lista: la devolución no registrada (proceso; gravedad alta, porque la consulta pública informa mal) y el vencimiento del mismo día (OP-04; gravedad media), cada una con destino Unidad V y una prueba de regresión: devolución registrada que vuelve a mostrar el ejemplar disponible, y vencimiento igual a la fecha de referencia marcado en plazo.'],
]
COTEJO_P13 = [
    ['La diferencia de MI-05 se explica por un registro que faltó y se corrige con una devolución, no borrando.', 'Indicadores 1 y 5'],
    ['El vencimiento de MB-104 se calcula con el plazo y se compara con la regla (Nivel 2 o 3).', 'Indicador 2'],
    ['Cada incidencia tiene gravedad, destino y una prueba que la reproduce (Nivel 2 o 3).', 'Indicador 5'],
    ['Lo que coincide también se anota (Nivel 3).', 'Indicador 4'],
]
CLAVES_E26 = [
    ['1', 'Respuesta abierta: cada fila de la Tabla 13.2 con la prueba y el resultado obtenido, o «pendiente» con el motivo (por ejemplo, E-12 o la prueba de carrera en la computadora del colegio).', 'Marcar «cumplida» una fila sin prueba.'],
    ['2', 'Cada paso de E-6a con su resultado y su mensaje, con la red desconectada (P-13). Si un paso falla, se anota el mensaje exacto y pasa a la lista de incidencias.', 'Hacer el recorrido con internet y anotarlo como P-13.'],
    ['3', 'Lista con código, dónde, qué pasa, gravedad, estado y destino; versión del prototipo revisada (por ejemplo, 0.6).', 'Lista sin gravedad o sin destino.'],
]
CRIT_C13 = [['8', '4: entradas (1), precondición con su fuente MP-3 (1), resultado con la regla del vencimiento (1), errores (1).', 'Sin el punto del resultado si usa «hoy» en lugar de la fecha de referencia.'],
            ['9', '4: cada incidencia completa (1 cada una) y su prueba reproducible (1 cada una).', 'Sin punto si la prueba no dice qué datos usar.']]
ERRORES_C13 = [
    ['Guardar la cantidad de disponibles', 'Contarla en el momento: es un dato derivado'],
    ['Calcular los vencidos con la fecha del día dentro de la consulta', 'Fecha de referencia como entrada, escrita en la pantalla'],
    ['Marcar vencido el préstamo que vence el mismo día de la fecha de referencia', 'Vencido = vencimiento anterior a la fecha de referencia'],
    ['Sumar a mano el total del informe', 'Contar de nuevo los préstamos del mes'],
    ['Agrupar el informe por el curso actual del estudiante', 'Curso al prestar (RI-08)'],
    ['Ocultar una incidencia en la demostración', 'Registrarla con gravedad y destino; ocultarla es lo que no se admite'],
]

RUBRICA_EXPLICACION = [
    'El H4 se califica con la misma lógica que los hitos H1 a H3: para cada criterio se registran el nivel del producto del equipo '
    'y el nivel individual de cada integrante, y se combinan en la proporción 60 % (equipo) y 40 % (individual). Por ejemplo, '
    'con 4, 3, 2 y 1 puntos para Sólido, Logrado, En desarrollo e Inicial, un producto Logrado (3) con una evidencia individual '
    'Sólida (4) da 3 × 0,6 + 4 × 0,4 = 3,4. La conversión a calificación la decide la institución.',
    'La evidencia individual es la resolución de una variante del banco, propuesta por el docente durante la revisión, el '
    'aporte registrado en la bitácora y la observación del docente. El estudiante explica qué capa toca la variante, qué '
    'archivo cambiaría y qué prueba lo comprobaría; no hace falta programarla en el momento. Las variantes no están en el '
    'dossier, en el buzón, en la nota D3, en el banco del H3 ni en las prácticas.',
    'La ausencia de evidencia se registra aparte («AE»), con la fecha acordada para entregarla; no se confunde con un '
    'desempeño de nivel Inicial. Una prueba que no se pudo ejecutar en la computadora del colegio se registra como pendiente '
    'del entorno, no como falla del equipo. La proporción 60/40 y los niveles son una propuesta editorial tomada del informe '
    'de Work (§4.3); no son una escala oficial del MEC.',
    'Las condiciones mínimas de aceptación de Work §4.3 son criterios del proyecto, no reglas automáticas de promoción. En el '
    'H4 se muestran las que corresponden a la Unidad IV; la instalación y la restauración reproducibles por otro equipo son '
    'evidencia de la Unidad VI.',
]
CALENDARIO_28 = (['Encuentro (36)', 'Encuentro (28)', 'Qué se hace'],
                 [['19 y 20', '15', 'Se unen: el docente entrega el entorno, la conexión y el inicio de sesión listos (base explicada, Work §7.5); el equipo hace la primera operación (OA-01 con PA-01 y persistencia).'],
                  ['21 y 22', '16', 'Se unen: lectores por carga inicial; los permisos mínimos vienen en la base y el equipo los prueba (P-11). OA-02 y OP-06 con P-10.'],
                  ['23', '17', 'Sin cambios: préstamo y prevención de duplicados.'],
                  ['24', '18', 'Sin cambios: devolución e historial.'],
                  ['25 y 26', '19', 'Se unen: solo disponibles, activos y vencidos con fecha de referencia; integración y H4. El informe mensual y la Práctica 13 pasan a actividad complementaria.']])
PROCEDENCIA = (['Recurso', 'Procedencia', 'Derechos'],
               [['Texto de los Capítulos 10 a 13 y de la apertura de la unidad', 'Redacción original para este libro.', 'Propios del proyecto.'],
                ['Figuras 10.1 a 13.1', 'Generadas con build/diagramas_u4.py; la Figura 10.2 usa la notación de capas de la Tabla 9.1 (diagramas_u3.py), sin símbolos nuevos; las demás son esquemas didácticos.', 'Propias; sin recursos de terceros.'],
                ['Base de proyecto (referencia docente y base del estudiante)', 'Adaptada del Piloto B v2.3 de la colección (fase2_pilotos/B_prueba_tecnica) al diseño del lote 3 v1.1: Edición, Parámetro, tipo de lector, curso al prestar, dos roles y ME-13; operaciones auxiliares OA-01 a OA-05; restauración segura nueva.', 'Propia del proyecto. PHP y SQLite son software libre; no se incluye código de terceros.'],
                ['Fragmentos de código del libro y de la guía', 'Leídos de los archivos del proyecto por build/fragmentos.py; el verificador comprueba que coincidan, línea por línea.', 'Propios.'],
                ['Caso Arapoty: operaciones auxiliares, ficha de entorno, alcance y banco del H4', 'Inventados. Fuente única: lote_4/caso/construccion.py, que lee sin modificarlos lote_3/caso/diseno.py y el proyecto.', 'Propios del proyecto.'],
                ['Caso de práctica Mbokaja (Unidad IV)', 'Inventado para este lote: lote_4/caso/mbokaja_u4.py, que amplía las fuentes de Mbokaja de los lotes 1 a 3.', 'Propio.'],
                ['Capacidades, niveles de desempeño, proporción 60/40, secuencia de encuentros, alcance mínimo y ruta técnica', 'Informe de Work v0.1 (§3, §4.2, §4.3, §5.2, §7.2, §7.5), como propuesta editorial. La ruta técnica es una referencia provisional, no probada en equipos escolares.', 'Insumo interno del proyecto.'],
                ['Relación con Laboratorio y Algorítmica', 'Se citan los temas del Diseño Curricular que menciona Work §8.2; no hay unidad de sintaxis PHP ni manual de SQL, ni ejercicios de Access o de Algorítmica.', 'No aplica.']])


def _sec(doc, secuencia):
    for titulo, filas in secuencia:
        M.tabla(doc, (['Momento', 'Tiempo', 'Qué se hace'], filas), ANCHO_SEC, rotulo=titulo)


def _claves(doc, rotulo, filas):
    M.tabla(doc, (['Act.', 'Respuesta esperada', 'Error frecuente'], filas), [1.2, 11.0, 4.4], rotulo=rotulo)


def _eval(doc, C_, claves, crit):
    filas = [[str(n), clave, detalle] for eid, n, clave, detalle in claves if eid == C_.EVAL_ID]
    M.tabla(doc, (['Ítem', 'Clave', 'Respuesta o criterio'], filas), [1.2, 1.8, 13.6], rotulo='Clave de la %s' % C_.EVAL_TITULO.lower())
    M.tabla(doc, (['Ítem', 'Puntaje completo', 'Puntaje parcial'], crit), [1.2, 8.4, 7.0], rotulo='Criterios de corrección de los ítems abiertos')


def _niveles(doc, rotulo, filas):
    M.tabla(doc, (['Nivel', 'Respuesta esperada'], filas), [2.2, 14.4], rotulo=rotulo)


def _errores(doc, rotulo, filas):
    M.tabla(doc, (['Error frecuente', 'Cómo se corrige'], filas), [8.6, 8.0], rotulo=rotulo)


def _cotejo(doc, rotulo, filas):
    M.tabla(doc, (['Criterio', 'Indicador'], filas), [13.0, 3.6], rotulo=rotulo)


def construir(ruta, claves, paginas, estado, figs):
    import cap3   # niveles de desempeño del lote 1
    doc = H.new_doc()
    Z.portada(doc, 'Guía docente con solucionario', estado)
    doc.add_heading('Guía docente — Lote 4', level=1)
    H.caja(doc, 'Sobre las capacidades y el entorno técnico', [
        'Las capacidades de las fichas (C3, C5, C6, C7, C8 y C9 en esta unidad, y C7 a C9 en el H4) son propuestas para el '
        'programa institucional del Plan Optativo, tomadas del informe de Work. No son capacidades oficiales del MEC.',
        'El entorno de la base de proyecto (HTML y CSS, PHP y SQLite, en una computadora local, sin servicios pagos) es la '
        'referencia editorial provisional. No es obligatorio y no se probó en las computadoras de ninguna institución ni en '
        'Windows: sus pruebas corrieron solo en el entorno de construcción de este material (sección 7).'], tipo='neutra')
    H.p_texto(doc, 'Cada encuentro sigue la estructura de taller de Work: 1 HC de problema y explicación, 3 HC de práctica y '
                   '1 HC de revisión, con la distribución por categorías de la versión 2.1 (práctica, gestión, diseño, '
                   'verificación y evaluación en esta unidad). Los tiempos son aproximados y la duración de la hora cátedra '
                   'la fija cada institución.', italic=True, size=9.5)

    # 0. antes del Encuentro 19
    doc.add_heading('0. Antes del Encuentro 19: entorno, base de proyecto y coordinación', level=2)
    doc.add_heading('0.1 Coordinación con Laboratorio', level=3)
    for t in LABORATORIO:
        H.p_texto(doc, t)
    doc.add_heading('0.2 Prueba de campo y ficha de entorno', level=3)
    for t in ESTADO_CAMPO:
        H.p_texto(doc, t)
    M.tabla(doc, (['Código', 'Qué se comprueba', 'Cómo', 'Qué se anota'], [list(f) for f in C.FICHA_ENTORNO]),
            [1.4, 3.4, 7.8, 4.0], rotulo='Ficha de entorno completa (E-1 a E-12, con E-6a y E-6b)', size=8.5)
    H.p_texto(doc, 'E-6a recorre el prototipo docente completo y sirve para la prueba de campo y para comparar. E-6b '
                   'comprueba solo lo que la base del estudiante trae preparado: no exige las operaciones que el curso '
                   'todavía tiene que construir.', size=10)
    M.tabla(doc, DIFERENCIAS_WINDOWS, [7.6, 9.0], rotulo='Diferencias ya conocidas en Windows (protocolo de campo del Piloto B)')
    doc.add_heading('0.3 Si el entorno de referencia no funciona: otro entorno con evidencias equivalentes', level=3)
    for t in ALTERNATIVO:
        H.p_texto(doc, t)
    M.tabla(doc, (['Evidencia', 'Qué tiene que mostrar el otro entorno'], [list(e) for e in C.EVIDENCIAS_EQUIVALENTES]),
            [4.0, 12.6], rotulo='Evidencias equivalentes (Work §7.5)')
    doc.add_heading('0.4 Protocolo de concurrencia para Windows', level=3)
    for t in C.PROTOCOLO_CONCURRENCIA:
        H.p_texto(doc, t)
    M.tabla(doc, PROTOCOLO_REGISTRO, [7.0, 3.2, 3.2, 3.2], rotulo='Registro de la prueba de concurrencia (una hoja por computadora)')
    doc.add_heading('0.5 Las dos distribuciones de la base de proyecto', level=3)
    H.p_texto(doc, 'La referencia docente es el sistema completo: el docente la usa para comparar, para las pruebas y para la '
                   'prueba de campo. No se entrega a los estudiantes. La base del estudiante trae la estructura, la conexión, '
                   'el ingreso preparado y los componentes esenciales, sin las operaciones resueltas: cada una responde '
                   '«PENDIENTE» hasta que el equipo la construye. Los archivos comunes son idénticos en las dos.')
    M.tabla(doc, tabla_archivos(), [5.6, 7.6, 3.4], rotulo='Archivos del proyecto y su estado en la base del estudiante', size=8.5)
    for t in texto_lineas():
        H.p_texto(doc, t)
    M.tabla(doc, tabla_lineas()[0], [9.6, 3.5, 3.5], rotulo='Tamaño de la base del estudiante (PHP propio)')
    H.caja(doc, 'Cuentas y datos', [
        'Las cuentas bibliotecaria1 y direccion1 son de demostración. El instalador genera una clave al azar para cada una y la '
        'muestra una sola vez (o usa la que se da con --clave=). No hay contraseñas reales en ningún material. Todos los datos '
        'son ficticios.',
        'Una instalación nunca borra una base existente: para empezar de cero, php instalar.php --reiniciar, que pide '
        'confirmación y guarda antes un respaldo verificado. php restaurar.php valida el respaldo antes de tocar nada, muestra '
        'qué contiene, pide escribir RESTAURAR y guarda una copia verificada de la base actual.'], tipo='neutra')

    # 1 a 4. capítulos
    for n, (C_, sec, errores, bloques) in enumerate((
            (cap10, SEC_C10, ERRORES_C10, [('Encuentro 19', CLAVES_E19), ('Encuentro 20', CLAVES_E20)]),
            (cap11, SEC_C11, ERRORES_C11, [('Encuentro 21', CLAVES_E21), ('Encuentro 22', CLAVES_E22)]),
            (cap12, SEC_C12, ERRORES_C12, [('Encuentro 23', CLAVES_E23), ('Encuentro 24', CLAVES_E24)]),
            (cap13, SEC_C13, ERRORES_C13, [('Encuentro 25', CLAVES_E25), ('Encuentro 26', CLAVES_E26)])), start=1):
        K.titulo_en_pagina_nueva(doc, '%d. %s — %s' % (n, C_.CAPITULO, C_.TITULO), nivel=2)
        M.ficha(doc, C_)
        _sec(doc, sec)
        if C_ is cap10:
            Z.tabla_leyenda(doc, 'capas', 'Leyenda: esquema de capas (Figura 10.2, la misma notación de la Tabla 9.1)', figs)
        _errores(doc, 'Errores frecuentes del %s' % C_.CAPITULO, errores)
        if C_ is cap11:
            H.p_texto(doc, 'Referencia para el docente: las validaciones del lector de la referencia docente (OA-03 y OA-04). '
                           'El libro no las publica: los equipos las construyen con la Tabla 11.2.', size=10)
            Z.codigo(doc, 'Referencia R-1')
        if C_ is cap12:
            H.p_texto(doc, 'Referencia para el docente: las comprobaciones de OP-01 de la referencia docente. El libro da su '
                           'especificación (Tabla 12.1), no el código.', size=10)
            Z.codigo(doc, 'Referencia R-2')
        if C_ is cap13:
            H.p_texto(doc, 'Referencia para el docente: la consulta del informe mensual (OP-05). El libro da el contrato y la '
                           'forma de comprobarlo (Ejemplo resuelto 13.2), no la consulta.', size=10)
            Z.codigo(doc, 'Referencia R-3')
        for enc, cl in bloques:
            _claves(doc, 'Claves de las actividades del %s' % enc, cl)
        if C_ is cap13:
            H.p_texto(doc, 'La Práctica 13 es un complemento editorial al índice de Work: se asigna en el Encuentro 25 o como '
                           'actividad complementaria y no se evalúa en el H4.', size=10)
        _niveles(doc, 'Práctica %d: claves por nivel' % C_.NUM, {cap10: CLAVES_P10, cap11: CLAVES_P11, cap12: CLAVES_P12, cap13: CLAVES_P13}[C_])
        _cotejo(doc, 'Lista de cotejo de la Práctica %d' % C_.NUM, {cap10: COTEJO_P10, cap11: COTEJO_P11, cap12: COTEJO_P12, cap13: COTEJO_P13}[C_])
        _eval(doc, C_, claves, {cap10: CRIT_C10, cap11: CRIT_C11, cap12: CRIT_C12, cap13: CRIT_C13}[C_])

    # 5. rúbrica H4
    K.titulo_en_pagina_nueva(doc, '5. Rúbrica del hito H4: circuito funcional completo y lista de incidencias', nivel=2)
    for t in RUBRICA_EXPLICACION:
        H.p_texto(doc, t)
    M.tabla(doc, (['Criterio', '4. Sólido', '3. Logrado', '2. En desarrollo', '1. Inicial'],
                  [['%s (%s)' % (r[0], r[1])] + r[2] for r in cap13.RUBRICA_H4]),
            [2.8, 3.6, 3.4, 3.4, 3.4], rotulo='Rúbrica del H4: descriptores por nivel', size=8.5)
    M.tabla(doc, (['Criterio', 'Evidencia del equipo (60 %)', 'Evidencia individual (40 %)'],
                  [[r[0], r[3], r[4]] for r in cap13.RUBRICA_H4]), [4.4, 5.8, 6.4], rotulo='Evidencias de cada criterio del H4')
    M.tabla(doc, (['Nivel de desempeño', 'Descriptor común (Work §4.3)'], [list(x) for x in cap3.NIVELES_DESEMPENO]),
            [3.6, 13.0], rotulo='Niveles de desempeño (propuesta editorial)')
    M.tabla(doc, (['Estudiante (código)', 'Criterio', 'Nivel del equipo', 'Nivel individual', 'Resultado', 'AE'],
                  [['', r[0], '', '', '', ''] for r in cap13.RUBRICA_H4]),
            [3.0, 5.0, 2.2, 2.2, 2.2, 2.0], rotulo='Planilla de registro del H4 (una por estudiante)')
    M.tabla(doc, (['Código', 'Variante', 'Qué tiene que encontrar el estudiante'], [list(v) for v in C.BANCO_H4]),
            [1.6, 7.0, 8.0], rotulo='Banco de variantes para la evidencia individual del H4')
    H.p_texto(doc, 'Ninguna de estas variantes está en el dossier, en el buzón, en la nota D3, en el banco del H3 ni en las '
                   'prácticas. Se asigna una por integrante; si el curso trabaja con su propia biblioteca, el docente formula '
                   'una variante equivalente.', italic=True, size=9.5)

    # 6. calendario, 7. resultados, 8. procedencia
    doc.add_heading('6. Calendario con menos encuentros', level=2)
    H.p_texto(doc, 'En la adaptación de 28 encuentros (distribución v2.1), la Unidad IV pasa de ocho a cinco encuentros. Cada '
                   'capítulo del libro tiene su recuadro «Si el calendario se acorta».')
    M.tabla(doc, CALENDARIO_28, [2.6, 2.6, 11.4], rotulo='Unidad IV en 36 y en 28 encuentros')
    doc.add_heading('7. Resultados de las pruebas de la base y entorno en que corrieron', level=2)
    tabla, entorno = tabla_resultados()
    H.p_texto(doc, 'Entorno de todas las pruebas: %s' % entorno, size=10)
    M.tabla(doc, tabla, [4.0, 6.6, 6.0], rotulo='Resultados de las pruebas (build/reproducir.py)')
    H.p_texto(doc, 'Estos resultados valen para ese entorno. En las computadoras del colegio, las pruebas E-1 a E-12 y la de '
                   'concurrencia siguen pendientes hasta que se hagan con la ficha de la sección 0.', italic=True, size=9.5)
    doc.add_heading('8. Procedencia y derechos de los recursos', level=2)
    M.tabla(doc, PROCEDENCIA, [4.4, 7.8, 4.4], rotulo='Inventario de recursos del lote')
    M.pegar_renglones(doc)
    Z.encadenar_inicio(doc)
    K.saltos_a_titulos(doc)
    H.finalizar(doc, ruta)
