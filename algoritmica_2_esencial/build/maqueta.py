# -*- coding: utf-8 -*-
"""Primitivas de maquetación comunes (libro y solucionario). Estilo de la Edición Esencial Comercial:
Arial, VERDE BTI, cajas por tipo, cantSplit universal, portada a página completa, índice poblado."""
import copy, re
import docx
from docx.shared import Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

DARK, MED, LIGHT, FICHA = '1B5E20', '2E7D32', 'E8F5E9', 'F4FBF5'
AMB, AZUL, CREMA, NARANJA = 'B8860B', '1B4F72', 'FFF8E1', 'FFF3E0'
TEMPLATE = '/home/claude/alg3/src/Algoritmica_3er_Curso_TOMO_COMPLETO.docx'
# Formato de la colección desde oct-2026: oficio 21,6 × 33 cm, márgenes estrechos (1,27 cm),
# tablas y cajas ajustadas al ancho de la página (100 %), por costo de impresión para docentes y estudiantes.
PAG_W, PAG_H, MARG = 21.6, 33.0, 1.27
ANCHO = round(PAG_W - 2 * MARG, 2)   # 19,06 cm útiles (en el Plan Anual horizontal se recalcula)


def formato_oficio(sec, horizontal=False):
    from docx.enum.section import WD_ORIENT
    sec.orientation = WD_ORIENT.LANDSCAPE if horizontal else WD_ORIENT.PORTRAIT
    sec.page_width, sec.page_height = (Cm(PAG_H), Cm(PAG_W)) if horizontal else (Cm(PAG_W), Cm(PAG_H))
    sec.top_margin = sec.bottom_margin = sec.left_margin = sec.right_margin = Cm(MARG)
    sec.header_distance = sec.footer_distance = Cm(0.6)


def nuevo_doc(titulo, asunto, palabras):
    d = docx.Document(TEMPLATE)
    body = d.element.body
    for el in list(body):
        if el.tag != qn('w:sectPr'):
            body.remove(el)
    formato_oficio(d.sections[0])
    st = d.styles
    tam = {'Heading 1': (15.5, DARK, 18, 6), 'Heading 2': (13.5, DARK, 12, 4), 'Heading 3': (11.5, MED, 10, 3), 'Heading 4': (10.5, MED, 8, 2)}
    for n, (sz, col, b, a) in tam.items():
        s = st[n]; s.font.name = 'Arial'; s.font.size = Pt(sz); s.font.bold = True; s.font.italic = False
        s.font.color.rgb = RGBColor.from_string(col)
        s.paragraph_format.space_before = Pt(b); s.paragraph_format.space_after = Pt(a)
        s.paragraph_format.keep_with_next = True
        rpr = s.element.get_or_add_rPr()
        rf = rpr.find(qn('w:rFonts'))
        if rf is None:
            rf = OxmlElement('w:rFonts'); rpr.insert(0, rf)
        for k in list(rf.attrib):
            del rf.attrib[k]
        for k in ('w:ascii', 'w:hAnsi', 'w:cs'):
            rf.set(qn(k), 'Arial')
    try:
        pre = st['Título preliminar']
    except KeyError:
        pre = st.add_style('Título preliminar', WD_STYLE_TYPE.PARAGRAPH)
        pre.base_style = st['Heading 1']
        ppr = pre.element.get_or_add_pPr()
        ol = OxmlElement('w:outlineLvl'); ol.set(qn('w:val'), '9'); ppr.append(ol)
    for n, ind in (('toc 1', 0), ('toc 2', 0.4)):
        s = st[n]; s.font.name = 'Arial'; s.font.size = Pt(9.5)
        s.paragraph_format.space_after = Pt(1.5); s.paragraph_format.space_before = Pt(0)
        s.paragraph_format.left_indent = Cm(ind)
    st['toc 1'].font.bold = True
    st['toc 1'].paragraph_format.space_before = Pt(5)
    cp = d.core_properties
    cp.title = titulo; cp.subject = asunto; cp.author = 'Equipo editorial'; cp.last_modified_by = 'Equipo editorial'
    cp.keywords = palabras; cp.comments = ''; cp.revision = 1
    import datetime
    cp.created = cp.modified = datetime.datetime(2026, 10, 2, 12, 0, 0)
    return d


# ---------------- utilidades XML ----------------

def shd(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    for old in tcPr.findall(qn('w:shd')):
        tcPr.remove(old)
    s = OxmlElement('w:shd'); s.set(qn('w:val'), 'clear'); s.set(qn('w:color'), 'auto'); s.set(qn('w:fill'), fill)
    tcPr.append(s)


def bordes(t, color='BFBFBF', sz='4', internos=True):
    tblPr = t._tbl.tblPr
    for old in tblPr.findall(qn('w:tblBorders')):
        tblPr.remove(old)
    b = OxmlElement('w:tblBorders')
    for e in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        x = OxmlElement('w:' + e)
        if e.startswith('inside') and not internos:
            x.set(qn('w:val'), 'none')
        else:
            x.set(qn('w:val'), 'single'); x.set(qn('w:sz'), sz); x.set(qn('w:space'), '0'); x.set(qn('w:color'), color)
        b.append(x)
    tblPr.append(b)


def ancho_fijo(t, cms):
    # toda tabla ocupa el ancho útil completo: las columnas se escalan en proporción
    k = ANCHO / sum(cms)
    cms = [c * k for c in cms]
    t.autofit = False
    tblPr = t._tbl.tblPr
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
    w = OxmlElement('w:tblW'); w.set(qn('w:w'), '5000'); w.set(qn('w:type'), 'pct')
    for old in tblPr.findall(qn('w:tblW')):
        tblPr.remove(old)
    tblPr.append(w)
    grid = t._tbl.tblGrid
    for gc in list(grid):
        grid.remove(gc)
    for c in cms:
        gc = OxmlElement('w:gridCol'); gc.set(qn('w:w'), str(int(c * 567))); grid.append(gc)
    for row in t.rows:
        for i, cell in enumerate(row.cells):
            if i < len(cms):
                cell.width = Cm(cms[i])


def cant_split(t, header=False):
    for i, row in enumerate(t.rows):
        trPr = row._tr.get_or_add_trPr()
        if trPr.find(qn('w:cantSplit')) is None:
            trPr.append(OxmlElement('w:cantSplit'))
        if header and i == 0 and trPr.find(qn('w:tblHeader')) is None:
            trPr.append(OxmlElement('w:tblHeader'))


def keep_rows(t, salvo_ultima=True):
    rows = t.rows[:-1] if salvo_ultima else t.rows
    for row in rows:
        for c in row.cells:
            for p in c.paragraphs:
                p.paragraph_format.keep_with_next = True


def margenes_celda(t, top=60, left=100):
    tblPr = t._tbl.tblPr
    m = OxmlElement('w:tblCellMar')
    for e, v in (('top', top), ('left', left), ('bottom', top), ('right', left)):
        x = OxmlElement('w:' + e); x.set(qn('w:w'), str(v)); x.set(qn('w:type'), 'dxa'); m.append(x)
    tblPr.append(m)


def run(p, txt, bold=False, italic=False, size=None, color=None, font=None):
    r = p.add_run(txt); r.bold = bold; r.italic = italic
    if size: r.font.size = Pt(size)
    if color: r.font.color.rgb = RGBColor.from_string(color)
    if font:
        r.font.name = font
        rpr = r._r.get_or_add_rPr(); rf = rpr.find(qn('w:rFonts'))
        rf.set(qn('w:hAnsi'), font); rf.set(qn('w:cs'), font)
    return r


def par(d, txt='', size=10.5, bold=False, italic=False, color=None, align='j', antes=0, despues=4, indent=None, keep=False, cont=None):
    cont = cont or d
    p = cont.add_paragraph()
    if txt:
        run(p, txt, bold, italic, size, color)
    p.alignment = {'j': WD_ALIGN_PARAGRAPH.JUSTIFY, 'c': WD_ALIGN_PARAGRAPH.CENTER, 'l': WD_ALIGN_PARAGRAPH.LEFT, 'r': WD_ALIGN_PARAGRAPH.RIGHT}[align]
    pf = p.paragraph_format; pf.space_before = Pt(antes); pf.space_after = Pt(despues)
    if indent is not None: pf.left_indent = Cm(indent)
    if keep: pf.keep_with_next = True
    return p


def heading(d, txt, nivel, salto=False, estilo=None):
    p = d.add_paragraph(style=estilo or 'Heading %d' % nivel)
    p.add_run(txt)
    if salto:
        p.paragraph_format.page_break_before = True
    return p


def salto(d):
    p = d.add_paragraph(); p.add_run().add_break(WD_BREAK.PAGE)
    p.paragraph_format.space_after = Pt(0)
    return p


def separador(d, pts=2):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(pts); p.paragraph_format.space_before = Pt(0)
    r = p.add_run(); r.font.size = Pt(4)
    return p


# ---------------- bloques ----------------

def ficha(d, cap, tema, inds):
    t = d.add_table(rows=3, cols=2); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    bordes(t, 'A5D6A7', '6'); margenes_celda(t, 70, 110)
    caps = cap if isinstance(cap, list) else [cap]
    caps_txt = caps if len(caps) == 1 else ['• ' + x for x in caps]
    for row, (k, v) in zip(t.rows, (('Capacidad' if len(caps) == 1 else 'Capacidades', caps_txt), ('Tema', [tema]), ('Indicadores de logro', ['• ' + i for i in inds]))):
        shd(row.cells[0], DARK); shd(row.cells[1], FICHA)
        run(row.cells[0].paragraphs[0], k, True, size=9, color='FFFFFF')
        for j, v1 in enumerate(v):
            pp = row.cells[1].paragraphs[0] if j == 0 else row.cells[1].add_paragraph()
            pp.paragraph_format.space_after = Pt(1)
            run(pp, v1, size=9.5)
    ancho_fijo(t, [3.6, 13.0]); cant_split(t); keep_rows(t)
    separador(d, 4)
    return t


CAJAS = [('Concepto clave', CREMA, DARK), ('En Paraguay', LIGHT, DARK), ('Aplicación profesional', LIGHT, DARK),
         ('Ejemplo', FICHA, DARK), ('Errores frecuentes', NARANJA, 'A04000'), ('Modelo', 'F7F7F7', DARK),
         ('Competencia', CREMA, DARK), ('Caso', 'F5F5F5', DARK)]


def caja(d, titulo, cuerpo, fill=None, color_tit=None, mono=False, borde='9E9E9E', cont=None):
    if fill is None:
        fill, color_tit = 'F5F5F5', DARK
        for pref, f, c in CAJAS:
            if titulo.startswith(pref):
                fill, color_tit = f, c
                break
    cont = cont or d
    t = cont.add_table(rows=1, cols=1); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    bordes(t, borde, '6'); margenes_celda(t, 80, 120)
    c = t.rows[0].cells[0]; shd(c, fill)
    p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(2); p.paragraph_format.keep_with_next = True
    run(p, titulo, True, size=10, color=color_tit)
    for i, b in enumerate(cuerpo):
        es_cod = mono or b.startswith('§')
        if b.startswith('§'):
            b = b[1:]
        pp = c.add_paragraph(); pp.paragraph_format.space_after = Pt(1 if es_cod else 2)
        if es_cod:
            pp.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run(pp, b, size=9, font='Courier New')
        else:
            pp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            run(pp, b, size=9.5)
        if i < len(cuerpo) - 1:
            pp.paragraph_format.keep_with_next = True
    ancho_fijo(t, [ANCHO]); cant_split(t)
    separador(d if cont is d else cont, 3)
    return t


def _anchos(hdr, rows, total=None):
    total = total or ANCHO
    L = []
    for j in range(len(hdr)):
        col = [hdr[j]] + [r[j] for r in rows]
        L.append(max(min(len(x), 60) for x in col) + 4)
    s = sum(L)
    w = [max(1.8, total * x / s) for x in L]
    k = total / sum(w)
    return [round(x * k, 2) for x in w]


def tabla(d, hdr, rows, anchos=None, size=9, rotulo=None, cont=None):
    cont = cont or d
    if rotulo:
        par(cont, rotulo, 9.5, True, color=DARK, keep=True, despues=2)
    t = cont.add_table(rows=1 + len(rows), cols=len(hdr)); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    bordes(t, 'BDBDBD', '4'); margenes_celda(t, 40, 90)
    for j, h in enumerate(hdr):
        c = t.rows[0].cells[j]; shd(c, MED)
        run(c.paragraphs[0], h, True, size=size, color='FFFFFF')
    for i, r in enumerate(rows, 1):
        for j, v in enumerate(r):
            c = t.rows[i].cells[j]
            p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
            run(p, str(v), size=size)
            if i % 2 == 0:
                shd(c, 'F5F5F5')
    ancho_fijo(t, anchos or _anchos(hdr, rows)); cant_split(t, header=True)
    if len(rows) <= 8:
        keep_rows(t)
    separador(cont, 4)
    return t


def imagen(d, ruta, epigrafe, ancho_cm=15.5, lead=None):
    if lead:
        par(d, lead, keep=True)
    p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = True; p.paragraph_format.space_after = Pt(2); p.paragraph_format.space_before = Pt(4)
    p.add_run().add_picture(ruta, width=Cm(min(ancho_cm * 1.1, 17.5)))
    pe = par(d, epigrafe, 8.5, italic=True, color='595959', align='c', despues=6)
    return pe


def banda(d, titulo, sub, color, nombre=True):
    t = d.add_table(rows=1, cols=1); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    bordes(t, color, '6'); margenes_celda(t, 110, 140)
    c = t.rows[0].cells[0]; shd(c, color)
    p = c.paragraphs[0]; p.style = d.styles['Heading 2']; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(1)
    run(p, titulo.upper() if False else titulo, True, size=13.5, color='FFFFFF')
    p2 = c.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(p2, sub, False, size=10, color='FFFFFF')
    ancho_fijo(t, [ANCHO]); cant_split(t)
    if nombre:
        par(d, 'Nombre y Apellido: _______________________________  Curso: ______  Fecha: ____ / ____ / ____', 9.5, antes=8, despues=6)
    return t


def linea_nombre(d):
    return par(d, 'Nombre y Apellido: _______________________________  Curso: ______  Fecha: ____ / ____ / ____', 9.5, antes=2, despues=6)


def renglones(d, n=2):
    t = d.add_table(rows=n, cols=1); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    tblPr = t._tbl.tblPr
    for old in tblPr.findall(qn('w:tblBorders')):
        tblPr.remove(old)
    b = OxmlElement('w:tblBorders')
    for e in ('top', 'left', 'right', 'insideV'):
        x = OxmlElement('w:' + e); x.set(qn('w:val'), 'none'); b.append(x)
    for e in ('bottom', 'insideH'):
        x = OxmlElement('w:' + e); x.set(qn('w:val'), 'single'); x.set(qn('w:sz'), '4'); x.set(qn('w:space'), '0'); x.set(qn('w:color'), 'A0A0A0'); b.append(x)
    tblPr.append(b)
    for row in t.rows:
        trPr = row._tr.get_or_add_trPr()
        h = OxmlElement('w:trHeight'); h.set(qn('w:val'), '400'); h.set(qn('w:hRule'), 'exact'); trPr.append(h)
        p = row.cells[0].paragraphs[0]; p.paragraph_format.space_after = Pt(0)
    ancho_fijo(t, [ANCHO]); cant_split(t); keep_rows(t)
    separador(d, 2)
    return t


# ---------------- portada / contraportada ----------------

def imagen_pagina_completa(d, ruta, nombre='Portada'):
    """Inserta la imagen anclada a la página entera (detrás del texto) y salta de página."""
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(0); p.paragraph_format.space_before = Pt(0)
    r = p.add_run()
    r.add_picture(ruta, width=Cm(PAG_W), height=Cm(PAG_H))
    inline = r._r.find('.//' + qn('wp:inline'))
    extent = inline.find(qn('wp:extent')); docpr = inline.find(qn('wp:docPr')); graphic = inline.find(qn('a:graphic'))
    docpr.set('name', nombre); docpr.set('descr', nombre)
    anchor = OxmlElement('wp:anchor')
    for k, v in (('distT', '0'), ('distB', '0'), ('distL', '0'), ('distR', '0'), ('simplePos', '0'), ('relativeHeight', '1'),
                 ('behindDoc', '1'), ('locked', '1'), ('layoutInCell', '1'), ('allowOverlap', '1')):
        anchor.set(k, v)
    sp = OxmlElement('wp:simplePos'); sp.set('x', '0'); sp.set('y', '0'); anchor.append(sp)
    for tag, rel in (('wp:positionH', 'page'), ('wp:positionV', 'page')):
        pos = OxmlElement(tag); pos.set('relativeFrom', rel)
        off = OxmlElement('wp:posOffset'); off.text = '0'; pos.append(off); anchor.append(pos)
    anchor.append(copy.deepcopy(extent))
    ee = OxmlElement('wp:effectExtent')
    for k in ('l', 't', 'r', 'b'):
        ee.set(k, '0')
    anchor.append(ee)
    anchor.append(OxmlElement('wp:wrapNone'))
    anchor.append(copy.deepcopy(docpr))
    anchor.append(OxmlElement('wp:cNvGraphicFramePr'))
    anchor.append(copy.deepcopy(graphic))
    inline.getparent().replace(inline, anchor)
    return p


def primera_pagina_sin_pie(d):
    sec = d.sections[0]
    sec.different_first_page_header_footer = True
    for hf in (sec.first_page_footer, sec.first_page_header):
        hf.is_linked_to_previous = False
        for p in hf.paragraphs:
            for r in list(p.runs):
                r._r.getparent().remove(r._r)


def portada_en_seccion(d):
    """Cierra la sección de la portada (sin pie) y abre la sección del cuerpo."""
    from docx.enum.section import WD_SECTION
    d.add_section(WD_SECTION.NEW_PAGE)
    s0 = d.sections[0]
    for hf in (s0.footer, s0.header):
        hf.is_linked_to_previous = False
        for p in hf.paragraphs:
            for el in list(p._p):
                if el.tag != qn('w:pPr'):
                    p._p.remove(el)
    return d.sections[-1]


def pie_paginas(d, sec=None):
    sec = sec or d.sections[0]
    ft = sec.footer
    ft.is_linked_to_previous = False
    p = ft.paragraphs[0]
    for el in list(p._p):
        if el.tag != qn('w:pPr'):
            p._p.remove(el)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    def fld(instr):
        for kind in ('begin', None, 'separate', 'txt', 'end'):
            r = OxmlElement('w:r'); rpr = OxmlElement('w:rPr'); sz = OxmlElement('w:sz'); sz.set(qn('w:val'), '17'); rpr.append(sz); r.append(rpr)
            if kind is None:
                e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = instr
            elif kind == 'txt':
                e = OxmlElement('w:t'); e.text = '1'
            else:
                e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), kind)
            r.append(e); p._p.append(r)
    run(p, 'Página ', size=8.5, color='777777'); fld(' PAGE ')
    run(p, ' de ', size=8.5, color='777777'); fld(' NUMPAGES ')


# ---------------- índice poblado ----------------

def indice(d, entradas, paginas=None):
    """entradas: [(nivel, texto)]; paginas: [int] o None (marcadores). Campo TOC con resultado ya poblado."""
    tabpos = Cm(ANCHO - 0.05)
    ps = []
    for i, (niv, txt) in enumerate(entradas):
        p = d.add_paragraph(style='toc %d' % niv)
        p.paragraph_format.tab_stops.add_tab_stop(tabpos, WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        if i == 0:
            for kind, val in (('begin', None), ('instr', ' TOC \\o "1-2" \\h \\z \\u '), ('separate', None)):
                r = OxmlElement('w:r')
                if kind == 'instr':
                    e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = val
                else:
                    e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), kind)
                r.append(e); p._p.append(r)
        run(p, txt, bold=(niv == 1), size=9.5)
        p.add_run('\t')
        run(p, str(paginas[i]) if paginas else '000', bold=(niv == 1), size=9.5)
        ps.append(p)
    r = OxmlElement('w:r'); e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), 'end'); r.append(e); ps[-1]._p.append(r)
    return ps


def no_actualizar_campos(d):
    s = d.settings.element
    for el in s.findall(qn('w:updateFields')):
        s.remove(el)


def paginas_de(pdf, textos, desde=1):
    """Devuelve la página (1-based) de la primera aparición en orden de cada texto, desde 'desde'."""
    import pymupdf
    doc = pymupdf.open(pdf)
    norm = lambda s: re.sub(r'\s+', '', s.replace('­', ''))
    pags = [norm(pg.get_text()) for pg in doc]
    out = []; cur = desde - 1
    for t in textos:
        nt = norm(t)
        found = None
        for i in range(cur, len(pags)):
            if nt in pags[i]:
                found = i; break
        if found is None:
            raise ValueError('No se encontró en el PDF: ' + t)
        out.append(found + 1); cur = found
    return out, len(pags)


def seccion_sin_pie(d):
    """Nueva sección (página nueva) cuyo pie y encabezado quedan vacíos."""
    from docx.enum.section import WD_SECTION
    sec = d.add_section(WD_SECTION.NEW_PAGE)
    for hf in (sec.footer, sec.header, sec.first_page_footer, sec.first_page_header):
        hf.is_linked_to_previous = False
        for p in hf.paragraphs:
            for el in list(p._p):
                if el.tag != qn('w:pPr'):
                    p._p.remove(el)
    sec.different_first_page_header_footer = False
    return sec


def purgar_relaciones(d):
    """Elimina del paquete las imágenes heredadas de la plantilla que el documento ya no usa."""
    xml = d.element.xml
    part = d.part
    for rid, rel in list(part.rels.items()):
        if rel.reltype.endswith('/image') and ('"%s"' % rid) not in xml:
            del part.rels[rid]
