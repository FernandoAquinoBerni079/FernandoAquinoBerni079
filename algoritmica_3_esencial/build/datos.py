# -*- coding: utf-8 -*-
"""Datos verificados del caso Copetín Karumbé (semana 1 = clases; semana 2 = prácticas de Access)."""
PROD={'P01':('Chipa','Panificados',3000),'P02':('Mbeju','Panificados',5000),
      'P03':('Empanada','Salados',6000),'P04':('Milanesa','Salados',15000),
      'P05':('Cocido','Bebidas',4000),'P06':('Gaseosa','Bebidas',8000)}
CLI={'C01':'Rosa Duarte','C02':'Luis Benítez','C03':'Ana Gómez','C04':'Miguel Ortiz'}
VEN={'V1':('03/03/2026','C01'),'V2':('03/03/2026','C02'),'V3':('04/03/2026','C01'),
     'V4':('04/03/2026','C03'),'V5':('05/03/2026','C04')}
DET=[('V1','P01',2,3000),('V1','P06',1,8000),('V2','P04',1,15000),('V2','P05',1,4000),
     ('V3','P03',3,6000),('V3','P06',2,8000),('V4','P01',4,3000),('V4','P02',1,5000),
     ('V5','P04',2,15000),('V5','P06',2,8000),('V5','P05',1,4000)]
# Semana 2 (prácticas 18-21): catálogo ampliado; gaseosa sube a 9.000 el 10/03/2026
PROD2=dict(PROD); PROD2['P06']=('Gaseosa','Bebidas',9000)
PROD2['P07']=('Jugo natural','Bebidas',7000); PROD2['P08']=('Sopa paraguaya','Panificados',6000)
CLI2=dict(CLI); CLI2['C05']='Teresa Villalba'; CLI2['C06']='Hugo Cáceres'
TEL2={'C01':'0981 401 220','C02':'0982 315 774','C03':'0971 662 109','C04':'0983 590 418','C05':'0985 207 336','C06':None}
VEN2={'V6':('09/03/2026','C02'),'V7':('09/03/2026','C05'),'V8':('10/03/2026','C01'),
      'V9':('10/03/2026','C06'),'V10':('11/03/2026','C05'),'V11':('11/03/2026','C03')}
DET2=[('V6','P03',2,6000),('V6','P07',1,7000),('V7','P01',3,3000),('V7','P05',2,4000),
      ('V8','P04',1,15000),('V8','P06',1,8000),('V8','P01',2,3000),('V9','P08',2,6000),('V9','P07',1,7000),
      ('V10','P02',1,5000),('V10','P05',1,4000),('V11','P03',4,6000),('V11','P06',2,9000)]
def agg(det,prod,ven,cli,key):
    r={}
    for v,p,q,pu in det:
        k={'venta':v,'cliente':ven[v][1],'cat':prod[p][1],'prod':p,'fecha':ven[v][0]}[key]
        r[k]=r.get(k,0)+q*pu
    return r
if __name__=='__main__':
    T=agg(DET,PROD,VEN,CLI,'venta'); assert T=={'V1':14000,'V2':19000,'V3':34000,'V4':17000,'V5':50000}
    assert sum(T.values())==134000 and sum(T.values())/5==26800
    assert agg(DET,PROD,VEN,CLI,'cliente')=={'C01':48000,'C02':19000,'C03':17000,'C04':50000}
    assert agg(DET,PROD,VEN,CLI,'cat')=={'Panificados':23000,'Salados':63000,'Bebidas':48000}
    for v,p,q,pu in DET: assert PROD[p][2]==pu
    T2=agg(DET2,PROD2,VEN2,CLI2,'venta'); print('Semana 2 por venta',T2,sum(T2.values()),sum(T2.values())/6)
    print('por cliente',agg(DET2,PROD2,VEN2,CLI2,'cliente'))
    print('por categoría',agg(DET2,PROD2,VEN2,CLI2,'cat'))
    print('por producto',agg(DET2,PROD2,VEN2,CLI2,'prod'))
    print('por fecha',agg(DET2,PROD2,VEN2,CLI2,'fecha'))
    # cruzada
    X={}
    for v,p,q,pu in DET2: X[(CLI2[VEN2[v][1]],PROD2[p][1])]=X.get((CLI2[VEN2[v][1]],PROD2[p][1]),0)+q*pu
    print('cruzada',X)
    # trampa: gaseosa con catálogo
    print('gaseosa real',sum(q*pu for v,p,q,pu in DET2 if p=='P06'),'con catálogo',sum(q*PROD2[p][2] for v,p,q,pu in DET2 if p=='P06'))
    print('total si se usa catálogo', sum(q*PROD2[p][2] for v,p,q,pu in DET2))
    # unidades semana 1
    U={}
    for v,p,q,pu in DET: U[p]=U.get(p,0)+q
    print('unidades s1',U)
    U2={}
    for v,p,q,pu in DET2: U2[p]=U2.get(p,0)+q
    print('unidades s2',U2)
    # renglones por categoría semana2
    from collections import Counter
    print('renglones por cat s2',Counter(PROD2[p][1] for v,p,q,pu in DET2))
    # redundancia tabla única semana 1
    rows=[(v,VEN[v][0],VEN[v][1],CLI[VEN[v][1]],p,*PROD[p],q) for v,p,q,pu in DET]
    red=(len(rows)-len(VEN))*2+(len(rows)-len(CLI))+(len(rows)-len(PROD))*3
    print('celdas redundantes',red)
