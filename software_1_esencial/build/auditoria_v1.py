import re, subprocess, docx
from docx.oxml.ns import qn
from caps import C
def txt(f):
    d=docx.Document(f); return re.sub(r'\s+',' ',' '.join(''.join(t.text or '' for t in p.iter(qn('w:t'))) for p in d.element.body.iter(qn('w:p'))))
B='out/Gabinete_Informatica_Software_1er_Curso_'
L=txt(B+'LIBRO_ESENCIAL_COMERCIAL_2026.docx'); S=txt(B+'SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026.docx')
P=txt(B+'PLANES_DE_CLASE_COMERCIAL_2026.docx'); A=txt(B+'PLAN_ANUAL_COMERCIAL_2026.docx')
ok=0; fallos=[]
def chk(cond,msg):
    global ok
    if cond: ok+=1
    else: fallos.append(msg)
# 1. 20 capacidades textuales en planes y plan anual; las de clase en el libro
for k,c in C.items():
    chk(c in P, f'cap {k} falta en Planes'); chk(c in A, f'cap {k} falta en Plan Anual')
    chk(c in L, f'cap {k} falta en Libro')
# 2. capacidades fusionadas eliminadas
for frag in ['y reflexiona sobre las aplicaciones','y las ventajas y desventajas de los actuales','y el funcionamiento del sistema operativo y del sistema de aplicación','y analiza el funcionamiento de su administración','y aplica procedimientos de conversión de números enteros','convertir un número entero de cualquier base']:
    for nm,t in (('Libro',L),('Planes',P),('Plan Anual',A)): chk(frag not in t, f'fusión residual «{frag}» en {nm}')
# 3. datos de almacenamiento: el ejemplo de la Clase 7 aparece una sola vez
chk(L.count('480 GB')==1 and L.count('₲ 280.000')==1, 'SSD 480 GB / ₲ 280.000 repetido en el Libro')
chk('480 GB' not in S, '480 GB sigue en el Solucionario')
for v in ['512 GB','₲ 320.000','3 TB','₲ 560.000','256 GB','₲ 210.000','6 TB','₲ 1.020.000']:
    chk(L.count(v)==1 and v in S, f'dato nuevo {v}: libro {L.count(v)} / sol {v in S}')
# 4. Clase 20 y Unidad 3: ningún par de operaciones comparte 2 o más números
from bincheck import nums
ops=[]
sec=L[L.index('Clase 20 — Operaciones con números binarios Capacidad'):L.index('Proyecto Final Integrador — Feria de Informática Durante')]
for a,o,b in re.findall(r'\b([01]{2,})\s*([+−×÷])\s*([01]{2,})\b',sec):
    ops.append((int(a,2),{'+':'+','−':'-','×':'*','÷':'/'}[o],int(b,2)))
ops=list(dict.fromkeys(ops))
for i in range(len(ops)):
    for j in range(i+1,len(ops)):
        s=nums(ops[i])&nums(ops[j])
        MISMO={frozenset({(5,'*',3),(5,'+',10)}),frozenset({(6,'*',5),(6,'+',24)})}  # productos parciales del mismo ejemplo resuelto
        if len(s)>=2 and frozenset({ops[i],ops[j]}) not in MISMO:
            fallos.append(f'operandos compartidos {ops[i]} / {ops[j]}')
ok+=1
# 5. coherencia aritmética de las respuestas nuevas
for a,o,b,r in [('1010','+','1001','10011'),('1010','*','11','11110'),('10100','/','100','101'),('11011','-','1010','10001'),('1110','+','1010','11000'),('1110','-','1010','100'),('11100','/','100','111'),('11000','/','11','1000'),('11010','-','1001','10001')]:
    x,y=int(a,2),int(b,2); v={'+':x+y,'-':x-y,'*':x*y,'/':x//y}[o]; chk(format(v,'b')==r, f'aritmética {a}{o}{b}')
for s in ['3. a) 11110 (10×3=30).','4. d) 101 (20÷4=5).','8. VERDADERO (27−10=17).','11100 ÷ 100 = 111 (28÷4=7)','d) 1000 (24÷3=8 ✓)','b) 10001 (26−9=17 ✓)','1110+1010 = 11000']:
    chk(s in S, f'solucionario sin «{s}»')
chk('3. El resultado de 1010 × 11 es… a) 11110.' in L and '4. El resultado de 10100 ÷ 100 es… a) 100. b) 110. c) 1001. d) 101.' in L,'opciones ítems 3/4 incoherentes')
# 6. legales y técnicos
chk('7593/2025)' not in A and '27/11/2027' in A, 'Ley 7593 en Plan Anual')
chk('no recibe actualizaciones de seguridad garantizadas' not in L and 'sin actualizaciones garantizadas' not in L, 'afirmación Windows en Libro')
chk('carece de actualizaciones garantizadas' not in S, 'afirmación Windows en Solucionario')
chk('se hace pasar por menor para ganar' not in L, 'grooming estrecho')
# 7. erratas
for nm,t in (('Libro',L),('Planes',P),('Plan Anual',A),('Sol',S)):
    chk('de el gabinete' not in t and 'el convención' not in t, f'errata en {nm}')
chk('Figuras 5.2 y 5.2' not in P and 'Figuras 8.2 y 8.2' not in P,'figuras duplicadas')
# 8. páginas
pdf=B+'LIBRO_ESENCIAL_COMERCIAL_2026.pdf'
info=subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout
chk('612 x 936' in info,'Libro no está en oficio')
info2=subprocess.run(['pdfinfo',B+'SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026.pdf'],capture_output=True,text=True).stdout
chk('612 x 936' in info2,'Solucionario no está en oficio')
print(f'controles OK: {ok} · fallos: {len(fallos)}'); [print(' -',f) for f in fallos]
