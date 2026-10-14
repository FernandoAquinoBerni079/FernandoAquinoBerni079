# -*- coding: utf-8 -*-
"""Edición diferencial del Plan Anual, los Planes de Clase y el Solucionario candidatos. Uso: python3 edit_docs.py 7|8|9
Plan Anual y Planes: solo .docx (el PDF va a verificacion/ para control visual). Solucionario: .docx y .pdf."""
import sys, os, re, copy
import docx, pymupdf
from docx.shared import Cm, Pt
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.section import WD_ORIENT
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import docx_ops as O
import maqueta as M
import render as R
import config_grados as G

g = sys.argv[1]
C = G.GRADOS[g]
B = O.E
OUT = B + '../%s/' % C['carpeta']
CTRL = B + '../verificacion/%s/control_pdf/' % C['carpeta']
M.DARK, M.MED, M.LIGHT, M.FICHA = '6A3E7A', '8E5BA6', 'F3ECF7', 'F8F3FA'
CAP = C['CAP']
TALLER = C['talleres']            # {'A': (encuentro, [caps]), ...}


def lit(ks, sep=' '):
    return sep.join('«%s»' % CAP[k] for k in ks)


def portada_seccion(d, ruta, horizontal_resto=False):
    """Portada a página completa en una sección vertical propia al principio del documento (sin pie)."""
    body = d.element.body
    p = M.imagen_pagina_completa(d, ruta)
    body.remove(p._p); body.insert(0, p._p)
    # sectPr de la sección de portada (oficio vertical, sin pie)
    sp = OxmlElement('w:sectPr')
    pgSz = OxmlElement('w:pgSz'); pgSz.set(qn('w:w'), str(int(21.59 / 2.54 * 1440))); pgSz.set(qn('w:h'), str(int(33.02 / 2.54 * 1440)))
    pgMar = OxmlElement('w:pgMar')
    for k in ('top', 'right', 'bottom', 'left'):
        pgMar.set(qn('w:' + k), '720')
    for k in ('header', 'footer', 'gutter'):
        pgMar.set(qn('w:' + k), '0')
    sp.append(pgSz); sp.append(pgMar)
    ppr = p._p.get_or_add_pPr(); ppr.append(sp)


def pdf_control(ruta):
    return O.a_pdf(ruta, CTRL)


# ---------------- Plan Anual ----------------

def plan_anual():
    d = docx.Document(C['base_pa'])
    O.margenes(d)
    for viejo, nuevo in C['pa_reemplazos']:
        O.reemplazar_en_doc(d, viejo, nuevo)
    # capacidades literales en las bandas de unidad
    n = 0
    for p in d.element.body.iter(qn('w:p')):
        tx = O.texto(p)
        m = re.match(r'^(Unidad (\d+) · [^·]+ · )Capacidades: ', tx)
        if m:
            u = int(m.group(2))
            O.reemplazar_parrafo(p, m.group(1) + 'Capacidades (programa MEC): ' + lit(C['unidad_caps'][u]))
            n += 1
    assert n >= 7, 'bandas de unidad: %d' % n
    # talleres PEC: capacidades del área vinculadas, en lugar de la vinculación genérica
    for letra, (enc, caps) in TALLER.items():
        O.reemplazar_en_doc(d, C['pa_pec_generico'][letra],
                            C['pa_pec_generico'][letra].replace('Vinculado a la unidad de Orientación correspondiente.',
                                                               'Capacidades del área vinculadas (programa MEC): ' + lit(caps) + ' Indicadores: elaboración editorial.'))
    portada_seccion(d, B + 'portadas/%s/portada_plan_anual.png' % g)
    ruta = OUT + C['nombre_pa'] + '.docx'; d.save(ruta)
    return ruta


# ---------------- Planes de Clase ----------------

def planes():
    d = docx.Document(C['base_planes'])
    O.margenes(d)
    for viejo, nuevo in C['planes_reemplazos']:
        O.reemplazar_en_doc(d, viejo, nuevo, min_veces=1)
    body = d.element.body
    fichas = [t for t in body.iter(qn('w:tbl')) if O.texto(t.find('.//' + qn('w:tc'))).strip() in ('Capacidad', 'Capacidades')]
    assert len(fichas) == 36, 'fichas de planes: %d' % len(fichas)
    for n, t in enumerate(fichas, 1):
        tipo, caps, extra = C['plan_caps'][n]
        tr = t.findall(qn('w:tr'))[0]; tcs = tr.findall(qn('w:tc'))
        rot = {'C': 'Capacidad' if len(caps) == 1 else 'Capacidades', 'P': 'Capacidades del área vinculadas',
               'E': 'Capacidades evaluadas', 'I': 'Capacidades evaluadas'}[tipo]
        O.reemplazar_parrafo(tcs[0].find(qn('w:p')), rot)
        viejo = O.texto(tcs[1]).strip()
        lineas = [CAP[k] for k in caps] if len(caps) == 1 else ['• ' + CAP[k] for k in caps]
        if tipo == 'P':
            obj = re.sub(r'\s*\(objetivo didáctico.*$', '', viejo).strip()
            lineas += ['Objetivo del taller (elaboración editorial; el PEC no tiene capacidades propias en el programa): ' + obj]
        O.fijar_celda(tcs[1], lineas)
    # talleres: los momentos remiten a las consignas agregadas en el tomo
    for letra in TALLER:
        O.reemplazar_en_doc(d, C['planes_cierre_pec'][letra], C['planes_cierre_pec'][letra] +
                            ' Resolución de las consignas 1 a 3 («Pensá y respondé») y acuerdo de la tarea «En equipo» (consigna 4).')
    portada_seccion(d, B + 'portadas/%s/portada_planes.png' % g)
    ruta = OUT + C['nombre_planes'] + '.docx'; d.save(ruta)
    return ruta


# ---------------- Solucionario ----------------

def solucionario():
    d = docx.Document(C['base_sol'])
    O.margenes(d)
    M.ANCHO = round(M.PAG_W - 2 * M.MARG, 2)
    for viejo, nuevo in C['sol_reemplazos']:
        O.reemplazar_en_doc(d, viejo, nuevo)
    body = d.element.body
    ini = next(el for el in body if el.tag == qn('w:p') and O.texto(el).strip().startswith('ANEXO DOCENTE'))
    els = list(body); i = els.index(ini)
    for el in els[i:]:
        if el.tag != qn('w:sectPr'):
            body.remove(el)
    R.NIVELES.update({'#': 1, '##': 2, '###': 3})
    R.render(d, R.leer(C['pec_sol']))
    portada_seccion(d, B + 'portadas/%s/portada_solucionario.png' % g)
    ruta = OUT + C['nombre_sol'] + '.docx'; d.save(ruta)
    pdf = O.a_pdf(ruta, OUT)
    return ruta, pdf


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    qué = sys.argv[2:] or ['pa', 'planes', 'sol']
    if 'pa' in qué:
        r = plan_anual(); p = pdf_control(r); print('Plan Anual', pymupdf.open(p).page_count, 'págs. (PDF solo de control)')
    if 'planes' in qué:
        r = planes(); p = pdf_control(r); print('Planes', pymupdf.open(p).page_count, 'págs. (PDF solo de control)')
    if 'sol' in qué:
        r, p = solucionario(); print('Solucionario', pymupdf.open(p).page_count, 'págs.')
