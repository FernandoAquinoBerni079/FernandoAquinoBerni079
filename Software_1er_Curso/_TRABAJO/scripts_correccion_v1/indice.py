import docx, subprocess, re, sys
from docx.oxml.ns import qn
T=lambda el:''.join(t.text or '' for t in el.iter(qn('w:t')))
def pages(pdf):
    n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout).group(1))
    return [subprocess.run(['pdftotext','-f',str(i),'-l',str(i),pdf,'-'],capture_output=True,text=True).stdout for i in range(1,n+1)]
norm=lambda s: re.sub(r'\s+',' ',s).strip().casefold()
def run(docx_in, pdf, docx_out):
    P=pages(pdf); d=docx.Document(docx_in)
    toc=[p for p in d.element.body.iter(qn('w:p')) if (p.find(qn('w:pPr')+'/'+qn('w:pStyle')) is not None and p.find(qn('w:pPr')+'/'+qn('w:pStyle')).get(qn('w:val')).startswith('TDC'))]
    ini=max(i for i,t in enumerate(P[:8]) if 'Índice' in t)+1
    ALIAS={'evaluación de la unidad':'evaluación de la unidad','evaluación integradora de la':'evaluación integradora'}
    cambios=0; desde=ini; filas=[]
    for p in toc:
        ts=list(p.iter(qn('w:t'))); title=''.join(t.text for t in ts[:-1]).strip(); num=ts[-1]
        key=norm(title)
        cands=[key]
        m=re.match(r'evaluación de la unidad (\d)',key)
        if m: cands.append(norm(f'EVALUACIÓN DE LA UNIDAD {m.group(1)}'))
        m=re.match(r'evaluación integradora de la (\S+) etapa',key)
        if m: cands.append(norm(f'EVALUACIÓN INTEGRADORA · {m.group(1)} ETAPA'))
        if key.startswith('prueba diagnóstica'): cands.append('prueba diagnóstica —')
        found=None
        for i in range(desde,len(P)):
            lines=[norm(l) for l in P[i].splitlines() if l.strip()]
            if any(l.startswith(c) for c in cands for l in lines):
                found=i+1; break
        assert found, title
        if num.text.strip()!=str(found): cambios+=1
        num.text=str(found); filas.append((title,found))
        if not key.startswith('unidad'): desde=found-1
    d.save(docx_out); return filas,cambios
if __name__=='__main__':
    f,c=run(*sys.argv[1:4]); print('entradas',len(f),'cambiadas',c)
    for t,n in f: print(n,t)
