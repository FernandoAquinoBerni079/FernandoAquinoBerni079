# -*- coding: utf-8 -*-
"""Corrección v2 (auditoría ChatGPT v2, hallazgos V2-01 y V2-02): solo maquetación de Planes de Clase y Plan Anual.
- Márgenes de la colección: 1,27 cm en todos los lados (antes 1,6/2,0 en los Planes y 1,5 en el Plan Anual).
- Las tablas se ensanchan en la misma proporción que el ancho útil (tblGrid y tcW), sin tocar el texto.
- Opcional: espaciado posterior de los párrafos de tabla y tamaño de letra, para que cada plan entre en una hoja.
Uso: python3 fix_v2_maqueta.py ENTRADA.docx SALIDA.docx [after_twips] [sz_medios_puntos]"""
import sys, docx
from docx.shared import Cm
from docx.oxml.ns import qn
ent, sal = sys.argv[1], sys.argv[2]
after = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3] != '-' else None
sz = sys.argv[4] if len(sys.argv) > 4 else None
d = docx.Document(ent)
M = Cm(1.27)
for s in d.sections:
    util0 = s.page_width - s.left_margin - s.right_margin
    s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = M
    s.header_distance = s.footer_distance = Cm(0.6)  # encabezado y pie dentro del margen de 1,27 cm
    k = (s.page_width - 2 * M) / util0
body = d.element.body
for tbl in body.iter(qn('w:tbl')):
    g = tbl.find(qn('w:tblGrid'))
    util = round((s.page_width - 2 * M) / 635)  # ancho útil en twips
    suma = sum(int(c.get(qn('w:w'))) for c in g)
    kt = util / suma if suma > 0.8 * util / k else k  # tablas de ancho completo: llenan el ancho útil
    for c in g:
        c.set(qn('w:w'), str(round(int(c.get(qn('w:w'))) * kt)))
    # algunas tablas traen tblW y tblLayout duplicados (auto y dxa); se deja uno solo, igual a la suma de la grilla
    tws = tbl.tblPr.findall(qn('w:tblW'))
    for x in tws[1:]: tbl.tblPr.remove(x)
    tws[0].set(qn('w:type'), 'dxa'); tws[0].set(qn('w:w'), str(sum(int(c.get(qn('w:w'))) for c in g)))
    for x in tbl.tblPr.findall(qn('w:tblLayout'))[1:]: tbl.tblPr.remove(x)
    for w in tbl.iter(qn('w:tcW')):
        if w.get(qn('w:type')) == 'dxa':
            w.set(qn('w:w'), str(round(int(w.get(qn('w:w'))) * kt)))
    if after is not None or sz:
        for p in tbl.iter(qn('w:p')):
            if after is not None:
                spc = p.find(qn('w:pPr') + '/' + qn('w:spacing'))
                if spc is not None and spc.get(qn('w:after')) and int(spc.get(qn('w:after'))) > after:
                    spc.set(qn('w:after'), str(after))
            if sz:
                for r in p.iter(qn('w:sz')):
                    if r.get(qn('w:val')) == '19': r.set(qn('w:val'), sz)
                for r in p.iter(qn('w:szCs')):
                    if r.get(qn('w:val')) == '19': r.set(qn('w:val'), sz)
# separadores vacíos entre tablas: de 2 pt a 1 pt
if after is not None:
    for p in body.iterchildren(qn('w:p')):
        if not ''.join(t.text or '' for t in p.iter(qn('w:t'))).strip():
            spc = p.find(qn('w:pPr') + '/' + qn('w:spacing'))
            if spc is not None and spc.get(qn('w:after')) == '40': spc.set(qn('w:after'), '20')
# Plan 36 (integradora, con las capacidades de toda la etapa): sus celdas heredan 3 pt de espacio posterior del estilo
# Normal; se anulan solo en ese plan para que entre en una hoja.
import re
plan = None
for el in body.iterchildren():
    if el.tag == qn('w:p'):
        m = re.match(r'Plan de Clase N\.º (\d+) —', ''.join(t.text or '' for t in el.iter(qn('w:t'))).strip())
        if m: plan = int(m.group(1))
    elif el.tag == qn('w:tbl') and plan == 36 and after is not None:
        for p in el.iter(qn('w:p')):
            ppr = p.find(qn('w:pPr'))
            if ppr is None: ppr = p.makeelement(qn('w:pPr'), {}); p.insert(0, ppr)
            spc = ppr.find(qn('w:spacing'))
            if spc is None: spc = ppr.makeelement(qn('w:spacing'), {}); ppr.append(spc)
            spc.set(qn('w:after'), '0')
# La última sección (Plan 36) no tenía «primera página distinta»: mostraba el encabezado «continuación» en su
# primera hoja. Se le agrega, como en las otras 35 secciones de plan.
if sum(1 for _ in body.iter(qn('w:titlePg'))) == 36:
    for s_ in d.sections:
        s_.different_first_page_header_footer = True
print('factor de ancho', round(k, 4))
d.save(sal)
