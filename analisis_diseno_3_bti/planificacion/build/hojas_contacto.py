# -*- coding: utf-8 -*-
"""Hojas de contacto para la revisión visual: todas las páginas del plan anual y de los planes de clase, seis por hoja.
Uso: python3 -B planificacion/build/hojas_contacto.py  →  planificacion/revision_visual/*.png"""
import os, sys
import pymupdf
from PIL import Image
AQUI = os.path.dirname(os.path.abspath(__file__)); PLAN = os.path.dirname(AQUI)
SAL = os.path.join(PLAN, 'revision_visual'); os.makedirs(SAL, exist_ok=True)
for viejo in os.listdir(SAL):   # las hojas de una corrida anterior
    if viejo.endswith('.png') and viejo.startswith(('plan_anual_pags_', 'planes_pags_')):
        os.remove(os.path.join(SAL, viejo))
for nombre, corto in (('ADS_3BTI_PLAN_ANUAL_OFICIO_O3', 'plan_anual'), ('ADS_3BTI_PLANES_DE_CLASE_OFICIO_O3', 'planes')):
    pdf = pymupdf.open(os.path.join(PLAN, nombre + '.pdf'))
    ims = []
    for p in pdf:
        px = p.get_pixmap(dpi=55)
        ims.append(Image.frombytes('RGB', (px.width, px.height), px.samples))
    for k in range(0, len(ims), 6):
        grupo = ims[k:k + 6]
        w = max(i.width for i in grupo); h = max(i.height for i in grupo)
        hoja = Image.new('RGB', (w * 3 + 20, h * 2 + 10), 'white')
        for j, im in enumerate(grupo):
            hoja.paste(im, ((j % 3) * (w + 10), (j // 3) * (h + 10)))
        hoja.save(os.path.join(SAL, '%s_pags_%03d-%03d.png' % (corto, k + 1, k + len(grupo))), optimize=True)
print(sorted(os.listdir(SAL)))
