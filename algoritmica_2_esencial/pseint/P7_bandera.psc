Algoritmo ControlSemana
    Definir venta, i, contador, diaBajo Como Entero
    Definir hubo Como Logico
    hubo <- Falso
    contador <- 0
    diaBajo <- 0
    Para i <- 1 Hasta 6 Con Paso 1 Hacer
        Leer venta
        Si venta >= 230000 Entonces
            contador <- contador + 1
        FinSi
        Si venta < 160000 Entonces
            hubo <- Verdadero
            diaBajo <- i
        FinSi
    FinPara
    Escribir "Días que alcanzaron 230000: ", contador
    Escribir "¿Hubo un día por debajo de 160000? ", hubo, "  (día ", diaBajo, ")"
FinAlgoritmo
