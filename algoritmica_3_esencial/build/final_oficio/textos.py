import sys, docx
from docx.oxml.ns import qn
def textos(path):
    d=docx.Document(path); out=[]
    for el in d.element.body.iter():
        if el.tag==qn('w:p'):
            t=''.join(x.text or '' for x in el.iter(qn('w:t')))
            out.append(t)
    return out
if __name__=='__main__':
    import difflib
    a=textos(sys.argv[1]); b=textos(sys.argv[2])
    for l in difflib.unified_diff(a,b,lineterm='',n=0):
        if l.startswith(('---','+++','@@')): continue
        print(l[:400])
