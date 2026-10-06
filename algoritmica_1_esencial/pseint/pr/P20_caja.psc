Algoritmo P20Caja
    Definir s, c, cg, venta Como Entero
    s <- 0
    c <- 0
    cg <- 0
    Leer venta
    Mientras venta <> 0 Hacer
        s <- s + venta
        c <- c + 1
        Si venta >= 10000 Entonces
            cg <- cg + 1
        FinSi
        Leer venta
    FinMientras
    Si c > 0 Entonces
        Escribir s, " ", s / c, " ", c, " ", cg
    Sino
        Escribir "sin ventas"
    FinSi
FinAlgoritmo
