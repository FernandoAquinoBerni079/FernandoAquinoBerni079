# -*- coding: utf-8 -*-
"""Operaciones de edición en el lugar sobre los .docx candidatos de Desarrollo Personal y Social (7.º, 8.º y 9.º).
Principio: no reconstruir. Se conservan párrafos, tablas, estilos e imágenes (las imágenes Gemini no se tocan: sus bytes
en word/media quedan idénticos y se verifican por SHA-256). Solo se cambia lo que figura en el informe diferencial."""
import copy, re, os, subprocess, hashlib, zipfile
import docx
from docx.shared import Cm, Pt, Emu
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

E = os.path.dirname(os.path.abspath(__file__)) + '/'
MARG = 1.27


def texto(el):
    return ''.join(t.text or '' for t in el.iter(qn('w:t')))


# ---------- márgenes y tablas ----------

def _escalar_tabla(tbl, f):
    """Escala anchos en dxa de una tabla (tblW, tblInd, gridCol, tcW) por el factor f; tablas en % no se tocan."""
    tblPr = tbl.find(qn('w:tblPr'))
    if tblPr is not None:
        for tag in ('w:tblW', 'w:tblInd'):
            w = tblPr.find(qn(tag))
            if w is not None and w.get(qn('w:type')) in (None, 'dxa') and w.get(qn('w:w')):
                w.set(qn('w:w'), str(int(round(int(w.get(qn('w:w'))) * f))))
    grid = tbl.find(qn('w:tblGrid'))
    if grid is not None:
        for gc in grid.findall(qn('w:gridCol')):
            if gc.get(qn('w:w')):
                gc.set(qn('w:w'), str(int(round(int(gc.get(qn('w:w'))) * f))))
    for tc in tbl.iter(qn('w:tc')):
        if tc.getparent().getparent() is not tbl:   # celdas de tablas anidadas: se escalan con su tabla
            continue
        tcPr = tc.find(qn('w:tcPr'))
        if tcPr is not None:
            w = tcPr.find(qn('w:tcW'))
            if w is not None and w.get(qn('w:type')) in (None, 'dxa') and w.get(qn('w:w')):
                w.set(qn('w:w'), str(int(round(int(w.get(qn('w:w'))) * f))))
    for inner in tbl.iter(qn('w:tbl')):
        if inner is not tbl and inner.getparent().getparent().getparent() is tbl:
            _escalar_tabla(inner, f)


def margenes(d, m=MARG, escalar=True):
    """Fija márgenes de m cm en todas las secciones y escala las tablas al nuevo ancho útil (las imágenes no cambian)."""
    s0 = d.sections[-1]
    w0 = s0.page_width - s0.left_margin - s0.right_margin
    for s in d.sections:
        s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Cm(m)
        s.header_distance = s.footer_distance = Cm(0.6)
    w1 = s0.page_width - s0.left_margin - s0.right_margin
    f = w1 / w0
    if escalar and abs(f - 1) > 0.005:
        for tbl in d.element.body.iter(qn('w:tbl')):
            if tbl.getparent().tag == qn('w:body'):
                _escalar_tabla(tbl, f)
    return f


# ---------- texto ----------

def reemplazar_parrafo(p_el, nuevo):
    """Reemplaza el texto de un párrafo conservando el formato de su primera corrida."""
    rs = p_el.findall(qn('w:r'))
    rs_t = [r for r in rs if r.find(qn('w:t')) is not None]
    if not rs_t:
        r = OxmlElement('w:r'); t = OxmlElement('w:t'); r.append(t); p_el.append(r); rs_t = [r]
    first = rs_t[0]
    for r in rs_t[1:]:
        p_el.remove(r)
    for t in first.findall(qn('w:t'))[1:]:
        first.remove(t)
    t = first.find(qn('w:t')); t.text = nuevo; t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')


def reemplazar_en_doc(d, viejo, nuevo, min_veces=1):
    """Reemplaza un texto que debe estar entero dentro de un párrafo. Devuelve cuántas veces lo hizo."""
    n = 0
    for p in d.element.body.iter(qn('w:p')):
        tx = texto(p)
        if viejo in tx:
            reemplazar_parrafo(p, tx.replace(viejo, nuevo)); n += 1
    assert n >= min_veces, 'no se encontró: ' + viejo[:80]
    return n


def celda_de(tabla_el, rotulo):
    """En una tabla de dos columnas (ficha), devuelve la celda de valor cuya fila empieza con el rótulo."""
    for tr in tabla_el.findall(qn('w:tr')):
        tcs = tr.findall(qn('w:tc'))
        if len(tcs) >= 2 and texto(tcs[0]).strip().startswith(rotulo):
            return tcs[1]
    return None


def fijar_celda(tc, lineas):
    """Reemplaza el contenido de una celda por varias líneas, clonando el formato del primer párrafo."""
    ps = tc.findall(qn('w:p'))
    modelo = copy.deepcopy(ps[0])
    for p in ps:
        tc.remove(p)
    for l in lineas:
        p = copy.deepcopy(modelo); reemplazar_parrafo(p, l); tc.append(p)


# ---------- portada ----------

def portada_imagen(d, ruta, primer_cuerpo):
    """Reemplaza todo lo que está antes del elemento primer_cuerpo por una portada de imagen a página completa,
    sin pie en la primera página. primer_cuerpo debe empezar en página nueva."""
    body = d.element.body
    els = list(body)
    i = els.index(primer_cuerpo)
    for el in els[:i]:
        if el.tag != qn('w:sectPr'):
            body.remove(el)
    import maqueta as M
    s = d.sections[0]
    p = M.imagen_pagina_completa(d, ruta)          # se agrega al final: lo movemos al principio
    body.remove(p._p); body.insert(0, p._p)
    # salto de página después de la portada
    br = OxmlElement('w:r'); b = OxmlElement('w:br'); b.set(qn('w:type'), 'page'); br.append(b); p._p.append(br)
    ppr = primer_cuerpo.find(qn('w:pPr'))
    if ppr is not None:
        pb = ppr.find(qn('w:pageBreakBefore'))
        if pb is not None:
            ppr.remove(pb)
    s.different_first_page_header_footer = True
    for hf in (s.first_page_footer, s.first_page_header):
        hf.is_linked_to_previous = False
        for q in hf.paragraphs:
            for r in list(q._p):
                if r.tag != qn('w:pPr'):
                    q._p.remove(r)


# ---------- PDF y control ----------

def a_pdf(ruta_docx, outdir):
    os.makedirs(outdir, exist_ok=True)
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', outdir, ruta_docx], check=True,
                   capture_output=True, env=dict(os.environ, HOME='/tmp/lohome'), timeout=900)
    return os.path.join(outdir, os.path.basename(ruta_docx)[:-5] + '.pdf')


def llenado(pg):
    bl = [b for b in pg.get_text('blocks') if b[4].strip() and not b[4].strip().startswith('Página')]
    ys = [b[3] for b in bl] + [r.y1 for im in pg.get_images(full=True) for r in pg.get_image_rects(im[0])] + \
         [dr['rect'].y1 for dr in pg.get_drawings() if dr['rect'].y1 < pg.rect.height * 0.94]
    return max(ys) / pg.rect.height if ys else 0


def media_sha(ruta):
    z = zipfile.ZipFile(ruta)
    return {n.split('/')[-1]: hashlib.sha256(z.read(n)).hexdigest() for n in z.namelist() if n.startswith('word/media/')}
