# -*- coding: utf-8 -*-
"""Formatos comerciales reutilizables del plan anual y del plan de clase (oficio vertical).

Decisiones de Fernando (20-oct-2026):
- oficio 21,59 × 33,02 cm, vertical; el plan anual también vertical, y la matriz extensa en un anexo horizontal antes
  que achicar la letra;
- campos editables de institución, docente, sección y año lectivo de uso;
- el año de EDICIÓN del material (fijo) se distingue del año lectivo de UTILIZACIÓN (editable);
- el plan anual sigue PRELIMINAR mientras falten indicadores e instrumentos definitivos;
- no se generan los 36 planes: el formato del plan de clase sale en blanco.

Los campos editables son controles de contenido de Word (texto sin formato) con su texto indicativo; en LibreOffice se
ven como texto que se reemplaza. Márgenes: perfil propuesto O3 de `../lote_1_oficio/build/perfiles.py` (interior
2,5 cm, exterior 1,8 cm, superior e inferior 1,5 cm, espejados); el anexo horizontal usa los mismos valores girados.

Uso: python3 formatos_comerciales/formatos.py  → FORMATO_PLAN_ANUAL_OFICIO y FORMATO_PLAN_DE_CLASE_OFICIO (.docx y .pdf)
"""
import csv, os, subprocess, sys
sys.dont_write_bytecode = True
from docx import Document
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(AQUI)
EDICION = '2026'   # año de edición del material: fijo
MATERIA = 'Análisis y Diseño de Sistemas'
CURSO = '3.er Curso · Bachillerato Técnico en Informática · Plan Optativo'
ROTULO = ('Propuesta editorial para el programa institucional del Plan Optativo. Las capacidades no son '
          'capacidades oficiales del MEC.')
VERDE, CLARO = '1B5E20', 'E8F5E9'   # identidad «verde BTI», provisional
PAPEL, M = (21.59, 33.02), dict(interior=2.5, exterior=1.8, superior=1.5, inferior=1.5)


# ---------------------------------------------------------------- utilidades
def documento():
    d = Document()
    st = d.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(10)
    st.paragraph_format.space_after = Pt(3)
    s = d.sections[0]
    s.page_width, s.page_height = Cm(PAPEL[0]), Cm(PAPEL[1])
    s.left_margin, s.right_margin = Cm(M['interior']), Cm(M['exterior'])
    s.top_margin, s.bottom_margin = Cm(M['superior']), Cm(M['inferior'])
    s.header_distance = s.footer_distance = Cm(0.6)
    d.settings.element.insert(0, OxmlElement('w:mirrorMargins'))
    return d


def campo(p, indicativo, ancho_cm=None):
    """Control de contenido de texto sin formato, editable, con texto indicativo."""
    sdt = OxmlElement('w:sdt'); pr = OxmlElement('w:sdtPr')
    al = OxmlElement('w:alias'); al.set(qn('w:val'), indicativo); pr.append(al)
    tag = OxmlElement('w:tag'); tag.set(qn('w:val'), indicativo); pr.append(tag)
    ph = OxmlElement('w:showingPlcHdr'); pr.append(ph)
    pr.append(OxmlElement('w:text'))
    sdt.append(pr)
    cont = OxmlElement('w:sdtContent'); r = OxmlElement('w:r'); rpr = OxmlElement('w:rPr')
    col = OxmlElement('w:color'); col.set(qn('w:val'), '808080'); rpr.append(col); r.append(rpr)
    t = OxmlElement('w:t'); t.text = '«%s»' % indicativo; t.set(qn('xml:space'), 'preserve'); r.append(t)
    cont.append(r); sdt.append(cont)
    p._p.append(sdt)
    return sdt


def sombrear(c, fill):
    pr = c._tc.get_or_add_tcPr(); s = OxmlElement('w:shd')
    s.set(qn('w:val'), 'clear'); s.set(qn('w:color'), 'auto'); s.set(qn('w:fill'), fill); pr.append(s)


def bordes(t):
    pr = t._tbl.tblPr; b = OxmlElement('w:tblBorders')
    for lado in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = OxmlElement('w:' + lado); e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), '4'); e.set(qn('w:color'), '9E9E9E'); b.append(e)
    pr.append(b)


def anchos(t, cm):
    pr = t._tbl.tblPr
    for tag in ('w:tblW', 'w:tblLayout'):
        o = pr.find(qn(tag))
        if o is not None: pr.remove(o)
    w = OxmlElement('w:tblW'); w.set(qn('w:w'), str(int(Cm(sum(cm)).twips))); w.set(qn('w:type'), 'dxa'); pr.append(w)
    l = OxmlElement('w:tblLayout'); l.set(qn('w:type'), 'fixed'); pr.append(l)
    g = t._tbl.tblGrid
    for x in list(g): g.remove(x)
    for a in cm:
        gc = OxmlElement('w:gridCol'); gc.set(qn('w:w'), str(int(Cm(a).twips))); g.append(gc)
    for r in t.rows:
        for c, a in zip(r.cells, cm): c.width = Cm(a)


def no_dividir(t, encabezado=True):
    for i, r in enumerate(t.rows):
        tr = r._tr.get_or_add_trPr(); tr.append(OxmlElement('w:cantSplit'))
        if i == 0 and encabezado: tr.append(OxmlElement('w:tblHeader'))


def tabla(d, enc, filas, cm, tam=8.5):
    t = d.add_table(rows=1 + len(filas), cols=len(enc)); t.alignment = WD_TABLE_ALIGNMENT.CENTER; bordes(t)
    for j, h in enumerate(enc):
        c = t.rows[0].cells[j]; sombrear(c, VERDE)
        r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(tam); r.font.color.rgb = RGBColor.from_string('FFFFFF')
    for i, f in enumerate(filas, 1):
        for j, v in enumerate(f):
            r = t.rows[i].cells[j].paragraphs[0].add_run(str(v)); r.font.size = Pt(tam)
    anchos(t, cm); no_dividir(t)
    return t


def pie(sec, texto):
    p = sec.footer.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(texto + ' · Página '); r.font.size = Pt(8)
    for instr in ('PAGE',):
        f1 = OxmlElement('w:fldSimple'); f1.set(qn('w:instr'), instr); rr = OxmlElement('w:r'); tt = OxmlElement('w:t'); tt.text = '1'; rr.append(tt); f1.append(rr); p._p.append(f1)


def identificacion(d, titulo, extra=()):
    h = d.add_paragraph(); h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = h.add_run(titulo); r.bold = True; r.font.size = Pt(15); r.font.color.rgb = RGBColor.from_string(VERDE)
    p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run('%s · %s' % (MATERIA, CURSO)); r.font.size = Pt(10)
    filas = [('Institución', 'nombre de la institución'), ('Docente', 'nombre y apellido'),
             ('Sección y turno', 'sección y turno'), ('Año lectivo de uso', 'año en que se aplica')] + list(extra)
    t = d.add_table(rows=len(filas), cols=2); bordes(t)
    for (k, ind), row in zip(filas, t.rows):
        sombrear(row.cells[0], CLARO)
        rk = row.cells[0].paragraphs[0].add_run(k); rk.bold = True; rk.font.size = Pt(9.5)
        campo(row.cells[1].paragraphs[0], ind)
    anchos(t, [4.5, PAPEL[0] - M['interior'] - M['exterior'] - 4.5]); no_dividir(t, encabezado=False)
    n = d.add_paragraph()
    r = n.add_run('Material: edición %s (año de edición, fijo). El año lectivo de uso se completa arriba y puede ser otro.' % EDICION)
    r.italic = True; r.font.size = Pt(8.5)
    n = d.add_paragraph(); r = n.add_run(ROTULO); r.italic = True; r.font.size = Pt(8.5)


def pdf(ruta):
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', AQUI, ruta], check=True,
                   capture_output=True, env=dict(os.environ, HOME='/tmp/lohome'))


# ---------------------------------------------------------------- plan anual
def plan_anual():
    filas = list(csv.DictReader(open(os.path.join(ADS, 'plan_anual', 'plan_anual_preliminar.csv'), encoding='utf-8')))
    assert len(filas) == 36
    d = documento()
    identificacion(d, 'PLAN ANUAL — VERSIÓN PRELIMINAR')
    av = d.add_paragraph()
    r = av.add_run('Versión preliminar: faltan los indicadores de los Capítulos 5 a 18 y los procedimientos e instrumentos '
                   'definitivos. Se genera desde plan_anual/plan_anual_preliminar.csv.')
    r.bold = True; r.font.size = Pt(9); r.font.color.rgb = RGBColor.from_string('8D6E00')
    util = PAPEL[0] - M['interior'] - M['exterior']
    for cap in sorted({int(f['capitulo']) for f in filas}):
        fs = [f for f in filas if int(f['capitulo']) == cap]
        f0 = fs[0]
        h = d.add_paragraph(); h.paragraph_format.keep_with_next = True; h.paragraph_format.space_before = Pt(6)
        r = h.add_run('Unidad %s · Capítulo %d. %s' % (f0['unidad'], cap, f0['titulo_capitulo'])); r.bold = True
        r.font.size = Pt(10.5); r.font.color.rgb = RGBColor.from_string(VERDE)
        t = tabla(d, ['Campo', 'Contenido'], [
            ['Capacidades (propuestas)', f0['capacidades_capitulo']],
            ['Secciones', f0['secciones']],
            ['Indicadores', f0['indicadores'].replace(' | ', '\n')],
            ['Antecedentes MEC', f0['antecedentes_mec']],
        ], [3.6, util - 3.6], tam=8.5)
        for row in t.rows[1:]:
            sombrear(row.cells[0], CLARO)
        tabla(d, ['Enc.', 'Foco del encuentro', 'Evidencia o evaluación', 'Hito', 'Procedimientos e instrumentos'],
              [[f['encuentro'], f['foco_work'], f['evidencia_work'], f['hito'] or '—', '(a definir)'] for f in fs],
              [1.0, 5.4, 4.6, 1.0, util - 12.0], tam=8.5)
    # Anexo horizontal: matriz de HC por categoría (9 columnas) — no se achica la letra en vertical
    sec = d.add_section(WD_SECTION.NEW_PAGE)
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width, sec.page_height = Cm(PAPEL[1]), Cm(PAPEL[0])
    sec.left_margin, sec.right_margin = Cm(M['superior']), Cm(M['inferior'])
    sec.top_margin, sec.bottom_margin = Cm(M['exterior']), Cm(M['interior'])
    h = d.add_paragraph(); r = h.add_run('Anexo — Matriz de horas cátedra por categoría (distribución de 180 HC, v2.1)')
    r.bold = True; r.font.size = Pt(11); r.font.color.rgb = RGBColor.from_string(VERDE)
    cats = ['A', 'D', 'P', 'V', 'Doc', 'G', 'E']
    tabla(d, ['Enc.', 'Cap.', 'Foco del encuentro'] + cats + ['Total'],
          [[f['encuentro'], f['capitulo'], f['foco_work']] + [f['hc_' + c] for c in cats]
           + [sum(int(f['hc_' + c]) for c in cats)] for f in filas]
          + [['', '', 'Total'] + [sum(int(f['hc_' + c]) for f in filas) for c in cats] + [180]],
          [1.0, 1.0, 14.2] + [1.35] * 7 + [1.4], tam=8.5)
    n = d.add_paragraph(); r = n.add_run('A análisis · D diseño · P programación · V verificación y validación · '
                                          'Doc documentación de entrega · G gestión del proyecto · E evaluación.')
    r.font.size = Pt(8.5)
    pie(d.sections[0], '%s · %s · Edición %s · Plan anual preliminar' % (MATERIA, '3.º BTI', EDICION))   # el anexo hereda el pie
    ruta = os.path.join(AQUI, 'FORMATO_PLAN_ANUAL_OFICIO.docx'); d.save(ruta); pdf(ruta)
    return ruta


# ---------------------------------------------------------------- plan de clase (en blanco)
def plan_de_clase():
    d = documento()
    util = PAPEL[0] - M['interior'] - M['exterior']
    t0 = d.add_paragraph(); r = t0.add_run('Plan de Clase N.º '); r.bold = True; r.font.size = Pt(14); r.font.color.rgb = RGBColor.from_string(VERDE)
    campo(t0, 'número'); r = t0.add_run(' — '); r.font.size = Pt(14); campo(t0, 'foco corto del encuentro')
    b = d.add_paragraph(); campo(b, 'institución'); b.add_run(' · Plan de Clase N.º '); campo(b, 'número'); b.add_run(' de 36 · Año lectivo '); campo(b, 'año de uso')
    t = d.add_table(rows=5, cols=4); bordes(t)
    datos = [('Docente', 'nombre y apellido', 'Disciplina', None), ('Curso', None, 'Tiempo', '5 HC (Encuentro N.º __ de 36)'),
             ('Organizador curricular', 'unidad y capítulo', 'Sección', 'sección'), ('Material', 'tomo: capítulo y secciones', 'Fecha', 'fecha'),
             ('Tema', 'tema del plan anual, textual', '', '')]
    fijos = {(0, 3): 'Análisis y Diseño de Sistemas (Plan Optativo, programa institucional)', (1, 1): '3.º BTI'}
    for i, (k1, v1, k2, v2) in enumerate(datos):
        c = t.rows[i].cells
        sombrear(c[0], CLARO); c[0].paragraphs[0].add_run(k1).bold = True
        if (i, 1) in fijos: c[1].paragraphs[0].add_run(fijos[(i, 1)])
        elif v1: campo(c[1].paragraphs[0], v1)
        if k2:
            sombrear(c[2], CLARO); c[2].paragraphs[0].add_run(k2).bold = True
            if (i, 3) in fijos: c[3].paragraphs[0].add_run(fijos[(i, 3)])
            elif v2 and v2.startswith('5 HC'): c[3].paragraphs[0].add_run(v2)
            elif v2: campo(c[3].paragraphs[0], v2)
    t.rows[4].cells[1].merge(t.rows[4].cells[3])
    anchos(t, [3.4, util / 2 - 3.4, 2.6, util / 2 - 2.6]); no_dividir(t, encabezado=False)
    for titulo, cuerpo in [
        ('Capacidades propuestas para el programa institucional (no son capacidades oficiales del MEC)', 'capacidad de la ficha del capítulo, textual, con su código'),
        ('Indicadores de logro', 'de 2 a 4 indicadores de la ficha que se evidencian en este encuentro'),
    ]:
        p = d.add_paragraph(); p.paragraph_format.space_before = Pt(6); rr = p.add_run(titulo); rr.bold = True; rr.font.color.rgb = RGBColor.from_string(VERDE)
        campo(d.add_paragraph(), cuerpo)
    m = tabla(d, ['Momento', 'Actividades', 'Tiempo'], [['Inicio', '', 'aprox. __ HC'], ['Desarrollo', '', 'aprox. __ HC'],
                                                       ['Cierre', '', 'aprox. __ HC'], ['Total', '', '5 HC']], [2.6, util - 5.0, 2.4], tam=9.5)
    for i in range(1, 4):
        campo(m.rows[i].cells[1].paragraphs[0], 'actividades del tramo, con secciones, figuras, tablas y actividades del tomo')
    for titulo, cuerpo in [('Recursos y medios auxiliares', 'solo los que usan las actividades'),
                           ('Tarea (si la guía la asigna)', 'número de actividad')]:
        p = d.add_paragraph(); p.paragraph_format.space_before = Pt(6); rr = p.add_run(titulo); rr.bold = True; rr.font.color.rgb = RGBColor.from_string(VERDE)
        campo(d.add_paragraph(), cuerpo)
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(6); rr = p.add_run('Evaluación'); rr.bold = True; rr.font.color.rgb = RGBColor.from_string(VERDE)
    e = tabla(d, ['Procedimientos', 'Instrumentos', 'Criterios'], [['', '', '']], [util / 3] * 3, tam=9.5)
    for j, ind in enumerate(('del plan anual, textual', 'del plan anual, textual', 'de la guía; nombrar la evidencia del encuentro (Work §5.2)')):
        campo(e.rows[1].cells[j].paragraphs[0], ind)
    d.add_paragraph('Observaciones: ' + '_' * 80).paragraph_format.space_before = Pt(8)
    f = d.add_paragraph('\n\nDocente ______________________________          Dirección — Visto bueno ______________________________')
    f.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pie(d.sections[0], '%s · 3.º BTI · Edición %s · Plan de clase' % (MATERIA, EDICION))
    ruta = os.path.join(AQUI, 'FORMATO_PLAN_DE_CLASE_OFICIO.docx'); d.save(ruta); pdf(ruta)
    return ruta


if __name__ == '__main__':
    for r in (plan_anual(), plan_de_clase()):
        print(os.path.basename(r))
