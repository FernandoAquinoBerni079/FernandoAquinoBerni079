# -*- coding: utf-8 -*-
"""Estima el cuerpo (pt) de cada línea de texto de una figura raster al ancho de impresión.

Método: contraste local (píxel frente a la mediana de su entorno) → componentes conexas con forma de glifo →
agrupación en líneas por solapamiento vertical y cercanía horizontal → altura de línea = altura de la caja de las
letras más altas (máxima altura de componente de la línea). Cuerpo ≈ esa altura / 0,68 (altura
de mayúsculas de Carlito = 0,65 em; ascendentes ≈ 0,70 em). Calibrado con texto de cuerpo conocido; error ±8 %.
Uso: python3 legibilidad.py <ancho_cm> <png> [...]   → lista de líneas ordenadas por cuerpo, con su recorte.
"""
import sys, os
import numpy as np
from PIL import Image
from scipy import ndimage


def lineas(ruta):
    g = np.asarray(Image.open(ruta).convert('L')).astype(float)
    fondo = ndimage.median_filter(g, size=31)
    m = np.abs(g - fondo) > 55
    lab, n = ndimage.label(m)
    objs = ndimage.find_objects(lab)
    comps = []
    for i, sl in enumerate(objs):
        h = sl[0].stop - sl[0].start; w = sl[1].stop - sl[1].start
        area = (lab[sl] == i + 1).sum()
        if 5 <= h <= 90 and 1 <= w <= 90 and area >= 6 and area / (h * w) < 0.9:
            comps.append((sl[0].start, sl[0].stop, sl[1].start, sl[1].stop, h))
    comps.sort(key=lambda c: (c[0], c[2]))
    grupos = []
    for c in comps:
        for gr in grupos:
            y0, y1, x0, x1 = gr['caja']
            ov = min(y1, c[1]) - max(y0, c[0])
            if ov > 0.5 * min(y1 - y0, c[4]) and (c[2] - x1) < 2.2 * max(c[4], y1 - y0) and c[3] > x0 - 2.2 * c[4]:
                gr['c'].append(c); gr['caja'] = (min(y0, c[0]), max(y1, c[1]), min(x0, c[2]), max(x1, c[3])); break
        else:
            grupos.append({'c': [c], 'caja': (c[0], c[1], c[2], c[3])})
    res = []
    for gr in grupos:
        if len(gr["c"]) < 3:            # menos de 3 glifos: íconos, flechas, números sueltos
            continue
        hs = sorted(c[4] for c in gr['c'])
        res.append((float(hs[-1]), gr["caja"], len(gr["c"])))
    return g.shape[1], res


if __name__ == '__main__':
    ancho = float(sys.argv[1])
    for ruta in sys.argv[2:]:
        w, ls = lineas(ruta)
        pxcm = w / ancho
        filas = sorted((h / pxcm / 0.03528 / 0.68, caja, n) for h, caja, n in ls)
        chicas = [f for f in filas if f[0] < 7.0]
        print('%s  líneas %d  mín %.1f pt  <7 pt: %d' % (os.path.basename(ruta), len(filas), filas[0][0] if filas else 0, len(chicas)))
        for pt, (y0, y1, x0, x1), n in chicas[:12]:
            print('    %.1f pt  y=%d-%d x=%d-%d  glifos=%d' % (pt, y0, y1, x0, x1, n))
