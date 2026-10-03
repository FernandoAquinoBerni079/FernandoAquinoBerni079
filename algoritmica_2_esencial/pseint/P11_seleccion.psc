Algoritmo PreciosSeleccion
    Definir p, i, j, posMin, aux, inter Como Entero
    Dimension p[7]
    Para i <- 1 Hasta 7 Con Paso 1 Hacer
        Leer p[i]
    FinPara
    inter <- 0
    Para i <- 1 Hasta 6 Con Paso 1 Hacer
        posMin <- i
        Para j <- i + 1 Hasta 7 Con Paso 1 Hacer
            Si p[j] < p[posMin] Entonces
                posMin <- j
            FinSi
        FinPara
        Si posMin <> i Entonces
            aux <- p[i]
            p[i] <- p[posMin]
            p[posMin] <- aux
            inter <- inter + 1
        FinSi
    FinPara
    Para i <- 1 Hasta 7 Con Paso 1 Hacer
        Escribir Sin Saltar p[i], " "
    FinPara
    Escribir ""
    Escribir "Intercambios: ", inter
FinAlgoritmo
