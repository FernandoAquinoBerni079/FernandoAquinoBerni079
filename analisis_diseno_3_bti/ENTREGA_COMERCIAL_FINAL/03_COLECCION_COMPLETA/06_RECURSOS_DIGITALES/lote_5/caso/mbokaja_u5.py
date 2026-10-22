# -*- coding: utf-8 -*-
"""Caso de transferencia de la Unidad V — Escuela Básica Mbokaja (institución y personas ficticias).

Amplía, sin modificarlas, las fuentes de Mbokaja de los lotes 1 a 4 con los datos nuevos de la Práctica 14
(batería nueva de pruebas). La Práctica 15 (revisión cruzada) usa el conjunto reservado DR del docente, que no se
publica. Códigos nuevos: M-F12, MS-7, MS-8 y los libros y lectores de la carga de la Práctica 14 (correspondencia
fija de la Práctica 11: MB-3xx → EJ-03xx). Ninguno repite un código anterior.
Este módulo genera lote_5/proyecto/cargador_dp/mbokaja_p14.json, que carga cargar_dp.php --datos=..."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(ADS, 'lote_4', 'caso'))
import mbokaja_u4 as MB4

DATOS_TITULO = 'Datos nuevos de Mbokaja (caso de práctica, ficticio)'
DATOS = [
    ('M-F12', 'El encargado anota los feriados en el registro. Si un préstamo vence en feriado, el lector puede devolverlo '
              'el día hábil siguiente sin que cuente como atraso.'),
]
SITUACIONES_TITULO = 'Situaciones nuevas (caso de práctica, ficticio)'
SITUACIONES = [
    ('MS-7', 'El miércoles 15 de julio es feriado. Un libro prestado el 8 de julio vence ese día.'),
    ('MS-8', 'Un voluntario escribió la etiqueta de un libro con dos cifras (MB-30) en lugar de tres.'),
]
# Carga de la Práctica 14 (mismo formato que dp.json): libros MB-301 a MB-305 → EJ-0301 a EJ-0305
P14 = {
    'conjunto': 'Mbokaja, Práctica 14 (caso de práctica, ficticio)',
    'parametros': [['plazo_dias', 7], ['maximo_estudiante', 2], ['maximo_docente', 5]],
    'obras': [['OB-0340', 'Leyendas del monte', 'Autora del caso (ficticia)'],
              ['OB-0350', 'Matemática en la cocina', 'Autor del caso (ficticio)']],
    'ediciones': [['ED-0340', 'OB-0340', 'Donación Mbokaja'], ['ED-0350', 'OB-0350', 'Donación Mbokaja']],
    'ejemplares': [['EJ-0301', 'ED-0340', 1], ['EJ-0302', 'ED-0340', 1], ['EJ-0303', 'ED-0340', 1],
                   ['EJ-0304', 'ED-0350', 1], ['EJ-0305', 'ED-0350', 0]],
    'lectores': [['LE-0321', 'Lector Mbokaja 21 (ficticio)', 'estudiante', '5.º grado', 1],
                 ['LE-0322', 'Lector Mbokaja 22 (ficticio)', 'estudiante', '6.º grado', 1],
                 ['LE-0323', 'Lector Mbokaja 23 (ficticio)', 'docente', None, 1]],
    'prestamos': [['EJ-0301', 'LE-0321', '5.º grado', '2026-07-08', '2026-07-15', None],
                  ['EJ-0302', 'LE-0322', '6.º grado', '2026-07-09', '2026-07-16', None],
                  ['EJ-0305', 'LE-0322', '6.º grado', '2026-06-01', '2026-06-08', '2026-06-05']],
    'fecha_referencia': '2026-07-16',
    'manual': [],
}
CORRESPONDENCIA_NOTA = ('Las etiquetas MB- y tres cifras se escriben EJ-0 y las mismas cifras (MB-301 → EJ-0301), como en la '
                        'Práctica 11. MB-30, la de dos cifras, se escribe tal cual.')
# Casos que la guía comprueba sobre la referencia v2 (la carga y la regla del feriado): (id, requisito, operación,
# cuenta, entradas, código esperado, nota)
CASOS_P14 = [
    ('M-01', 'RF-08', 'OP-04', 'bibliotecaria', ['2026-07-16'], None,
     'EJ-0301 aparece vencido el 16/07, aunque el 15 fue feriado: la regla M-F12 no está en el sistema'),
    ('M-02', 'RF-05', 'OP-01', 'bibliotecaria', ['LE-0322', 'EJ-0303', '2026-07-16'], 'ME-04', 'Segundo préstamo de LE-0322: se registra'),
    ('M-03', 'RF-05', 'OP-01', 'bibliotecaria', ['LE-0322', 'EJ-0304', '2026-07-16'], 'ME-02', 'Tercer préstamo: máximo de estudiantes'),
    ('M-04', 'RF-10', 'OP-01', 'bibliotecaria', ['LE-0323', 'EJ-0305', '2026-07-16'], 'MV-06', 'Ejemplar dado de baja'),
    ('M-05', 'RF-04', 'OP-01', 'bibliotecaria', ['LE-0323', 'EJ-0301', '2026-07-16'], 'ME-03', 'Ejemplar ya prestado'),
    ('M-06', 'RF-07', 'OA-01', 'bibliotecaria', ['MB-30', 'ED-0340'], 'MV-02', 'Etiqueta con dos cifras (MS-8)'),
]


def p14_json():
    d = dict(P14)
    act = [p for p in d['prestamos'] if p[5] is None]
    disp = {}
    for o in d['obras']:
        eds = [e[0] for e in d['ediciones'] if e[1] == o[0]]
        ejs = [x[0] for x in d['ejemplares'] if x[1] in eds and x[2] == 1]
        disp[o[0]] = [len(ejs), len([x for x in ejs if x not in [p[0] for p in act]])]
    d['esperado'] = {'obras': len(d['obras']), 'ediciones': len(d['ediciones']), 'ejemplares': len(d['ejemplares']),
                     'lectores': len(d['lectores']), 'prestamos': len(d['prestamos']), 'prestamos_activos': len(act),
                     'activos_por_lector': {l[0]: len([p for p in act if p[1] == l[0]]) for l in d['lectores']},
                     'ejemplares_y_disponibles_por_obra': disp}
    return d


def casos_p14_json():
    out = []
    for c in CASOS_P14:
        control = {'filas': [({'ejemplar': 'EJ-0301'}, {'vencido': 1})]} if c[0] == 'M-01' else None
        out.append({'id': c[0], 'requisito': c[1], 'clase': '', 'descripcion': c[6], 'operacion': c[2], 'cuenta': c[3],
                    'entradas': c[4], 'esperado_codigo': c[5], 'control': control, 'esperado': c[6]})
    return out


FUENTES = dict(DATOS + SITUACIONES)
FUENTES.update(MB4.FUENTES)

if __name__ == '__main__':
    json.dump(p14_json(), open(os.path.join(os.path.dirname(AQUI), 'proyecto', 'cargador_dp', 'mbokaja_p14.json'), 'w',
                               encoding='utf8'), ensure_ascii=False, indent=1)
