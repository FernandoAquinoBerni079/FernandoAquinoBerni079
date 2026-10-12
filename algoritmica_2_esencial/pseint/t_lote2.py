import subprocess, os, sys
sys.path.insert(0,'.')
P='/home/claude/pseint/pseint'
def run(name, code, inputs=(), perfil='Flexible'):
    f=name+'.psc'; open(f,'w',encoding='latin-1').write(code)
    args=[P+'/bin/pseint',f,'--profile='+P+'/perfiles/'+perfil,'--nouser']+['--input='+str(x) for x in inputs]
    r=subprocess.run(args,capture_output=True,env=dict(os.environ,LD_LIBRARY_PATH=P+'/lib'),timeout=20)
    return r.stdout.decode('latin-1').strip().replace('\n',' | ')
print(run('glob','''SubProceso Mostrar()
 Escribir "umbral visto desde el módulo: ", umbral
FinSubProceso
Algoritmo Principal
 umbral <- 50000
 Mostrar()
FinAlgoritmo'''))
print(run('glob2','''SubProceso Cambiar()
 total <- 99
FinSubProceso
Algoritmo Principal
 total <- 5
 Cambiar()
 Escribir total
FinAlgoritmo'''))
print(run('cmp','''Algoritmo C
 Escribir "chipa" < "empanada"
 Escribir "Chipa" = "chipa"
 Escribir "Zapallo" < "anana"
 Escribir Mayusculas("Chipa") = Mayusculas("chipa")
 Escribir "10" < "9"
 Escribir "EMP-01" <> "EMP-02"
 Escribir "Ña Rosa", " ", Longitud("Ña Rosa")
 Escribir Subcadena("SOP-07", 5, 6), " ", Longitud("COC-12"), " ", Concatenar("Producto de categoría ", Subcadena("COC-12",1,3))
FinAlgoritmo'''))
print(run('trunc','''Algoritmo T
 Definir monto Como Entero
 monto <- 55555
 monto <- trunc(monto - monto * 0.10)
 Escribir monto
 Escribir redon(55555 * 0.9)
FinAlgoritmo'''))
