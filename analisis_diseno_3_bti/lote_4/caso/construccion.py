# -*- coding: utf-8 -*-
"""Fuente única de la construcción del prototipo (Unidad IV, Capítulos 10 a 13). Caso Arapoty, ficticio.

Lee sin modificarlos `lote_3/caso/diseno.py` (catálogo v1.1, contratos OP-01 a OP-06 corregidos en la v1.1,
pantallas, mensajes ME-01 a ME-13) y el proyecto de `lote_4/proyecto/` (código, mensajes y resultados de pruebas).
Contiene:
  - incrementos y tareas de cada encuentro, con su operación, requisito y prueba;
  - operaciones auxiliares OA-01 a OA-04 (no figuran en el Capítulo 9) con contrato y prueba propios (PA-01 a PA-04);
  - ficha de entorno E-1 a E-12, con E-6 separada en E-6a (referencia docente) y E-6b (base del estudiante);
  - alcance mínimo de Work §7.2 (textual) y cómo lo cubre el prototipo;
  - evidencias equivalentes para otro entorno y protocolo de concurrencia para Windows;
  - banco de variantes del H4.
Los mensajes MA y MV y los textos de ME se leen de proyecto/referencia_docente/src/mensajes.php: no se copian."""
import os, re, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
L4 = os.path.dirname(AQUI)
ADS = os.path.dirname(L4)
PROY = os.path.join(L4, 'proyecto')
REF = os.path.join(PROY, 'referencia_docente')
BASE = os.path.join(PROY, 'base_estudiante')
sys.path.insert(0, os.path.join(ADS, 'lote_3', 'caso'))
import diseno as X
R, D, MO = X.R, X.D, X.MO


# ------------------------------------------------------------------ mensajes (leídos del código)
def leer_mensajes():
    s = open(os.path.join(REF, 'src', 'mensajes.php'), encoding='utf8').read()
    return dict(re.findall(r"'((?:ME|MA|MV)-\d\d)' => '((?:[^'\\]|\\.)*)'", s))


MENSAJES_PHP = leer_mensajes()


def con_datos(cod, *datos):
    """Texto de un mensaje con sus datos, como mensaje() en PHP (%s y %d)."""
    t = MENSAJES_PHP[cod]
    for d in datos:
        t = re.sub(r'%[sd]', lambda m: str(d), t, count=1)
    return t


# Ejemplos de la Tabla 8.6 con los datos con que el diseño los escribió: el código tiene que reproducirlos.
EJEMPLOS_ME = {'ME-02': (2, 'estudiantes'), 'ME-03': ('EJ-0457', '12/03'), 'ME-04': ('09/03',)}

# Para qué sirve cada mensaje nuevo de la Unidad IV (MA: operaciones auxiliares; MV: validación de entradas).
USO_MENSAJE = {
    'MA-01': 'OA-01: alta de ejemplar registrada', 'MA-02': 'OA-01: código de ejemplar repetido',
    'MA-03': 'OA-01: la edición no existe', 'MA-04': 'OA-02: obra y edición registradas',
    'MA-05': 'OA-02 y OA-03: código ya usado', 'MA-06': 'OA-03: lector registrado',
    'MA-07': 'OA-04: lector corregido', 'MA-08': 'OP-06: lector o ejemplar inactivado',
    'MV-01': 'Falta un dato obligatorio', 'MV-02': 'Código con otro formato', 'MV-03': 'Estudiante sin curso (RI-06)',
    'MV-04': 'Docente con curso (RI-06)', 'MV-05': 'OP-01: el lector no existe', 'MV-06': 'OP-01: ejemplar dado de baja (RI-03)',
    'MV-07': 'OA-04 y OP-06: no existe o ya estaba inactivo', 'MV-08': 'Fecha imposible', 'MV-09': 'La base está ocupada',
    'MV-10': 'OP-02: devolución anterior a la salida', 'MV-11': 'OP-05: mes imposible', 'MV-12': 'Formulario vencido (ficha CSRF)',
}

# ------------------------------------------------------------------ operaciones auxiliares de la Unidad IV
# (código, nombre, pantalla, entradas, precondición, resultado, errores, requisitos, prueba, capítulo)
AUXILIARES = [
    ('OA-01', 'dar de alta un ejemplar', 'PT-08', 'Código del ejemplar, código de una edición ya cargada, cuenta.',
     'Rol de bibliotecaria (RNF-02).', 'Un ejemplar nuevo, activo, de esa edición. MA-01.',
     ['MV-01', 'MV-02', 'MA-03', 'MA-02', 'ME-13'], ['RF-07', 'RF-10', 'RNF-02'], 'PA-01', 10),
    ('OA-02', 'registrar una obra y su edición', 'PT-08', 'Código de obra, título y autor (si la obra es nueva), código de edición, editorial y año, cuenta.',
     'Rol de bibliotecaria.', 'La edición queda registrada, en una obra nueva o existente. MA-04.',
     ['MV-01', 'MV-02', 'MA-05', 'ME-13'], ['RF-07', 'RNF-02'], 'PA-02', 11),
    ('OA-03', 'registrar un lector', 'PT-08', 'Código, nombre, tipo y curso, cuenta.',
     'Rol de bibliotecaria.', 'Lector activo, con su tipo; curso solo si es estudiante (RI-06). MA-06.',
     ['MV-01', 'MV-02', 'MV-03', 'MV-04', 'MA-05', 'ME-13'], ['RF-06', 'RF-11', 'RNF-02', 'RNF-03'], 'PA-03', 11),
    ('OA-04', 'corregir un lector', 'PT-08', 'Código, nombre y curso nuevos, cuenta.',
     'Rol de bibliotecaria.', 'Nombre y curso corregidos; el código, el tipo y el historial no cambian (RI-08). MA-07.',
     ['MV-01', 'MV-03', 'MV-04', 'MV-07', 'ME-13'], ['RF-11', 'RNF-02'], 'PA-04', 11),
]
AUX = {a[0]: a for a in AUXILIARES}
PRUEBAS_AUX = [
    ('PA-01', 'OA-01', 'Dar de alta EJ-0800 en ED-0060, cerrar la conexión, volver a abrir la base y encontrarlo activo; rechazar el mismo código, un formato inválido, una edición inexistente y la cuenta de dirección.'),
    ('PA-02', 'OA-02', 'Registrar una obra nueva con su edición y una edición nueva de una obra existente; rechazar un código de edición repetido.'),
    ('PA-03', 'OA-03', 'Registrar un estudiante con curso y un docente sin curso; rechazar al estudiante sin curso y al docente con curso.'),
    ('PA-04', 'OA-04', 'Corregir el nombre y el curso de un estudiante y comprobar que sus préstamos anteriores conservan el curso que tenían.'),
]

# ------------------------------------------------------------------ incrementos y tareas (Capítulo 6, Tabla 6.3)
# (encuentro, tarea, operación, pantalla, requisitos, pruebas)
TAREAS = [
    (19, 'Preparar el entorno, instalar la base y registrar la versión 0.1', '—', '—', ['RS-01', 'RS-02'], ['E-1 a E-12']),
    (20, 'Alta de un ejemplar de punta a punta', 'OA-01', 'PT-08', ['RF-07', 'RF-10'], ['PA-01']),
    (21, 'Obras, ediciones y ejemplares', 'OA-02, OA-01', 'PT-08', ['RF-07'], ['PA-02']),
    (21, 'Inactivar un ejemplar sin perder su historial', 'OP-06', 'PT-08', ['RF-10'], ['P-10']),
    (22, 'Lectores: alta y corrección', 'OA-03, OA-04', 'PT-08', ['RF-11', 'RF-06'], ['PA-03', 'PA-04']),
    (22, 'Permisos por zona en cada pantalla y operación', 'todas', 'PT-03 a PT-09', ['RNF-02'], ['P-11']),
    (23, 'Préstamo con todas sus reglas', 'OP-01', 'PT-05', ['RF-01', 'RF-02', 'RF-04', 'RF-05', 'RF-06', 'RF-11'], ['P-01', 'P-02', 'P-05', 'P-06a', 'P-06b', 'P-07']),
    (24, 'Devolución única con historial', 'OP-02', 'PT-06', ['RF-03'], ['P-03']),
    (25, 'Consulta pública y préstamos activos', 'OP-03, OP-04', 'PT-01, PT-02, PT-07', ['RF-07', 'RF-08', 'RNF-03'], ['P-08', 'P-12', 'P-04']),
    (25, 'Informe mensual por curso', 'OP-05', 'PT-09', ['RF-09'], ['P-09']),
    (26, 'Integración, demostración y lista de incidencias', 'todas', 'todas', ['RS-01'], ['P-13']),
]

# ------------------------------------------------------------------ ficha de entorno (plan, §4)
# (código, qué se comprueba, cómo, qué se anota)
FICHA_ENTORNO = [
    ('E-1', 'Sistema operativo', 'En cada equipo: edición y versión de Windows (u otro) y si es de 32 o 64 bits. Se relevan, no se suponen.', 'Versión exacta por equipo'),
    ('E-2', 'Funcionamiento sin internet', 'Desconectar la red y hacer el recorrido de E-6a o E-6b.', 'Si todo funcionó desconectado (P-13)'),
    ('E-3', 'Sin costos obligatorios', 'Revisar la licencia de cada componente: intérprete, base de datos, navegador y editor.', 'Componente, versión, licencia y origen del instalador (P-15)'),
    ('E-4', 'Instalación reproducible', 'Un paquete fijo (carpeta con versiones anotadas, disponible sin conexión) y pasos numerados; instalar en un segundo equipo siguiendo solo la ficha.', 'Si el segundo equipo quedó igual sin ayuda; tiempo empleado'),
    ('E-5', 'Prueba mínima', 'php verificar_entorno.php en la carpeta que se va a usar.', 'Línea de resultado'),
    ('E-6a', 'Recorrido del prototipo docente completo', 'En referencia_docente/: consultar sin sesión, ingresar, dar de alta un ejemplar, prestar, intentar prestar el mismo ejemplar, devolver, ver el informe con la cuenta de dirección y salir; o bash pruebas/prueba_http.sh.', 'Si cada paso dio el resultado y el mensaje esperados'),
    ('E-6b', 'Comprobación de la base del estudiante', 'En base_estudiante/: bash pruebas/prueba_base.sh. Solo comprueba lo que la base trae preparado; no exige las operaciones que todavía construye el curso.', 'Línea de resultado'),
    ('E-7', 'Permisos del usuario de estudiante', 'Repetir E-5 y E-6b con la cuenta que usan los estudiantes, sin permisos de administrador.', 'Si funcionó; qué carpeta necesitó escritura'),
    ('E-8', 'Si hace falta administrador', 'Lo resuelve una sola vez el responsable técnico, antes del Encuentro 19.', 'Qué se hizo, quién y cuándo'),
    ('E-9', 'Antivirus y políticas', 'Comprobar que no bloquean el intérprete ni el puerto local.', 'Mensaje exacto si hubo bloqueo'),
    ('E-10', 'Ubicación de los datos', 'La carpeta datos/ en un disco local: no en una carpeta de red ni en un pendrive mientras el sistema funciona.', 'Ruta usada'),
    ('E-11', 'Respaldo', 'php respaldar.php y comprobar que el archivo existe.', 'Ruta y tamaño'),
    ('E-12', 'Restauración probada', 'Cargar un dato, restaurar el respaldo con php restaurar.php y comprobar que el estado es el del respaldo y que quedó la copia antes_de_restaurar.', 'Resultado'),
]
FICHA_LIBRO = ['E-1', 'E-2', 'E-5', 'E-6b', 'E-7', 'E-10', 'E-11', 'E-12']   # la versión breve del libro

# ------------------------------------------------------------------ alcance mínimo de producto (Work §7.2, textual)
# (función, resultado verificable (Work), cómo lo cumple el prototipo, operación, prueba)
ALCANCE = [
    ('Catálogo y ejemplares', 'Distingue la descripción bibliográfica del ejemplar físico y muestra su disponibilidad.',
     'Obra, edición y ejemplar separados; disponibles contados, no guardados', 'OA-01, OA-02, OP-03', 'PA-01, PA-02, P-08'),
    ('Lectores', 'Registra lectores ficticios mediante código interno, con los datos mínimos del caso.',
     'Código LE- y cuatro cifras; tipo y curso según RI-06; sin cédula', 'OA-03, OA-04', 'PA-03, PA-04'),
    ('Préstamo', 'Registra un ejemplar para un lector habilitado, con fecha de vencimiento y validación del servidor.',
     'OP-01 con RI-01 a RI-03, RI-07 y RI-08, en el servidor', 'OP-01', 'P-01, P-02, P-05, P-06a, P-06b, P-07'),
    ('Devolución', 'Cierra el préstamo correcto una sola vez y conserva su historial.',
     'Una sola sentencia sobre el préstamo activo del ejemplar; sin borrado', 'OP-02', 'P-03'),
    ('Consultas', 'Lista préstamos activos, vencidos y ejemplares disponibles.',
     'OP-04 con fecha de referencia; OP-03 pública', 'OP-03, OP-04', 'P-04, P-08'),
    ('Permisos', 'La consulta de catálogo no permite modificar préstamos; las operaciones requieren un rol autorizado.',
     'Consulta sin formularios de escritura; ME-13 en el servidor', 'todas', 'P-11, P-12'),
    ('Persistencia y entrega', 'Conserva información entre ejecuciones y puede instalarse y restaurarse siguiendo la guía.',
     'Persistencia comprobada; instalación y restauración seguras (la entrega es de la Unidad VI)', '—', 'PA-01, E-11, E-12'),
]

# ------------------------------------------------------------------ otro entorno: evidencias equivalentes (Work §7.5)
EVIDENCIAS_EQUIVALENTES = [
    ('Formularios', 'Las pantallas PT-01 a PT-09 con sus campos y mensajes.'),
    ('Validaciones del servidor', 'Cada entrada se valida al recibirla, aunque el navegador ya la haya validado (MV-01 a MV-12).'),
    ('Permisos', 'El rol se comprueba en el servidor en cada pedido: ME-13 sin cambiar datos; ME-12 solo en el ingreso.'),
    ('Transacciones', 'OP-01 es atómica: compara y registra sin que otro pedido escriba en el medio.'),
    ('Restricciones en la base', 'Un solo préstamo activo por ejemplar (RI-01) y historial sin borrado (RI-04, RI-05), protegidos por la base.'),
    ('Persistencia', 'Los datos siguen después de cerrar y volver a abrir el sistema.'),
    ('Consultas seguras', 'Consultas parametrizadas: una comilla en una entrada no altera la consulta.'),
    ('Pruebas', 'Las pruebas P-01 a P-13 que corresponden y PA-01 a PA-04, con su resultado registrado.'),
    ('Respaldo y restauración', 'Respaldo verificado y restauración que no destruye datos sin aviso.'),
]

# ------------------------------------------------------------------ concurrencia en Windows (decisión 6 de Fernando)
PROTOCOLO_CONCURRENCIA = [
    'La simultaneidad se prueba con dos o más procesos independientes, cada uno con su propia conexión a la base: php pruebas/prueba_carrera.php hace eso.',
    'No sirve como prueba abrir dos pestañas contra el servidor incorporado de PHP en Windows: atiende los pedidos de a uno y la carrera no ocurre.',
    'Se registra en la ficha: versión de Windows, de PHP y de SQLite, ubicación de la base, cantidad de rondas y el resultado de cada ronda.',
    'Si una ronda falla o no se puede ejecutar, se anota como pendiente con el mensaje exacto. No se declara aprobada.',
]

# ------------------------------------------------------------------ H4: banco de variantes (no están en el dossier, el buzón, D3, el banco del H3 ni las prácticas)
BANCO_H4 = [
    ('V4-1', 'La dirección decide que los estudiantes de 7.º grado puedan tener tres préstamos activos; los demás estudiantes siguen con dos.',
     'Parámetro nuevo por curso o regla en comprobar_prestamo (reglas de negocio); ME-02 con el máximo correcto; una prueba nueva junto a P-06a.'),
    ('V4-2', 'La bibliotecaria pide que el mensaje de un ejemplar inexistente muestre el código que se escribió.',
     'Plantilla de ME-05 en src/mensajes.php (presentación del mensaje) y la llamada en OP-01 y OP-02; la prueba compara el texto.'),
    ('V4-3', 'Los códigos de ejemplar de una donación grande van a tener cinco cifras (EJ-12345).',
     'Validación de OA-01 y restricción CHECK de la base (persistencia): las dos tienen que cambiar juntas; PA-01 con el formato nuevo.'),
    ('V4-4', 'El informe mensual tiene que poder pedirse también por un rango de dos meses.',
     'Entradas y validación de OP-05 (reglas de negocio), la consulta con dos fechas y P-09 con un rango.'),
    ('V4-5', 'Una devolución tiene que registrar también quién la recibió.',
     'Columna nueva en prestamos (persistencia) que no rompe el historial; OP-02 guarda la cuenta; prueba de que la devolución sigue siendo única.'),
]

# ------------------------------------------------------------------ registro de incidencias (formato; ejemplos ficticios del equipo modelo)
INCIDENCIAS = [
    ('IN-01', 'PT-07', 'Con fecha de referencia vacía, la pantalla mostró MV-08 sin decir qué fecha usar.', 'Media', 'Abierta', 'Unidad V'),
    ('IN-02', 'PT-08', 'El formulario de alta de lector no recuerda el tipo elegido después de un error.', 'Baja', 'Abierta', 'Unidad V'),
    ('IN-03', 'OP-05', 'En un mes sin préstamos el informe muestra solo el total 0, sin mensaje de vacío.', 'Baja', 'Abierta', 'Unidad V'),
]


def resultados_pruebas():
    """Resumen de la última ejecución de build/reproducir.py (con el entorno en que corrió)."""
    p = os.path.join(L4, 'resultados_pruebas', 'resumen.json')
    return json.load(open(p, encoding='utf8')) if os.path.exists(p) else None


def existe(cod):
    return (X.existe(cod) or cod in AUX or cod in dict((p[0], p) for p in PRUEBAS_AUX) or cod in MENSAJES_PHP
            or cod in dict((f[0], f) for f in FICHA_ENTORNO) or cod in dict((v[0], v) for v in BANCO_H4))
