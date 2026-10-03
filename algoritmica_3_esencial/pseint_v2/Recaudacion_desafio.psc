Algoritmo RecaudacionConContador
    Definir total, importe, i, mayores Como Entero
    Definir promedio Como Real
    total <- 0
    mayores <- 0
    Para i <- 1 Hasta 6 Hacer
        Leer importe
        total <- total + importe
        Si importe > 20000 Entonces
            mayores <- mayores + 1
        FinSi
    FinPara
    promedio <- total / 6
    Escribir "Total: ", total, "  Promedio: ", promedio, "  Mayores a 20000: ", mayores
FinAlgoritmo
