# -*- coding: utf-8 -*-
"""Libro del estudiante — Desarrollo Personal y Social 7.º, oficio 21,6 × 33 cm, márgenes 1,27 cm.
Fuentes: fuente/tomo/*.md (marcado de GUIA_REDACCION.md) · arquitectura: curriculo.py.
Uso: python3 build_libro.py  → salida/…_LIBRO_DEL_ESTUDIANTE_2026.docx y .pdf"""
import os, re, json, subprocess, sys
import maqueta as M
import render as R
import curriculo as C

B = os.path.dirname(os.path.abspath(__file__)) + '/'
F = B + '../fuente/tomo/'
OUT = B + '../salida/'
NOMBRE = 'Desarrollo_Personal_y_Social_7mo_Grado_LIBRO_DEL_ESTUDIANTE_2026'
PARCIAL = '--parcial' in sys.argv  # permite construir aunque falten encuentros (solo para pruebas)


def secciones(ruta):
    """front.md → {clave: [líneas]}"""
    out, k = {}, None
    for l in R.leer(ruta):
        if l.startswith('@@'):
            k = l[2:].strip(); out[k] = []
        elif k:
            out[k].append(l)
    return out


FRONT = secciones(F + 'front.md')


def fuente(n):
    p = F + 'e%02d.md' % n
    if not os.path.exists(p):
        if PARCIAL:
            return None
        raise FileNotFoundError(p)
    return R.leer(p)


def titulo_enc(e):
    n, t, k, u, caps, tit, _ = e
    return C.rotulo(e)


def entradas():
    E = [(1, 'Prueba diagnóstica — ¿Qué sabés ya?')]
    for e in C.ENCUENTROS:
        n, t, k, u, caps, tit, _ = e
        if PARCIAL and fuente(n) is None:
            continue
        if t == 'C' and not any(x[1] == 'UNIDAD %d — %s' % (u, C.UNIDADES[u]) for x in E):
            E.append((1, 'UNIDAD %d — %s' % (u, C.UNIDADES[u])))
        E.append((1 if t in 'PI' else 2, titulo_enc(e)))
    if os.path.exists(F + 'anexo_pec.md'):
        E.append((1, 'Anexo — Proyecto Educativo Comunitario'))
        E += [(2, l[3:].strip()) for l in R.leer(F + 'anexo_pec.md') if l.startswith('## ')]
    if os.path.exists(F + 'glosario.md'):
        E.append((1, 'Glosario'))
    E.append((1, 'Créditos y datos de la edición'))
    return E


NOTAS = {}  # título → renglones de «Espacio para anotaciones» (regla N-02)


def notas(d, titulo):
    n = NOTAS.get(titulo, 0)
    if n > 2:
        M.par(d, 'Espacio para anotaciones y respuestas', 10, True, color=M.DARK, keep=True, antes=8, despues=2)
        M.renglones(d, n)


def apertura_unidad(d, u):
    M.heading(d, 'UNIDAD %d — %s' % (u, C.UNIDADES[u]), 1, salto=True)
    for l in FRONT['U%d' % u]:
        if l.strip():
            M.par(d, l.strip(), 11, despues=6)
    filas = [('Capacidades de la unidad (programa MEC)', ['• ' + C.CAP[k] for k in C.UNIDAD_CAPS[u]]), ('Período aproximado', [C.PERIODO[u]])]
    M.ficha_filas(d, filas, 4.6)


def glosario(d, ruta):
    M.heading(d, 'Glosario', 1, salto=True)
    for l in R.leer(ruta):
        if ':' in l and l.strip():
            t, df = l.split(':', 1)
            p = M.par(d, '', despues=3)
            M.run(p, t.strip() + ': ', True, size=10, color=M.DARK); M.run(p, df.strip(), size=10)


def creditos(d):
    M.heading(d, 'Créditos y datos de la edición', 1, salto=True)
    for t in ['Desarrollo Personal y Social · 7.º grado · Educación Escolar Básica, Tercer Ciclo. Libro del estudiante. Edición Esencial Comercial 2026.',
              'Este libro sigue el programa de estudio de Desarrollo Personal y Social del Ministerio de Educación y Ciencias para el 7.º grado (componente local), con sus dos componentes: Orientación Educacional y Vocacional y Proyecto Educativo Comunitario. Las capacidades se citan textualmente del programa. No es una publicación oficial del Ministerio ni cuenta con su aprobación o certificación.',
              'Los indicadores de logro de los talleres del Proyecto Educativo Comunitario, los casos, los diálogos y el proyecto modelo son de elaboración editorial. Belén, Rodrigo, Dahiana, Matías y el Colegio Arasa Poty son personajes e institución ficticios, creados con fines didácticos.',
              'Figuras e infografías: esquemas de elaboración editorial. Las figuras de las clases provienen de la edición anterior de la serie y se reproducen sin modificaciones; las figuras de los talleres del proyecto fueron elaboradas para esta edición. Portada: diseño editorial.',
              'Información sobre normas y servicios de ayuda vigente a octubre de 2026.',
              'República del Paraguay · 2026']:
        M.par(d, t, 10, despues=6)


def construir(paginas=None):
    R.USADAS.clear()
    E = entradas()
    d = M.nuevo_doc('Desarrollo Personal y Social 7.º grado — Libro del estudiante', 'Desarrollo Personal y Social · Tercer Ciclo · EEB',
                    'Desarrollo Personal y Social; Orientación; Proyecto Educativo Comunitario; 7.º grado')
    M.imagen_pagina_completa(d, B + 'portadas/portada_libro.png')
    cuerpo = M.portada_en_seccion(d); M.pie_paginas(d, cuerpo)
    M.heading(d, 'Presentación', 1, estilo='Título preliminar')
    for l in FRONT['PRESENTACION']:
        if l.strip():
            M.par(d, l.strip(), 11, despues=6)
    R.render(d, FRONT['COMO_USAR'])
    M.heading(d, 'Índice', 1, salto=True, estilo='Título preliminar')
    M.indice(d, E, paginas)
    # prueba diagnóstica
    M.heading(d, E[0][1], 1, salto=True)
    M.linea_nombre(d)
    R.render(d, FRONT['DIAGNOSTICA'])
    unidad_abierta = set()
    for e in C.ENCUENTROS:
        n, t, k, u, caps, tit, _ = e
        L = fuente(n)
        if L is None:
            continue
        rot = titulo_enc(e)
        if t == 'C':
            if u not in unidad_abierta:
                apertura_unidad(d, u); unidad_abierta.add(u)
                M.heading(d, rot, 2)
            else:
                M.heading(d, rot, 2, salto=True)
            R.render(d, L); notas(d, rot)
        elif t == 'P':
            M.heading(d, rot, 1, salto=True)
            if k == 1:
                M.caja(d, 'Componente 2 — Proyecto Educativo Comunitario', [x.strip() for x in FRONT['PEC'] if x.strip()])
            R.render(d, L); notas(d, rot)
        else:
            M.salto(d)
            color = 'B8860B' if t == 'E' else '1B4F72'
            M.banda(d, rot, 'Desarrollo Personal y Social · 7.º grado', color, nombre=True, nivel=1 if t == 'I' else 2)
            R.render(d, L); notas(d, rot)
    # anexo, glosario y créditos
    if os.path.exists(F + 'anexo_pec.md'):
        M.heading(d, 'Anexo — Proyecto Educativo Comunitario', 1, salto=True)
        A = R.leer(F + 'anexo_pec.md')
        A = [('#H2 ' + l[3:]) if l.startswith('## ') else ('## ' + l[4:]) if l.startswith('### ') else l for l in A]
        primero = True
        bloques, cur = [], []
        for l in A:
            if l.startswith('#H2 '):
                if cur: bloques.append(cur)
                cur = [l]
            else:
                cur.append(l)
        if cur: bloques.append(cur)
        for b in bloques:
            if b[0].startswith('#H2 '):
                M.heading(d, b[0][4:].strip(), 2, salto=not primero); primero = False
                R.render(d, b[1:])
            else:
                R.render(d, b)
    if os.path.exists(F + 'glosario.md'):
        glosario(d, F + 'glosario.md')
    creditos(d)
    M.no_actualizar_campos(d)
    M.purgar_relaciones(d)
    return d, E


def pdf(docx_path):
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', OUT, docx_path],
                   check=True, capture_output=True, env=dict(os.environ, HOME='/tmp/lohome'))
    return docx_path[:-5] + '.pdf'


def llenado(pg):
    bl = [b for b in pg.get_text('blocks') if b[4].strip() and not b[4].strip().startswith('Página')]
    ys = [b[3] for b in bl] + [r.y1 for im in pg.get_images(full=True) for r in pg.get_image_rects(im[0])] + \
         [dr['rect'].y1 for dr in pg.get_drawings() if dr['rect'].y1 < pg.rect.height * 0.95]
    return max(ys) / pg.rect.height if ys else 0


def ciclo(ruta, pags):
    for vuelta in range(5):
        d, E = construir(pags); d.save(ruta); p = pdf(ruta)
        nuevas, total = M.paginas_de(p, [t for _, t in E], desde=4)
        if nuevas == pags:
            return d, E, p, pags, total
        pags = nuevas
    return d, E, p, pags, total


if __name__ == '__main__':
    import pymupdf
    os.makedirs(OUT, exist_ok=True)
    ruta = OUT + NOMBRE + '.docx'
    d, E = construir(); d.save(ruta); p = pdf(ruta)
    pags, total = M.paginas_de(p, [t for _, t in E], desde=4)
    d, E, p, pags, total = ciclo(ruta, pags)
    # Regla N-02: una pieza que termina con más del 55 % de hoja libre se completa con renglones útiles
    for ronda in range(3):
        doc = pymupdf.open(p); falt = {}
        for k, (niv, t) in enumerate(E):
            if t.startswith(('UNIDAD', 'Anexo', 'Glosario', 'Créditos')):
                continue
            sig = next((pags[j] for j in range(k + 1, len(E)) if pags[j] > pags[k]), total + 1)
            ult = sig - 1
            fr = llenado(doc[ult - 1])
            if fr < 0.45 and t not in NOTAS:
                falt[t] = int((0.92 - fr) * doc[ult - 1].rect.height / 72 * 2.54 / 0.71) - 3
        if not falt:
            break
        NOTAS.update(falt)
        d, E, p, pags, total = ciclo(ruta, pags)
    doc = pymupdf.open(p)
    vac = [i + 1 for i, pg in enumerate(doc) if 3 < i < len(doc) - 1 and llenado(pg) < 0.25]
    print('páginas', total, '· anotaciones', len(NOTAS), '· casi vacías', vac)
    print('MB docx', round(os.path.getsize(ruta) / 1e6, 2), '· MB pdf', round(os.path.getsize(p) / 1e6, 2))
    print('figuras', R.USADAS)
    json.dump({'entradas': E, 'paginas': pags, 'total': total, 'notas': NOTAS, 'figuras': R.USADAS},
              open(B + 'indice_libro.json', 'w'), ensure_ascii=False, indent=0)
