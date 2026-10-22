# -*- coding: utf-8 -*-
"""Figuras R3 de Informática 3.º BTC, a partir de las R2 (que no se modifican).

- Figura 2: la nota «Esquema de laboratorio; no corresponde a un registro tributario real.» medía 6 pt al tamaño del
  tomo. Se quita de la imagen y pasa al pie de figura (texto del DOCX), en el tomo y en el laboratorio.
- Figura 19: la nota «Esquema didáctico · no es un sitio publicado.» se reescribe más grande (de 6,4 a ≈ 9 pt a
  15,5 cm), y «WhatsApp», nombre de una aplicación comercial, se reemplaza por «Mensajería», término que usa el tomo.
- Las demás se copian sin cambios. Con el ancho de 15,5 cm del tomo R3 ningún texto queda por debajo de 7 pt
  (medición en LEGIBILIDAD_R3_3BTC.md).
Uso: python3 figuras_r3_3btc.py <carpeta figuras R2> <carpeta salida R3>
"""
import os, shutil, sys
from PIL import Image, ImageDraw, ImageFont

REG = '/usr/local/share/fonts/carlito/Carlito-Regular.ttf'
BOLD = '/root/.fonts/Carlito-Bold.ttf'


def figura_2(origen, destino):
    im = Image.open(origen).convert('RGB'); d = ImageDraw.Draw(im)
    fondo = im.getpixel((1490, 950))
    d.rectangle((1028, 912, 1500, 986), fill=fondo)               # separador y nota de dos líneas
    im.save(destino)


def figura_19(origen, destino):
    im = Image.open(origen).convert('RGB'); d = ImageDraw.Draw(im)
    fondo = im.getpixel((1440, 648))
    d.rectangle((1246, 628, 1425, 670), fill=fondo)
    d.text((1251, 649), 'Mensajería', font=ImageFont.truetype(BOLD, 38), fill=(15, 34, 54), anchor='lm')
    d.rectangle((480, 967, 1060, 1023), fill=(255, 255, 255))     # franja blanca bajo el recuadro azul
    d.text((768, 994), 'Esquema didáctico · no es un sitio publicado.', font=ImageFont.truetype(REG, 33),
           fill=(85, 96, 108), anchor='mm')
    im.save(destino)


if __name__ == '__main__':
    r2, r3 = sys.argv[1], sys.argv[2]
    os.makedirs(r3, exist_ok=True)
    for n in range(1, 21):
        o = os.path.join(r2, 'R2_Figura_%02d.png' % n); s = os.path.join(r3, 'R3_Figura_%02d.png' % n)
        {2: figura_2, 19: figura_19}.get(n, shutil.copyfile)(o, s)
    shutil.copyfile(os.path.join(r2, 'R2_Figura_20.svg'), os.path.join(r3, 'R3_Figura_20.svg'))
    print('20 figuras R3 en', r3)
