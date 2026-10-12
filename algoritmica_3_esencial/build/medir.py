import re,sys
L=open(sys.argv[1]).read().split('\n')
cl=None;data={};act=False;ficha=0
for l in L:
    m=re.match(r'\[Heading 1\] Clase (\d+)',l)
    if m: cl=int(m.group(1));data[cl]=[0,0,0,0];act=False;ficha=3;continue
    if l.startswith('[Heading 1]'): cl=None;continue
    if cl is None: continue
    if 'Actividades de aplicación' in l: act=True;continue
    if 'EVALUACIÓN' in l: cl=None;continue
    if ficha and l.startswith('  |'): ficha-=1; continue
    t=re.sub(r'^\s*\[[^\]]*\]\s*|^\s*\|\s*','',l)
    w=len(re.findall(r'\w+',t))
    if act: 
        if re.match(r'\d+\.',t.strip()): data[cl][2]+=1
        data[cl][1]+=w
    else: data[cl][0]+=w
    if t.startswith('Figura'): data[cl][3]+=1
tot=0
for k,v in data.items(): print(f"Clase {k:2d}: desarrollo {v[0]:5d} palabras · actividades {v[1]:4d} palabras / {v[2]} ítems · figuras {v[3]}"); tot+=v[0]
print('mín',min(v[0] for v in data.values()),'máx',max(v[0] for v in data.values()),'total',tot)
