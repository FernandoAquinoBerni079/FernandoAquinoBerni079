Algoritmo CierreDeCaja
 total <- 0
 cantidad <- 0
 Repetir
  Leer monto
  Si monto <> 0 Entonces
   total <- total + monto
   cantidad <- cantidad + 1
  FinSi
 Hasta Que monto = 0
 Si cantidad > 0 Entonces
  promedio <- total / cantidad
  Escribir cantidad, " ventas - Total: ", total, " - Promedio: ", promedio
 Sino
  Escribir "No se cargaron ventas"
 FinSi
FinAlgoritmo