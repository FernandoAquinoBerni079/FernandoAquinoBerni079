"""Revisión visual binaria de FINAL OFICIO v3 (pendiente señalado en la reauditoría 04, B.8).

Uso: python3 -I revision_visual_v3.py
Mide cada página de los 5 PDF renderizados (pymupdf) y deja en build/revision_visual_v3/:
  - revision_visual_v3.md: papel, márgenes medidos y letra mínima por documento, con excepciones;
  - hojas de contacto JPG (12 páginas por hoja) de los 5 PDF;
  - páginas sueltas a mayor resolución: Planes 1, 26, 28 y 31 (9 pt) y Libro 33, 102, 110 y 116.
Márgenes: caja de todo lo impreso (texto, trazos e imágenes) fuera de encabezado y pie, que van
a 0,6 cm del borde por diseño. Portadas y contraportadas a página completa quedan excluidas.
"""
import os, re, glob, json
import pymupdf

R = '/home/claude/alg3/'; O = R + 'salida_FINAL_OFICIO_v3/'; D = R + 'build/revision_visual_v3/'
CM = 72 / 2.54; MARG = 1.27; FRANJA = 1.27 * CM      # encabezado/pie viven dentro de la franja del margen
os.makedirs(D, exist_ok=True)
DOCS = [('Libro', 'LIBRO'), ('Solucionario', 'SOLUCIONARIO'), ('Planes de Clase', 'PLANES_DE_CLASE'),
        ('Plan Anual', 'PLAN_ANUAL_'), ('Muestra', 'MUESTRA')]


def a_pagina_completa(p):
    return any(r.width > p.rect.width * 0.9 and r.height > p.rect.height * 0.9
               for im in p.get_images(full=True) for r in p.get_image_rects(im[0]))


def medir(p):
    """Márgenes del TEXTO (letra por letra, sin espacios) y de TRAZOS/FONDOS/IMÁGENES, por separado."""
    W, H = p.rect.width, p.rect.height
    txt, tams, otros = [], [], []
    for b in p.get_text('rawdict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                cs = [c for c in s['chars'] if c['c'].strip()]
                if not cs:
                    continue
                r = pymupdf.Rect(min(c['bbox'][0] for c in cs), min(c['bbox'][1] for c in cs),
                                 max(c['bbox'][2] for c in cs), max(c['bbox'][3] for c in cs))
                if r.y1 <= FRANJA or r.y0 >= H - FRANJA:      # encabezado o pie
                    continue
                txt.append(r); tams.append(round(s['size'], 1))
    for dr in p.get_drawings():
        r = dr['rect']
        if r.y1 > FRANJA and r.y0 < H - FRANJA and r.width > 0.5:
            otros.append(r)
    for im in p.get_images(full=True):
        otros += list(p.get_image_rects(im[0]))
    if not txt and not otros:
        return None
    def m(cajas):
        if not cajas:
            return dict(izq=99, der=99, sup=99, inf=99)
        return dict(izq=min(r.x0 for r in cajas) / CM, der=(W - max(r.x1 for r in cajas)) / CM,
                    sup=min(r.y0 for r in cajas) / CM, inf=(H - max(r.y1 for r in cajas)) / CM)
    return dict(texto=m(txt), trazos=m(otros), letra=min(tams) if tams else None, tams=tams)


def contacto(doc, nombre, por_hoja=12, cols=4):
    out = []
    for k in range(0, doc.page_count, por_hoja):
        n = min(por_hoja, doc.page_count - k); filas = (n + cols - 1) // cols
        tw, th = 300, 460
        hoja = pymupdf.open(); pg = hoja.new_page(width=cols * tw, height=filas * th)
        for j in range(n):
            q = doc[k + j]
            r = pymupdf.Rect((j % cols) * tw + 6, (j // cols) * th + 6, (j % cols + 1) * tw - 6, (j // cols + 1) * th - 18)
            # apaisadas: se respetan proporciones dentro de la celda
            pg.show_pdf_page(r, doc, k + j, keep_proportion=True)
            pg.insert_text(((j % cols) * tw + 8, (j // cols + 1) * th - 5), 'pág. %d' % (k + j + 1), fontsize=10)
            pg.draw_rect(r, color=(0.75, 0.75, 0.75), width=0.5)
        f = D + '%s_contacto_%02d-%02d.jpg' % (nombre, k + 1, k + n)
        pg.get_pixmap(dpi=100).save(f, jpg_quality=72); out.append(f)
    return out


def main():
    filas, excep, archivos = [], [], []
    for titulo, clave in DOCS:
        f = next(x for x in glob.glob(O + '*.pdf') if clave in os.path.basename(x))
        d = pymupdf.open(f); nombre = titulo.replace(' ', '_')
        papel = sorted({(round(p.rect.width / CM, 2), round(p.rect.height / CM, 2)) for p in d})
        ms = []; fuera_txt = []; fuera_tr = {}
        for i, p in enumerate(d):
            if a_pagina_completa(p):
                continue
            m = medir(p)
            if m is None:
                excep.append('%s pág. %d: sin contenido medible' % (titulo, i + 1)); continue
            m['pag'] = i + 1; ms.append(m)
            for lado in ('izq', 'der', 'sup', 'inf'):
                if m['texto'][lado] < MARG - 0.05:
                    fuera_txt.append('pág. %d %s %.2f cm' % (i + 1, lado, m['texto'][lado]))
                if m['trazos'][lado] < MARG - 0.05:
                    v = round(m['trazos'][lado], 2)
                    fuera_tr.setdefault((lado, v), []).append(i + 1)
        mn = lambda k, lado: min(x[k][lado] for x in ms)
        letras = sorted({t for x in ms for t in x['tams']})
        filas.append((titulo, d.page_count, ' / '.join('%.2f × %.2f' % x for x in papel),
                      '%.2f / %.2f / %.2f / %.2f' % tuple(mn('texto', l) for l in ('izq', 'der', 'sup', 'inf')),
                      '%.2f / %.2f' % (mn('trazos', 'izq'), mn('trazos', 'der')),
                      letras[0], d.page_count - len(ms)))
        excep.append('**%s** — texto fuera de 1,27 cm: %s' % (titulo, '; '.join(fuera_txt) if fuera_txt else 'ninguno'))
        for (lado, v), pags in sorted(fuera_tr.items()):
            excep.append('%s — filete o fondo a %.2f cm (%s) en %d págs.: %s' %
                         (titulo, v, 'izquierda' if lado == 'izq' else 'derecha' if lado == 'der' else lado, len(pags),
                          ', '.join(map(str, pags[:12])) + (' …' if len(pags) > 12 else '')))
        chicas = sorted({(x['pag'], t) for x in ms for t in x['tams'] if t < 8})
        for pg, t in chicas:
            excep.append('%s pág. %d: texto de %.1f pt (< 8 pt)' % (titulo, pg, t))
        archivos += contacto(d, nombre)
        if titulo == 'Planes de Clase':
            idx = json.load(open(R + 'build/indice_planes_v2.json'))
            for n in (1, 26, 28, 31):
                pg = idx['paginas'][n - 1]; out = D + 'Planes_plan%02d_pag%02d.jpg' % (n, pg)
                d[pg - 1].get_pixmap(dpi=110).save(out, jpg_quality=80); archivos.append(out)
                m = next(x for x in ms if x['pag'] == pg)
                excep.append('Planes — Plan %d (pág. %d, compactado): tamaños de letra %s pt; margen inferior libre %.2f cm; '
                             'firmas «Docente» y «Dirección — Visto bueno» en la hoja: %s' %
                             (n, pg, sorted(set(m['tams'])), m['texto']['inf'], 'sí' if 'Dirección — Visto bueno' in d[pg - 1].get_text() else 'NO'))
        if titulo == 'Libro':
            for n in (33, 102, 110, 116):
                out = D + 'Libro_pag%03d.jpg' % n
                d[n - 1].get_pixmap(dpi=100).save(out, jpg_quality=80); archivos.append(out)
    L = ['# Revisión visual binaria — Algorítmica 3.º FINAL OFICIO v3', '',
         'Medido con pymupdf sobre los 5 PDF de `salida_FINAL_OFICIO_v3/` (12/10/2026). **Texto:** cajas de cada letra, sin espacios, '
         'fuera de encabezado y pie (que van a 0,6 cm del borde por diseño). **Trazos:** filetes, fondos, bordes de tabla e imágenes. '
         'Las portadas y contraportadas a página completa no se miden. Objetivo: 1,27 cm (tolerancia 0,05 cm).', '',
         '| Documento | Págs. | Papel (cm) | Texto: izq. / der. / sup. / inf. mín. (cm) | Trazos: izq. / der. mín. (cm) | Letra mín. (pt) | Págs. a página completa |',
         '|---|---|---|---|---|---|---|']
    for t in filas:
        L.append('| %s | %d | %s | %s | %s | %.1f | %d |' % t)
    L += ['', '## Detalle', ''] + ['- ' + e for e in excep] + ['', '## Imágenes (en esta carpeta)', '']
    L += ['- `%s` (%d KB)' % (os.path.basename(a), os.path.getsize(a) // 1024) for a in archivos]
    open(D + 'revision_visual_v3.md', 'w').write('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
