# -*- coding: utf-8 -*-
"""Planes de Clase — Desarrollo Personal y Social 7.º (formato V3 de la colección Esencial Comercial, oficio vertical).
Capacidad, tema e indicadores se leen de las fichas del libro; procedimientos e instrumentos, iguales al Plan Anual
(pa_rows.json); momentos, recursos y criterios, de fuente/planes. Entregable: solo .docx (el PDF es de control).
Una sección por plan: título con estilo «Plan de Clase», banda, datos, capacidad/indicadores, momentos
(cantSplit selectivo: Desarrollo divisible), recursos, evaluación, observaciones y firmas; encabezado de
continuación por STYLEREF; portada a página completa; índice poblado y verificado contra el PDF."""
import os, re, json
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import maqueta as M
import json as _json
import curriculo as C


def a_pdf(docx_path, outdir):
    import subprocess, os
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', outdir, docx_path], check=True, capture_output=True, env=dict(os.environ, HOME='/tmp/lohome'))
    return outdir + os.path.basename(docx_path)[:-5] + '.pdf'

B = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = B + '../salida/'; CTRL = B + '../verificacion/control_pdf/'
NOMBRE = 'Desarrollo_Personal_y_Social_7mo_Grado_PLANES_DE_CLASE_2026'
DARK, MED, LIGHT, GRIS = M.DARK, M.MED, M.LIGHT, 'BFBFBF'
W = M.ANCHO
MIN_HC, HC = 40, 3


def planes():
    from build_plan_anual import ficha_de
    rows = {r['n']: r for r in _json.load(open(B + 'pa_rows.json'))}
    out = []
    for e in C.ENCUENTROS:
        n, t, k, u, caps_n, tit, _ = e
        j = _json.load(open(B + '../fuente/planes/e%02d.json' % n, encoding='utf-8'))
        if t in 'CP':
            caps, tema, inds = ficha_de(n)
        else:
            caps = [C.CAP[c] for c in (C.UNIDAD_CAPS[u] if t == 'E' else caps_n)]
            inds = rows[n]['indicadores']; tema = rows[n]['tema'][0]
        unidad = ('UNIDAD %d — %s' % (u, C.UNIDADES[u])) if t in 'CE' else ('Proyecto Educativo Comunitario — taller %d de 7' % k) if t == 'P' else ('Unidades 1 a 4' if n == 18 else 'Unidades 5 a 7')
        material = 'Libro del estudiante · ' + {'C': 'Clase %d' % k, 'P': 'Taller PEC %d y ficha de la bitácora' % k, 'E': 'Evaluación de la Unidad %d (página propia)' % u, 'I': 'Evaluación integradora (página propia)'}[t]
        tiempos = [j['inicio']['min'], j['desarrollo']['min'], j['cierre']['min']]
        assert sum(tiempos) == HC * MIN_HC, 'minutos distintos de 120 en el plan %d' % n
        out.append(dict(idx=n, titulo=C.rotulo(e), tipo=t, unidad=unidad, material=material,
                        tema=(tema if t in 'CP' else tema), capacidad=caps, cap_rot='Capacidades del área vinculadas' if t == 'P' else None,
                        indicadores=inds, nombres=['Inicio', 'Desarrollo', 'Cierre'], tiempos=tiempos,
                        momentos={'Inicio': j['inicio']['acts'], 'Desarrollo': j['desarrollo']['acts'], 'Cierre': j['cierre']['acts']},
                        recursos=j['recursos'], proc=rows[n]['proc'], inst=rows[n]['inst'], criterios=j['criterios']))
    return out


PL = planes()


def sec_setup(sec, primera=True):
    M.formato_oficio(sec)
    sec.different_first_page_header_footer = primera


def fld(par, instr, size=8.5, italic=False, color=None):
    for el in ('begin', 'instr', 'end'):
        r = OxmlElement('w:r'); rPr = OxmlElement('w:rPr')
        s = OxmlElement('w:sz'); s.set(qn('w:val'), str(int(size * 2))); rPr.append(s)
        if italic: rPr.append(OxmlElement('w:i'))
        if color:
            c = OxmlElement('w:color'); c.set(qn('w:val'), color); rPr.append(c)
        r.append(rPr)
        if el == 'instr':
            e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = instr
        else:
            e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), el)
        r.append(e); par._p.append(r)


def limpiar(par):
    for el in list(par._p):
        if el.tag != qn('w:pPr'):
            par._p.remove(el)


def pie(sec):
    for foot in (sec.first_page_footer, sec.footer):
        foot.is_linked_to_previous = False
        par = foot.paragraphs[0]; par.alignment = WD_ALIGN_PARAGRAPH.CENTER; limpiar(par)
        r = par.add_run('Página '); r.font.size = Pt(8.5); r.font.color.rgb = RGBColor.from_string('777777')
        fld(par, ' PAGE ')
        r = par.add_run(' de '); r.font.size = Pt(8.5); r.font.color.rgb = RGBColor.from_string('777777')
        fld(par, ' NUMPAGES ')


def encabezado_cont(sec):
    sec.first_page_header.is_linked_to_previous = False
    for p in sec.first_page_header.paragraphs:
        limpiar(p)
    hdr = sec.header; hdr.is_linked_to_previous = False
    par = hdr.paragraphs[0]; par.alignment = WD_ALIGN_PARAGRAPH.RIGHT; limpiar(par)
    fld(par, ' STYLEREF "Plan de Clase" \\* MERGEFORMAT ', size=8.5, italic=True, color=MED)
    r = par.add_run(' · continuación'); r.font.size = Pt(8.5); r.italic = True; r.font.color.rgb = RGBColor.from_string(DARK)


def tabla(d, filas, cols, anchos, proteger=True):
    t = d.add_table(rows=filas, cols=cols); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    M.bordes(t, GRIS, '4'); M.margenes_celda(t, 40, 90)
    M.ancho_fijo(t, anchos)
    if proteger:
        M.cant_split(t)
    return t


def celda(cell, val, bold=False, blanco=False, size=9, center=False, vinetas=False):
    par = cell.paragraphs[0]
    if center: par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    items = val if isinstance(val, list) else [val]
    for i, linea in enumerate(items):
        if i:
            par = cell.add_paragraph()
        par.paragraph_format.space_after = Pt(1)
        r = par.add_run(('• ' if vinetas else '') + linea)
        r.bold = bold; r.font.size = Pt(size)
        if blanco: r.font.color.rgb = RGBColor.from_string('FFFFFF')


def desproteger(row):
    trPr = row._tr.get_or_add_trPr()
    cs = trPr.find(qn('w:cantSplit'))
    if cs is not None: trPr.remove(cs)


def esp(d, pts=2):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(pts); p.paragraph_format.space_before = Pt(0)
    r = p.add_run(); r.font.size = Pt(3)


def plan(d, p, total):
    idx = p['idx']
    tp = d.add_paragraph(style='Plan de Clase'); tp.add_run('Plan de Clase N.º %d — %s' % (idx, p['titulo']))
    t = tabla(d, 1, 1, [W]); M.shd(t.rows[0].cells[0], DARK)
    celda(t.rows[0].cells[0], 'Institución: ______________________________     ·     Plan de Clase N.º %d de %d · 2026' % (idx, total), bold=True, blanco=True, center=True)
    esp(d)
    datos = [('Docente', '______________________________', 'Área', 'Desarrollo Personal y Social'),
             ('Curso', '7.º grado — Educación Escolar Básica, Tercer Ciclo', 'Tiempo', '%d horas cátedra (%d min)' % (HC, HC * MIN_HC)),
             ('Unidad', p['unidad'], 'Sección', '____________'),
             ('Material', p['material'], 'Fecha', '____ / ____ / 2026')]
    t = tabla(d, len(datos) + 1, 4, [2.4, 6.4, 2.1, 6.1])
    for i, (l1, v1, l2, v2) in enumerate(datos):
        c = t.rows[i].cells
        M.shd(c[0], MED); celda(c[0], l1, bold=True, blanco=True); celda(c[1], v1)
        M.shd(c[2], MED); celda(c[2], l2, bold=True, blanco=True); celda(c[3], v2)
    fr = t.rows[len(datos)]
    M.shd(fr.cells[0], MED); celda(fr.cells[0], 'Tema', bold=True, blanco=True)
    celda(fr.cells[1].merge(fr.cells[3]), p['tema'])
    esp(d)
    t = tabla(d, 2, 2, [3.4, 13.6])
    M.shd(t.rows[0].cells[0], MED); capv = p['capacidad'] if isinstance(p['capacidad'], list) else [p['capacidad']]; celda(t.rows[0].cells[0], p['cap_rot'] or ('Capacidad' if len(capv) == 1 else 'Capacidades'), bold=True, blanco=True); celda(t.rows[0].cells[1], capv, vinetas=len(capv) > 1)
    M.shd(t.rows[1].cells[0], MED); celda(t.rows[1].cells[0], ['Indicadores', 'de logro'] + (['(elaboración', 'editorial)'] if p['tipo'] == 'P' else []), bold=True, blanco=True); celda(t.rows[1].cells[1], p['indicadores'], vinetas=True)
    esp(d)
    nm = len(p['nombres'])
    t = tabla(d, nm + 1, 3, [2.6, 12.3, 2.1])
    for j, hh in enumerate(('MOMENTO', 'ACTIVIDADES', 'TIEMPO')):
        M.shd(t.rows[0].cells[j], DARK); celda(t.rows[0].cells[j], hh, bold=True, blanco=True, center=(j != 1))
    t.rows[0]._tr.get_or_add_trPr().append(OxmlElement('w:tblHeader'))
    for c in t.rows[0].cells:
        for par in c.paragraphs: par.paragraph_format.keep_with_next = True
    for i, (nombre, mins) in enumerate(zip(p['nombres'], p['tiempos']), 1):
        c = t.rows[i].cells
        M.shd(c[0], LIGHT); celda(c[0], nombre, bold=True)
        celda(c[1], p['momentos'][nombre], vinetas=True, size=8.5); celda(c[2], '%d min' % mins, center=True)
    for i in range(2, nm):
        desproteger(t.rows[i])
    esp(d)
    t = tabla(d, 1, 2, [3.4, 13.6])
    M.shd(t.rows[0].cells[0], MED); celda(t.rows[0].cells[0], ['Recursos y medios', 'auxiliares'], bold=True, blanco=True)
    celda(t.rows[0].cells[1], p['recursos'])
    esp(d)
    t = tabla(d, 4, 2, [3.4, 13.6])
    fb = t.rows[0].cells[0].merge(t.rows[0].cells[1]); M.shd(fb, DARK); celda(fb, 'EVALUACIÓN', bold=True, blanco=True, center=True, size=10)
    for i, (l, v, vin) in enumerate((('Procedimientos', p['proc'], False), ('Instrumentos', p['inst'], False), ('Criterios', p['criterios'], True)), 1):
        M.shd(t.rows[i].cells[0], MED); celda(t.rows[i].cells[0], l, bold=True, blanco=True); celda(t.rows[i].cells[1], v, vinetas=vin)
    esp(d)
    po = d.add_paragraph(); po.paragraph_format.space_after = Pt(10); po.paragraph_format.keep_with_next = True; r = po.add_run('Observaciones: '); r.bold = True; r.font.size = Pt(9.5)
    r = po.add_run('_' * 74); r.font.size = Pt(9.5)
    t = tabla(d, 1, 2, [8.5, 8.5])
    for c in t.rows[0].cells:
        tcPr = c._tc.get_or_add_tcPr(); b = OxmlElement('w:tcBorders')
        for e in ('top', 'left', 'bottom', 'right'):
            x = OxmlElement('w:' + e); x.set(qn('w:val'), 'nil'); b.append(x)
        tcPr.append(b)
    celda(t.rows[0].cells[0], ['____________________________', 'Docente'], center=True, size=8.5)
    celda(t.rows[0].cells[1], ['____________________________', 'Dirección — Visto bueno'], center=True, size=8.5)


COMO_SE_USA = [
 'Los 36 planes siguen la secuencia del libro del estudiante y tienen la misma numeración que el Plan Anual: 20 planes corresponden a las clases del componente Orientación Educacional y Vocacional, 7 a los talleres del Proyecto Educativo Comunitario (Planes 17, 19, 24, 29, 32, 34 y 35), 7 a las evaluaciones de unidad y 2 a las evaluaciones integradoras de etapa (Planes 18 y 36). Completan las 3 horas cátedra semanales del área; la institución puede ajustar fechas sin alterar la progresión.',
 'El tema, la capacidad y los indicadores se toman de las fichas del libro; las capacidades se transcriben textualmente del programa del MEC. En los talleres del proyecto, que no tienen capacidades propias en el programa, se indican las capacidades del área vinculadas y los indicadores son de elaboración editorial. Los procedimientos y los instrumentos coinciden con el Plan Anual.',
 'Los tiempos se calcularon con una hora cátedra de 40 minutos: 3 horas cátedra equivalen a 120 minutos, repartidos en inicio, desarrollo y cierre. La institución que trabaje con otra duración de hora cátedra reajusta el reparto en la misma proporción.',
 'Las secciones «Mirate» del libro son privadas y no se califican. Las tareas del proyecto fuera del aula se hacen en horario escolar, con autorización de la dirección y, cuando corresponde, de las familias. La institución, el docente, la sección y la fecha quedan en blanco para su llenado; el documento es editable.',
]


def construir(pags=None):
    d = M.nuevo_doc('Desarrollo Personal y Social 7.º grado — Planes de clase', 'Material del docente: 36 planes de clase', 'Desarrollo Personal y Social; planes de clase; Proyecto Educativo Comunitario')
    st = d.styles
    st['Normal'].font.size = Pt(9.5)
    try:
        ps = st['Plan de Clase']
    except KeyError:
        ps = st.add_style('Plan de Clase', WD_STYLE_TYPE.PARAGRAPH)
    ps.base_style = st['Normal']; ps.font.name = 'Arial'; ps.font.size = Pt(13.5); ps.font.bold = True
    ps.font.color.rgb = RGBColor.from_string(DARK)
    pf = ps.paragraph_format; pf.space_before = Pt(0); pf.space_after = Pt(6); pf.keep_with_next = True
    ppr = ps.element.get_or_add_pPr()
    if ppr.find(qn('w:outlineLvl')) is None:
        ol = OxmlElement('w:outlineLvl'); ol.set(qn('w:val'), '0'); ppr.append(ol)
    sec_setup(d.sections[0], primera=False)
    M.imagen_pagina_completa(d, B + 'portadas/portada_planes.png')
    sec = d.add_section(WD_SECTION.NEW_PAGE); sec_setup(sec, primera=False)
    s0 = d.sections[0]
    for hf in (s0.footer, s0.header):
        hf.is_linked_to_previous = False
        for p in hf.paragraphs: limpiar(p)
    M.heading(d, 'Cómo se usa este documento', 1, estilo='Título preliminar')
    for t in COMO_SE_USA:
        M.par(d, t, 10)
    M.heading(d, 'Índice', 1, estilo='Título preliminar')
    E = [(1, 'Plan de Clase N.º %d — %s' % (p['idx'], p['titulo'])) for p in PL]
    ps_ = M.indice(d, E, pags)
    for q in ps_:
        q.style = d.styles['toc 2']; q.paragraph_format.left_indent = Cm(0)
        for r in q.runs: r.bold = False
        q.paragraph_format.tab_stops.add_tab_stop(Cm(M.ANCHO - 0.05), 2, 1)
    pie(sec)
    for p in PL:
        s = d.add_section(WD_SECTION.NEW_PAGE); sec_setup(s, primera=True); pie(s); encabezado_cont(s)
        plan(d, p, len(PL))
    M.no_actualizar_campos(d)
    M.purgar_relaciones(d)
    return d, E


if __name__ == '__main__':
    tmp = B + 'tmp/'; os.makedirs(tmp, exist_ok=True)
    d, E = construir(None)
    p1 = tmp + NOMBRE + '.docx'; d.save(p1); pdf1 = a_pdf(p1, tmp)
    import pymupdf
    doc = pymupdf.open(pdf1)
    idx_last = max(i for i, pg in enumerate(doc) if re.search(r'\.{5,}\s*000', pg.get_text())) + 1
    pags, total = M.paginas_de(pdf1, [t for _, t in E], desde=idx_last + 1)
    for it in range(3):
        d, E = construir(pags)
        out = OUT + NOMBRE + '.docx'; d.save(out); os.makedirs(CTRL, exist_ok=True); pdf = a_pdf(out, CTRL)
        pags2, total = M.paginas_de(pdf, [t for _, t in E], desde=idx_last + 1)
        if pags2 == pags: break
        pags = pags2
    json.dump({'entradas': E, 'paginas': pags, 'total': total}, open(B + 'indice_planes.json', 'w'), ensure_ascii=False, indent=1)
    print('Planes: páginas', total, 'índice verificado =', pags2 == pags)
