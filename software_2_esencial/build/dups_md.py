import re,itertools,glob,os
S='/home/claude/sw2/src_md/'
B={}
for n in range(1,21):
    t=open(S+'tomo_clase%02d.md'%n).read(); i=t.index('## Actividades de aplicación')
    B['C%d-dev'%n]=t[:i]; B['C%d-act'%n]=t[i:]
    B['P%d'%n]=open(S+'lab_practica%02d.md'%n).read()
for f in glob.glob(S+'lab_ficha_*.md'): B['F'+f[-4]]=open(f).read()
for k in ['eval_u1','integ1','caso1','eval_u2','integ2','caso2','diagnostica']: B[k]=open(S+'tomo_%s.md'%k).read()
CONST={'12 V','5 V','3,3 V','5 %','4,7 GB','8,5 GB','25 GB','700 MB','100 m','90 m','10 m','2,4 GHz','5 GHz','6 GHz','150','305','220','802','568','642','255.255.255','192.168','1.000','1.024','16','24','48','12','13','11','20','80','50','95','2,4','3,5','5.400','7.200','550 MB','4,5 MB','1,385 MB','7,8 MB','22,2 MB','2 GB','4 GB','8 GB','16 GB','32 GB','10 Gb','1 Gb','1918'}
def nums(s):
    s=re.sub(r'\[\[(IMG|CAJA)[^\]]*\]\]','',s)
    s=re.sub(r'(Figura|Clase|Práctica|Ficha|Actividad|Paso|Plan|Ley|Resolución) [\dA-Z]+(\.\d+)?','',s)
    s=re.sub(r'^\s*\d+\.\s','',s,flags=re.M)
    out=set()
    for m in re.finditer(r'(?<![\w.,])(\d{1,3}(?:\.\d{3})+|\d+(?:,\d+)?)(?:\s?(GB|TB|MB|W|V|m|GHz|Mbps|Gb|GB/s|MB/s|%|ms|núcleos|hilos|puertos|PC|páginas))?',s):
        v=m.group(1)+(' '+m.group(2) if m.group(2) else '')
        if re.fullmatch(r'\d',m.group(1)) and not m.group(2): continue
        if v in CONST or m.group(1) in CONST: continue
        out.add(v)
    return out
N={k:nums(v) for k,v in B.items()}
res=[]
for a,b in itertools.combinations(sorted(N),2):
    c=N[a]&N[b]
    if len(c)>=2: res.append((len(c),a,b,sorted(c)))
for r in sorted(res,reverse=True): print(r[0],'|',r[1],'<->',r[2],'|',r[3][:10])
