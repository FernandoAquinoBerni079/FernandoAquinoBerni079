# -*- coding: utf-8 -*-
"""Controles de la corrección v2 (V2-01 y V2-02): Planes de Clase y Plan Anual. Uso: python3 control_v2.py (desde build/).
HISTÓRICO: verificó la v2 (commit 558a335). Desde la v3 el Plan Anual cambia a propósito (H02) y rige control_v3.py."""
import re, subprocess, io, docx, pymupdf
from docx.oxml.ns import qn
S = '../salida/Gabinete_Informatica_Software_1er_Curso_'
ok = 0; fallos = []
def chk(c, m):
    global ok
    if c: ok += 1
    else: fallos.append(m)
def ocup(pg):
    bl = [b for b in pg.get_text('blocks') if not b[4].strip().startswith('Página')]
    return max(b[3] for b in bl) / pg.rect.height if bl else 0
cm = lambda v: round(v / 72 * 2.54, 1)
# Planes de Clase
P = pymupdf.open(S + 'PLANES_DE_CLASE_COMERCIAL_2026.pdf')
chk(P.page_count == 38, 'Planes: %d páginas (se esperan 38: portada, índice y 36 planes)' % P.page_count)
nums = [int(m.group(1)) for pg in P for m in [re.search(r'Plan de Clase N\.º (\d+) de 36', pg.get_text())] if m]
chk(nums == list(range(1, 37)), 'Planes: cada página 3–38 debe abrir un plan, en orden')
chk(not any('continuación' in pg.get_text() for pg in P), 'Planes: quedan páginas de continuación')
for i, pg in enumerate(P):
    chk((cm(pg.rect.width), cm(pg.rect.height)) == (21.6, 33.0), 'Planes p%d no es oficio' % (i + 1))
    if i >= 2:
        t = pg.get_text(); chk('Docente' in t and 'Dirección — Visto bueno' in t, 'Planes p%d: faltan las firmas' % (i + 1))
# Plan Anual
A = pymupdf.open(S + 'PLAN_ANUAL_COMERCIAL_2026.pdf')
chk(A.page_count <= 11, 'Plan Anual: %d páginas (máximo 11)' % A.page_count)
chk(ocup(A[-1]) > 0.25 and 'Firma del docente' in A[-1].get_text(), 'Plan Anual: la última hoja solo tiene la firma')
for i, pg in enumerate(A[1:], 2):
    chk((cm(pg.rect.width), cm(pg.rect.height)) == (33.0, 21.6), 'Plan Anual p%d no es oficio horizontal' % i)
# márgenes de la colección en los .docx
for n in ('PLANES_DE_CLASE', 'PLAN_ANUAL'):
    d = docx.Document(S + n + '_COMERCIAL_2026.docx')
    chk(all(round(x.cm, 2) == 1.27 for s in d.sections for x in (s.top_margin, s.bottom_margin, s.left_margin, s.right_margin)), n + ': márgenes distintos de 1,27 cm')
# identidad textual con la versión v1 (commit 61feba7): solo cambian los números de página del índice
def txt(blob):
    d = docx.Document(io.BytesIO(blob)); return [''.join(t.text or '' for t in p.iter(qn('w:t'))) for p in d.element.body.iter(qn('w:p'))]
for n in ('PLANES_DE_CLASE', 'PLAN_ANUAL'):
    f = 'software_1_esencial/salida/Gabinete_Informatica_Software_1er_Curso_' + n + '_COMERCIAL_2026.docx'
    v1 = txt(subprocess.run(['git', 'show', '61feba7:' + f], capture_output=True, cwd='../..').stdout)
    v2 = txt(open('../../' + f, 'rb').read())
    chk(len(v1) == len(v2) and all(re.sub(r'\d+$', '', a) == re.sub(r'\d+$', '', b) for a, b in zip(v1, v2)), n + ': el texto cambió respecto de la v1')
# Muestra
M = pymupdf.open(S + 'MUESTRA_COMERCIAL_2026.pdf'); tm = ''.join(p.get_text() for p in M)
chk(M.page_count == 13 and 'Plan de Clase N.º 1 de 36' in tm and 'continuación' not in tm, 'Muestra: debe cerrar con el Plan 1 en una hoja')
chk(not re.search(r'Opción correcta|Resultado esperado|Orientación:', tm), 'Muestra: revela claves')
print('Controles v2 (Planes de Clase, Plan Anual y Muestra): %d OK · %d fallos' % (ok, len(fallos))); [print(' -', f) for f in fallos]
