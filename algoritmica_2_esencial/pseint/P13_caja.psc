Funcion importe <- CalcularImporte(precio, cantidad)
    importe <- precio * cantidad
FinFuncion

Funcion neto <- AplicarDescuento(monto)
    Si monto >= 100000 Entonces
        neto <- monto - monto * 0.10
    Sino
        neto <- monto
    FinSi
FinFuncion

SubProceso MostrarTicket(articulo, total)
    Escribir "Librería Arandu | ", articulo, " | Total: ", total
FinSubProceso

Algoritmo CajaArandu
    Definir art Como Caracter
    Definir p, c, bruto, final Como Entero
    Escribir "Artículo, precio y cantidad:"
    Leer art, p, c
    bruto <- CalcularImporte(p, c)
    final <- AplicarDescuento(bruto)
    MostrarTicket(art, final)
FinAlgoritmo
