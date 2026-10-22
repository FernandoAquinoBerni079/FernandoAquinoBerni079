"""Coteja las claves de opción múltiple y de completar/VF del solucionario con el tomo (por sección y número)."""
import re, sys
def secciones_tomo(lineas):
    sec = None; preg = {}; opc = {}; cur = None
    for l in lineas:
        m = re.match(r'\{Heading 2\} (Clase \d+)', l)
        if m: sec = m.group(1); continue
        m = re.match(r'(Evaluación de la (?:Unidad \d|Etapa \d))', l)
        if m and not l.startswith('{'): sec = m.group(1); continue
        if l.startswith('{Heading 1}'): 
            if 'Unidad' not in l: pass
        m = re.match(r'(\d\.\d) (.*)', l)
        if m and sec: cur = (sec, m.group(1)); preg[cur] = m.group(2); opc[cur] = {}; continue
        m = re.match(r'([a-d])\) (.*)', l)
        if m and cur: opc[cur][m.group(1)] = m.group(2)
    return preg, opc
def claves_sol(lineas):
    sec = None; k = {}
    for l in lineas:
        m = re.match(r'\{Heading 2\} (Clase \d+|Evaluación de la (?:Unidad \d|Etapa \d))', l)
        if m: sec = m.group(1); continue
        m = re.match(r'(\d\.\d) (.*)', l)
        if m and sec: k[(sec, m.group(1))] = m.group(2)
    return k
t = open(sys.argv[1]).read().split('\n'); s = open(sys.argv[2]).read().split('\n')
preg, opc = secciones_tomo(t); k = claves_sol(s)
nmc = 0; prob = []
for key, ops in opc.items():
    if not ops: continue
    nmc += 1
    clave = k.get(key)
    if not clave: prob.append(('SIN CLAVE', key)); continue
    m = re.match(r'([a-d])\) (.*)', clave)
    if not m: prob.append(('CLAVE NO LETRA', key, clave)); continue
    letra, txt = m.groups()
    if ops.get(letra, '').strip() != txt.strip():
        prob.append(('TEXTO DISTINTO', key, letra, ops.get(letra), '| sol:', txt))
# distribución de letras
from collections import Counter
dist = Counter(re.match(r'([a-d])', k[key]).group(1) for key, ops in opc.items() if ops and key in k and re.match(r'[a-d]\)', k[key]))
# preguntas sin opciones (completar/VF/abiertas) sin clave
falt = [key for key in preg if key not in k]
print('MC:', nmc, 'distribución', dict(dist)); print('preguntas totales', len(preg), 'sin clave', falt)
for p in prob: print(p)
