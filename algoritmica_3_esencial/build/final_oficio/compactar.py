"""Ajuste de maquetación: cuando el final de una clase o práctica desborda unas pocas líneas
a una página casi vacía, reduce a la mitad el espaciado antes/después de los párrafos de
esa unidad (nunca el texto, la letra ni el interlineado).

Uso: python3 -I compactar.py DOC.docx PAG [PAG ...]   (PAG = folio de la página casi vacía)
"""
import sys, re, docx
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

norm = lambda s: re.sub(r'\s+', ' ', s).strip()


def unidades(d):
    toc = [(norm(p.text.rsplit('\t', 1)[0]), int(p.text.rsplit('\t', 1)[1]))
           for p in d.paragraphs if p.style.name.startswith('toc') and '\t' in p.text]
    raiz = d.element.body
    def tope(e):
        while e.getparent() is not raiz:
            e = e.getparent()
        return e
    txt = lambda p: norm(''.join(t.text or '' for t in p.iter(qn('w:t'))))
    body = [p for p in raiz.iter(qn('w:p'))
            if not (p.pPr is not None and p.pPr.pStyle is not None and p.pPr.pStyle.val.lower().startswith('toc'))]
    heads = []; k = 0
    for tit, pag in toc:
        while txt(body[k]) != tit:
            k += 1
        heads.append((tit, pag, tope(body[k])))
    return heads


def compactar(d, pags):
    heads = unidades(d)
    hechos = []
    for pag in pags:
        i = max(j for j, h in enumerate(heads) if h[1] <= pag)
        tit, _, ini = heads[i]
        fin = heads[i + 1][2] if i + 1 < len(heads) else None
        el = ini; n = 0
        while el is not None and el is not fin:
            for p in ([el] if el.tag == qn('w:p') else list(el.iter(qn('w:p')))):
                pPr = p.get_or_add_pPr()
                sp = pPr.find(qn('w:spacing'))
                if sp is None:
                    sp = OxmlElement('w:spacing'); pPr.append(sp)
                    sp.set(qn('w:after'), '120')      # heredado de Normal
                for a in ('w:before', 'w:after'):
                    v = sp.get(qn(a))
                    if v and int(v) > 0:
                        sp.set(qn(a), str(int(v) // 2))
                n += 1
            el = el.getnext()
        hechos.append((pag, tit, n))
    return hechos


if __name__ == '__main__':
    d = docx.Document(sys.argv[1])
    for h in compactar(d, [int(x) for x in sys.argv[2:]]):
        print('compactada pág.', h[0], '·', h[1], '·', h[2], 'párrafos')
    d.save(sys.argv[1])
