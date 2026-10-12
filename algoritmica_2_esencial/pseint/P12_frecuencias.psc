Algoritmo SimulacionCompras
    Definir frec, i, u, suma Como Entero
    Dimension frec[6]
    Para i <- 1 Hasta 6 Con Paso 1 Hacer
        frec[i] <- 0
    FinPara
    Para i <- 1 Hasta 20 Con Paso 1 Hacer
        u <- Azar(6) + 1
        frec[u] <- frec[u] + 1
    FinPara
    suma <- 0
    Para i <- 1 Hasta 6 Con Paso 1 Hacer
        Escribir i, " unidades: ", frec[i], " clientes"
        suma <- suma + frec[i]
    FinPara
    Escribir "Clientes simulados: ", suma
FinAlgoritmo
