# -*- coding: utf-8 -*-
"""Control nuevo: todo el texto del DOCX tiene que aparecer impreso en su PDF (por párrafo y por palabras).
Detecta contenido que el renderizado pierde (filas de tabla, recuadros recortados). Se aplica al A4 original y
a las pruebas en oficio. Uso: python3 lote_1_oficio/build/docx_vs_pdf.py  → lote_1_oficio/DOCX_VS_PDF.json"""
import os, re, sys, json, collections
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__)); OFI = os.path.dirname(AQUI); ADS = os.path.dirname(OFI)
import docx, pymupdf
from docx.oxml.ns import qn
W = lambda t: re.findall(r'[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{2,}', t)


def docx_pal(ruta):
    d = docx.Document(ruta); c = collections.Counter()
    for p in d.element.body.iter(qn('w:p')):
        if p.getparent() is not None and p.getparent().tag in (qn('w:sdtContent'),):
            continue
        c.update(W(''.join(t.text or '' for t in p.iter(qn('w:t')))))
    return c


def pdf_pal(ruta):
    c = collections.Counter()
    for pg in pymupdf.open(ruta):
        c.update(W(re.sub(r'-\n', '', pg.get_text())))
    return c


casos = [('A4', os.path.join(ADS, 'lote_1', 'ADS_3BTI_LOTE1_ESTUDIANTE')), ('A4', os.path.join(ADS, 'lote_1', 'ADS_3BTI_LOTE1_GUIA_DOCENTE'))]
for p in ('O1', 'O2', 'O3'):
    for n in ('ESTUDIANTE', 'GUIA_DOCENTE'):
        casos.append((p, os.path.join(OFI, p, 'ADS_3BTI_LOTE1_%s_OFICIO_%s' % (n, p))))
def parrafos_no_impresos(dx, pdf):
    """Párrafos del DOCX (de 12 caracteres o más) que no están en el PDF: se buscan en trozos de 12 caracteres sin
    espacios, lo que tolera cortes de renglón y celdas que se extraen intercaladas; falta si falta más de la mitad."""
    P = re.sub(r'\s+', '', ' '.join(p.get_text() for p in pymupdf.open(pdf)))
    malas = []
    for el in docx.Document(dx).element.body.iter(qn('w:p')):
        txt = ''.join(t.text or '' for t in el.iter(qn('w:t'))); s = re.sub(r'\s+', '', txt)
        if len(s) >= 12:
            trozos = [s[i:i + 12] for i in range(0, len(s) - 11, 12)]
            if sum(x not in P for x in trozos) > len(trozos) * 0.5:
                malas.append(txt[:120])
    return malas


res = {}; fallos = 0
for perfil, base in casos:
    no_imp = parrafos_no_impresos(base + '.docx', base + '.pdf')
    falta = docx_pal(base + '.docx') - pdf_pal(base + '.pdf')
    # una palabra partida por el ancho de celda («Fragmen-to») no es una pérdida: se descuenta si sus partes están
    falta = {k: v for k, v in falta.items() if v > 0}
    res[os.path.basename(base) + ' (' + perfil + ')'] = {'parrafos_no_impresos': no_imp,
        'palabras_del_docx_que_no_aparecen_en_el_pdf': sum(falta.values()), 'detalle_palabras': dict(sorted(falta.items(), key=lambda x: -x[1])[:40])}
    if no_imp and perfil != 'A4':
        fallos += 1
    print('%-45s párrafos no impresos %2d | palabras %3d %s' % (os.path.basename(base), len(no_imp), sum(falta.values()), dict(list(falta.items())[:6])))
json.dump(res, open(os.path.join(OFI, 'DOCX_VS_PDF.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('Pruebas en oficio con párrafos no impresos:', fallos)
sys.exit(1 if fallos else 0)
