# -*- coding: utf-8 -*-
"""Regenera la planificación completa, en orden: extracción de la colección aprobada, planes de clase (dos vueltas para
las páginas), plan anual, controles, prueba de fuentes, hojas de contacto y manifiesto. Guarda la salida de cada paso
en planificacion/evidencias/. Se detiene en el primer paso que falle.
Uso: ADS_MEC_PDF=<copia del Diseño Curricular> python3 -B planificacion/build/construir_todo.py"""
import os, subprocess, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); PLAN = os.path.dirname(AQUI)
EVID = os.path.join(PLAN, 'evidencias'); os.makedirs(EVID, exist_ok=True)
PASOS = ['extraer_coleccion', 'planes_clase', 'plan_anual', 'controles_plan', 'prueba_fuentes_plan', 'hojas_contacto',
         'manifiesto_plan']
for paso in PASOS:
    r = subprocess.run([sys.executable, '-B', os.path.join(AQUI, paso + '.py')], capture_output=True, text=True)
    salida = r.stdout + r.stderr
    salida = '\n'.join(l for l in salida.splitlines() if 'fitz' not in l)
    open(os.path.join(EVID, 'salida_%s.txt' % paso), 'w', encoding='utf8').write(salida + '\n')
    print('%-22s %s' % (paso, 'correcto' if r.returncode == 0 else 'FALLA'))
    if r.returncode:
        print(salida[-2000:]); sys.exit(1)
