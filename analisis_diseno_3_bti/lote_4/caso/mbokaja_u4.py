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

# ------------------------------------------------------------------ Práctica 11, v1.1 (corrección de la auditoría)
# La práctica se ejecuta en una COPIA DE PRÁCTICA de la base del equipo (o, si el equipo no llegó, de la referencia
# docente), sin cambiar la base Arapoty: las etiquetas de Mbokaja se cargan con una correspondencia fija, porque el
# sistema entregado valida EJ- y cuatro cifras. Lo que no se puede ejecutar con el entorno entregado se resuelve en papel.
CORRESPONDENCIA_TITULO = 'Cómo se cargan los datos de Mbokaja en la copia de práctica (correspondencia fija)'
# (dato de Mbokaja, cómo se escribe en la copia de práctica, por qué)
CORRESPONDENCIA = [
    ('Etiqueta MB- y tres cifras (por ejemplo, MB-201)', 'EJ-0 y las mismas tres cifras (EJ-0201)',
     'El sistema entregado valida EJ- y cuatro cifras; la correspondencia conserva las cifras de la etiqueta.'),
    ('Etiqueta con otro formato (MB205)', 'Tal como figura en la planilla (MB205)', 'Para ver qué responde el sistema.'),
    ('Obra «La laguna de los patos»', 'Obra OB-0210, edición ED-0210', 'Códigos asignados por el encargado.'),
    ('Obra «Canciones del recreo»', 'Obra OB-0220, edición ED-0220', 'Códigos asignados por el encargado.'),
    ('Obra «Mapas de mi país»', 'Obra OB-0230, edición ED-0230', 'Códigos asignados por el encargado.'),
    ('Editorial y año de las donaciones', '«Donación Mbokaja»', 'La planilla no los trae.'),
    ('Lectores ML-1, ML-2 y ML-3', 'LE-0301, LE-0302 y LE-0303, con el nombre «Lector ML-1 (ficticio)» y así',
     'Datos ficticios; el sistema no guarda datos personales reales.'),
]
EJECUCION_TITULO = 'Qué se ejecuta en la copia de práctica y qué se resuelve en papel'
EJECUCION = [
    ('Nivel 1', 'En papel, y después se comprueba en la copia', 'Clasificar cada fila y prever el mensaje; luego cargar las filas tal cual y comparar.'),
    ('Nivel 2', 'Se ejecuta en la copia de práctica', 'Cargar el lote corregido con la correspondencia y comprobar con la consulta pública.'),
    ('Nivel 3', 'En papel (diseño)', 'El sistema entregado no tiene un rol de voluntario: se decide y se diseña la prueba, sin programarla.'),
]
# Secuencia de comprobación del Nivel 2 (la ejecuta lote_4/practica_11/comprobar_practica_11.php sobre una copia aislada
# de la referencia docente). (paso, fuente, operación, entradas, mensaje esperado)
PASOS_P11 = [
    (1, 'MD-01', 'OA-02', ['OB-0210', 'La laguna de los patos', 'Autora del caso (ficticia)', 'ED-0210', 'Donación Mbokaja'], 'MA-04'),
    (2, 'MD-01', 'OA-01', ['EJ-0201', 'ED-0210'], 'MA-01'),
    (3, 'MD-02', 'OA-01', ['EJ-0202', 'ED-0210'], 'MA-01'),
    (4, 'MD-03', 'OA-02', ['OB-0220', 'Canciones del recreo', 'Autor del caso (ficticio)', 'ED-0220', 'Donación Mbokaja'], 'MA-04'),
    (5, 'MD-03', 'OA-01', ['EJ-0202', 'ED-0220'], 'MA-02'),
    (6, 'MD-04', 'OA-01', ['EJ-0204', 'ED-0210'], 'MA-01'),
    (7, 'MD-05', 'OA-02', ['OB-0230', 'Mapas de mi país', '', 'ED-0230', 'Donación Mbokaja'], 'MV-01'),
    (8, 'MD-06', 'OA-01', ['MB205', 'ED-0230'], 'MV-02'),
    (9, 'MD-06', 'OA-02', ['OB-0230', 'Mapas de mi país', 'Equipo editorial (ficticio)', 'ED-0230', 'Donación Mbokaja'], 'MA-04'),
    (10, 'MD-05 y MD-06', 'OA-01', ['EJ-0205', 'ED-0230'], 'MA-01'),
    (11, 'ML-1', 'OA-03', ['LE-0301', 'Lector ML-1 (ficticio)', 'estudiante', ''], 'MV-03'),
    (12, 'ML-2', 'OA-03', ['LE-0302', 'Lector ML-2 (ficticio)', 'docente', '6.º'], 'MV-04'),
    (13, 'ML-3', 'OA-03', ['LE-0303', 'Lector ML-3 (ficticio)', 'estudiante', '6.º grado'], 'MA-06'),
]
# Consultas públicas al final: (texto buscado, obras esperadas, ejemplares, disponibles, o el mensaje si no hay obras)
CONSULTAS_P11 = [
    ('laguna', 1, 3, 3, None),
    ('Canciones', 0, 0, 0, 'ME-08'),
    ('Mapas', 1, 1, 1, None),
]
