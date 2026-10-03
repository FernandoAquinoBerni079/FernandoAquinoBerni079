Algoritmo RecaudacionSemana
    Definir total, importe, i Como Entero
    Definir promedio Como Real
    total <- 0
    Para i <- 1 Hasta 6 Hacer
        Escribir "Importe de la venta ", i, ":"
        Leer importe
        total <- total + importe
        Escribir "Total acumulado: ", total
    FinPara
    promedio <- total / 6
    Escribir "Total: ", total
    Escribir "Promedio: ", promedio
FinAlgoritmo
