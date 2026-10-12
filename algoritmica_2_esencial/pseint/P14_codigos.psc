Algoritmo CodigosArticulos
    Definir cod, cat, num, msj Como Caracter
    Escribir "Código del artículo (formato XXX-NN):"
    Leer cod
    cat <- Subcadena(cod, 1, 3)
    num <- Subcadena(cod, 5, 6)
    msj <- Concatenar("Categoría ", Mayusculas(cat))
    msj <- Concatenar(msj, ", número ")
    msj <- Concatenar(msj, num)
    Escribir msj
    Escribir "Longitud del código: ", Longitud(cod)
FinAlgoritmo
