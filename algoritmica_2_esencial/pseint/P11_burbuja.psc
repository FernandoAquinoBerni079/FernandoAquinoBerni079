Algoritmo RankingBurbuja
    Definir u, i, j, aux, pasadas Como Entero
    Definir nom, auxN Como Caracter
    Definir hubo Como Logico
    Dimension u[7], nom[7]
    nom[1] <- "Cuaderno"
    nom[2] <- "Bolígrafo"
    nom[3] <- "Lápiz"
    nom[4] <- "Regla"
    nom[5] <- "Carpeta"
    nom[6] <- "Resaltador"
    nom[7] <- "Goma"
    Para i <- 1 Hasta 7 Con Paso 1 Hacer
        Leer u[i]
    FinPara
    i <- 1
    pasadas <- 0
    Repetir
        hubo <- Falso
        Para j <- 1 Hasta 7 - i Con Paso 1 Hacer
            Si u[j] < u[j+1] Entonces
                aux <- u[j]
                u[j] <- u[j+1]
                u[j+1] <- aux
                auxN <- nom[j]
                nom[j] <- nom[j+1]
                nom[j+1] <- auxN
                hubo <- Verdadero
            FinSi
        FinPara
        pasadas <- pasadas + 1
        i <- i + 1
    Hasta Que NO hubo O i > 6
    Para i <- 1 Hasta 7 Con Paso 1 Hacer
        Escribir i, ". ", nom[i], " ", u[i]
    FinPara
    Escribir "Pasadas: ", pasadas
FinAlgoritmo
