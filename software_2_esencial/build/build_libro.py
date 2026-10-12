# -*- coding: utf-8 -*-
"""Arma Gabinete_Informatica_Software_2do_Curso_LIBRO_ESENCIAL_COMERCIAL_2026 (.docx y .pdf) desde src_md/:
Clase N → Práctica N → Ficha de continuación (según el Plan Anual) → evaluaciones → PFI.
Dos pasadas: la segunda puebla el índice con las páginas reales leídas del PDF."""
import os, re, subprocess, sys, glob, hashlib, io
import maqueta as M

B = '/home/claude/sw2/build/'
S = '/home/claude/sw2/src_md/'
OUT = '/home/claude/sw2/salida/'
os.makedirs(OUT, exist_ok=True)
NOMBRE = 'Gabinete_Informatica_Software_2do_Curso_LIBRO_ESENCIAL_COMERCIAL_2026'
FIG = B + 'figs_src/'
FIG_OPT = B + 'figs_opt/'
POR = B + 'portadas/'
# Ficha de continuación que sigue a cada clase (secuencias del Plan Anual)
FICHA_TRAS = {1: 'A', 4: 'B', 5: 'C', 7: 'D', 8: 'E', 10: 'F', 12: 'G', 14: 'H', 16: 'I', 17: 'J', 18: 'K', 20: 'L'}
UNIDADES = {1: 'Componentes básicos de una computadora', 2: 'Redes de computadoras'}


def leer(nombre):
    return open(S + nombre + '.md').read().split('\n')


def titulo_de(lineas):
    return re.sub(r'^@@H[12] ', '', lineas[0]).strip()


# ---------- PNG sin pérdida: mismos píxeles, menos bytes ----------
def figura(nombre):
    src = FIG + nombre
    if not nombre.lower().endswith('.png'):
        return src
    os.makedirs(FIG_OPT, exist_ok=True)
    dst = FIG_OPT + nombre
    if not os.path.exists(dst):
        from PIL import Image
        import numpy as np
        a = Image.open(src)
        buf = io.BytesIO(); a.save(buf, 'PNG', optimize=True)
        b = Image.open(io.BytesIO(buf.getvalue()))
        same = a.mode == b.mode and a.size == b.size and np.array_equal(np.asarray(a), np.asarray(b))
        if same and buf.tell() < os.path.getsize(src):
            open(dst, 'wb').write(buf.getvalue())
        else:
            open(dst, 'wb').write(open(src, 'rb').read())
    return dst


# ---------- render de un bloque de texto marcado ----------
ROTULOS = ('Capacidades', 'Marcá', 'Completá', 'Verdadero o falso', 'Respondé', 'Relacioná', 'Ordená', 'Resolvé', 'Calculá', 'Analizá', 'Explicá', 'Pensá')


def render(d, L, nivel=0, foto_cm=None):
    f = (1, 0.5, 0.2)[nivel]; kimg = (1, 0.85, 0.72)[nivel]
    i = 0
    while i < len(L):
        l = L[i]
        s = l.strip()
        if not s or s == '/':
            i += 1; continue
        if l.startswith('@@H'):
            i += 1; continue  # el título lo pone quien llama
        if l.startswith('[[FICHA]]'):
            j = L.index('[[/FICHA]]', i)
            blk = L[i + 1:j]
            cap = [x[len('Capacidad: '):] for x in blk if x.startswith('Capacidad: ')]
            caps = [c for c in cap[0].split(' || ')] if cap else []
            tema = next(x[len('Tema: '):] for x in blk if x.startswith('Tema: '))
            inds = [x[2:] for x in blk if x.startswith('- ')]
            M.ficha(d, caps if len(caps) > 1 else caps[0], tema, inds)
            i = j + 1; continue
        m = re.match(r'\[\[CAJA (.*)\]\]$', l)
        if m:
            j = L.index('[[/CAJA]]', i)
            tit = m.group(1); cuerpo = [x for x in L[i + 1:j] if x.strip() and x.strip() != '/']
            if ' / ' in tit and not cuerpo:
                tit, resto = tit.split(' / ', 1); cuerpo = [resto]
            if tit.startswith('EVALUACIÓN'):
                M.banda(d, tit.replace('EVALUACIÓN INTEGRADORA · ', 'Evaluación integradora · ').replace('EVALUACIÓN DE LA UNIDAD', 'Evaluación de la Unidad'),
                        ' '.join(cuerpo), M.DARK, nombre=False)
            else:
                M.caja(d, tit, cuerpo)
            i = j + 1; continue
        if l.startswith('[[TABLA]]'):
            j = L.index('[[/TABLA]]', i)
            filas = [[c.strip() for c in x.split(' | ')] for x in L[i + 1:j]]
            M.tabla(d, filas[0], filas[1:])
            i = j + 1; continue
        m = re.match(r'\[\[IMG (\S+)\|([\d.]+)\]\]', l)
        if m:
            cap = L[i + 1]
            ancho = float(m.group(2)) if foto_cm is None else foto_cm
            M.imagen(d, figura(m.group(1)), cap, ancho * kimg)
            i += 2; continue
        if l.startswith('## '):
            M.heading(d, s[3:].strip(), 3); i += 1; continue
        if s.startswith('Nombre y Apellido:'):
            M.linea_nombre(d); i += 1; continue
        if re.fullmatch(r'_{8,}', s):
            M.renglones(d, 1); i += 1; continue
        if re.match(r'^[a-e]\) ', s) and l.startswith('    '):
            M.par(d, s, indent=0.9, despues=round(1 * f), keep=bool(i + 1 < len(L) and re.match(r'^\s{4}[a-e]\) ', L[i + 1])))
            i += 1; continue
        if re.match(r'^\s{2,}\d+\. ', l):
            M.par(d, s, indent=0.6, despues=round(2 * f)); i += 1; continue
        if re.match(r'^\d+\. ', s):
            sig = L[i + 1] if i + 1 < len(L) else ''
            M.par(d, s, indent=0.3, despues=round(2 * f), keep=sig.startswith('    '))
            i += 1; continue
        if s.startswith('Punto de control:'):
            p = M.par(d, '', antes=round(2 * f), despues=round(6 * f))
            M.run(p, 'Punto de control: ', True, size=10.5, color=M.DARK); M.run(p, s[len('Punto de control:'):].strip(), size=10.5)
            i += 1; continue
        m = re.match(r'^(Actividad \d+) — (Objetivo: )?(.*)$', s)
        if m:
            p = M.par(d, '', antes=round(6 * f), despues=round(3 * f), keep=True)
            M.run(p, m.group(1) + ' — ', True, size=10.5, color=M.MED); M.run(p, ('Objetivo: ' if m.group(2) else '') + m.group(3), size=10.5, italic=True)
            i += 1; continue
        if s.startswith(('Competencia de la práctica:', 'Competencia de la ficha:', 'Competencia integradora:')):
            k, v = s.split(':', 1)
            M.caja(d, 'Competencia', [v.strip()])
            i += 1; continue
        if s.startswith('• '):
            M.par(d, s, indent=0.3, despues=round(2 * f)); i += 1; continue
        if s.endswith(':') and len(s) < 70 and s.startswith(ROTULOS):
            M.par(d, s, bold=True, color=M.DARK, keep=True, antes=round(4 * f), despues=round(2 * f)); i += 1; continue
        M.par(d, s, despues=round(4 * f)); i += 1
    return d


# ---------- índice ----------
def entradas():
    E = [(1, 'Prueba diagnóstica — ¿Qué sabés ya?')]
    for n in range(1, 21):
        if n == 1:
            E.append((1, 'UNIDAD 1 — %s' % UNIDADES[1]))
        if n == 11:
            E.append((1, 'UNIDAD 2 — %s' % UNIDADES[2]))
        E.append((2, titulo_de(leer('tomo_clase%02d' % n))))
        E.append((2, titulo_de(leer('lab_practica%02d' % n))))
        if n in FICHA_TRAS:
            E.append((2, titulo_de(leer('lab_ficha_' + FICHA_TRAS[n]))))
        if n == 10:
            E += [(2, 'Evaluación de la Unidad 1'), (2, 'Evaluación integradora de la 1.ª etapa')]
        if n == 20:
            E += [(2, 'Evaluación de la Unidad 2'), (2, 'Evaluación integradora de la 2.ª etapa')]
    E.append((1, titulo_de(leer('lab_pfi'))))
    return E


def unidad(d, u):
    quitar_vacio_final(d)
    M.heading(d, 'UNIDAD %d — %s' % (u, UNIDADES[u]), 1, salto=True)
    L = leer('tomo_unidad%d' % u)
    render(d, L[1:])


def evaluacion(d, nombre, titulo, extra=()):
    quitar_vacio_final(d)
    M.heading(d, titulo, 2, salto=True)
    L = leer(nombre)
    # el título ya va como encabezado: se omite la banda original
    if L[0].startswith('[[CAJA EVALUACIÓN'):
        j = L.index('[[/CAJA]]')
        sub = ' '.join(x for x in L[1:j] if x.strip())
        M.par(d, sub, italic=True, color='555555', despues=4)
        L = L[j + 1:]
    render(d, L, COMP.get(titulo, 0))
    for e in extra:
        render(d, leer(e), COMP.get(titulo, 0))


COMP = {}


def quitar_vacio_final(d):
    """Quita los párrafos vacíos que quedaron al final de la unidad anterior: si la hoja se llenó justo,
    pasarían solos a una hoja nueva y el salto de la sección siguiente la dejaría en blanco."""
    from docx.oxml.ns import qn
    body = d.element.body
    while True:
        el = body[-2] if body[-1].tag == qn('w:sectPr') else body[-1]
        if el.tag != qn('w:p'):
            return
        if ''.join(t.text or '' for t in el.iter(qn('w:t'))).strip() or list(el.iter(qn('w:drawing'))) or list(el.iter(qn('w:br'))) or el.find('.//' + qn('w:sectPr')) is not None:
            return
        body.remove(el)


def construir(paginas=None):
    d = M.nuevo_doc('Gabinete de Informática – Software · 2.º Curso · Libro del estudiante con prácticas de laboratorio',
                    'Edición Esencial Comercial 2026', 'BTI; Gabinete de Informática; Software; hardware; redes')
    M.imagen_pagina_completa(d, POR + 'portada_libro.jpg')
    sec = M.portada_en_seccion(d)
    M.pie_paginas(d, sec)
    # Presentación e índice
    M.heading(d, 'Presentación', 1, estilo='Título preliminar')
    render(d, leer('pre_presentacion'))
    M.heading(d, 'Índice', 1, salto=True, estilo='Título preliminar')
    E = entradas()
    M.indice(d, E, paginas)
    # Prueba diagnóstica
    M.heading(d, 'Prueba diagnóstica — ¿Qué sabés ya?', 1, salto=True)
    render(d, leer('tomo_diagnostica')[1:])
    for n in range(1, 21):
        if n in (1, 11):
            unidad(d, 1 if n == 1 else 2)
        C = leer('tomo_clase%02d' % n)
        quitar_vacio_final(d)
        M.heading(d, titulo_de(C), 2, salto=(n not in (1, 11)))
        render(d, C[1:], COMP.get(titulo_de(C), 0))
        P = leer('lab_practica%02d' % n)
        quitar_vacio_final(d)
        M.heading(d, titulo_de(P), 2, salto=True)
        render(d, P[1:], COMP.get(titulo_de(P), 0), foto_cm=8.5)
        if n in FICHA_TRAS:
            F = leer('lab_ficha_' + FICHA_TRAS[n])
            quitar_vacio_final(d)
            M.heading(d, titulo_de(F), 2, salto=True)
            render(d, F[1:], COMP.get(titulo_de(F), 0))
        if n == 10:
            evaluacion(d, 'tomo_eval_u1', 'Evaluación de la Unidad 1')
            evaluacion(d, 'tomo_integ1', 'Evaluación integradora de la 1.ª etapa', extra=('tomo_caso1',))
        if n == 20:
            evaluacion(d, 'tomo_eval_u2', 'Evaluación de la Unidad 2')
            evaluacion(d, 'tomo_integ2', 'Evaluación integradora de la 2.ª etapa', extra=('tomo_caso2',))
    PF = leer('lab_pfi')
    quitar_vacio_final(d)
    M.heading(d, titulo_de(PF), 1, salto=True)
    render(d, PF[1:], COMP.get(titulo_de(PF), 0))
    # contraportada
    quitar_vacio_final(d)
    M.seccion_sin_pie(d)
    M.imagen_pagina_completa(d, POR + 'contraportada.jpg', 'Contraportada')
    M.no_actualizar_campos(d)
    M.purgar_relaciones(d)
    return d, E


def pdf(docx_path):
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', OUT, docx_path],
                   check=True, capture_output=True, env=dict(os.environ, HOME='/tmp/lohome'))
    return docx_path[:-5] + '.pdf'


if __name__ == '__main__':
    ruta = OUT + NOMBRE + '.docx'
    d, E = construir(); d.save(ruta); p = pdf(ruta)
    def desde(pdfp):
        import pymupdf
        for i, pg in enumerate(pymupdf.open(pdfp)):
            if 'Nombre y Apellido' in pg.get_text():
                return i + 1
    for vuelta in range(4):
        pags, total = M.paginas_de(p, [t for _, t in E], desde=desde(p))
        d, E = construir(pags); d.save(ruta); p = pdf(ruta)
        pags2, total = M.paginas_de(p, [t for _, t in E], desde=desde(p))
        if pags2 == pags:
            break
    import pymupdf
    def casi_vacias(pdfp):
        doc = pymupdf.open(pdfp); out = []
        for i, pg in enumerate(doc):
            bl = [b for b in pg.get_text('blocks') if not b[4].strip().startswith('Página')]
            ys = [b[3] for b in bl] + [r.y1 for im in pg.get_images(full=True) for r in pg.get_image_rects(im[0])]
            fr = max(ys) / pg.rect.height if ys else 0
            if fr < 0.22 and 3 < i < len(doc) - 1:
                out.append(i + 1)
        return out
    for ronda in range(3):
        vac = casi_vacias(p)
        if not vac:
            break
        for v in vac:
            k = max(j for j, pg in enumerate(pags2) if pg < v)
            t = E[k][1]
            if E[k][0] == 1 and k + 1 < len(E) and pags2[k + 1] < v:
                pass
            COMP[t] = min(COMP.get(t, 0) + 1, 2)
        print('ronda', ronda, 'casi vacías', vac)
        for vuelta in range(4):
            d, E = construir(pags2); d.save(ruta); p = pdf(ruta)
            nuevas, total = M.paginas_de(p, [t for _, t in E], desde=desde(p))
            if nuevas == pags2:
                break
            pags2 = nuevas
    for vuelta in range(5):
        final, total = M.paginas_de(p, [t for _, t in E], desde=desde(p))
        if final == pags2:
            break
        pags2 = final
        d, E = construir(pags2); d.save(ruta); p = pdf(ruta)
    print('compactadas', COMP, '· casi vacías', casi_vacias(p))
    print('páginas', total, '· índice estable', final == pags2, '· MB', round(os.path.getsize(ruta) / 1e6, 1))
    import json
    json.dump({'entradas': E, 'paginas': final, 'total': total, 'comp': COMP}, open(B + 'indice_libro.json', 'w'), ensure_ascii=False)
