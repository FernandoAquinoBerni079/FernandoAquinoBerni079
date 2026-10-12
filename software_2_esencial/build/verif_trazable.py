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
def bloque_de(item):
    """Respuesta exacta del ítem en la clave: (rótulo del destino, texto)."""
    if item.startswith('Ficha E'):
        return '## Ficha E (sección completa)', seccion('Ficha E')
    m = re.match(r'Práctica (\d+)', item)
    if m:
        rot = 'Práctica %s — Resultado esperado' % m.group(1)
        b = re.findall(r'^' + re.escape(rot) + r'.*$', SOL, re.M)
        assert len(b) == 1, rot
        return rot, b[0]
    m = re.match(r'Caso ([12])', item)
    if m:
        sec = seccion('Evaluación integradora de la %s.ª etapa' % m.group(1))
        b = re.findall(r'^Desarrollo del caso:.*$', sec, re.M)
        assert len(b) == 1, item
        return 'Integradora %s.ª etapa · Desarrollo del caso' % m.group(1), b[0]
    raise KeyError(item)
def fila(item, datos, op, res, buscar):
    rot, zona = bloque_de(item)
    FILAS.append((item, datos, op, res, all(b in zona for b in buscar), buscar, rot))

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
    FILAS.append(('Clase 10 · ' + et, 'ejemplo de la biblioteca', 'sin redondeo previo', 'G. ' + txt, ('G. ' + txt) in t, ['(libro) G. ' + txt], 'Libro, Clase 10 (ejemplo resuelto)'))
# Clase 16 y Clase 19 (ejemplos resueltos: se rehacen con los datos del propio enunciado)
t = leer('tomo_clase16.md')
t16 = [int(x) for x in re.search(r'Los tendidos medidos en el plano son de ([\d, y]+) metros', t).group(1).replace(' y ', ', ').split(', ')]
FILAS.append(('Clase 16 · cable', str(t16), 'suma × 1,1', '%d m; ≈ %d m' % (sum(t16), round(sum(t16) * 1.1)), ('= %d m' % sum(t16)) in t and ('unos %d m' % round(sum(t16) * 1.1)) in t, ['(libro) %d m' % sum(t16)], 'Libro, Clase 16 (ejemplo resuelto)'))
t = leer('tomo_clase19.md')
pts = [int(x) for x in re.findall(r'punto \d, (\d+) m', t)]
cp, cr = [int(x) for x in re.search(r'cordones de (\d+) m en el puesto y de (\d+) m en el rack', t).groups()]
for k, f in enumerate(pts, 1):
    c = f + cp + cr; okk = f <= 90 and c <= 100
    enc = ('(%d m)' % c in t or '= %d m' % c in t) and (('Paso %d' % k) in t) and (('No cumple' in t) if not okk else True)
    FILAS.append(('Clase 19 · punto %d' % k, '%d m fijo; cordones %d + %d' % (f, cp, cr), 'fijo ≤ 90 y canal ≤ 100', '%d m; %s' % (c, 'cumple' if okk else 'no cumple'), enc, ['(libro) %d m' % c], 'Libro, Clase 19 (ejemplo resuelto)'))
# Práctica 15 / 16 / 19
t = leer('lab_practica16.md')
tend = [int(x) for x in re.search(r'tendidos de ([\d, y]+) metros', t).group(1).replace(' y ', ', ').split(', ')]
fila('Práctica 16 · cable', str(tend), 'suma × 1,1', '%d m; %s m' % (sum(tend), dec(sum(tend) * 1.1)), ['%d m' % sum(tend), dec(sum(tend) * 1.1)])
fila('Práctica 16 · patch cords', '%d puntos' % len(tend), 'puntos × 2 + 1', str(len(tend) * 2 + 1), ['%d × 2 + 1 = %d' % (len(tend), len(tend) * 2 + 1)])
t = leer('lab_practica15.md')
pc, imp, ap = [int(x) for x in re.search(r'\((\d+) computadoras, (\d+) impresora de red, (\d+) access point[^)]*y el router\)', t).groups()]
bocas = pc + imp + ap + 1
fila('Práctica 15 · bocas', '%d PC + %d impresora + %d AP + router' % (pc, imp, ap), 'techo(bocas × 1,2)', '%d; %d' % (bocas, math.ceil(bocas * 1.2)), ['= %d' % bocas, '→ %d' % math.ceil(bocas * 1.2)])
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
t = leer('tomo_caso2.md')
pc0, imp2, ap0 = [int(x) for x in re.search(r'tiene (\d+) computadoras, (\d+) impresora de red y (\d+) access point', t).groups()]
pcn = int(re.search(r'sumar al aula (\d+) computadoras y un segundo access point', t).group(1))
pcs, aps = pc0 + pcn, ap0 + 1; b2 = pcs + imp2 + aps + 1
fila('Caso 2 · bocas', '%d PC + %d impresora + %d AP + router' % (pcs, imp2, aps), 'suma', str(b2), ['%d PC + impresora + %d access points + enlace al router = %d bocas' % (pcs, aps, b2)])
fijo = int(re.search(r'a (\d+) m de tendido fijo', t).group(1))
cp, cr = [int(x) for x in re.search(r'cordones de (\d+) m en el puesto y (\d+) m en el rack', t).groups()]
canal = fijo + cp + cr
fila('Caso 2 · canal', '%d + %d + %d' % (fijo, cp, cr), 'suma; 100 − canal', '%d m; %d m' % (canal, 100 - canal), ['%d + %d + %d = %d m' % (fijo, cp, cr, canal), '%d m de margen' % (100 - canal)])
