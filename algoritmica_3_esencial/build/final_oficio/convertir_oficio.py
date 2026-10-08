"""Convierte un .docx FINAL_CONTENIDO_A4 a oficio 21,6 x 33 cm sin tocar el texto.

Uso: python3 -I convertir_oficio.py ENTRADA.docx SALIDA.docx PORTADA.jpg [CONTRA.jpg] [--fig rIdX=ruta.jpg ...]
Solo cambia maquetación: tamaño de hoja, márgenes, anchos de tablas, extensión de
imágenes, blobs de portada/contraportada (y figura retocada) y posición del tabulador del índice.
"""
import sys, re, docx
from docx.shared import Cm, Emu
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

PAG_W, PAG_H, MARG = 21.6, 33.0, 1.27
ANCHO = round(PAG_W - 2 * MARG, 2)          # 19,06 cm
TWIP = 567.0                                 # twips por cm
EMU = 360000                                 # EMU por cm


def convertir(ent, sal, portada, contra=None, figs=()):
    d = docx.Document(ent)
    # 1. Secciones
    for s in d.sections:
        s.page_width, s.page_height = Cm(PAG_W), Cm(PAG_H)
        s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Cm(MARG)
        s.header_distance = s.footer_distance = Cm(0.6)
    body = d.element.body
    # 2. Tablas al 100 %
    for tbl in body.iter(qn('w:tbl')):
        grid = tbl.find(qn('w:tblGrid'))
        cols = grid.findall(qn('w:gridCol')) if grid is not None else []
        tot = sum(int(c.get(qn('w:w'))) for c in cols)
        f = ANCHO * TWIP / tot if tot else 1
        for c in cols:
            c.set(qn('w:w'), str(round(int(c.get(qn('w:w'))) * f)))
        for tcw in tbl.iter(qn('w:tcW')):
            if tcw.get(qn('w:type')) in (None, 'dxa'):
                tcw.set(qn('w:w'), str(round(int(tcw.get(qn('w:w'))) * f)))
        tblPr = tbl.find(qn('w:tblPr'))
        for old in tblPr.findall(qn('w:tblW')):
            tblPr.remove(old)
        w = OxmlElement('w:tblW'); w.set(qn('w:w'), '5000'); w.set(qn('w:type'), 'pct')
        # orden del schema: tblStyle, tblpPr, tblOverlap, bidiVisual, tblStyleRowBandSize, tblStyleColBandSize, tblW
        prev = [tblPr.find(qn(t)) for t in ('w:tblStyle', 'w:tblpPr', 'w:tblOverlap', 'w:bidiVisual',
                                              'w:tblStyleRowBandSize', 'w:tblStyleColBandSize')]
        prev = [p for p in prev if p is not None]
        if prev:
            prev[-1].addnext(w)
        else:
            tblPr.insert(0, w)
    # 3. Imágenes en línea: x1,1 con tope 17,5 cm (proporcionales)
    for inl in body.iter(qn('wp:inline')):
        ext = inl.find(qn('wp:extent'))
        cx, cy = int(ext.get('cx')), int(ext.get('cy'))
        nx = min(cx * 1.1, 17.5 * EMU); k = nx / cx
        ext.set('cx', str(round(cx * k))); ext.set('cy', str(round(cy * k)))
        for x in inl.iter(qn('a:ext')):
            x.set('cx', str(round(cx * k))); x.set('cy', str(round(cy * k)))
    # 4. Portada / contraportada a página completa
    blobs = [portada, contra]
    anchors = list(body.iter(qn('wp:anchor')))
    for anc, ruta in zip(anchors, blobs):
        if ruta is None:
            continue
        ext = anc.find(qn('wp:extent'))
        ext.set('cx', str(round(PAG_W * EMU))); ext.set('cy', str(round(PAG_H * EMU)))
        for x in anc.iter(qn('a:ext')):
            x.set('cx', str(round(PAG_W * EMU))); x.set('cy', str(round(PAG_H * EMU)))
        rid = next(anc.iter(qn('a:blip'))).get(qn('r:embed'))
        d.part.related_parts[rid]._blob = open(ruta, 'rb').read()
    for rid, ruta in figs:
        d.part.related_parts[rid]._blob = open(ruta, 'rb').read()
    # 5. Tabuladores del índice: al borde derecho del ancho útil
    for tab in body.iter(qn('w:tab')):
        if tab.get(qn('w:val')) == 'right' and tab.get(qn('w:pos')):
            tab.set(qn('w:pos'), str(round((ANCHO - 0.05) * TWIP)))
    d.save(sal)


if __name__ == '__main__':
    a = sys.argv[1:]
    figs = []
    while '--fig' in a:
        i = a.index('--fig'); rid, ruta = a[i + 1].split('=', 1); figs.append((rid, ruta)); del a[i:i + 2]
    convertir(a[0], a[1], a[2], a[3] if len(a) > 3 else None, figs)
