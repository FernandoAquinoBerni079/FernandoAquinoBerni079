# -*- coding: utf-8 -*-
"""Muestra comercial: portada, presentación e índice del libro, Clase 1 con su Práctica 1, contraportada,
portada del solucionario, portada y primera hoja del Plan Anual, portada de los Planes y el Plan de Clase N.º 1."""
import json, os, pymupdf
B = '/home/claude/sw2/build/'; O = '/home/claude/sw2/salida/'; N = 'Gabinete_Informatica_Software_2do_Curso_'
L = pymupdf.open(O + N + 'LIBRO_ESENCIAL_COMERCIAL_2026.pdf')
S = pymupdf.open(O + N + 'SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026.pdf')
A = pymupdf.open(O + N + 'PLAN_ANUAL_COMERCIAL_2026.pdf')
P = pymupdf.open(O + N + 'PLANES_DE_CLASE_COMERCIAL_2026.pdf')
jl = json.load(open(B + 'indice_libro.json')); pg = {t: p for (n, t), p in zip(jl['entradas'], jl['paginas'])}
fichaA = pg['Ficha A — Compatibilidad gabinete · placa madre · fuente']
jp = json.load(open(B + 'indice_planes.json')); p1, p2 = jp['paginas'][0], jp['paginas'][1]
M = pymupdf.open()
for doc, a, b in ((L, 0, fichaA - 2), (L, L.page_count - 1, L.page_count - 1), (S, 0, 0), (A, 0, 1), (P, 0, 0), (P, p1 - 1, p2 - 2)):
    M.insert_pdf(doc, from_page=a, to_page=b)
M.set_metadata({'title': 'Gabinete de Informática – Software · 2.º Curso · Muestra comercial', 'author': 'Equipo editorial', 'subject': 'Edición Esencial Comercial 2026'})
M.subset_fonts()
out = O + N + 'MUESTRA_COMERCIAL_2026.pdf'
M.save(out, garbage=4, deflate=True, deflate_images=True, deflate_fonts=True, clean=True)
print('muestra', M.page_count, 'págs', round(os.path.getsize(out) / 1e6, 2), 'MB')
