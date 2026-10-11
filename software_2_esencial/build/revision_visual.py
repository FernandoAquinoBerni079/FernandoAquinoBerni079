# -*- coding: utf-8 -*-
"""Revisión visual (hallazgo N13): renderiza cada página de los cinco PDF, arma hojas de contacto
y una matriz página → observación (tamaño, orientación, ocupación, imágenes, tablas, vacías)."""
import pymupdf, os, re
from PIL import Image, ImageDraw, ImageFont
O = '/home/claude/sw2/salida/'; R = '/home/claude/sw2/build/revision_visual/'
N = 'Gabinete_Informatica_Software_2do_Curso_'
PDF = [('Libro', 'LIBRO_ESENCIAL_COMERCIAL_2026', 'V'), ('Solucionario', 'SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026', 'V'),
       ('Plan Anual', 'PLAN_ANUAL_COMERCIAL_2026', 'H'), ('Planes de Clase', 'PLANES_DE_CLASE_COMERCIAL_2026', 'V'), ('Muestra', 'MUESTRA_COMERCIAL_2026', 'V')]
cm = lambda pt: round(pt / 72 * 2.54, 1)
fuente = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)
filas = []; resumen = []
for f in os.listdir(R):
    if f.endswith(('.png', '.jpg')): os.remove(R + f)
for nombre, arch, ori in PDF:
    d = pymupdf.open(O + N + arch + '.pdf'); miniaturas = []; obs_pdf = 0
    for i, pg in enumerate(d):
        w, h = cm(pg.rect.width), cm(pg.rect.height)
        es_pa = nombre == 'Muestra' and 'PLAN ANUAL' in pg.get_text().upper() and w > h
        tam_ok = (w, h) == ((21.6, 33.0) if ori == 'V' else (33.0, 21.6)) or (i == 0 and (w, h) in ((21.6, 33.0), (33.0, 21.6))) or (es_pa and (w, h) == (33.0, 21.6))
        bl = [b for b in pg.get_text('blocks') if b[4].strip() and not b[4].strip().startswith('Página')]
        imgs = [r for im in pg.get_images(full=True) for r in pg.get_image_rects(im[0])]
        dib = [x['rect'] for x in pg.get_drawings() if x['rect'].height > 2]
        ys = [b[3] for b in bl] + [r.y1 for r in imgs]
        ocup = max(ys) / pg.rect.height if ys else 0.0
        palabras = len(pg.get_text().split())
        tablas = len(pg.find_tables().tables)
        obs = []
        if not tam_ok: obs.append('TAMAÑO %sx%s' % (w, h))
        if not bl and not imgs: obs.append('PÁGINA VACÍA')
        elif ocup < 0.20 and 0 < i < len(d) - 1: obs.append('CASI VACÍA')
        recortes = [b for b in bl if b[2] > pg.rect.width - 0.5 * 72 / 2.54 or b[0] < 0.5 * 72 / 2.54]
        if recortes: obs.append('TEXTO FUERA DE MARGEN')
        obs_pdf += bool(obs)
        if es_pa and not obs: obs.append('Página del Plan Anual: horizontal, correcto')
        filas.append((nombre, i + 1, '%s × %s' % (w, h), 'horizontal' if w > h else 'vertical', '%d %%' % round(ocup * 100), palabras, len(imgs), tablas, '; '.join(obs) or 'Sin observación'))
        pix = pg.get_pixmap(dpi=50); im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
        dr = ImageDraw.Draw(im); dr.rectangle([0, 0, 52, 28], fill='white'); dr.text((4, 2), str(i + 1), fill='red', font=fuente)
        miniaturas.append(im)
    # hojas de contacto de 24 páginas
    por = 24; cols = 6 if ori == 'V' else 4
    for k in range(0, len(miniaturas), por):
        grupo = miniaturas[k:k + por]; mw = max(m.width for m in grupo); mh = max(m.height for m in grupo)
        filas_n = (len(grupo) + cols - 1) // cols
        hoja = Image.new('RGB', (cols * (mw + 8) + 8, filas_n * (mh + 8) + 8), (90, 90, 90))
        for j, m in enumerate(grupo):
            hoja.paste(m, (8 + (j % cols) * (mw + 8), 8 + (j // cols) * (mh + 8)))
        hoja.save(R + '%s_p%03d-%03d.jpg' % (re.sub(r'\W', '_', nombre), k + 1, k + len(grupo)), quality=82)
    resumen.append((nombre, len(d), obs_pdf))
L = ['# Revisión visual de los cinco PDF (matriz página → observación)', '',
     'Generada por `build/revision_visual.py` sobre los PDF de `salida/`. Las hojas de contacto (`build/revision_visual/*.jpg`) muestran cada página en miniatura con su número en rojo, para la revisión a ojo del auditor.', '',
     'Criterios: tamaño oficio 21,6 × 33,0 cm (vertical; el Plan Anual en horizontal, salvo su portada); página vacía = sin texto ni imagen; casi vacía = el contenido termina antes del 20 % de la altura (se exceptúan la portada y la contraportada); texto fuera de margen = un bloque a menos de 0,5 cm del borde.', '',
     '| PDF | Páginas | Páginas con observación |', '|---|---|---|'] + ['| %s | %d | %d |' % r for r in resumen] + ['',
     '| PDF | Pág. | Tamaño (cm) | Orientación | Ocupación | Palabras | Imágenes | Tablas | Observación |', '|---|---|---|---|---|---|---|---|---|']
L += ['| %s | %d | %s | %s | %s | %d | %d | %d | %s |' % f for f in filas]
open('/home/claude/sw2/build/revision_visual.md', 'w').write('\n'.join(L) + '\n')
print(resumen); print([f for f in filas if not f[-1].startswith(('Sin', 'Página del'))])
