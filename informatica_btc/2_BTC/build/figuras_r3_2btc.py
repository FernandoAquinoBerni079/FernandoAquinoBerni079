# -*- coding: utf-8 -*-
"""Figuras R3 de Informática 2.º BTC, a partir de las R2 (que no se modifican).

- Figura 1: el ícono verde de la barra de título, parecido al de una planilla comercial (O-2-05), se reemplaza por un
  ícono neutro de cuadrícula en el azul de la colección.
- Figura 2: la celda B3 mostraba «900.000». En el caso, la columna B es Régimen y el importe está en C (Figura 1:
  Cliente 2 · SIMPLE · 900.000). Se reemplaza por «SIMPLE» en los dos paneles (celda y rango).
- Las demás figuras se copian sin cambios: en el tomo, a 15,5 cm, ningún texto queda por debajo de 7,8 pt
  (medición en `LEGIBILIDAD_R3_2BTC.md`). El problema de 4-6 pt estaba en el laboratorio, donde las figuras iban
  reducidas; en R3 el laboratorio las usa a 15,5 cm.
Uso: python3 figuras_r3_2btc.py <carpeta figuras R2> <carpeta salida R3>
"""
import os, shutil, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

REGULAR = '/usr/local/share/fonts/carlito/Carlito-Regular.ttf'
AZUL = (11, 79, 124)


def figura_1(origen, destino):
    im = Image.open(origen).convert('RGB'); a = np.asarray(im).astype(int)
    m = (a[..., 1] > a[..., 0] + 40) & (a[..., 1] > a[..., 2] + 20)          # píxeles verdes del ícono
    ys, xs = np.where(m[200:340, 300:480]); x0, x1, y0, y1 = xs.min() + 300, xs.max() + 300, ys.min() + 200, ys.max() + 200
    d = ImageDraw.Draw(im)
    fondo = im.getpixel((x1 + 18, (y0 + y1) // 2))
    d.rectangle((x0 - 3, y0 - 3, x1 + 3, y1 + 3), fill=fondo)
    d.rounded_rectangle((x0, y0, x1, y1), radius=6, outline=AZUL, width=4)
    for k in (1, 2):                                                      # cuadrícula 3 × 3 neutra
        x = x0 + (x1 - x0) * k / 3; y = y0 + (y1 - y0) * k / 3
        d.line((x, y0 + 2, x, y1 - 2), fill=AZUL, width=3); d.line((x0 + 2, y, x1 - 2, y), fill=AZUL, width=3)
    im.save(destino)


def figura_2(origen, destino):
    im = Image.open(origen).convert('RGB'); a = np.asarray(im.convert('L')).astype(int); d = ImageDraw.Draw(im)
    for zona in ((295, 545, 430, 600), (1045, 540, 1175, 600)):          # «900.000» en la celda y en el rango
        zx0, zy0, zx1, zy1 = zona
        ys, xs = np.where(a[zy0:zy1, zx0:zx1] < 80)
        x0, x1, y0, y1 = zx0 + xs.min(), zx0 + xs.max(), zy0 + ys.min(), zy0 + ys.max()
        fondo = im.getpixel((x0 - 6, y0 - 4))
        d.rectangle((x0 - 4, y0 - 4, x1 + 4, y1 + 4), fill=fondo)
        tam = round((y1 - y0 + 1) / 0.644)                                # misma altura de mayúsculas que las cifras
        f = ImageFont.truetype(REGULAR, tam)
        d.text(((x0 + x1) / 2, (y0 + y1) / 2 + 1), 'SIMPLE', font=f, fill=(15, 23, 40), anchor='mm')
    im.save(destino)


if __name__ == '__main__':
    r2, r3 = sys.argv[1], sys.argv[2]
    os.makedirs(r3, exist_ok=True)
    for n in range(1, 14):
        origen = os.path.join(r2, 'R2_Figura_%02d.png' % n); destino = os.path.join(r3, 'R3_Figura_%02d.png' % n)
        {1: figura_1, 2: figura_2}.get(n, shutil.copyfile)(origen, destino)
    for n in (5, 8, 9):
        shutil.copyfile(os.path.join(r2, 'R2_Figura_%02d.svg' % n), os.path.join(r3, 'R3_Figura_%02d.svg' % n))
    print('13 figuras R3 en', r3)
