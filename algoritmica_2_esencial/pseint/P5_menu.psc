Algoritmo MenuLibreria
    Definir opcion, precio Como Entero
    Escribir "1 Cuaderno  2 Bolígrafo  3 Lápiz  4 Regla  5 Carpeta"
    Leer opcion
    precio <- 0
    Segun opcion Hacer
        1:
            precio <- 8000
        2:
            precio <- 3000
        3:
            precio <- 2000
        4:
            precio <- 4000
        5:
            precio <- 15000
        De Otro Modo:
            Escribir "Opción inválida"
    FinSegun
    Si precio > 0 Entonces
        Escribir "Precio: ", precio
    FinSi
FinAlgoritmo
