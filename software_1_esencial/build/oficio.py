import docx, sys
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
W,H,M=12240,18720,720          # oficio 8,5 × 13 in · márgenes estrechos 1,27 cm
TEXTW=W-2*M
A='{http://schemas.openxmlformats.org/drawingml/2006/main}'
def run(src,dst,cov,back):
    d=docx.Document(src); b=d.element.body
    for s in b.iter(qn('w:sectPr')):
        pg=s.find(qn('w:pgSz')); pg.set(qn('w:w'),str(W)); pg.set(qn('w:h'),str(H))
        m=s.find(qn('w:pgMar'))
        for k in ('top','bottom','left','right'): m.set(qn('w:'+k),str(M))
        m.set(qn('w:header'),'708'); m.set(qn('w:footer'),'708')
    # portada y contraportada a página completa
    cx,cy=str(round(21.59/2.54*914400)),str(round(33.02/2.54*914400))
    imgs={'media/image27.jpg':cov,'media/image28.jpg':back}
    for dr in b.iter(qn('w:drawing')):
        a=dr.find(qn('wp:anchor'))
        if a is None: continue
        blip=dr.find('.//'+A+'blip'); part=d.part.related_parts[blip.get(qn('r:embed'))]
        tgt=d.part.rels[blip.get(qn('r:embed'))].target_ref
        part._blob=open(imgs[tgt],'rb').read()
        a.find(qn('wp:extent')).set('cx',cx); a.find(qn('wp:extent')).set('cy',cy)
        for e in dr.iter(A+'ext'): e.set('cx',cx); e.set('cy',cy)
    # tablas ajustadas a la ventana
    n=0
    for t in b.iter(qn('w:tbl')):
        if t.getparent().tag==qn('w:tc'): continue
        pr=t.find(qn('w:tblPr'))
        w=pr.find(qn('w:tblW'))
        if w is None: w=OxmlElement('w:tblW'); pr.append(w)
        w.set(qn('w:type'),'pct'); w.set(qn('w:w'),'5000')
        lay=pr.find(qn('w:tblLayout'))
        if lay is not None: pr.remove(lay)
        ind=pr.find(qn('w:tblInd'))
        if ind is not None: ind.set(qn('w:w'),'0'); ind.set(qn('w:type'),'dxa')
        g=t.find(qn('w:tblGrid'))
        if g is not None:
            cols=g.findall(qn('w:gridCol')); tot=sum(int(c.get(qn('w:w'))) for c in cols) or 1
            f=TEXTW/tot
            for c in cols: c.set(qn('w:w'),str(round(int(c.get(qn('w:w')))*f)))
            for tc in t.iter(qn('w:tcW')):
                if tc.get(qn('w:type'))=='dxa': tc.set(qn('w:w'),str(round(int(tc.get(qn('w:w')))*f)))
        n+=1
    d.core_properties.author='Biblioteca Comercial 2026'
    d.save(dst); print('tablas ajustadas',n)
run(*sys.argv[1:5])
