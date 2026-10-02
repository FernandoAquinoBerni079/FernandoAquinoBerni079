import docx, copy, re
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from ed import *
from caps import C, SEQ
doc=docx.Document('Gabinete_Informatica_Software_1er_Curso_PLAN_ANUAL_ESENCIAL_COMERCIAL_2026.docx')
t=doc.tables[0]
def mk_run(src_r, text, bold=False, italic=False):
    r=copy.deepcopy(src_r)
    for x in list(r):
        if x.tag!=qn('w:rPr'): r.remove(x)
    rpr=r.find(qn('w:rPr'))
    if rpr is None: rpr=OxmlElement('w:rPr'); r.insert(0,rpr)
    for tagn,flag in ((qn('w:b'),bold),(qn('w:i'),italic)):
        e=rpr.find(tagn)
        if flag and e is None: rpr.insert(0,OxmlElement(tagn.split('}')[1].join(['w:',''])) if False else OxmlElement('w:'+tagn.split('}')[1]))
        if not flag and e is not None: rpr.remove(e)
    tt=OxmlElement('w:t'); tt.text=text; tt.set('{http://www.w3.org/XML/1998/namespace}space','preserve'); r.append(tt)
    return r
RES={18:'Todas las capacidades de la Unidad 1, transcriptas en las secuencias 1 a 15.',
     36:'Todas las capacidades de las Unidades 2 y 3, transcriptas en las secuencias 19 a 34.'}
n_done=0
for row in t.rows:
    tcs=row._tr.findall(qn('w:tc'))
    if len(tcs)!=7: continue
    num=''.join(x.text or '' for x in tcs[0].iter(qn('w:t'))).strip()
    if num=='N°':
        p=tcs[1].find(qn('w:p')); set_ptext(p,'TEMAS Y CAPACIDAD MEC'); continue
    if not num.isdigit(): continue
    n=int(num)
    p=tcs[1].findall(qn('w:p'))[-1]; src_r=p.find(qn('w:r'))
    lab=copy.deepcopy(p)
    for r in lab.findall(qn('w:r')): lab.remove(r)
    lab.append(mk_run(src_r,'Capacidad MEC:',bold=True))
    p.addnext(lab); prev=lab
    caps=[RES[n]] if n in RES else [C[c] for c in SEQ[n]]
    for c in caps:
        q=copy.deepcopy(lab)
        for r in q.findall(qn('w:r')): q.remove(r)
        q.append(mk_run(src_r,('«'+c+'»') if n not in RES else c,italic=True))
        prev.addnext(q); prev=q
    if n==30:
        ip=tcs[2].findall(qn('w:p'))[-1]
        r=ip.findall(qn('w:r'))[-1]
        r.append(OxmlElement('w:br'))
        tt=OxmlElement('w:t'); tt.text='• Sintetiza el diagnóstico en un informe breve y reconoce el valor de abstraer, analizar y sintetizar en el trabajo técnico.'; tt.set('{http://www.w3.org/XML/1998/namespace}space','preserve'); r.append(tt)
    n_done+=1
assert n_done==36,n_done
LOG.append(('H1/H2/H3 capacidad MEC en las 36 secuencias','','',n_done))
replace(doc,'internos de el gabinete','internos del gabinete',tag='H11')
replace(doc,'aplicando el convención indicada','aplicando la convención indicada',tag='Errata «el convención»')
replace(doc,'Ficha K: diagnóstico de una notebook con 2 GB libres en C:, Descargas de 40 GB, un programa que no responde y un archivo extraviado; evidencias a observar.',
 'Ficha K: diagnóstico de una notebook con 2 GB libres en C:, Descargas de 40 GB, un programa que no responde y un archivo extraviado; evidencias a observar; síntesis escrita del diagnóstico.',tag='H1 seq 30 procedimientos')
replace(doc,'• Los contenidos de ética, licencias y seguridad se trabajan conforme al marco legal paraguayo vigente (Leyes 1328/98, 4439/2011, 5994/2017 y 7593/2025).',
 '• Los contenidos de ética, licencias y seguridad se trabajan conforme al marco legal paraguayo aplicable y actualizado: Ley 1328/98, Ley 4439/2011 y Ley 5994/2017. La Ley 7593/2025 de Protección de Datos Personales se estudia como norma publicada el 27/11/2025, con entrada en vigencia diferida hasta el 27/11/2027 conforme a su artículo 57.',tag='H4 marco legal')
replace(doc,'Capacidades oficiales conservadas; fichas A–G','Capacidades oficiales transcriptas en cada secuencia; fichas A–G',tag='H2 banda U1')
replace(doc,'Capacidades oficiales conservadas; fichas H–K','Capacidades oficiales transcriptas en cada secuencia; fichas H–K',tag='H2 banda U2')
replace(doc,'Capacidades oficiales conservadas.','Capacidades oficiales transcriptas en cada secuencia.',tag='H2 banda U3')
doc.save('PA_v2.docx')
for l in LOG: print(l[0],'·',l[3])
