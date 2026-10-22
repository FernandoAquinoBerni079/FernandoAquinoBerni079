"""Coteja claves del solucionario 3.º con el tomo: MC (letra y texto), cantidad de ítems B/C/D por sección."""
import re, sys, collections
def sec_de(l):
    m = re.match(r'\{Heading 2\} (Clase \d+)', l)
    if m: return m.group(1)
    m = re.match(r'(?:\{Heading 2\} )?(?:EVALUACIÓN|Evaluación) (?:DE LA|de la) (UNIDAD|Unidad|ETAPA|Etapa) (\d)', l)
    if m: return 'Eval ' + m.group(1).capitalize()[0] + m.group(2)
    return None
def tomo(lineas):
    sec=None; cur=None; mc=collections.defaultdict(dict); items=collections.defaultdict(list); bloque=None
    for l in lineas:
        s=sec_de(l)
        if s: sec=s; cur=None; continue
        if l.startswith('{Heading 1}') and sec and not l.startswith('{Heading 1} Unidad'): sec=None
        m=re.match(r'([A-D])\. ', l)
        if m and sec: bloque=m.group(1); continue
        m=re.match(r'(\d+)\. (.*)', l)
        if m and sec: cur=int(m.group(1)); items[sec].append((bloque,cur)); continue
        m=re.match(r'\s+([a-d])\) (.*)', l)
        if m and sec and cur: mc[(sec,cur)][m.group(1)]=m.group(2)
    return mc, items
def sol(lineas):
    sec=None; k={}; items=collections.defaultdict(list)
    for l in lineas:
        s=sec_de(l)
        if s: sec=s; continue
        m=re.match(r'(\d+) \| ([a-d])\) \| (.*)', l)
        if m and sec: k[(sec,int(m.group(1)))]=(m.group(2),m.group(3)); items[sec].append(int(m.group(1))); continue
        m=re.match(r'(\d+)\. ', l)
        if m and sec: items[sec].append(int(m.group(1)))
    return k, items
t=open(sys.argv[1]).read().split('\n'); s=open(sys.argv[2]).read().split('\n')
mc,it=tomo(t); k,its=sol(s)
dist=collections.Counter(); prob=[]
for key,ops in mc.items():
    if key not in k: prob.append(('sin clave',key)); continue
    L,txt=k[key]; dist[L]+=1
    if ops.get(L,'').rstrip('.').strip()!=txt.rstrip('.').strip(): prob.append(('texto',key,L,ops.get(L),txt))
for key in k:
    if key not in mc: prob.append(('clave sin pregunta',key))
for sec in it:
    a=[n for b,n in it[sec]]; b=its.get(sec,[])
    if sorted(a)!=sorted(b): prob.append(('items',sec,a,b))
print('MC:',len(mc),'distribución',dict(sorted(dist.items())),'secciones',len(it))
for p in prob: print(p)
