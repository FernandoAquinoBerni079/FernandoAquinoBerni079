Algoritmo CompraUtiles
    Definir cantCuad, cantBol, total, pago, vuelto Como Entero
    Escribir "Cantidad de cuadernos:"
    Leer cantCuad
    Escribir "Cantidad de bolígrafos:"
    Leer cantBol
    total <- cantCuad * 8000 + cantBol * 3000
    Escribir "Total a pagar: ", total
    Escribir "Pago del cliente:"
    Leer pago
    vuelto <- pago - total
    Escribir "Vuelto: ", vuelto
FinAlgoritmo
