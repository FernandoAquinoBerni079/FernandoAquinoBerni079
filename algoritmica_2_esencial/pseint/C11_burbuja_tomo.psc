Algoritmo P
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
FinAlgoritmo