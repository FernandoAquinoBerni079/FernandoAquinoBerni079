Funcion total <- CalcularTotal(precio, cantidad)
 total <- precio * cantidad
FinFuncion
Funcion neto <- AplicarDescuento(monto)
 Si monto >= 50000 Entonces
  neto <- monto - monto * 0.10
 Sino
  neto <- monto
 FinSi
FinFuncion
SubProceso ImprimirTicket(total)
 Escribir "Copetín Karumbé - Total: G. ", total
FinSubProceso
Algoritmo Caja
 Leer precio, cantidad
 bruto <- CalcularTotal(precio, cantidad)
 neto <- AplicarDescuento(bruto)
 ImprimirTicket(neto)
FinAlgoritmo