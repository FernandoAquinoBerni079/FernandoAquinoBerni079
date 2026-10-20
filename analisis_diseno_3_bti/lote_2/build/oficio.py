# -*- coding: utf-8 -*-
"""Perfil de página O3 de la colección (decisión de Fernando del 20-oct-2026), aplicado sobre la maqueta del lote 1.

Oficio 21,59 × 33,02 cm, vertical; interior 2,5 cm, exterior 1,8 cm, superior e inferior 1,5 cm; márgenes espejados.
Es la misma capa que usó la candidata O3 aprobada del lote 1 (`lote_1_oficio_candidata/build/construir_candidata.py`),
reunida acá para que cualquier lote (y después el tomo anual) la aplique igual:
  1. página y márgenes del perfil, con márgenes espejados;
  2. anchos de tabla escalados al ancho útil (las fuentes los escriben para 16,6 cm) y ajustados por palabra: ninguna
     palabra de una celda queda más ancha que su columna (métrica de Carlito, igual a Calibri), sin cambiar el ancho
     total de la tabla;
  3. índice con la tabulación derecha al nuevo ancho;
  4. sin el párrafo vacío de separación antes de un título que abre hoja o del final del documento;
  5. tablas en HOJA_NUEVA: su rótulo abre hoja nueva (lo decide el ciclo de construcción con el control de filas).
`lote_1/build/helpers.py`, `maqueta.py` y `comun.py` se importan sin modificarlos: los cambios se hacen al importar."""
import os, re, sys
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
L2 = os.path.dirname(AQUI)
ADS = os.path.dirname(L2)
FUENTE_L1 = os.path.join(ADS, 'lote_1', 'build')
CANDIDATA = os.path.join(ADS, 'lote_1_oficio_candidata', 'build')
for p in (FUENTE_L1, CANDIDATA):
    if p not in sys.path:
        sys.path.append(p)

from docx.shared import Cm
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import helpers as H
import maqueta as M
import comun as K
import controles_impresion as CI   # control de filas de la candidata O3, sin cambios
assert os.path.dirname(H.__file__) == FUENTE_L1 and os.path.dirname(M.__file__) == FUENTE_L1, 'se importó otra maqueta'

PERFIL = dict(nombre='O3', papel=(21.59, 33.02), interior=2.5, exterior=1.8, superior=1.5, inferior=1.5, espejo=True)
ENCABEZADO_PIE = 0.6
ANCHO_FUENTE = 16.6
ANCHO = round(PERFIL['papel'][0] - PERFIL['interior'] - PERFIL['exterior'], 2)   # 17,29 cm
F = ANCHO / ANCHO_FUENTE

_new_doc, _fijar, _rellenar, _finalizar = H.new_doc, M.fijar_anchos, K.rellenar_indice, H.finalizar
AJUSTES = []
HOJA_NUEVA = set()
_FUENTES = {}
CARLITO = {False: '/usr/local/share/fonts/carlito/Carlito-Regular.ttf', True: '/usr/local/share/fonts/carlito/Carlito-Bold.ttf'}
MARGEN_CELDA = 2 * 0.19 + 0.06


def new_doc():
    doc = _new_doc()
    s = doc.sections[0]
    s.page_width, s.page_height = Cm(PERFIL['papel'][0]), Cm(PERFIL['papel'][1])
    s.left_margin, s.right_margin = Cm(PERFIL['interior']), Cm(PERFIL['exterior'])
    s.top_margin, s.bottom_margin = Cm(PERFIL['superior']), Cm(PERFIL['inferior'])
    s.header_distance = s.footer_distance = Cm(ENCABEZADO_PIE)
    st = doc.settings.element
    if st.find(qn('w:mirrorMargins')) is None:
        st.insert(0, OxmlElement('w:mirrorMargins'))
    return doc


def _ancho_cm(palabra, pt, negrita):
    from PIL import ImageFont
    k = (pt, negrita)
    if k not in _FUENTES:
        _FUENTES[k] = ImageFont.truetype(CARLITO[negrita], size=int(round(pt * 20)))
    return _FUENTES[k].getlength(palabra) / 20 / 72 * 2.54


def _minimo_columna(t, j):
    m = 0.0
    for fila in t.rows:
        if j >= len(fila.cells):
            continue
        for p in fila.cells[j].paragraphs:
            for r in p.runs:
                pt = r.font.size.pt if r.font.size else 10.5
                for w in re.findall(r'\S+', r.text):
                    m = max(m, _ancho_cm(w, pt, bool(r.bold)))
    return m + MARGEN_CELDA


def fijar_anchos(t, anchos):
    a = [round(x * F, 3) for x in anchos]
    minimos = [_minimo_columna(t, j) for j in range(len(a))]
    for j in range(len(a)):
        falta = minimos[j] - a[j]
        if falta > 0:
            k = max(range(len(a)), key=lambda c: a[c] - minimos[c] if c != j else -1e9)
            assert a[k] - minimos[k] >= falta, 'no hay holgura para la columna %d de «%s»' % (j, t.rows[0].cells[0].text[:30])
            AJUSTES.append((t.rows[0].cells[0].text[:40], j + 1, round(a[j], 2), round(minimos[j], 2)))
            a[k] = round(a[k] - falta, 3); a[j] = round(minimos[j], 3)
    _fijar(t, a)


TAB_FUENTE = str(int(Cm(ANCHO_FUENTE).twips))


def rellenar_indice(doc, entradas, paginas):
    _rellenar(doc, entradas, paginas)
    for tab in doc.element.body.iter(qn('w:tab')):
        if tab.get(qn('w:pos')) == TAB_FUENTE:
            tab.set(qn('w:pos'), str(int(Cm(ANCHO).twips)))


def finalizar(doc, ruta):
    body = doc.element.body
    for p in list(body.iterchildren(qn('w:p'))):
        vacio = (not ''.join(t.text or '' for t in p.iter(qn('w:t'))).strip() and p.find('.//' + qn('w:drawing')) is None
                 and p.find('.//' + qn('w:br')) is None and p.find('.//' + qn('w:fldChar')) is None)
        sig = p.getnext()
        if vacio and sig is not None and (sig.tag == qn('w:sectPr') or sig.find('.//' + qn('w:pageBreakBefore')) is not None):
            body.remove(p)
    for t in body.iterchildren(qn('w:tbl')):
        prev = t.getprevious()
        rot = ''.join(x.text or '' for x in prev.iter(qn('w:t'))) if prev is not None and prev.tag == qn('w:p') else ''
        if rot and rot in HOJA_NUEVA:
            ppr = prev.find(qn('w:pPr'))
            if ppr is None:
                ppr = OxmlElement('w:pPr'); prev.insert(0, ppr)
            if ppr.find(qn('w:pageBreakBefore')) is None:
                ppr.insert(0, OxmlElement('w:pageBreakBefore'))
    return _finalizar(doc, ruta)


def incompletas(dx, pdf):
    """Rótulos de las tablas a las que les falta alguna fila en el PDF (control de filas de la candidata O3)."""
    return [x['rotulo'] for x in CI.filas_de_tablas(dx, pdf) if x['filas_impresas'] < x['filas_docx'] and x['rotulo']]


H.new_doc = new_doc
M.fijar_anchos = fijar_anchos
K.rellenar_indice = rellenar_indice
H.finalizar = finalizar
