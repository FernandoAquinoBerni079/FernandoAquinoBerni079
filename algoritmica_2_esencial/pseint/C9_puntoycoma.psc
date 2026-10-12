Algoritmo P
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
FinAlgoritmo