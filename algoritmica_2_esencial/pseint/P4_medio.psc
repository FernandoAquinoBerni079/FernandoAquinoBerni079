Algoritmo MedioDePago
    Definir medio Como Caracter
    Definir stock Como Entero
    Escribir "Medio de pago (efectivo, QR, tarjeta, cheque):"
    Leer medio
    Escribir "Stock del artículo:"
    Leer stock
    Si NO (stock > 0) Entonces
        Escribir "Venta rechazada: sin stock"
    Sino
        Si (medio = "efectivo") O (medio = "QR") O (medio = "tarjeta") Entonces
            Escribir "Venta aceptada"
        Sino
            Escribir "Medio de pago no aceptado"
        FinSi
    FinSi
FinAlgoritmo
