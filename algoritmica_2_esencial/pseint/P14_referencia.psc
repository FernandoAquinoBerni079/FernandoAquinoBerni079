SubProceso RecargoValor(monto)
    monto <- monto + 5000
    Escribir "Dentro (por valor): ", monto
FinSubProceso

SubProceso RecargoRef(monto Por Referencia)
    monto <- monto + 5000
    Escribir "Dentro (por referencia): ", monto
FinSubProceso

Algoritmo PasajeParametros
    Definir total Como Entero
    total <- 40000
    RecargoValor(total)
    Escribir "Después del pasaje por valor: ", total
    RecargoRef(total)
    Escribir "Después del pasaje por referencia: ", total
FinAlgoritmo
