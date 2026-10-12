Algoritmo P17Envio
    Definir pedido, envio Como Entero
    Leer pedido
    Si pedido >= 70000 Entonces
        envio <- 0
        Escribir "¡Envío gratis!"
    Sino
        envio <- 8000
    FinSi
    Escribir pedido + envio
FinAlgoritmo
