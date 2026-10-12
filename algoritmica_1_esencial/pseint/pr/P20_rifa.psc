Algoritmo P20Rifa
    Definir monto, total, c, altos Como Entero
    total <- 0
    c <- 0
    altos <- 0
    Leer monto
    Mientras monto <> 0 Hacer
        total <- total + monto
        c <- c + 1
        Si monto > 40000 Entonces
            altos <- altos + 1
        FinSi
        Leer monto
    FinMientras
    Si c > 0 Entonces
        Escribir total, " ", c, " ", total / c, " ", altos
    Sino
        Escribir "sin talonarios"
    FinSi
FinAlgoritmo
