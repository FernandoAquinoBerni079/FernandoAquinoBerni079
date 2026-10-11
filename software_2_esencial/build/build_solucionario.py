# -*- coding: utf-8 -*-
"""Arma Gabinete_Informatica_Software_2do_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026 desde src_md/sol.md."""
import os, re, json
import maqueta as M
from build_libro import pdf, OUT, B, S

NOMBRE = 'Gabinete_Informatica_Software_2do_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026'
L = open(S + 'sol.md').read().split('\n')


def entradas():
    E = []
    for l in L:
        if l.startswith('# '):
            E.append((1, l[2:].strip()))
        elif l.startswith('## ') and not l.startswith('## Presentación'):
            E.append((2, l[3:].strip()))
    return E


def construir(pags=None):
    d = M.nuevo_doc('Gabinete de Informática – Software · 2.º Curso · Solucionario del docente', 'Material exclusivo del docente',
                    'BTI; Gabinete de Informática; Software; solucionario')
    M.imagen_pagina_completa(d, B + 'portadas/portada_solucionario.jpg')
    sec = M.portada_en_seccion(d)
    E = entradas()
    i = 0; primera_clase = True
    while i < len(L):
        l = L[i]; s = l.strip()
        if not s:
            i += 1; continue
        if l.startswith('## Presentación'):
            M.heading(d, 'Presentación', 1, estilo='Título preliminar')
            j = i + 1
            while not L[j].startswith('#'):
                if L[j].strip():
                    M.par(d, L[j].strip())
                j += 1
            M.heading(d, 'Índice', 1, salto=True, estilo='Título preliminar')
            M.indice(d, E, pags)
            i = j; continue
        if l.startswith('# '):
            M.heading(d, s[2:], 1, salto=True); i += 1; continue
        if l.startswith('## '):
            M.heading(d, s[3:], 2); i += 1; continue
        if l.startswith('### '):
            M.heading(d, s[4:], 3); i += 1; continue
        if l.startswith('[[TABLA]]'):
            j = L.index('[[/TABLA]]', i)
            filas = [[c.strip() for c in x.split(' | ')] for x in L[i + 1:j]]
            M.tabla(d, filas[0], filas[1:], anchos=[3.0, 4.0, 3.6, 3.4, 2.4] if len(filas[0]) == 5 else None, size=8)
            i = j + 1; continue
        m = re.match(r'^(Práctica \d+|Ficha [A-L]) — (Resultado esperado:)(.*)$', s)
        if m:
            p = M.par(d, '', despues=5, antes=2)
            M.run(p, m.group(1) + ' — Resultado esperado: ', True, size=10, color=M.MED); M.run(p, m.group(3).strip(), size=10)
            i += 1; continue
        m = re.match(r'^(Opción correcta|Completar|V-F|Desarrollo del caso|Consigna \d+):(.*)$', s)
        if m:
            p = M.par(d, '', despues=3)
            M.run(p, m.group(1) + ': ', True, size=10); M.run(p, m.group(2).strip(), size=10)
            i += 1; continue
        M.par(d, s, size=10, despues=2, indent=0.3 if re.match(r'^(\d+\)|•)', s) else None)
        i += 1
    M.pie_paginas(d, sec)
    M.no_actualizar_campos(d)
    M.purgar_relaciones(d)
    return d, E


if __name__ == '__main__':
    ruta = OUT + NOMBRE + '.docx'
    d, E = construir(); d.save(ruta); p = pdf(ruta)
    import pymupdf
    def desde(pdfp):
        for i, pg in enumerate(pymupdf.open(pdfp)):
            if i > 2 and 'Consigna 1' in pg.get_text():
                return i + 1
    for v in range(4):
        pags, total = M.paginas_de(p, [t for _, t in E], desde=desde(p))
        d, E = construir(pags); d.save(ruta); p = pdf(ruta)
        p2, total = M.paginas_de(p, [t for _, t in E], desde=desde(p))
        if p2 == pags:
            break
    print('páginas', total, '· índice estable', p2 == pags)
    json.dump({'entradas': E, 'paginas': p2, 'total': total}, open(B + 'indice_sol.json', 'w'), ensure_ascii=False)
