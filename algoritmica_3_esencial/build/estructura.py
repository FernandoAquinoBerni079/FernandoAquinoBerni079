# -*- coding: utf-8 -*-
import json,re
def cargar():
    B=json.load(open('/home/claude/alg3/build/tomo_blocks.json'))
    # separar filas-caja embebidas en tablas
    out=[]
    for b in B:
        if b['t']=='tabla':
            extra=[r for r in b['rows'] if len(r)==1]
            b['rows']=[r for r in b['rows'] if len(r)>1]
            out.append(b)
            for r in extra:
                lines=[x for x in r[0].split('\n') if x.strip()]
                out.append({'t':'caja','title':lines[0],'body':lines[1:]})
        else: out.append(b)
    # epígrafes
    for i,b in enumerate(out):
        if b['t']=='img' and i+1<len(out) and out[i+1]['t']=='p' and out[i+1]['text'].startswith('Figura'):
            b['epigrafe']=out[i+1]['text']; out[i+1]['t']='_del'
    out=[b for b in out if b['t']!='_del']
    # dividir
    pre=[];clases={};evals=[];unidades={}
    cur=None;modo='pre';u=None;ev=None
    for b in out:
        if b['t']=='h1':
            m=re.match(r'Clase (\d+) — (.*)',b['text'])
            mu=re.match(r'UNIDAD (\d+) — (.*)',b['text'])
            if m:
                n=int(m.group(1)); cur={'n':n,'titulo':m.group(2),'unidad':u,'cuerpo':[],'acts':[]}
                clases[n]=cur; modo='cuerpo'; continue
            if mu:
                u=int(mu.group(1)); unidades[u]=mu.group(2); modo='skip'; continue
            modo='skip'; continue
        if b['t']=='banda':
            ev={'banda':b['text'],'items':[],'tras_clase':max(clases) if clases else 0}; evals.append(ev); modo='eval'; continue
        if modo=='cuerpo':
            if b['t']=='ficha': cur['ficha']=b; continue
            if b['t']=='h3' and 'Actividades' in b['text']: modo='acts'; continue
            cur['cuerpo'].append(b)
        elif modo=='acts': cur['acts'].append(b)
        elif modo=='eval': ev['items'].append(b)
        elif modo=='pre' or modo=='skip': pre.append(b)
    return pre,clases,evals,unidades
if __name__=='__main__':
    pre,C,E,U=cargar()
    print(U); print(len(C),[ (e['banda'][:40],e['tras_clase'],len(e['items'])) for e in E])
    import sys
    n=int(sys.argv[1]) if len(sys.argv)>1 else 13
    for i,b in enumerate(C[n]['cuerpo']):
        s=b.get('text') or b.get('title') or b.get('file') or str(b.get('hdr'))
        print(i,b['t'],s[:110])
