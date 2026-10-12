Algoritmo ValidarCodigo
    Definir cod Como Caracter
    Leer cod
    Si (Longitud(cod) = 6) Y (Subcadena(cod, 4, 4) = "-") Entonces
        Escribir cod, ": formato válido"
    Sino
        Escribir cod, ": formato inválido"
    FinSi
FinAlgoritmo
