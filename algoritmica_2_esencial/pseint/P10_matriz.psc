Algoritmo MatrizVentas
    Definir v, f, c, totalFila, totalCol, general, mejorDia, mejorCol, facturacion Como Entero
    Definir precio Como Entero
    Dimension v[3,5], precio[3]
    Para f <- 1 Hasta 3 Con Paso 1 Hacer
        Para c <- 1 Hasta 5 Con Paso 1 Hacer
            Leer v[f,c]
        FinPara
    FinPara
    precio[1] <- 8000
    precio[2] <- 3000
    precio[3] <- 15000
    general <- 0
    facturacion <- 0
    Para f <- 1 Hasta 3 Con Paso 1 Hacer
        totalFila <- 0
        Para c <- 1 Hasta 5 Con Paso 1 Hacer
            totalFila <- totalFila + v[f,c]
        FinPara
        Escribir "Fila ", f, ": ", totalFila, " unidades, ", totalFila * precio[f], " guaraníes"
        general <- general + totalFila
        facturacion <- facturacion + totalFila * precio[f]
    FinPara
    mejorCol <- 0
    mejorDia <- 0
    Para c <- 1 Hasta 5 Con Paso 1 Hacer
        totalCol <- 0
        Para f <- 1 Hasta 3 Con Paso 1 Hacer
            totalCol <- totalCol + v[f,c]
        FinPara
        Escribir "Día ", c, ": ", totalCol
        Si totalCol > mejorCol Entonces
            mejorCol <- totalCol
            mejorDia <- c
        FinSi
    FinPara
    Escribir "Total general: ", general, "  Facturación: ", facturacion
    Escribir "Día de más unidades: ", mejorDia, " (", mejorCol, ")"
FinAlgoritmo
