Algoritmo P
 codigo <- "MIX-01"
 Escribir Subcadena(codigo, 1, 3), "|", Subcadena(codigo, 5, 6), "|", Longitud(codigo)
 Escribir Longitud("María"), "|", Mayusculas("María"), "|", Mayusculas("chipa"), "|", Longitud("Ramón"), "|", Mayusculas("Ramón")
 Escribir Concatenar("EMP", "-01"), "|", "MIX" + "-01", "|", Subcadena("Sándwich mixto", 1, 8)
 nombre <- "Sopa paraguaya"
 cuenta <- 0
 Para i <- 1 Hasta Longitud(nombre) Con Paso 1 Hacer
  Si Subcadena(nombre, i, i) = "a" Entonces
   cuenta <- cuenta + 1
  FinSi
 FinPara
 Escribir cuenta
 Escribir "chipa" < "empanada", "|", "Chipa" = "chipa", "|", "Zapallo" < "anana"
FinAlgoritmo