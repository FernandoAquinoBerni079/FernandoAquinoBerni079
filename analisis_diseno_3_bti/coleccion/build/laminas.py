# -*- coding: utf-8 -*-
"""Láminas de revisión visual de los documentos anuales → coleccion/revision_visual/*.png: una por unidad del libro
(apertura y primeras páginas de cada capítulo), una por cada tipo de pieza (índice, figuras, código, hitos,
prácticas, evaluaciones, tablas repartidas, márgenes) y las de la guía y el cuaderno. Las páginas se eligen leyendo
el PDF, no a mano. Uso: python3 -B coleccion/build/laminas.py"""
import os, re, sys, json
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
COL = os.path.dirname(AQUI)
import pymupdf
from PIL import Image

RV = os.path.join(COL, 'revision_visual')
os.makedirs(RV, exist_ok=True)
P = {k: pymupdf.open(os.path.join(COL, n)) for k, n in (('libro', 'ADS_3BTI_LIBRO_ANUAL_ESTUDIANTE_OFICIO_O3.pdf'),
                                                         ('guia', 'ADS_3BTI_GUIA_DOCENTE_ANUAL_OFICIO_O3.pdf'),
                                                         ('cuaderno', 'ADS_3BTI_CUADERNO_ANUAL_PRACTICAS_OFICIO_O3.pdf'))}
HECHAS = {}


def lamina(nombre, pdf, pags, dpi=48, por_fila=5):
    pags = sorted(set(p for p in pags if 1 <= p <= len(pdf)))[:15]
    ims = []
    for n in pags:
        px = pdf[n - 1].get_pixmap(dpi=dpi)
        ims.append(Image.frombytes('RGB', (px.width, px.height), px.samples))
    w, h = ims[0].size
    filas = [ims[i:i + por_fila] for i in range(0, len(ims), por_fila)]
    c = Image.new('RGB', (min(por_fila, len(ims)) * (w + 10) - 10, len(filas) * (h + 10) - 10), (130, 130, 130))
    for r, fila in enumerate(filas):
        for k, im in enumerate(fila):
            c.paste(im, (k * (w + 10), r * (h + 10)))
    c.save(os.path.join(RV, nombre))
    HECHAS[nombre] = pags


def con(pdf, patron, inicio=True):
    rx = re.compile(patron, re.M)
    return [i + 1 for i, pg in enumerate(pdf) if i > 4 and rx.search(pg.get_text())]


L, G, C = P['libro'], P['guia'], P['cuaderno']
lamina('00_portadas_e_indices.png', L, [1, 2, 3, 4, 5])
primera = lambda pg: next((l.strip() for l in pg.get_text().split('\n') if l.strip()), '')
unidades = [i + 1 for i, pg in enumerate(L) if i > 4 and re.match(r'Unidad (I|II|III|IV|V|VI) — ', primera(pg))]
assert len(unidades) == 6, unidades
capitulos = {int(m.group(1)): i + 1 for i, pg in enumerate(L) if i > 4 for m in [re.search(r'^Capítulo (\d+) — ', pg.get_text(), re.M)] if m}
rangos = {'I': (1, 3), 'II': (4, 6), 'III': (7, 9), 'IV': (10, 13), 'V': (14, 16), 'VI': (17, 18)}
for k, (u, (a, b)) in enumerate(rangos.items()):
    pags = [unidades[k]] + [p for c in range(a, b + 1) for p in (capitulos[c], capitulos[c] + 1)]
    lamina('%02d_unidad_%s.png' % (k + 1, u), L, pags)
figs = con(L, r'^Figura \d+\.\d+ —')
lamina('07_figuras_1.png', L, figs[:15]); lamina('08_figuras_2.png', L, figs[15:30])
lamina('09_bloques_de_codigo.png', L, con(L, r'^Código \d+\.\d+ —'))
lamina('10_hitos_H1_a_H6.png', L, con(L, r'^(Revisión de la Unidad \w+ — )?Hito H\d|^Criterios del H\d'))
lamina('11_practicas.png', L, [p for p in con(L, r'^Práctica \d+ — ')])
lamina('12_evaluaciones.png', L, con(L, r'^Evaluación del Capítulo \d+$'))
ctr = json.load(open(os.path.join(COL, 'CONTROLES_IMPRESION.json'), encoding='utf8'))['controles']['tablas']
lamina('13_tablas_repartidas_libro.png', L, [p for f in ctr['libro'] for p in f['paginas']])
lamina('14_margenes_espejados.png', L, [20, 21, 120, 121], dpi=60, por_fila=4)
lamina('15_guia_parte_general_e_indice.png', G, [1, 2, 3, 4, 5, 6])
partes = con(G, r'^Parte (I|II|III|IV|V|VI) — ')
lamina('16_guia_inicio_de_cada_parte.png', G, partes + [p + 1 for p in partes])
lamina('17_guia_rubricas_y_claves.png', G, con(G, r'^Rúbrica del H\d: descriptores') + con(G, r'^Clave de la evaluación del capítulo (1|7|13|17)$'))
lamina('18_guia_referencias_de_codigo.png', G, con(G, r'^Referencia R-\d+ —'))
lamina('19_guia_tablas_repartidas.png', G, [p for f in ctr['guia'] for p in f['paginas']])
lamina('20_cuaderno_1.png', C, list(range(1, 16)))
lamina('21_cuaderno_2.png', C, list(range(16, len(C) + 1)))
json.dump(HECHAS, open(os.path.join(RV, 'paginas_de_cada_lamina.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('%d láminas en %s' % (len(HECHAS), os.path.relpath(RV, COL)))
for k, v in HECHAS.items():
    print(' ', k, v)
