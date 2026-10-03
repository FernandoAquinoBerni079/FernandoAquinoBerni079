import pymupdf, json, os
O='/home/claude/alg3/salida_v2/'; B='/home/claude/alg3/build/'
L=pymupdf.open(O+'Algoritmica_3er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026_v2.pdf')
S=pymupdf.open(O+'Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026_v2.pdf')
P=pymupdf.open(O+'Algoritmica_3er_Curso_PLANES_DE_CLASE_ESENCIAL_COMERCIAL_2026_v2.pdf')
A=pymupdf.open(O+'Algoritmica_3er_Curso_PLAN_ANUAL_ESENCIAL_COMERCIAL_2026_v2.pdf')
ji=json.load(open(B+'indice_libro.json')); pg={t:p for (n,t),p in zip(ji['entradas'],ji['paginas'])}
c1=pg['Clase 1 — ¿Qué es un lenguaje de programación?']; c2=pg['Clase 2 — Niveles de lenguaje: de la máquina al alto nivel']
jp=json.load(open(B+'indice_planes.json')); p1,p2=jp['paginas'][0],jp['paginas'][1]
M=pymupdf.open()
for doc,a,b in ((L,0,c2-2),(L,L.page_count-1,L.page_count-1),(S,0,0),(A,0,1),(P,0,0),(P,p1-1,p2-2)):
    M.insert_pdf(doc,from_page=a,to_page=b)
M.set_metadata({'title':'Algorítmica · 3.er Curso · Muestra comercial','author':'Equipo editorial','subject':'Edición Esencial Comercial 2026'})
M.subset_fonts()
out=O+'Algoritmica_3er_Curso_MUESTRA_COMERCIAL_2026_v2.pdf'
M.save(out,garbage=4,deflate=True,deflate_images=True,deflate_fonts=True,clean=True)
print('muestra', M.page_count, 'págs', round(os.path.getsize(out)/1e6,2),'MB')
