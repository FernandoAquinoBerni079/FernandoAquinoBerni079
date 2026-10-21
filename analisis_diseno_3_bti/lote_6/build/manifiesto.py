# -*- coding: utf-8 -*-
"""Manifiesto SHA-256 del lote 6 → lote_6/MANIFIESTO_LOTE_6.json: cada archivo de lote_6/ (salvo el propio manifiesto)
y los archivos del plan anual preliminar regenerados en este lote. El conjunto DR y el banco de variantes V6 no están en el
repositorio y, por lo tanto, tampoco en el manifiesto. Uso: python3 lote_6/build/manifiesto.py (después de los controles)."""
import os, json, hashlib
AQUI = os.path.dirname(os.path.abspath(__file__))
L5 = os.path.dirname(AQUI)
ADS = os.path.dirname(L5)
SALIDA = os.path.join(L5, 'MANIFIESTO_LOTE_6.json')


def entrada(raiz, ruta):
    datos = open(os.path.join(raiz, ruta), 'rb').read()
    return {'ruta': ruta, 'bytes': len(datos), 'sha256': hashlib.sha256(datos).hexdigest()}


archivos = []
for d, carpetas, fs in os.walk(L5):
    carpetas[:] = sorted(c for c in carpetas if c != '__pycache__')
    for f in sorted(fs):
        ruta = os.path.relpath(os.path.join(d, f), L5)
        if os.path.join(L5, ruta) != SALIDA:
            archivos.append(entrada(L5, ruta))
plan = [entrada(ADS, os.path.join('plan_anual', f)) for f in ('plan_anual_preliminar.py', 'plan_anual_preliminar.csv',
                                                               'PLAN_ANUAL_PRELIMINAR.md')]
r = json.load(open(os.path.join(L5, 'resultados_pruebas', 'resumen.json'), encoding='utf8'))['entorno']
v = json.load(open(os.path.join(L5, 'verificacion_resultado.json'), encoding='utf8'))
json.dump({'lote': 'ADS 3.º BTI — lote 6 (Unidad VI, Capítulos 17 y 18), v1.0 (para auditoría)',
           'fecha': r['fecha'][:10],
           'estado': 'Para auditoría independiente. No validado en laboratorios escolares ni aprobado para la venta.',
           'entorno_de_las_pruebas': '%s, PHP %s, SQLite %s (contenedor de construcción; no es una computadora escolar ni '
                                     'Windows)' % (r['sistema'], r['php'], r['sqlite']),
           'verificador': '%d correctos, %d fallos' % (v['correctos'], v['fallos']),
           'reservados': 'No incluidos: el conjunto DR (lote 5) y el banco de variantes V6 son exclusivos del docente y están fuera del repositorio.',
           'archivos': archivos, 'plan_anual': plan},
          open(SALIDA, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('%d archivos del lote y %d del plan anual' % (len(archivos), len(plan)))
