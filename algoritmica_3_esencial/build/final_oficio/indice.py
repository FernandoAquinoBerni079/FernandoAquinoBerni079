"""Localiza en el PDF la página de cada entrada del índice y (opcional) reescribe los números.

Uso: python3 -I indice.py DOC.docx DOC.pdf [--escribir]
Imprime: entrada, número actual, página hallada (número de folio impreso en el pie).
"""
import sys, re, docx, pymupdf

norm = lambda s: re.sub(r'\s+', ' ', s).strip()


def entradas(d):
    return [p for p in d.paragraphs if p.style.name.startswith('toc') and '\t' in p.text]


def folios(pdf):
    """Texto normalizado y folio impreso («Página N de M») de cada página."""
    out = []
    for i, pg in enumerate(pymupdf.open(pdf)):
        t = pg.get_text()
        m = re.search(r'Página\s+(\d+)\s+de\s+\d+', t)
        out.append((norm(t), int(m.group(1)) if m else i + 1))
    return out


def hallar(d, pdf):
    ps = entradas(d); pgs = folios(pdf)
    # saltar las páginas del índice: empezar después de la última página que contenga el título de la última entrada con tabulador
    ini = 0
    for i, (t, _) in enumerate(pgs):
        if norm(ps[-1].text.split('\t')[0]) in t and i < len(pgs) // 3:
            ini = i + 1
    res = []; k = ini
    for p in ps:
        tit = norm(p.text.split('\t')[0])
        j = k
        while j < len(pgs) and tit not in pgs[j][0]:
            j += 1
        if j == len(pgs):
            res.append((p, None)); continue
        res.append((p, pgs[j][1])); k = j
    return res


if __name__ == '__main__':
    d = docx.Document(sys.argv[1])
    res = hallar(d, sys.argv[2]); cambios = 0
    for p, n in res:
        tit, act = p.text.rsplit('\t', 1)
        marca = '' if str(n) == act else '  <-- cambia'
        if marca: cambios += 1
        print(f'{act:>4} -> {n}  {tit[:70]}{marca}')
        if '--escribir' in sys.argv and n is not None and str(n) != act:
            runs = [r for r in p.runs if r.text]
            r = runs[-1]
            assert r.text.endswith(act), r.text
            r.text = r.text[:len(r.text) - len(act)] + str(n)
    print('CAMBIOS', cambios, 'NO_HALLADAS', sum(n is None for _, n in res))
    if '--escribir' in sys.argv:
        d.save(sys.argv[1])
