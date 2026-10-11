import docx, sys
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
T=lambda el:''.join(t.text or '' for t in el.iter(qn('w:t')))
def fix(src,dst):
    d=docx.Document(src); b=d.element.body; n=0; skip=0
    for el in list(b.iterchildren()):
        if el.tag!=qn('w:p'): continue
        brs=[x for x in el.iter(qn('w:br')) if x.get(qn('w:type'))=='page']
        if not brs or T(el).strip() or el.find(qn('w:pPr')+'/'+qn('w:sectPr')) is not None: continue
        if el.find('.//'+qn('w:drawing')) is not None: skip+=1; continue
        nx=el.getnext()
        tgt=nx if nx is not None and nx.tag==qn('w:p') else (nx.find('.//'+qn('w:p')) if nx is not None else None)
        if tgt is None: skip+=1; continue
        pr=tgt.find(qn('w:pPr'))
        if pr is None: pr=OxmlElement('w:pPr'); tgt.insert(0,pr)
        if pr.find(qn('w:pageBreakBefore')) is None:
            k=OxmlElement('w:pageBreakBefore')
            anchor=None
            for tag in ('w:pStyle','w:keepNext','w:keepLines'):
                if pr.find(qn(tag)) is not None: anchor=pr.find(qn(tag))
            (anchor.addnext(k) if anchor is not None else pr.insert(0,k))
        b.remove(el); n+=1
    d.save(dst); print('saltos convertidos',n,'omitidos',skip)
fix(sys.argv[1],sys.argv[2])
