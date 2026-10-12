import docx, json, re
d=docx.Document('/home/claude/alg3/src/Algoritmica_3er_Curso_PLANES_DE_CLASE.docx')
body=list(d.element.body.iterchildren())
planes=[];cur=None
def cells(t):
    out=[]
    for r in t.rows:
        row=[];prev=None
        for c in r.cells:
            if c._tc is prev: continue
            prev=c._tc; row.append([p.text for p in c.paragraphs])
        out.append(row)
    return out
for el in body:
    tag=el.tag.split('}')[1]
    if tag=='p':
        p=docx.text.paragraph.Paragraph(el,d)
        if p.style.name=='Plan de Clase':
            m=re.match(r'Plan de Clase N\.º (\d+) — (.*)',p.text)
            cur={'n':int(m.group(1)),'titulo':m.group(2),'tablas':[]}; planes.append(cur)
    elif tag=='tbl' and cur:
        cur['tablas'].append(cells(docx.table.Table(el,d)))
out=[]
for p in planes:
    T=p['tablas']
    info={}
    for row in T[1]:
        for i in range(0,len(row)-1,2): info[row[i][0]]=' '.join(row[i+1]).strip()
    cap=' '.join(T[2][0][1]); inds=[x.lstrip('• ').strip() for x in T[2][1][1] if x.strip()]
    mom={r[0][0]:[x.lstrip('• ').strip() for x in r[1] if x.strip()] for r in T[3][1:]}
    tiempos={r[0][0]:r[2][0] for r in T[3][1:]}
    rec=' '.join(T[4][0][1])
    ev={r[0][0]:[x.lstrip('• ').strip() for x in r[1] if x.strip()] for r in T[5][1:]}
    out.append(dict(n=p['n'],titulo=p['titulo'],info=info,capacidad=cap,indicadores=inds,momentos=mom,tiempos=tiempos,recursos=rec,
        proc=' '.join(ev.get('Procedimientos',[])),inst=' '.join(ev.get('Instrumentos',[])),criterios=ev.get('Criterios',[])))
json.dump(out,open('planes_old.json','w'),ensure_ascii=False,indent=1)
print(len(out))
for o in out: print(o['n'], o['titulo'][:50],'|',o['info'].get('Material','')[:80],'|',o['tiempos'])
