# -*- coding: utf-8 -*-
"""Compara la prueba en oficio con el lote 1 original en A4 y deja el resultado en lote_1_oficio/COMPARACION.json.

Controles:
- texto idéntico del DOCX (párrafos y celdas, en orden), salvo los números de página del índice y la línea de versión;
- palabras idénticas en el PDF (multiconjunto), salvo las mismas excepciones y los pies «Página N de M»;
- figuras regeneradas: mismo tamaño en píxeles que las originales (el PNG puede diferir en bytes por metadatos);
- medidas de lectura: caracteres por renglón de texto corrido (mediana), páginas y páginas con menos de la mitad ocupada.
Uso: python3 lote_1_oficio/build/comparar.py"""
import os, re, sys, json, glob, collections, statistics, hashlib
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__)); OFI = os.path.dirname(AQUI); ADS = os.path.dirname(OFI)
L1 = os.path.join(ADS, 'lote_1')
import docx, pymupdf
from PIL import Image
from docx.oxml.ns import qn

VERSION = re.compile(r'^Versión v1\.0 \(lote 1, para auditoría\)( · prueba en oficio O\d, no definitiva)?$')
INDICE = re.compile(r'^(.*?)\t(\d+|—)$')


def texto_docx(ruta):
    d = docx.Document(ruta); out = []
    for el in d.element.body:
        if el.tag == qn('w:p'):
            out.append(''.join(t.text or '' for t in el.iter(qn('w:t'))) + ('\t' if el.find('.//' + qn('w:tab')) is not None else ''))
        elif el.tag == qn('w:tbl'):
            for tc in el.iter(qn('w:tc')):
                out.append(''.join(t.text or '' for t in tc.iter(qn('w:t'))))
    norm = []
    for x in out:
        if VERSION.match(x.strip()):
            x = '«línea de versión»'
        norm.append(x)
    return norm


def texto_docx_sin_indice(ruta):
    d = docx.Document(ruta); out = []
    for p in d.element.body.iter(qn('w:p')):
        tabs = p.findall('.//' + qn('w:tab'))
        runs = []
        for r in p.iter(qn('w:r')):
            for c in r:
                if c.tag == qn('w:t'): runs.append(c.text or '')
                elif c.tag == qn('w:tab'): runs.append('\t')
        s = ''.join(runs)
        m = INDICE.match(s)
        if m: s = m.group(1) + '\t«pág.»'
        if VERSION.match(s.strip()): s = '«línea de versión»'
        out.append(s)
    return out


def palabras_pdf(ruta):
    c = collections.Counter()
    for pg in pymupdf.open(ruta):
        t = re.sub(r'(Página|Guía docente — Lote 1 ·)?\s*Página \d+ de \d+', ' ', pg.get_text())
        t = re.sub(r'prueba en oficio O\d, no definitiva', ' ', t)
        c.update(re.findall(r'[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+', t))   # sin números: el índice y los pies cambian
    return c


def lectura(ruta):
    d = pymupdf.open(ruta); H = d[0].rect.height
    largos, bajas = [], []
    for i, pg in enumerate(d):
        ys = [b[3] for b in pg.get_text('blocks') if not re.match(r'\s*.*Página \d+ de \d+\s*$', b[4])]
        if ys and max(ys) / H < 0.5: bajas.append(i + 1)
        for b in pg.get_text('dict')['blocks']:
            for l in b.get('lines', []):
                s = ''.join(sp['text'] for sp in l['spans'])
                tam = max((sp['size'] for sp in l['spans']), default=0)
                if 10 <= tam <= 11 and len(s) > 40:   # renglones de texto corrido a 10,5 pt
                    largos.append(len(s))
    return len(d), int(statistics.median(largos)), max(largos), bajas


res = {}
orig = {'libro': os.path.join(L1, 'ADS_3BTI_LOTE1_ESTUDIANTE'), 'guia': os.path.join(L1, 'ADS_3BTI_LOTE1_GUIA_DOCENTE')}
for doc, base in orig.items():
    n, med, mx, bajas = lectura(base + '.pdf')
    res.setdefault('A4', {})[doc] = {'paginas': n, 'caracteres_por_renglon_mediana': med, 'maximo': mx, 'paginas_menos_de_media': bajas}
figs_o = {os.path.basename(f): Image.open(f).size for f in glob.glob(os.path.join(L1, 'build', 'figs', '*.png'))}
fallos = 0
for perfil in ('O1', 'O2', 'O3'):
    R = res.setdefault(perfil, {})
    for doc, base in orig.items():
        nom = 'ESTUDIANTE' if doc == 'libro' else 'GUIA_DOCENTE'
        nuevo = os.path.join(OFI, perfil, 'ADS_3BTI_LOTE1_%s_OFICIO_%s' % (nom, perfil))
        a, b = texto_docx_sin_indice(base + '.docx'), texto_docx_sin_indice(nuevo + '.docx')
        a_v = [x for x in a if x.strip()]; b_v = [x for x in b if x.strip()]
        igual = a_v == b_v
        pa, pb = palabras_pdf(base + '.pdf'), palabras_pdf(nuevo + '.pdf')
        n, med, mx, bajas = lectura(nuevo + '.pdf')
        R[doc] = {'texto_docx_identico': igual, 'parrafos_con_texto': len(b_v),
                  'pdf_palabras_faltan': dict(pa - pb), 'pdf_palabras_sobran': dict(pb - pa),
                  'paginas': n, 'caracteres_por_renglon_mediana': med, 'maximo': mx, 'paginas_menos_de_media': bajas}
        if not igual:
            fallos += 1
            for k, (x, y) in enumerate(zip(a_v, b_v)):
                if x != y:
                    R[doc]['primera_diferencia'] = [k, x[:120], y[:120]]; break
    figs_n = {os.path.basename(f): Image.open(f).size for f in glob.glob(os.path.join(AQUI, 'figs', '*.png'))}
    R['figuras_mismo_tamano'] = figs_n == figs_o
    if figs_n != figs_o: fallos += 1
json.dump(res, open(os.path.join(OFI, 'COMPARACION.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
for k, v in res.items():
    print(k, json.dumps(v, ensure_ascii=False)[:700])
print('Fallos de identidad:', fallos)
sys.exit(1 if fallos else 0)
