import docx, re, copy
from docx.oxml.ns import qn
from ed import *
from caps import C, SEQ
doc=docx.Document('Gabinete_Informatica_Software_1er_Curso_PLANES_DE_CLASE_ESENCIAL_COMERCIAL_2026.docx')
body=doc.element.body
# mapear cada tabla al plan en curso
plan=None; tabla_plan={}
for el in body.iterchildren():
    if el.tag==qn('w:p'):
        m=re.match(r'Plan de Clase N\.º (\d+) —',ptext(el).strip())
        if m: plan=int(m.group(1))
    elif el.tag==qn('w:tbl') and plan:
        tabla_plan[el]=plan
        m=None
        for t in el.iter(qn('w:t')):
            pass
# en el encabezado de cada plan aparece «Plan de Clase N.º X de 36»; usarlo también
for el in body.iterchildren(qn('w:tbl')):
    m=re.search(r'Plan de Clase N\.º (\d+) de 36',ptext(el)) 
from docx.table import Table
hechos=0
for tbl,n in tabla_plan.items():
    t=Table(tbl,doc)
    for r in t.rows:
        if r.cells[0].text.strip()=='Capacidad':
            cell=r.cells[-1]; ps=cell.paragraphs
            caps=[C[c] for c in SEQ[n]]
            textos=caps if len(caps)==1 else ['• '+c for c in caps]
            p0=ps[0]._p
            for p in ps[1:]: p._p.getparent().remove(p._p)
            set_ptext(p0,textos[0]); prev=p0
            for s in textos[1:]:
                q=copy.deepcopy(p0); set_ptext(q,s); prev.addnext(q); prev=q
            hechos+=1
assert hechos==36, hechos
LOG.append(('H1/H3 capacidades textuales en los 36 planes','','',hechos))
def scoped(n, old, new, tag, count=1):
    k=0
    for tbl,pn in tabla_plan.items():
        if pn!=n: continue
        for p in tbl.iter(qn('w:p')):
            if old in ptext(p):
                ts=list(p.iter(qn('w:t'))); full=''.join(t.text or '' for t in ts)
                # reutiliza el reemplazo general sobre un doc-falso
                i=full.index(old); j=i+len(old); pos=0; first=None
                for t in ts:
                    s=pos; e=pos+len(t.text or ''); pos=e
                    if e<=i or s>=j: continue
                    tx=t.text or ''
                    if first is None: first=t; t.text=tx[:i-s]+new+(tx[j-s:] if e>=j else '')
                    else: t.text=tx[j-s:] if e>j else ''
                k+=1
    assert k==count,(tag,k); LOG.append((tag,old,new,k))
# Plan 30: indicador y cierre de la capacidad de abstracción, análisis y síntesis
for tbl,pn in tabla_plan.items():
    if pn!=30: continue
    t=Table(tbl,doc)
    for r in t.rows:
        if r.cells[0].text.strip().startswith('Indicadores'):
            last=r.cells[-1].paragraphs[-1]._p
            q=copy.deepcopy(last); set_ptext(q,'• Sintetiza el diagnóstico en un informe breve y reconoce el valor de abstraer, analizar y sintetizar en el trabajo técnico.'); last.addnext(q)
            LOG.append(('H1 Plan 30 indicador','','',1))
scoped(30,'Registro de una conclusión técnica en el cuaderno.','Síntesis escrita del diagnóstico (paso 5 de la Ficha K): una línea por problema con síntoma, tema, dato observado y solución; breve reflexión sobre el valor de abstraer, analizar y sintetizar en el trabajo técnico.','H1 Plan 30 cierre')
replace(doc,'Figuras 5.2 y 5.2','Figuras 5.1 y 5.2',tag='H9 Plan 6')
replace(doc,'Figuras 8.2 y 8.2','Figuras 8.1 y 8.2',tag='H10 Plan 11')
replace(doc,'internos de el gabinete','internos del gabinete',count=2,tag='H11 Plan 6')
doc.save('PLANES_v2.docx')
for l in LOG: print(l[0],'·',l[3])
