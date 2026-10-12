Algoritmo P21Caja
    Definir venta, suma, c, cd, mayor, bruto Como Entero
    Definir cobrar Como Real
    suma <- 0
    c <- 0
    cd <- 0
    mayor <- 0
    bruto <- 0
    Leer venta
    Mientras venta <> 0 Hacer
        Si venta >= 50000 Entonces
            cobrar <- venta - venta * 10 / 100
            cd <- cd + 1
        Sino
            cobrar <- venta
        FinSi
        suma <- suma + cobrar
        bruto <- bruto + venta
        c <- c + 1
        Si venta > mayor Entonces
            mayor <- venta
        FinSi
        Leer venta
    FinMientras
    Si c > 0 Entonces
        Escribir suma, " ", c, " ", cd, " ", suma / c, " bruto ", bruto, " desc ", bruto - suma, " mayor ", mayor
    Sino
        Escribir "sin ventas"
    FinSi
FinAlgoritmo
