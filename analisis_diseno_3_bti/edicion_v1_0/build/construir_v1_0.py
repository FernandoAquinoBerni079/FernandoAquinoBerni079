# -*- coding: utf-8 -*-
"""Construcción completa de la edición comercial v1.0, en orden: documentos de la colección, planificación, cubiertas,
paquete ENTREGA_COMERCIAL_FINAL/, auditoría final y cierre (informe, manifiesto y ZIP). Se detiene en el primer paso
que falle. Lee edicion_v1_0/datos_edicion.json: completar ahí titular, editor e ISBN y volver a ejecutar.
Uso: ADS_DIC=<diccionario Hunspell de español, sin extensión> ADS_MEC_PDF=<copia del Diseño Curricular del MEC> python3 -B analisis_diseno_3_bti/edicion_v1_0/build/construir_v1_0.py
"""
import os, subprocess, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
PASOS = ['documentos_coleccion.py', 'plan/extraer_coleccion.py', 'plan/planes_clase.py', 'plan/plan_anual.py',
         'plan/prueba_fuentes_plan.py', 'plan/controles_plan.py', 'cubiertas.py', 'empaquetar.py', 'auditoria_final.py',
         'cierre_entrega.py']

for paso in PASOS:
    print('\n=== %s' % paso, flush=True)
    r = subprocess.run([sys.executable, '-B', os.path.join(AQUI, paso)])
    if r.returncode:
        sys.exit('Falló %s (código %d): la construcción se detiene.' % (paso, r.returncode))
print('\nEdición v1.0 construida y verificada.')
