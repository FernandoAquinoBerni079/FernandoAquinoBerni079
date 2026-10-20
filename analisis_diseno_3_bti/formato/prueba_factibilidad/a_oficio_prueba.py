"""Prueba de factibilidad: copia de un DOCX A4 del lote 1 llevada a oficio (21,59 x 33,02 cm). No toca originales."""
import sys, docx
from docx.shared import Cm
from docx.oxml.ns import qn
src, dst, var = sys.argv[1:4]
d = docx.Document(src)
for s in d.sections:
    s.page_width, s.page_height = Cm(21.59), Cm(33.02)
    if var == 'B':
        s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Cm(1.27)
        s.header_distance = s.footer_distance = Cm(0.6)
if var == 'B':
    f = (21.59 - 2 * 1.27) / 16.6
    for t in d.element.body.iter(qn('w:tbl')):
        for gc in t.iter(qn('w:gridCol')):
            gc.set(qn('w:w'), str(int(int(gc.get(qn('w:w'))) * f)))
        for tc in t.iter(qn('w:tcW')):
            if tc.get(qn('w:type')) == 'dxa':
                tc.set(qn('w:w'), str(int(int(tc.get(qn('w:w'))) * f)))
        tw = t.find(qn('w:tblPr') + '/' + qn('w:tblW'))
        if tw is not None and tw.get(qn('w:type')) == 'dxa':
            tw.set(qn('w:w'), str(int(int(tw.get(qn('w:w'))) * f)))
d.save(dst)
