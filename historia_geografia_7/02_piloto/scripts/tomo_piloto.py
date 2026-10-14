"""Piloto de maqueta del tomo de Historia y Geografía 7.º.

Toma el DOCX base (texto e imágenes idénticos al maestro de octubre, ver
diagnóstico §2), conserva solo las secciones del piloto y aplica una de tres
variantes de maqueta. No cambia ninguna palabra del texto ni ninguna imagen:
solo saltos de página, tamaño de papel, márgenes, cuerpo de letra, la
disposición de las opciones múltiples y renglones para responder.

Uso: python3 tomo_piloto.py BASE.docx VARIANTE SALIDA.docx [paginas.json]
VARIANTE: oficio_actual | oficio_mejorado | a4_mejorado
paginas.json (opcional): {titulo: página}, para escribir el índice con números.
"""
import copy
import json
import re
import sys

import docx
from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt
from docx.table import Table
from docx.text.paragraph import Paragraph

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'

# Secciones del piloto: (título que empieza el bloque, título del bloque siguiente)
PILOTO = [
    ('UNIDAD 1 — Cómo mirar el tiempo y el espacio', 'Clase 2 — '),
    ('Clase 14 — ', 'Clase 15 — '),
    ('Clase 18 — ', 'UNIDAD 6 — '),   # incluye Continuación F y Evaluación U5
]

VARIANTES = {
    'oficio_actual':   dict(papel=(21.59, 33.02), margen=None, suma_pt=0.0, opciones=False, renglones=False),
    'oficio_mejorado': dict(papel=(21.59, 33.02), margen=(2.0, 2.0, 2.2, 2.0), suma_pt=1.0, opciones=True, renglones=True),
    'a4_mejorado':     dict(papel=(21.0, 29.7), margen=(1.8, 1.8, 2.0, 2.0), suma_pt=1.0, opciones=True, renglones=True),
}


def texto(el):
    return ''.join(t.text or '' for t in el.iter(W + 't'))


def es_p(el):
    return el.tag == W + 'p'


def estilo(doc, el):
    return Paragraph(el, doc).style.name if es_p(el) else ''


def poner_salto_antes(p_el):
    ppr = p_el.get_or_add_pPr()
    if ppr.find(qn('w:pageBreakBefore')) is None:
        ppr.insert(0, OxmlElement('w:pageBreakBefore'))


def parrafo_salto(doc):
    """Párrafo mínimo (1 pt, sin espacio) con salto antes: sirve para que una
    tabla (la banda de la evaluación) empiece en hoja nueva."""
    p = OxmlElement('w:p')
    ppr = OxmlElement('w:pPr')
    ppr.append(OxmlElement('w:pageBreakBefore'))
    sp = OxmlElement('w:spacing')
    sp.set(qn('w:before'), '0'); sp.set(qn('w:after'), '0')
    sp.set(qn('w:line'), '20'); sp.set(qn('w:lineRule'), 'exact')
    ppr.append(sp)
    rpr = OxmlElement('w:rPr'); sz = OxmlElement('w:sz'); sz.set(qn('w:val'), '2'); rpr.append(sz)
    ppr.append(rpr)
    p.append(ppr)
    return p


def recortar(doc):
    body = doc.element.body
    els = [e for e in body if e.tag != W + 'sectPr']
    conservar = set()
    # portada, presentación e índice: hasta la tabla de la prueba diagnóstica
    for i, e in enumerate(els):
        if e.tag == W + 'tbl' and texto(e).startswith('Prueba diagnóstica'):
            fin_frente = i
            break
    conservar.update(range(0, fin_frente))
    for ini, fin in PILOTO:
        a = next(i for i, e in enumerate(els) if es_p(e) and texto(e).startswith(ini)
                 and estilo(doc, e) == 'Heading 1')
        b = next(i for i, e in enumerate(els) if i > a and es_p(e) and texto(e).startswith(fin)
                 and estilo(doc, e) == 'Heading 1')
        conservar.update(range(a, b))
    for i, e in enumerate(els):
        if i not in conservar:
            body.remove(e)
    # párrafos vacíos que solo forzaban un salto (p. ej., antes de la prueba
    # diagnóstica, que no entra en el piloto): los saltos los pone corregir_saltos
    for e in [e for e in body if es_p(e)]:
        if not texto(e).strip() and e.find('.//' + W + 'pageBreakBefore') is not None \
                and not e.findall('.//' + A + 'blip'):
            body.remove(e)


def limpiar_relaciones(doc):
    """Quita del paquete las imágenes que ya no usa ninguna parte conservada."""
    usadas = {b.get(R + 'embed') for b in doc.element.body.iter(A + 'blip')}
    usadas |= {e.get(R + 'id') for e in doc.element.body.iter() if e.get(R + 'id')}
    for rid, rel in list(doc.part.rels.items()):
        if rel.reltype.endswith('/image') and rid not in usadas:
            del doc.part.rels[rid]


def es_banda_evaluacion(el):
    return el.tag == W + 'tbl' and re.match(r'EVALUACI[ÓO]N', texto(el).strip(), re.I)


def corregir_saltos(doc):
    """Regla: cada unidad, clase, continuación y evaluación empieza en hoja nueva.
    Una clase que sigue inmediatamente al título de su unidad comparte la hoja
    con él (la unidad abre la hoja)."""
    body = doc.element.body
    els = [e for e in body if e.tag != W + 'sectPr']
    for i, e in enumerate(els):
        st = estilo(doc, e)
        if st == 'Heading 1':
            t = texto(e)
            if t in ('Presentación', 'Índice'):
                continue
            previo = els[i - 1] if i else None
            if t.startswith('Clase') and previo is not None and estilo(doc, previo) == 'Heading 1' \
                    and texto(previo).startswith('UNIDAD'):
                continue
            poner_salto_antes(e)
        elif es_banda_evaluacion(e):
            e.addprevious(parrafo_salto(doc))


def agrandar_letra(doc, suma):
    if not suma:
        return
    for st in doc.styles:
        try:
            f = st.font
        except AttributeError:
            continue
        if f is not None and f.size is not None:
            f.size = Pt(f.size.pt + suma)
    for r in doc.element.body.iter(W + 'sz'):
        v = r.get(qn('w:val'))
        if v and r.getparent().tag in (W + 'rPr',) and int(v) > 4:
            r.set(qn('w:val'), str(int(round(int(v) + 2 * suma))))
    for r in doc.element.body.iter(W + 'szCs'):
        v = r.get(qn('w:val'))
        if v and int(v) > 4:
            r.set(qn('w:val'), str(int(round(int(v) + 2 * suma))))


OPC = re.compile(r'^\s{2,}([a-d])\)\s')


def agrupar_opciones(doc, ancho_util_cm):
    """Junta las cuatro opciones a)–d) de cada ítem en uno o dos renglones con
    tabulaciones. El texto de cada opción no cambia."""
    body = doc.element.body
    els = [e for e in body if e.tag != W + 'sectPr']
    i = 0
    while i < len(els):
        grupo = []
        j = i
        while j < len(els) and es_p(els[j]) and OPC.match(texto(els[j])) and \
                OPC.match(texto(els[j])).group(1) == 'abcd'[len(grupo)]:
            grupo.append(els[j]); j += 1
        if len(grupo) == 4:
            ops = [texto(g).strip() for g in grupo]
            larga = max(len(o) for o in ops)
            por_renglon = 4 if larga <= 22 else 2
            primero = Paragraph(grupo[0], doc)
            pf = primero.paragraph_format
            pf.left_indent = Cm(0.6)
            pf.space_after = Pt(4)
            paso = (ancho_util_cm - 0.6) / por_renglon
            for k in range(1, por_renglon):
                pf.tab_stops.add_tab_stop(Cm(0.6 + paso * k))
            run_modelo = grupo[0].find(W + 'r')
            for t in list(grupo[0]):
                if t.tag == W + 'r':
                    grupo[0].remove(t)
            for k, o in enumerate(ops):
                if k:
                    sep = copy.deepcopy(run_modelo)
                    for c in list(sep):
                        if c.tag != W + 'rPr':
                            sep.remove(c)
                    if k % por_renglon == 0:
                        br = OxmlElement('w:br'); sep.append(br)
                    else:
                        sep.append(OxmlElement('w:tab'))
                    grupo[0].append(sep)
                r = copy.deepcopy(run_modelo)
                for c in list(r):
                    if c.tag != W + 'rPr':
                        r.remove(c)
                t = OxmlElement('w:t'); t.text = o
                t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
                r.append(t)
                grupo[0].append(r)
            for g in grupo[1:]:
                body.remove(g)
            els = [e for e in body if e.tag != W + 'sectPr']
            i = els.index(grupo[0]) + 1
        else:
            i += 1


RENGLONES = [
    (re.compile(r'^\d+\.\s*(Explicá|Respondé|¿|Describí|Escribí|Fundamentá|Compará|Justificá|Relacioná|Trabajá con la fuente|Identificá|Proponé|Analizá|Indicá|Nombrá)'), 3),
    (re.compile(r'^\d+\.\s*\(\.\.\.\.\)'), 1),   # V/F: renglón para justificar
]


def renglon(doc):
    p = OxmlElement('w:p')
    ppr = OxmlElement('w:pPr')
    bdr = OxmlElement('w:pBdr'); b = OxmlElement('w:bottom')
    b.set(qn('w:val'), 'single'); b.set(qn('w:sz'), '4'); b.set(qn('w:space'), '1'); b.set(qn('w:color'), '9AA5B1')
    bdr.append(b)
    # renglones seguidos con el mismo borde forman un grupo: «between» dibuja
    # la línea entre ellos (sin él, Word y LibreOffice muestran una sola)
    bt = OxmlElement('w:between')
    for k in ('val', 'sz', 'space', 'color'):
        bt.set(qn('w:' + k), b.get(qn('w:' + k)))
    bdr.append(bt)
    ppr.append(bdr)
    sp = OxmlElement('w:spacing'); sp.set(qn('w:before'), '0'); sp.set(qn('w:after'), '0')
    sp.set(qn('w:line'), '440'); sp.set(qn('w:lineRule'), 'exact'); ppr.append(sp)
    ind = OxmlElement('w:ind'); ind.set(qn('w:left'), '340'); ppr.append(ind)
    p.append(ppr)
    return p


def agregar_renglones(doc):
    """Renglones para responder bajo las preguntas abiertas y para justificar
    los verdadero/falso. La consigna queda unida a sus renglones."""
    body = doc.element.body
    for e in [e for e in body if es_p(e)]:
        t = texto(e).strip()
        for rx, n in RENGLONES:
            if rx.match(t):
                Paragraph(e, doc).paragraph_format.keep_with_next = True
                ancla = e
                for k in range(n):
                    nuevo = renglon(doc)
                    if k < n - 1:
                        nppr = nuevo.find(W + 'pPr'); kn = OxmlElement('w:keepNext'); nppr.insert(0, kn)
                    ancla.addnext(nuevo); ancla = nuevo
                break


def ajustar_pagina(doc, papel, margen):
    s = doc.sections[0]
    s.page_width, s.page_height = Cm(papel[0]), Cm(papel[1])
    if margen:
        s.left_margin, s.right_margin, s.top_margin, s.bottom_margin = (Cm(x) for x in margen)
    ancho = papel[0] - s.left_margin.cm - s.right_margin.cm
    # imágenes: misma proporción; solo se reducen si no entran en el ancho útil
    for ext in doc.element.body.iter('{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}extent'):
        cx, cy = int(ext.get('cx')), int(ext.get('cy'))
        maxcx = int(Cm(ancho))
        if cx > maxcx:
            f = maxcx / cx
            ext.set('cx', str(maxcx)); ext.set('cy', str(int(cy * f)))
            gd = ext.getparent()
            for x in gd.iter(A + 'ext'):
                x.set('cx', str(maxcx)); x.set('cy', str(int(int(x.get('cy')) * f)))
    # tablas: ancho total al ancho útil, columnas proporcionales
    for t in doc.element.body.iter(W + 'tbl'):
        grid = t.find(W + 'tblGrid')
        if grid is None:
            continue
        cols = grid.findall(W + 'gridCol')
        tot = sum(int(c.get(qn('w:w'))) for c in cols)
        if not tot:
            continue
        objetivo = int(Cm(ancho).twips) if hasattr(Cm(ancho), 'twips') else int(ancho / 2.54 * 1440)
        if t.getparent().tag != W + 'body':
            continue
        f = objetivo / tot
        for c in cols:
            c.set(qn('w:w'), str(int(int(c.get(qn('w:w'))) * f)))
        for tc in t.iter(W + 'tcW'):
            if tc.get(qn('w:type')) == 'dxa':
                tc.set(qn('w:w'), str(int(int(tc.get(qn('w:w'))) * f)))
        tw = t.find(W + 'tblPr/' + W + 'tblW')
        if tw is not None and tw.get(qn('w:type')) == 'dxa':
            tw.set(qn('w:w'), str(objetivo))
    return ancho


def indice_estatico(doc, ancho_cm, paginas):
    """Reemplaza el campo de índice por un índice de las secciones del piloto
    con número de página real (calculado en una primera pasada)."""
    body = doc.element.body
    els = [e for e in body if e.tag != W + 'sectPr']
    i_ind = next(i for i, e in enumerate(els) if es_p(e) and texto(e) == 'Índice')
    # quitar el campo del índice (párrafos de estilo toc y el cierre del campo)
    j = i_ind + 1
    while j < len(els) and es_p(els[j]) and (estilo(doc, els[j]).startswith('toc') or
                                              els[j].findall('.//' + W + 'fldChar')):
        body.remove(els[j]); j += 1
    def primera_linea(e):
        return texto(e) if es_p(e) else texto(e.find('.//' + W + 'p'))
    orden = [primera_linea(e) for e in body
             if (es_p(e) and estilo(doc, e) == 'Heading 1' and texto(e) not in ('Presentación', 'Índice'))
             or es_banda_evaluacion(e)]
    ancla = [e for e in body if es_p(e) and texto(e) == 'Índice'][0]
    for t in orden:
        etiqueta = t
        m = re.match(r'^EVALUACIÓN DE LA UNIDAD (\d+)$', t)
        if m:
            etiqueta = 'Evaluación de la Unidad ' + m.group(1)
        p = docx.text.paragraph.Paragraph(OxmlElement('w:p'), doc)
        ancla.addnext(p._p); ancla = p._p
        pf = p.paragraph_format
        pf.tab_stops.add_tab_stop(Cm(ancho_cm), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        pf.space_after = Pt(3)
        es_unidad = t.startswith('UNIDAD')
        pf.left_indent = Cm(0 if es_unidad else 0.6)
        pf.space_before = Pt(8 if es_unidad else 0)
        num = str(paginas.get(t, '')) if paginas else ''
        run = p.add_run(etiqueta + '\t' + num)
        run.bold = es_unidad
    return orden


def main():
    base, variante, salida = sys.argv[1:4]
    paginas = json.load(open(sys.argv[4])) if len(sys.argv) > 4 else {}
    v = VARIANTES[variante]
    doc = docx.Document(base)
    recortar(doc)
    limpiar_relaciones(doc)
    corregir_saltos(doc)
    ancho = ajustar_pagina(doc, v['papel'], v['margen'])
    agrandar_letra(doc, v['suma_pt'])
    if v['opciones']:
        agrupar_opciones(doc, ancho)
    if v['renglones']:
        agregar_renglones(doc)
    orden = indice_estatico(doc, ancho, paginas)
    doc.save(salida)
    json.dump(orden, open(salida + '.secciones.json', 'w'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
