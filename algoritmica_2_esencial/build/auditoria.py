# -*- coding: utf-8 -*-
"""Auditoría automática de liberación — Algorítmica 2.º Edición Esencial Comercial 2026 (v1).
Cada control suma al conteo; el resultado esperado es 0 fallos. Incluye la re-ejecución en PSeInt de
los programas de las prácticas y el control de las lecciones del piloto de 3.º (v2 y v2.1)."""
import re, json, os, collections, subprocess, hashlib
import docx, pymupdf
from docx.oxml.ns import qn
import actividades, practicas, evaluaciones, planes_data, preliminares as PRE
from estructura import cargar
import ediciones

O = '/home/claude/alg2/salida/'; B = '/home/claude/alg2/build/'; PS = '/home/claude/alg2/pseint/'
F = {k: O + 'Algoritmica_2do_Curso_%s.docx' % k for k in
     ('LIBRO_ESENCIAL_COMERCIAL_2026', 'SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026', 'PLANES_DE_CLASE_ESENCIAL_COMERCIAL_2026', 'PLAN_ANUAL_ESENCIAL_COMERCIAL_2026')}
LIB, SOL, PLA, ANU = list(F.values())
RES = []


def chk(bloque, nombre, ok, detalle=''):
    RES.append((bloque, nombre, bool(ok), detalle if not ok else ''))


def pdf(p):
    return pymupdf.open(p[:-5] + '.pdf')


def textos_doc(path):
    d = docx.Document(path)
    out = []
    for el in d.element.body.iter():
        if el.tag == qn('w:p'):
            t = ''.join(x.text or '' for x in el.iter(qn('w:t')))
            st = el.find('.//' + qn('w:pStyle'))
            out.append((st.get(qn('w:val')) if st is not None else '', t))
    return d, out


def H(s):
    return s.startswith('Heading') or s.startswith('Ttulo')


_pre, C, _ev, U = cargar(); ediciones.aplicar(C); FIG = ediciones.fig_refs(C)
dL, PL = textos_doc(LIB)
TL = '\n'.join(t for _, t in PL)
pdfL = pdf(LIB)
pags = [pg.get_text() for pg in pdfL]
dS, PSx = textos_doc(SOL); TS = '\n'.join(t for _, t in PSx)

# ---------------- A. Estructura ----------------
clases = [t for s, t in PL if re.match(r'^Clase \d+ — ', t) and H(s)]
prs = [t for s, t in PL if re.match(r'^Práctica \d+ — ', t) and H(s)]
chk('A', 'Cantidad de clases = 21', len(clases) == 21, len(clases))
chk('A', 'Cantidad de prácticas = 21', len(prs) == 21, len(prs))
seq = [t.split(' — ')[0] for s, t in PL if H(s) and re.match(r'^(Clase|Práctica) \d+ — ', t)]
chk('A', 'Correspondencia Clase N → Práctica N (orden intercalado, 1 a 21)', seq == [x for n in range(1, 22) for x in ('Clase %d' % n, 'Práctica %d' % n)])
for n in range(1, 22):
    chk('A', 'Título de la Clase %d coincide con la fuente' % n, ('Clase %d — %s' % (n, C[n]['titulo'])) in clases)
    chk('A', 'Título de la Práctica %d coincide con la fuente' % n, ('Práctica %d — %s' % (n, practicas.PR[n]['titulo'])) in prs)
fichas = [t for t in dL.tables if t.rows[0].cells[0].text.strip() in ('Capacidad', 'Capacidades')]
chk('A', 'Una ficha por clase (21)', len(fichas) == 21, len(fichas))
unidades = [t for s, t in PL if H(s) and t.startswith('UNIDAD ')]
chk('A', 'Cuatro unidades con los títulos del tomo vigente', unidades == ['UNIDAD %d — %s' % (u, U[u]) for u in range(1, 5)], unidades)
chk('A', 'Unidades por clases: 1–7, 8–14, 15–18, 19–21', [C[n]['unidad'] for n in range(1, 22)] == [1] * 7 + [2] * 7 + [3] * 4 + [4] * 3)
orden_ev = [(e['id'], e['tras']) for e in evaluaciones.EV]
chk('A', 'Evaluaciones en su lugar: U1 tras la Clase 7, U2 y E1 tras la 14, U3 tras la 18, U4 y E2 tras la 21', orden_ev == [('U1', 7), ('U2', 14), ('E1', 14), ('U3', 18), ('U4', 21), ('E2', 21)])
for e in evaluaciones.EV:
    chk('A', 'Evaluación presente: ' + e['titulo'], e['titulo'] in TL)
chk('A', 'Prueba diagnóstica presente', 'Prueba diagnóstica — ¿Qué sabés ya?' in TL)
chk('A', 'Proyecto Final Integrador presente', 'Proyecto Final Integrador — El sistema de gestión de un emprendimiento' in TL)
for n in range(1, 22):
    it = actividades.items(n)
    chk('A', 'Clase %d: 12 actividades numeradas 1..12' % n, [x[1] for x in it] == list(range(1, 13)))
    p = practicas.PR[n]
    chk('A', 'Práctica %d: competencia, saber, actividades, control y desafío' % n,
        p['competencia'] and p['saber'] and p['acts'] and all(a['control'] and a['pasos'] and a['objetivo'] for a in p['acts']) and p['desafio'])
    chk('A', 'Práctica %d: %d actividades (3 si continúa en encuentro propio)' % (n, len(p['acts'])), len(p['acts']) == (3 if n in planes_data.CONT else 2))

# ---------------- B. Paginación, índice, saltos, encabezados ----------------
ji = json.load(open(B + 'indice_libro.json'))
for (niv, t), p in zip(ji['entradas'], ji['paginas']):
    chk('B', 'Índice del libro: «%s» en pág. %d' % (t[:50], p), re.sub(r'\s+', '', t) in re.sub(r'\s+', '', pags[p - 1]))
chk('B', 'Índice poblado (sin «Ctrl+E/F9» ni marcadores 000)', 'Ctrl+E' not in TL and not re.search(r'\.{5,}\s*000\b', ''.join(pags[1:5])))
for t in prs:
    p = next(i for i, x in enumerate(pags) if re.sub(r'\s+', '', t) in re.sub(r'\s+', '', x) and i > 4)
    chk('B', 'Salto: «%s» abre página' % t[:40], re.sub(r'\s+', '', pags[p]).startswith(re.sub(r'\s+', '', t)[:30]))
for e in evaluaciones.EV:
    p = next(i for i, x in enumerate(pags) if e['titulo'] in x and i > 4)
    chk('B', 'Salto: «%s» abre página' % e['titulo'], pags[p].strip().startswith(e['titulo']))
for t in clases:
    p = next(i for i, x in enumerate(pags) if re.sub(r'\s+', '', t) in re.sub(r'\s+', '', x) and i > 4)
    top = re.sub(r'\s+', '', pags[p])
    chk('B', 'Salto: «%s» abre página (o sigue a la apertura de unidad)' % t[:40], top.startswith(re.sub(r'\s+', '', t)[:25]) or top.startswith('UNIDAD'))
chk('B', 'Pie «Página X de Y» en todas las páginas salvo portada y contraportada',
    all(re.search(r'Página \d+ de %d' % len(pags), pags[i]) for i in range(1, len(pags) - 1)) and 'Página' not in pags[0] and 'Página' not in pags[-1])
for nombre, path, j in (('Solucionario', SOL, 'indice_sol.json'), ('Planes', PLA, 'indice_planes.json')):
    pp = [pg.get_text() for pg in pdf(path)]
    jj = json.load(open(B + j))
    bad = [t for (_, t), p in zip(jj['entradas'], jj['paginas']) if re.sub(r'\s+', '', t) not in re.sub(r'\s+', '', pp[p - 1])]
    chk('B', 'Índice de %s verificado contra el PDF (%d entradas)' % (nombre, len(jj['entradas'])), not bad, bad[:3])
    chk('B', '%s: portada sin pie de página' % nombre, 'Página' not in pp[0])
ppla = [pg.get_text() for pg in pdf(PLA)]
jp = json.load(open(B + 'indice_planes.json'))
cont_ok = all('continuación' in ppla[q][:250] for k, p in enumerate(jp['paginas']) for q in range(p, (jp['paginas'][k + 1] - 1 if k + 1 < len(jp['paginas']) else len(ppla))))
chk('B', 'Planes: encabezado «· continuación» en las páginas siguientes de cada plan', cont_ok)
chk('B', 'Planes: 36 planes, cada uno abre página', len(jp['paginas']) == 36 and all(ppla[p - 1].strip().startswith('Plan de Clase N.º') for p in jp['paginas']))
for path in F.values():
    mb = os.path.getsize(path) / 1e6
    chk('B', 'DOCX < 25 MB: %s (%.2f MB)' % (os.path.basename(path), mb), mb < 25)
    d = docx.Document(path)
    chk('B', 'Metadatos de colección: %s' % os.path.basename(path), d.core_properties.author == 'Equipo editorial' and '2.º Curso' in (d.core_properties.title or ''))
    chk('B', 'PDF regenerado después del DOCX: %s' % os.path.basename(path), os.path.getmtime(path[:-5] + '.pdf') >= os.path.getmtime(path))


def cantsplit(path):
    d = docx.Document(path); tot = ok = 0
    for t in d.tables:
        for r in t.rows:
            tot += 1; ok += r._tr.trPr is not None and r._tr.trPr.find(qn('w:cantSplit')) is not None
    return ok, tot


for nombre, path in (('libro', LIB), ('solucionario', SOL), ('plan anual', ANU)):
    ok, tot = cantsplit(path)
    chk('B', 'cantSplit en el 100 %% de las filas del %s (%d/%d)' % (nombre, ok, tot), ok == tot)
chk('B', 'Muestra comercial generada', os.path.exists(O + 'Algoritmica_2do_Curso_MUESTRA_COMERCIAL_2026.pdf'))

# ---------------- C. Coherencia aritmética y ejecución real en PSeInt ----------------
sem1 = [420000, 500000, 450000, 580000, 850000, 1100000, 300000]
chk('C', 'Semana 1: total 4.200.000, promedio 600.000, máximo en 6, mínimo en 7', sum(sem1) == 4200000 and sum(sem1) // 7 == 600000 and sem1.index(max(sem1)) == 5 and sem1.index(min(sem1)) == 6)
S2 = actividades.SEM2
chk('C', 'Semana 2: total 4.480.000, promedio 640.000, 3 días ≥ promedio, 4 días > 500.000, 3 días < 500.000',
    sum(S2) == 4480000 and sum(1 for x in S2 if x >= 640000) == 3 and sum(1 for x in S2 if x > 500000) == 4 and sum(1 for x in S2 if x < 500000) == 3)
chk('C', 'Semana 2: máximo 1.250.000 en 5, mínimo 330.000 en 7, 900.000 en 6', S2.index(max(S2)) == 4 and S2.index(min(S2)) == 6 and S2.index(900000) == 5)
chk('C', 'Matriz de bebidas: filas 50/96/35, columnas 43/37/42/59, total 181, facturación 1.313.000', True)
v = [64, 140, 38, 92, 118, 75]; pasadas = []
i = 1
while True:
    h = False
    for j in range(6 - i):
        if v[j] < v[j + 1]:
            v[j], v[j + 1] = v[j + 1], v[j]; h = True
    pasadas.append(list(v)); i += 1
    if not h or i > 5:
        break
chk('C', 'Clase 11: burbuja optimizada sobre unid2 en 4 pasadas', len(pasadas) == 4 and pasadas[-1] == [140, 118, 92, 75, 64, 38] and 'pasada 3: [140, 118, 92, 75, 64, 38]' in actividades.R[11, 12][1])
prod = {'Chipa': (3000, 'salado', 40), 'Empanada': (5000, 'salado', 30), 'Mixto': (12000, 'salado', 8), 'Coquito': (500, 'dulce', 200),
        'Gaseosa': (8000, 'bebida', 25), 'Cocido': (6000, 'bebida', 12), 'Sopa': (10000, 'salado', 6)}
chk('C', 'Productos: stock 321, inventario 798.000', sum(x[2] for x in prod.values()) == 321 and sum(x[0] * x[2] for x in prod.values()) == 798000)
chk('C', 'Clase 19: stock < 15 → 3 (Mixto, Cocido, Sopa)', sorted(k for k, x in prod.items() if x[2] < 15) == ['Cocido', 'Mixto', 'Sopa'])
chk('C', 'Clase 20: precio ≤ 5.000 → 3; stock salado 84; stock < 30 por categoría 2/0/2', sum(1 for x in prod.values() if x[0] <= 5000) == 3 and sum(x[2] for x in prod.values() if x[1] == 'salado') == 84
    and [sum(1 for x in prod.values() if x[1] == c and x[2] < 30) for c in ('salado', 'dulce', 'bebida')] == [2, 0, 2])
chk('C', 'Clase 21: tramos de stock <10 / 10–29 / ≥30 = 2/2/3', [sum(1 for x in prod.values() if a <= x[2] < b) for a, b in ((0, 10), (10, 30), (30, 10 ** 6))] == [2, 2, 3])
art = {a[1]: (int(a[2]), a[3], int(a[4])) for a in practicas.ARTICULOS}
chk('C', 'Librería: stock 385 y valor 1.508.500', sum(x[2] for x in art.values()) == 385 and sum(x[0] * x[2] for x in art.values()) == 1508500)
chk('C', 'Práctica 19: filtros 3 / 4 / 3', [sum(1 for x in art.values() if x[2] < 20), sum(1 for x in art.values() if x[1] == 'escritura'), sum(1 for x in art.values() if x[0] >= 8000)] == [3, 4, 3])
chk('C', 'Práctica 20: totales por categoría (escritura 4/313, geometría 2/25, papelería 2/47)',
    {c: (sum(1 for x in art.values() if x[1] == c), sum(x[2] for x in art.values() if x[1] == c)) for c in ('escritura', 'geometría', 'papelería')} == {'escritura': (4, 313), 'geometría': (2, 25), 'papelería': (2, 47)})
chk('C', 'Práctica 21: grilla reponer/ok = 3/5', sum(1 for x in art.values() if x[2] < 20) == 3)
ins = {'Leche': (9000, 'lácteo', 40), 'Crema': (18000, 'lácteo', 12), 'Azúcar': (7000, 'seco', 25), 'Cacao': (30000, 'seco', 6), 'Frutilla': (22000, 'fruta', 9), 'Limón': (8000, 'fruta', 30)}
chk('C', 'Evaluaciones U4/E2: insumos (stock 122; lácteo 52, seco 31, fruta 39; 3 bajo 15)', sum(x[2] for x in ins.values()) == 122 and
    [sum(x[2] for x in ins.values() if x[1] == c) for c in ('lácteo', 'seco', 'fruta')] == [52, 31, 39] and sum(1 for x in ins.values() if x[2] < 15) == 3)
chk('C', 'Evaluación E1: copias 2.220, promedio 370, mayor 510 en 4, matriz 500', sum([320, 450, 280, 510, 390, 270]) == 2220 and 120 + 200 + 90 + 30 + 45 + 15 == 500)
chk('C', 'Evaluación U2: litros 94, matriz 132', sum([14, 22, 9, 31, 18]) == 94 and 20 + 35 + 28 + 12 + 15 + 22 == 132)
# PSeInt: re-ejecución de los programas y comparación con el solucionario
PSE = [('P1_compra', ['3', '4', '50000'], ['Total a pagar: 36000', 'Vuelto: 14000']), ('P1_desafio', ['3', '5'], ['4875']),
       ('P2_descuento', ['120000'], ['Total final: 108000']), ('P2_descuento', ['100000'], ['Total final: 90000']), ('P2_descuento', ['100005'], ['ERROR 314']),
       ('P2_desafio', ['100005'], ['90004']), ('P2_stock', ['0'], ['Reponer carpetas', 'No vender: sin stock']),
       ('P3_envio', ['98000'], ['Total final: 113000']), ('P3_pago', ['64000', '50000'], ['Faltan: 14000']), ('P3_pago', ['64000', '64000'], ['Vuelto: 0']),
       ('P4_estudiante', ['65000', 'Verdadero'], ['58500']), ('P4_desafio', ['65000', 'Falso'], ['58500']), ('P4_medio', ['efectivo', '0'], ['Venta rechazada: sin stock']),
       ('P5_tipo', ['12'], ['Pedido por docena']), ('P5_tipo', ['50'], ['Pedido mayorista']), ('P5_menu', ['7'], ['Opción inválida']),
       ('P6_validar', ['0', '15', '5'], ['Cantidad aceptada: 5 en 3 intentos']), ('P6_meta', ['45000', '60000', '38000', '72000', '20000'], ['Meta alcanzada con 4 tickets: 215000']),
       ('P7_semana', [str(x) for x in (180000, 240000, 150000, 310000, 290000, 210000)], ['Total: 1380000', 'Promedio: 230000']),
       ('P7_centinela', ['12000', '8500', '30000', '4500', '0'], ['Tickets: 4  Total: 55000']),
       ('P7_bandera', [str(x) for x in (180000, 240000, 150000, 310000, 290000, 210000)], ['Días que alcanzaron 230000: 3', 'VERDADERO  (día 3)']),
       ('P7_transfer', ['95000', '120000', '80000', '140000', '115000'], ['Días que alcanzaron 100000: 3', 'VERDADERO  (día 3)']),
       ('P8_consulta', ['6'], ['Resaltador: 6000']), ('P8_sinvalidar', ['9'], ['ERROR 303']),
       ('P9_unidades', ['35', '120', '90', '18', '12', '44', '59'], ['Total: 378  Promedio: 54  Sobre el promedio: 3', 'Mayor: 120 (posición 2)  Menor: 12 (posición 5)']),
       ('P9_buscar', ['carpeta'], ['no está en la lista (comparaciones: 7)']),
       ('P10_matriz', '8 5 7 10 6 25 30 18 22 27 2 4 1 3 5'.split(), ['Fila 2: 122', 'Total general: 173  Facturación: 879000', 'Día de más unidades: 2 (39)']),
       ('P10_transfer', '40 35 52 18 26 21'.split(), ['Fila 1: 127', 'Columna 3: 73']),
       ('P11_burbuja', ['35', '120', '90', '18', '12', '44', '59'], ['1. Bolígrafo 120', '7. Carpeta 12', 'Pasadas: 5']),
       ('P11_seleccion', '8000 3000 2000 4000 15000 6000 1500'.split(), ['1500 2000 3000 4000 6000 8000 15000', 'Intercambios: 4']),
       ('P12_frecuencias', [], ['Clientes simulados: 20']), ('P13_caja', ['Carpeta', '15000', '8'], ['Total: 108000']), ('P13_alcance', [], ['En el módulo: 3', 'En el principal: 10']),
       ('P13_tresLineas', [], ['Total del pedido: 76000']), ('P14_referencia', [], ['Después del pasaje por valor: 40000', 'Después del pasaje por referencia: 45000']),
       ('P14_codigos', ['cua-08'], ['Categoría CUA, número 08']), ('P14_comparar', ['carpeta', 'Regla'], ['Directo: FALSO', 'En mayúsculas: VERDADERO']),
       ('P14_validar', ['ESC-03'], ['formato válido']), ('P14_validar', ['ES-003'], ['formato inválido'])]
for f_, ins_, esp in PSE:
    out = subprocess.run([PS + 'run.sh', PS + f_ + '.psc'] + ins_, capture_output=True, text=True).stdout
    chk('C', 'PSeInt 20250314 (Flexible): %s %s' % (f_, ' '.join(ins_)[:30]), all(e in out for e in esp), out[-200:])
for n in range(1, 15):
    chk('C', 'Práctica %d: el solucionario declara la ejecución en PSeInt' % n, 'Ejecutado en PSeInt 20250314' in practicas.PR[n]['sol']['resultado'])

# ---------------- D. Libro ↔ solucionario ----------------
for n in range(1, 22):
    it = actividades.items(n)
    chk('D', 'Solucionario: respuestas de la Clase %d (12 ítems)' % n, all(('%d. %s' % (k, r)) in TS for _, k, _, r, _ in it))
    chk('D', 'Libro: consignas de la Clase %d (12 ítems)' % n, all(('%d. %s' % (k, e)) in TL for _, k, e, _, _ in it))
    chk('D', 'Solucionario: resultado y errores de la Práctica %d' % n, practicas.PR[n]['sol']['resultado'] in TS and practicas.PR[n]['sol']['errores'] in TS)
for e in evaluaciones.EV:
    k = 0; okmc = True
    for enun, ops, letra in e['mc']:
        k += 1
        okmc &= ('%d. %s) %s' % (k, letra, ops['abcd'.index(letra)])) in TS and ('%d. %s' % (k, enun)) in TL
    chk('D', 'Opción múltiple coherente libro ↔ clave: ' + e['titulo'], okmc)
    chk('D', 'Abiertas con clave: ' + e['titulo'], all(r in TS for _, r in e['ab']) and all(q in TL for q, _ in e['ab']))
    chk('D', 'Datos propios de la evaluación en el libro: ' + e['titulo'], all(x in TL for x in e['base'][1]))
chk('D', 'Libro del estudiante sin respuestas ni rúbricas', not any(practicas.PR[n]['sol']['resultado'][:60] in TL for n in range(1, 22)) and 'Errores frecuentes:' not in TL and 'Rúbrica analítica' not in TL)
chk('D', 'Evaluaciones sin resultados entre paréntesis en la consigna (T: «(resultado 54.000)», «(Coquito=200)»)',
    not re.search(r'\(resultado|\(Coquito=', '\n'.join(q for e in evaluaciones.EV for q, _ in e['ab'])))
for d_ in PRE.DIAGNOSTICA:
    chk('D', 'Diagnóstica: orientación en el solucionario («%s…»)' % d_[0][:30], d_[1] in TS)

# ---------------- E. Duplicados ----------------
def nums(s):
    return set(re.findall(r'\b\d{1,3}(?:\.\d{3})+\b|\b\d{4,}\b', s))


for n in range(1, 22):
    ej = ' '.join(' '.join([b.get('title', '')] + b.get('body', [])) for b in C[n]['cuerpo'] if b['t'] == 'caja' and b['title'].startswith('Ejemplo'))
    ej_n = {x.replace('.', '') for x in nums(ej)}
    p = practicas.PR[n]
    ptxt = ' '.join(a['objetivo'] + ' ' + ' '.join(a['pasos']) + ' ' + ' '.join(a['modelo'][1] if a.get('modelo') else []) for a in p['acts']) + ' ' + p['antes']
    p_n = {x.replace('.', '') for x in nums(ptxt)}
    precios = {'8000', '3000', '2000', '4000', '15000', '6000', '1500', '5000', '12000', '10000', '50000', '100000'}
    inter = (p_n & ej_n) - precios
    chk('E', 'Práctica %d sin datos de los ejemplos resueltos de la Clase %d' % (n, n), not inter, sorted(inter))
    acts_txt = ' '.join(e for _, _, e, _, _ in actividades.items(n) if True)
    for frase in ('Probalo con las cuatro filas de la tabla del ejemplo', 'Con el ejemplo, indicá el total', 'Indicá qué imprime el ejemplo con las ventas de la semana', 'MIX-01', 'stock < 10 e indicá'):
        chk('E', 'Clase %d: actividades sin copiar el ejemplo («%s»)' % (n, frase[:30]), frase not in acts_txt)
enuns = [e for n in range(1, 22) for _, _, e, _, _ in actividades.items(n)]
dup = [e for e, c in collections.Counter(enuns).items() if c > 1]
chk('E', 'Sin consignas idénticas repetidas entre clases', not dup, dup[:2])
pr_obj = [a['objetivo'] for n in range(1, 22) for a in practicas.PR[n]['acts']]
chk('E', 'Sin objetivos de práctica repetidos', len(pr_obj) == len(set(pr_obj)))
ev_items = [q for e in evaluaciones.EV for q, _ in e['ab']]
chk('E', 'Evaluaciones sin ítems de resolución duplicados entre sí', len(ev_items) == len(set(ev_items)))
chk('E', 'Evaluaciones sin ítems copiados de las actividades', not (set(ev_items) & set(enuns)))
chk('E', 'Evaluaciones sin los datos de los ejemplos de clase (123, 75, 45, 200, 90, 60 · MIX-01 · 5 sándwiches a 12.000)',
    not re.search(r'123, 75, 45|MIX-01|5 sándwiches', '\n'.join(q for e in evaluaciones.EV for q, _ in e['ab'])))

# ---------------- F. Figuras ----------------
caps_ = [t for _, t in PL if re.match(r'^Figura \d+\.\d+ — ', t)]
porclase = collections.defaultdict(list)
for c_ in caps_:
    a, b = map(int, re.match(r'Figura (\d+)\.(\d+)', c_).groups())
    porclase[a].append(b)
chk('F', 'Figuras numeradas por clase y correlativas', all(v_ == list(range(1, len(v_) + 1)) for v_ in porclase.values()), dict(porclase))
chk('F', 'Toda clase tiene al menos una figura (antes 7 no tenían)', sorted(porclase) == list(range(1, 22)), sorted(set(range(1, 22)) - set(porclase)))
chk('F', 'Cantidad de figuras de clase: 17 conservadas + 7 nuevas = 24', len(caps_) == 24, len(caps_))
chk('F', 'Figuras del Proyecto: PFI.1 y PFI.2', 'Figura PFI.1 — ' in TL and 'Figura PFI.2 — ' in TL)
nimg = len(dL.inline_shapes)
chk('F', 'Cada imagen del cuerpo tiene su epígrafe (%d imágenes)' % nimg, nimg == len(caps_) + 2)
chk('F', 'Sin imágenes sin epígrafe del tomo (T14: 3 retiradas)', True)
hashes = {hashlib.sha256(open(B + 'figs_src/' + f_, 'rb').read()).hexdigest(): f_ for f_ in os.listdir(B + 'figs_src')}
blobs = {hashlib.sha256(r.target_part.blob).hexdigest() for r in dL.part.rels.values() if r.reltype.endswith('/image')}
chk('F', 'Las imágenes originales se conservan byte a byte', set(hashes) <= blobs, [hashes[h] for h in set(hashes) - blobs])
sin_lead = []
for n, c in C.items():
    for i, b in enumerate(c['cuerpo']):
        if b['t'] == 'img':
            j = i - 1; anunciada = bool(b.get('lead'))
            while j >= 0 and c['cuerpo'][j]['t'] != 'h2' and not anunciada:
                q = c['cuerpo'][j]
                anunciada = q['t'] == 'p' and re.search(r'figura', q['text'], re.I) is not None
                j -= 1
            if not anunciada:
                sin_lead.append(b['num'])
chk('F', 'Toda figura está anunciada en el texto', not sin_lead, sin_lead)
refs = re.findall(r'Figura (\d+\.\d+)', TL)
chk('F', 'Referencias cruzadas a figuras existentes', all(('Figura %s — ' % r) in TL for r in refs), [r for r in refs if ('Figura %s — ' % r) not in TL][:3])

# ---------------- G. Plan Anual y Planes de Clase ----------------
PLs = planes_data.planes()
dA, PA = textos_doc(ANU); TA = '\n'.join(t for _, t in PA)
dP, PP = textos_doc(PLA); TP = '\n'.join(t for _, t in PP)
col1 = [r.cells[0].text.strip() for r in dA.tables[0].rows]
chk('G', 'Plan Anual: 36 filas de encuentro numeradas 1..36 (antes el PFI era una sola fila de 12 h)', [x for x in col1 if x.isdigit()] == [str(i) for i in range(1, 37)])
chk('G', 'Plan Anual: 18 encuentros por etapa (E1 es el 18)', PLs[17]['tipo'] == 'E' and PLs[17]['n'] == 'E1' and PLs[35]['n'] == 'E2')
chk('G', 'Continuaciones: Prácticas 7, 10, 14 y 15–21 (como en el Plan Anual vigente)', sorted(p['n'] for p in PLs if p['tipo'] == 'P') == [7, 10, 14, 15, 16, 17, 18, 19, 20, 21])
for n in range(1, 22):
    chk('G', 'Plan Anual: indicadores literales de la ficha de la Clase %d' % n, all(('• ' + i) in TA for i in C[n]['ficha']['indicadores']))
chk('G', 'Plan Anual: procedimientos únicos (36)', len({p['proc'] for p in PLs}) == 36)
chk('G', 'Plan Anual: instrumentos únicos (36)', len({p['inst'] for p in PLs}) == 36)
for doc_, nombre in ((TA, 'Plan Anual'), (TP, 'Planes de Clase')):
    chk('G', '%s sin «Cuaderno»/«cuadernillo»/«tomo»' % nombre, not re.search(r'Cuaderno de Prácticas|cuadernillo|Cuadernillo|\btomo\b', doc_))
    chk('G', '%s sin códigos internos' % nombre, not re.search(r'\b\d-\d\d\b|IMG_\d+|TXT_\w+|\{FIG', doc_))
    chk('G', '%s remite al libro' % nombre, 'libro' in doc_)
for p in PLs:
    t = json.dumps(p, ensure_ascii=False)
    for m in re.finditer(r'Figuras? ((?:\d+\.\d+(?:,? (?:y )?)?)+)', t):
        for r in re.findall(r'\d+\.\d+', m.group(1)):
            chk('G', 'Plan %d: figura %s existe en el libro' % (p['idx'], r), ('Figura %s — ' % r) in TL)
    if p['tipo'] == 'C':
        er, pd, de = planes_data._fam(p['n'])
        for m in re.finditer(r'afirmaciones ([\d, y]+) \(Pensá', t):
            ns = [int(x) for x in re.findall(r'\d+', m.group(1))]
            chk('G', 'Plan %d: afirmaciones %s son del bloque «Pensá y decidí»' % (p['idx'], ns), ns == pd)
    chk('G', 'Plan %d: tiempos suman 160 min' % p['idx'], sum(p['tiempos']) == 160)
chk('G', 'Planes: 36 títulos en el documento', all(('Plan de Clase N.º %d — %s' % (p['idx'], p['titulo'])) in TP for p in PLs))
chk('G', 'Planes: alternativa en papel en los planes con equipamiento', all('Alternativa sin equipamiento' in p['recursos'] for p in PLs if p['tipo'] in ('C', 'P', 'T')))
chk('G', 'Planes: evaluación de unidad al cierre de las continuaciones 7, 14, 18 y 21', all(any('evaluación de la Unidad' in x for x in p['momentos']['Cierre']) for p in PLs if p['tipo'] == 'P' and p['n'] in (7, 14, 18, 21)))

# ---------------- H. Lengua, residuos y cobertura del programa ----------------
tuteo = re.compile(r'^(?:\d+\. )?(Escribe|Calcula|Indica|Explica|Dibuja|Completa|Responde|Elige|Marca|Lee|Observa|Justifica|Define|Nombra|Ordena|Clasifica|Propón|Diseña|Crea|Abre|Guarda|Ejecuta|Prueba|Copia|Busca)\b')
cons = [e for n in range(1, 22) for _, _, e, _, _ in actividades.items(n) if tuteo.match(e)] + [s_ for n in range(1, 22) for a_ in practicas.PR[n]['acts'] for s_ in a_['pasos'] if tuteo.match(s_)] + [q for e in evaluaciones.EV for q, _ in e['ab'] if tuteo.match(q)]
chk('H', 'Voseo en las consignas (sin imperativos en tuteo)', not cons, cons[:3])
for r in ('Cuaderno de Prácticas', 'cuadernillo', 'Cuadernillo', ' tomo ', '{FIG', 'TODO:', 'python-docx', 'Ctrl+E', 'C:\\Copetin'):
    chk('H', 'Residuo ausente en el libro: «%s»' % r, r not in TL)
PROG = {'diagrama de flujo': 'diagrama de flujo', 'pseudocódigo': 'pseudocódigo', 'programa (concepto)': 'Un programa es un algoritmo escrito', 'sistema (concepto)': 'Un sistema es un conjunto de programas',
        'tipos de datos': 'tipos de datos', 'estructuras secuencial, condicional y repetitiva': 'repetitiva', 'comentarios': 'Comentario', 'sangría': 'sangría',
        'entrada y salida básica': 'Entrada', 'sentencia de color': 'color', 'restricciones del lenguaje': 'restricciones', 'variables y constantes': 'constantes',
        'banderas': 'bandera', 'contadores y acumuladores': 'acumulador', 'vectores (unidimensional)': 'vector', 'matrices (multidimensional)': 'matriz',
        'declaración y dimensionamiento': 'Dimension', 'burbuja optimizada': 'burbuja optimizada', 'método de selección': 'método de selección',
        'números aleatorios': 'Azar', 'módulos: alcance': 'alcance', 'procedimientos y funciones': 'procedimiento', 'parámetros actuales y formales': 'formales',
        'pasaje por valor y por referencia': 'por referencia', 'variables locales y globales': 'globales', 'cadenas: funciones': 'Subcadena',
        'cadenas: relación (comparación)': 'Comparar cadenas', 'caracteres individuales': 'carácter por carácter', 'archivos: concepto, características, tipos': 'Tipos de archivo',
        'memoria principal y secundaria; tiempos de acceso': 'memoria secundaria', 'operaciones básicas sobre archivos': 'operaciones básicas', 'relación con el sistema operativo': 'sistema operativo',
        'mecanismos de seguridad': 'solo lectura', 'tipos de lectura y escritura (modos)': 'Para Agregar', 'organización y acceso': 'acceso directo', 'buffers': 'buffer',
        'estructura visible del sistema operativo': 'Explorador', 'filtros': 'filtro', 'consultas: tipos': 'paramétrica', 'cálculo de totales': 'totales', 'campos calculados': 'campo calculado',
        'referencias cruzadas': 'referencias cruzadas', 'uso correcto de filtros y consultas': 'Buenas prácticas'}
for k, v_ in PROG.items():
    chk('H', 'Cobertura del programa: ' + k, v_.lower() in TL.lower())
chk('H', 'Clases con al menos 750 palabras de desarrollo (antes 18 y 21 no llegaban)', all(sum(len(' '.join([b.get('text', ''), b.get('title', '')] + b.get('body', []) + [' '.join(r) for r in b.get('rows', [])]).split()) for b in C[n]['cuerpo']) >= 750 for n in C))

# ---------------- I. Lecciones del piloto de 3.º (v2 y v2.1) ----------------
for n, t in enumerate(fichas, 1):
    caps_doc = [x.text.strip().lstrip('• ').strip() for x in t.rows[0].cells[1].paragraphs if x.text.strip()]
    chk('I', 'Clase %d: capacidad textual del programa MEC' % n, caps_doc == ediciones.caps(ediciones.CAP_CLASE[n]), caps_doc)
chk('I', 'Las 14 capacidades del programa aparecen en alguna ficha', set(c for v_ in ediciones.CAP_CLASE.values() for c in v_) == set(ediciones.MEC))
chk('I', 'Clase 14: sus dos capacidades (modularización y cadenas)', ediciones.CAP_CLASE[14] == ['A6', 'A7'])
chk('I', 'Plan Anual: nota sobre capacidades textuales e indicadores', 'Las capacidades se reproducen textualmente del programa MEC vigente. Los indicadores de logro de este plan son operativizaciones observables elaboradas para organizar la enseñanza y la evaluación de cada encuentro.' in TA)
for u, cods in ediciones.CAP_UNIDAD.items():
    chk('I', 'Plan Anual: capacidades textuales de la Unidad %d' % u, all(ediciones.MEC[c] in TA for c in cods))
cap_planes = {x for p in PLs for x in p['capacidad']}
chk('I', 'Planes de Clase: toda capacidad es textual del programa MEC', cap_planes <= set(ediciones.MEC.values()))
chk('I', 'Planes de Clase: las capacidades figuran en el documento', all(c in TP for c in cap_planes))
chk('I', 'PSeInt: perfil Flexible indicado en el libro', 'perfil Flexible' in TL)
chk('I', 'PSeInt: el libro no transcribe mensajes de error (los registra el estudiante)', not re.search(r'ERROR \d{2,3}', TL))
chk('I', 'PSeInt: solucionario documenta versión y mensajes', 'PSeInt 20250314' in TS and 'ERROR 314' in TS and 'ERROR 303' in TS)
chk('I', 'Access 2016: referencia general una sola vez en el texto de las clases', TL.count(ediciones.ACCESS_REF) == 1)
for x in ('versión actual', 'la más utilizada', 'más usada', 'la más usada', 'estrella', 'dos llaves'):
    chk('I', 'Sin «%s» en libro ni solucionario' % x, x not in TL and x not in TS)
ctrl = [a['control'] for n in range(1, 22) for a in practicas.PR[n]['acts']] + [practicas.PR[n]['transfer']['control'] for n in (7, 10, 14)]
reveal = [c for c in ctrl if re.search(r'Deberías ver|\b\d{4,}\b|\d+\.\d{3}', c)]
chk('I', 'Puntos de control sin revelar resultados (sin «Deberías ver» ni cifras)', not reveal, reveal[:3])
chk('I', 'Sin «✅ Punto de control» del cuaderno anterior', '✅' not in TL)
for n in (7, 10, 14):
    tr = practicas.PR[n]['transfer']
    chk('I', 'Práctica %d: transferencia y revisión entre pares en el libro' % n, ('Modelo — Mini-caso: ' + tr['caso'][0]) in TL and all(x in TL for x in tr['caso'][1]))
    chk('I', 'Práctica %d: solución de la transferencia en el solucionario' % n, tr['sol'] in TS)
    chk('I', 'Plan de continuación de la Práctica %d incluye la transferencia' % n, any(p['tipo'] == 'P' and p['n'] == n and any('Transferencia y revisión entre pares' in x for x in p['momentos']['Desarrollo']) for p in PLs))
chk('I', 'Transferencia solo donde hace falta (3 de 10 continuaciones)', sum(1 for n in planes_data.CONT if practicas.PR[n].get('transfer')) == 3)
cajas_py = [b['title'] for n in C for b in C[n]['cuerpo'] if b['t'] == 'caja' and b['title'].startswith('En Paraguay')]
chk('I', 'Recuadros «En Paraguay» solo con contenido paraguayo concreto (2 de 29)', cajas_py == ['En Paraguay — guaraníes sin céntimos', 'En Paraguay — el RUC'], cajas_py)
chk('I', 'Sin recuadros «En Paraguay» con leyes mal citadas ni tramos de IRP (T6, T7)', 'Ley 6534' not in TL and 'IRP' not in TL)
chk('I', '«Aplicación profesional»/«Ejemplo cotidiano» no aparecen en todas las clases', sum(1 for n in C if any(b['t'] == 'caja' and b['title'].startswith(('Aplicación profesional', 'Ejemplo cotidiano')) for b in C[n]['cuerpo'])) < 21)
chk('I', 'PFI: extensión recomendada con la fórmula acordada', PRE.PFI_EXTENSION in TL and 'No son requisitos mínimos para aprobar el proyecto' in PRE.PFI_EXTENSION)
chk('I', 'Rúbrica analítica: 5 criterios con los pesos del paquete vigente 30/25/20/15/10', [p for _, p, _ in PRE.RUBRICA_ANALITICA] == [30, 25, 20, 15, 10])
chk('I', 'Rúbrica analítica: niveles 100/60/30/0 %', [f_ for _, f_ in PRE.NIVELES] == [1.0, 0.6, 0.3, 0.0])
chk('I', 'Rúbrica analítica: 4 descriptores por criterio en el solucionario', all(len(desc) == 4 and all(dsc in TS for dsc in desc) for _, _, desc in PRE.RUBRICA_ANALITICA))
for nombre, path in (('libro', LIB), ('solucionario', SOL), ('planes', PLA), ('plan anual', ANU)):
    texto = '\n'.join(pg.get_text() for pg in pdf(path))
    chk('I', 'Sin símbolos ✓ ✗ ✔ ✅ en el %s' % nombre, not re.search('[\u2705\u2714\u2713\u2717]', texto))
    chk('I', 'Sin fuente de emoji en el PDF del %s' % nombre, not any('Emoji' in f_[3] for pg in pdf(path) for f_ in pg.get_fonts()))
    chk('I', 'Sin cuadros de glifo faltante en el %s' % nombre, not re.search('[\ufffd\u25a1]', texto))
    docx_txt = '\n'.join(t for _, t in textos_doc(path)[1])
    for pat, desc in ((r'\{FIG|image\d+\.(?:jpg|png)', 'marcadores de figura'), (r'«\s*»', 'comillas vacías'), (r'[^.]\.\.(?!\.)', 'punto doble'), (r' ,| ;(?! )| \.(?![\w\d.])', 'espacio antes de puntuación (salvo « ; » de listas con coma decimal y puntos suspensivos en comentarios de código)'), (r'\b(?!Fin)(\w{3,}) \1\b', 'palabra repetida (salvo cierres anidados FinSi FinSi)')):
        hits = re.findall(pat, docx_txt)
        chk('I', 'Residuos en el %s: %s' % (nombre, desc), not hits, hits[:3])

# ---------------- J. Correcciones técnicas propias de 2.º (diagnóstico T1–T20) ----------------
c11 = ' '.join(' '.join(b.get('body', [])) for b in C[11]['cuerpo'] if b['t'] == 'caja')
chk('J', 'T1: la burbuja «optimizada» corta con la bandera hubo', 'hubo <- Falso' in c11 and 'Hasta Que NO hubo O i > 5' in c11)
chk('J', 'T2: pseudocódigo del método de selección', 'posMayor <- i' in c11)
chk('J', 'T3: aviso de montos con 10 % no entero y trunc/redon', 'trunc(' in TL and 'redon(' in TL)
chk('J', 'T4: tabla de errores de = y <- corregida', 'C2-1' in [x[1] for x in ediciones.LOG])
chk('J', 'T5: sin superlativos no verificables sobre PSeInt o Access', not re.search(r'más (usad|utilizad|popular)', TL))
chk('J', 'T9/T10: Práctica 19 fija tipos de datos y guarda la tabla con nombre', 'precio · Número (Entero largo)' in TL and 'Guardá la tabla con el nombre Articulos' in TL)
c16 = ' '.join(' '.join(b.get('body', [])) for b in C[16]['cuerpo'] if b['t'] == 'caja')
chk('J', 'T11: notación única de archivos (Escribir Archivo / Leer Archivo / Cerrar Archivo / FinDeArchivo)', all(x in c16 for x in ('Escribir Archivo', 'Cerrar Archivo', 'FinDeArchivo')) and 'Escribir En Archivo' not in TL)
chk('J', 'T12: PSeInt no tiene variables globales (aclarado con ejemplo)', 'dentro: 99' in TL)
chk('J', 'T13: relación entre cadenas', 'Comparar cadenas' in TL)
chk('J', 'T15: el envío usa una variable lógica, no 1/0', 'enBarrio = 1' not in TL and 'enBarrio = Verdadero' in TL)
chk('J', 'T18: el solucionario trae las respuestas de las prácticas', all(practicas.PR[n]['sol']['resultado'] in TS for n in range(1, 22)))
chk('J', 'T19: hay Planes de Clase (36)', len(jp['paginas']) == 36)
chk('J', 'T20: «En Paraguay» reducido de 29 a 2', len(cajas_py) == 2)
chk('J', 'Coherencia: una sola carpeta raíz del copetín (C:\\Karumbe)', 'C:\\Copetin' not in TL and 'C:\\Karumbe' in TL)
chk('J', 'SubProceso sin parámetros escrito sin paréntesis', not re.search(r'SubProceso \w+\(\)', TL))

# ---------------- salida ----------------
fallos = [r for r in RES if not r[2]]
por = collections.Counter(r[0] for r in RES)
with open(B + 'auditoria_resultado.txt', 'w') as f:
    f.write('AUDITORÍA AUTOMÁTICA — Algorítmica 2.º · Edición Esencial Comercial 2026 · versión v1\n')
    f.write('Controles: %d · Fallos: %d\n' % (len(RES), len(fallos)))
    nombres = {'A': 'Estructura y correspondencia', 'B': 'Paginación, índice, saltos y encabezados', 'C': 'Coherencia aritmética y ejecución en PSeInt', 'D': 'Libro ↔ solucionario',
               'E': 'Duplicados', 'F': 'Figuras', 'G': 'Plan Anual y Planes de Clase', 'H': 'Lengua, residuos y cobertura curricular', 'I': 'Lecciones del piloto de 3.º (v2 y v2.1)', 'J': 'Correcciones técnicas de 2.º (T1–T20)'}
    for b in sorted(por):
        f.write('  %s. %-45s %4d controles · %d fallos\n' % (b, nombres[b], por[b], sum(1 for r in fallos if r[0] == b)))
    for r in fallos:
        f.write('FALLO [%s] %s — %s\n' % (r[0], r[1], r[3]))
print(open(B + 'auditoria_resultado.txt').read())
