# -*- coding: utf-8 -*-
"""Conjunto de datos de prueba independiente (DP) de la Unidad V — caso Arapoty, ficticio.

Decisión 2 de Fernando (21-oct-2026): un cargador inicializa una copia descartable de la base con este conjunto,
sin modificar la base de la clase ni la referencia docente; es reproducible, comprueba el estado esperado y se niega
a sobrescribir datos. Una parte (DP_MANUAL) la cargan los equipos con sus propias operaciones, para probarlas.

Independencia: todos los códigos están en el rango 1000-1999 (OB-1xxx, ED-1xxx, EJ-1xxx, LE-1xxx), que no usa
ningún lote anterior; los títulos y las fechas (mayo de 2026) no aparecen en ejemplos resueltos, prácticas ni bancos.
El conjunto reservado (DR) NO está acá: es exclusivo del docente y no se publica (ver dr_plantilla.py).
Este módulo genera lote_5/proyecto/cargador_dp/dp.json, que lee cargar_dp.php."""
import os, json

PARAMETROS = [('plazo_dias', 7), ('maximo_estudiante', 2), ('maximo_docente', 5)]
OBRAS = [  # código, título, autor
    ('OB-1001', 'El río de los pájaros', 'Autora de prueba (ficticia)'),
    ('OB-1002', 'Huerta escolar paso a paso', 'Autor de prueba (ficticio)'),
    ('OB-1003', 'Diccionario 100% escolar', 'Equipo de prueba (ficticio)'),
    ('OB-1004', 'Juegos_de_patio', 'Autora de prueba (ficticia)'),
]
EDICIONES = [  # código, obra, editorial y año
    ('ED-1001', 'OB-1001', 'Editorial de prueba, 2020'),
    ('ED-1002', 'OB-1001', 'Editorial de prueba, 2024'),
    ('ED-1003', 'OB-1002', 'Editorial de prueba, 2022'),
    ('ED-1004', 'OB-1003', 'Editorial de prueba, 2019'),
    ('ED-1005', 'OB-1004', 'Editorial de prueba, 2021'),
]
EJEMPLARES = [  # código, edición, activo
    ('EJ-1001', 'ED-1001', 1), ('EJ-1002', 'ED-1001', 1), ('EJ-1003', 'ED-1001', 1), ('EJ-1004', 'ED-1001', 1),
    ('EJ-1005', 'ED-1002', 1), ('EJ-1006', 'ED-1003', 0), ('EJ-1007', 'ED-1004', 1), ('EJ-1008', 'ED-1005', 1),
    ('EJ-1009', 'ED-1003', 1), ('EJ-1010', 'ED-1003', 1), ('EJ-1011', 'ED-1003', 1), ('EJ-1012', 'ED-1003', 1),
]
LECTORES = [  # código, nombre, tipo, curso, activo
    ('LE-1001', 'Lector de prueba 1 (ficticio)', 'estudiante', '1.º BTI', 1),
    ('LE-1002', 'Lector de prueba 2 (ficticio)', 'estudiante', '9.º grado', 1),
    ('LE-1003', 'Lector de prueba 3 (ficticio)', 'docente', None, 1),
    ('LE-1004', 'Lector de prueba 4 (ficticio, egresado)', 'estudiante', '3.º BTI', 0),
    ('LE-1005', 'Lector de prueba 5 (ficticio)', 'estudiante', '2.º BTI', 1),
]
# ejemplar, lector, curso al prestar, salida, vencimiento, devolución
PRESTAMOS = [
    ('EJ-1001', 'LE-1001', '1.º BTI', '2026-05-04', '2026-05-11', None),     # vencido al 12/05
    ('EJ-1002', 'LE-1002', '9.º grado', '2026-05-05', '2026-05-12', None),   # vence el mismo día de la referencia
    ('EJ-1003', 'LE-1002', '9.º grado', '2026-05-06', '2026-05-13', None),   # LE-1002 en su máximo (2)
    ('EJ-1009', 'LE-1003', None, '2026-05-04', '2026-05-11', None),          # docente: 4 activos (uno menos que 5)
    ('EJ-1010', 'LE-1003', None, '2026-05-04', '2026-05-11', None),
    ('EJ-1011', 'LE-1003', None, '2026-05-05', '2026-05-12', None),
    ('EJ-1012', 'LE-1003', None, '2026-05-05', '2026-05-12', None),
    ('EJ-1006', 'LE-1004', '3.º BTI', '2026-03-02', '2026-03-09', '2026-03-06'),   # historial del ejemplar inactivo
    ('EJ-1005', 'LE-1005', '1.º BTI', '2026-04-06', '2026-04-13', '2026-04-10'),   # RI-08: hoy está en 2.º BTI
]
FECHA_REFERENCIA = '2026-05-12'

# Parte manual: la cargan los equipos con SUS operaciones (OA-02, OA-01, OA-03), en este orden, y la comprueban.
# (operación, entradas, mensaje esperado)
DP_MANUAL = [
    ('OA-02', ['OB-1005', 'Mapas del barrio', 'Autora de prueba (ficticia)', 'ED-1006', 'Editorial de prueba, 2023'], 'MA-04'),
    ('OA-01', ['EJ-1013', 'ED-1006'], 'MA-01'),
    ('OA-01', ['EJ-1014', 'ED-1006'], 'MA-01'),
    ('OA-03', ['LE-1006', 'Lector de prueba 6 (ficticio)', 'estudiante', '8.º grado'], 'MA-06'),
]


def estado_esperado():
    """Lo que tiene que haber en la copia después de la carga automática (sin la parte manual)."""
    activos = [p for p in PRESTAMOS if p[5] is None]
    disp = {}
    for o in OBRAS:
        eds = [e[0] for e in EDICIONES if e[1] == o[0]]
        ejs = [x[0] for x in EJEMPLARES if x[1] in eds and x[2] == 1]
        disp[o[0]] = [len(ejs), len([x for x in ejs if x not in [p[0] for p in activos]])]
    return {'obras': len(OBRAS), 'ediciones': len(EDICIONES), 'ejemplares': len(EJEMPLARES),
            'lectores': len(LECTORES), 'prestamos': len(PRESTAMOS), 'prestamos_activos': len(activos),
            'activos_por_lector': {l[0]: len([p for p in activos if p[1] == l[0]]) for l in LECTORES},
            'ejemplares_y_disponibles_por_obra': disp}


def datos():
    return {'conjunto': 'DP (datos de prueba independientes, Unidad V)', 'parametros': PARAMETROS, 'obras': OBRAS,
            'ediciones': EDICIONES, 'ejemplares': EJEMPLARES, 'lectores': LECTORES, 'prestamos': PRESTAMOS,
            'fecha_referencia': FECHA_REFERENCIA, 'manual': DP_MANUAL, 'esperado': estado_esperado()}


def escribir(ruta):
    json.dump(datos(), open(ruta, 'w', encoding='utf8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    escribir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'proyecto', 'cargador_dp', 'dp.json'))
