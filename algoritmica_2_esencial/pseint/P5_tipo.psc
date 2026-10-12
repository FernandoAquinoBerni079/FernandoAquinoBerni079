Algoritmo TipoPedido
    Definir cantidad Como Entero
    Escribir "Cantidad de cuadernos del pedido:"
    Leer cantidad
    Si cantidad < 12 Entonces
        Escribir "Pedido minorista"
    Sino
        Si cantidad < 50 Entonces
            Escribir "Pedido por docena"
        Sino
            Escribir "Pedido mayorista"
        FinSi
    FinSi
FinAlgoritmo
