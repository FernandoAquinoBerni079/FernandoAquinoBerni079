Algoritmo ConsultaArticulo
    Definir precios, i, num Como Entero
    Definir nombres Como Caracter
    Dimension precios[7], nombres[7]
    nombres[1] <- "Cuaderno"
    nombres[2] <- "Bolígrafo"
    nombres[3] <- "Lápiz"
    nombres[4] <- "Regla"
    nombres[5] <- "Carpeta"
    nombres[6] <- "Resaltador"
    nombres[7] <- "Goma"
    precios[1] <- 8000
    precios[2] <- 3000
    precios[3] <- 2000
    precios[4] <- 4000
    precios[5] <- 15000
    precios[6] <- 6000
    precios[7] <- 1500
    Escribir "Número de artículo (1 a 7):"
    Leer num
    Si (num >= 1) Y (num <= 7) Entonces
        Escribir nombres[num], ": ", precios[num]
    Sino
        Escribir "No existe ese artículo"
    FinSi
FinAlgoritmo
