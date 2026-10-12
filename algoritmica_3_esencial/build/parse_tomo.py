# -*- coding: utf-8 -*-
"""Convierte el TOMO_COMPLETO actual en una lista de bloques estructurados (JSON)."""
import docx, json, re, shutil, os
from docx.oxml.ns import qn
SRC='/home/claude/alg3/src/Algoritmica_3er_Curso_TOMO_COMPLETO.docx'
d=docx.Document(SRC)
rels=d.part.rels
blocks=[]
def ptext(p): return p.text
for el in d.element.body.iterchildren():
    tag=el.tag.split('}')[1]
    if tag=='p':
        p=docx.text.paragraph.Paragraph(el,d)
        blips=el.findall('.//'+qn('a:blip'))
        if blips:
            rid=blips[0].get(qn('r:embed'))
            part=rels[rid].target_part
            name=os.path.basename(part.partname)
            open('figs_src/'+name,'wb').write(part.blob)
            ext=el.find('.//'+qn('wp:extent'))
            cx=int(ext.get('cx')) if ext is not None else 0
            blocks.append({'t':'img','file':name,'ancho_cm':round(cx/360000,2)})
            continue
        st=p.style.name; tx=p.text
        if not tx.strip(): continue
        if st.startswith('toc'): continue
        if st.startswith('Heading'):
            blocks.append({'t':'h%s'%st[-1],'text':tx.strip()})
        else:
            blocks.append({'t':'p','text':tx})
    elif tag=='tbl':
        t=docx.table.Table(el,d)
        rows=[]
        for r in t.rows:
            cells=[];prev=None
            for c in r.cells:
                if c._tc is prev: continue
                prev=c._tc
                cells.append([pp.text for pp in c.paragraphs])
            rows.append(cells)
        if len(rows)==3 and rows[0][0][0].strip()=='Capacidad':
            inds=[x.lstrip('• ').strip() for x in rows[2][1] if x.strip()]
            if len(inds)==1 and '\n' in inds[0]: inds=[x.lstrip('• ').strip() for x in inds[0].split('\n')]
            blocks.append({'t':'ficha','capacidad':'\n'.join(rows[0][1]).strip(),'tema':'\n'.join(rows[1][1]).strip(),'indicadores':inds})
        elif len(rows)==1 and len(rows[0])==1:
            paras=[x for x in rows[0][0] if x.strip()]
            title=paras[0]; body=paras[1:]
            if 'EVALUACIÓN' in title.upper() and len(paras)<=2:
                blocks.append({'t':'banda','text':' / '.join(paras)})
            else:
                blocks.append({'t':'caja','title':title,'body':body})
        else:
            hdr=['\n'.join(c).strip() for c in rows[0]]
            # caja con más de una fila? (tabla 1 columna)
            if len(rows[0])==1:
                paras=[x for r in rows for c in r for x in c if x.strip()]
                blocks.append({'t':'caja','title':paras[0],'body':paras[1:]})
            else:
                body=[['\n'.join(c).strip() for c in r] for r in rows[1:]]
                # caja embebida al final (concepto) en tabla de datos? detectar filas de 1 celda
                blocks.append({'t':'tabla','hdr':hdr,'rows':body})
json.dump(blocks,open('tomo_blocks.json','w'),ensure_ascii=False,indent=1)
from collections import Counter
print(Counter(b['t'] for b in blocks))
