# -*- coding: utf-8 -*-
"""Guía docente con solucionario del lote 5 (Unidad V, Capítulos 14 a 16): preparación de las copias descartables y del
cargador DP, procedimiento del conjunto reservado DR (solo la plantilla: los datos no se publican), referencia docente
v2 y v2 con SC-02 con sus diferencias, secuencia de cada encuentro en HC, claves de las actividades, prácticas y
evaluaciones, listas de cotejo, fragmentos de referencia que el libro no publica, rúbrica del H5 con evidencias,
planillas de registro y de recuperación, banco de variantes, calendario de 28 encuentros, resultados de las pruebas
con su entorno y procedencia de los recursos.
Los datos se leen de caso/verificacion.py, caso/datos_prueba_u5.py, caso/mbokaja_u5.py, del proyecto y de
resultados_pruebas/resumen.json (la ejecución real); no se copian."""
import os
import oficio as O
H, M, K = O.H, O.M, O.K
import piezas_u5 as Z
import diferencias as D
import cap14, cap15, cap16
V, DP, MB = cap14.V, cap14.DP, cap14.MB
L5 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ANCHO_SEC = [3.2, 2.4, 11.0]


def _r(texto):
    return texto.replace('Resultado: ', '')


# ---------------------------------------------------------------- 0. antes del Encuentro 27
COPIAS = [
    'Toda la unidad trabaja sobre copias descartables. El cargador (lote_5/proyecto/cargador_dp/cargar_dp.php) copia el '
    'código de una base, sin su carpeta datos/, a una carpeta nueva, y crea ahí una base con un conjunto de datos de prueba. '
    'La base de la clase, la del lote 4 y las referencias no cambian. Si la carpeta de destino ya existe, se niega y no cambia '
    'nada: para repetir una prueba se crea otra copia.',
    'Antes de copiar, el cargador comprueba el archivo de datos; después de cargar, compara el estado de la base con el '
    'esperado (obras, ejemplares, lectores, préstamos activos por lector y disponibles por obra) e informa «Estado esperado: '
    'correcto» y una huella SHA-256 de los datos. La huella es la misma en cualquier computadora y con cualquier base del '
    'curso: si la de un equipo es distinta, algo se cargó de otra forma y se averigua antes de probar.',
    'Las cuentas bibliotecaria1 y direccion1 de la copia reciben una clave al azar que el cargador muestra una sola vez (o '
    'la que se da con --clave=). La copia lleva un archivo COPIA_DESCARTABLE_DP.txt: los programas de prueba de la matriz '
    'se niegan a correr sobre una carpeta que no lo tenga, para no tocar nunca una base de trabajo.',
]
CARGA = (['Paso', 'Comando o acción', 'Qué se comprueba'],
         [['1', 'php cargar_dp.php --sistema=<base del equipo> --destino=<carpeta nueva>', '«Estado esperado: correcto» y la huella (sección 7)'],
          ['2', 'Carga manual de la Tabla 14.4 con las operaciones del equipo (OA-02, OA-01 dos veces, OA-03)', 'MA-04, MA-01, MA-01 y MA-06: la carga también es una prueba'],
          ['3', 'Matriz del equipo sobre la copia', 'Esperado escrito antes; obtenido, entorno y condición'],
          ['4', 'Al terminar, se borra la carpeta de la copia', 'La base de la clase no cambió']])

DR_PROCEDIMIENTO = [
    'El conjunto reservado DR es exclusivo del docente (decisión de Fernando). El repositorio del proyecto es público: por eso '
    'ni los datos de DR, ni la semilla con que se generan, ni sus resultados completos están en el repositorio ni en esta guía. '
    'Lo que se publica es la plantilla: la estructura del archivo y un generador, lote_5/caso/dr_plantilla.py, que no tiene '
    'datos.',
    'El docente genera su conjunto con una semilla propia, que no anota en ningún archivo público: python3 '
    'lote_5/caso/dr_plantilla.py --semilla=<privada> --salida=<carpeta fuera del repositorio>. El generador se niega a '
    'escribir dentro del repositorio y a sobrescribir un dr.json existente. Después de generar, carga DR en una copia de la '
    'referencia docente v2, ejecuta sus casos y deja el resultado en comprobacion_dr.txt, en la misma carpeta privada.',
    'La estructura de los casos es pública; los datos no. Lo que protege la revisión cruzada es que nadie conoce los códigos, '
    'los títulos, los cursos ni las fechas antes de la sesión. Conviene que el docente agregue, en su copia privada, uno o dos '
    'casos propios que no estén en la plantilla.',
    'En el Encuentro 30 el docente prepara, para cada equipo revisor, una copia del prototipo del otro equipo con DR: php '
    'cargar_dp.php --datos=<carpeta privada>/dr.json --sistema=<prototipo revisado> --destino=<copia>. Los casos se entregan '
    'impresos en el momento y se retiran al terminar. Las copias se borran después de la sesión. Ningún dato de DR se sube a '
    'un repositorio, a una carpeta compartida ni a una plataforma del curso.',
]
DR_PLANTILLA = (['Campo de dr.json', 'Qué contiene (sin datos)'],
                [['conjunto, parametros', 'Nombre del conjunto («no publicar») y los mismos parámetros de DP (plazo y máximos)'],
                 ['obras, ediciones', 'Cuatro obras con una edición cada una; códigos en un rango que no se cruza con DP ni con los lotes 1 a 4'],
                 ['ejemplares', 'Diez ejemplares, uno dado de baja con un préstamo en su historial'],
                 ['lectores', 'Dos estudiantes activos, una docente y un estudiante inactivo, con cursos elegidos al azar'],
                 ['prestamos, fecha_referencia', 'Tres préstamos activos (un estudiante en su máximo) y uno devuelto; fecha de referencia al vencimiento'],
                 ['esperado', 'El estado que el cargador comprueba después de cargar'],
                 ['casos', 'Ocho casos R-01 a R-08: un límite de RF-05, rechazos de RF-04, RF-06, RF-10, RF-03 y RNF-02, y dos casos normales']])

LABORATORIO = [
    'Antes del Encuentro 29, el docente confirma con Laboratorio que en los equipos se puede respaldar y restaurar una copia '
    '(E-11 y E-12 de la ficha de entorno). Si no se puede, la restauración se hace en la computadora preparada por el docente '
    'y se registra como pendiente del entorno en las demás.',
    'Antes del Encuentro 30, el docente decide si alguna persona de la biblioteca real participa de una sesión de uso. Solo '
    'con autorización de la institución, con la copia descartable y datos ficticios, sin fotografiar ni grabar caras ni '
    'pantallas con datos personales, y sin anotar su nombre. Si no hay autorización, las dos sesiones se hacen con '
    'compañeros en roles, que es la forma prevista.',
    'Las sesiones de uso de esta unidad no son la revisión de bocetos del Capítulo 8: se usa el sistema funcionando, con '
    'tareas nuevas que la persona no ensayó.',
]

DESCRIPCION_DIF = {
    'LEEME.txt': 'Línea de versión y aviso de que la referencia del lote 4 se conserva',
    'pruebas/prueba_in02.sh': 'Prueba nueva de IN-02 (siete comprobaciones por HTTP, base temporal)',
    'public/_plantilla.php': 'guardar_aviso() guarda lo escrito si falló; tomar_entradas(), valor() y elegido()',
    'public/lectores.php': 'El alta de lector envía lo escrito y lo vuelve a mostrar, con el tipo elegido',
    'pruebas/prueba_contratos.php': 'Tres comprobaciones nuevas de SC-02 (mes vacío y mes con préstamos)',
    'public/informe.php': 'PT-09 muestra la tabla solo si el mes tiene préstamos',
    'src/mensajes.php': 'Mensaje nuevo ME-14',
    'src/reglas.php': 'OP-05 responde ME-14, sin filas, si el mes no tiene préstamos',
}


def tabla_diferencias():
    filas = []
    for nueva, antes, titulo in D.PARES:
        for r, tipo, d in D.diferencias(antes, os.path.join(L5, 'proyecto', nueva)):
            mas = sum(1 for l in d if l.startswith('+') and not l.startswith('+++'))
            menos = sum(1 for l in d if l.startswith('-') and not l.startswith('---'))
            filas.append([nueva.replace('referencia_docente_', ''), r, DESCRIPCION_DIF.get(r, ''), '+%d / −%d' % (mas, menos)])
    return (['Versión', 'Archivo', 'Qué cambia', 'Líneas'], filas)


# ---------------------------------------------------------------- capítulo 14
SEC_C14 = [
    ('Encuentro 27 — Cobertura y datos independientes (5 HC de verificación)', [
        ['Problema y explicación', 'aprox. 1 HC', 'Apertura de la unidad y del capítulo. Sección 14.1 con la Tabla 14.1 y el Ejemplo resuelto 14.1. Sección 14.2 con la Tabla 14.2 y la Figura 14.1.'],
        ['Taller de pruebas', 'aprox. 3 HC', 'Tablas 14.3 y 14.4 y recuadro de la copia descartable. Cada equipo prepara su copia con el cargador y carga a mano la parte manual (Actividad 2). Ejemplo resuelto 14.2. Matriz del equipo escrita antes de ejecutar (Actividad 3).'],
        ['Revisión', 'aprox. 1 HC', 'Actividades 1 y 4 como plenario; el docente revisa que cada matriz tenga doce casos y seis límites o rechazos. Evidencia (Work, encuentro 27): matriz con resultados esperados y requisitos cubiertos.'],
    ]),
    ('Encuentro 28 — Ejecutar, registrar y reportar (5 HC de verificación)', [
        ['Problema y explicación', 'aprox. 1 HC', 'Sección 14.3 con las Tablas 14.5 y 14.6 y el Ejemplo resuelto 14.3. Actividad 1.'],
        ['Taller de pruebas', 'aprox. 3 HC', 'Cada equipo ejecuta su matriz sobre la copia, con consultas de control (Actividad 2). Sección 14.4 con la Tabla 14.7, la Figura 14.2 y las Tablas 14.8 y 14.9: cobertura y reportes de defecto (Actividad 3).'],
        ['Revisión', 'aprox. 1 HC', 'Actividad 4 y Desafío. Evidencia (Work, encuentro 28): resultados obtenidos e incidencias reproducibles. Práctica 14 en el nivel que indique el docente.'],
    ]),
]
CLAVES_E27 = [
    ['1', '(a) Normal. (b) Límite: un carácter especial en el borde de la búsqueda (C-13). (c) Rechazo: ME-01 y ningún dato cambia (C-07). (d) Excepción: una fecha imposible, MV-10 (C-11).', 'Clasificar (c) como excepción: es una operación que no se debe hacer, con su mensaje.'],
    ['2', 'La copia se crea con «Estado esperado: correcto» y la huella de la sección 7, la misma en todos los equipos. La parte manual da MA-04, MA-01, MA-01 y MA-06. Si un mensaje es otro, se anota tal cual y se revisa antes de seguir.', 'Cargar la parte manual en la base de la clase, o volver a usar una copia que ya tiene pruebas hechas.'],
    ['3', 'Doce casos o más, cada uno con identificador, requisito, clase, entradas y resultado esperado (mensaje y estado de los datos), escritos antes de ejecutar; seis o más de límite o de rechazo.', 'Casos sin requisito, o el esperado «que funcione».'],
    ['4', 'El sistema se construyó y se ajustó con esos datos: ya responde bien a ellos. Los datos independientes ponen a prueba lo que nadie miró, sobre todo los bordes. Además, los ejemplos del libro no tienen todos los casos de límite.', 'Responder que da lo mismo porque «los datos son ficticios».'],
]
CLAVES_E28 = [
    ['1', '(a) Comprobado. (b) Pendiente, con el motivo (no hay computadora sin red disponible). (c) Reproducido. (d) Simulado: es un dato de práctica.', 'Marcar (b) como comprobado «porque en casa anduvo».'],
    ['2', 'Cada caso con obtenido (mensaje exacto), entorno, condición y, si cambia datos, la consulta de control y su resultado.', 'Anotar «correcto» sin la consulta de control.'],
    ['3', 'La tabla de cobertura señala los requisitos sin caso y los que solo tienen casos normales; cada caso que no coincide tiene un reporte con pasos, esperado, obtenido, gravedad, entorno y condición.', 'Un reporte sin pasos, o sin la condición.'],
    ['4', 'Antes se revisa el requisito y el contrato (ME-02 es el del máximo; ME-04, el del préstamo registrado) y el estado de los datos (la huella de la copia y los préstamos activos del lector). Si el lector estaba en su máximo, el sistema tiene un defecto y se reporta. Cambiar el esperado para que coincida sería ocultarlo.', 'Cambiar el esperado.'],
    ['5', 'Respuesta abierta. Por ejemplo: RF-01, un préstamo a un lector que no existe (rechazo, con su mensaje y sin cambiar datos); RF-02, un préstamo del 28/05 que vence el 04/06 (límite: el vencimiento pasa de mes); RNF-03, buscar en la consulta pública el código de un lector (rechazo: no devuelve datos de lectores).', 'Casos sin esperado o de clase normal.'],
]
CLAVES_P14 = [
    ['Nivel 1', 'Ocho casos con requisito, clase, entradas y esperado. Deben estar, con los datos de la carga: el segundo préstamo de LE-0322 (EJ-0303: ME-04), el tercero (EJ-0304: ME-02, máximo de estudiantes), el ejemplar dado de baja (EJ-0305: MV-06) y EJ-0301 ya prestado (ME-03). Los obtenidos coinciden con los de la tabla comprobada de esta sección.'],
    ['Nivel 2', 'Doce casos o más, seis de límite o de rechazo, con MS-8: MB-30 se escribe tal cual y OA-01 responde MV-02. Con fecha de referencia 16/07, el sistema muestra EJ-0301 vencido (venció el 15, día de MS-7). No es un defecto: el sistema cumple RF-08 tal como está especificado. Es una necesidad que el catálogo no tiene (M-F12): falla la validación, no la verificación.'],
    ['Nivel 3', 'Cobertura contra MR-01 a MR-08 con los huecos señalados. Solicitud de cambio con el formato de SC-01: qué se pide (no contar como atraso un vencimiento en feriado), por qué (M-F12), requisitos afectados (RF-08 y un dato nuevo, los feriados), contrato de OP-04, pantalla para cargar feriados, pruebas que cambian (P-04 y los casos de vencimiento) y versión nueva.'],
]
COTEJO_P14 = [
    ['La copia se cargó con «Estado esperado: correcto» y la huella quedó anotada.', 'Indicador 3'],
    ['Cada caso tiene requisito, esperado escrito antes, obtenido, entorno y condición.', 'Indicador 4'],
    ['Hay al menos seis límites o rechazos (Nivel 2 o 3).', 'Indicador 2'],
    ['El feriado se trata como necesidad sin requisito (validación), no como defecto (Nivel 2 o 3).', 'Indicador 1'],
    ['La cobertura señala los huecos (Nivel 3).', 'Indicador 5'],
]
CRIT_C14 = [['8', '4: dos límites a los lados de TA-1 (1), dos rechazos de TA-2 o TA-3 (1), fuentes citadas (1), esperados con mensaje y estado (1).', 'Sin el punto de los límites si los dos casos están del mismo lado del borde.'],
            ['9', '4: pasos (1), esperado y obtenido (1), gravedad y entorno (1), condición (1).', 'Un punto por cada parte.']]
ERRORES_C14 = [
    ['Probar con los datos de los ejemplos', 'Datos independientes (DP) en una copia descartable'],
    ['Escribir el esperado después de ejecutar', 'Esperado escrito en la matriz antes de la primera ejecución'],
    ['Un solo caso por regla', 'Dos casos a los lados de cada borde'],
    ['Anotar «correcto» sin mirar los datos', 'Consulta de control del estado final'],
    ['Dar por buena una prueba que no se pudo hacer', 'Pendiente, con el motivo'],
    ['Llamar defecto a una necesidad que el catálogo no tiene', 'Verificar contra el requisito; validar contra la necesidad; solicitud de cambio'],
]

# ---------------------------------------------------------------- capítulo 15
SEC_C15 = [
    ('Encuentro 29 — Integración, permisos, persistencia y restauración (5 HC de verificación)', [
        ['Problema y explicación', 'aprox. 1 HC', 'Sección 15.1 con la Tabla 15.1. Sección 15.2 con la Tabla 15.2. Actividad 1.'],
        ['Taller de pruebas', 'aprox. 3 HC', 'Cada equipo ejecuta la Tabla 15.2 completa con su prototipo (Actividad 2), la prueba de persistencia entre procesos y la de restauración del Ejemplo resuelto 15.1 (Actividad 3).'],
        ['Revisión', 'aprox. 1 HC', 'Actividad 4. Registro con entorno y condición. Evidencia (Work, encuentro 29): evidencia del circuito completo y recuperación.'],
    ]),
    ('Encuentro 30 — Sesiones de uso y aceptación (5 HC: 1 de análisis y 4 de verificación)', [
        ['Sesiones de uso', 'aprox. 2 HC (verificación)', 'Sección 15.3, Tabla 15.3 y recuadro sobre la biblioteca real. Dos sesiones por equipo, con compañeros de otro equipo en roles distintos y tareas nuevas (Actividades 1 y 2).'],
        ['Revisión cruzada', 'aprox. 2 HC (verificación)', 'Práctica 15 con el conjunto reservado DR (sección 0.2), en copias preparadas por el docente.'],
        ['Aceptación y prioridades', 'aprox. 1 HC (análisis)', 'Sección 15.4, Tablas 15.4 y 15.5, Ejemplo resuelto 15.2: acta de aceptación y prioridad de las correcciones con lo observado (Actividades 3 y 4). Evidencia (Work, encuentro 30): observaciones de dos usuarios o roles y prioridades.'],
    ]),
]
CLAVES_E29 = [
    ['1', 'Respaldar (el respaldo existe y se verifica); registrar un préstamo nuevo (queda registrado); restaurar (pide confirmación y guarda una copia previa); buscar el préstamo (ya no está, porque el respaldo es anterior).', 'Restaurar sin haber hecho un cambio: no se comprueba nada.'],
    ['2', 'Diez operaciones con las tres cuentas. Cada rechazo es ME-13 y una consulta muestra que ningún dato cambió; la consulta pública responde sin sesión y no muestra lectores; con la cuenta permitida, la operación no responde ME-13 (y ME-12 queda solo para el ingreso).', 'Anotar solo el mensaje, sin comprobar los datos.'],
    ['3', 'Persistencia con dos procesos distintos (uno escribe y termina, otro busca) y restauración con los cuatro pasos, registradas con su entorno y su condición.', 'Comprobar la persistencia en el mismo proceso que escribió.'],
    ['4', 'No. Se registra comprobada en esa notebook, con su entorno, y pendiente en el laboratorio hasta que se haga allí (E-12).', 'Marcar E-12 como comprobada.'],
]
CLAVES_E30 = [
    ['1', '(a) Observación. (b) Opinión. (c) Observación. (d) Opinión.', 'Tratar (b) como evidencia de aceptación.'],
    ['2', 'Dos sesiones con roles distintos y tareas que la persona no ensayó; cada fila con lo que hizo, dónde se detuvo, la dificultad y el requisito. El observador no ayuda; las opiniones se anotan aparte.', 'Ayudar a la persona, o repetir las tareas del recorrido de prueba.'],
    ['3', 'Cada criterio con su evidencia y su estado (aceptado, no aceptado con el caso que falla, o pendiente con su motivo); prioridades por gravedad, frecuencia y requisito, y lo que es un pedido nuevo como solicitud de cambio.', 'Marcar «aceptado» un criterio sin caso ejecutado.'],
    ['4', 'No. El criterio queda pendiente y la versión candidata lo declara así, en sus límites conocidos. Si es imprescindible, el equipo no se declara aprobado en esa condición: se registra la recuperación (Capítulo 16).', 'Aceptarlo porque «seguro anda».'],
]
CLAVES_P15 = [
    ['Nivel 1', 'Cada caso de DR con la Tabla 15.6 completa. Los resultados esperados están en el archivo privado del docente (comprobacion_dr.txt, fuera del repositorio); sobre la referencia v2, todos coinciden. Cada diferencia con el prototipo revisado se reproduce dos veces antes de reportarla.'],
    ['Nivel 2', 'Tres casos propios de límite o de rechazo con los datos de DR (por ejemplo, el préstamo que completa el máximo de la docente, una devolución con fecha anterior a la salida o la búsqueda con un carácter especial), con su esperado escrito antes. Cada caso que no coincide tiene un reporte con su gravedad.'],
    ['Nivel 3', 'Prioridad de cada defecto recibido con gravedad, frecuencia y requisito (Tabla 15.5), con su justificación. Lo que se corrige en el Capítulo 16 y lo que queda como límite conocido, con el motivo (por ejemplo, poco impacto y una corrección que toca muchas pantallas).'],
]
COTEJO_P15 = [
    ['La copia se preparó con el cargador y la huella quedó anotada.', 'Indicador 1'],
    ['Cada caso tiene esperado, obtenido, entorno y condición.', 'Indicador 1'],
    ['Los defectos se reproducen antes de reportarse y el revisor no corrige.', 'Indicador 5'],
    ['Ningún dato reservado se copia fuera de la sesión.', 'Indicador 4'],
    ['Las prioridades se justifican con gravedad, frecuencia y requisito (Nivel 3).', 'Indicador 5'],
]
CRIT_C15 = [['8', '4: reservar una franja (1), intentar una reserva superpuesta (1), esperado con mensaje y sin cambios (1), consulta del estado final (1).', 'Sin el punto de la consulta si solo se mira el mensaje.'],
            ['9', '4: dos observaciones con su requisito (1 cada una), la opinión aparte (1), qué se hace con cada una (1).', 'Sin punto si la «observación» es una opinión.']]
ERRORES_C15 = [
    ['Probar la persistencia en el mismo proceso', 'Un proceso escribe y termina; otro busca'],
    ['Restaurar sin un cambio previo', 'Respaldar, cambiar, restaurar y comprobar que el cambio ya no está'],
    ['Probar los permisos solo desde el menú', 'Enviar la operación con cada cuenta: el servidor decide'],
    ['Ayudar a la persona en la sesión de uso', 'Observar y anotar dónde se detiene'],
    ['Usar datos de lectores reales en una sesión', 'Copia descartable con datos ficticios'],
    ['Aceptar un criterio sin evidencia', 'Pendiente, con el motivo'],
]

# ---------------------------------------------------------------- capítulo 16
SEC_C16 = [
    ('Encuentro 31 — Diagnosticar, corregir y volver a probar (5 HC: 2 de práctica y 3 de verificación)', [
        ['Diagnóstico', 'aprox. 1 HC (verificación)', 'Sección 16.1 con la Figura 16.1, la Tabla 16.1 y el Ejemplo resuelto 16.1: IN-02 se reproduce con prueba_in02.sh sobre el prototipo del lote 4. Actividad 1.'],
        ['Corrección', 'aprox. 2 HC (práctica)', 'Sección 16.2 con los Códigos 16.1 y 16.2. Cada equipo corrige su incidencia de mayor prioridad con el cambio mínimo (Actividad 2).'],
        ['Revisión y regresión', 'aprox. 2 HC (verificación)', 'Revisión entre pares con la Tabla 16.2; regresión con las Tablas 16.3 y el Ejemplo resuelto 16.2 (Actividad 3). Sección 16.3: SC-02 (Tablas 16.4 y 16.5, Código 16.3) y trazabilidad (Tabla 16.6). Actividad 4 y Desafío. Evidencia (Work, encuentro 31): registro de regresión y trazabilidad actualizada.'],
    ]),
    ('Encuentro 32 — Recuperación técnica y revisión de la Unidad V, H5 (5 HC: 2 de práctica, 1 de verificación y 2 de evaluación)', [
        ['Recuperación técnica', 'aprox. 2 HC (práctica)', 'Sección 16.4 y Tabla 16.7: cada equipo revisa las condiciones mínimas y usa este tiempo para recuperar la que le falte (Actividad 2). El docente registra la recuperación pendiente de quien no llegue (sección 4).'],
        ['Versión candidata', 'aprox. 1 HC (verificación)', 'Tabla 16.8, límites conocidos y versión en la bitácora (Actividades 1 y 3). Lista de verificación del H5.'],
        ['Revisión de la unidad (H5)', 'aprox. 2 HC (evaluación)', 'Presentación de la versión candidata con su evidencia, revisión con la rúbrica (sección 4) y un reporte del banco V5 para cada integrante, resuelto en forma individual. Se completa la planilla. Evidencia (Work, encuentro 32): H5, versión candidata con límites conocidos.'],
    ]),
]
CLAVES_E31 = [
    ['1', '(a) Síntoma. (b) Capa. (c) Causa.', 'Confundir la causa con el síntoma.'],
    ['2', 'Reproducción con pasos que se repiten; diagnóstico con síntoma, causa, capa e impacto (como la Tabla 16.1); corrección mínima; revisión de otro integrante con preguntas concretas, y lo que encontró.', 'Corregir sin reproducir, o revisar la propia corrección.'],
    ['3', 'La prueba nueva (pasa en la versión corregida y falla en la anterior), las pruebas de lo que el cambio toca y el núcleo P-01, P-03, P-07 y P-11, con resultado y entorno.', 'Correr solo la prueba nueva.'],
    ['4', 'La regla es correcta: un docente no lleva curso (RI-06, MV-04). Quitar la validación dejaría entrar datos mal cargados y no resolvería IN-02, que está en la presentación. Sería corregir algo que no estaba roto.', 'Aceptar la propuesta porque «el error desaparece».'],
    ['5', 'Respuesta abierta, con los campos de SC-02: quién y cuándo, qué se pide, por qué (la observación de la sesión), qué no es, requisitos, contrato y pantalla, mensaje, pruebas afectadas, decisión y versión nueva.', 'Escribir un defecto como si fuera un pedido de cambio.'],
]
CLAVES_E32 = [
    ['1', '(a) Pendiente del entorno. (b) Falla: el criterio no está aceptado; se corrige o se declara como límite conocido, con su condición. (c) Límite conocido.', 'Contar (a) como falla del equipo.'],
    ['2', 'Las seis condiciones de Work §4.3 con su evidencia y su estado. Si falta una, la planilla de recuperación: qué falta, qué evidencia hay, qué hay que hacer y quién lo hace.', 'Marcar comprobada una condición sin evidencia, o declarar aprobado al equipo con una condición faltante.'],
    ['3', 'Tabla de límites con condición y qué se hace; versión candidata identificada en la bitácora, con los aportes de cada integrante.', 'Ocultar un límite conocido.'],
]
CRIT_C16 = [['8', '4: síntoma con la fuente SO-3 (1), causa probable (1), capa (1), impacto con las pruebas de regresión (1).', 'Sin el punto de la capa si la ubica en la base sin haber comprobado el estado al recargar.'],
            ['9', '4: qué y por qué con SO-4 (1), reglas que cambian (1), pantalla y pruebas (1), versión nueva (1).', 'Sin el punto de la versión si reemplaza la anterior sin conservarla.']]
ERRORES_C16 = [
    ['Corregir sin reproducir', 'Reproducir con pasos que se repiten; si no se reproduce, pedir más información'],
    ['Cambiar una regla para que el error no aparezca', 'Buscar la causa en su capa; cambiar lo mínimo'],
    ['Revisar la propia corrección', 'Revisión de otro integrante con preguntas concretas'],
    ['Correr solo la prueba nueva', 'Regresión: lo que el cambio toca y el núcleo'],
    ['Tratar un pedido nuevo como defecto', 'Solicitud de cambio con su impacto y su versión'],
    ['Declarar aprobado a un equipo al que le falta una condición mínima', 'Registrar la recuperación y ofrecer el procedimiento'],
]

RUBRICA_EXPLICACION = [
    'El H5 se califica con la misma lógica que los hitos H1 a H4: para cada criterio se registran el nivel del producto del '
    'equipo y el nivel individual de cada integrante, y se combinan en la proporción 60 % (equipo) y 40 % (individual). Por '
    'ejemplo, con 4, 3, 2 y 1 puntos para Sólido, Logrado, En desarrollo e Inicial, un producto Logrado (3) con una evidencia '
    'individual En desarrollo (2) da 3 × 0,6 + 2 × 0,4 = 2,6. La conversión a calificación la decide la institución.',
    'La evidencia individual es la resolución de un reporte de defecto del banco V5, entregado por el docente durante la '
    'revisión, el aporte registrado en la bitácora y la observación del docente. El estudiante explica la causa probable, la '
    'capa, el impacto, la corrección mínima y las pruebas de regresión; no hace falta programarla en el momento. Los reportes '
    'del banco no están en el libro, en las prácticas ni en el conjunto reservado.',
    'La ausencia de evidencia se registra aparte («AE»), con la fecha acordada para entregarla; no se confunde con un desempeño '
    'de nivel Inicial. Una prueba que no se pudo ejecutar en la computadora del colegio se registra como pendiente del entorno, '
    'no como falla del equipo. La proporción 60/40 y los niveles son una propuesta editorial tomada del informe de Work '
    '(§4.3); no son una escala oficial del MEC.',
    'Las condiciones mínimas de aceptación de Work §4.3 son criterios del proyecto, no reglas automáticas de promoción. Si a '
    'un equipo le falta una, no se lo declara aprobado en esa condición: se registra la necesidad de recuperación y se le '
    'ofrece el procedimiento de la planilla siguiente, en el tiempo que la institución disponga (el Encuentro 32 prevé 2 HC de '
    'práctica). No se suponen horas extraordinarias de docentes ni de estudiantes que la institución no haya dispuesto. La '
    'instalación por otro equipo es evidencia de la Unidad VI.',
]
PROCEDIMIENTO_RECUPERACION = [
    '1. El docente marca la condición que falta en la planilla, con la evidencia que el equipo presentó.',
    '2. Acuerda con el equipo qué tiene que hacer para recuperarla (por ejemplo, la prueba de restauración con sus cuatro pasos) '
    'y qué evidencia tiene que entregar.',
    '3. La recuperación se hace en el tiempo que la institución disponga: las 2 HC de práctica del Encuentro 32 o, en la '
    'adaptación de 28 encuentros, el tiempo que la institución asigne. Si no hay tiempo asignado, queda registrada como '
    'pendiente, con su fecha prevista, y se informa a la coordinación.',
    '4. Cuando el equipo entrega la evidencia, el docente cambia el estado en la planilla y anota la fecha. Hasta entonces, la '
    'condición no se declara aprobada.',
]
CALENDARIO_28 = (['Encuentro (36)', 'Encuentro (28)', 'Qué se hace'],
                 [['27', '20', 'Sin cambios: cobertura y datos independientes (cargador DP, matriz).'],
                  ['28', '21', 'Sin cambios: ejecución, registro y reportes de defecto.'],
                  ['29', '22', 'Sin cambios: integración, permisos, persistencia y restauración (condiciones mínimas).'],
                  ['30', '23', 'Sin cambios: dos sesiones de uso, revisión cruzada con DR y acta de aceptación.'],
                  ['31 y 32', '24', 'Se unen (5 HC: 2 de práctica, 1 de verificación y 2 de evaluación). «Sin encuentro de reserva para recuperación técnica.» Se conservan las 2 HC del H5. Se prioriza la corrección de mayor prioridad con su regresión, las condiciones mínimas y la defensa; SC-02 y el Desafío pasan a lectura.']])
CALENDARIO_TEXTO = [
    'En la adaptación de 28 encuentros (distribución v2.1), la Unidad V pasa de seis a cinco encuentros y de 30 a 25 HC. Cada '
    'capítulo del libro tiene su recuadro «Si el calendario se acorta».',
    'Lo que no se reduce: las condiciones mínimas de aceptación, los doce casos con seis límites o rechazos, la ejecución con '
    'su registro, permisos, persistencia y restauración, las dos sesiones de uso, la corrección de mayor prioridad con su '
    'regresión y la defensa del H5. Lo que se reduce: los ejemplos resueltos 14.1 y 15.2, los niveles 3 de las prácticas, el '
    'ejemplo complementario SC-02 y el Desafío, que pasan a lectura.',
    'Como no hay encuentro de reserva, un equipo que no cumple una condición mínima no se declara aprobado: se registra la '
    'recuperación con la planilla de la sección 4 y se le ofrece el procedimiento, en el tiempo que la institución disponga. '
    'Cada cambio de alcance se anota en la bitácora del curso con la fecha y el motivo.',
]
PROCEDENCIA = (['Recurso', 'Procedencia', 'Derechos'],
               [['Texto de los Capítulos 14 a 16 y de la apertura de la unidad', 'Redacción original para este libro.', 'Propios del proyecto.'],
                ['Figuras 14.1, 14.2 y 16.1', 'Generadas con build/diagramas_u5.py sobre el lienzo de diagramas_u3.py; esquemas didácticos, sin notaciones ni símbolos nuevos.', 'Propias; sin recursos de terceros.'],
                ['Referencia docente v2 y v2 con SC-02', 'Copias de la referencia del lote 4 (que no se modifica) con la corrección de IN-02 y el cambio SC-02; diferencias en lote_5/proyecto/DIFERENCIAS_v2.md.', 'Propias.'],
                ['Cargador DP, matriz e integración', 'Escritos para este lote: lote_5/proyecto/cargador_dp y matriz.', 'Propios.'],
                ['Fragmentos de código del libro y de la guía', 'Leídos de los archivos del proyecto por build/fragmentos_u5.py; el verificador comprueba que coincidan, línea por línea.', 'Propios.'],
                ['Conjunto de prueba DP y casos C-01 a C-20', 'Inventados: lote_5/caso/datos_prueba_u5.py y verificacion.py. Resultados: ejecución real (build/reproducir.py).', 'Propios del proyecto.'],
                ['Conjunto reservado DR', 'Solo la plantilla (lote_5/caso/dr_plantilla.py). Los datos los genera el docente fuera del repositorio.', 'Propios; no se publican.'],
                ['Caso de práctica Mbokaja (Unidad V)', 'Inventado: lote_5/caso/mbokaja_u5.py, que amplía las fuentes de Mbokaja de los lotes 1 a 4.', 'Propio.'],
                ['Sesiones de uso del equipo modelo', 'Simulación del libro, rotulada como tal.', 'Propia.'],
                ['Capacidades, niveles de desempeño, proporción 60/40, secuencia de encuentros y condiciones mínimas', 'Informe de Work v0.1 (§4.2, §4.3, §5.1, §5.2, §6), como propuesta editorial.', 'No son documentos oficiales del MEC.']])


def tabla_p14():
    r = V.resumen()['practica_14']
    res = {c['id']: c for c in r['casos']}
    filas = []
    for c in MB.CASOS_P14:
        o = res[c[0]]
        obt = o['obtenido'].get('codigo') or ('EJ-0301 vencido' if c[0] == 'M-01' else '—')
        filas.append([c[0], c[1], '%s · %s' % (c[2], ' · '.join(c[4])), c[5] or 'Lista de vencidos', obt,
                      'Comprobado' if o['correcto'] else 'No coincide'])
    return (['Caso', 'Req.', 'Operación y entradas', 'Esperado', 'Obtenido', 'Condición'], filas)


def tabla_resultados():
    r = V.resumen()
    filas = []
    c = r['cargador_dp']
    filas.append(['Cargador DP', 'Carga sobre la v2 y sobre la base del estudiante; misma huella; se niega a sobrescribir',
                  'Correcto' if c['ok'] else 'Falla'])
    for v, nombre in (('v1_lote4', 'Prototipo del lote 4'), ('v2', 'Referencia v2'), ('v2_sc02', 'Referencia v2 con SC-02')):
        m = r['matriz'][v]
        filas.append([nombre, 'Matriz C-01 a C-20 con DP', '%d de %d coinciden' % (m['correctos'], m['total'])])
    filas.append(['Práctica 14', 'Carga de Mbokaja y casos M-01 a M-06 (v2)', '%d de %d coinciden' % (
        sum(1 for x in r['practica_14']['casos'] if x['correcto']), len(r['practica_14']['casos']))])
    filas.append(['IN-02', 'prueba_in02.sh sobre el lote 4 (tiene que fallar) y sobre la v2', '%s; %s' % (
        _r(r['in02']['lote4']), _r(r['in02']['v2']))])
    for v, nombre in (('v2', 'Regresión v2'), ('v2_sc02', 'Regresión v2 con SC-02')):
        for prueba, x in r['regresion'][v].items():
            filas.append([nombre, prueba, _r(x['resultado'])])
    for v, nombre in (('v1_lote4', 'Integración, lote 4'), ('v2', 'Integración, v2')):
        i = r['integracion'][v]
        filas.append([nombre, 'Permisos; persistencia entre procesos; restauración', '%s; %s; %s' % (
            _r(i['permisos']), 'correcta' if i['persistencia'] else 'falla', 'correcta' if i['restauracion'] else 'falla')])
    return (['Qué', 'Prueba', 'Resultado'], filas)


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
    r = V.resumen()
    doc = H.new_doc()
    Z.portada(doc, 'Guía docente con solucionario', estado)
    doc.add_heading('Guía docente — Lote 5', level=1)
    H.caja(doc, 'Sobre las capacidades y los resultados', [
        'Las capacidades de las fichas (C3, C6, C7, C8, C9 y C10 en esta unidad, y C8 y C9 en el H5) son propuestas para el '
        'programa institucional del Plan Optativo, tomadas del informe de Work. No son capacidades oficiales del MEC.',
        'Todos los resultados del equipo modelo que se informan corrieron en el entorno de construcción de este material '
        '(sección 7), no en las computadoras de ninguna institución ni en Windows. Las sesiones de uso del libro son una '
        'simulación rotulada. El material no está validado en aulas.'], tipo='neutra')
    H.p_texto(doc, 'Cada encuentro sigue la estructura de taller de Work: 1 HC de problema y explicación, 3 HC de práctica y '
                   '1 HC de revisión, con la distribución por categorías de la versión 2.1. En esta unidad casi todas las HC '
                   'son de verificación: el taller es diseñar, ejecutar y registrar pruebas. Los tiempos son aproximados y la '
                   'duración de la hora cátedra la fija cada institución.', italic=True, size=9.5)

    # 0. antes del Encuentro 27
    doc.add_heading('0. Antes del Encuentro 27: copias, datos de prueba y coordinación', level=2)
    doc.add_heading('0.1 Las copias descartables y el cargador DP', level=3)
    for t in COPIAS:
        H.p_texto(doc, t)
    M.tabla(doc, CARGA, [1.2, 8.6, 6.8], rotulo='Preparación de una copia con DP')
    H.p_texto(doc, 'Huella de DP en el entorno de construcción, igual desde la referencia v2 y desde la base del estudiante del '
                   'lote 4: %s.' % r['cargador_dp']['huella'], size=9.5)
    doc.add_heading('0.2 El conjunto reservado DR (exclusivo del docente)', level=3)
    for t in DR_PROCEDIMIENTO:
        H.p_texto(doc, t)
    M.tabla(doc, DR_PLANTILLA, [4.4, 12.2], rotulo='Plantilla de DR (estructura sin datos)')
    doc.add_heading('0.3 Coordinación con Laboratorio y sesiones de uso', level=3)
    for t in LABORATORIO:
        H.p_texto(doc, t)
    doc.add_heading('0.4 Referencia docente v2 y v2 con SC-02', level=3)
    H.p_texto(doc, 'La referencia docente del lote 4 queda como estaba. La corrección de IN-02 está en una copia nueva, '
                   'lote_5/proyecto/referencia_docente_v2, y el cambio aprobado SC-02, en otra copia sobre la v2, '
                   'referencia_docente_v2_sc02. Las dos se entregan solo al docente. El diff completo de cada archivo está en '
                   'lote_5/proyecto/DIFERENCIAS_v2.md; la regresión de las dos versiones, en la sección 7.')
    M.tabla(doc, tabla_diferencias(), [1.8, 5.0, 7.6, 2.2], rotulo='Archivos que cambian en las versiones v2', size=8.5)

    # 1 a 3. capítulos
    for n, (C_, sec, errores, bloques) in enumerate((
            (cap14, SEC_C14, ERRORES_C14, [('Encuentro 27', CLAVES_E27), ('Encuentro 28', CLAVES_E28)]),
            (cap15, SEC_C15, ERRORES_C15, [('Encuentro 29', CLAVES_E29), ('Encuentro 30', CLAVES_E30)]),
            (cap16, SEC_C16, ERRORES_C16, [('Encuentro 31', CLAVES_E31), ('Encuentro 32', CLAVES_E32)])), start=1):
        K.titulo_en_pagina_nueva(doc, '%d. %s — %s' % (n, C_.CAPITULO, C_.TITULO), nivel=2)
        M.ficha(doc, C_)
        _sec(doc, sec)
        _errores(doc, 'Errores frecuentes del %s' % C_.CAPITULO, errores)
        if C_ is cap16:
            H.p_texto(doc, 'Referencia para el docente: la corrección completa de IN-02 en la referencia v2. El libro muestra '
                           'solo lo necesario para entender la corrección (Códigos 16.1 y 16.2).', size=10)
            Z.codigo(doc, 'Referencia R-4')
            Z.codigo(doc, 'Referencia R-5')
            H.p_texto(doc, 'Referencia para el docente: el cambio SC-02 completo (mensaje y pantalla). El libro muestra la '
                           'regla (Código 16.3).', size=10)
            Z.codigo(doc, 'Referencia R-6')
            Z.codigo(doc, 'Referencia R-7')
        for enc, cl in bloques:
            _claves(doc, 'Claves de las actividades del %s' % enc, cl)
        if C_ is cap14:
            H.p_texto(doc, 'Práctica 14: la copia de práctica se carga con mbokaja_p14.json. Los casos siguientes se '
                           'comprobaron sobre una copia de la referencia v2 (resultados en la sección 7).', size=10)
            M.tabla(doc, tabla_p14(), [1.2, 1.4, 6.6, 2.6, 2.6, 2.2], rotulo='Práctica 14: casos comprobados', size=8.5)
            _niveles(doc, 'Práctica 14: claves por nivel', CLAVES_P14)
            _cotejo(doc, 'Lista de cotejo de la Práctica 14', COTEJO_P14)
        if C_ is cap15:
            H.p_texto(doc, 'Práctica 15: los datos y los casos los entrega el docente con DR (sección 0.2). Las claves de los '
                           'casos de DR están solo en su archivo privado; acá van los criterios.', size=10)
            _niveles(doc, 'Práctica 15: claves por nivel', CLAVES_P15)
            _cotejo(doc, 'Lista de cotejo de la Práctica 15', COTEJO_P15)
        if C_ is cap16:
            H.p_texto(doc, 'El Capítulo 16 no tiene práctica independiente: la actividad integradora es el H5 (sección 4).',
                      size=10)
        _eval(doc, C_, claves, {cap14: CRIT_C14, cap15: CRIT_C15, cap16: CRIT_C16}[C_])

    # 4. rúbrica H5
    K.titulo_en_pagina_nueva(doc, '4. Rúbrica del hito H5: evidencia de calidad y límites conocidos', nivel=2)
    for t in RUBRICA_EXPLICACION:
        H.p_texto(doc, t)
    M.tabla(doc, (['Criterio', '4. Sólido', '3. Logrado', '2. En desarrollo', '1. Inicial'],
                  [['%s (%s)' % (x[0], x[1])] + x[2] for x in cap16.RUBRICA_H5]),
            [2.8, 3.6, 3.4, 3.4, 3.4], rotulo='Rúbrica del H5: descriptores por nivel', size=8.5)
    M.tabla(doc, (['Criterio', 'Evidencia del equipo (60 %)', 'Evidencia individual (40 %)'],
                  [[x[0], x[3], x[4]] for x in cap16.RUBRICA_H5]), [4.4, 5.8, 6.4], rotulo='Evidencias de cada criterio del H5')
    M.tabla(doc, (['Nivel de desempeño', 'Descriptor común (Work §4.3)'], [list(x) for x in cap3.NIVELES_DESEMPENO]),
            [3.6, 13.0], rotulo='Niveles de desempeño (propuesta editorial)')
    M.tabla(doc, (['Estudiante (código)', 'Criterio', 'Nivel del equipo', 'Nivel individual', 'Resultado', 'AE'],
                  [['', x[0], '', '', '', ''] for x in cap16.RUBRICA_H5]),
            [3.0, 5.0, 2.2, 2.2, 2.2, 2.0], rotulo='Planilla de registro del H5 (una por estudiante)')
    M.tabla(doc, (['Condición (Work §4.3)', 'Evidencia', 'Estado', 'Recuperación'],
                  [[f[0], '', '', ''] for f in cap16.tabla_167()[1]]),
            [6.0, 4.4, 2.8, 3.4], rotulo='Planilla de condiciones mínimas (una por equipo)')
    doc.add_heading('Procedimiento de recuperación técnica', level=3)
    for t in PROCEDIMIENTO_RECUPERACION:
        H.p_texto(doc, t)
    M.tabla(doc, (['Equipo', 'Condición que falta', 'Qué hay que hacer', 'Evidencia por entregar', 'Fecha', 'Estado'],
                  [['', '', '', '', '', ''] for _ in range(3)]),
            [2.2, 3.4, 3.8, 3.4, 1.8, 2.0], rotulo='Planilla de recuperación')
    M.tabla(doc, (['Código', 'Reporte de defecto', 'Qué tiene que razonar el estudiante'], [list(v) for v in V.BANCO_H5]),
            [1.6, 7.0, 8.0], rotulo='Banco de variantes V5 para la evidencia individual del H5')
    H.p_texto(doc, 'Ninguno de estos reportes está en el libro, en las prácticas ni en el conjunto reservado. Se asigna uno por '
                   'integrante; si el curso trabaja con su propia biblioteca, el docente formula uno equivalente. V5-5 puede '
                   'no ser un defecto: se valora que el estudiante lo distinga.', italic=True, size=9.5)

    # 5. calendario, 6. diferencias con el plan, 7. resultados, 8. procedencia
    doc.add_heading('5. Calendario con menos encuentros', level=2)
    for t in CALENDARIO_TEXTO:
        H.p_texto(doc, t)
    M.tabla(doc, CALENDARIO_28, [2.6, 2.6, 11.4], rotulo='Unidad V en 36 y en 28 encuentros')
    doc.add_heading('6. Condición de cada resultado de la unidad', level=2)
    H.p_texto(doc, 'Lo que se presenta en el libro y en esta guía tiene una de cuatro condiciones (Tabla 14.5). Comprobado: la '
                   'matriz, la regresión, los permisos, la persistencia y la restauración, en el entorno de construcción. '
                   'Reproducido: IN-02 e IN-01 bis. Simulado: las sesiones de uso del equipo modelo y los datos de Mbokaja. '
                   'Pendiente: la prueba de campo en las computadoras del colegio y en Windows (E-1 a E-12, P-13, '
                   'concurrencia) y la instalación por otro equipo (Unidad VI).')
    doc.add_heading('7. Resultados de las pruebas y entorno en que corrieron', level=2)
    H.p_texto(doc, 'Entorno de todas las pruebas: %s. %s' % (V.entorno_texto(), r['entorno']['tipo']), size=10)
    M.tabla(doc, tabla_resultados(), [4.0, 7.0, 5.6], rotulo='Resultados de las pruebas (build/reproducir.py)', size=8.5)
    H.p_texto(doc, 'Los archivos de cada ejecución, con su entorno, están en lote_5/resultados_pruebas/. Estos resultados '
                   'valen para ese entorno; en las computadoras del colegio siguen pendientes hasta que se hagan allí.',
              italic=True, size=9.5)
    doc.add_heading('8. Procedencia y derechos de los recursos', level=2)
    M.tabla(doc, PROCEDENCIA, [4.4, 7.8, 4.4], rotulo='Inventario de recursos del lote')
    M.pegar_renglones(doc)
    Z.encadenar_inicio(doc)
    K.saltos_a_titulos(doc)
    H.finalizar(doc, ruta)
