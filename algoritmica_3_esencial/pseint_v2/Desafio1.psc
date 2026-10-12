Algoritmo CobroConDescuento
    Definir cantMbeju, cantCocido, pago, total, vuelto Como Entero
    Leer cantMbeju
    Leer cantCocido
    Leer pago
    total <- cantMbeju * 5000 + cantCocido * 4000 + 5000
    Si total > 25000 Entonces
        total <- total - 2000
    FinSi
    Si pago >= total Entonces
        vuelto <- pago - total
        Escribir "Total: ", total, "  Vuelto: ", vuelto
    SiNo
        Escribir "El pago no alcanza"
    FinSi
FinAlgoritmo
