Algoritmo DescuentoLibreria
    Definir total Como Entero
    Escribir "Total de la compra:"
    Leer total
    Si total >= 100000 Entonces
        total <- total - total * 0.10
        Escribir "Se aplicó el 10 % de descuento"
    FinSi
    Escribir "Total final: ", total
FinAlgoritmo
