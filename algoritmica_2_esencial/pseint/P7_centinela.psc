Algoritmo TicketsDelTurno
    Definir importe, total, cantidad Como Entero
    total <- 0
    cantidad <- 0
    Escribir "Importe (0 para cerrar):"
    Leer importe
    Mientras importe <> 0 Hacer
        total <- total + importe
        cantidad <- cantidad + 1
        Escribir "Importe (0 para cerrar):"
        Leer importe
    FinMientras
    Escribir "Tickets: ", cantidad, "  Total: ", total
FinAlgoritmo
