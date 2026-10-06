Proceso CajaBasica
    Definir precio, cantidad, total, cobrar Como Real
    Escribir "Precio unitario:"
    Leer precio
    Escribir "Cantidad:"
    Leer cantidad
    total <- precio * cantidad
    Si total >= 50000 Entonces
        cobrar <- total - total * 10 / 100
    Sino
        cobrar <- total
    FinSi
    Escribir "Total a cobrar: ", cobrar
FinProceso
