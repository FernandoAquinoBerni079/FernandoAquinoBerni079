SubProceso AplicarDescuento(monto Por Referencia)
 Si monto >= 50000 Entonces
  monto <- monto - monto * 0.10
 FinSi
FinSubProceso
Algoritmo ProbarReferencia
 Definir monto Como Real
 monto <- 60000
 AplicarDescuento(monto)
 Escribir monto
FinAlgoritmo