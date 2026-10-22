# -*- coding: utf-8 -*-
"""Utilidades de edición diferencial de DOCX (R1 → R2): reemplazos controlados, celdas, imágenes, índices estáticos.

Toda función que modifica texto registra el cambio en REGISTRO y exige el número de apariciones esperado: si el texto
de origen no está o aparece más veces de lo previsto, la construcción se detiene (no se edita «a ciegas»).
"""
import copy, io, re, subprocess, os
import docx
from docx.oxml.ns import qn
from PIL import Image

REGISTRO = []


def parrafos(doc):
    """Todos los párrafos del cuerpo, incluidos los de tablas (anidadas)."""
    for p in doc.element.body.iter(qn('w:p')):
        yield docx.text.paragraph.Paragraph(p, doc._body)


def poner_texto(p, texto):
    """Reemplaza el texto del párrafo conservando el formato del primer run con texto."""
    runs = [r for r in p.runs if r.text]
    if not runs:
        p.add_run(texto); return
    runs[0].text = texto
    for r in runs[1:]:
        r._r.getparent().remove(r._r)


def reemplazar(doc, viejo, nuevo, veces=1, doc_nombre='', motivo=''):
    n = 0
    for p in parrafos(doc):
        if viejo in p.text:
            k = p.text.count(viejo)
            esperado = p.text.replace(viejo, nuevo)
            for r in p.runs:                      # si cabe en un run, se preserva el formato mixto del párrafo
                if viejo in r.text:
                    r.text = r.text.replace(viejo, nuevo)
            if p.text != esperado:                # el texto viejo estaba repartido entre runs
                poner_texto(p, esperado)
            n += k
    if n != veces:
        raise SystemExit('«%s»: %d apariciones, se esperaban %d (%s)' % (viejo[:70], n, veces, doc_nombre))
    REGISTRO.append({'documento': doc_nombre, 'antes': viejo, 'despues': nuevo, 'apariciones': n, 'motivo': motivo})


def celdas_unicas(fila):
    prev = None
    for c in fila.cells:
        if c._tc is prev:
            continue
        prev = c._tc
        yield c


def poner_celda(celda, lineas):
    """Escribe una lista de líneas en la celda: una por párrafo, copiando el formato del primer párrafo."""
    ps = celda.paragraphs
    modelo = copy.deepcopy(ps[0]._p)
    for p in ps[1:]:
        p._p.getparent().remove(p._p)
    poner_texto(ps[0], lineas[0])
    ancla = ps[0]._p
    for t in lineas[1:]:
        nuevo = copy.deepcopy(modelo)
        ancla.addnext(nuevo); ancla = nuevo
        poner_texto(docx.text.paragraph.Paragraph(nuevo, celda), t)


def reemplazar_imagen(doc, indice, ruta_png, ancho_cm=None):
    """Sustituye la imagen n.º `indice` (1 = primera del cuerpo) y ajusta el alto a la proporción nueva."""
    dibujos = list(doc.element.body.iter(qn('w:drawing')))
    dr = dibujos[indice - 1]
    blip = dr.find('.//' + qn('a:blip'))
    parte = doc.part.related_parts[blip.get(qn('r:embed'))]
    datos = open(ruta_png, 'rb').read()
    parte._blob = datos
    w, h = Image.open(io.BytesIO(datos)).size
    ext = dr.find('.//' + qn('wp:extent'))
    cx = int(ancho_cm * 360000) if ancho_cm else int(ext.get('cx'))
    cy = int(cx * h / w)
    ext.set('cx', str(cx)); ext.set('cy', str(cy))
    for e in dr.iter(qn('a:ext')):
        if e.get('cx'):
            e.set('cx', str(cx)); e.set('cy', str(cy))
    return cx / 360000, cy / 360000


def a_pdf(ruta_docx, carpeta):
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', carpeta, ruta_docx],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return os.path.join(carpeta, os.path.basename(ruta_docx)[:-5] + '.pdf')


def recalcular_indice(doc, ruta_pdf, patron_entrada=r'^((?:Clase|Evaluación|Práctica|Plan de Clase|Unidad|Anexo|Recursos)\b.*?)\s+·\s+(\d+)$', clave=None, primera=2):
    """Actualiza los números de página de las entradas «Título  ·  N» buscando el título en el PDF renderizado.

    `clave(titulo)` devuelve el texto a buscar (por omisión, el título completo, sin «…» final). Se busca la primera
    página ≥ `primera` (para no confundir con la página del índice) cuyo texto contenga la clave al inicio de una línea.
    Devuelve la lista de (entrada, página anterior, página nueva)."""
    import pymupdf
    pags = [pg.get_text() for pg in pymupdf.open(ruta_pdf)]
    # se empieza a buscar después de la última página de índice (páginas con 3 o más líneas «… · N»)
    idx = [i for i, t in enumerate(pags) if sum(bool(re.search(r'·\s+\d+\s*$', l)) for l in t.split('\n')) >= 3]
    if idx:
        primera = max(primera, idx[-1] + 2)
    cambios = []
    for p in parrafos(doc):
        m = re.match(patron_entrada, p.text)
        if not m:
            continue
        tit, num = m.group(1).strip(), int(m.group(2))
        buscar = clave(tit) if clave else tit.rstrip('…').strip()
        hallada = None
        for i in range(primera - 1, len(pags)):
            lineas = [l.strip() for l in pags[i].split('\n')]
            texto = ' '.join(lineas)
            if any(l.startswith(buscar[:40]) for l in lineas) or (len(buscar) > 40 and buscar[:60] in texto):
                hallada = i + 1
                break
        if hallada is None:
            raise SystemExit('Índice: no se encontró «%s» en %s' % (buscar, ruta_pdf))
        if hallada != num:
            poner_texto(p, re.sub(r'\d+$', str(hallada), p.text))
        cambios.append((tit, num, hallada))
    return cambios


def renglones_respuesta(doc, cantidad_por_seccion, patron=r'^4\.\d ', ancho=92, alto_pt=20, color='78909C'):
    """Agrega renglones de respuesta después de cada pregunta abierta (párrafos que empiezan con «4.n »).

    `cantidad_por_seccion(seccion)` devuelve cuántos renglones van según la sección en curso: 'clase',
    'unidad' (evaluación de unidad) o 'etapa'. La sección se detecta recorriendo el cuerpo en orden."""
    from docx.shared import Pt, RGBColor
    from docx.enum.text import WD_LINE_SPACING
    seccion, total = 'clase', 0
    for el in list(doc.element.body.iterchildren()):
        texto = ''.join(x.text or '' for x in el.iter(qn('w:t')))
        if el.tag == qn('w:tbl'):
            if texto.startswith('Evaluación de la Unidad'):
                seccion = 'unidad'
            elif texto.startswith('Evaluación de la Etapa'):
                seccion = 'etapa'
            continue
        if el.tag != qn('w:p'):
            continue
        p = docx.text.paragraph.Paragraph(el, doc._body)
        if p.style.name.startswith('Heading 2') or p.style.name.startswith('Heading 1'):
            seccion = 'clase'
        if re.match(patron, p.text):
            ancla = el
            for _ in range(cantidad_por_seccion(seccion)):
                nuevo = doc.add_paragraph()._p          # se crea al final y se mueve debajo de la pregunta
                ancla.addnext(nuevo); ancla = nuevo
                q = docx.text.paragraph.Paragraph(nuevo, doc._body)
                q.style = doc.styles['Normal']
                pf = q.paragraph_format
                pf.space_before = Pt(0); pf.space_after = Pt(0)
                pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY; pf.line_spacing = Pt(alto_pt)
                r = q.add_run('_' * ancho); r.font.size = Pt(10); r.font.color.rgb = RGBColor.from_string(color)
                total += 1
            # la pregunta y sus renglones no se separan entre páginas (el último renglón queda libre)
            p.paragraph_format.keep_with_next = True
            bloque = []
            e = el.getnext()
            while e is not None and e is not ancla.getnext():
                bloque.append(e); e = e.getnext()
            for b in bloque[:-1]:
                docx.text.paragraph.Paragraph(b, doc._body).paragraph_format.keep_with_next = True
    return total


def saltos_a_salto_antes(doc):
    """Convierte los párrafos que solo contienen un salto de página manual en párrafos vacíos con «salto de página
    anterior». Así, si el contenido previo termina justo al pie, no queda una página en blanco."""
    from docx.shared import Pt
    n = 0
    for p in list(doc.paragraphs):
        brs = p._p.findall('.//' + qn('w:br'))
        if brs and all(b.get(qn('w:type')) == 'page' for b in brs) and not p.text.strip():
            for b in brs:
                b.getparent().remove(b)
            pf = p.paragraph_format
            pf.page_break_before = True; pf.space_before = Pt(0); pf.space_after = Pt(0)
            pf.line_spacing = Pt(1)
            n += 1
    return n


def escalar_letra(doc, mapa):
    """Cambia el cuerpo de los runs según `mapa` {pt viejo: pt nuevo} (runs con tamaño explícito y estilos)."""
    from docx.shared import Pt
    n = 0
    for el in doc.element.body.iter(qn('w:r')):
        r = docx.text.run.Run(el, doc._body)
        if r.font.size is not None and r.font.size.pt in mapa:
            r.font.size = Pt(mapa[r.font.size.pt]); n += 1
    for st in doc.styles:
        try:
            if st.font.size is not None and st.font.size.pt in mapa:
                st.font.size = Pt(mapa[st.font.size.pt])
        except AttributeError:
            pass
    return n
