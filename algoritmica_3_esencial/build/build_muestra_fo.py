import pymupdf, json, os, docx
O='/home/claude/alg3/salida_FINAL_OFICIO/'; B='/home/claude/alg3/build/'; N='Algoritmica_3er_Curso_'
L=pymupdf.open(O+N+'LIBRO_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO.pdf')
S=pymupdf.open(O+N+'SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO.pdf')
P=pymupdf.open(O+N+'PLANES_DE_CLASE_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO.pdf')
A=pymupdf.open(O+N+'PLAN_ANUAL_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO.pdf')
# páginas del índice del libro FINAL_OFICIO (leídas del .docx, ya verificadas contra el PDF)
D=docx.Document(O+N+'LIBRO_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO.docx')
pg={p.text.rsplit('\t',1)[0]:int(p.text.rsplit('\t',1)[1]) for p in D.paragraphs if p.style.name.startswith('toc') and '\t' in p.text}
c2=pg['Clase 2 — Niveles de lenguaje: de la máquina al alto nivel']
jp=json.load(open(B+'indice_planes.json')); p1,p2=jp['paginas'][0],jp['paginas'][1]
M=pymupdf.open()
for doc,a,b in ((L,0,c2-2),(L,L.page_count-1,L.page_count-1),(S,0,0),(A,0,1),(P,0,0),(P,p1-1,p2-2)):
    M.insert_pdf(doc,from_page=a,to_page=b)
M.set_metadata({'title':'Algorítmica · 3.er Curso · Muestra comercial','author':'Equipo editorial','subject':'Edición Esencial Comercial 2026'})
M.subset_fonts()
out=O+N+'MUESTRA_COMERCIAL_2026_FINAL_OFICIO.pdf'
M.save(out,garbage=4,deflate=True,deflate_images=True,deflate_fonts=True,clean=True)
print('muestra', M.page_count, 'págs', round(os.path.getsize(out)/1e6,2),'MB', 'libro 1..',c2-1)
