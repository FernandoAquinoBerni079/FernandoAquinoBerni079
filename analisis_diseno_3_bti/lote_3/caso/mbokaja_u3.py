# -*- coding: utf-8 -*-
"""Caso de transferencia de la Unidad III — Escuela Básica Mbokaja (institución y personas ficticias).

Amplía, sin modificarlos, `lote_1/caso/mbokaja.py` y `lote_2/caso/mbokaja_u2.py` con los datos nuevos de las Prácticas
7, 8 y 9 (Work §7.4: otro conjunto de datos y una decisión nueva en cada práctica).
  - Práctica 7: pérdida y reposición de un ejemplar, devoluciones sin anotar y la doble carga de un préstamo.
  - Práctica 8: una sesión de uso del boceto con tres personas; el voluntario de 9.º es menor de edad y trabaja con
    supervisión: sirve para decidir permisos mínimos y privacidad, sin suponer acceso a datos personales ni a
    funciones administrativas.
  - Práctica 9: contrato de la devolución con el libro dañado y la reposición, y el mantenimiento del entorno.
Códigos que siguen la numeración de Mbokaja: M-F8 y M-F9 (datos), MS-3 a MS-5 (situaciones), OBS-1 a OBS-6
(observaciones de la sesión)."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(ADS, 'lote_2', 'caso'))
import mbokaja_u2 as MB2
MB = MB2.MB

INSTITUCION = MB.INSTITUCION

DATOS_TITULO = 'Datos nuevos de Mbokaja (caso de práctica, ficticio)'
DATOS = [
    ('M-F8', 'Los libros de la lectura obligatoria del mes tienen tres ejemplares cada uno; los demás libros, uno solo.'),
    ('M-F9', 'Nadie en la escuela sabe instalar programas. El profesor de informática de un colegio vecino puede venir una vez por mes.'),
]
SITUACIONES_TITULO = 'Situaciones nuevas (caso de práctica, ficticio)'
SITUACIONES = [
    ('MS-3', 'Un lector perdió un ejemplar de la lectura obligatoria. Su familia lo repuso con otro ejemplar de la misma edición, como pide la norma M-N5.'),
    ('MS-4', 'Un miércoles, dos voluntarios de 9.º cargaron por separado el mismo préstamo: el mismo libro, el mismo lector y la misma fecha.'),
    ('MS-5', 'Los voluntarios de 9.º ayudan los miércoles, siempre con el encargado presente. Son estudiantes menores de edad.'),
]

OBSERVACIONES_TITULO = 'Registro de la sesión de uso del boceto en Mbokaja (caso de práctica, ficticio)'
# (código, quién, tarea, qué se observó)
OBSERVACIONES = [
    ('OBS-1', 'Voluntario de 9.º', 'Registrar un préstamo', 'Al buscar al lector, la pantalla le mostró el nombre, el grado y el teléfono de la familia.'),
    ('OBS-2', 'Encargado', 'Registrar una devolución', 'No encontró dónde hacerlo: el botón decía «Cerrar transacción».'),
    ('OBS-3', 'Estudiante del turno mañana', 'Consultar si hay un libro', 'Escribió una palabra del título y la pantalla quedó en blanco, sin ningún mensaje.'),
    ('OBS-4', 'Voluntario de 9.º', 'Registrar un préstamo', 'Pulsó dos veces «Guardar» porque la pantalla no cambió, y quedaron dos préstamos iguales.'),
    ('OBS-5', 'Encargado', 'Registrar un préstamo', 'Con la tecla Tab, el cursor saltó del campo «Libro» al botón «Borrar todo».'),
    ('OBS-6', 'Encargado', 'Registrar un préstamo', 'Apareció un recuadro rojo sin texto; no supo qué había pasado ni qué hacer.'),
]

FUENTES = dict(DATOS + SITUACIONES + [(c, t) for c, _, _, t in OBSERVACIONES])
FUENTES.update(MB2.FUENTES)
