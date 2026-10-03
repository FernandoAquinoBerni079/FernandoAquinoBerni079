Algoritmo UnidadesSemana
    Definir unid, i, total, sobre, mayor, posMayor, menor, posMenor Como Entero
    Definir promedio Como Real
    Dimension unid[7]
    Para i <- 1 Hasta 7 Con Paso 1 Hacer
        Leer unid[i]
    FinPara
    total <- 0
    Para i <- 1 Hasta 7 Con Paso 1 Hacer
        total <- total + unid[i]
    FinPara
    promedio <- total / 7
    sobre <- 0
    mayor <- unid[1]
    posMayor <- 1
    menor <- unid[1]
    posMenor <- 1
    Para i <- 1 Hasta 7 Con Paso 1 Hacer
        Si unid[i] > promedio Entonces
            sobre <- sobre + 1
        FinSi
        Si unid[i] > mayor Entonces
            mayor <- unid[i]
            posMayor <- i
        FinSi
        Si unid[i] < menor Entonces
            menor <- unid[i]
            posMenor <- i
        FinSi
    FinPara
    Escribir "Total: ", total, "  Promedio: ", promedio, "  Sobre el promedio: ", sobre
    Escribir "Mayor: ", mayor, " (posición ", posMayor, ")  Menor: ", menor, " (posición ", posMenor, ")"
FinAlgoritmo
