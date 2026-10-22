# -*- coding: utf-8 -*-
"""Cuerpo (pt) de una línea de texto dentro de una caja de una figura, al ancho de impresión dado.
Altura de referencia = componente más alta de la línea (mayúscula o ascendente ≈ 0,70 em en Carlito y sans afines).
Uso desde Python: cuerpo(ruta, (x0, y0, x1, y1), ancho_cm)."""
import numpy as np
from PIL import Image
from scipy import ndimage


def cuerpo(ruta, caja, ancho_cm):
    im = Image.open(ruta).convert('L'); W = im.size[0]
    g = np.asarray(im.crop(caja)).astype(float)
    fondo = np.median(g)
    m = np.abs(g - fondo) > 70
    lab, n = ndimage.label(m)
    hs = sorted(sl[0].stop - sl[0].start for sl in ndimage.find_objects(lab) if (sl[1].stop - sl[1].start) < 3 * (sl[0].stop - sl[0].start) + 4)
    if not hs:
        return None
    med = np.median(hs)
    h = max(x for x in hs if x <= 1.7 * med)
    px_por_pt = W / (ancho_cm / 2.54 * 72)
    return h / px_por_pt / 0.70
