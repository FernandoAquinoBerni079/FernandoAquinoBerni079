Funcion importe <- CalcularImporte(precio, cantidad)
    importe <- precio * cantidad
FinFuncion

Algoritmo TresLineas
    Definir total Como Entero
    total <- CalcularImporte(8000, 5) + CalcularImporte(3000, 10) + CalcularImporte(1500, 4)
    Escribir "Total del pedido: ", total
FinAlgoritmo
