Algoritmo ControlPago
    Definir total, pago Como Entero
    Escribir "Total:"
    Leer total
    Escribir "Pago:"
    Leer pago
    Si pago >= total Entonces
        Escribir "Vuelto: ", pago - total
    Sino
        Escribir "Faltan: ", total - pago
    FinSi
FinAlgoritmo
