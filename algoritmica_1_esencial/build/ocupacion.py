# -*- coding: utf-8 -*-
"""Ocupación vertical de cada página interior del PDF: (borde inferior del último contenido - margen superior)
/ alto útil. Cuenta texto, imágenes y dibujos (renglones, bordes de tabla). Excluye el pie de página."""
import sys, pymupdf
def ocupacion(pdf, margen_cm=1.27):
    doc = pymupdf.open(pdf); res = []
    for i, pg in enumerate(doc, 1):
        H = pg.rect.height; W = pg.rect.width; m = margen_cm / 2.54 * 72
        top, bot = m, H - m
        ys = []
        for b in pg.get_text('blocks'):
            if b[3] > bot - 4 and b[1] > bot - 40: continue   # pie
            if b[4].strip(): ys.append(b[3])
        for im in pg.get_image_info():
            ys.append(im['bbox'][3])
        for d in pg.get_drawings():
            r = d['rect']
            if r.y1 <= bot - 4 and r.width > 2: ys.append(r.y1)
        palabras = len(pg.get_text().split())
        full = any(im['bbox'][2] - im['bbox'][0] > W * .95 and im['bbox'][3] - im['bbox'][1] > H * .95 for im in pg.get_image_info())
        occ = 0 if not ys else max(0, (min(max(ys), bot) - top) / (bot - top))
        res.append((i, round(occ, 3), palabras, full))
    return res
if __name__ == '__main__':
    pdf = sys.argv[1]; um = float(sys.argv[2]) if len(sys.argv) > 2 else .25
    r = ocupacion(pdf)
    bajas = [x for x in r if x[1] < um and not x[3]]
    print(len(r), 'páginas; bajo %d%%:' % (um * 100), len(bajas))
    for x in bajas: print('  p.%d  %d%%  %d palabras' % (x[0], x[1] * 100, x[2]))
