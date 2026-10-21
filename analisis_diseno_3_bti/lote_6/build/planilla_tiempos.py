# -*- coding: utf-8 -*-
"""Planilla de tiempos del Encuentro 35 (decisión D-5) → lote_6/instrumentos/planilla_tiempos_encuentro_35.xlsx.
El docente escribe la cantidad de equipos y de estudiantes, los minutos de cada HC de su institución (no se suponen),
los minutos por demostración, por cambio y por defensa, y las recuperaciones previstas. La planilla calcula, con un solo
evaluador, si todo entra en el Encuentro 35 (alternativa A), cuántas defensas pasan al 36 (alternativa B) y cuántos
minutos necesitan tiempo institucional autorizado (B+). Las fórmulas son las de caso/instrumentos_u6.py: tiempos().

v1.1 (auditoría del lote 6): los minutos que pasan al Encuentro 36 son defensas enteras × minutos por defensa (más los
minutos de demostración que no entraron, si las demostraciones solas superan el Encuentro 35); la planilla comprueba que
los datos sean enteros positivos y, si no lo son, no calcula (no hay división por cero). La comprobación recalcula la
planilla con pycel (un evaluador de fórmulas independiente) y la compara con tiempos() en casos de límite.
Uso: python3 lote_6/build/planilla_tiempos.py   (escribe y comprueba; sale con 1 si algo no coincide)"""
import os, sys, tempfile, shutil
AQUI = os.path.dirname(os.path.abspath(__file__))
L6 = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(L6, 'caso'))
import instrumentos_u6 as I
RUTA = os.path.join(L6, 'instrumentos', 'planilla_tiempos_encuentro_35.xlsx')
# Entradas en B4:B11 (orden de I.TIEMPOS_CAMPOS). B13: datos válidos. Resultados desde la fila 14.
_MIN = [I.VALIDACION[k] for k, _, _ in I.TIEMPOS_CAMPOS]
VALIDOS = ('=IF(AND(' + ','.join('ISNUMBER(B%d),INT(B%d)=B%d,B%d>=%d' % (f, f, f, f, m) for f, m in zip(range(4, 12), _MIN))
           + '),"Sí","No: revisá los datos (enteros; equipos, estudiantes, minutos de la HC, de la demostración y de la '
             'defensa, mayores que 0)")')
G = lambda f: '=IF($B$13<>"Sí","—",%s)' % f   # no se calcula con datos inválidos
SALIDAS = [  # (etiqueta, fórmula, clave de I.tiempos)
    ('Minutos de demostraciones', G('B4*(B7+B8)'), 'demostraciones'),
    ('Minutos de defensas individuales', G('B5*B9'), 'defensas'),
    ('Minutos requeridos en el Encuentro 35', G('B14+B15'), 'requerido_35'),
    ('Minutos disponibles en el Encuentro 35 (5 HC)', G('5*B6'), 'disponible_35'),
    ('Diferencia en el Encuentro 35 (negativo: no alcanza)', G('B17-B16'), 'diferencia_35'),
    ('Minutos de demostración que no entran en el Encuentro 35', G('MAX(0,B14-B17)'), 'demostraciones_excedentes'),
    ('Defensas que pasan al Encuentro 36 (enteras)', G('IF(B18>=0,0,IF(B19>0,B5,ROUNDUP(-B18/B9,0)))'), 'defensas_que_pasan_al_36'),
    ('Minutos trasladados al Encuentro 36 (defensas × minutos por defensa, más demostraciones)', G('B20*B9+B19'),
     'minutos_trasladados_al_36'),
    ('Minutos de recuperaciones en el Encuentro 36', G('B10*B11'), 'recuperaciones_36'),
    ('Minutos de evaluación disponibles en el Encuentro 36 (3 HC)', G('3*B6'), 'disponible_36'),
    ('Diferencia en el Encuentro 36 (negativo: no alcanza)', G('B23-B22-B21'), 'diferencia_36'),
    ('Alternativa', G('IF(B18>=0,"A",IF(B24>=0,"B","B + calendario institucional autorizado"))'), 'alternativa'),
    ('Minutos sin lugar (requieren tiempo institucional autorizado)', G('MAX(0,-B24)'), 'minutos_sin_lugar'),
    ('Aviso', G('IF(B19>0,"Las demostraciones solas superan el Encuentro 35","")'), 'aviso'),
]
FILA_ALTERNATIVAS = 14 + len(SALIDAS) + 1


def escribir(valores=None, ruta=None):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill
    from openpyxl.worksheet.datavalidation import DataValidation
    v = valores or I.EJEMPLO_TIEMPOS
    wb = Workbook(); ws = wb.active; ws.title = 'Encuentro 35'
    ws['A1'] = 'Planilla de tiempos del Encuentro 35 — demostración y defensa individual (un solo evaluador)'
    ws['A1'].font = Font(bold=True)
    ws['A2'] = ('Escribí tus valores en la columna B (celdas amarillas). Los de ejemplo son ficticios: no son la duración '
                'de la HC de ninguna institución.')
    ws['A3'] = 'Dato'; ws['B3'] = 'Valor'; ws['C3'] = 'Quién lo escribe'
    amarillo = PatternFill('solid', fgColor='FFF2CC')
    for i, (k, que, quien) in enumerate(I.TIEMPOS_CAMPOS, start=4):
        ws['A%d' % i] = que; ws['B%d' % i] = v[k]; ws['C%d' % i] = quien
        ws['B%d' % i].fill = amarillo
        dv = DataValidation(type='whole', operator='greaterThanOrEqual', formula1=str(I.VALIDACION[k]), showErrorMessage=True,
                            error='Escribí un número entero mayor o igual que %d.' % I.VALIDACION[k])
        ws.add_data_validation(dv); dv.add('B%d' % i)
    ws['A12'] = 'Resultado'; ws['A12'].font = Font(bold=True)
    ws['A13'] = '¿Los datos son válidos?'; ws['B13'] = VALIDOS
    for i, (et, f, _) in enumerate(SALIDAS, start=14):
        ws['A%d' % i] = et; ws['B%d' % i] = f
    ws['A%d' % FILA_ALTERNATIVAS] = 'Alternativas'; ws['A%d' % FILA_ALTERNATIVAS].font = Font(bold=True)
    for i, (cod, tit, texto) in enumerate(I.ALTERNATIVAS, start=FILA_ALTERNATIVAS + 1):
        ws['A%d' % i] = '%s. %s' % (cod, tit); ws['B%d' % i] = texto
    ws.column_dimensions['A'].width = 70; ws.column_dimensions['B'].width = 44; ws.column_dimensions['C'].width = 24
    destino = ruta or RUTA
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    wb.save(destino)
    return destino


def recalcular(valores):
    """Valores de la planilla (B13 y resultados) recalculados por pycel, sobre una copia temporal."""
    from pycel import ExcelCompiler
    tmp = tempfile.mkdtemp(prefix='ads_planilla_')
    try:
        x = escribir(valores, os.path.join(tmp, 'p.xlsx'))
        xl = ExcelCompiler(filename=x)
        return xl.evaluate('Encuentro 35!B13'), {clave: xl.evaluate('Encuentro 35!B%d' % i)
                                                  for i, (_, _, clave) in enumerate(SALIDAS, start=14)}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _igual(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return (a or '') == (b or '')
    return abs(float(a) - float(b)) < 1e-9


EJ = I.EJEMPLO_TIEMPOS
CASOS = [  # (nombre, valores, qué se espera: claves de tiempos() o 'inválido')
    ('Ejemplo de control de la auditoría', EJ,
     {'defensas_que_pasan_al_36': 2, 'minutos_trasladados_al_36': 12, 'diferencia_36': 48, 'alternativa': 'B'}),
    ('Límite A/B: el Encuentro 35 alcanza justo (diferencia 0)', dict(EJ, estudiantes=27, min_defensa=5),
     {'diferencia_35': 0, 'alternativa': 'A', 'defensas_que_pasan_al_36': 0}),
    ('Límite A/B: falta un minuto (pasa una defensa entera)', dict(EJ, estudiantes=17, min_defensa=8),
     {'diferencia_35': -1, 'alternativa': 'B', 'defensas_que_pasan_al_36': 1, 'minutos_trasladados_al_36': 8}),
    ('Límite B/B+: el Encuentro 36 alcanza justo (diferencia 0)', dict(EJ, recuperaciones=41, min_recuperacion=3),
     {'diferencia_36': 0, 'alternativa': 'B', 'minutos_sin_lugar': 0}),
    ('Límite B/B+: falta un minuto en el Encuentro 36', dict(EJ, recuperaciones=1, min_recuperacion=124),
     {'diferencia_36': -1, 'alternativa': 'B + calendario institucional autorizado', 'minutos_sin_lugar': 1}),
    ('Las demostraciones solas superan el Encuentro 35', dict(EJ, equipos=16, min_demo=12, min_cambio=3),
     {'demostraciones_excedentes': 15, 'defensas_que_pasan_al_36': 24, 'minutos_trasladados_al_36': 159,
      'aviso': 'Las demostraciones solas superan el Encuentro 35'}),
    ('Sin recuperaciones ni cambio entre equipos (ceros permitidos)', dict(EJ, recuperaciones=0, min_cambio=0),
     {'recuperaciones_36': 0}),
    ('Inválido: minutos por defensa 0 (división por cero)', dict(EJ, min_defensa=0), 'inválido'),
    ('Inválido: estudiantes negativos', dict(EJ, estudiantes=-3), 'inválido'),
    ('Inválido: minutos de la HC 0', dict(EJ, min_hc=0), 'inválido'),
    ('Inválido: equipos con decimales', dict(EJ, equipos=2.5), 'inválido'),
]


def comprobar_casos():
    res = []
    for nombre, v, esperado in CASOS:
        validez, xl = recalcular(v)
        if esperado == 'inválido':
            try:
                I.tiempos(**v); py_rechaza = False
            except ValueError:
                py_rechaza = True
            bien = py_rechaza and str(validez).startswith('No') and all(x == '—' for x in xl.values())
            res.append((nombre, bien, 'la función rechaza: %s; la planilla no calcula: %s' % (py_rechaza, str(validez)[:2])))
            continue
        t = I.tiempos(**v)
        iguales = all(_igual(t[k], xl[k]) for k in t)
        esperados = all(_igual(t[k], e) for k, e in esperado.items())
        res.append((nombre, validez == 'Sí' and iguales and esperados,
                    'planilla = función: %s; valores esperados: %s' % (iguales, esperados)))
    return res


if __name__ == '__main__':
    escribir()
    r = comprobar_casos()
    for nombre, bien, det in r:
        print('%s %s — %s' % ('CORRECTO' if bien else 'FALLA   ', nombre, det))
    print('Resultado: %d de %d casos correctos' % (sum(b for _, b, _ in r), len(r)))
    sys.exit(0 if all(b for _, b, _ in r) else 1)
