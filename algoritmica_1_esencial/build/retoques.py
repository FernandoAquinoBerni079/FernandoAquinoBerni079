# -*- coding: utf-8 -*-
"""Retoques mínimos de cuatro imágenes del tomo (copias en figs_ret/; los originales de figs_src/ no se tocan):
quitar las marcas ✓ (política del piloto), la marca de agua y el artefacto «blend», y cambiar «» por comillas
rectas dentro del código de la Figura 21.1."""
from PIL import Image, ImageDraw, ImageFont
S = '/home/claude/alg1/build/figs_src/'; R = '/home/claude/alg1/build/figs_ret/'
FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'


def tapar(d, im, caja, muestra):
    d.rectangle(caja, fill=im.getpixel(muestra))


# Figura 5.1: «= 30 ✓»
im = Image.open(S + 'src_02.png').convert('RGB'); d = ImageDraw.Draw(im)
tapar(d, im, (852, 588, 890, 622), (900, 600)); im.save(R + 'src_02.png')
# Figura 14.2: «vuelto = 8.000 ✓» y marca de agua
im = Image.open(S + 'src_07.png').convert('RGB'); d = ImageDraw.Draw(im)
tapar(d, im, (976, 590, 1012, 630), (970, 640)); tapar(d, im, (880, 816, 940, 872), (870, 840)); im.save(R + 'src_07.png')
# Figura 3.1: artefacto «blend» con rueda de color
im = Image.open(S + 'src_01.png').convert('RGB'); d = ImageDraw.Draw(im)
tapar(d, im, (443, 332, 483, 392), (440, 360)); im.save(R + 'src_01.png')
# Figura 21.1: ✓ final y comillas «» en el código
im = Image.open(S + 'src_12.png').convert('RGB'); d = ImageDraw.Draw(im)
tapar(d, im, (722, 972, 752, 1002), (760, 990))
fondo = im.getpixel((700, 145))
f = ImageFont.truetype(FB, 20)
for x0, x1 in ((673, 683), (777, 787)):
    d.rectangle((x0, 142, x1, 166), fill=fondo)
    d.text(((x0 + x1) / 2, 147), '"', font=f, fill=(30, 30, 30), anchor='mt')
im.save(R + 'src_12.png')
print('retocadas: src_01, src_02, src_07, src_12')
