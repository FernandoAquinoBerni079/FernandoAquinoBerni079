# -*- coding: utf-8 -*-
"""Caso de transferencia de la Unidad II — Escuela Básica Mbokaja (institución y personas ficticias).

Amplía `lote_1/caso/mbokaja.py` (que no se modifica y se importa tal cual) con los datos nuevos de las Prácticas 5 y 6.
Work §7.4: cada práctica trabaja otro conjunto de datos y exige una decisión nueva; por eso las situaciones MS-1 y MS-2
no aparecen en ningún ejemplo resuelto, y la solicitud MC-1 no se parece a la SC-01 del caso Arapoty.
Códigos: MP-# (relato del proceso actual), MS-# (situaciones nuevas), M-F7 (dato nuevo, sigue a M-F1…M-F6),
MR-## (requisitos acordados para la práctica), MC-# (solicitud de cambio)."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(AQUI)), 'lote_1', 'caso'))
import mbokaja as MB

INSTITUCION = MB.INSTITUCION

DATO_NUEVO = ('M-F7', 'Para el año próximo, la cooperadora recibió en donación una computadora para la biblioteca. '
                      'No tendrá conexión a internet.')

PROCESO_TITULO = 'Cómo se presta hoy en la biblioteca de Mbokaja (relato del encargado, caso de práctica, ficticio)'
PROCESO = [
    ('MP-1', 'El lector pide un libro al encargado, que lo busca en el estante.'),
    ('MP-2', 'Si el libro no está, el encargado le dice que vuelva otro día.'),
    ('MP-3', 'Si está, el encargado busca en la caja la ficha de cartón de ese libro.'),
    ('MP-4', 'Anota en la ficha el nombre del lector, su grado y la fecha, y le entrega el libro.'),
    ('MP-5', 'Cuando el lector devuelve el libro, el encargado busca la ficha y tacha la línea.'),
    ('MP-6', 'Si no encuentra la ficha enseguida, deja el libro en el estante y piensa tacharla después.'),
]

SITUACIONES_TITULO = 'Dos situaciones nuevas (caso de práctica, ficticio)'
SITUACIONES = [
    ('MS-1', 'Un estudiante devuelve un libro con hojas arrancadas. La norma M-N5 dice que el libro dañado se repone con otro igual o de valor similar.'),
    ('MS-2', 'Una estudiante del turno mañana quiere retirar un libro, pero la biblioteca abre solo de tarde (V-01).'),
]

CATALOGO_TITULO = 'Requisitos acordados para la biblioteca de Mbokaja (caso de práctica, ficticio)'
# (id, tipo, enunciado, fuentes)
CATALOGO = [
    ('MR-01', 'Funcional', 'El sistema debe registrar cada préstamo con el libro, el lector y la fecha.', 'V-03, MP-4'),
    ('MR-02', 'Funcional', 'El sistema debe registrar la devolución y cerrar el préstamo que corresponde.', 'V-11, MP-6'),
    ('MR-03', 'Funcional', 'El sistema debe mostrar al encargado qué lector tiene cada libro prestado, también los prestados a docentes.', 'MN-01'),
    ('MR-04', 'Funcional', 'El sistema debe rechazar el préstamo de un libro que ya está prestado.', 'MN-04'),
    ('MR-05', 'Funcional', 'El sistema debe permitir consultar qué libros están disponibles.', 'MN-02'),
    ('MR-06', 'Funcional', 'El sistema debe informar los libros más prestados en un período elegido.', 'MN-03'),
    ('MR-07', 'Calidad: privacidad', 'La consulta de libros disponibles no debe mostrar datos de los estudiantes.', 'MN-05'),
    ('MR-08', 'Restricción', 'El sistema debe funcionar en la computadora de la biblioteca sin conexión a internet.', 'M-F7, M-F2'),
]

CAMBIO_TITULO = 'Solicitud de la dirección de Mbokaja (caso de práctica, ficticio)'
CAMBIO = [
    ('MC-1', 'La directora pide que los docentes puedan llevar libros por un mes, en lugar de siete días, y que sus préstamos se registren igual que los de los estudiantes.'),
    ('MC-2', 'Lo pide porque el registro de los docentes en un cuaderno aparte no le permite saber qué libros faltan (V-08).'),
]

FUENTES = dict([DATO_NUEVO] + PROCESO + SITUACIONES + [(c, t) for c, _, t, _ in CATALOGO] + CAMBIO)
FUENTES.update(MB.FUENTES)
