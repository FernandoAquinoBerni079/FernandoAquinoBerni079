# -*- coding: utf-8 -*-
"""Retoque mínimo de la Figura 9.1 (image12.jpg, imagen del tomo), en copia (figs_ret/): se quitan el ✓ de
«ACEPTA» y las ✗ de los dos «RECHAZA» (política del piloto). El original de figs_src/ no se toca."""
from PIL import Image, ImageDraw
S = '/home/claude/alg3/build/figs_src/'; R = '/home/claude/alg3/build/figs_ret/'
im = Image.open(S + 'image12.jpg').convert('RGB'); d = ImageDraw.Draw(im)
for y0, y1 in ((83, 111), (233, 262), (384, 414)):
    for y in range(y0, y1 + 1):
        d.line([(716, y), (750, y)], fill=im.getpixel((712, y)))
im.save(R + 'image12.jpg', quality=95)
print('retocada: image12.jpg (Figura 9.1)')
