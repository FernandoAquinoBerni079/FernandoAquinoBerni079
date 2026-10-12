import docx,re,sys
from indice import pages,norm
def chk(dx,pdf):
    P=[norm(t) for t in pages(pdf)]; d=docx.Document(dx); bad=[]
    tocs=[p for p in d.paragraphs if p.style.name.lower().startswith(('toc','tdc'))]
    ents=[]
    for p in tocs:
        m=re.match(r'(.*?)\t?\s*(\d+)\s*$',p.text)
        if m: ents.append((norm(m.group(1)),int(m.group(2))))
    last=ents[-1][0]; ini=next(i for i,t in enumerate(P) if last in t)+1
    for title,num in ents:
        alt=[title]+[norm('evaluación integradora · %s etapa'%m.group(1)) for m in [re.match(r'evaluación integradora de la (\S+) etapa',title)] if m]
        found=next((i+1 for i in range(ini,len(P)) if any(a in P[i] for a in alt)),None)
        if found!=num: bad.append((title[:55],num,found))
    print(dx.split('/')[-1][38:],'índice termina p',ini,'entradas',len(ents),'difieren',len(bad)); [print('  ',b) for b in bad]
for f in sys.argv[1:]: chk(f,f.replace('.docx','.pdf'))
