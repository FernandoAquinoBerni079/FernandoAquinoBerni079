# -*- coding: utf-8 -*-
"""Caso de práctica de la Unidad I — Escuela Básica Mbokaja (institución y personas ficticias).

Las Prácticas 1, 2 y 3 trabajan con este caso, y no con el Colegio Técnico Arapoty, para cumplir la regla de
Work §7.4: cada práctica usa datos distintos de los ejemplos resueltos y exige una decisión nueva. Las tres
prácticas comparten la misma escuela, de modo que el estudiante acumula un segundo dossier completo.
Códigos: V-xx (relato de la visita, Práctica 1), M-N# (normas de la biblioteca, Práctica 2),
M-F# (datos para decidir, Práctica 3), MN-xx (necesidades del relevamiento de referencia, Práctica 3).
Las tarjetas de rol de la Práctica 2 están en la guía docente: el estudiante que entrevista no debe leerlas."""

INSTITUCION = 'Escuela Básica Mbokaja'
DESCRIPCION = ('Escuela ficticia de 1.º a 9.º grado, con turno mañana y turno tarde. La biblioteca funciona en '
               'un aula del primer piso. Todos los nombres y datos son inventados para este libro.')

PERSONAS = [
    ('Prof. Hugo Benítez', 'docente de Matemática, encargado de la biblioteca'),
    ('Lic. Graciela Núñez', 'directora'),
    ('Sofía', 'estudiante de 8.º grado, turno mañana (solo nombre de pila)'),
]

# ---- Práctica 1: relato de la visita de un estudiante de 3.º BTI (mezcla hechos, supuestos y soluciones)
VISITA_TITULO = 'Relato de la visita a la biblioteca de la Escuela Básica Mbokaja (caso de práctica, ficticio)'
VISITA = [
    ('V-01', 'La biblioteca funciona en un aula del primer piso y abre los lunes, miércoles y viernes, de 13:30 a 16:00.'),
    ('V-02', 'La atiende el Prof. Hugo Benítez, que también da clases de Matemática.'),
    ('V-03', 'Los préstamos se anotan en fichas de cartón, una por libro, que se guardan en una caja.'),
    ('V-04', 'Seguramente muchas fichas se pierden, porque la caja queda abierta sobre el escritorio.'),
    ('V-05', 'Mientras estuvimos, vimos a seis estudiantes pedir libros en media hora.'),
    ('V-06', 'Los estudiantes del turno mañana no deben usar la biblioteca, porque solo abre de tarde.'),
    ('V-07', 'Hay que poner una computadora con un programa de préstamos.'),
    ('V-08', 'El profesor nos dijo que el año pasado no volvieron unos quince libros.'),
    ('V-09', 'Una docente nos comentó que la directora quiere saber qué libros se leen más.'),
    ('V-10', 'Con un lector de códigos de barras se terminarían las demoras.'),
    ('V-11', 'En la caja había fichas de hace más de un año sin la devolución anotada.'),
    ('V-12', 'Los libros más pedidos deben ser los de la lectura obligatoria del mes.'),
]
# Clave (guía docente): H = hecho observado o testimonio registrado; S = supuesto; A = solución anticipada.
VISITA_CLAVE = {'V-01': 'H', 'V-02': 'H', 'V-03': 'H', 'V-04': 'S', 'V-05': 'H', 'V-06': 'S', 'V-07': 'A',
                'V-08': 'H', 'V-09': 'H', 'V-10': 'A', 'V-11': 'H', 'V-12': 'S'}

# ---- Práctica 2: documento que el estudiante analiza (las tarjetas de rol van en la guía docente)
NORMAS_TITULO = 'Normas de la biblioteca de la Escuela Básica Mbokaja (caso de práctica, ficticio)'
NORMAS = [
    ('M-N1', 'El plazo de préstamo es de siete días.'),
    ('M-N2', 'El préstamo es personal: el libro lo retira y lo devuelve el mismo lector.'),
    ('M-N3', 'Todo préstamo, también el de los docentes, se anota en la ficha del libro.'),
    ('M-N4', 'La biblioteca atiende en el horario publicado en la puerta.'),
    ('M-N5', 'El libro dañado o perdido se repone con otro igual o de valor similar.'),
]

TARJETAS = [
    ('Encargado de la biblioteca — Prof. Hugo Benítez', [
        'Lo que hacés: abrís lunes, miércoles y viernes de 13:30 a 16:00. Anotás cada préstamo en la ficha del '
        'libro y, cuando vuelve, tachás la línea.',
        'Lo que te preocupa: los libros de la lectura obligatoria se agotan el primer día. El año pasado no '
        'volvieron unos quince libros.',
        'Tu opinión: el plazo de siete días es corto; para vos tendría que ser de quince días.',
        'Solo si te preguntan cómo prestás a los docentes: «A los docentes no les hago ficha; los anoto en un '
        'cuaderno mío, porque ellos siempre devuelven».',
        'Solo si te preguntan qué te gustaría cambiar: «Me gustaría abrir en un recreo de la mañana, pero no '
        'tengo horas asignadas».',
    ]),
    ('Lectora — Sofía, 8.º grado, turno mañana', [
        'Lo que hacés: venís muy poco, porque la biblioteca abre de tarde y vos estudiás de mañana.',
        'Lo que te preocupa: no sabés qué libros hay; a veces te enterás de un libro cuando ya lo devolvieron.',
        'Tu opinión: la biblioteca tendría que abrir de mañana.',
        'Solo si te preguntan cómo conseguís los libros: «Le pido a una amiga del turno tarde que lo saque a su '
        'nombre y me lo pase».',
        'Si te preguntan algo que no está en esta tarjeta, respondé «no sé».',
    ]),
    ('Dirección — Lic. Graciela Núñez', [
        'Lo que hacés: aprobás las normas de la biblioteca y decidís qué libros se compran con el aporte de la '
        'cooperadora.',
        'Lo que te preocupa: querés saber qué libros se leen más, para decidir las compras. Los datos de los '
        'estudiantes, que son menores de edad, no pueden circular.',
        'Tu opinión: el plazo de siete días de las normas está bien.',
        'Solo si te preguntan por los recursos del año próximo: «El Prof. Benítez va a tener cuatro horas '
        'semanales para la biblioteca, en lugar de seis».',
        'Si te piden un dato que no está en esta tarjeta, respondé que lo vas a averiguar.',
    ]),
]

# ---- Práctica 3: datos para decidir el alcance
DATOS_TITULO = 'Datos para decidir (Escuela Básica Mbokaja, caso de práctica, ficticio)'
DATOS = [
    ('M-F1', 'La biblioteca no tiene computadora. La secretaría tiene una notebook que usa toda la mañana.'),
    ('M-F2', 'La biblioteca no tiene conexión a internet.'),
    ('M-F3', 'Este año la cooperadora puede pagar un armario con llave o materiales de oficina, pero no una computadora.'),
    ('M-F4', 'El año próximo el encargado tendrá cuatro horas semanales para la biblioteca, en lugar de seis.'),
    ('M-F5', 'Un grupo de estudiantes de 9.º se ofreció para ayudar en la biblioteca los miércoles.'),
    ('M-F6', 'El encargado estima unos cuarenta préstamos por semana.'),
]
NECESIDADES_TITULO = 'Necesidades del relevamiento de referencia (Escuela Básica Mbokaja)'
NECESIDADES = [
    ('MN-01', 'Saber qué lector tiene cada libro prestado, también los prestados a docentes.', 'M-N3 y el registro paralelo del encargado'),
    ('MN-02', 'Que los lectores del turno mañana sepan qué libros hay y puedan retirarlos.', 'Lectora y V-06'),
    ('MN-03', 'Que la dirección sepa qué libros se leen más, para decidir compras.', 'Dirección y V-09'),
    ('MN-04', 'Que los libros vuelvan: hoy no se sabe quién tiene los que faltan.', 'V-08 y V-11'),
    ('MN-05', 'Que los datos de los estudiantes, menores de edad, no circulen.', 'Dirección'),
]

FUENTES = dict(VISITA + NORMAS + DATOS + [(c, t) for c, t, _ in NECESIDADES])
