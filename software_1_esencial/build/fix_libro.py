import docx, copy
from docx.oxml.ns import qn
from ed import *
from caps import C, CLASE
doc=docx.Document('LIBRO_orig.docx')
# H3 — capacidades separadas y textuales en las fichas de clase
old={9:'Analiza las características principales de los diferentes tipos de software y reflexiona sobre las aplicaciones actuales de la informática.',
 11:'Reconoce el origen y evolución de los Sistemas Operativos y las ventajas y desventajas de los actuales.',
 12:'Analiza los diferentes tipos de licencias de software y el funcionamiento del sistema operativo y del sistema de aplicación.',
 16:'Identifica los diferentes tipos de memoria y analiza el funcionamiento de su administración.',
 17:'Reconoce los diferentes tipos de Sistemas de Numeración utilizados en la informática y aplica procedimientos de conversión de números enteros.',
 18:'Aplica procedimientos para convertir un número entero de cualquier base.'}
for k,v in old.items():
    split_p(doc, v, [C[c] for c in CLASE[k]], tag=f'H3 Clase {k}')
# H1 — Ficha K: capacidad omitida, trabajada en la ficha
p=find_p(doc,'Separar los problemas y atacarlos de a uno evita soluciones que tapan un síntoma sin resolver la causa.')
assert len(p)==1
q=insert_after(p[0],'Esta ficha trabaja una capacidad del programa: «'+C[17]+'» Diagnosticar es exactamente eso: abstraer (quedarte con los datos que importan y dejar de lado el ruido), analizar (separar el caso en problemas y asociar cada uno con su tema) y sintetizar (resumir el diagnóstico en pocas líneas que otra persona pueda seguir).')
p=find_p(doc,'4. Proponé una solución segura para cada problema, sin borrar nada que no haya sido revisado y respaldado.')
assert len(p)==1
insert_after(p[0],'5. Sintetizá el diagnóstico en un informe breve, con una línea por problema (síntoma, tema, dato observado y solución), y explicá en una oración por qué separar el caso en partes facilitó encontrar la solución.')
LOG.append(('H1 Ficha K','(nuevo párrafo + paso 5)','',1))
# H5 — datos de almacenamiento sin repetir el ejemplo de la Clase 7
replace(doc,'11. Con los precios del taller (SSD 480 GB ₲ 280.000; HDD 1 TB ₲ 350.000), ¿qué unidad',
 '11. Otro proveedor ofrece un SSD de 512 GB a ₲ 320.000 y un HDD de 3 TB a ₲ 560.000. ¿Qué unidad',tag='H5 Act. 11')
replace(doc,'Justificá.\u0000','',count=0,tag='noop') if False else None
replace(doc,'b) Con los precios del taller (SSD 480 GB ₲ 280.000; HDD 1 TB ₲ 350.000), recomendá',
 'b) Con la lista de precios de un mayorista (SSD 256 GB ₲ 210.000; HDD 6 TB ₲ 1.020.000), recomendá',tag='H5 Integradora 1, 3 b)')
# H6 — Clase 20 sin operandos de los ejemplos resueltos
replace(doc,'1011 (11 fuentes) + 110 (6 fuentes) = 10001 (17 fuentes). El técnico verifica en decimal —11 + 6 = 17—',
 '1010 (10 fuentes) + 1001 (9 fuentes) = 10011 (19 fuentes). El técnico verifica en decimal —10 + 9 = 19—',tag='H6 Ejemplo stock')
def item_opts(stem_old, stem_new, opts, tag):
    ps=all_ps(doc); idx=[i for i,p in enumerate(ps) if ptext(p).strip()==stem_old]
    assert len(idx)==1,(tag,len(idx))
    i=idx[0]; replace(doc,stem_old,stem_new,tag=tag)
    for k,o in enumerate(opts):
        p=ps[i+1+k]; t=ptext(p); lead=t[:len(t)-len(t.lstrip())]
        assert t.strip()[:2]=='abcd'[k]+')',(tag,t)
        set_ptext(p, lead+'abcd'[k]+') '+o+'.')
item_opts('3. El resultado de 110 × 11 es…','3. El resultado de 1010 × 11 es…',['11110','1101','10110','11000'],'H6 ítem 3')
item_opts('4. El resultado de 1111 ÷ 101 es…','4. El resultado de 10100 ÷ 100 es…',['100','110','1001','101'],'H6 ítem 4')
replace(doc,'8. (....) El resultado de 1011 − 110 es 101.','8. (....) El resultado de 11001 − 1010 es 1111.',tag='H6 ítem 8')
replace(doc,'tiene 110₂ teclados y el B, 101₂.','tiene 1110₂ teclados y el B, 1010₂.',tag='H6 ítem 12')
replace(doc,'11110 ÷ 110','11100 ÷ 100',tag='H6 Práctica 20 división')
replace(doc,'d) 10010 ÷ 11 =','d) 11000 ÷ 11 =',tag='H6 Eval. U3 3 d)')
replace(doc,'b) 10110 − 1001 =','b) 11010 − 1001 =',tag='H6 Integradora 2, 4 b)')
# H7 — Windows no genuino
replace(doc,'Le explicás que la copia ilegal viola la Ley 1328/98, no recibe actualizaciones de seguridad garantizadas y expone su negocio a riesgos y sanciones.',
 'Le explicás que la copia sin licencia vulnera las condiciones de licencia y puede implicar infracción de la Ley 1328/98, con riesgo de sanciones para su negocio. Microsoft mantiene las actualizaciones críticas de seguridad incluso en copias no genuinas, pero reserva determinadas actualizaciones, descargas y beneficios para el software original; además, una activación no oficial puede introducir programas maliciosos.',tag='H7 Clase 9 ejemplo')
replace(doc,'Instalar copias sin licencia, además de violar la Ley 1328/98, deja al equipo sin actualizaciones garantizadas: un riesgo que un técnico serio nunca recomienda.',
 'Instalar copias sin licencia, además de vulnerar las condiciones de licencia y poder implicar infracción de la Ley 1328/98, limita el acceso a determinadas actualizaciones, descargas y beneficios reservados al software original, y expone al equipo a riesgos si se usan activadores no oficiales; las actualizaciones críticas de seguridad de Windows, en cambio, siguen disponibles incluso en copias no genuinas. Es una práctica que un técnico serio nunca recomienda.',tag='H7 Clase 12')
# H8 — grooming
replace(doc,'6. El engaño de un adulto que se hace pasar por menor para ganar confianza se llama ______________.',
 '6. El acercamiento, contacto o manipulación de una persona adulta hacia una persona menor de edad con fines sexuales se llama ______________.',tag='H8 Clase 8 ítem 6')
doc.save('LIBRO_v2.docx')
for l in LOG: print(l[0],'·',l[3])
