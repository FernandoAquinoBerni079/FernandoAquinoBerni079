"""Compara el texto de dos docx (cuerpo, tablas, encabezados, pies y propiedades).
Ignora solo el número final de las entradas del índice («título\tN»)."""
import sys, re, zipfile
import docx
from docx.oxml.ns import qn
def textos(path):
    d=docx.Document(path); out=[]
    for el in d.element.body.iter(qn('w:p')):
        out.append(''.join((x.text or '') if x.tag==qn('w:t') else '\t' for x in el.iter(qn('w:t'),qn('w:tab')) if x.getparent().tag==qn('w:r')))
    return out
def partes(f):
    z=zipfile.ZipFile(f); out={}
    for n in sorted(z.namelist()):
        if re.match(r'word/(header|footer)\d*\.xml|docProps/core\.xml',n):
            out[n]=re.sub(r'<dcterms:modified.*?</dcterms:modified>','',z.read(n).decode())
            out[n]=re.sub('<[^>]+>','|',out[n])
    return out
a,b=[x for x in textos(sys.argv[1]) if x.strip()],[x for x in textos(sys.argv[2]) if x.strip()]  # los separadores vacíos no son contenido
print('parrafos',len(a),len(b))
dif=[];idx=0
for x,y in zip(a,b):
    if x==y: continue
    if '\t' in x and x.rsplit('\t',1)[0]==y.rsplit('\t',1)[0] and re.fullmatch(r'\d+',x.rsplit('\t',1)[1]) and re.fullmatch(r'\d+',y.rsplit('\t',1)[1]):
        idx+=1; continue
    dif.append((x,y))
pa,pb=partes(sys.argv[1]),partes(sys.argv[2])
print('numeros de indice cambiados',idx)
print('diferencias de texto',len(dif)+(len(a)!=len(b)))
for x,y in dif[:5]: print(repr(x[:120]),'||',repr(y[:120]))
print('encabezados/pies/propiedades iguales', pa==pb, [k for k in pa if pa.get(k)!=pb.get(k)])
