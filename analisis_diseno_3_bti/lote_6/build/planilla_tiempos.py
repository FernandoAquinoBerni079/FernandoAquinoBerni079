# -*- coding: utf-8 -*-
"""Planilla de tiempos del Encuentro 35 (decisión D-5) → lote_6/instrumentos/planilla_tiempos_encuentro_35.xlsx.
El docente escribe la cantidad de equipos y de estudiantes, los minutos de cada HC de su institución (no se suponen),
los minutos por demostración, por cambio y por defensa, y las recuperaciones previstas. La planilla calcula, con un solo
evaluador, si todo entra en el Encuentro 35 (alternativa A), cuántas defensas pasan al 36 (alternativa B) y cuántos
minutos necesitan tiempo institucional autorizado (B+). Las fórmulas son las de caso/instrumentos_u6.py: tiempos(); la
comprobación recalcula la planilla con pycel (evaluador independiente) y compara con esa función.
Uso: python3 lote_6/build/planilla_tiempos.py   (escribe y comprueba)"""
import os, sys, tempfile, shutil
AQUI = os.path.dirname(os.path.abspath(__file__))
L6 = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(L6, 'caso'))
import instrumentos_u6 as I
RUTA = os.path.join(L6, 'instrumentos', 'planilla_tiempos_encuentro_35.xlsx')
SALIDAS = [  # (etiqueta, fórmula con las celdas de entrada B4:B11, clave de I.tiempos)
    ('Minutos de demostraciones', '=B4*(B7+B8)', 'demostraciones'),
    ('Minutos de defensas individuales', '=B5*B9', 'defensas'),
    ('Minutos requeridos en el Encuentro 35', '=B14+B15', 'requerido_35'),
    ('Minutos disponibles en el Encuentro 35 (5 HC)', '=5*B6', 'disponible_35'),
    ('Diferencia en el Encuentro 35 (negativo: no alcanza)', '=B17-B16', 'diferencia_35'),
    ('Defensas que pasan al Encuentro 36', '=IF(B18<0,ROUNDUP(-B18/B9,0),0)', 'defensas_que_pasan_al_36'),
    ('Minutos de recuperaciones en el Encuentro 36', '=B10*B11', 'recuperaciones_36'),
    ('Minutos de evaluación disponibles en el Encuentro 36 (3 HC)', '=3*B6', 'disponible_36'),
    ('Diferencia en el Encuentro 36 (negativo: no alcanza)', '=B21-B20-MAX(0,-B18)', 'diferencia_36'),
    ('Alternativa', '=IF(B18>=0,"A",IF(B22>=0,"B","B + calendario institucional autorizado"))', 'alternativa'),
    ('Minutos sin lugar (requieren tiempo institucional autorizado)', '=MAX(0,-B22)', 'minutos_sin_lugar'),
]


def escribir(valores=None):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill
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
    ws['A13'] = 'Resultado'; ws['A13'].font = Font(bold=True)
    for i, (et, f, _) in enumerate(SALIDAS, start=14):
        ws['A%d' % i] = et; ws['B%d' % i] = f
    ws['A26'] = 'Alternativas'; ws['A26'].font = Font(bold=True)
    for i, (cod, tit, texto) in enumerate(I.ALTERNATIVAS, start=27):
        ws['A%d' % i] = '%s. %s' % (cod, tit); ws['B%d' % i] = texto
    ws.column_dimensions['A'].width = 62; ws.column_dimensions['B'].width = 40; ws.column_dimensions['C'].width = 24
    os.makedirs(os.path.dirname(RUTA), exist_ok=True)
    wb.save(RUTA)
    return RUTA


def comprobar(valores=None):
    """Recalcula la planilla con pycel (un evaluador de fórmulas de Excel independiente de este programa) y compara cada
    resultado con I.tiempos(). En el entorno de construcción no hay LibreOffice Calc; la planilla se abre también en
    Excel o en LibreOffice Calc, que calculan las mismas fórmulas."""
    from pycel import ExcelCompiler
    v = valores or I.EJEMPLO_TIEMPOS
    tmp = tempfile.mkdtemp(prefix='ads_planilla_')
    try:
        x = os.path.join(tmp, 'p.xlsx')
        escribir(v); shutil.copy2(RUTA, x)
        xl = ExcelCompiler(filename=x)
        esperado = I.tiempos(**v)
        res = []
        for i, (et, _, clave) in enumerate(SALIDAS, start=14):
            obtenido = xl.evaluate('Encuentro 35!B%d' % i)
            e = esperado[clave]
            bien = obtenido == e or (isinstance(e, (int, float)) and isinstance(obtenido, (int, float)) and abs(obtenido - e) < 1e-9)
            res.append((et, e, obtenido, bien))
        return res
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    escribir()
    casos = [I.EJEMPLO_TIEMPOS, dict(I.EJEMPLO_TIEMPOS, estudiantes=18), dict(I.EJEMPLO_TIEMPOS, estudiantes=40, recuperaciones=8)]
    fallos = 0
    for c in casos:
        r = comprobar(c)
        fallos += sum(not b for *_, b in r)
        print('Caso', {k: c[k] for k in ('equipos', 'estudiantes', 'min_hc', 'recuperaciones')}, '→',
              [x for x in r if x[0] == 'Alternativa'][0][2], '·', sum(b for *_, b in r), 'de', len(r), 'coinciden')
    escribir()   # deja la planilla con los valores de ejemplo
    sys.exit(1 if fallos else 0)
