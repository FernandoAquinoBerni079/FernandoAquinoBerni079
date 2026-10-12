Algoritmo DescuentoEstudiante
    Definir total Como Entero
    Definir esEstudiante Como Logico
    Escribir "Total:"
    Leer total
    Escribir "¿Presenta carnet de estudiante? (Verdadero/Falso)"
    Leer esEstudiante
    Si (esEstudiante = Verdadero) O (total >= 50000) Entonces
        total <- total - total * 0.10
        Escribir "Descuento estudiantil aplicado"
    Sino
        Escribir "Sin descuento"
    FinSi
    Escribir "Total final: ", total
FinAlgoritmo
