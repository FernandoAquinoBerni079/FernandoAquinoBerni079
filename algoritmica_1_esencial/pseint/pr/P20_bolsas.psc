Algoritmo P20Bolsas
    Definir kilos, total, bolsas, mayor Como Entero
    total <- 0
    bolsas <- 0
    mayor <- 0
    Leer kilos
    Mientras kilos <> 0 Hacer
        total <- total + kilos
        bolsas <- bolsas + 1
        Si kilos > mayor Entonces
            mayor <- kilos
        FinSi
        Leer kilos
    FinMientras
    Si bolsas > 0 Entonces
        Escribir total, " ", bolsas, " ", total / bolsas, " ", mayor
    Sino
        Escribir "sin bolsas"
    FinSi
FinAlgoritmo
