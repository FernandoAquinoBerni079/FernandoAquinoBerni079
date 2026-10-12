Algoritmo Cantina5
    Definir venta, i, contador, diaBajo Como Entero
    Definir hubo Como Logico
    hubo <- Falso
    contador <- 0
    diaBajo <- 0
    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        Leer venta
        Si venta > 100000 Entonces
            contador <- contador + 1
        FinSi
        Si venta < 85000 Entonces
            hubo <- Verdadero
            diaBajo <- i
        FinSi
    FinPara
    Escribir "Días que alcanzaron 100000: ", contador
    Escribir "¿Hubo un día por debajo de 85000? ", hubo, "  (día ", diaBajo, ")"
FinAlgoritmo
