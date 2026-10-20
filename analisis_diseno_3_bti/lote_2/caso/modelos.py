# -*- coding: utf-8 -*-
"""Modelos funcionales del caso Arapoty (Capítulo 5), como datos: proceso actual y propuesto (diagrama de actividades
con particiones), diagrama de contexto, diagrama de casos de uso y plantillas de los tres casos de uso prioritarios.

Las figuras del Capítulo 5 se dibujan a partir de estos datos (build/diagramas.py) y el texto del capítulo los cita,
así que figura, texto y controles no pueden decir cosas distintas. La notación de cada modelo es la de
`lote_2_plan/NOTACIONES_CAPITULO_5.md` (aprobada por Fernando): una notación por modelo, sin mezclar símbolos.

Diagramas de actividades. Nodo: (id, tipo, carril, fila, desplazamiento, texto). Tipos: inicial, accion, decision
(también fusión), final. «fila» es el orden vertical; «desplazamiento» corre el nodo dentro de su carril (en anchos
de nodo). Flujo: (desde, hasta, guarda o None). Toda salida de una decisión lleva guarda entre corchetes."""

PROCESO_ACTUAL = dict(
    titulo='Proceso actual de préstamo y devolución',
    notacion='actividad',
    carriles=['Lector', 'Bibliotecaria'],
    nodos=[
        ('ini', 'inicial', 'Lector', 0, 0, None),
        ('a1', 'accion', 'Lector', 1, 0, 'Pedir un libro\nen el mostrador'),
        ('a2', 'accion', 'Bibliotecaria', 2, 0, 'Buscar el libro\nen el estante (1)'),
        ('d1', 'decision', 'Bibliotecaria', 3, 0, None),
        ('a3', 'accion', 'Bibliotecaria', 4, 1.08, 'Decir que\nno está'),
        ('fin1', 'final', 'Bibliotecaria', 5, 1.08, None),
        ('a4', 'accion', 'Bibliotecaria', 4, 0, 'Anotar título, lector,\ncurso y fecha en\nel cuaderno (2)'),
        ('a5', 'accion', 'Lector', 5, 0, 'Llevar el libro y,\nal terminar,\ndevolverlo'),
        ('a6', 'accion', 'Bibliotecaria', 6, 0, 'Buscar el préstamo\nen el cuaderno\npor el título (3)'),
        ('a7', 'accion', 'Bibliotecaria', 7, 0, 'Tachar la línea\ndel préstamo'),
        ('fin2', 'final', 'Bibliotecaria', 8, 0, None),
    ],
    flujos=[('ini', 'a1', None), ('a1', 'a2', None), ('a2', 'd1', None), ('d1', 'a3', '[no está]'),
            ('d1', 'a4', '[está en el estante]'), ('a3', 'fin1', None), ('a4', 'a5', None), ('a5', 'a6', None),
            ('a6', 'a7', None), ('a7', 'fin2', None)],
)
# Problemas del dossier marcados con (1), (2) y (3) en las acciones del proceso actual (Tabla 5.2).
PROBLEMAS_ACTUAL = [
    ('(1)', 'Buscar el libro en el estante', 'Si no está, puede estar prestado, mal ubicado o perdido; el lector espera en la fila para saberlo.', ['E1-L6', 'O1-4', 'E3-L2']),
    ('(2)', 'Anotar en el cuaderno', 'Con fila, la anotación sale ilegible, y el mismo libro puede quedar anotado a dos lectores.', ['E1-L2', 'E4-L4']),
    ('(3)', 'Buscar el préstamo por el título', 'Con varios ejemplares del mismo título, no se sabe a qué préstamo corresponde el que vuelve; encontrar quién lo llevó lleva hasta media hora.', ['E4-L2', 'E1-L4']),
]

PROCESO_PROPUESTO = dict(
    titulo='Proceso propuesto de préstamo',
    notacion='actividad',
    carriles=['Lector', 'Bibliotecaria', 'Sistema'],
    nodos=[
        ('ini', 'inicial', 'Lector', 0, 0, None),
        ('a1', 'accion', 'Lector', 1, 0, 'Pedir un\nejemplar'),
        ('a2', 'accion', 'Bibliotecaria', 2, 0, 'Indicar el lector\ny el ejemplar'),
        ('a3', 'accion', 'Sistema', 3, 0, 'Comprobar lector\nactivo y máximo\nvigente (RF-05, RF-06)'),
        ('d1', 'decision', 'Sistema', 4, 0, None),
        ('a4', 'accion', 'Sistema', 5, 0, 'Comprobar que el\nejemplar no tenga un\npréstamo activo (RF-04)'),
        ('d2', 'decision', 'Sistema', 6, 0, None),
        ('a5', 'accion', 'Sistema', 7, 0, 'Registrar el préstamo\ny su vencimiento\n(RF-01, RF-02)'),
        ('m1', 'decision', 'Sistema', 7, 1.08, None),
        ('a6', 'accion', 'Sistema', 8, 1.08, 'Mostrar el motivo\ndel rechazo\n(RF-04 a RF-06)'),
        ('a7', 'accion', 'Bibliotecaria', 8, 0, 'Entregar el ejemplar\ncon su fecha\nde vencimiento'),
        ('a8', 'accion', 'Bibliotecaria', 10, 0, 'Explicar el\nmotivo al lector'),
        ('a9', 'accion', 'Lector', 9, 0, 'Llevar el\nejemplar'),
        ('fin1', 'final', 'Lector', 10, 0, None),
        ('fin2', 'final', 'Bibliotecaria', 11, 0, None),
    ],
    flujos=[('ini', 'a1', None), ('a1', 'a2', None), ('a2', 'a3', None), ('a3', 'd1', None),
            ('d1', 'a4', '[habilitado]'), ('d1', 'm1', '[no habilitado]'), ('a4', 'd2', None),
            ('d2', 'a5', '[disponible]'), ('d2', 'm1', '[ya prestado]'), ('m1', 'a6', None), ('a5', 'a7', None),
            ('a7', 'a9', None), ('a9', 'fin1', None), ('a6', 'a8', None), ('a8', 'fin2', None)],
)
# Qué cambia del proceso actual al propuesto (Tabla 5.3): paso, quién lo hace ahora, decisión tomada.
CAMBIOS_PROCESO = [
    ('Saber si el libro está', 'La bibliotecaria, mirando el estante (1)', 'El sistema, por la consulta de disponibilidad (RF-07), antes de llegar al mostrador', 'El lector no pierde el recreo en la fila (E3-L2).'),
    ('Comprobar si se puede prestar', 'Nadie: se presta lo que hay en el estante', 'El sistema comprueba lector y ejemplar (RF-04 a RF-06)', 'Las reglas RN-01, RN-02 y RN-04 se cumplen siempre, también con fila.'),
    ('Anotar el préstamo', 'La bibliotecaria, a mano, con apuro (2)', 'El sistema registra ejemplar, lector y fecha (RF-01) y calcula el vencimiento (RF-02)', 'Desaparece la letra ilegible y el doble préstamo (E1-L2, E4-L4).'),
    ('Identificar la devolución', 'La bibliotecaria, buscando por título (3)', 'El sistema, por el código del ejemplar (RF-03)', 'Cada ejemplar devuelto cierra su propio préstamo (E4-L2).'),
    ('Explicar un rechazo', 'No existe: el problema aparece después', 'El sistema muestra el motivo y la bibliotecaria lo explica', 'Las decisiones quedan a la vista de las dos personas.'),
]

# ------------------------------------------------------------------ diagrama de contexto (5.2)
CONTEXTO = dict(
    titulo='Diagrama de contexto del sistema de préstamos',
    notacion='contexto',
    sistema='Sistema de préstamos\nde la biblioteca',
    entidades=['Bibliotecaria', 'Lector', 'Dirección'],
    # (origen, destino, rótulo, fuentes del dossier que lo respaldan)
    flujos=[
        ('Bibliotecaria', 'Sistema', 'datos del préstamo', ['D1-A4', 'E1-L2']),
        ('Bibliotecaria', 'Sistema', 'código del ejemplar devuelto', ['E4-L2']),
        ('Bibliotecaria', 'Sistema', 'alta o baja de un lector', ['E4-L6']),
        ('Sistema', 'Bibliotecaria', 'préstamos activos y vencidos', ['E1-L4']),
        ('Sistema', 'Bibliotecaria', 'motivo del rechazo', ['E4-L4']),
        ('Lector', 'Sistema', 'título buscado', ['E3-L1']),
        ('Sistema', 'Lector', 'disponibilidad del título', ['E3-L3']),
        ('Dirección', 'Sistema', 'mes del informe', ['E5-L2']),
        ('Sistema', 'Dirección', 'informe mensual por curso', ['E5-L2', 'E1-L8']),
    ],
)
# Quedan fuera del límite (Work §7.2, «fuera del núcleo») o no intercambian información con el sistema.
FUERA_DEL_LIMITE = [
    ('Encargado de informática', 'Instala y cuida la computadora (E4-L10), pero no da ni recibe información de préstamos. No es una entidad externa del diagrama.'),
    ('Inscripción de estudiantes', 'Dice quiénes son lectores (Figura 1.1). En el núcleo, la bibliotecaria carga los lectores a mano: no hay un flujo automático con la secretaría.'),
    ('Compra de libros', 'Usaría los títulos más pedidos, pero está fuera del alcance mínimo.'),
    ('Familias, catálogo nacional y notificaciones externas', 'Fuera del núcleo (Work §7.2): no se dibujan.'),
]

# ------------------------------------------------------------------ casos de uso (5.3 y 5.4)
CASOS_USO = dict(
    titulo='Diagrama de casos de uso del sistema de préstamos',
    notacion='casos_de_uso',
    limite='Sistema de préstamos de la biblioteca',
    actores=['Bibliotecaria', 'Lector', 'Dirección'],
    casos=[('CU-01', 'Registrar préstamo'), ('CU-02', 'Registrar devolución'), ('CU-03', 'Consultar disponibilidad'),
           ('CU-04', 'Obtener informe\nmensual por curso'), ('CU-05', 'Inactivar lector\no ejemplar')],
    asociaciones=[('Bibliotecaria', 'CU-01'), ('Bibliotecaria', 'CU-02'), ('Bibliotecaria', 'CU-03'), ('Lector', 'CU-03'),
                  ('Bibliotecaria', 'CU-04'), ('Dirección', 'CU-04'), ('Bibliotecaria', 'CU-05')],
)
PRIORITARIOS = ['CU-01', 'CU-02', 'CU-03']   # Work §4.2, C4: tres casos de uso prioritarios con flujo alternativo

# Plantilla: actor, precondición, escenario principal, flujos alternativos (numerados desde el paso donde se desvían),
# requisitos que cubre.
PLANTILLAS = [
    dict(id='CU-01', nombre='Registrar préstamo', actor='Bibliotecaria',
         precondicion='La bibliotecaria inició su sesión (RNF-02). El lector está frente al mostrador con el ejemplar.',
         escenario=[
             'La bibliotecaria indica el lector.',
             'El sistema muestra el lector y sus préstamos activos.',
             'La bibliotecaria indica el ejemplar por su código.',
             'El sistema comprueba que el lector esté activo y que no haya alcanzado el máximo vigente (RF-05, RF-06).',
             'El sistema comprueba que el ejemplar no tenga un préstamo activo (RF-04).',
             'El sistema registra el préstamo con el ejemplar, el lector y la fecha de salida, y calcula el vencimiento (RF-01, RF-02).',
             'El sistema muestra la fecha de vencimiento, y la bibliotecaria entrega el ejemplar.',
         ],
         alternativos=[
             ('4a', 'El lector está inactivo: el sistema rechaza el préstamo y muestra el motivo. No se crea ningún préstamo. Termina el caso de uso (RF-06).'),
             ('4b', 'El lector ya tiene el máximo vigente de préstamos activos: el sistema rechaza el préstamo, muestra el motivo y la cantidad de préstamos activos. Termina el caso de uso (RF-05).'),
             ('5a', 'El ejemplar ya tiene un préstamo activo: el sistema rechaza la operación y muestra el motivo. El préstamo original sigue siendo el único activo. Termina el caso de uso (RF-04).'),
         ],
         requisitos=['RF-01', 'RF-02', 'RF-04', 'RF-05', 'RF-06', 'RNF-02']),
    dict(id='CU-02', nombre='Registrar devolución', actor='Bibliotecaria',
         precondicion='La bibliotecaria inició su sesión (RNF-02). Un lector entrega un ejemplar en el mostrador.',
         escenario=[
             'La bibliotecaria indica el código del ejemplar devuelto.',
             'El sistema muestra el préstamo activo de ese ejemplar, con el lector que lo tiene (RF-08).',
             'La bibliotecaria confirma la devolución.',
             'El sistema cierra ese préstamo con la fecha de devolución, lo conserva en el historial y el ejemplar vuelve a figurar disponible (RF-03).',
         ],
         alternativos=[
             ('1a', 'El código no corresponde a ningún ejemplar de la biblioteca (el libro no es de la biblioteca, como en E2-L10): el sistema lo informa y la bibliotecaria aparta el libro. Termina el caso de uso.'),
             ('2a', 'El ejemplar no tiene un préstamo activo (devolución sin préstamo identificable, como en E4-L2): el sistema lo informa y no cierra ningún préstamo. La bibliotecaria aparta el ejemplar y lo anota para revisarlo con el historial. Termina el caso de uso.'),
         ],
         requisitos=['RF-03', 'RF-08', 'RNF-02']),
    dict(id='CU-03', nombre='Consultar disponibilidad', actor='Lector (también la bibliotecaria)',
         precondicion='Ninguna: la consulta es pública y no pide sesión.',
         escenario=[
             'El lector escribe el título, o parte de él.',
             'El sistema muestra los títulos que coinciden.',
             'El lector elige un título.',
             'El sistema muestra cuántos ejemplares de ese título están disponibles, sin ningún dato de los lectores (RF-07, RNF-03).',
         ],
         alternativos=[
             ('2a', 'Ningún título coincide: el sistema lo informa y propone revisar lo escrito. Vuelve al paso 1.'),
             ('4a', 'No hay ejemplares disponibles: el sistema muestra «0 disponibles», sin decir quién los tiene (RNF-03). Termina el caso de uso.'),
         ],
         requisitos=['RF-07', 'RNF-03']),
]
PLANTILLA = {p['id']: p for p in PLANTILLAS}
