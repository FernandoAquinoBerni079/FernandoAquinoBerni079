# -*- coding: utf-8 -*-
"""Prácticas del cuaderno vigente de 1.º → estructura del libro (titulo, competencia, saber, acts, desafio) y PFI."""
import docx, json, re
from docx.oxml.ns import qn
import parse_tomo1 as PT  # reutiliza la detección de código
d = docx.Document('/home/claude/alg1/src/Algoritmica_1er_Curso_CUADERNO_PRACTICAS.docx')
items = []
for el in d.element.body.iterchildren():
    tag = el.tag.split('}')[1]
    if tag == 'p':
        p = docx.text.paragraph.Paragraph(el, d)
        if el.findall('.//' + qn('a:blip')):
            items.append(('img', '')); continue
        if p.text.strip():
            items.append((p.style.name, p.text.strip()))
    elif tag == 'tbl':
        t = docx.table.Table(el, d)
        if len(t.rows) == 1 and len(t.columns) == 1:
            items.append(('caja', PT.lineas_celda(t.rows[0].cells[0])))
        else:
            rows = [[c.text.strip() for c in r.cells] for r in t.rows]
            items.append(('tabla', rows))
PR = {}; cur = None; act = None; modo = None; pfi = []
for st, x in items:
    if st == 'Heading 1' and x.startswith('PROYECTO FINAL'):
        modo = 'pfi'; cur = None; continue
    if modo == 'pfi':
        pfi.append((st, x)); continue
    if st == 'Heading 2':
        m = re.match(r'Práctica (\d+) — (.+)', x)
        if m:
            cur = {'n': int(m.group(1)), 'titulo': m.group(2), 'competencia': '', 'saber': [], 'acts': [], 'desafio': '', 'extra': []}
            PR[cur['n']] = cur; modo = 'cab'; act = None
        else:
            cur = None; modo = None
        continue
    if cur is None:
        continue
    if st == 'Heading 3':
        if x.startswith('Lo que necesitás'):
            modo = 'saber'
        elif x.startswith('Actividad'):
            m = re.match(r'Actividad (\d+) — (.+)', x)
            act = {'titulo': m.group(2), 'objetivo': '', 'modelo': None, 'pasos': [], 'control': ''}; cur['acts'].append(act); modo = 'act'
        elif x.startswith('Desafío'):
            modo = 'des'
        continue
    if modo == 'cab':
        if isinstance(x, str) and (x.startswith('Nombre y Apellido') or x == 'Competencia'):
            continue
        if st == 'caja':
            cur['competencia'] = ' '.join(x[1:]) if x and x[0].startswith('Competencia') else ' '.join(x)
        else:
            cur['competencia'] = x
    elif modo == 'saber':
        if st == 'caja':
            cur['extra'].append(('caja', x))
        elif st in ('img', 'tabla'):
            cur['extra'].append((st, x))
        else:
            cur['saber'].append(x)
    elif modo == 'act':
        if st == 'caja':
            if x and x[0].startswith('✅'):
                act['control'] = re.sub(r'^✅\s*Punto de control\s*[—:-]\s*', '', ' '.join(x)); continue
            act['modelo'] = (x[0].split(' — ', 1)[1] if ' — ' in x[0] else x[0], x[1:]); continue
        if st == 'tabla':
            act.setdefault('tablas', []).append(x); continue
        if x.startswith('Objetivo:'):
            act['objetivo'] = x[len('Objetivo:'):].strip()
        elif x.startswith('✅'):
            act['control'] = re.sub(r'^✅\s*Punto de control\s*[—:-]\s*', '', x)
        elif re.match(r'^\d+\. ', x):
            act['pasos'].append(re.sub(r'^\d+\. ', '', x))
        else:
            act.setdefault('otros', []).append(x)
    elif modo == 'des':
        cur['desafio'] = (cur['desafio'] + ' ' + x).strip()
json.dump({'PR': PR, 'PFI': pfi}, open('/home/claude/alg1/build/cuaderno.json', 'w'), ensure_ascii=False, indent=1)
print(len(PR), [len(p['acts']) for p in PR.values()])
print([ (n, [a.get('otros') for a in p['acts'] if a.get('otros')]) for n,p in PR.items() if any(a.get('otros') for a in p['acts'])][:5])
print([ (n, p['extra'][:1]) for n,p in PR.items() if p['extra']][:6])
