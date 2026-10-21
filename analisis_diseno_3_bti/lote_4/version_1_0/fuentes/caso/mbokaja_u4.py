# -*- coding: utf-8 -*-
"""Caso de transferencia de la Unidad IV — Escuela Básica Mbokaja (institución y personas ficticias).

Amplía, sin modificarlos, las fuentes de Mbokaja de los lotes 1 a 3 con los datos nuevos de las Prácticas 10 a 13.
  - Práctica 10: la computadora donada y las etiquetas propias de los libros.
  - Práctica 11: un lote de libros donados con un código repetido, un título mal escrito y datos que faltan, y
    lectores con datos incompletos (MD, ML).
  - Práctica 12: dos voluntarios cargan el mismo libro al mismo tiempo (MS-6) y un libro vuelve dañado (MS-1).
  - Práctica 13 (complemento editorial): el registro de una semana y una consulta que no coincide (MI).
Códigos nuevos: M-F10, M-F11, MD-01 a MD-06, ML-1 a ML-3, MS-6, MI-01 a MI-07."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(ADS, 'lote_3', 'caso'))
import mbokaja_u3 as MB3

DATOS_TITULO = 'Datos nuevos de Mbokaja (caso de práctica, ficticio)'
DATOS = [
    ('M-F10', 'El profesor del colegio vecino dejó instalado en la computadora donada un sistema de prueba, sin internet, con una copia de la base del curso.'),
    ('M-F11', 'Los libros de Mbokaja tienen etiquetas escritas a mano con MB-, un guion y tres cifras (por ejemplo, MB-104).'),
]
LOTE_TITULO = 'Lote de libros donados que llegó a Mbokaja (caso de práctica, ficticio)'
# (código, etiqueta del libro, título escrito en la planilla, autor, observación)
LOTE = [
    ('MD-01', 'MB-201', 'La laguna de los patos', 'Autora del caso (ficticia)', ''),
    ('MD-02', 'MB-202', 'La laguna de los patos', 'Autora del caso (ficticia)', 'Segundo ejemplar del mismo título'),
    ('MD-03', 'MB-202', 'Canciones del recreo', 'Autor del caso (ficticio)', 'La etiqueta repite la de MD-02'),
    ('MD-04', 'MB-204', 'La lagna de los patos', 'Autora del caso (ficticia)', 'Título mal escrito'),
    ('MD-05', 'MB-205', 'Mapas de mi país', '', 'Falta el autor'),
    ('MD-06', 'MB205', 'Mapas de mi país', 'Equipo editorial (ficticio)', 'Etiqueta sin guion'),
]
LECTORES_TITULO = 'Lectores nuevos que hay que registrar en Mbokaja (caso de práctica, ficticio)'
LECTORES = [
    ('ML-1', 'Estudiante de 4.º grado, sin grado anotado en la planilla.'),
    ('ML-2', 'Docente de Ciencias, con «6.º» anotado en la columna del grado.'),
    ('ML-3', 'Estudiante de 6.º grado, con todos sus datos.'),
]
SITUACIONES_TITULO = 'Situación nueva (caso de práctica, ficticio)'
SITUACIONES = [
    ('MS-6', 'Un miércoles, dos voluntarios cargaron en dos computadoras, al mismo tiempo, el mismo libro (MB-104) para dos lectores distintos.'),
]
SEMANA_TITULO = 'Registro de la semana del 6 al 10 de abril en Mbokaja (caso de práctica, ficticio)'
SEMANA = [
    ('MI-01', 'Lunes 6: préstamo de MB-104 a un estudiante de 5.º grado.'),
    ('MI-02', 'Lunes 6: préstamo de MB-105 a un estudiante de 6.º grado.'),
    ('MI-03', 'Miércoles 8: devolución de MB-104, anotada en la ficha de cartón pero no en el sistema.'),
    ('MI-04', 'Miércoles 8: préstamo de MB-201 a una docente.'),
    ('MI-05', 'Viernes 10: la consulta del sistema dice «0 disponibles» para el título de MB-104, que está en el estante.'),
    ('MI-06', 'Viernes 10: el informe de abril del sistema cuenta 3 préstamos; el encargado cuenta 3 en las fichas.'),
    ('MI-07', 'Viernes 10: la lista de préstamos activos al 13 de abril marca MB-104 como vencido.'),
]

FUENTES = dict(DATOS + [(c, '%s — %s' % (e, t)) for c, e, t, _, _ in LOTE] + LECTORES + SITUACIONES + SEMANA)
FUENTES.update(MB3.FUENTES)
