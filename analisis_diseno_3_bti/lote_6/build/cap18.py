# -*- coding: utf-8 -*-
"""Capítulo 18 — «Demostrar, defender y aprender del proyecto» (Work §6: secciones 18.1 a 18.4 y cierre «Evaluación
integradora de la segunda etapa y cierre del proyecto»; encuentros 35 y 36).

Decisiones de Fernando (21-oct-2026): D-3, sin prueba escrita adicional (los instrumentos son la demostración, la
defensa individual y la evaluación integradora); D-4, sin práctica independiente; D-5, dos alternativas para el
Encuentro 35 y una planilla para calcular la duración, sin suponer un segundo evaluador; las variantes definitivas de
la defensa se reservan fuera del repositorio (solo los ejemplos son públicos). Recuperación sin horas extraordinarias.
Capacidades de Work §5.2: C1 a C10 (Encuentro 35) y C7, C9 y C10 (Encuentro 36)."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
L6 = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(L6, 'caso'))
import instrumentos_u6 as I
try:
    import construccion as C4
except ImportError:
    C4 = None

NUM = 18
UNIDAD = 'Unidad VI — Entregar y comunicar'
CAPITULO = 'Capítulo 18'
TITULO = 'Demostrar, defender y aprender del proyecto'
ENCUENTROS = (35, 36)
SECCIONES = ['18.1 Demostración organizada por requisitos y evidencias',
             '18.2 Defensa individual de decisiones y resolución de una variante',
             '18.3 Recuperación de aprendizajes pendientes',
             '18.4 Retrospectiva y mejoras futuras justificadas']
REVISION_WORK = 'Evaluación integradora de la segunda etapa y cierre del proyecto'
PRACTICA_WORK = None

ROTULO_CAPACIDAD = ('Capacidades propuestas para el programa institucional (C1 a C10 en el Encuentro 35; C7, C9 y C10 en '
                    'el Encuentro 36; no son capacidades oficiales del MEC)')
CAPACIDAD = ('En la demostración y la defensa (Encuentro 35) se ponen en juego las diez capacidades, C1 a C10.\n'
             'C7. Organiza y registra el trabajo colaborativo.\n'
             'C9. Verifica y mejora la solución a partir de evidencia.\n'
             'C10. Documenta, entrega y defiende el prototipo.')
TEMA = ('Demostración organizada por requisitos y evidencias, defensa individual de una decisión y una prueba, resolución '
        'de una variante y preguntas de transferencia. Recuperación de aprendizajes pendientes, retrospectiva con mejoras '
        'justificadas y evaluación integradora de la segunda etapa.')
INDICADORES = [
    'Demuestra el sistema con un guion que va de cada requisito imprescindible a su evidencia, en el tiempo acordado.',
    'Explica, solo, una decisión del proyecto y una prueba, con su evidencia.',
    'Resuelve una variante nueva: ubica el cambio en el requisito, el modelo, los contratos y las capas, y elige las pruebas.',
    'Comunica qué está aceptado, qué no y qué queda pendiente, sin exagerar ni ocultar.',
    'Propone mejoras futuras apoyadas en límites, incidencias u observaciones registradas, con su prioridad.',
]
TIEMPO = ('Dos encuentros de 5 HC (35 y 36 de la secuencia anual). Encuentro 35: 5 HC de evaluación (demostración y '
          'defensa). Encuentro 36: 3 HC de evaluación (recuperación) y 2 de gestión (retrospectiva y cierre).')

APERTURA = [
    'El proyecto está entregado. Falta mostrar qué se logró, con evidencia, y que cada integrante pueda explicar por qué el '
    'sistema es como es. Una demostración no es un paseo por las pantallas: es un recorrido por lo que la biblioteca pidió y '
    'por las pruebas que dicen que se cumplió.',
    'Después de la defensa, el año se cierra con dos tareas: recuperar lo que quedó pendiente y mirar hacia atrás para '
    'decidir, con evidencia, qué se haría distinto y qué se mejoraría.',
]
ARTICULACION = [
    'Con el Capítulo 4 y el catálogo v1.1: el guion de demostración se ordena por los requisitos imprescindibles.',
    'Con el Capítulo 9 (H3): como en la evaluación integradora de la primera etapa, se combinan el producto del equipo y la '
    'evidencia individual.',
    'Con los Capítulos 14 a 17: las evidencias de la demostración son las pruebas, la regresión y el acta de entrega.',
]
AVISO_ENTORNO = C4.AVISO_ENTORNO if C4 else ('Estado del entorno: no probado en la institución', [])

# ------------------------------------------------------------------ encuentro 35
E35_TITULO = 'Encuentro 35 — Demostración y defensa individual'

S181 = ('18.1 Demostración organizada por requisitos y evidencias', [
    'La demostración sigue un guion (Tabla 18.1): por cada requisito imprescindible, la evidencia que ya existe y qué se '
    'muestra en vivo. Tiene un tiempo fijo y el guion dice qué hacer si un paso falla: se dice y se muestra lo registrado, '
    'sin ocultarlo (Figura 18.1).',
    'Se muestran primero los requisitos que la biblioteca consideró imprescindibles y después los importantes. Lo que no se '
    'puede mostrar en vivo, como la restauración en el laboratorio, se presenta con su evidencia y su condición.',
])
TABLA_181_ROTULO = 'Tabla 18.1 — Guion de demostración del equipo modelo'
TABLA_181 = (I.GUION_CAMPOS, [list(g) for g in I.GUION_MODELO])
LEAD_FIG181 = 'La Figura 18.1 muestra cómo se arma cada paso del guion.'
EPI_FIG181 = 'Figura 18.1 — Un paso de la demostración: del requisito a la evidencia.'
EJ181 = ('Ejemplo resuelto 18.1: un paso que falla en vivo', [
    'Consigna: durante la demostración, el préstamo de RF-01 responde ME-02 en lugar de ME-04. ¿Qué hace el equipo?',
    'Lo dice: «el lector ya tenía dos préstamos en esta copia». Muestra la evidencia registrada de C-01 y su entorno, y '
    'sigue con el guion. Al terminar, revisa la copia: un integrante había hecho un préstamo de prueba antes.',
    'Lo que no hace: cambiar de lector sin decirlo, ni seguir como si nada. Mostrar un fallo con honestidad también es una '
    'evidencia de C10.',
])

S182 = ('18.2 Defensa individual de decisiones y resolución de una variante', [
    'En la defensa, cada estudiante explica solo una decisión del proyecto y una prueba, con su evidencia, y resuelve una '
    'variante nueva: un cambio acotado de una regla o de un requisito. No la programa: dice qué requisito cambia, qué capas '
    'toca, qué cambia en el modelo y en los contratos, y qué pruebas habría que agregar (Tabla 18.2).',
    'Las variantes de la defensa son reservadas: las entrega el docente en el momento. Para practicar están los ejemplos '
    'públicos, como el del Ejemplo resuelto 18.2. Al final, el docente puede hacer una pregunta de transferencia con otro '
    'proyecto escolar (Tabla 18.3).',
])
TABLA_182_ROTULO = 'Tabla 18.2 — Rúbrica de la defensa individual'
TABLA_182 = (['Criterio', '4. Sólido', '3. Logrado', '2. En desarrollo', '1. Inicial'],
             [['%s (%s)' % (c, cap)] + niveles for c, cap, niveles in I.RUBRICA_DEFENSA])
EJ182 = ('Ejemplo resuelto 18.2: una variante de práctica (ejemplo público, no se usa en la defensa)', [
    'Variante: «%s»' % I.V6_EJEMPLOS[0]['situacion'],
    'Qué cambia: %s' % I.V6_EJEMPLOS[0]['que_cambia'],
    'Capas: %s Modelo y contratos: %s' % (I.V6_EJEMPLOS[0]['capas'], I.V6_EJEMPLOS[0]['modelo_y_contratos']),
    'Pruebas: %s' % I.V6_EJEMPLOS[0]['pruebas'],
])
TABLA_183_ROTULO = 'Tabla 18.3 — Preguntas de transferencia (proyectos alternativos de Work §7.4)'
TABLA_183 = (['Proyecto', 'Pregunta'], [list(t) for t in I.TRANSFERENCIA])
ACT_E35 = [
    ('Ejercitá', [
        'Ordená el guion de tu equipo: escribí, para cada requisito imprescindible, la evidencia que ya tenés y qué vas a '
        'mostrar en vivo, como la Tabla 18.1.',
    ]),
    ('Resolvé', [
        'Resolvé estas dos variantes de práctica con la forma del Ejemplo resuelto 18.2:\n(a) «%s» (b) «%s»'
        % (I.V6_EJEMPLOS[1]['situacion'], I.V6_EJEMPLOS[2]['situacion']),
        'Elegí la decisión y la prueba que vas a explicar en tu defensa y escribí, para cada una, la evidencia que vas a mostrar.',
    ]),
]

# ------------------------------------------------------------------ encuentro 36
E36_TITULO = 'Encuentro 36 — Recuperación, retrospectiva y cierre'

S183 = ('18.3 Recuperación de aprendizajes pendientes', [
    'La planilla anual (Tabla 18.5) reúne, para cada estudiante, los hitos H1 a H6 y la defensa. Quien tiene una evidencia '
    'ausente, un criterio en nivel Inicial o una condición mínima sin cumplir recibe una ficha de recuperación acotada '
    '(Tabla 18.4), que resuelve en las 3 HC de evaluación del encuentro.',
    'El orden es el de la prioridad: primero las condiciones mínimas, después las evidencias ausentes y por último los '
    'criterios en nivel Inicial. Un pendiente del entorno no se recupera: es de la institución.',
])
TABLA_184_ROTULO = 'Tabla 18.4 — Fichas de recuperación'
TABLA_184 = (['Ficha', 'Cuándo se usa', 'Qué se pide', 'Evidencia', 'Prioridad'],
             [[c, cu, q, ev, str(p)] for c, cu, q, ev, p in I.FICHAS_RECUPERACION])
TABLA_185_ROTULO = 'Tabla 18.5 — Planilla anual de hitos (una por estudiante)'
TABLA_185 = (['Hito', 'Encuentro', 'Qué se evaluó', 'Nivel', 'AE', 'Recuperación'],
             [[h, str(e), q, '', '', ''] for h, e, _, q in I.PLANILLA_ANUAL])
RECUPERACION = ('Si algo no se recupera', I.REGLA_RECUPERACION)

S184 = ('18.4 Retrospectiva y mejoras futuras justificadas', [
    'En la retrospectiva, el equipo mira la bitácora del año y responde con evidencia: qué funcionó, qué no y por qué '
    '(Tabla 18.6). No se trata de opiniones («salió lindo»), sino de hechos registrados.',
    'Cada mejora futura tiene que apoyarse en algo que pasó: un límite conocido, una incidencia o una observación de uso, y '
    'llevar su prioridad. Es la «propuesta de continuidad» que pide Work: lo que haría el próximo equipo que tome el proyecto.',
])
TABLA_186_ROTULO = 'Tabla 18.6 — Retrospectiva del equipo modelo (simulación del libro)'
TABLA_186 = (I.RETRO_CAMPOS, [list(r) for r in I.RETRO_MODELO])
EJ183 = ('Ejemplo resuelto 18.3: de una opinión a una mejora justificada', [
    'Opinión: «habría que hacer el sistema más lindo».',
    'Pregunta: ¿qué evidencia hay? En la sesión S1 (Tabla 15.3), la bibliotecaria escribió el código del lector dos veces.',
    'Mejora justificada: que el formulario de préstamo conserve el lector después de un préstamo, para el segundo libro. '
    'Requisito: RNF-01. Prioridad: media. Prueba: dos préstamos seguidos al mismo lector.',
])
ACT_E36 = [
    ('Ejercitá', [
        'Clasificá cada anotación de una retrospectiva como hecho con evidencia u opinión:\n(a) «la regresión encontró un '
        'error antes de entregar»; (b) «el proyecto fue difícil»; (c) «la restauración no se probó en el laboratorio».',
    ]),
    ('Resolvé', [
        'Completá la retrospectiva de tu equipo como la Tabla 18.6, con al menos tres mejoras justificadas.',
    ]),
]

# ------------------------------------------------------------------ cierre: evaluación integradora
INTEGRADORA_TITULO = 'Evaluación integradora de la segunda etapa y cierre del proyecto'
INTEGRADORA_TEXTO = I.INTEGRADORA
TABLA_187_ROTULO = 'Tabla 18.7 — Rúbrica de producto final: aspectos y ponderación (propuesta editorial, Work §4.3)'
TABLA_187 = (['Aspecto', 'Peso', 'Evidencia principal', 'Capítulos'], [[a, '%d %%' % p, e, c] for a, p, e, c in I.PRODUCTO])
CIERRE = ('Cierre del proyecto', [
    'El cierre registra la versión final del paquete, la bitácora completa con los aportes de cada integrante y la '
    'propuesta de continuidad.',
    'El material y el sistema siguen siendo un prototipo educativo con datos ficticios: lo que no se probó en el laboratorio '
    'queda escrito como pendiente.',
])

REPASO = ('Para repasar', [
    'La demostración sigue un guion por requisitos y evidencias, con tiempo fijo; si algo falla, se dice y se muestra lo registrado.',
    'En la defensa, cada estudiante explica una decisión y una prueba, y resuelve una variante sin programarla.',
    'La recuperación sigue una prioridad; lo que no se recupera no se declara aprobado.',
    'La retrospectiva separa hechos de opiniones, y cada mejora se apoya en una evidencia.',
    'La evaluación integradora combina el H6, el producto final y la defensa individual.',
])
CALENDARIO = ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, los Encuentros 35 y 36 pasan a ser el 27 y el 28, sin cambios.',
    'El Encuentro 28 recibe también las recuperaciones técnicas de la Unidad V, que en esa versión no tienen encuentro de '
    'reserva. Se ordenan por la misma prioridad: condiciones mínimas, evidencias ausentes y nivel Inicial. La retrospectiva '
    'se condensa en la ficha del equipo; la defensa individual no se reduce.',
])

# El Capítulo 18 no tiene práctica independiente (D-4) ni prueba escrita adicional (D-3).
PRACTICA_TITULO = None
PRACTICA_INTRO = []
NIVELES = []
PRACTICA_CONTROL = None
EVAL_ID = None
EVAL_TITULO = None
EVAL_TEXTO_BASE = None
EVAL_ITEMS = []
EVAL_PUNTAJE = None
EVAL_FUENTES = {}
