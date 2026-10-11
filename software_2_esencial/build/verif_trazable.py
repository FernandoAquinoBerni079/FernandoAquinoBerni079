# -*- coding: utf-8 -*-
"""Matriz trazable de respuestas numéricas: lee los datos del enunciado en src_md, recalcula y busca el
resultado en el solucionario (sol.md). Devuelve filas (ítem, datos, operación, resultado, ¿está en la clave?)."""
import re, math
S = '/home/claude/sw2/src_md/'
leer = lambda f: open(S + f).read()
SOL = leer('sol.md')
g = lambda x: ('{:,.0f}'.format(x)).replace(',', '.')
def dec(x, n=1):
    return ('%.*f' % (n, x)).replace('.', ',')
def num(t):
    return float(t.replace('.', '').replace(',', '.'))
FILAS = []
def seccion(titulo):
    """Texto de la clave limitado a la sección «## titulo…» (hasta la siguiente sección ##)."""
    m = re.search(r'^## ' + re.escape(titulo) + r'.*?(?=^## |\Z)', SOL, re.M | re.S)
    assert m, titulo
    return m.group(0)
def sec_de(item):
    if item.startswith('Ficha E'): return 'Ficha E'
    m = re.match(r'Práctica (\d+)', item)
    if m: return 'Clase %s ' % m.group(1)
    if item.startswith('Caso 1'): return 'Evaluación integradora de la 1.ª etapa'
    if item.startswith('Caso 2'): return 'Evaluación integradora de la 2.ª etapa'
    raise KeyError(item)
def fila(item, datos, op, res, buscar):
    zona = seccion(sec_de(item))
    FILAS.append((item, datos, op, res, all(b in zona for b in buscar), buscar))

# Ficha E
t = leer('lab_ficha_E.md')
cap = float(re.search(r'HDD de (\d+) TB usado al (\d+) %', t).group(1)); pct = float(re.search(r'usado al (\d+) %', t).group(1))
usados = cap * 1000 * pct / 100; minimo = usados / 0.8
fila('Ficha E', '%g TB al %g %%' % (cap, pct), 'usados ÷ 0,80', '%s GB' % dec(minimo), [g(usados) + ' GB', dec(minimo).rstrip('0').rstrip(','), 'no cumple'])
# Práctica 2
t = leer('lab_practica02.md')
casos = re.findall(r'(\d+,\d+) V en la (?:línea )?de \+(\d+(?:,\d)?)', t)
for med, nom in casos:
    m, n = num(med), num(nom)
    okk = n * 0.95 <= m <= n * 1.05
    fila('Práctica 2 · %s V en +%s' % (med, nom), 'rango ±5 %', '%s ≤ m ≤ %s' % (dec(n * .95, 3), dec(n * 1.05, 3)), 'SÍ' if okk else 'NO', ['%s V en +%s → %s' % (med, nom, 'SÍ' if okk else 'NO')])
# Práctica 4
t = leer('lab_practica04.md')
carr = [int(x) for x in re.findall(r'x(\d+) \(\d+\)', t)]
fila('Práctica 4 · PCIe 3.0', 'carriles %s' % carr, 'carriles × 1', ' / '.join(str(c) for c in carr), [' / '.join(str(c) for c in carr) + ' GB/s'])
fila('Práctica 4 · PCIe 5.0', 'carriles %s' % carr, 'carriles × 4', ' / '.join(str(4 * c) for c in carr), [' / '.join(str(4 * c) for c in carr) + ' GB/s'])
# Práctica 9
t = leer('lab_practica09.md')
gb = float(re.search(r'archivo institucional de (\d+) GB', t).group(1))
for nombre, capf, vel in re.findall(r'(CD|DVD|Blu-ray) \((\d+(?:,\d+)?) GB; (\d+(?:,\d+)?) MB/s\)', t):
    discos = math.ceil(gb / num(capf)); horas = gb * 1000 / num(vel) / 3600
    fila('Práctica 9 · %s' % nombre, '%g GB; %s GB; %s MB/s' % (gb, capf, vel), 'techo(GB/cap) y GB·1000/vel/3600', '%d discos; %s h' % (discos, dec(horas)),
         ['%s %d discos y ≈ %s h' % (nombre, discos, dec(horas))])
# Práctica 10
t = leer('lab_practica10.md')
m = re.search(r'Precio del equipo \(([\d.]+) / ([\d.]+)\), Precio del insumo \(([\d.]+) / ([\d.]+)\), Rendimiento en páginas \(([\d.]+) / ([\d.]+)\).*?Costo de ([\d.]+) páginas', t)
eqA, eqB, inA, inB, rA, rB, pm = [num(x) for x in m.groups()]
cA, cB = inA / rA, inB / rB
fila('Práctica 10', 'insumos y rendimientos', 'insumo ÷ rendimiento; × %s' % g(pm), 'G. %s / G. %s; mensual G. %s / G. %s' % (g(cA), g(cB), g(cA * pm), g(cB * pm)),
     ['G. %s (inyección)' % g(cA), 'G. %s (láser)' % g(cB), 'G. %s vs. G. %s' % (g(cA * pm), g(cB * pm)), dec((eqB - eqA) / (cA * pm - cB * pm))])
# Clase 10 (ejemplo resuelto: se verifica contra el propio libro)
t = leer('tomo_clase10.md')
pa = num(re.search(r'\(([\d.]+) por año\)', t).group(1))
(eA, bA, rdA), (eB, bB, rdB) = [[num(x) for x in re.search(r'Impresora ' + k + r',[^\n]*?equipo G\. ([\d.]+); [^\n]*?G\. ([\d.]+) que rinde ([\d.]+) páginas', t).groups()] for k in 'AB']
for et, txt in (('uso A', g(pa * bA / rdA)), ('uso B', g(pa * bB / rdB)), ('año A', g(eA + pa * bA / rdA)), ('año B', g(eB + pa * bB / rdB)),
                ('caja A', g(eA + math.ceil(pa / rdA) * bA)), ('caja B', g(eB + math.ceil(pa / rdB) * bB))):
    FILAS.append(('Clase 10 · ' + et, 'ejemplo de la biblioteca', 'sin redondeo previo', 'G. ' + txt, ('G. ' + txt) in t, ['(libro) G. ' + txt]))
# Práctica 15 / 16 / 19
t = leer('lab_practica16.md')
tend = [int(x) for x in re.search(r'tendidos de ([\d, y]+) metros', t).group(1).replace(' y ', ', ').split(', ')]
fila('Práctica 16 · cable', str(tend), 'suma × 1,1', '%d m; %s m' % (sum(tend), dec(sum(tend) * 1.1)), ['%d m' % sum(tend), dec(sum(tend) * 1.1)])
fila('Práctica 16 · patch cords', '%d puntos' % len(tend), 'puntos × 2 + 1', str(len(tend) * 2 + 1), ['%d × 2 + 1 = %d' % (len(tend), len(tend) * 2 + 1)])
bocas = 6 + 1 + 1 + 1
fila('Práctica 15 · bocas', '6 PC + impresora + AP + router', 'techo(bocas × 1,2)', '%d; %d' % (bocas, math.ceil(bocas * 1.2)), ['= %d' % bocas, '→ %d' % math.ceil(bocas * 1.2)])
t = leer('lab_practica19.md')
t19 = [int(x) for x in re.search(r'ocho puntos de ([\d, y]+) metros', t).group(1).replace(' y ', ', ').split(', ')]
can = [x + 5 for x in t19]
fila('Práctica 19 · canales', str(t19), 'tendido + 5', ', '.join(map(str, can)), [', '.join(map(str, can[:-1])) + ' y %d m' % can[-1], '100 − %d = %d m' % (max(can), 100 - max(can))])
can20 = [x + 5 for x in tend]
fila('Práctica 20 · canales del local', 'tendidos de la Práctica 16: %s' % tend, 'tendido + 5 (procedimiento de la Práctica 19)', ', '.join(map(str, can20)),
     [', '.join(map(str, can20[:-1])) + ' y %d m' % can20[-1], 'no se usa la tabla de la segunda sucursal'])
# Caso 1 y Caso 2
t = leer('tomo_caso1.md')
pr = [num(x) for x in re.findall(r'G\. ([\d.]+)\)', t)]
fila('Caso 1', 'precios %s' % len(pr), 'suma; × 10', 'G. %s; G. %s' % (g(sum(pr)), g(sum(pr) * 10)), [g(sum(pr)), g(sum(pr) * 10)])
fila('Caso 2 · bocas', '13 PC + impresora + 2 AP + router', 'suma', '17', ['= 17 bocas'])
fila('Caso 2 · canal', '47 + 3 + 2', 'suma; 100 − canal', '52 m; 48 m', ['47 + 3 + 2 = 52 m', '48 m de margen'])
