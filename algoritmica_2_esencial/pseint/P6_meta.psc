Algoritmo MetaLibreria
    Definir acumulado, venta, tickets Como Entero
    acumulado <- 0
    tickets <- 0
    Mientras acumulado < 200000 Hacer
        Escribir "Importe del ticket:"
        Leer venta
        acumulado <- acumulado + venta
        tickets <- tickets + 1
    FinMientras
    Escribir "Meta alcanzada con ", tickets, " tickets: ", acumulado
FinAlgoritmo
