Algoritmo SemanaLibreria
    Definir venta, total, i, dias Como Entero
    Definir promedio Como Real
    total <- 0
    Para i <- 1 Hasta 6 Con Paso 1 Hacer
        Escribir "Venta del día ", i, ":"
        Leer venta
        total <- total + venta
    FinPara
    promedio <- total / 6
    Escribir "Total: ", total
    Escribir "Promedio: ", promedio
FinAlgoritmo
