"""Reemplazos de texto a nivel de párrafo, preservando el formato del primer run."""
import copy, re
from docx.oxml.ns import qn
LOG=[]
def ptext(p): return ''.join(t.text or '' for t in p.iter(qn('w:t')))
def all_ps(doc):
    return list(doc.element.body.iter(qn('w:p')))
def replace(doc, old, new, count=1, tag=''):
    n=0
    for p in all_ps(doc):
        ts=list(p.iter(qn('w:t')))
        full=''.join(t.text or '' for t in ts)
        while old in full and (count is None or n<count):
            i=full.index(old); j=i+len(old)
            pos=0; first=None
            for t in ts:
                s=pos; e=pos+len(t.text or ''); pos=e
                if e<=i or s>=j:
                    continue
                txt=t.text or ''
                if first is None:
                    first=t
                    t.text=txt[:i-s]+new+(txt[j-s:] if e>=j else '')
                else:
                    t.text=txt[j-s:] if e>j else ''
                t.set('{http://www.w3.org/XML/1998/namespace}space','preserve')
            n+=1
            full=''.join(t.text or '' for t in ts)
    if count is not None and n!=count:
        raise SystemExit(f'[{tag}] esperaba {count} reemplazos de {old[:70]!r}, hubo {n}')
    LOG.append((tag,old,new,n))
    return n
def find_p(doc, exact):
    r=[p for p in all_ps(doc) if ptext(p).strip()==exact]
    return r
def set_ptext(p, text):
    ts=list(p.iter(qn('w:t')))
    ts[0].text=text; ts[0].set('{http://www.w3.org/XML/1998/namespace}space','preserve')
    for t in ts[1:]: t.text=''
    # quita <w:br> intermedios
    for br in list(p.iter(qn('w:br'))): br.getparent().remove(br)
def split_p(doc, exact, parts, tag='', expect=1):
    ps=find_p(doc, exact)
    if len(ps)!=expect: raise SystemExit(f'[{tag}] {len(ps)} párrafos para {exact[:60]!r}')
    for p in ps:
        set_ptext(p, parts[0]); prev=p
        for s in parts[1:]:
            q=copy.deepcopy(p); set_ptext(q, s); prev.addnext(q); prev=q
    LOG.append((tag,exact,' ‖ '.join(parts),len(ps)))
def insert_after(p, text, bold_label=None):
    q=copy.deepcopy(p)
    rs=q.findall(qn('w:r'))
    for r in rs[1:]: q.remove(r)
    for br in list(q.iter(qn('w:br'))): br.getparent().remove(br)
    r=rs[0]
    for t in r.findall(qn('w:t'))[1:]: r.remove(t)
    t=r.find(qn('w:t')); t.text=text; t.set('{http://www.w3.org/XML/1998/namespace}space','preserve')
    p.addnext(q); return q
