import docx, sys, json
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
T=lambda el:''.join(t.text or '' for t in el.iter(qn('w:t')))
SUB=('Marcá la opción correcta','Completá los espacios','Verdadero o falso','Respondé y fundamentá','Desafío final')
def is_break(el):
    x=el.xml if el.tag==qn('w:p') else ''
    return 'w:type="page"' in x or 'pageBreakBefore' in x
def ppr(p):
    e=p.find(qn('w:pPr'))
    if e is None: e=OxmlElement('w:pPr'); p.insert(0,e)
    return e
def set_keepnext(p):
    pr=ppr(p)
    if pr.find(qn('w:keepNext')) is None:
        k=OxmlElement('w:keepNext')
        # orden del schema: pStyle, keepNext...
        st=pr.find(qn('w:pStyle'))
        (st.addnext(k) if st is not None else pr.insert(0,k))
def tighten(p, after, before):
    pr=ppr(p); sp=pr.find(qn('w:spacing'))
    if sp is None:
        sp=OxmlElement('w:spacing')
        # insertar antes de ind/jc/rPr si existen
        anchor=None
        for tag in ('w:ind','w:contextualSpacing','w:jc','w:outlineLvl','w:rPr','w:sectPr'):
            anchor=pr.find(qn(tag))
            if anchor is not None: break
        (anchor.addprevious(sp) if anchor is not None else pr.append(sp))
    a=sp.get(qn('w:after')); b=sp.get(qn('w:before'))
    if a is None or int(a)>after: sp.set(qn('w:after'),str(after))
    if b is not None and int(b)>before: sp.set(qn('w:before'),str(before))
def run(src,dst,plan):
    d=docx.Document(src); ch=list(d.element.body.iterchildren())
    for el in d.element.body.iter(qn('w:p')):
        if T(el).strip().startswith(SUB): set_keepnext(el)
    for head,(after,before) in plan.items():
        idx=[i for i,el in enumerate(ch) if T(el).strip().startswith(head)]
        idx=[i for i in idx if i>60]  # salta el índice
        assert idx, head
        i=idx[0]; j=i+1
        while j<len(ch) and not is_break(ch[j]): j+=1
        for el in ch[i:j]:
            for p in ([el] if el.tag==qn('w:p') else list(el.iter(qn('w:p')))):
                tighten(p,after,before)
    d.save(dst)
if __name__=='__main__':
    run(sys.argv[1],sys.argv[2],json.loads(sys.argv[3]))
