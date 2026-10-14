# -*- coding: utf-8 -*-
"""Configuración por grado de la edición diferencial. Capacidades: transcripción literal del programa MEC
(7.º: programa completo, págs. 55-57; 8.º: extracto oficial «Capacidades para el 8.º grado», pág. 54-56)."""
import os, sys
E = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, E + '../../7mo/build')
import curriculo as C7

BASE = E + '../base_candidata/'
PEC = E + 'fuente_pec/'

CAP7 = dict(C7.CAP)

# 8.º: transcripción literal de «Capacidades para el 8º grado» (programa MEC, págs. 54-56). Se conserva la grafía
# del original («cohersivas», «referente»); se omiten solo los dos puntos con que el programa introduce la lista de contenidos.
CAP8 = {
    1: 'Establece relaciones armónicas con los integrantes de la comunidad educativa.',
    2: 'Interpreta los criterios de evaluación a ser considerados en este nivel educativo.',
    3: 'Plantea actividades relacionadas al PEI que permitan desarrollar el sentido de pertenencia y el progreso institucional.',
    4: 'Descubre características psicológicas y emocionales de su persona según la etapa evolutiva.',
    5: 'Toma conciencia de su individualidad y singularidad para lograr conocimiento y aceptación de sí mismo.',
    6: 'Identifica habilidades para la construcción de su identidad personal.',
    7: 'Determina la importancia de los estados afectivos para un relacionamiento positivo consigo mismo y con los demás.',
    8: 'Toma conciencia de su sexualidad como parte esencial de su desarrollo integral.',
    9: 'Identifica características de relaciones violentas y cohersivas en el noviazgo.',
    10: 'Identifica las influencias de adicciones y estilos o tendencias de grupos sociales en el desarrollo personal.',
    11: 'Valora la importancia de la afectividad para un desarrollo personal armónico.',
    12: 'Investiga sobre los Derechos Humanos referente a la educación de los niños, las niñas y los adolescentes.',
    13: 'Analiza los derechos y obligaciones de los/as docentes.',
    14: 'Reconoce casos de vulnerabilidad de Derechos y los procedimientos para realizar denuncias.',
    15: 'Comprende la importancia de conformar organizaciones estudiantiles como proceso de establecimiento gradual de una cultura cívica democrática.',
    16: 'Participa activamente en las organizaciones estudiantiles de su institución educativa',
    17: 'Toma conciencia sobre la importancia del proceso de enseñanza–aprendizaje como parte de su desarrollo personal y profesional.',
    18: 'Planifica adecuadamente su tiempo para el estudio.',
    19: 'Practica medidas de prevención, mitigación y atención en situaciones de riesgos físicos y psicológicos en la vida escolar y familiar',
    20: 'Elabora proyectos sobre prevención y mitigación de riesgo para el contexto escolar',
}

GRADOS = {
 '7': dict(
    carpeta='7mo', grado='7.º',
    base_tomo=BASE + '7mo/DPS_7mo_TOMO_INTEGRAL_PEC_OFICIO_2026.docx',
    base_pa=BASE + '7mo/DPS_7mo_PLAN_ANUAL_PEC_OFICIO_2026.docx',
    base_planes=BASE + '7mo/DPS_7mo_PLANES_DE_CLASE_PEC_OFICIO_2026.docx',
    base_sol=BASE + '7mo/DPS_7mo_SOLUCIONARIO_DOCENTE_PEC_OFICIO_2026.docx',
    nombre_tomo='DPS_7mo_TOMO_INTEGRAL_PEC_OFICIO_2026',
    nombre_pa='DPS_7mo_PLAN_ANUAL_PEC_OFICIO_2026',
    nombre_planes='DPS_7mo_PLANES_DE_CLASE_PEC_OFICIO_2026',
    nombre_sol='DPS_7mo_SOLUCIONARIO_DOCENTE_PEC_OFICIO_2026',
    pec_tomo=os.environ.get('PEC_TOMO_7', PEC + 'pec7_tomo.md'), pec_sol=PEC + 'pec7_sol.md',
    CAP=CAP7,
    unidad_caps={1: [1, 2], 2: [3, 4], 3: [5, 6, 7], 4: [8, 9, 10], 5: [11, 12, 13, 14], 6: [15, 16], 7: [17, 18]},
    # capacidad(es) literal(es) de cada una de las 21 fichas de clase, en orden
    caps_clase=[[1], [2], [1], [3], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13, 14], [15], [16], [16], [17], [18], [3, 10]],
    tomo_reemplazos=[
        ('Las siete evaluaciones de unidad se trabajan como encuentros propios, y seis continuaciones prácticas permiten profundizar contenidos sin apurar las clases temáticas.',
         'Las siete evaluaciones de unidad se trabajan como encuentros propios. Además, el área tiene un segundo componente, el Proyecto Educativo Comunitario: en seis talleres, tu grado va a detectar una necesidad de la escuela, planificar un proyecto, llevarlo a cabo con autorización, evaluarlo y compartir lo aprendido. Las actividades complementarias de algunas unidades sirven para profundizar cuando haya tiempo.'),
        ('En 2026, el MINNA y el MITIC impulsan un proyecto de ley para proteger a los niños, niñas y adolescentes en los entornos digitales. Si sufrís',
         'En Paraguay hay servicios gratuitos de orientación para niños, niñas y adolescentes. Si sufrís'),
    ] + [('Continuación práctica %d — ' % k, 'Actividad complementaria %d (opcional) — ' % k) for k in range(1, 7)],
    portada_lema='La escuela como una comunidad',
    talleres={'A': (4, [1, 2]), 'B': (21, [1, 14]), 'C': (23, [8, 14]), 'D': (26, [11, 14]), 'E': (29, [17, 14]), 'F': (32, [4, 1])},
    pa_reemplazos=[
        ('21 clases temáticas + 7 evaluaciones de unidad + 6 talleres PEC articulados con las continuaciones prácticas del tomo + 2 integradoras',
         '21 clases temáticas (Orientación Educacional y Vocacional) + 6 talleres del Proyecto Educativo Comunitario (encuentros 4, 21, 23, 26, 29 y 32) + 7 evaluaciones de unidad + 2 integradoras = 36 encuentros. Las continuaciones prácticas del tomo quedan como actividades complementarias opcionales.'),
        ('Las seis continuaciones prácticas originales permanecen en el tomo como material de apoyo y refuerzo de Orientación;',
         'Las seis continuaciones prácticas originales permanecen en el tomo como «actividades complementarias (opcionales)» de apoyo y refuerzo de Orientación;'),
    ],
    pa_pec_generico={
        'A': 'Taller PEC A — Mirar antes de actuar. Diagnóstico participativo de necesidades. Vinculado a la unidad de Orientación correspondiente.',
        'B': 'Taller PEC B — Elegir con razones. Priorización y fundamentación del problema. Vinculado a la unidad de Orientación correspondiente.',
        'C': 'Taller PEC C — Pasar de la idea al plan. Objetivos, beneficiarios y productos. Vinculado a la unidad de Orientación correspondiente.',
        'D': 'Taller PEC D — Organizar para cumplir. Cronograma, roles, recursos y autorizaciones. Vinculado a la unidad de Orientación correspondiente.',
        'E': 'Taller PEC E — Actuar y registrar. Ejecución segura y bitácora. Vinculado a la unidad de Orientación correspondiente.',
        'F': 'Taller PEC F — Aprender de los resultados. Evaluación, informe y devolución. Vinculado a la unidad de Orientación correspondiente.',
    },
    # (tipo, capacidades) por plan 1..36: C clase, P taller PEC, E evaluación de unidad, I integradora
    plan_caps={1: ('C', [1], 0), 2: ('C', [2], 0), 3: ('C', [1], 0), 4: ('P', [1, 2], 0), 5: ('E', [1, 2], 0), 6: ('C', [3], 0), 7: ('C', [3], 0),
               8: ('C', [4], 0), 9: ('E', [3, 4], 0), 10: ('C', [5], 0), 11: ('C', [6], 0), 12: ('C', [7], 0), 13: ('E', [5, 6, 7], 0),
               14: ('C', [8], 0), 15: ('C', [9], 0), 16: ('C', [10], 0), 17: ('E', [8, 9, 10], 0), 18: ('I', list(range(1, 11)), 0),
               19: ('C', [11], 0), 20: ('C', [12], 0), 21: ('P', [1, 14], 0), 22: ('C', [13, 14], 0), 23: ('P', [8, 14], 0),
               24: ('E', [11, 12, 13, 14], 0), 25: ('C', [15], 0), 26: ('P', [11, 14], 0), 27: ('C', [16], 0), 28: ('C', [16], 0),
               29: ('P', [17, 14], 0), 30: ('E', [15, 16], 0), 31: ('C', [17], 0), 32: ('P', [4, 1], 0), 33: ('C', [18], 0),
               34: ('C', [3, 10], 0), 35: ('E', [17, 18], 0), 36: ('I', list(range(11, 19)), 0)},
    planes_reemplazos=[('(articulado con la unidad correspondiente)', '(componente Proyecto Educativo Comunitario)'),
        ('21 clases temáticas + 7 evaluaciones de unidad + 6 talleres PEC articulados con las continuaciones prácticas del tomo + 2 evaluaciones integradoras',
         '21 clases temáticas + 6 talleres del Proyecto Educativo Comunitario + 7 evaluaciones de unidad + 2 evaluaciones integradoras'),
        ('Los seis talleres PEC reemplazan en esta planificación las seis continuaciones prácticas de los encuentros 4, 21, 23, 26, 29, 32.',
         'Los seis talleres PEC ocupan los encuentros 4, 21, 23, 26, 29 y 32; las continuaciones prácticas del tomo quedan como actividades complementarias opcionales, sin encuentro propio.')],
    planes_cierre_pec={
        'A': 'Completar Ficha 1: mapa de necesidades y fuentes de evidencia.',
        'B': 'Escribir una fundamentación de cinco a ocho líneas.',
        'C': 'Consultar cómo se vincula la propuesta con el PEI y las capacidades del área.',
        'D': 'Preparar cuadro de recursos disponibles, faltantes y alternativas de costo cero.',
        'E': 'Ante cambios, documentar la causa y acordar ajustes con el docente.',
        'F': 'Preparar una presentación de tres minutos para el colegio.',
    },
    sol_reemplazos=[('Orientaciones para las continuaciones prácticas', 'Orientaciones para las actividades complementarias (opcionales)')]
                   + [('Continuación %d — ' % k, 'Actividad complementaria %d — ' % k) for k in range(1, 7)],
 ),
}
G7 = GRADOS['7']
GRADOS['8'] = dict(
    carpeta='8vo', grado='8.º',
    base_tomo=BASE + '8vo/DPS_8vo_TOMO_INTEGRAL_PEC_OFICIO_2026.docx',
    base_pa=BASE + '8vo/DPS_8vo_PLAN_ANUAL_PEC_OFICIO_2026.docx',
    base_planes=BASE + '8vo/DPS_8vo_PLANES_DE_CLASE_PEC_OFICIO_2026.docx',
    base_sol=BASE + '8vo/DPS_8vo_SOLUCIONARIO_DOCENTE_PEC_OFICIO_2026.docx',
    nombre_tomo='DPS_8vo_TOMO_INTEGRAL_PEC_OFICIO_2026',
    nombre_pa='DPS_8vo_PLAN_ANUAL_PEC_OFICIO_2026',
    nombre_planes='DPS_8vo_PLANES_DE_CLASE_PEC_OFICIO_2026',
    nombre_sol='DPS_8vo_SOLUCIONARIO_DOCENTE_PEC_OFICIO_2026',
    pec_tomo=PEC + 'pec8_tomo.md', pec_sol=PEC + 'pec8_sol.md',
    CAP=CAP8,
    unidad_caps={1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9, 10, 11], 4: [12, 13, 14], 5: [15, 16], 6: [17, 18], 7: [19, 20]},
    # 27 fichas en orden: 21 clases y 6 continuaciones (que pasan a actividades complementarias)
    caps_clase=[[1], [2], [3], [4], [5], [6], [7], [8], [9], [10, 11], [12], [13], [14],
                [15], [15],          # Clase 14, Actividad complementaria 1
                [15], [15],          # Clase 15, Actividad complementaria 2
                [16], [16],          # Clase 16, Actividad complementaria 3
                [17], [17],          # Clase 17, Actividad complementaria 4
                [18], [18], [18],    # Clases 18 y 19, Actividad complementaria 5
                [19], [19],          # Clase 20, Actividad complementaria 6
                [20]],               # Clase 21
    tomo_reemplazos=[
        ('En esta edición, las siete evaluaciones de unidad se trabajan como encuentros propios y seis continuaciones prácticas profundizan las Unidades 5 a 7.',
         'En esta edición, las siete evaluaciones de unidad se trabajan como encuentros propios. Además, el área tiene un segundo componente, el Proyecto Educativo Comunitario: en seis talleres, tu grado va a detectar una necesidad de la escuela, planificar un proyecto, llevarlo a cabo con autorización, evaluarlo y compartir lo aprendido. Las actividades complementarias de las Unidades 5 a 7 sirven para profundizar cuando haya tiempo.'),
        ('esta continuación permite', 'esta actividad complementaria permite'),
    ] + [('Continuación práctica %d — ' % k, 'Actividad complementaria %d (opcional) — ' % k) for k in range(1, 7)],
    portada_lema='La escuela y su comunidad cercana',
    talleres={'A': (20, [3, 1]), 'B': (22, [3, 6]), 'C': (24, [3, 20]), 'D': (27, [20, 16]), 'E': (30, [19, 20]), 'F': (33, [20, 2])},
    pa_reemplazos=[
        ('Las seis continuaciones prácticas originales permanecen en el tomo como material de apoyo y refuerzo de Orientación;',
         'Las seis continuaciones prácticas originales permanecen en el tomo como «actividades complementarias (opcionales)» de apoyo y refuerzo de Orientación;'),
        ('las metas del PEC son indicadores didácticos editoriales', 'las metas del PEC son indicadores didácticos de elaboración editorial.'),
        ('Proyecto modelo del grado: Patio seguro: prevención y convivencia.', 'Proyecto modelo del grado: «Patio seguro: campaña de prevención y convivencia».'),
    ],
    pa_pec_generico=G7['pa_pec_generico'],
    plan_caps={1: ('C', [1], 0), 2: ('C', [2], 0), 3: ('C', [3], 0), 4: ('E', [1, 2, 3], 0), 5: ('C', [4], 0), 6: ('C', [5], 0), 7: ('C', [6], 0),
               8: ('E', [4, 5, 6], 0), 9: ('C', [7], 0), 10: ('C', [8], 0), 11: ('C', [9], 0), 12: ('C', [10, 11], 0), 13: ('E', [7, 8, 9, 10, 11], 0),
               14: ('C', [12], 0), 15: ('C', [13], 0), 16: ('C', [14], 0), 17: ('E', [12, 13, 14], 0), 18: ('I', list(range(1, 15)), 0),
               19: ('C', [15], 0), 20: ('P', [3, 1], 0), 21: ('C', [15], 0), 22: ('P', [3, 6], 0), 23: ('C', [16], 0), 24: ('P', [3, 20], 0),
               25: ('E', [15, 16], 0), 26: ('C', [17], 0), 27: ('P', [20, 16], 0), 28: ('C', [18], 0), 29: ('C', [18], 0), 30: ('P', [19, 20], 0),
               31: ('E', [17, 18], 0), 32: ('C', [19], 0), 33: ('P', [20, 2], 0), 34: ('C', [20], 0), 35: ('E', [19, 20], 0), 36: ('I', list(range(15, 21)), 0)},
    planes_reemplazos=G7['planes_reemplazos'][:2] + [
        ('Los seis talleres PEC reemplazan en esta planificación las seis continuaciones prácticas de los encuentros 20, 22, 24, 27, 30, 33.',
         'Los seis talleres PEC ocupan los encuentros 20, 22, 24, 27, 30 y 33; las continuaciones prácticas del tomo quedan como actividades complementarias opcionales, sin encuentro propio.'),
        ('Los materiales originales de continuación práctica que permanecen en el tomo', 'Las actividades complementarias (opcionales) que permanecen en el tomo')],
    planes_cierre_pec=G7['planes_cierre_pec'],
    sol_reemplazos=[('Continuación práctica %d — ' % k, 'Actividad complementaria %d (opcional) — ' % k) for k in range(1, 7)]
                   + [('Las respuestas de las anteriores continuaciones prácticas', 'Las respuestas de las actividades complementarias (opcionales)')],
)
