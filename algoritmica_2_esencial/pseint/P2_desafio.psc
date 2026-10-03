Algoritmo DescuentoTrunc
    Definir total Como Entero
    Leer total
    Si total >= 100000 Entonces
        total <- trunc(total - total * 0.10)
    FinSi
    Escribir "Total final: ", total
FinAlgoritmo
