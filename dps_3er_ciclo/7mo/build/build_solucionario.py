# -*- coding: utf-8 -*-
"""Solucionario docente — Desarrollo Personal y Social 7.º, oficio vertical. Fuentes: fuente/sol/*.md. Entregables: .docx y .pdf."""
import os, json, sys
import maqueta as M
import render as R
import curriculo as C
from build_libro import secciones, pdf, OUT, B, llenado

S = B + '../fuente/sol/'
NOMBRE = 'Desarrollo_Personal_y_Social_7mo_Grado_SOLUCIONARIO_DOCENTE_2026'
FRONT = secciones(S + 'front.md')
PARCIAL = '--parcial' in sys.argv


def entradas():
    E = [(1, 'Protocolo para temas sensibles y privacidad'), (1, 'Orientaciones para la prueba diagnóstica')]
    vistas = set()
    for e in C.ENCUENTROS:
        n, t, k, u, *_ = e
        if PARCIAL and not os.path.exists(S + 'e%02d.md' % n):
            continue
        if t in 'CE' and u not in vistas:
            vistas.add(u); E.append((1, 'UNIDAD %d — %s' % (u, C.UNIDADES[u])))
        E.append((1 if t in 'PI' else 2, C.rotulo(e)))
    if os.path.exists(S + 'anexo_pec.md'):
        E.append((1, 'Guía general del Proyecto Educativo Comunitario'))
    E.append((1, 'Criterios generales de valoración'))
    return E


def construir(paginas=None):
    E = entradas()
    d = M.nuevo_doc('Desarrollo Personal y Social 7.º grado — Solucionario docente', 'Material exclusivo del docente',
                    'Desarrollo Personal y Social; solucionario; Proyecto Educativo Comunitario')
    M.imagen_pagina_completa(d, B + 'portadas/portada_solucionario.png')
    cuerpo = M.portada_en_seccion(d); M.pie_paginas(d, cuerpo)
    M.heading(d, 'Cómo usar este solucionario', 1, estilo='Título preliminar')
    for l in FRONT['COMO_USAR']:
        if l.strip():
            M.par(d, l.strip(), 10.5, despues=5)
    M.heading(d, 'Índice', 1, salto=True, estilo='Título preliminar')
    M.indice(d, E, paginas)
    M.heading(d, 'Protocolo para temas sensibles y privacidad', 1, salto=True)
    R.render(d, [l for l in FRONT['SENSIBLES'] if not l.startswith('## ')])
    M.heading(d, 'Orientaciones para la prueba diagnóstica', 1)
    R.render(d, FRONT['DIAGNOSTICA'])
    vistas = set()
    for e in C.ENCUENTROS:
        n, t, k, u, *_ = e
        ruta = S + 'e%02d.md' % n
        if PARCIAL and not os.path.exists(ruta):
            continue
        L = R.leer(ruta)
        if t in 'CE' and u not in vistas:
            vistas.add(u); M.heading(d, 'UNIDAD %d — %s' % (u, C.UNIDADES[u]), 1, salto=True)
            M.heading(d, C.rotulo(e), 2)
        else:
            M.heading(d, C.rotulo(e), 1 if t in 'PI' else 2, salto=(t in 'PI'))
        R.render(d, L)
    if os.path.exists(S + 'anexo_pec.md'):
        M.heading(d, 'Guía general del Proyecto Educativo Comunitario', 1, salto=True)
        R.render(d, R.leer(S + 'anexo_pec.md'))
    M.heading(d, 'Criterios generales de valoración', 1, salto=True)
    R.render(d, [l for l in FRONT['CRITERIOS'] if not l.startswith('## ')])
    M.no_actualizar_campos(d)
    M.purgar_relaciones(d)
    return d, E


if __name__ == '__main__':
    import pymupdf
    ruta = OUT + NOMBRE + '.docx'
    d, E = construir(); d.save(ruta); p = pdf(ruta)
    pags, total = M.paginas_de(p, [t for _, t in E], desde=3)
    for vuelta in range(5):
        d, E = construir(pags); d.save(ruta); p = pdf(ruta)
        nuevas, total = M.paginas_de(p, [t for _, t in E], desde=3)
        if nuevas == pags:
            break
        pags = nuevas
    doc = pymupdf.open(p)
    vac = [i + 1 for i, pg in enumerate(doc) if 2 < i < len(doc) - 1 and llenado(pg) < 0.25]
    print('Solucionario: páginas', total, '· índice estable', nuevas == pags, '· casi vacías', vac)
    json.dump({'entradas': E, 'paginas': pags, 'total': total}, open(B + 'indice_sol.json', 'w'), ensure_ascii=False, indent=0)
