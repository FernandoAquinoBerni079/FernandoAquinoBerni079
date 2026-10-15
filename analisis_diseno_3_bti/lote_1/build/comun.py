# -*- coding: utf-8 -*-
"""Piezas de maqueta del lote 1 que no estaban en el piloto: portada del lote, ficha con varias capacidades,
registros del dossier, índice estático y conversión a PDF. helpers.py y maqueta.py se usan sin cambios
(copiados del Capítulo 4 v2.1; build/verificar.py comprueba que sean idénticos)."""
import os, re, subprocess, shutil, tempfile
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

import helpers as H
import maqueta as M

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
import sys
sys.path.insert(0, os.path.join(RAIZ, 'caso'))
import dossier as D

VERSION = 'v1.0 (lote 1, para auditoría)'


def portada(doc, tipo_doc, estado):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]
    H.sombrear_celda(c, H.ID['DARK'])
    p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run('\nAnálisis y Diseño de Sistemas\n3.er Curso · Bachillerato Técnico en Informática\n')
    r.bold = True; r.font.size = Pt(22); r.font.color.rgb = RGBColor.from_string('FFFFFF')
    H.cant_split(t)
    doc.add_paragraph()
    H.p_texto(doc, 'Del problema al prototipo web', bold=True, size=14, color=H.ID['DARK'], align='center')
    H.p_texto(doc, 'LOTE EDITORIAL 1 — PRELIMINARES Y UNIDAD I (CAPÍTULOS 1 A 3)', bold=True, size=12,
              color=H.ID['MED'], align='center')
    H.p_texto(doc, tipo_doc, size=11.5, align='center')
    H.p_texto(doc, 'Plan Optativo · propuesta para el programa institucional · Biblioteca Comercial 2026', size=11, align='center')
    H.p_texto(doc, 'Proyecto conductor: Sistema de Gestión de Biblioteca Escolar', bold=True, size=11.5,
              color=H.ID['MED'], align='center')
    doc.add_paragraph()
    H.caja(doc, 'Estado de este documento', estado, tipo='neutra')
    H.p_texto(doc, 'Versión %s' % VERSION, size=10, align='center', antes=6)
    H.p_texto(doc, 'República del Paraguay · 2026', bold=True, size=12, align='center', antes=6)
    H.salto_pagina(doc)


def titulo_en_pagina_nueva(doc, texto, nivel=1):
    """Título que empieza página con «salto de página antes»: no deja una hoja en blanco si la anterior termina justo."""
    h = doc.add_heading(texto, level=nivel)
    h.paragraph_format.page_break_before = True
    return h


def encabezado_capitulo(doc, C):
    titulo_en_pagina_nueva(doc, '%s — %s' % (C.CAPITULO, C.TITULO))
    H.p_texto(doc, C.UNIDAD, italic=True, size=10.5, color=H.ID['MED'])
    M.ficha(doc, C)
    for t in C.APERTURA:
        H.p_texto(doc, t)
    H.caja(doc, 'Con qué se conecta este capítulo', C.ARTICULACION, tipo='neutra')


def registro(doc, cod, lead=None):
    """Caja de un registro del dossier con todas sus líneas y su contexto."""
    r = D.REGISTRO[cod]
    if lead:
        H.keep_next(H.p_texto(doc, lead))
    lineas = []
    for c, hab, txt in r['lineas']:
        lineas.append('%s  %s%s' % (c, (hab + ': ') if hab else '', txt))
    H.caja(doc, 'Registro %s — %s (caso ficticio)' % (cod, r['titulo']), lineas, tipo='referencia',
           nota=r['contexto'])


def tabla_codigos(doc, rotulo, pares, enc=('Código', 'Texto'), anchos=(1.8, 14.8), extra_col=None):
    if extra_col:
        filas = [[c, t, ''] for c, t in pares]
        return M.tabla(doc, (list(enc) + [extra_col[0]], filas), list(anchos), rotulo=rotulo)
    return M.tabla(doc, (list(enc), [[c, t] for c, t in pares]), list(anchos), rotulo=rotulo)


# ---------------------------------------------------------------- índice estático
MARCA_INDICE = '§§INDICE§§'


def indice_marcador(doc, titulo='Índice'):
    doc.add_heading(titulo, level=1)
    H.p_texto(doc, MARCA_INDICE, size=9)
    H.salto_pagina(doc)


def rellenar_indice(doc, entradas, paginas):
    """Reemplaza el párrafo marcador por las líneas del índice. entradas: [(nivel, texto)]."""
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    marca = [p for p in doc.paragraphs if p.text == MARCA_INDICE][0]
    ancla = marca
    for nivel, texto in entradas:
        pag = paginas.get(texto, 0)
        np_ = OxmlElement('w:p')
        ancla._p.addnext(np_)
        from docx.text.paragraph import Paragraph
        p = Paragraph(np_, ancla._parent)
        pf = p.paragraph_format
        pf.space_after = Pt(1.5); pf.space_before = Pt(3 if nivel == 1 else 0)
        pf.left_indent = Cm({1: 0, 2: 0.5, 3: 1.0}[nivel])
        pf.tab_stops.add_tab_stop(Cm(16.6), alignment=2, leader=1)   # derecha, con puntos
        r = p.add_run(texto); r.font.size = Pt(9.8 if nivel == 1 else 9.3); r.bold = (nivel == 1)
        r2 = p.add_run('\t%s' % (pag or '—')); r2.font.size = Pt(9.5)
        ancla = p
    marca._p.getparent().remove(marca._p)


def a_pdf(ruta_docx, carpeta_salida):
    os.makedirs(carpeta_salida, exist_ok=True)
    perfil = tempfile.mkdtemp(prefix='lo_perfil_')
    try:
        subprocess.run(['soffice', '-env:UserInstallation=file://' + perfil, '--headless', '--convert-to', 'pdf',
                        '--outdir', carpeta_salida, ruta_docx], check=True, capture_output=True, timeout=300)
    finally:
        shutil.rmtree(perfil, ignore_errors=True)
    return os.path.join(carpeta_salida, os.path.splitext(os.path.basename(ruta_docx))[0] + '.pdf')


def paginas_de_titulos(ruta_pdf, titulos, desde=2):
    """Primera página (1-based) en que cada título aparece como línea propia, a partir de la página 'desde'."""
    import pymupdf
    pdf = pymupdf.open(ruta_pdf)
    lineas_pag = []
    for i, pg in enumerate(pdf):
        lineas_pag.append([l.strip() for l in pg.get_text().split('\n')])
    res = {}
    for t in titulos:
        for i in range(desde, len(lineas_pag)):
            ls = lineas_pag[i]
            # títulos largos pueden partirse en dos renglones
            unidas = [ls[k] + ' ' + ls[k + 1] for k in range(len(ls) - 1)]
            if t in ls or t in unidas:
                res[t] = i + 1
                break
    return res, len(pdf)


def saltos_a_titulos(doc):
    """Convierte cada párrafo que solo contiene un salto de página y va seguido de un título en «salto de página
    antes» de ese título. Así, si la página anterior termina justo, no queda una hoja en blanco (caso de
    helpers.evaluacion(), que no se modifica). Devuelve cuántos saltos convirtió."""
    from docx.oxml.ns import qn
    ps = doc.paragraphs
    n = 0
    for p, sig in zip(ps, ps[1:]):
        brs = p._p.findall('.//' + qn('w:br'))
        solo_salto = (p.text.strip() == '' and brs and all(b.get(qn('w:type')) == 'page' for b in brs))
        if solo_salto and sig.style.name.startswith('Heading'):
            sig.paragraph_format.page_break_before = True
            p._p.getparent().remove(p._p)
            n += 1
    return n
