Algoritmo EnvioLibreria
    Definir total Como Entero
    Escribir "Total de la compra:"
    Leer total
    Si total >= 150000 Entonces
        Escribir "Envío sin cargo"
    Sino
        total <- total + 15000
        Escribir "Se suma el envío: 15000"
    FinSi
    Escribir "Total final: ", total
FinAlgoritmo
