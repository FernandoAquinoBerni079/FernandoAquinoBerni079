Algoritmo BuscarArticulo
    Definir nombres, buscado Como Caracter
    Definir i, pos Como Entero
    Dimension nombres[7]
    nombres[1] <- "Cuaderno"
    nombres[2] <- "Bolígrafo"
    nombres[3] <- "Lápiz"
    nombres[4] <- "Regla"
    nombres[5] <- "Carpeta"
    nombres[6] <- "Resaltador"
    nombres[7] <- "Goma"
    Escribir "Artículo a buscar:"
    Leer buscado
    pos <- 0
    i <- 1
    Mientras (i <= 7) Y (pos = 0) Hacer
        Si nombres[i] = buscado Entonces
            pos <- i
        FinSi
        i <- i + 1
    FinMientras
    Si pos > 0 Entonces
        Escribir buscado, " está en la posición ", pos, " (comparaciones: ", i - 1, ")"
    Sino
        Escribir buscado, " no está en la lista (comparaciones: ", i - 1, ")"
    FinSi
FinAlgoritmo
