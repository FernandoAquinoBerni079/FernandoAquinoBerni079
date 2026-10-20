# -*- coding: utf-8 -*-
"""Versión de PRUEBA del lote 1 en oficio, reconstruida desde las fuentes del lote 1 sin modificarlas.

Uso: python3 lote_1_oficio/build/construir_oficio.py O1|O2|O3
Salida: lote_1_oficio/<perfil>/ADS_3BTI_LOTE1_ESTUDIANTE_OFICIO_<perfil>.docx/.pdf y …_GUIA_DOCENTE_OFICIO_<perfil>.docx/.pdf

Qué hace:
- importa los módulos de `lote_1/build/` (contenido, caso, maqueta, constructor y guía) tal como están;
- cambia solo la geometría:
  - página oficio y márgenes del perfil;
  - anchos de tabla escalados en proporción al nuevo ancho útil (las fuentes los escriben para 16,6 cm);
  - tabulación derecha del índice al nuevo ancho;
- el índice estático se recalcula sobre el PDF real, con el mismo bucle del constructor original;
- las figuras se regeneran con el mismo código en `lote_1_oficio/build/figs/` y se imprimen a su tamaño;
- la única diferencia de texto intencional es la línea de versión de la portada, que marca el documento como prueba.

No escribe nada dentro de `lote_1/`.
"""
import os, sys, json, importlib
sys.dont_write_bytecode = True   # no deja cachés dentro de lote_1/

AQUI = os.path.dirname(os.path.abspath(__file__))
OFI = os.path.dirname(AQUI)
ADS = os.path.dirname(OFI)
FUENTE = os.path.join(ADS, 'lote_1', 'build')
sys.path.insert(0, AQUI)
sys.path.insert(1, FUENTE)

import perfiles as PF
from docx.shared import Cm
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

clave = sys.argv[1] if len(sys.argv) > 1 else 'O1'
P = PF.PERFILES[clave]
ANCHO = PF.ancho_util(P)
F = ANCHO / PF.ANCHO_A4
SALIDA = os.path.join(OFI, clave)
os.makedirs(SALIDA, exist_ok=True)

import helpers as H
import maqueta as M
import comun as K
import diagramas
import construir as C
import guia
import cap3

assert os.path.dirname(H.__file__) == FUENTE and os.path.dirname(C.__file__) == FUENTE, 'se importó otra copia de las fuentes'

# ---------------------------------------------------------------- geometría
_new_doc = H.new_doc


def new_doc():
    doc = _new_doc()
    s = doc.sections[0]
    s.page_width, s.page_height = Cm(P['papel'][0]), Cm(P['papel'][1])
    s.left_margin, s.right_margin = Cm(P['interior']), Cm(P['exterior'])
    s.top_margin, s.bottom_margin = Cm(P['superior']), Cm(P['inferior'])
    s.header_distance = s.footer_distance = Cm(PF.ENCABEZADO_PIE)
    if P['espejo']:   # márgenes simétricos: en Word, «izquierdo» pasa a ser el interior
        st = doc.settings.element
        if st.find(qn('w:mirrorMargins')) is None:
            st.insert(0, OxmlElement('w:mirrorMargins'))
    return doc


H.new_doc = new_doc

_fijar = M.fijar_anchos


def fijar_anchos(t, anchos):
    _fijar(t, [round(a * F, 3) for a in anchos])


M.fijar_anchos = fijar_anchos

_rellenar = K.rellenar_indice
TAB_A4 = str(int(Cm(PF.ANCHO_A4).twips))


def rellenar_indice(doc, entradas, paginas):
    _rellenar(doc, entradas, paginas)
    for tab in doc.element.body.iter(qn('w:tab')):
        if tab.get(qn('w:pos')) == TAB_A4:
            tab.set(qn('w:pos'), str(int(Cm(ANCHO).twips)))


K.rellenar_indice = rellenar_indice

_finalizar = H.finalizar


def finalizar(doc, ruta):
    """Quita el párrafo vacío de separación que deja `maqueta.tabla` cuando lo sigue un título con salto de página
    o el final del documento: ahí no separa nada y, si la tabla termina justo al pie, pasa solo a la hoja
    siguiente y deja una hoja en blanco (se vio en la guía con los perfiles O2 y O3). No cambia ningún texto."""
    body = doc.element.body
    for p in list(body.iterchildren(qn('w:p'))):
        vacio = (not ''.join(t.text or '' for t in p.iter(qn('w:t'))).strip() and p.find('.//' + qn('w:drawing')) is None
                 and p.find('.//' + qn('w:br')) is None and p.find('.//' + qn('w:fldChar')) is None)
        sig = p.getnext()
        if vacio and sig is not None and (sig.tag == qn('w:sectPr') or sig.find('.//' + qn('w:pageBreakBefore')) is not None):
            body.remove(p)
    # Tablas que LibreOffice dejó con celdas sin imprimir en la vuelta anterior: su rótulo abre hoja nueva.
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


HOJA_NUEVA = set()   # rótulos de las tablas que deben empezar en hoja nueva


def tablas_con_perdida(ruta_docx, ruta_pdf, minimo=4):
    """Rótulos de las tablas con encabezado repetido a las que les faltan palabras en el PDF. Es la combinación
    «encabezado repetido» + «no dividir fila»: si la tabla empieza cerca del pie, LibreOffice imprime el encabezado
    y la primera fila y omite las demás (se vio en la Tabla 3.5 del PDF A4 original y en la guía con el perfil O2).
    Se cuenta el déficit de palabras del documento (DOCX menos PDF) que cae en las celdas de cada tabla; con menos de
    `minimo` palabras no se marca: son palabras partidas por el ancho de una celda angosta, no filas perdidas."""
    import re, collections, docx as _docx, pymupdf
    W = lambda t: re.findall(r'[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{2,}', t)
    pdf = collections.Counter()
    for pg in pymupdf.open(ruta_pdf):
        pdf.update(W(pg.get_text()))
    d = _docx.Document(ruta_docx)
    doc = collections.Counter()
    for p in d.element.body.iter(qn('w:p')):
        doc.update(W(''.join(x.text or '' for x in p.iter(qn('w:t')))))
    deficit = doc - pdf
    puntajes = []
    for t in d.tables:
        trp = t.rows[0]._tr.trPr
        if trp is None or trp.find(qn('w:tblHeader')) is None:
            continue
        tw = collections.Counter()
        for tc in t._tbl.iter(qn('w:tc')):
            tw.update(W(''.join(x.text or '' for x in tc.iter(qn('w:t')))))
        puntaje = sum(min(c, deficit[w]) for w, c in tw.items())
        if puntaje >= minimo:
            prev = t._tbl.getprevious()
            puntajes.append((puntaje, ''.join(x.text or '' for x in prev.iter(qn('w:t')))))
    # una sola tabla por vuelta, la de mayor déficit: las palabras que pierde una tabla también figuran en otras
    return [max(puntajes)[1]] if puntajes else []


H.finalizar = finalizar

K.VERSION = K.VERSION + ' · prueba en oficio %s, no definitiva' % clave
diagramas.AQUI = AQUI   # figuras regeneradas fuera de lote_1/
C.RUTA_EST = os.path.join(SALIDA, 'ADS_3BTI_LOTE1_ESTUDIANTE_OFICIO_%s.docx' % clave)
C.RUTA_GUIA = os.path.join(SALIDA, 'ADS_3BTI_LOTE1_GUIA_DOCENTE_OFICIO_%s.docx' % clave)

if __name__ == '__main__':
    riesgos = [(r[0], r[2], r[3]) for r in cap3.TABLA_34[1]]
    figs = diagramas.generar(riesgos)
    assert all(os.path.dirname(f).startswith(AQUI) for f in figs.values()), figs
    for vuelta in range(8):   # construir, detectar tablas con celdas no impresas, corregir y volver a construir
        claves, paginas, total = C.construir_estudiante(figs, SALIDA)
        guia.construir(C.RUTA_GUIA, claves, paginas, C.ESTADO)
        pdf_g = K.a_pdf(C.RUTA_GUIA, SALIDA)
        nuevas = set(tablas_con_perdida(C.RUTA_EST, C.RUTA_EST[:-5] + '.pdf')) | set(tablas_con_perdida(C.RUTA_GUIA, pdf_g))   # a lo sumo una por documento
        if not nuevas - HOJA_NUEVA:
            assert not nuevas, 'tablas que siguen perdiendo celdas: %s' % nuevas
            break
        HOJA_NUEVA.update(nuevas)
    else:
        raise AssertionError('no se pudo evitar la pérdida de celdas: %s' % HOJA_NUEVA)
    import pymupdf
    print('%s · %s · ancho útil %.2f cm · libro %d págs. · guía %d págs.' % (clave, P['nombre'], ANCHO, total, len(pymupdf.open(pdf_g))))
    print('tablas que empiezan en hoja nueva para no perder celdas:', sorted(HOJA_NUEVA))
    json.dump({'perfil': clave, 'ancho_util': ANCHO, 'factor_tablas': F, 'tablas_en_hoja_nueva': sorted(HOJA_NUEVA),
               'paginas_libro': paginas, 'claves': claves},
              open(os.path.join(SALIDA, 'resultado_construccion.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
