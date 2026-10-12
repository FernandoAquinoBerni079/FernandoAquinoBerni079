Algoritmo CobroParaLlevar
    Definir cantMbeju, cantCocido, pago, total, vuelto Como Entero
    Escribir "Cantidad de mbeju:"
    Leer cantMbeju
    Escribir "Cantidad de cocidos:"
    Leer cantCocido
    Escribir "Pago:"
    Leer pago
    total <- cantMbeju + 5000 + cantCocido * 4000 + 5000
    Si pago >= total Entonces
        vuelto <- pago - total
        Escribir "Total: ", total, "  Vuelto: ", vuelto
    SiNo
        Escribir "El pago no alcanza"
    FinSi
FinAlgoritmo
