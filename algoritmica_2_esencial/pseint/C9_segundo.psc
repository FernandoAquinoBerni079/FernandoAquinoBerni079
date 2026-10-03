Algoritmo P
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
FinAlgoritmo