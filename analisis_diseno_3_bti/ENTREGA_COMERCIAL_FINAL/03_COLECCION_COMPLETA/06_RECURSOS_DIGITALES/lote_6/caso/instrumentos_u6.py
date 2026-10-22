# -*- coding: utf-8 -*-
"""Instrumentos de la Unidad VI (fuente única para el libro, la guía y las planillas):
rúbrica del H6, guion de demostración, rúbrica de defensa individual, rúbrica de producto final, preguntas de
transferencia, planilla de tiempos del Encuentro 35 (decisión D-5), fichas de recuperación, planilla anual H1 a H6,
registro de retrospectiva y composición de la evaluación integradora de la segunda etapa.
Las proporciones (60/40 y la ponderación de Work §4.3) y los niveles son propuestas editoriales: la conversión a
calificación la decide la institución. Los ejemplos de variantes son públicos; el banco definitivo de la defensa está
fuera del repositorio (caso/v6_plantilla.py)."""
import os, sys, math
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import v6_plantilla as V6

# ------------------------------------------------------------------ H6 (Encuentro 34)
# (criterio, capacidad, [Sólido, Logrado, En desarrollo, Inicial], evidencia del equipo, evidencia individual)
RUBRICA_H6 = [
    ('Guía de instalación reproducible', 'C10',
     ['Otro equipo instala sin ayuda; cada paso tiene comando, resultado esperado y qué hacer si falla; los ajustes se volvieron a probar.',
      'Otro equipo instala con la guía; algún paso necesitó una aclaración que quedó corregida.',
      'La instalación necesitó ayuda del equipo autor en más de un paso.',
      'Sin guía, o la guía no permite instalar.'],
     'Guía, acta del equipo receptor y prueba de la propia guía', 'Paso de la guía que redactó o probó, según la bitácora'),
    ('Manual por tareas', 'C10',
     ['Tareas completas, con mensajes y qué hacer ante cada error; una persona ajena las sigue.',
      'Tareas principales con sus pasos y mensajes.',
      'Manual por pantallas o tareas incompletas.',
      'Sin manual.'],
     'Manual del paquete', 'Tarea que escribió'),
    ('Respaldo y restauración', 'C10',
     ['Documentados como tareas y comprobados por el equipo receptor, con la copia previa.',
      'Documentados y comprobados por el equipo autor.',
      'Documentados sin comprobar.',
      'Sin respaldo ni restauración.'],
     'Tareas y registro de la restauración', 'Explica qué protege la copia previa'),
    ('Procedencia y licencias', 'C7',
     ['Cada recurso con autor, licencia y fuente verificada según su versión; nada de origen desconocido; autoría de cada integrante.',
      'Ficha completa de los recursos que se entregan.',
      'Ficha incompleta o licencias sin verificar.',
      'Sin ficha, o recursos de origen desconocido.'],
     'Ficha de procedencia', 'Aportes registrados en la bitácora'),
    ('Coherencia del paquete', 'C10',
     ['Código, datos, pruebas y documentación de la misma versión; la inspección estática da 0 incoherencias y las pruebas en aislamiento pasan.',
      'Coherente, con alguna incoherencia menor corregida en el encuentro.',
      'Incoherencias que impiden usar parte del paquete.',
      'Paquete incompleto.'],
     'Lista de entrega y resultado de la inspección y de las pruebas', 'Incoherencia que encontró o corrigió'),
    ('Límites y pendientes declarados', 'C10',
     ['Límites conocidos y pendientes del entorno separados de las fallas, con lo que se hace en cada caso.',
      'Límites conocidos escritos.',
      'Límites incompletos.',
      'Límites ocultos.'],
     'Límites del paquete y acta de entrega', 'Distingue un límite de un pendiente del entorno'),
]

# ------------------------------------------------------------------ demostración (18.1)
GUION_CAMPOS = ['Requisito', 'Evidencia que ya existe', 'Qué se muestra en vivo', 'Si falla en vivo', 'Tiempo']
# guion del equipo modelo: requisitos imprescindibles del catálogo v1.1 con sus evidencias de los lotes 4 y 5
GUION_MODELO = [
    ('RF-01 y RF-02', 'C-01, C-02 (matriz, Tabla 14.6)', 'Préstamo válido y su vencimiento', 'Se muestra el resultado registrado de C-01', '1/10 de HC'),
    ('RF-04', 'C-06 y P-07 (prueba de pedidos simultáneos)', 'Segundo préstamo del mismo ejemplar: ME-03', 'Resultado de la prueba de carrera', '1/10 de HC'),
    ('RF-05', 'C-03 a C-05 (límites)', 'Estudiante en su máximo: ME-02', 'Resultado registrado de C-03', '1/10 de HC'),
    ('RF-03', 'C-09, C-10', 'Devolución y segunda devolución: ME-07 y ME-06', 'Resultado registrado de C-10', '1/10 de HC'),
    ('RNF-02', 'Permisos con las tres cuentas (Tabla 15.2)', 'Préstamo con la cuenta de dirección: ME-13', 'Tabla 15.2', '1/10 de HC'),
    ('RS-01', 'Guía ejecutada en una carpeta limpia (Tabla 17.6)', 'Instalación y restauración', 'Acta de entrega', '1/10 de HC'),
]

# ------------------------------------------------------------------ defensa individual (18.2)
RUBRICA_DEFENSA = [
    ('Explica una decisión', 'C5, C6',
     ['Explica la decisión, la alternativa descartada y su costo, con la evidencia.', 'Explica la decisión y por qué se tomó.',
      'Describe la decisión sin justificarla.', 'No puede explicar ninguna decisión del proyecto.']),
    ('Explica una prueba', 'C9',
     ['Explica qué comprueba, el esperado, el obtenido y qué haría si fallara.', 'Explica qué comprueba y su resultado.',
      'Nombra la prueba sin explicar qué comprueba.', 'No puede explicar ninguna prueba.']),
    ('Resuelve la variante', 'C3 a C8',
     ['Ubica el cambio en el requisito, el modelo, los contratos y las capas, y elige las pruebas y la regresión.',
      'Ubica el cambio y nombra las pruebas nuevas.', 'Ubica el cambio en una sola parte, sin pruebas.',
      'No ubica el cambio.']),
    ('Comunica aceptación y límites', 'C10',
     ['Dice qué está aceptado, qué no y qué queda pendiente, sin exagerar ni ocultar.', 'Dice qué está aceptado y sus límites.',
      'Omite límites importantes.', 'Presenta como probado lo que no se probó.']),
]
# preguntas de transferencia (Work §7.4: proyectos alternativos); se usan como pregunta oral, una por estudiante
TRANSFERENCIA = [
    ('Préstamo de equipos audiovisuales', '¿Qué regla de la biblioteca se conserva y cuál cambia si se prestan proyectores por período?'),
    ('Inscripción a talleres escolares', '¿Qué protección de RI-01 usarías para que no se supere el cupo de un taller?'),
    ('Gestión de solicitudes de soporte', '¿Qué parte del historial de préstamos se parece al historial de estados de una solicitud?'),
    ('Reserva de espacios escolares', '¿Qué prueba de límite harías para dos reservas que se tocan en el horario?'),
]

# ------------------------------------------------------------------ producto final (Work §4.3, ponderación editorial)
PRODUCTO = [  # (aspecto, peso, evidencia principal, capítulos)
    ('Problema y relevamiento', 15, 'Dossier, alcance y H1', '1 a 3'),
    ('Requisitos y trazabilidad', 20, 'Catálogo, matriz requisito-modelo-prueba y H2', '4 a 6'),
    ('Modelos y diseño', 20, 'Modelo de datos, pantallas, contratos y H3', '7 a 9'),
    ('Prototipo e integración', 20, 'Circuito funcional, persistencia y H4', '10 a 13'),
    ('Pruebas y mejora', 15, 'Matriz, regresión, límites y H5', '14 a 16'),
    ('Documentación y defensa', 10, 'Paquete de entrega, H6, demostración y defensa', '17 y 18'),
]
NIVELES_PRODUCTO = ['Cumple el criterio del hito con evidencia reproducible y lo mejoró con lo aprendido después.',
                    'Cumple el criterio del hito con evidencia suficiente.',
                    'Cumple en parte; tiene inconsistencias que requieren revisión.',
                    'No cumple todavía; la evidencia es insuficiente.']
INTEGRADORA = [
    'La evaluación integradora de la segunda etapa reúne tres evidencias: el H6 (Encuentro 34), la rúbrica de producto final '
    'y la defensa individual (Encuentro 35). Como en el H3, combina el producto del equipo y la evidencia individual.',
    'La rúbrica de producto usa los seis aspectos de la ponderación editorial de Work §4.3. En cada aspecto, 60 % es evidencia '
    'del producto del equipo y 40 %, evidencia individual (la defensa, la bitácora y la observación del docente).',
    'Es una propuesta editorial. La conversión a calificación y el régimen de promoción son de la institución. La ausencia de '
    'evidencia se registra aparte y no se confunde con un nivel Inicial; un pendiente del entorno no es una falla del equipo.',
]

# ------------------------------------------------------------------ planilla de tiempos del Encuentro 35 (D-5)
TIEMPOS_CAMPOS = [  # (clave, qué es, quién lo escribe)
    ('equipos', 'Cantidad de equipos', 'Docente'),
    ('estudiantes', 'Cantidad de estudiantes', 'Docente'),
    ('min_hc', 'Minutos de cada HC en la institución', 'Docente (no se supone)'),
    ('min_demo', 'Minutos por demostración de equipo', 'Docente'),
    ('min_cambio', 'Minutos de cambio entre equipos', 'Docente'),
    ('min_defensa', 'Minutos por defensa individual', 'Docente'),
    ('recuperaciones', 'Estudiantes con recuperación en el Encuentro 36', 'Docente'),
    ('min_recuperacion', 'Minutos por recuperación', 'Docente'),
]


VALIDACION = {  # entrada → mínimo permitido (entero); min_defensa > 0 evita la división por cero
    'equipos': 1, 'estudiantes': 1, 'min_hc': 1, 'min_demo': 1, 'min_cambio': 0, 'min_defensa': 1,
    'recuperaciones': 0, 'min_recuperacion': 0}


def validar_tiempos(**v):
    """Lista de problemas de los datos (vacía si son válidos): enteros, y positivos donde corresponde."""
    malos = []
    for k, minimo in VALIDACION.items():
        x = v.get(k)
        if isinstance(x, bool) or not isinstance(x, int) or x < minimo:
            malos.append('%s tiene que ser un entero mayor o igual que %d (se escribió %r)' % (k, minimo, x))
    return malos


def tiempos(equipos, estudiantes, min_hc, min_demo, min_cambio, min_defensa, recuperaciones, min_recuperacion):
    """Duración requerida y distribución, con un solo evaluador (no se supone un segundo evaluador).
    v1.1 (auditoría del lote 6): lo que pasa al Encuentro 36 se cuenta por defensas enteras —minutos trasladados =
    defensas trasladadas × minutos por defensa—, no por el déficit en minutos; y si las demostraciones solas superan el
    Encuentro 35, pasan al 36 todas las defensas y los minutos de demostración que no entraron."""
    v = dict(equipos=equipos, estudiantes=estudiantes, min_hc=min_hc, min_demo=min_demo, min_cambio=min_cambio,
             min_defensa=min_defensa, recuperaciones=recuperaciones, min_recuperacion=min_recuperacion)
    malos = validar_tiempos(**v)
    if malos:
        raise ValueError('; '.join(malos))
    demos = equipos * (min_demo + min_cambio)
    defensas = estudiantes * min_defensa
    requerido = demos + defensas
    disp35 = 5 * min_hc
    dif35 = disp35 - requerido
    demos_excedentes = max(0, demos - disp35)       # minutos de demostración que no entran en el 35
    if dif35 >= 0:
        pasan = 0
    elif demos_excedentes > 0:
        pasan = estudiantes                          # ninguna defensa entra en el 35
    else:
        pasan = math.ceil(-dif35 / min_defensa)      # defensas enteras: una defensa no se parte
    trasladados = pasan * min_defensa + demos_excedentes
    recup = recuperaciones * min_recuperacion
    disp36 = 3 * min_hc            # HC de evaluación del Encuentro 36 (las 2 de gestión son de la retrospectiva)
    dif36 = disp36 - recup - trasladados
    return {'demostraciones': demos, 'defensas': defensas, 'requerido_35': requerido, 'disponible_35': disp35,
            'diferencia_35': dif35, 'demostraciones_excedentes': demos_excedentes, 'defensas_que_pasan_al_36': pasan,
            'minutos_trasladados_al_36': trasladados, 'recuperaciones_36': recup, 'disponible_36': disp36,
            'diferencia_36': dif36,
            'alternativa': 'A' if dif35 >= 0 else ('B' if dif36 >= 0 else 'B + calendario institucional autorizado'),
            'minutos_sin_lugar': max(0, -dif36),
            'aviso': 'Las demostraciones solas superan el Encuentro 35' if demos_excedentes else ''}


# ejemplo con valores ficticios que el docente reemplaza (no es la duración de la HC de ninguna institución)
EJEMPLO_TIEMPOS = dict(equipos=6, estudiantes=24, min_hc=45, min_demo=12, min_cambio=3, min_defensa=6,
                       recuperaciones=5, min_recuperacion=15)
ALTERNATIVAS = [
    ('A', 'Todo en el Encuentro 35',
     'Si la planilla da diferencia positiva o cero: demostraciones en plenario con tiempo fijo y, después, las defensas '
     'individuales una por una. Mientras el docente toma una defensa, el resto del curso completa su ficha de '
     'retrospectiva (preparación del Encuentro 36, sin evaluación). Un solo evaluador.'),
    ('B', 'Defensas que continúan en el Encuentro 36',
     'Si el Encuentro 35 no alcanza: las defensas que faltan se toman al comienzo de las 3 HC de evaluación del Encuentro '
     '36, antes que las recuperaciones; se cuentan por defensas enteras. Las recuperaciones se ordenan por prioridad '
     '(condición mínima, evidencia ausente, '
     'nivel Inicial) en el tiempo que queda. Ninguna evidencia obligatoria se elimina.'),
    ('B+', 'Si tampoco alcanza el Encuentro 36',
     'Los minutos que la planilla da «sin lugar» se programan en el tiempo que la institución autorice dentro de su '
     'calendario, y se registran (qué estudiantes, qué evidencia, cuándo). No se suponen horas extraordinarias de '
     'docentes ni de estudiantes que la institución no haya dispuesto.'),
]
PREPARACION_35 = [
    'Guion de demostración de cada equipo, revisado en el Encuentro 34.',
    'Una variante del banco reservado por estudiante, impresa, y la pregunta de transferencia que le toca.',
    'Planilla de defensa individual y planilla anual H1 a H6, impresas o en la computadora del docente.',
    'Paquete de cada equipo instalado en la computadora de la demostración, con su copia de datos ficticios.',
    'Orden de las defensas y de las demostraciones, calculado con la planilla de tiempos.',
]

# ------------------------------------------------------------------ recuperación (18.3)
FICHAS_RECUPERACION = [  # (código, cuándo se usa, qué se pide, evidencia, prioridad)
    ('FR-1', 'Falta una condición mínima de aceptación (Work §4.3)',
     'La prueba o la corrección que falta, en una copia descartable, con su registro', 'Resultado con su entorno', 1),
    ('FR-2', 'Falta una evidencia individual (AE) de un hito',
     'La evidencia que faltó, en su forma más breve: explicar una decisión o una prueba del hito', 'Registro del docente', 2),
    ('FR-3', 'Un criterio quedó en nivel Inicial',
     'Una tarea acotada sobre ese criterio, con otra situación (por ejemplo, un ejemplo público de V6)', 'Resolución y nivel nuevo', 3),
    ('FR-4', 'La defensa individual no se pudo hacer',
     'La defensa con otra variante del banco reservado', 'Planilla de defensa', 2),
]
REGLA_RECUPERACION = [
    'La recuperación se hace en las 3 HC de evaluación del Encuentro 36, con este orden de prioridad: condiciones mínimas, '
    'evidencias ausentes, criterios en nivel Inicial.',
    'Lo que no se recupera no se declara aprobado: se registra qué falta, qué hay que hacer y cuándo, y se informa a la '
    'coordinación. No se suponen horas extraordinarias de docentes ni de estudiantes que la institución no haya dispuesto.',
    'Un pendiente del entorno (por ejemplo, la prueba en Windows) no es una falla del estudiante y no se recupera: se '
    'registra como pendiente de la institución.',
]
PLANILLA_ANUAL = [  # (hito, encuentro, capítulo, qué se evaluó)
    ('H1', 6, 3, 'Problema y alcance defendidos'),
    ('H2', 12, 6, 'Requisitos y modelos funcionales versionados'),
    ('H3', 18, 9, 'Dossier consistente y evidencia individual'),
    ('H4', 26, 13, 'Circuito funcional completo y lista de incidencias'),
    ('H5', 32, 16, 'Evidencia de calidad y límites conocidos'),
    ('H6', 34, 17, 'Paquete reproducible; ajustes finales'),
    ('Defensa', 35, 18, 'Rúbrica de producto y preguntas de transferencia'),
]

# ------------------------------------------------------------------ retrospectiva (18.4)
RETRO_CAMPOS = ['Qué', 'Evidencia', 'Por qué pasó', 'Mejora futura', 'Prioridad']
# retrospectiva del equipo modelo (simulación del libro): cada mejora se apoya en un límite, incidencia u observación real
RETRO_MODELO = [
    ('Funcionó: la regresión detectó a tiempo lo que el cambio podía romper', 'Tablas 16.3 y 16.5', 'Se ejecutó completa después de cada cambio', 'Mantener la regresión del núcleo en cada versión', '—'),
    ('No funcionó: los formularios de PT-08 pierden lo escrito después de un error', 'Tabla 16.8 (límite conocido)', 'La corrección de IN-02 se hizo solo en el alta de lector', 'Aplicar el mismo patrón a los demás formularios', 'Alta'),
    ('No funcionó: el mensaje de fecha vacía tiene un espacio doble', 'IN-01 bis (reproducido)', 'El mensaje se arma con un dato vacío', 'Mensaje propio para la fecha vacía', 'Baja'),
    ('Pendiente: nada se probó en Windows ni en el laboratorio', 'Tabla 17.6', 'El entorno de construcción es Linux', 'Prueba de campo con la ficha de entorno', 'Alta'),
]
RETRO_NOTA = ('La retrospectiva del equipo modelo es una simulación del libro, armada con sus límites reales. La de tu '
              'equipo sale de tu bitácora y de tus pruebas.')

V6_EJEMPLOS = V6.EJEMPLOS
V6_CAMPOS = V6.CAMPOS
