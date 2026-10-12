# -*- coding: utf-8 -*-
"""Mide la ocupación de cada página interior de un PDF (altura usada por contenido, sin encabezado ni pie).
Uso: python3 ocupacion.py archivo.pdf [umbral=0.25]. Una página 'residual' es una página interior con texto cuya
altura útil ocupada es menor que el umbral, o una que sólo trae firmas/encabezado."""
import sys, pymupdf

def medir(pdf, margen_sup=0.03, margen_inf=0.035):
    # oficio: margen de 1,27 cm = 3,85 % del alto; el pie (0,6 cm) queda por debajo del corte inferior
    d = pymupdf.open(pdf); res = []
    for i, pg in enumerate(d):
        h = pg.rect.height; top = h * margen_sup; bot = h * (1 - margen_inf)
        bl = [b for b in pg.get_text('blocks') if b[1] >= top - 1 and b[3] <= bot + 1 and b[4].strip()]
        imgs = [pg.get_image_bbox(x) for x in pg.get_images(full=True)]
        ys = [b[3] for b in bl] + [r.y1 for r in imgs if r.y1 <= bot + 1]
        # dibujos (cajas, tablas)
        for dr in pg.get_drawings():
            r = dr['rect']
            if r.y1 <= bot + 1 and r.height < h * 0.9: ys.append(r.y1)
        uso = (max(ys) - top) / (bot - top) if ys else 0.0
        txt = ' '.join(b[4] for b in bl)
        res.append((i + 1, round(max(uso, 0), 3), len(txt.split()), txt[:70].replace('\n', ' ')))
    return res

if __name__ == '__main__':
    um = float(sys.argv[2]) if len(sys.argv) > 2 else 0.25
    r = medir(sys.argv[1])
    bajos = [x for x in r if x[1] < um and (x[2] > 0 or x[1] > 0)]
    print('páginas', len(r), '· residuales (<%d%%): %d' % (um * 100, len(bajos)))
    for x in bajos: print(x)
