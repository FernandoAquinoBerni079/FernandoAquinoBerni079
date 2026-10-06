Algoritmo P15Expr
    Definir a, b, c, total, cantidad Como Entero
    Definir medioPago Como Caracter
    Escribir 7 + 2 * 3, " ", (7 + 2) * 3, " ", 18 - 6 / 2, " ", 4 * 5 - 3 * 2, " ", 100 - (20 + 5) * 2
    a <- 12
    b <- 12
    c <- 5
    Escribir a > b, " ", a >= b, " ", c <> 5, " ", a - b = 0, " ", c * 3 <= a + b
    total <- 58000
    cantidad <- 4
    medioPago <- "efectivo"
    Escribir (total >= 60000) Y (medioPago = "QR")
    Escribir (total >= 60000) O (cantidad >= 4)
    Escribir NO (medioPago = "QR")
    Escribir (total > 50000) Y (cantidad < 10) Y (medioPago = "efectivo")
    Escribir (total > 50000) Y (medioPago = "efectivo")
    medioPago <- "QR"
    Escribir (total > 50000) Y (medioPago = "efectivo")
FinAlgoritmo
