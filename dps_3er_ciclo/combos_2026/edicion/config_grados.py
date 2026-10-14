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
