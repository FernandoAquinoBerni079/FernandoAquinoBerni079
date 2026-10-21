# -*- coding: utf-8 -*-
"""Controles de impresión del lote 5 y láminas de revisión visual → lote_5/CONTROLES_FINALES.json,
lote_5/revision_visual/*.png. Mismo programa que el del lote 4 (lote_4/build/controles_finales.py), con las figuras,
los fragmentos de código y las láminas de la Unidad V.

1. Filas de tablas (control de la candidata O3, sin cambios): cada fila de cada tabla de 2 o más columnas del DOCX se
   busca en orden en el PDF; se detallan las tablas repartidas entre páginas (todas sus filas y el encabezado repetido).
2. Párrafos no impresos y palabras partidas en celdas.
3. Figuras: cada figura impresa con su epígrafe en la misma página, y la cantidad de imágenes esperada.
4. Índice: cada entrada en la página que indica.
5. Márgenes espejados medidos en el PDF.
6. Cortes de tabla.
7. Bloques de código impresos enteros, dentro de los márgenes y sin repartirse entre páginas (libro y guía).
Uso: python3 lote_5/build/controles_finales.py   (sale con 1 si algo falla)"""
import os, re, sys, json, collections
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
L2 = os.path.dirname(AQUI)   # carpeta del lote 5
sys.path.insert(0, AQUI)
import construir as B   # pone en la ruta la maqueta, el perfil O3 y las piezas de los lotes 1 a 4
import oficio as O
CI = O.CI
import pymupdf
from PIL import Image

DOCS = {'libro': B.RUTA_EST[:-5], 'guia': B.RUTA_GUIA[:-5], 'cuaderno': B.RUTA_CUAD[:-5]}
RES = {}; FALLOS = []


def chk(clave, cond, detalle):
    RES.setdefault(clave, []).append({'resultado': 'correcto' if cond else 'FALLA', 'detalle': detalle})
    if not cond:
        FALLOS.append('%s: %s' % (clave, detalle))
    print(('CORRECTO ' if cond else 'FALLA    ') + '[%s] %s' % (clave, detalle))


TABLAS = {}
for doc, base in DOCS.items():
    filas = CI.filas_de_tablas(base + '.docx', base + '.pdf')
    TABLAS[doc] = filas
    malas = [f for f in filas if f['filas_impresas'] != f['filas_docx']]
    chk('1. Filas de tablas', not malas, '%s: %d tablas de 2 o más columnas, todas con todas sus filas impresas (%d filas)%s'
        % (doc, len(filas), sum(f['filas_docx'] for f in filas), '' if not malas else ' — incompletas: %s' % [(m['rotulo'][:40], m['filas_faltantes']) for m in malas]))
    for f in filas:
        if len(f['paginas']) > 1:
            chk('1. Tablas repartidas entre páginas', f['filas_impresas'] == f['filas_docx'] and f['encabezado_repetido'] >= len(f['paginas']) - 1,
                '%s: «%s», págs. %s: %d de %d filas, encabezado repetido %d vez/veces'
                % (doc, (f['rotulo'] or f['primera_celda'])[:70], f['paginas'], f['filas_impresas'], f['filas_docx'], f['encabezado_repetido']))
    no = CI.parrafos_no_impresos(base + '.docx', base + '.pdf')
    chk('2. Párrafos impresos', not no, '%s: ningún párrafo del DOCX falta en el PDF%s' % (doc, '' if not no else ' — faltan %s' % no[:3]))
    part = CI.palabras_partidas(base + '.docx', base + '.pdf')
    chk('2. Palabras enteras', not part, '%s: ninguna palabra de celda partida en el PDF%s' % (doc, '' if not part else ' — %s' % part))

def filas_por_pagina(dx, pdf):
    """Página de cada fila de datos de cada tabla, con el mismo emparejamiento DOCX-PDF que CI.filas_de_tablas."""
    pf = [(i + 1, [c or '' for c in r]) for i, pg in enumerate(pymupdf.open(pdf))
          for tb in sorted(pg.find_tables().tables, key=lambda x: x.bbox[1]) if tb.col_count >= 2 for r in tb.extract()]
    k = 0; out = []
    for rot, filas in CI._tablas_docx(dx):
        pags = []
        for fila in filas:
            j = k
            while j < len(pf) and not (len(pf[j][1]) == len(fila) and all(CI._igual(a, b) for a, b in zip(fila, pf[j][1]))):
                j += 1
            if j < len(pf):
                pags.append(pf[j][0]); k = j + 1
        out.append((rot or filas[0][0], pags[1:]))
    return out


for doc, base in DOCS.items():
    cortes = [(r[:50], dict(collections.Counter(p))) for r, p in filas_por_pagina(base + '.docx', base + '.pdf') if len(set(p)) > 1]
    solas = [c for c in cortes if min(c[1].values()) < 2]
    chk('6. Cortes de tabla', not solas, '%s: %d tablas repartidas, ninguna deja menos de dos filas de datos en una página%s'
        % (doc, len(cortes), '' if not solas else ' — %s' % solas))

pE = pymupdf.open(DOCS['libro'] + '.pdf')
epis = [(i + 1, m.group(0)) for i, pg in enumerate(pE) for m in re.finditer(r'Figura \d+\.\d —', pg.get_text())]
# imágenes realmente dibujadas en cada página (LibreOffice comparte los recursos entre páginas: get_images no sirve)
dib = {i + 1: [x['bbox'] for x in pg.get_image_info()] for i, pg in enumerate(pE)}
def figura_sobre_epigrafe(p, e):
    pg = pE[p - 1]; r = pg.search_for(e)
    return r and any(b[3] <= r[0].y0 + 2 and b[2] - b[0] > 150 for b in dib[p])
chk('3. Figuras', [e for _, e in epis] == ['Figura %s —' % n for n in ('14.1', '14.2', '16.1')]
    and all(figura_sobre_epigrafe(p, e) for p, e in epis),
    'las 3 figuras impresas, cada una con su imagen encima de su epígrafe, en la misma página: %s' % ', '.join('%s pág. %d' % (e[:11], p) for p, e in epis))
n_img = sum(len(v) for v in dib.values())
chk('3. Figuras', n_img == 3, 'imágenes dibujadas en el libro: %d (las 3 figuras)' % n_img)

# 7. bloques de código: cada línea impresa entera, en letra monoespaciada y dentro del ancho útil
import fragmentos_u5 as F
mono = [(i + 1, x) for i, pg in enumerate(pE) for b in pg.get_text('dict')['blocks'] for l in b.get('lines', []) for x in l['spans']
        if 'Mono' in x['font'] or 'Courier' in x['font']]
impresas = re.sub(r'[ \t]+', ' ', '\n'.join(pg.get_text() for pg in pE))
faltan = [l for f in F.FRAGMENTOS for l in F.extraer(f) if l.strip() and re.sub(r'\s+', ' ', l.strip()) not in impresas]
chk('7. Bloques de código', not faltan, '%d líneas de código de %d fragmentos, todas impresas enteras y sin caracteres perdidos%s'
    % (sum(1 for f in F.FRAGMENTOS for l in F.extraer(f) if l.strip()), len(F.FRAGMENTOS), '' if not faltan else ' — faltan %s' % faltan[:3]))
W0 = pE[0].rect.width
fuera = [(p, x['text'][:30]) for p, x in mono if x['bbox'][2] > W0 - 1.6 / 2.54 * 72 or x['bbox'][0] < 1.6 / 2.54 * 72]
chk('7. Bloques de código', mono and not fuera, '%d tramos en letra monoespaciada, todos dentro de los márgenes%s' % (len(mono), '' if not fuera else ' — %s' % fuera[:3]))
cortes_cod = []
norm = lambda t: re.sub(r'[ \t]+', ' ', t)
pG = pymupdf.open(DOCS['guia'] + '.pdf')
for f in F.TODOS:
    pdf_f = pE if f in F.FRAGMENTOS else pG
    pag = [i for i, pg in enumerate(pdf_f) if (f + ' —') in pg.get_text()]
    ls = [re.sub(r'\s+', ' ', l.strip()) for l in F.extraer(f) if l.strip()]
    if len(pag) != 1 or not all(l in norm(pdf_f[pag[0]].get_text()) for l in ls):
        cortes_cod.append((f, [p + 1 for p in pag]))
chk('7. Bloques de código', not cortes_cod, 'cada bloque de código (%d: 3 del libro y 4 de la guía) entero en la página de su rótulo y su ficha%s'
    % (len(F.TODOS), '' if not cortes_cod else ' — %s' % cortes_cod))

ind = pE[1].get_text()
entradas = [(m.group(1).strip(), int(m.group(2))) for m in re.finditer(r'^(.+?)\s*\.{3,}\s*(\d+)\s*$', ind, re.M)]
malas = [(t, n) for t, n in entradas if t[:30] not in re.sub(r'\s+', ' ', pE[n - 1].get_text())]
chk('4. Índice', entradas and not malas and len(entradas) == len(B.entradas_indice()),
    '%d entradas; cada una en la página que indica%s' % (len(entradas), '' if not malas else ' — no coinciden: %s' % malas[:5]))

W = pE[0].rect.width; med = []
for n in range(4, 12):
    bl = [b for b in pE[n - 1].get_text('blocks') if len(b[4]) > 80]
    if bl:
        med.append((n, round(min(b[0] for b in bl) / 72 * 2.54, 2), round((W - max(b[2] for b in bl)) / 72 * 2.54, 2)))
ok = med and all((iz >= 2.45 if n % 2 else de >= 2.3) and (de >= 1.6 if n % 2 else iz >= 1.75) for n, iz, de in med)
chk('5. Márgenes espejados', ok, 'impares con el interior (2,5 cm) a la izquierda y pares a la derecha: %s' % med)

# ---------------------------------------------------------------- láminas
RV = os.path.join(L2, 'revision_visual'); os.makedirs(RV, exist_ok=True)


def lamina(nombre, pags, pdf=pE, dpi=60):
    ims = []
    for n in pags:
        pix = pdf[n - 1].get_pixmap(dpi=dpi); ims.append(Image.frombytes('RGB', (pix.width, pix.height), pix.samples))
    filas = [ims[i:i + 4] for i in range(0, len(ims), 4)]
    w, h = ims[0].size
    c = Image.new('RGB', (min(4, len(ims)) * (w + 12) - 12, len(filas) * (h + 12) - 12), (130, 130, 130))
    for r, fila in enumerate(filas):
        for k, im in enumerate(fila):
            c.paste(im, (k * (w + 12), r * (h + 12)))
    c.save(os.path.join(RV, nombre)); return nombre


def pags_con(pdf, texto):
    return [i + 1 for i, pg in enumerate(pdf) if texto in pg.get_text()]


pC = pymupdf.open(DOCS['cuaderno'] + '.pdf')
import cap14, cap15, cap16
fig_p = lambda pref: sorted({p for p, e in epis if e.startswith(pref)})
cod_p = lambda *fs: sorted({i + 1 for i, pg in enumerate(pE) for f in fs if (f + ' —') in pg.get_text()})
lams = {
    'indice': lamina('01_indice_y_apertura.png', [2, 3], dpi=70),
    'verificar_validar': lamina('02_verificar_validar_y_limites.png', sorted(set(pags_con(pE, cap14.TABLA_141_ROTULO) + fig_p('Figura 14.1'))), dpi=65),
    'copia_dp': lamina('03_datos_DP_y_copia_descartable.png', sorted(set(pags_con(pE, cap14.TABLA_143_ROTULO) + pags_con(pE, cap14.TABLA_144_ROTULO))), dpi=65),
    'matriz': lamina('04_matriz_ejecutada_y_condiciones.png', sorted(set(pags_con(pE, cap14.TABLA_145_ROTULO) + pags_con(pE, 'C-20'))), dpi=65),
    'cobertura_reporte': lamina('05_cobertura_y_reporte_de_defecto.png', sorted(set(pags_con(pE, cap14.TABLA_147_ROTULO) + fig_p('Figura 14.2') + pags_con(pE, cap14.TABLA_148_ROTULO))), dpi=65),
    'integracion_permisos': lamina('06_integracion_permisos_y_restauracion.png', sorted(set(pags_con(pE, cap15.TABLA_151_ROTULO) + pags_con(pE, cap15.TABLA_152_ROTULO))), dpi=65),
    'sesiones_aceptacion': lamina('07_sesiones_de_uso_y_aceptacion.png', sorted(set(pags_con(pE, cap15.SESIONES_ROTULO) + pags_con(pE, cap15.TABLA_154_ROTULO))), dpi=65),
    'in02': lamina('08_IN02_diagnostico_correccion_y_regresion.png', sorted(set(fig_p('Figura 16.1') + cod_p('Código 16.1', 'Código 16.2') + pags_con(pE, cap16.TABLA_163_ROTULO))), dpi=70),
    'sc02': lamina('09_SC02_mejora_y_trazabilidad.png', sorted(set(pags_con(pE, cap16.TABLA_164_ROTULO) + cod_p('Código 16.3') + pags_con(pE, cap16.TABLA_166_ROTULO))), dpi=65),
    'h5': lamina('10_condiciones_minimas_y_H5.png', sorted(set(pags_con(pE, cap16.TABLA_167_ROTULO) + pags_con(pE, 'Criterios del H5'))), dpi=65),
    'practicas': lamina('11_practicas.png', [i + 1 for i, pg in enumerate(pE) if pg.get_text().startswith('Práctica ')], dpi=55),
    'evaluaciones': lamina('12_evaluaciones.png', [i + 1 for i, pg in enumerate(pE) if pg.get_text().startswith('Evaluación del Capítulo')], dpi=55),
    'guia_dp_dr': lamina('13_guia_cargador_DR_y_diferencias.png', sorted(set(pags_con(pG, 'Preparación de una copia con DP') + pags_con(pG, 'Plantilla de DR') + pags_con(pG, 'Archivos que cambian en las versiones v2'))), pdf=pG, dpi=65),
    'guia_rubrica': lamina('14_guia_rubrica_H5_recuperacion_y_banco.png', sorted(set(pags_con(pG, 'Rúbrica del H5: descriptores por nivel') + pags_con(pG, 'Planilla de recuperación') + pags_con(pG, 'Banco de variantes V5'))), pdf=pG, dpi=65),
    'guia_referencias': lamina('15_guia_referencias_R4_a_R7_y_resultados.png', sorted(set(pags_con(pG, 'Referencia R-4 —') + pags_con(pG, 'Referencia R-7 —') + pags_con(pG, 'Resultados de las pruebas (build/reproducir.py)'))), pdf=pG, dpi=65),
    'margenes': lamina('16_margenes_espejados_pags_6_7.png', [6, 7], dpi=60),
    'tablas_repartidas': lamina('17_tablas_repartidas.png', sorted({p for f in TABLAS['libro'] if len(f['paginas']) > 1 for p in f['paginas']}) or [4], dpi=55),
    'cuaderno': lamina('18_cuaderno_de_practicas.png', list(range(1, len(pC) + 1)), pdf=pC, dpi=45),
}
RES['laminas'] = lams
RES['tablas'] = TABLAS
json.dump({'fallos': FALLOS, 'controles': RES}, open(os.path.join(L2, 'CONTROLES_FINALES.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
n = sum(len(v) for k, v in RES.items() if k[0].isdigit())
print('\nResultado: %d controles, %d fallos' % (n, len(FALLOS)))
sys.exit(1 if FALLOS else 0)
