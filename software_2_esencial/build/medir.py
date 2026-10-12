import re,sys
T=open('/home/claude/sw2/src/TOMO.txt').read().splitlines()
idx=[i for i,l in enumerate(T) if re.match(r'## Clase \d+ —',l)]
fin=len(T)
rows=[]
for k,i in enumerate(idx):
    j=idx[k+1] if k+1<len(idx) else fin
    blk=T[i:j]
    act=next(n for n,l in enumerate(blk) if l.startswith('### Actividades'))
    dev=blk[:act]
    # quitar ficha (tabla) y epígrafes
    txt=[l for l in dev[1:] if not l.startswith('|') or 'Concepto clave' in l or 'Ejemplo' in l or 'En Paraguay' in l]
    txt=[l for l in txt if not re.match(r'(Figura|Fotografía|Imagen|Ilustración) \d',l) and not l.startswith('#')]
    words=len(re.findall(r'\w+',' '.join(txt)))
    rest=blk[act:]
    # cortar en el siguiente bloque grande (#, ###) que no sea parte de actividades
    end=next((n for n,l in enumerate(rest[1:],1) if l.startswith('#')),len(rest))
    acts=len([l for l in rest[:end] if re.match(r'\d+\\?\.',l)])
    caps=[l for l in dev if re.match(r'(Figura|Fotografía|Imagen|Ilustración) \d',l)]
    flags=''.join(['C' if any('Concepto clave' in l for l in dev) else '-','E' if any('Ejemplo' in l for l in dev) else '-','P' if any('En Paraguay' in l for l in dev) else '-','T' if any(l.startswith('| :-:') for l in dev[8:]) else '-'])
    rows.append((T[i][3:60],words,acts,len(caps),flags,[c[:70] for c in caps]))
for r in rows: print(f'{r[0]:<58} {r[1]:>5} pal  {r[2]:>2} act  {r[3]} fig {r[4]}')
print()
for r in rows:
    for c in r[5]: print('  ',r[0][:8],c)
