# -*- coding: utf-8 -*-
"""Fuente única de la arquitectura anual de Desarrollo Personal y Social 7.º (versión candidata con PEC).
Capacidades: transcripción literal del programa de estudio del MEC, 7.º grado (Drive 1EkkOgUbux0RQPwkw4GYGnUeDpb8_UldE,
págs. 55-57, «Capacidades para el 7.º grado»). Se respetan la puntuación y las erratas del original; los dos puntos con que el programa introduce los temas
(capacidades 1, 3 y 18) se cierran con punto."""

CAP = {
    1: 'Valora la importancia de integrarse y pertenecer a la comunidad educativa.',
    2: 'Reconoce la organización interna de la institución educativa.',
    3: 'Reconoce sus fortalezas, debilidades, intereses, habilidades y oportunidades para construir su proyecto de vida.',
    4: 'Expresa su habilidad de sentir, pensar y actuar como elementos que se observan en el proceso del autoconocimiento.',
    5: 'Valora la relación afectiva positiva entre los miembros de la familia y de su entorno.',
    6: 'Analiza las causas y las consecuencias del uso y abuso de la tecnología como elemento que afecta la relación personal directa y afectiva (celulares, Internet, otros) en el marco de la convivencia familiar y/ social.',
    7: 'Reconoce que los cambios que se generan en la pubertad y en la adolescencia forman parte de una etapa de la vida.',
    8: 'Analiza los artículos referentes a sus derechos y sus responsabilidades considerando su formación como ciudadano.',
    9: 'Reflexiona sobre los principales artículos relacionados con la No discriminación, expresados en el Código de la Niñez y la Adolescencia, la convención de los Derechos Humanos y de los Derechos sexuales y Derechos reproductivos.',
    10: 'Reconoce la importancia de conocer las leyes que protegen a los niños, las niñas y los adolescentes. y, además, que cada derecho lleva implícito una responsabilidad.',
    11: 'Identifica los diferentes tipos de liderazgo.',
    12: 'Participa con actitud democrática en el proceso de elección del Parlamento Escolar.',
    13: 'Valora la importancia de una correcta elección de autoridades y su incidencia en la vida del grupo.',
    14: 'Asume la responsabilidad de pertenecer a un grupo considerando sus habilidades y/o intereses.',
    15: 'Analiza las condiciones de organización para el estudio.',
    16: 'Planifica adecuadamente su tiempo para el estudio.',
    17: 'Identifica las medidas de prevención y mitigación en situaciones de riesgos.',
    18: 'Aplica normas de comportamiento en caso de riesgos.',
}
# Temas que el programa asocia a cada capacidad (literal, para la matriz de cobertura)
TEMAS_MEC = {
    1: ['Historia de la institución: fundador, primeros directivos, etc.', 'Identidad e integración a la comunidad educativa.', 'Proyecto Educativo Institucional.'],
    2: ['Organigrama de la institución.', 'Miembros de la institución educativa (directores, docentes, alumnos, otros). Funciones.', 'Dependencias de la institución.'],
    3: ['Autoconocimiento. Técnicas y procesos.', 'Autoestima', 'Autovaloración', 'Asertividad'],
    4: ['Pensamiento crítico y objetivo.'],
    5: ['Relaciones afectivas saludables (en la familia, con los compañeros, con los amigos)', 'Noviazgo: implicancia, compromiso.'],
    6: ['Influencia emocional, positiva y negativa, de los teléfonos celulares y de Internet con sus redes sociales.'],
    7: ['Influencia de los cambios en su afectividad.', 'Formas de afrontar esos cambios.'],
    8: ['Código de la Niñez y la Adolescencia.', 'Derechos Humanos.', 'Derechos sexuales y derechos reproductivos.'],
    9: ['El respeto como valor universal.', 'Respeto a la diversidad.', 'Tolerancia.'],
    10: ['Identificación de responsabilidades a partir de los derechos.'],
    11: ['Liderazgo: Concepto. Tipos. Características.'],
    12: ['Parlamento Escolar: Concepto. Conformación. Deberes. Responsabilidades.', 'Conformación del Parlamento Escolar', 'Derecho a la participación', 'Participación protagónica.'],
    13: ['Proceso electoral en el grado', 'Proceso electoral en la institución.'],
    14: ['Clubes: Concepto, Objetivos, Organización, Tipos.'],
    15: ['Condiciones que afectan positiva o negativamente al estudio y al aprendizaje: psicológicas, fisiológicas, ambientales, materiales.'],
    16: ['Organización del tiempo.', 'Concienciación del tiempo que se dedica al estudio.'],
    17: ['Físico: Violencia', 'Psicológico: Prevención. Mitigación. Emergencia.', 'Ambiental: Desastre. Factores de riesgo. Violencia.'],
    18: ['Físicos', 'Psicológicos', 'Ambientales: Incendio. Interrupción de energía eléctrica. Falta de suministro de agua potable. Tormenta.'],
}
# Propósito del componente PEC: literal del programa de 7.º («El componente Proyecto Educativo Comunitario»)
PEC_PROPOSITO = ('Con este componente, se pretende que niños, niñas y adolescentes desarrollen capacidades que les ayuden a planificar, '
                 'implementar y evaluar proyectos de servicio social, con el fin de mejorar y transformar el entorno en el cual se '
                 'desenvuelven en un marco de compromiso con la sociedad.')

UNIDADES = {
    1: 'Sentido de pertenencia', 2: 'Autoconocimiento', 3: 'Vida afectiva', 4: 'Derechos y responsabilidades',
    5: 'Organizaciones estudiantiles', 6: 'Organización y planificación', 7: 'Gestión de riesgo',
}
UNIDAD_CAPS = {1: [1, 2], 2: [3, 4], 3: [5, 6, 7], 4: [8, 9, 10], 5: [11, 12, 13, 14], 6: [15, 16], 7: [17, 18]}
PERIODO = {1: 'Febrero – marzo', 2: 'Marzo – abril', 3: 'Abril – mayo', 4: 'Mayo – junio', 5: 'Agosto', 6: 'Septiembre', 7: 'Octubre – noviembre'}

# tipo: C = clase temática (Componente Orientación), P = taller del Proyecto Educativo Comunitario,
#       E = evaluación de unidad, I = evaluación integradora de etapa
# (n.º de encuentro, tipo, número dentro del tipo, unidad, capacidades, título, origen en el paquete anterior)
ENCUENTROS = [
    (1, 'C', 1, 1, [1], 'Bienvenida al tercer ciclo: pertenecer', 'Clase 1 (+ prueba diagnóstica)'),
    (2, 'C', 2, 1, [2], 'Cómo se organiza mi colegio', 'Clase 2 + Continuación 1 (horario y evaluación)'),
    (3, 'C', 3, 1, [1], 'El PEI, los proyectos de la escuela y las normas de convivencia', 'Clase 3'),
    (4, 'E', 1, 1, [1, 2], 'Sentido de pertenencia', 'Evaluación U1'),
    (5, 'C', 4, 2, [3], '¿Quién soy? Fortalezas, debilidades, intereses y habilidades', 'Clase 4'),
    (6, 'C', 5, 2, [3], 'Autoestima, autovaloración y asertividad', 'Clase 5'),
    (7, 'C', 6, 2, [4], 'Sentir, pensar y actuar: el pensamiento crítico', 'Clase 6'),
    (8, 'E', 2, 2, [3, 4], 'Autoconocimiento', 'Evaluación U2'),
    (9, 'C', 7, 3, [5], 'Relaciones afectivas saludables', 'Clase 7'),
    (10, 'C', 8, 3, [6], 'Tecnología, redes y convivencia', 'Clase 8'),
    (11, 'C', 9, 3, [7], 'Los cambios de la pubertad y la adolescencia', 'Clase 9'),
    (12, 'E', 3, 3, [5, 6, 7], 'Vida afectiva', 'Evaluación U3'),
    (13, 'C', 10, 4, [8], 'Mis derechos y mis responsabilidades', 'Clase 10'),
    (14, 'C', 11, 4, [9], 'No discriminación, respeto y tolerancia', 'Clase 11'),
    (15, 'C', 12, 4, [10], 'Las leyes que me protegen: cada derecho, una responsabilidad', 'Clase 12 + Clase 21 (red de apoyo)'),
    (16, 'E', 4, 4, [8, 9, 10], 'Derechos y responsabilidades', 'Evaluación U4'),
    (17, 'P', 1, 0, [1, 2], 'Nuestra escuela como comunidad: qué es un Proyecto Educativo Comunitario', 'Nuevo (sustituye a Continuación 1)'),
    (18, 'I', 1, 0, list(range(1, 11)), 'Primera etapa (Unidades 1 a 4)', 'Integradora 1.ª etapa'),
    (19, 'P', 2, 0, [1, 2], 'Diagnóstico participativo: conocer y priorizar las necesidades', 'Nuevo (sustituye a Continuación 2)'),
    (20, 'C', 13, 5, [11], 'Liderazgo: tipos y características', 'Clase 13'),
    (21, 'C', 14, 5, [12], 'El Parlamento Escolar y la participación protagónica', 'Clase 14 + Continuación 2 (reglamento)'),
    (22, 'C', 15, 5, [13, 14], 'Elecciones en el grado y clubes', 'Clase 15 + Continuación 3 (simulación)'),
    (23, 'E', 5, 5, [11, 12, 13, 14], 'Organizaciones estudiantiles', 'Evaluación U5'),
    (24, 'P', 3, 0, [1, 14], 'Elegir y fundamentar nuestro proyecto: eje, objetivos y beneficiarios', 'Nuevo (sustituye a Continuación 3)'),
    (25, 'C', 16, 6, [15], 'Las condiciones para estudiar', 'Clase 16 + Continuación 4 (auditoría)'),
    (26, 'C', 17, 6, [16], 'Organizá tu tiempo: el estudio como hábito', 'Clase 17'),
    (27, 'C', 18, 6, [16], 'Mi plan semanal de estudio y mis metas', 'Clase 18 + Continuación 5 (semana real)'),
    (28, 'E', 6, 6, [15, 16], 'Organización y planificación', 'Evaluación U6'),
    (29, 'P', 4, 0, [11, 14], 'Planificar el proyecto: actividades, cronograma, recursos y responsables', 'Nuevo (sustituye a Continuación 4)'),
    (30, 'C', 19, 7, [17], 'Prevención y mitigación frente a los riesgos', 'Clase 19 + Continuación 6 (mapa de riesgos)'),
    (31, 'C', 20, 7, [18], 'Normas de comportamiento en caso de riesgos', 'Clase 20'),
    (32, 'P', 5, 0, [14, 17], 'Ejecutar con seguridad y hacer el seguimiento', 'Nuevo (sustituye a Continuación 5)'),
    (33, 'E', 7, 7, [17, 18], 'Gestión de riesgo', 'Evaluación U7'),
    (34, 'P', 6, 0, [4, 14], 'Evaluar los resultados del proyecto', 'Nuevo (sustituye a Continuación 6)'),
    (35, 'P', 7, 0, [1, 14], 'Socializar lo aprendido y cerrar el año', 'Nuevo (sustituye a Clase 21 «Cierre del año»)'),
    (36, 'I', 2, 0, list(range(11, 19)), 'Segunda etapa (Unidades 5 a 7)', 'Integradora 2.ª etapa'),
]
assert [e[0] for e in ENCUENTROS] == list(range(1, 37))
ETAPA = lambda n: 1 if n <= 18 else 2
PEC_ETAPAS = {
    1: 'Introducción y comprensión del proyecto · identificación de necesidades',
    2: 'Diagnóstico participativo y priorización de problemas',
    3: 'Formulación I: eje, fundamentación, objetivos y beneficiarios',
    4: 'Formulación II: actividades, cronograma, recursos · organización y responsabilidades',
    5: 'Ejecución y seguimiento',
    6: 'Evaluación de resultados',
    7: 'Socialización de aprendizajes · cierre',
}
PEC_MES = {1: 'Junio', 2: 'Agosto', 3: 'Agosto', 4: 'Septiembre', 5: 'Octubre', 6: 'Noviembre', 7: 'Noviembre'}


def rotulo(e):
    n, t, k, u, caps, tit, _ = e
    return {'C': 'Clase %d — %s' % (k, tit), 'P': 'Taller PEC %d — %s' % (k, tit),
            'E': 'Evaluación de la Unidad %d — %s' % (u, tit), 'I': 'Evaluación integradora — %s' % tit}[t]


if __name__ == '__main__':
    from collections import Counter
    c = Counter(e[1] for e in ENCUENTROS)
    print(c, 'etapa1', sum(1 for e in ENCUENTROS if e[0] <= 18), 'etapa2', sum(1 for e in ENCUENTROS if e[0] > 18))
    cub = {k: [e[0] for e in ENCUENTROS if e[1] == 'C' and k in e[4]] for k in CAP}
    assert all(cub.values()), cub
    print(cub)
