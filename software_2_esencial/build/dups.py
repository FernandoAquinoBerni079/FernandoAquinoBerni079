import re,itertools,collections
T=open('/home/claude/sw2/src/TOMO.txt').read(); L=open('/home/claude/sw2/src/LAB.txt').read()
B={}
# tomo
lines=T.splitlines(); marks=[]
for i,l in enumerate(lines):
    m=re.match(r'## (Clase \d+)',l)
    if m: marks.append((i,m.group(1)+' desarrollo'))
    if l.startswith('### Actividades de aplicación'): marks.append((i,marks[-1][1].replace('desarrollo','actividades')))
    for k in ['EVALUACIÓN DE LA UNIDAD 1','EVALUACIÓN INTEGRADORA · 1.ª','Caso integrador — El presupuesto','EVALUACIÓN DE LA UNIDAD 2','EVALUACIÓN INTEGRADORA · 2.ª','Caso integrador — La red','Prueba diagnóstica']:
        if k in l and not l.startswith(('Presentación','Al final')): marks.append((i,k))
    if l.startswith('# UNIDAD 2'): marks.append((i,'(u2 intro)'))
marks.sort()
for (i,n),(j,_) in zip(marks,marks[1:]+[(len(lines),'')]):
    B.setdefault(n,'')
    B[n]+='\n'.join(lines[i:j])
for p in re.split(r'\n# ',L):
    t=p.split('\n')[0]
    if t.startswith(('Práctica','Ficha','Proyecto')): B[t.split(' —')[0]]=p
def nums(s):
    s=re.sub(r'(Figura|Fotografía|Clase|Práctica|Ficha|Actividad|Plan) [\dA-Z]+(\.\d+)?','',s)
    s=re.sub(r'^\d+\\?\.','',s,flags=re.M)
    out=set()
    for m in re.finditer(r'(?<![\w.,])(\d{1,3}(?:\.\d{3})+|\d+(?:,\d+)?)(?:\s?(GB|TB|MB|W|V|m|GHz|MHz|Mbps|Gbps|GB/s|ppm|dpi|%|ms|núcleos|hilos|puertos|PC|equipos|páginas))?',s):
        v=m.group(1)
        if v in {'1','2','3','4','5','6','7','8','9','10','0'} and not m.group(2): continue
        out.add(v+(' '+m.group(2) if m.group(2) else ''))
    return out
N={k:nums(v) for k,v in B.items()}
res=[]
for a,b in itertools.combinations(N,2):
    if a.split()[:2]==b.split()[:2]: continue  # same clase desarrollo vs actividades handled below
    c=N[a]&N[b]
    if len(c)>=3: res.append((len(c),a,b,sorted(c)))
# within clase: desarrollo vs actividades
for k in N:
    if k.endswith('desarrollo'):
        a=k.replace('desarrollo','actividades'); c=N[k]&N.get(a,set())
        if len(c)>=2: res.append((len(c),k,a,sorted(c)))
for r in sorted(res,reverse=True)[:60]: print(r[0],'|',r[1],'<->',r[2],'|',r[3][:12])
