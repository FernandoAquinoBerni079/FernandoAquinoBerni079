"""Comprueba que cada variante del piloto conserva todo el texto y todas las
imágenes de las secciones elegidas del DOCX base: mismas palabras en el mismo
orden y mismas imágenes byte a byte. El índice nuevo se excluye de la
comparación porque se genera.

Uso: python3 verificar_tomo.py BASE.docx PILOTO1.docx [PILOTO2.docx ...]
"""
import hashlib
import re
import sys

import docx

sys.path.insert(0, __import__('os').path.dirname(__file__))
from tomo_piloto import PILOTO, W, A, R, estilo, es_p, texto  # noqa: E402


def palabras(elementos):
    out = []
    for e in elementos:
        trozos = []
        for x in e.iter():
            if x.tag == W + 't':
                trozos.append(x.text or '')
            elif x.tag in (W + 'tab', W + 'br', W + 'p'):
                trozos.append(' ')
        out += re.findall(r'\w+', ''.join(trozos).lower())
    return out


def imagenes(doc, elementos):
    hs = []
    for e in elementos:
        for b in e.iter(A + 'blip'):
            hs.append(hashlib.sha256(doc.part.related_parts[b.get(R + 'embed')].blob).hexdigest())
    return hs


def secciones_base(doc):
    els = [e for e in doc.element.body if e.tag != W + 'sectPr']
    i_ind = next(i for i, e in enumerate(els) if es_p(e) and texto(e) == 'Índice')
    sel = els[:i_ind + 1]
    for ini, fin in PILOTO:
        a = next(i for i, e in enumerate(els) if es_p(e) and texto(e).startswith(ini) and estilo(doc, e) == 'Heading 1')
        b = next(i for i, e in enumerate(els) if i > a and es_p(e) and texto(e).startswith(fin) and estilo(doc, e) == 'Heading 1')
        sel += els[a:b]
    return sel


def secciones_piloto(doc):
    els = [e for e in doc.element.body if e.tag != W + 'sectPr']
    i_ind = next(i for i, e in enumerate(els) if es_p(e) and texto(e) == 'Índice')
    j = i_ind + 1
    while j < len(els) and es_p(els[j]) and estilo(doc, els[j]) != 'Heading 1':
        j += 1   # líneas del índice generado
    return els[:i_ind + 1] + els[j:]


def main():
    base = docx.Document(sys.argv[1])
    sb = secciones_base(base)
    pb, ib = palabras(sb), imagenes(base, sb)
    ok = True
    for ruta in sys.argv[2:]:
        d = docx.Document(ruta)
        sp = secciones_piloto(d)
        pp, ip = palabras(sp), imagenes(d, sp)
        iguales = pp == pb
        if not iguales:
            import difflib
            dif = [x for x in difflib.ndiff(pb, pp) if x[0] in '+-'][:20]
        print(f'{ruta}: palabras base {len(pb)}, piloto {len(pp)}, mismo texto y orden: {"sí" if iguales else "NO"}; '
              f'imágenes {len(ib)}/{len(ip)}, idénticas: {"sí" if ib == ip else "NO"}')
        if not iguales:
            print('   ', dif)
        ok &= iguales and ib == ip
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
