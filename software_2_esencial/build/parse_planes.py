import docx,re,json
from docx.oxml.ns import qn
d=docx.Document('/home/claude/sw2/src/GabineteSoftware_2do_Curso_PLANES_DE_CLASE.docx')
T=d.tables
def cells(t):
    out=[]
    for r in t.rows:
        seen=set(); cs=[]
        for c in r.cells:
            if id(c._tc) in seen: continue
            seen.add(id(c._tc)); cs.append([p.text for p in c.paragraphs if p.text.strip()])
        out.append(cs)
    return out
PL=[]; i=1
while i<len(T):
    h=cells(T[i])
    m=re.search(r'Plan de Clase N\.º (\d+) de 36',' '.join(h[0][0]))
    if not m: i+=1; continue
    n=int(m.group(1))
    dat=cells(T[i+1]); ci=cells(T[i+2]); mo=cells(T[i+3]); rec=cells(T[i+4]); ev=cells(T[i+5])
    bul=lambda xs:[x.lstrip('• ').strip() for x in xs]
    p=dict(idx=n, unidad=dat[2][1][0], material=dat[3][1][0], tema=' '.join(dat[4][1]),
           capacidad=ci[0][1], indicadores=bul(ci[1][1]),
           momentos={mo[k][0][0]:bul(mo[k][1]) for k in (1,2,3)}, tiempos=[int(re.search(r'\d+',mo[k][2][0]).group()) for k in (1,2,3)],
           recursos=' '.join(rec[0][1]), proc=' '.join(ev[1][1]), inst=' '.join(ev[2][1]), criterios=bul(ev[3][1]))
    PL.append(p); i+=6
# títulos desde los párrafos «Plan de Clase N.º k — título» si existen
print(len(PL), [p['idx'] for p in PL][:5], PL[0]['tiempos'])
json.dump(PL,open('/home/claude/sw2/build/planes_orig.json','w'),ensure_ascii=False,indent=0)
