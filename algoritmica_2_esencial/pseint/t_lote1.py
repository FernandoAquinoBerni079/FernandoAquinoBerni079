# -*- coding: utf-8 -*-
import subprocess, os
P='/home/claude/pseint/pseint'
def run(name, code, inputs=(), perfil='Flexible'):
    f=name+'.psc'; open(f,'w',encoding='latin-1').write(code)
    args=[P+'/bin/pseint',f,'--profile='+P+'/perfiles/'+perfil,'--nouser']+['--input='+str(x) for x in inputs]
    r=subprocess.run(args,capture_output=True,env=dict(os.environ,LD_LIBRARY_PATH=P+'/lib'),timeout=20)
    out=r.stdout.decode('latin-1').strip().replace('\n',' | ')
    print('##',name,inputs,'->',out[-400:])
T={}
T['C2_desc']=('''Algoritmo DescuentoPorMonto
 Leer cantidad, precio
 monto <- cantidad * precio
 Si monto >= 50000 Entonces
  descuento <- monto * 0.10
  monto <- monto - descuento
  Escribir "Descuento aplicado: ", descuento
 FinSi
 Escribir "Total a pagar: ", monto
FinAlgoritmo''',[(12,5000),(8,3000)])
T['C2_igual_en_si']=('''Algoritmo P
 monto <- 36000
 Si monto = 36000 Entonces
  Escribir "compara"
 FinSi
 Escribir monto
FinAlgoritmo''',[()])
T['C2_entero_desc']=('''Algoritmo P
 Definir monto Como Entero
 Leer monto
 Si monto >= 50000 Entonces
  monto <- monto - monto * 0.10
 FinSi
 Escribir "Total: ", monto
FinAlgoritmo''',[(60000,),(55555,)])
T['C4_logico']=('''Algoritmo P
 Definir enBarrio Como Logico
 Leer monto, enBarrio
 Si (monto >= 50000) Y (enBarrio = Verdadero) Entonces
  Escribir "Envio gratis"
 SiNo
  Escribir "Envio con costo"
 FinSi
FinAlgoritmo''',[(60000,'Falso'),(60000,'Verdadero'),(60000,'F')])
T['C5_segun']=('''Algoritmo MenuMostrador
 Leer opcion
 Segun opcion Hacer
  1: Escribir "Chipa - 3.000"
  2: Escribir "Empanada - 5.000"
  De Otro Modo: Escribir "Opción inválida"
 FinSegun
FinAlgoritmo''',[(2,),(9,)])
T['C7_cierre']=('''Algoritmo CierreDeCaja
 total <- 0
 cantidad <- 0
 Repetir
  Leer monto
  Si monto <> 0 Entonces
   total <- total + monto
   cantidad <- cantidad + 1
  FinSi
 Hasta Que monto = 0
 Si cantidad > 0 Entonces
  promedio <- total / cantidad
  Escribir cantidad, " ventas - Total: ", total, " - Promedio: ", promedio
 Sino
  Escribir "No se cargaron ventas"
 FinSi
FinAlgoritmo''',[(30000,54000,24000,12000,0),(0,)])
T['C9_puntoycoma']=('''Algoritmo P
 Dimension ventas[7]
 Para i <- 1 Hasta 7 Hacer
  Leer ventas[i]
 FinPara
 total <- 0
 mayor <- ventas[1] ; posMayor <- 1
 menor <- ventas[1] ; posMenor <- 1
 Para i <- 1 Hasta 7 Con Paso 1 Hacer
  total <- total + ventas[i]
  Si ventas[i] > mayor Entonces mayor <- ventas[i] ; posMayor <- i FinSi
  Si ventas[i] < menor Entonces menor <- ventas[i] ; posMenor <- i FinSi
 FinPara
 promedio <- total / 7
 Escribir total, " ", promedio, " ", mayor, " ", posMayor, " ", menor, " ", posMenor
FinAlgoritmo''',[(420000,500000,450000,580000,850000,1100000,300000)])
T['C9_segundo']=('''Algoritmo P
 Dimension ventas[7]
 Para i <- 1 Hasta 7 Hacer
  Leer ventas[i]
 FinPara
 mayor <- ventas[1] ; segundo <- 0
 Para i <- 2 Hasta 7 Con Paso 1 Hacer
  Si ventas[i] > mayor Entonces
   segundo <- mayor
   mayor <- ventas[i]
  Sino
   Si ventas[i] > segundo Entonces
    segundo <- ventas[i]
   FinSi
  FinSi
 FinPara
 Escribir mayor, " ", segundo
FinAlgoritmo''',[(420000,500000,450000,580000,850000,1100000,300000)])
T['C11_burbuja_tomo']=('''Algoritmo P
 Dimension unid[6]
 Para i <- 1 Hasta 6 Hacer
  Leer unid[i]
 FinPara
 Para i <- 1 Hasta 5 Con Paso 1 Hacer
  Para j <- 1 Hasta 6-i Con Paso 1 Hacer
   Si unid[j] < unid[j+1] Entonces
    aux <- unid[j]
    unid[j] <- unid[j+1]
    unid[j+1] <- aux
   FinSi
  FinPara
 FinPara
 Para i <- 1 Hasta 6 Hacer
  Escribir Sin Saltar unid[i], " "
 FinPara
FinAlgoritmo''',[(123,75,45,200,90,60)])
T['C12_azar']=('''Algoritmo P
 Para d <- 1 Hasta 5 Hacer
  venta <- Azar(900001) + 300000
  Escribir venta
 FinPara
FinAlgoritmo''',[()])
T['C13_caja']=('''Funcion total <- CalcularTotal(precio, cantidad)
 total <- precio * cantidad
FinFuncion
Funcion neto <- AplicarDescuento(monto)
 Si monto >= 50000 Entonces
  neto <- monto - monto * 0.10
 Sino
  neto <- monto
 FinSi
FinFuncion
SubProceso ImprimirTicket(total)
 Escribir "Copetín Karumbé - Total: G. ", total
FinSubProceso
Algoritmo Caja
 Leer precio, cantidad
 bruto <- CalcularTotal(precio, cantidad)
 neto <- AplicarDescuento(bruto)
 ImprimirTicket(neto)
FinAlgoritmo''',[(5000,12)])
T['C14_ref']=('''SubProceso AplicarDescuento(monto Por Referencia)
 Si monto >= 50000 Entonces
  monto <- monto - monto * 0.10
 FinSi
FinSubProceso
Algoritmo ProbarReferencia
 Definir monto Como Real
 monto <- 60000
 AplicarDescuento(monto)
 Escribir monto
FinAlgoritmo''',[()])
T['C14_valor']=('''SubProceso AplicarDescuento(monto)
 Si monto >= 50000 Entonces
  monto <- monto - monto * 0.10
 FinSi
FinSubProceso
Algoritmo ProbarValor
 Definir monto Como Real
 monto <- 60000
 AplicarDescuento(monto)
 Escribir monto
FinAlgoritmo''',[()])
T['C14_cadenas']=('''Algoritmo P
 codigo <- "MIX-01"
 Escribir Subcadena(codigo, 1, 3), "|", Subcadena(codigo, 5, 6), "|", Longitud(codigo)
 Escribir Longitud("María"), "|", Mayusculas("María"), "|", Mayusculas("chipa"), "|", Longitud("Ramón"), "|", Mayusculas("Ramón")
 Escribir Concatenar("EMP", "-01"), "|", "MIX" + "-01", "|", Subcadena("Sándwich mixto", 1, 8)
 nombre <- "Sopa paraguaya"
 cuenta <- 0
 Para i <- 1 Hasta Longitud(nombre) Con Paso 1 Hacer
  Si Subcadena(nombre, i, i) = "a" Entonces
   cuenta <- cuenta + 1
  FinSi
 FinPara
 Escribir cuenta
 Escribir "chipa" < "empanada", "|", "Chipa" = "chipa", "|", "Zapallo" < "anana"
FinAlgoritmo''',[()])
T['C8_fuera_rango']=('''Algoritmo P
 Dimension ventas[7]
 ventas[8] <- 1
FinAlgoritmo''',[()])
T['C6_rep_valida']=('''Algoritmo P
 Repetir
  Escribir "Cantidad (mayor que 0):"
  Leer cantidad
 Hasta Que cantidad > 0
 Escribir "ok ", cantidad
FinAlgoritmo''',[(-2,0,3)])
for k,(code,ins) in T.items():
    for i in ins: run(k,code,i)
