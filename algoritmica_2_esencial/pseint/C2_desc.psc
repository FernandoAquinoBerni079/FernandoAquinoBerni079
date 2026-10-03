Algoritmo DescuentoPorMonto
 Leer cantidad, precio
 monto <- cantidad * precio
 Si monto >= 50000 Entonces
  descuento <- monto * 0.10
  monto <- monto - descuento
  Escribir "Descuento aplicado: ", descuento
 FinSi
 Escribir "Total a pagar: ", monto
FinAlgoritmo