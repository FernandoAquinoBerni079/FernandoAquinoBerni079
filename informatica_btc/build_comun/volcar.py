"""Vuelca un DOCX en texto con orden del cuerpo: párrafos (con estilo) y tablas (filas | celdas), marca imágenes."""
import sys, docx
from docx.oxml.ns import qn
def volcar(ruta):
    d = docx.Document(ruta); out = []; nimg = 0
    for el in d.element.body.iterchildren():
        if el.tag == qn('w:p'):
            p = docx.text.paragraph.Paragraph(el, d)
            imgs = el.findall('.//' + qn('w:drawing'))
            for _ in imgs:
                nimg += 1
                blips = el.findall('.//{http://schemas.openxmlformats.org/drawingml/2006/main}blip')
                rid = blips[0].get(qn('r:embed')) if blips else None
                out.append('[IMG %d %s]' % (nimg, d.part.related_parts[rid].partname if rid else '?'))
            br = 'w:br' in el.xml and 'w:type="page"' in el.xml
            t = p.text
            if t.strip() or br:
                out.append(('{%s} ' % p.style.name if p.style.name not in ('Normal',) else '') + t + (' <<SALTO>>' if br else ''))
        elif el.tag == qn('w:tbl'):
            t = docx.table.Table(el, d); out.append('<TABLA>')
            for r in t.rows:
                cel = []; prev = None
                for c in r.cells:
                    if c._tc is prev: continue
                    prev = c._tc; cel.append(c.text.replace('\n', ' / '))
                out.append(' | '.join(cel))
            out.append('</TABLA>')
    return '\n'.join(out)
print(volcar(sys.argv[1]))
