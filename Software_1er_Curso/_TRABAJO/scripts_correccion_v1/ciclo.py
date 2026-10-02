import subprocess, re, json, sys, shutil, os
from paginar import run as tight
LO='/tmp/lo'
def render(docx_path):
    shutil.copy(docx_path, LO); name=os.path.basename(docx_path)
    subprocess.run(f'cd {LO} && HOME={LO} timeout 600 soffice --headless --convert-to pdf {name}',shell=True,capture_output=True)
    return os.path.join(LO,name.replace('.docx','.pdf'))
def fill(pdf):
    out=subprocess.run(['pdftotext','-bbox-layout',pdf,'-'],capture_output=True,text=True).stdout
    pages=re.split(r'<page ',out)[1:]; res=[]
    for pg in pages:
        H=float(re.search(r'height="([\d.]+)"',pg).group(1))
        ys=[]; heads=[]
        for blk in re.finditer(r'<line xMin="[\d.]+" yMin="([\d.]+)" xMax="[\d.]+" yMax="([\d.]+)">(.*?)</line>',pg,re.S):
            words=' '.join(re.findall(r'>([^<]*)</word>',blk.group(3)))
            if re.match(r'Página \d+ de \d+',words): continue
            ys.append(float(blk.group(2))); heads.append(words)
        res.append((max(ys)/H if ys else 0, heads[:1]))
    return res
def block_of(pdf,i,res):
    for j in range(i,max(-1,i-8),-1):
        txt=subprocess.run(['pdftotext','-f',str(j+1),'-l',str(j+1),pdf,'-'],capture_output=True,text=True).stdout
        m=re.search(r'^((Clase|Práctica|Ficha) [0-9A-K]+ —|EVALUACIÓN[^\n]*)',txt,re.M)
        if m: return m.group(1)
if __name__!="__main__": raise ImportError
src=sys.argv[1]; base=sys.argv[2]
plan={}; LEVELS=[(60,60),(30,40),(0,20)]
cur=src
for it in range(5):
    pdf=render(cur); r=fill(pdf); n=len(r)
    bad=[(i,f) for i,f in enumerate(r) if 0<i<n-1 and f[0]<0.25 and f[0]>0]
    print('iter',it,'páginas',n,'casi vacías',[(i+1,round(f[0],2)) for i,f in bad]); sys.stdout.flush()
    if not bad: break
    for i,_ in bad:
        h=block_of(pdf,i,r)
        if h is None: continue
        key=h.split(' —')[0]+' —' if '—' in h else h
        lv=plan.get(key,-1)+1
        if lv>=len(LEVELS): print('  sin margen para',key); continue
        plan[key]=lv
    nxt=f'{base}_{it}.docx'
    tight(src,nxt,{k:list(LEVELS[v]) for k,v in plan.items()}); cur=nxt
json.dump(plan,open(base+'_plan.json','w'),ensure_ascii=False)
print('FINAL',cur,plan)
