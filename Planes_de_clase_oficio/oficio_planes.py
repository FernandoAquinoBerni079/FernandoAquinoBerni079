# -*- coding: utf-8 -*-
"""Planes de Clase -> oficio (21,59x33,02), margenes 1,27 cm, tablas a la ventana,
Capacidad/Tema/Indicadores 20/80, portada propia (indice en hoja aparte), cada plan en hoja nueva.
uso: python3 oficio_planes.py IN.docx OUT.docx"""
import sys, re, copy
import docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

W, H, M = 12240, 18720, 720
UTIL = W - 2 * M            # 10800 twips = 19,05 cm
LABELS = ('capacidad', 'capacidades', 'indicadores', 'indicador', 'tema', 'recursos', 'procedimientos',
          'instrumentos', 'criterios', 'contenidos')
TBLPR_ORDER = ['tblStyle','tblpPr','tblOverlap','bidiVisual','tblStyleRowBandSize','tblStyleColBandSize',
               'tblW','jc','tblCellSpacing','tblInd','tblBorders','shd','tblLayout','tblCellMar','tblLook']

def txt(el): return ''.join(t.text or '' for t in el.iter(qn('w:t')))
def tag(e): return e.tag.split('}')[1]

def ppr(p):
    pr = p.find(qn('w:pPr'))
    if pr is None:
        pr = OxmlElement('w:pPr'); p.insert(0, pr)
    return pr

def put(pr, el, order):
    """inserta el hijo respetando el orden del esquema (order = lista de nombres)"""
    n = tag(el); old = pr.find(qn('w:' + n))
    if old is not None: pr.remove(old)
    idx = order.index(n)
    for i, ch in enumerate(pr):
        t = tag(ch)
        if t in order and order.index(t) > idx:
            pr.insert(i, el); return
    pr.append(el)

PPR_ORDER = ['pStyle','keepNext','keepLines','pageBreakBefore','framePr','widowControl','numPr',
             'suppressLineNumbers','pBdr','shd','tabs','suppressAutoHyphens','kinsoku','wordWrap',
             'overflowPunct','topLinePunct','autoSpaceDE','autoSpaceDN','bidi','adjustRightInd','snapToGrid',
             'spacing','ind','contextualSpacing','mirrorIndents','suppressOverlap','jc','textDirection',
             'textAlignment','textboxTightWrap','outlineLvl','divId','cnfStyle','rPr','sectPr','pPrChange']

def page_break_before(p):
    pr = ppr(p)
    if pr.find(qn('w:pageBreakBefore')) is None:
        put(pr, OxmlElement('w:pageBreakBefore'), PPR_ORDER)

def spacing(p, before=None, after=None):
    pr = ppr(p); sp = pr.find(qn('w:spacing'))
    if sp is None:
        sp = OxmlElement('w:spacing'); put(pr, sp, PPR_ORDER)
    if before is not None: sp.set(qn('w:before'), str(before))
    if after is not None: sp.set(qn('w:after'), str(after))

# ---------- secciones ----------
def paginas(d):
    for s in d.element.body.iter(qn('w:sectPr')):
        pg = s.find(qn('w:pgSz')); pg.set(qn('w:w'), str(W)); pg.set(qn('w:h'), str(H))
        if qn('w:orient') in pg.attrib: del pg.attrib[qn('w:orient')]
        m = s.find(qn('w:pgMar'))
        for k in ('top','bottom','left','right'): m.set(qn('w:' + k), str(M))
        m.set(qn('w:header'), '708'); m.set(qn('w:footer'), '708'); m.set(qn('w:gutter'), '0')

# ---------- tablas ----------
def span(tc):
    g = tc.find(qn('w:tcPr') + '/' + qn('w:gridSpan'))
    return int(g.get(qn('w:val'))) if g is not None else 1

def set_grid(t, widths):
    g = t.find(qn('w:tblGrid'))
    for c in list(g): g.remove(c)
    for w in widths:
        c = OxmlElement('w:gridCol'); c.set(qn('w:w'), str(w)); g.append(c)
    for tr in t.findall(qn('w:tr')):
        i = 0
        for tc in tr.findall(qn('w:tc')):
            n = span(tc); w = sum(widths[i:i + n]); i += n
            pr = tc.find(qn('w:tcPr'))
            if pr is None:
                pr = OxmlElement('w:tcPr'); tc.insert(0, pr)
            tw = pr.find(qn('w:tcW'))
            if tw is None:
                tw = OxmlElement('w:tcW'); pr.insert(0, tw)
            tw.set(qn('w:type'), 'dxa'); tw.set(qn('w:w'), str(w))

def normaliza_tblpr(t):
    pr = t.find(qn('w:tblPr')); keep = {}
    for ch in list(pr):
        keep.setdefault(tag(ch), ch)      # primer valor gana, se eliminan duplicados
        pr.remove(ch)
    w = OxmlElement('w:tblW'); w.set(qn('w:type'), 'pct'); w.set(qn('w:w'), '5000'); keep['tblW'] = w
    jc = OxmlElement('w:jc'); jc.set(qn('w:val'), 'center'); keep['jc'] = jc
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); keep['tblLayout'] = lay
    ind = keep.pop('tblInd', None)
    for n in TBLPR_ORDER:
        if n in keep: pr.append(keep[n])

def es_etiqueta(tc):
    f = re.sub(r'[^a-záéíóúñ ]', '', txt(tc).strip().lower()).split(' ')[0]
    return f in LABELS

def tablas(d):
    n = veinte = 0
    for t in d.element.body.iter(qn('w:tbl')):
        if t.getparent().tag == qn('w:tc'): continue
        g = [int(c.get(qn('w:w'))) for c in t.find(qn('w:tblGrid'))]
        filas = t.findall(qn('w:tr'))
        if len(g) == 2 and any(es_etiqueta(tr.findall(qn('w:tc'))[0]) for tr in filas
                               if len(tr.findall(qn('w:tc'))) == 2):
            nuevo = [round(UTIL * .2), UTIL - round(UTIL * .2)]; veinte += 1
        else:
            f = UTIL / sum(g); nuevo = [round(x * f) for x in g]; nuevo[-1] += UTIL - sum(nuevo)
        set_grid(t, nuevo); normaliza_tblpr(t); n += 1
    return n, veinte

# ---------- portada / indice / planes ----------
def es_titulo_plan(p):
    st = p.find(qn('w:pPr') + '/' + qn('w:pStyle'))
    return (st is not None and re.match(r'Plan de Clase N\.º\s*\d+', txt(p).strip()) is not None)

def portada_e_indice(d):
    b = d.element.body; kids = list(b); info = {}
    idx = next((i for i, c in enumerate(kids) if tag(c) == 'p' and txt(c).strip().lower() == 'índice'), None)
    if idx is None: return {'indice': False}
    page_break_before(kids[idx])
    # portada: lo que esta antes del indice
    cover = kids[:idx]
    for c in cover:
        if tag(c) == 'tbl':                       # banda de titulo mas grande
            for rpr in c.iter(qn('w:rPr')):
                sz = rpr.find(qn('w:sz'))
                if sz is not None: sz.set(qn('w:val'), str(int(sz.get(qn('w:val'))) * 2))
            for tr in c.findall(qn('w:tr')):
                trpr = tr.find(qn('w:trPr'))
                if trpr is None: trpr = OxmlElement('w:trPr'); tr.insert(0, trpr)
                h = OxmlElement('w:trHeight'); h.set(qn('w:val'), '3400'); h.set(qn('w:hRule'), 'atLeast'); trpr.append(h)
                for tcpr in tr.iter(qn('w:tcPr')):
                    v = OxmlElement('w:vAlign'); v.set(qn('w:val'), 'center'); tcpr.append(v)
            for p in c.iter(qn('w:p')):
                spacing(p, 0, 0)
        elif tag(c) == 'p':
            for rpr in c.iter(qn('w:rPr')):
                sz = rpr.find(qn('w:sz'))
                if sz is not None: sz.set(qn('w:val'), str(round(int(sz.get(qn('w:val'))) * 1.3)))
            spacing(c, before=200, after=120)
    # aire arriba: parrafo espaciador antes de la banda y antes del primer texto
    sp0 = OxmlElement('w:p'); spacing(sp0, 2400, 0); b.insert(0, sp0)
    first_p = next(c for c in cover if tag(c) == 'p' and txt(c).strip())
    spacing(first_p, before=1800, after=200)
    pais = [c for c in cover if tag(c) == 'p' and txt(c).strip().startswith('República')]
    if pais: spacing(pais[0], before=3600, after=0)
    # espacio tras el titulo del indice
    return {'indice': True}

def planes_en_hoja_propia(d):
    b = d.element.body; n = fix = 0
    for p in list(b.iterchildren(qn('w:p'))):
        if not es_titulo_plan(p): continue
        n += 1
        prev = p.getprevious()
        sp = prev.find(qn('w:pPr') + '/' + qn('w:sectPr')) if prev is not None and tag(prev) == 'p' else None
        if sp is not None:
            ty = sp.find(qn('w:type'))
            if ty is not None and ty.get(qn('w:val')) == 'continuous':
                ty.set(qn('w:val'), 'nextPage'); fix += 1
        else:
            page_break_before(p); fix += 1
    return n, fix

def convertir(src, dst):
    d = docx.Document(src)
    paginas(d)
    info = portada_e_indice(d)
    nt, nv = tablas(d)
    npl, fix = planes_en_hoja_propia(d)
    d.save(dst)
    return dict(tablas=nt, tablas_20_80=nv, planes=npl, planes_corregidos=fix, **info)

if __name__ == '__main__':
    print(convertir(sys.argv[1], sys.argv[2]))
