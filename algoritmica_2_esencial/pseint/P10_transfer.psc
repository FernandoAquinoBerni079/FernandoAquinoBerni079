Algoritmo Cantina
    Definir m, f, c, t Como Entero
    Dimension m[2,3]
    Para f <- 1 Hasta 2 Con Paso 1 Hacer
        Para c <- 1 Hasta 3 Con Paso 1 Hacer
            Leer m[f,c]
        FinPara
    FinPara
    Para f <- 1 Hasta 2 Con Paso 1 Hacer
        t <- 0
        Para c <- 1 Hasta 3 Con Paso 1 Hacer
            t <- t + m[f,c]
        FinPara
        Escribir "Fila ", f, ": ", t
    FinPara
    Para c <- 1 Hasta 3 Con Paso 1 Hacer
        t <- 0
        Para f <- 1 Hasta 2 Con Paso 1 Hacer
            t <- t + m[f,c]
        FinPara
        Escribir "Columna ", c, ": ", t
    FinPara
FinAlgoritmo
