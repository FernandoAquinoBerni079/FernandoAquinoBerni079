# -*- coding: utf-8 -*-
"""Hojas de contacto para la revisión visual: n páginas por hoja, con el número de página rotulado."""
import os, sys
import pymupdf
from PIL import Image, ImageDraw


def hojas(pdf, destino, prefijo, por_hoja=6, columnas=3, dpi=58):
    d = pymupdf.open(pdf); os.makedirs(destino, exist_ok=True); salidas = []
    for a in range(0, len(d), por_hoja):
        imgs = []
        for i in range(a, min(a + por_hoja, len(d))):
            pm = d[i].get_pixmap(dpi=dpi)
            im = Image.frombytes('RGB', (pm.width, pm.height), pm.samples)
            ImageDraw.Draw(im).rectangle((0, 0, im.width - 1, im.height - 1), outline=(150, 150, 150))
            ImageDraw.Draw(im).text((6, 4), 'p. %d' % (i + 1), fill=(200, 0, 0))
            imgs.append(im)
        w = max(i.width for i in imgs); h = max(i.height for i in imgs)
        filas = (len(imgs) + columnas - 1) // columnas
        lienzo = Image.new('RGB', (columnas * w + (columnas + 1) * 8, filas * h + (filas + 1) * 8), 'white')
        for k, im in enumerate(imgs):
            lienzo.paste(im, (8 + (k % columnas) * (w + 8), 8 + (k // columnas) * (h + 8)))
        ruta = os.path.join(destino, '%s_%02d-%02d.png' % (prefijo, a + 1, min(a + por_hoja, len(d))))
        lienzo.save(ruta, optimize=True); salidas.append(ruta)
    return salidas


if __name__ == '__main__':
    for r in hojas(sys.argv[1], sys.argv[2], sys.argv[3], *(int(x) for x in sys.argv[4:])):
        print(r)
