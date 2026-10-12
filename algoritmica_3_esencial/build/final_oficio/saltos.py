"""Ajuste de maquetación: reemplaza el párrafo vacío de salto de página que precede a una
tabla de evaluación por «salto de página antes» en el primer párrafo de esa tabla.
Evita la página en blanco cuando el contenido anterior llena la hoja justa."""
import sys, docx
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
d = docx.Document(sys.argv[1]); n = 0
for p in list(d.element.body.iter(qn('w:p'))):
    if p.getparent() is d.element.body and any(b.get(qn('w:type')) == 'page' for b in p.iter(qn('w:br'))) \
            and not ''.join(t.text or '' for t in p.iter(qn('w:t'))) and p.getnext().tag == qn('w:tbl'):
        q = next(p.getnext().iter(qn('w:p')))
        pPr = q.get_or_add_pPr()
        pb = OxmlElement('w:pageBreakBefore')
        ant = [pPr.find(qn(t)) for t in ('w:pStyle', 'w:keepNext', 'w:keepLines')]
        ant = [a for a in ant if a is not None]
        (ant[-1].addnext(pb) if ant else pPr.insert(0, pb))
        p.getparent().remove(p); n += 1
print('saltos movidos', n); d.save(sys.argv[1])
# Párrafo separador vacío (sin texto, imagen ni salto) justo antes de un párrafo con salto de página antes:
# no ocupa lugar útil y, si la hoja anterior quedó llena, genera una página en blanco.
d = docx.Document(sys.argv[1]); n = 0
for p in list(d.element.body):
    if p.tag != qn('w:p'): continue
    nx = p.getnext()
    vacio = not ''.join(t.text or '' for t in p.iter(qn('w:t'))) and not list(p.iter(qn('w:drawing'))) \
        and not list(p.iter(qn('w:br'))) and not list(p.iter(qn('w:sectPr')))
    if vacio and nx is not None and nx.tag == qn('w:p') and nx.find('.//' + qn('w:pageBreakBefore')) is not None:
        p.getparent().remove(p); n += 1
print('separadores vacíos antes de salto quitados', n); d.save(sys.argv[1])
