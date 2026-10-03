Algoritmo ValidarCantidad
    Definir stock, cantidad, intentos Como Entero
    stock <- 12
    intentos <- 0
    Repetir
        Escribir "Cantidad de carpetas (1 a ", stock, "):"
        Leer cantidad
        intentos <- intentos + 1
    Hasta Que (cantidad >= 1) Y (cantidad <= stock)
    Escribir "Cantidad aceptada: ", cantidad, " en ", intentos, " intentos"
FinAlgoritmo
