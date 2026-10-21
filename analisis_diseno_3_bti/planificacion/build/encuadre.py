# -*- coding: utf-8 -*-
"""Encuadre curricular e institucional del plan anual, separado en tres niveles:

A. Disposiciones oficiales: citas textuales del Diseño Curricular del MEC, con su página. Se comprobaron contra la copia
   identificada por SHA-256 (la misma que usó el informe de Work). El PDF del MEC no se copia al repositorio:
   `controles_plan.py` vuelve a comprobar las citas si se le indica la ruta con la variable ADS_MEC_PDF.
B. Propuesta editorial de la colección: lo que decidió el informe de Work v0.1 y aprobó la colección v0.2. No es
   programa ni capacidad oficial del MEC.
C. Decisiones que corresponden a la institución y no están confirmadas: no se inventan; quedan como campos a completar.
"""
MEC = {
    'titulo': 'Diseño Curricular del Bachillerato Técnico en Servicios, Informática. Plan de estudios de enseñanzas '
              'mínimas, mayo de 2026 (MEC, Dirección General de Tercer Ciclo de la EEB y de la Educación Media)',
    'archivo': 'DISEÑO CURRICULAR DE INFORMATICA - MAYO 2026 (1).pdf',
    'paginas': 111,
    'bytes': 1457383,
    'sha256': 'a0052cc50782715b0a62091430e38b14adcdd6c9ae54fc49320ebce64bdd0856',
}

# (página, cita textual, qué se toma para el plan)
CITAS_MEC = [
    (29, 'El plan optativo es un espacio previsto para que las propias instituciones educativas elijan, conforme con las '
         'necesidades y los intereses de los estudiantes, qué desarrollar con cada grupo.',
     'Fundamento para ofrecer la asignatura como propuesta institucional.'),
    (29, 'Cada institución puede elaborar su propio programa de estudio a ser implementado en el espacio del plan optativo.',
     'El programa de esta asignatura lo adopta la institución; no es un programa nacional.'),
    (24, 'El Proyecto Curricular Institucional es el espacio donde se concretiza la adecuación curricular.',
     'La adopción del programa, sus capacidades y su horario se registran en el PCI.'),
    (24, 'en ningún caso se reemplazarán las disciplinas incluidas en el currículum nacional, así como tampoco se podrán '
         'disminuir sus cargas horarias establecidas.',
     'El optativo no toma horas de Laboratorio, Algorítmica ni de otras disciplinas.'),
    (34, 'Vigente según la Resolución N° 2141/2016',
     'Plan de estudios del Bachillerato Técnico en Servicios, especialidad Informática, como lo presenta el documento.'),
    (34, 'Plan Optativo 5',
     'En 3.º curso, la tabla asigna 5 al Plan Optativo. La tabla no indica la unidad; el informe de Work la lee como '
     'horas cátedra semanales. La institución lo confirma.'),
    (31, 'g) definir los indicadores de logros en relación con cada capacidad y, consecuentemente, decidir los '
         'procedimientos e instrumentos de evaluación que aplicará.',
     'Estructura de la planificación: capacidades, temas, indicadores, procedimientos e instrumentos.'),
    (33, 'Para la elaboración de los indicadores, se debe considerar en primer lugar el verbo utilizado para enunciar la '
         'capacidad',
     'Criterio con que se revisaron los indicadores de cada capítulo.'),
    (96, 'Aprendizaje basado en proyectos (ABP): es una estrategia de enseñanza aprendizaje especialmente relevante para la '
         'adquisición de competencias.',
     'Enfoque metodológico del proyecto anual.'),
    (101, 'Contempla todo el proceso, desde el principio al fin (evaluación continua).',
     'Evaluación continua basada en evidencias.'),
    (101, 'Se adecua a las características de cada alumno (evaluación individual).',
     'Evidencia individual en cada hito y defensa individual.'),
]

# Lo que el documento del MEC NO establece en las páginas comprobadas (se buscó en las 111 páginas)
NO_ESTABLECE = [
    'La duración de la hora cátedra en minutos.',
    'La cantidad de semanas o de encuentros del año lectivo, y sus fechas.',
    'Etapas, períodos de evaluación o fechas de entrega para el Plan Optativo.',
    'Un programa, competencias o capacidades para una asignatura llamada «Análisis y Diseño de Sistemas».',
    'Un trámite de aprobación del programa institucional del Plan Optativo.',
]

PROPUESTA_EDITORIAL = [
    ('Nombre de la asignatura', 'Análisis y Diseño de Sistemas', 'Work §2.2'),
    ('Competencia general', 'Competencia propuesta (sección 2 de este plan)', 'Work §4.1'),
    ('Capacidades', 'C1 a C10, propuestas para el programa institucional', 'Work §4.2; libro, págs. 7 y fichas'),
    ('Carga y duración', '36 encuentros de 5 HC (180 HC). Los 36 encuentros son una estimación editorial, no una cantidad '
     'que fije el MEC', 'Work §2.2 y §5.1'),
    ('Unidades y capítulos', '6 unidades y 18 capítulos, dos encuentros por capítulo', 'Work §5 y §6; libro'),
    ('Caso conductor', 'Biblioteca escolar ficticia (Colegio Técnico Arapoty) y caso de práctica Mbokaja', 'Work §7; libro'),
    ('Entorno técnico', 'HTML y CSS, PHP y SQLite en una computadora local: referencia provisional, no obligatoria',
     'Work §7.5; guía, Parte IV, sección 0'),
    ('Evaluación', 'Hitos H1 a H6, ponderación sugerida, 60 % de producto y 40 % individual, cuatro niveles',
     'Work §4.3; guía'),
    ('Adaptación a 28 encuentros', 'Alternativa para un año con menos encuentros; no reemplaza a la secuencia ordinaria',
     'guía, parte general, sección 1'),
]

INSTITUCIONAL = [
    ('Adopción del programa en el PCI', 'La institución incorpora la asignatura en su Proyecto Curricular Institucional (MEC, p. 24).'),
    ('Carga horaria', 'Confirmar que las 5 del Plan Optativo de 3.º son horas cátedra semanales y cómo se reparten en la semana.'),
    ('Duración de la hora cátedra', 'La fija la institución. El plan no convierte HC a minutos.'),
    ('Calendario', 'Fechas de inicio y fin del año lectivo, semanas efectivas, feriados y fechas de cada encuentro.'),
    ('Secuencia', 'Elegir la secuencia ordinaria de 36 encuentros o la adaptación a 28, según las semanas efectivas.'),
    ('Etapas y calificación', 'Períodos de evaluación, régimen de calificación y promoción, y conversión de los niveles '
                              'de desempeño a calificaciones.'),
    ('Coordinación', 'Acuerdos con Algorítmica 3.º (antes del Encuentro 13) y con Laboratorio 3.º (antes del Encuentro 19).'),
    ('Equipamiento y entorno', 'Computadoras disponibles, prueba de campo E-1 a E-12 en Windows y en los equipos escolares.'),
    ('Datos reservados', 'Custodia del conjunto DR (Unidad V) y de las variantes V6 (Unidad VI), fuera del repositorio y '
                         'de las carpetas del alumnado.'),
]
