# -*- coding: utf-8 -*-
"""Actividades de aplicación de las 21 clases (fuente única libro ↔ solucionario).
Base: las 12 actividades de cada clase del tomo vigente, emparejadas con su respuesta del solucionario
(acts_base.json). Se reemplazan las que copiaban el ejemplo resuelto de la clase o revelaban el
resultado, y las que usaban notación vieja. Marcador N = ítem nuevo o modificado (notas del piloto).
Datos nuevos (verificados por cálculo): semana 2 del copetín, matriz de bebidas, vector del ranking."""
import json

FAM = {'Ejercitá': 'Ejercitá', 'Resolvé': 'Resolvé (caso Copetín Karumbé)', 'Pensá': 'Pensá y decidí (justificá tu respuesta)', 'Desafío': 'Desafío'}
BASE = json.load(open('/home/claude/alg2/build/acts_base.json'))

SEM2 = [350000, 520000, 660000, 470000, 1250000, 900000, 330000]
DIAS = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
assert sum(SEM2) == 4480000 and sum(SEM2) // 7 == 640000
BEB = {'Cocido': [14, 9, 11, 16], 'Gaseosa': [22, 18, 25, 31], 'Jugo': [7, 10, 6, 12]}
assert [sum(v) for v in BEB.values()] == [50, 96, 35]
assert [sum(c) for c in zip(*BEB.values())] == [43, 37, 42, 59]
assert 50 * 6000 + 96 * 8000 + 35 * 7000 == 1313000
G = lambda x: '{:,}'.format(x).replace(',', '.')

_TAB_SEM2 = ('Semana 2 del copetín (ventas diarias en guaraníes)', ['Día'] + [d[:3] for d in DIAS], [['Venta'] + [G(x) for x in SEM2]])
DATOS = {
 6: [_TAB_SEM2], 7: [_TAB_SEM2], 9: [_TAB_SEM2],
 10: [('Matriz bebidas[3,4]: unidades vendidas de lunes a jueves', ['Bebida', 'Lu', 'Ma', 'Mi', 'Ju'],
       [[k] + [str(x) for x in v] for k, v in BEB.items()])],
 11: [('Vector del ranking: unid2 = unidades vendidas de seis productos en el mes', ['Posición', '1', '2', '3', '4', '5', '6'],
       [['unid2', '64', '140', '38', '92', '118', '75']])],
}

R = {}   # (clase, número) → (enunciado, respuesta)
# --- Clase 2
R[2, 6] = ('Escribí un algoritmo que lea el monto de una venta y, si llega a 30.000, muestre "Llevás un coquito de regalo"; en todos los casos, que muestre el monto.',
           'Leer monto / Si monto >= 30000 Entonces Escribir "Llevás un coquito de regalo" FinSi / Escribir "Monto: ", monto.')
R[2, 12] = ('Escribí un algoritmo que lea el importe de una venta y muestre "Con descuento" si llega a 50.000. Probalo con ventas de 45.000 y de 75.000 y anotá qué imprime en cada caso.',
            'Leer importe / Si importe >= 50000 Entonces Escribir "Con descuento" FinSi. Con 45.000: no imprime nada (45.000 >= 50.000 es F). Con 75.000: imprime "Con descuento" (V).')
# --- Clase 3
R[3, 2] = ('Indicá qué camino toma el primer ejemplo de la clase con monto = 49.999 y cuál es el total.',
           'Sino (49.999 >= 50.000 es Falso): total = 49.999, sin descuento. Un guaraní menos que el umbral alcanza para cambiar de camino.')
R[3, 8] = ('Para una venta de 9 sopas paraguayas a 10.000, indicá el monto, el camino que toma y el total final.',
           'monto = 90.000. Camino Entonces (90.000 >= 50.000 es V). Total = 90.000 − 9.000 = 81.000.')
R[3, 12] = ('Escribí un algoritmo de caja que lea el monto y, con un Si… Sino, muestre el total final y el mensaje correspondiente. Probalo con 30.000, 49.999, 50.000 y 90.000 y armá una tabla con monto, camino y total.',
            'Leer monto / Si monto >= 50000 Entonces total <- monto − monto * 0.10 ; msj <- "Aplicó descuento" Sino total <- monto ; msj <- "Sin descuento" FinSi / Escribir total, msj. Tabla: 30.000 → Sino → 30.000 ; 49.999 → Sino → 49.999 ; 50.000 → Entonces → 45.000 ; 90.000 → Entonces → 81.000.')
# --- Clase 4
R[4, 4] = ('Evaluá para monto = 75000 y enBarrio = Verdadero: (monto >= 50000) Y (enBarrio = Verdadero).',
           'Verdadero (V Y V = V): corresponde envío gratis.')
R[4, 6] = ('El copetín cambia la regla: hay envío gratis si el monto llega a 80.000 O si el cliente es socio. Escribí el algoritmo con un Si… Sino y probalo con monto = 60.000 y socio = Verdadero.',
           'Leer monto, socio / Si (monto >= 80000) O (socio = Verdadero) Entonces Escribir "Envío gratis" Sino Escribir "Envío con costo" FinSi. Con 60.000 y socio V: F O V = V → "Envío gratis".')
R[4, 12] = ('Construí la tabla de verdad completa de la condición (monto >= 80000) O (socio = Verdadero) para las cuatro combinaciones posibles, e indicá en cuántos casos hay envío gratis. Compará con la regla del ejemplo de la clase, que usaba Y.',
            'V-V → V ; V-F → V ; F-V → V ; F-F → F. Hay envío gratis en 3 de los 4 casos. Con Y había envío gratis en 1 de 4: el O es más permisivo que el Y.')
# --- Clase 5
R[5, 1] = ('Con el primer ejemplo de la clase (umbrales 20.000 y 50.000), indicá el resultado para monto = 19.999.',
           'Venta chica (19.999 < 20.000 es V).')
R[5, 2] = ('Con el mismo ejemplo, indicá el resultado para monto = 50.000.',
           'Venta grande: 50.000 < 20.000 es F y 50.000 < 50.000 es F → cae en el último Sino.')
R[5, 8] = ('Para monto = 49.999, seguí la traza del primer ejemplo paso a paso e indicá el resultado.',
           'monto = 49.999: < 20.000 es F → entra al Sino; 49.999 < 50.000 es V → "Venta mediana".')
# --- Clase 6
R[6, 5] = ('Si el jueves de la primera semana hubiera vendido 650.000 en lugar de 580.000, ¿qué imprimiría el ejemplo de la clase?',
           'Días que alcanzaron el promedio: 3 (jueves 650.000, viernes 850.000 y sábado 1.100.000 alcanzan 600.000).')
R[6, 6] = ('Escribí un algoritmo con Mientras que lea las 7 ventas de la semana 2 (tabla de datos) y cuente cuántas alcanzaron su promedio de 640.000.',
           'promedio <- 640000 ; contador <- 0 ; i <- 1 ; Mientras i <= 7 Hacer Leer venta ; Si venta >= promedio Entonces contador <- contador + 1 FinSi ; i <- i + 1 FinMientras ; Escribir contador. Resultado con la semana 2: 3 (miércoles 660.000, viernes 1.250.000 y sábado 900.000).')
R[6, 8] = ('Con la semana 2, contá a mano cuántos días superan 500.000 y escribí la condición que usaría el contador.',
           'Condición: venta > 500000. Superan 500.000: martes 520.000, miércoles 660.000, viernes 1.250.000 y sábado 900.000 → 4 días.')
R[6, 12] = ('Escribí un algoritmo que recorra las 7 ventas de la semana 2 con un Mientras, cuente los días con venta menor a 500.000 y muestre el resultado. Verificá el conteo a mano.',
            'contador <- 0 ; i <- 1 ; Mientras i <= 7 Hacer Leer venta ; Si venta < 500000 Entonces contador <- contador + 1 FinSi ; i <- i + 1 FinMientras ; Escribir contador. Menores a 500.000: lunes 350.000, jueves 470.000 y domingo 330.000 → 3 días.')
# --- Clase 7
R[7, 5] = ('Con las ventas de la semana 2 (tabla de datos), calculá el total y el promedio.',
           'Total: 4.480.000 ; promedio: 4.480.000 / 7 = 640.000.')
R[7, 6] = ('Escribí un algoritmo con Para que lea las 7 ventas de la semana 2, las acumule en total y muestre el promedio.',
           'total <- 0 ; Para i <- 1 Hasta 7 Con Paso 1 Hacer Leer venta ; total <- total + venta FinPara ; Escribir total / 7. Con la semana 2: promedio 640.000.')
R[7, 12] = ('Escribí un algoritmo que recorra las 7 ventas con un Para, acumule el total, cuente con un contador los días que alcanzaron 640.000 y active una bandera si algún día vendió más de 1.000.000. Con la semana 2, anotá total, contador y bandera.',
            'total = 4.480.000 ; contador = 3 (miércoles, viernes y sábado alcanzan 640.000) ; bandera = Verdadero (el viernes vendió 1.250.000 > 1.000.000).')
# --- Clase 8
R[8, 6] = ('Escribí un algoritmo que declare el vector ventas[7], cargue las 7 ventas de la primera semana y muestre la venta del miércoles.',
           'Dimension ventas[7] / Para i <- 1 Hasta 7 Con Paso 1 Hacer Leer ventas[i] FinPara / Escribir ventas[3]. Muestra 450.000.')
R[8, 12] = ('Escribí un algoritmo que cargue el vector ventas[7] y un vector dias[7] con los nombres, y muestre, uno por uno, cada día con su venta. Anotá qué línea aparece en sexto lugar.',
            'Dimension ventas[7], dias[7] ; cargar ambos ; Para i <- 1 Hasta 7 Con Paso 1 Hacer Escribir dias[i], ": ", ventas[i] FinPara. Sexta línea: «Sábado: 1100000».')
# --- Clase 9 (semana 2)
R[9, 2] = ('Indicá el promedio de la semana 2 si la suma es 4.480.000 y hay 7 elementos.', '640.000 (4.480.000 / 7).')
R[9, 3] = ('Indicá la posición del máximo en el vector de la semana 2.', 'Posición 5 (viernes, 1.250.000).')
R[9, 4] = ('Indicá el valor del mínimo del vector de la semana 2 y su posición.', '330.000, posición 7 (domingo).')
R[9, 6] = ('Escribí un algoritmo que recorra ventas[7] con los datos de la semana 2, acumule el total y muestre el promedio.',
           'suma <- 0 ; Para i <- 1 Hasta 7 Con Paso 1 Hacer suma <- suma + ventas[i] FinPara ; Escribir suma / 7. Resultado: 640.000.')
R[9, 7] = ('Escribí un algoritmo que encuentre el mayor elemento de ventas[7] y la posición donde está. Probalo con la semana 2.',
           'mayor <- ventas[1] ; pos <- 1 ; Para i <- 2 Hasta 7 Con Paso 1 Hacer Si ventas[i] > mayor Entonces mayor <- ventas[i] ; pos <- i FinSi FinPara ; Escribir mayor, pos. Con la semana 2: 1.250.000 en la posición 5.')
R[9, 8] = ('Escribí un algoritmo con bandera que indique si en la semana 2 hubo algún día con venta de exactamente 900.000 y, si lo hubo, en qué posición.',
           'band <- Falso ; pos <- 0 ; Para i <- 1 Hasta 7 Con Paso 1 Hacer Si ventas[i] = 900000 Entonces band <- Verdadero ; pos <- i FinSi FinPara ; Escribir band, pos. Resultado: Verdadero, posición 6 (sábado).')
R[9, 12] = ('Escribí un algoritmo que recorra ventas[7] y muestre en un solo recorrido: el total, el promedio, el mejor día (posición y valor) y el peor día. Verificá con los datos de la semana 2.',
            'Un solo Para de 1 a 7 con un acumulador y el control de mayor y menor con sus posiciones. Resultados: total 4.480.000 ; promedio 640.000 ; mejor día posición 5 (1.250.000) ; peor día posición 7 (330.000).')
# --- Clase 10 (matriz de bebidas)
R[10, 2] = ('Indicá el valor de bebidas[3,2] en la matriz de datos.', '10 (fila Jugo, columna Ma).')
R[10, 3] = ('Indicá el total de la fila de la Gaseosa.', '22 + 18 + 25 + 31 = 96.')
R[10, 4] = ('Indicá el total de la columna del jueves.', '16 + 31 + 12 = 59.')
R[10, 6] = ('Escribí un algoritmo que recorra la matriz bebidas[3,4] y muestre el total vendido por cada bebida (por fila).',
            'Para f <- 1 Hasta 3: totalFila <- 0 ; Para c <- 1 Hasta 4: totalFila <- totalFila + bebidas[f,c] FinPara ; Escribir totalFila FinPara. Resultados: Cocido 50, Gaseosa 96, Jugo 35.')
R[10, 7] = ('Escribí un algoritmo que calcule el total de cada día (por columna) de la matriz bebidas[3,4].',
            'Para c <- 1 Hasta 4: totalCol <- 0 ; Para f <- 1 Hasta 3: totalCol <- totalCol + bebidas[f,c] FinPara ; Escribir totalCol FinPara. Resultados: Lu 43, Ma 37, Mi 42, Ju 59.')
R[10, 8] = ('Calculá a mano el total general de la matriz de bebidas sumando primero por filas y verificá que coincida con la suma por columnas.',
            'Por filas: 50 + 96 + 35 = 181. Por columnas: 43 + 37 + 42 + 59 = 181. Coinciden.')
R[10, 12] = ('Escribí un algoritmo que recorra la matriz bebidas[3,4] y muestre el total por bebida, el total por día y el total general. Con los precios Cocido 6.000, Gaseosa 8.000 y Jugo 7.000 en un vector paralelo, calculá además la facturación total.',
             'Totales por fila: 50, 96, 35 ; por columna: 43, 37, 42, 59 ; total general 181. Facturación: 50 × 6.000 + 96 × 8.000 + 35 × 7.000 = 300.000 + 768.000 + 245.000 = 1.313.000.')
# --- Clase 11 (vector unid2)
R[11, 3] = ('En el vector unid2 de la tabla de datos, ¿qué valor queda primero después de ordenarlo de forma descendente y en qué posición estaba antes de ordenar?',
            '140, que estaba en la posición 2.')
R[11, 6] = ('Escribí un algoritmo que ordene de mayor a menor el vector unid2 con la burbuja optimizada (bandera hubo) e indicá el resultado.',
            'La misma burbuja de la clase con Si unid2[j] < unid2[j+1] e intercambio con aux. Resultado: [140, 118, 92, 75, 64, 38].')
R[11, 7] = ('Escribí un algoritmo que ordene unid2 de menor a mayor con el método de selección e indicá el resultado y cuántos intercambios hace.',
            'Selección: en cada vuelta busca el menor del tramo y lo lleva al frente. Resultado: [38, 64, 75, 92, 118, 140]. Hace 3 intercambios (en las vueltas 4 y 5 el menor ya está en su lugar).')
R[11, 8] = ('Con unid2 ordenado de forma descendente, escribí las instrucciones que muestran el ranking (puesto y unidades) de los tres primeros.',
            'Para k <- 1 Hasta 3 Con Paso 1 Hacer Escribir k, ".º: ", unid2[k] FinPara. Muestra 140, 118 y 92.')
R[11, 12] = ('Ordená a mano unid2 de mayor a menor con la burbuja optimizada, mostrando el vector después de cada pasada e indicando en qué pasada corta el ciclo.',
             'Pasada 1: [140, 64, 92, 118, 75, 38] ; pasada 2: [140, 92, 118, 75, 64, 38] ; pasada 3: [140, 118, 92, 75, 64, 38] ; pasada 4: sin intercambios → hubo = Falso y el ciclo corta (4 pasadas en lugar de 5).')
# --- Clase 12
R[12, 6] = ('Escribí un algoritmo que pida cuántas mesas están habilitadas y sortee la mesa que recibe un postre gratis.',
            'Leer mesas ; ganadora <- Azar(mesas) + 1 ; Escribir "Mesa ganadora: ", ganadora. Con 6 mesas, el resultado es un entero entre 1 y 6.')
# --- Clase 13
R[13, 6] = ('Usá la función CalcularTotal(precio, cantidad) de la clase para calcular el importe de 7 empanadas a 5.000.',
            'importe <- CalcularTotal(5000, 7). Devuelve 35.000.')
R[13, 8] = ('Definí una función que reciba un monto y devuelva el total con 10 % de descuento si llega a 50.000; probala con 90.000 y con 40.000.',
            'Funcion t <- Desc(monto) Si monto >= 50000 Entonces t <- monto − monto * 0.10 Sino t <- monto FinSi FinFuncion. Desc(90000) = 81.000 ; Desc(40000) = 40.000.')
R[13, 12] = ('Escribí un mini-sistema con una función CalcularTotal, una función AplicarDescuento y un procedimiento ImprimirTicket, y usalos para cobrar 6 sándwiches mixtos a 12.000. Indicá el bruto y el total final.',
             'bruto <- CalcularTotal(12000, 6) = 72.000 ; neto <- AplicarDescuento(72000) = 72.000 − 7.200 = 64.800 ; ImprimirTicket(64800). Total final: 64.800.')
# --- Clase 14
R[14, 1] = ('Indicá el resultado de Longitud("Ña Rosa").', '7 (el espacio también es un carácter).')
R[14, 3] = ('Indicá el resultado de Subcadena("SOP-07", 5, 6).', '"07".')
R[14, 6] = ('Escribí un algoritmo que lea el código de un producto (formato XXX-NN) y muestre por separado la categoría y el número usando Subcadena. Probalo con "SOP-07".',
            'Leer codigo ; cat <- Subcadena(codigo, 1, 3) ; num <- Subcadena(codigo, 5, 6) ; Escribir cat, " ", num. Con "SOP-07" → "SOP" y "07".')
R[14, 7] = ('Escribí un algoritmo que lea el nombre de una clienta y muestre su longitud y su versión en mayúsculas. Probalo con "Ña Rosa".',
            'Leer nombre ; Escribir Longitud(nombre), " ", Mayusculas(nombre). Con "Ña Rosa" → 7 y "ÑA ROSA".')
R[14, 12] = ('Escribí un algoritmo que tome el código "COC-12", extraiga la categoría y el número con Subcadena, muestre la longitud del código y arme un mensaje concatenando "Producto de categoría " con la categoría.',
             'codigo <- "COC-12" ; cat <- Subcadena(codigo, 1, 3) ; num <- Subcadena(codigo, 5, 6) ; Escribir Longitud(codigo) (= 6) ; Escribir Concatenar("Producto de categoría ", cat). Resultado: "COC", "12", 6 y "Producto de categoría COC".')
# --- Clase 15
R[15, 7] = ('Describí el contenido que tendría el archivo ventas_semana2.txt con las 7 ventas de la semana 2 (una línea por día, formato Día;monto).',
            'Lunes;350000 / Martes;520000 / Miércoles;660000 / Jueves;470000 / Viernes;1250000 / Sábado;900000 / Domingo;330000.')
# --- Clase 16 (notación única de la Unidad 3)
R[16, 1] = ('Ordená las operaciones para grabar datos en un archivo: cerrar, abrir, escribir.',
            'Abrir → escribir → cerrar. Para consultar después lo grabado, se vuelve a abrir, esta vez en modo lectura.')
R[16, 6] = ('Escribí el pseudocódigo conceptual que abre stock.txt en escritura, graba una línea por producto (código;stock) a partir de los vectores codigos[7] y stock[7], y cierra el archivo.',
            'Abrir "stock.txt" Para Escritura ; Para i <- 1 Hasta 7 Con Paso 1 Hacer Escribir Archivo codigos[i], ";", stock[i] FinPara ; Cerrar Archivo.')
R[16, 7] = ('Escribí el pseudocódigo conceptual que abre stock.txt en lectura y muestra todas las líneas guardadas, sin saber de antemano cuántas son.',
            'Abrir "stock.txt" Para Lectura ; Mientras No FinDeArchivo Hacer Leer Archivo linea ; Escribir linea FinMientras ; Cerrar Archivo.')
R[16, 12] = ('Escribí el ciclo completo del copetín con la notación de la unidad: crear el archivo del día, escribir las ventas por producto, cerrarlo, y luego volver a abrirlo en lectura para mostrar lo guardado. Indicá el orden de las operaciones.',
             'Abrir "ventas_dia.txt" Para Escritura → Escribir Archivo producto, ";", monto (en un ciclo) → Cerrar Archivo → Abrir "ventas_dia.txt" Para Lectura → Mientras No FinDeArchivo: Leer Archivo linea y mostrarla → Cerrar Archivo.')
# --- Clase 18 (carpeta raíz única)
R[18, 2] = ('Escribí la ruta de un archivo cierre.txt dentro de C:\\Karumbe\\Ventas.', 'C:\\Karumbe\\Ventas\\cierre.txt')
R[18, 6] = ('Diseñá el árbol de carpetas que usaría el copetín para guardar las compras de todo el año 2026, organizado por mes.',
            'Karumbe\\Compras\\2026\\ con una subcarpeta por mes (enero, febrero, …, diciembre).')
R[18, 7] = ('Escribí la ruta completa del archivo compras_semana.txt de marzo dentro de esa estructura.',
            'C:\\Karumbe\\Compras\\2026\\marzo\\compras_semana.txt')
R[18, 12] = ('Diseñá la estructura de carpetas completa del copetín para 2026 (ventas, compras, respaldos), con al menos dos niveles de subcarpetas, y escribí la ruta de un archivo de ejemplo dentro de ella.',
             'Karumbe\\{Ventas, Compras, Respaldos}\\2026\\{mes}\\… Ejemplo de ruta: C:\\Karumbe\\Respaldos\\2026\\abril\\ventas_semana.txt. (Se acepta toda estructura coherente con dos niveles.)')
# --- Clase 19
R[19, 3] = ('Escribí la condición del filtro «productos con stock menor a 15».', 'stock < 15')
R[19, 4] = ('Indicá qué productos quedan visibles con el filtro stock < 15 y cuántos son.', 'Sándwich mixto (8), Cocido (12) y Sopa paraguaya (6): 3 registros.')
R[19, 12] = ('Diseñá tres filtros útiles para el copetín (uno por cada campo distinto), distintos de los de la clase, escribí su condición y anticipá cuántos registros mostraría cada uno con la tabla dada.',
             'Ejemplos: stock < 15 → 3 (Mixto, Cocido, Sopa) ; categoria = "dulce" → 1 (Coquito) ; precio <= 5000 → 3 (Chipa, Empanada, Coquito). (Se aceptan filtros coherentes con la tabla y con el conteo correcto.)')
# --- Clase 20
R[20, 3] = ('Contá cuántos productos cuestan 5.000 o menos.', '3: Chipa (3.000), Empanada (5.000) y Coquito (500).')
R[20, 4] = ('Calculá el stock total de los productos salados (suma del campo stock con el criterio categoria = "salado").', '40 + 30 + 8 + 6 = 84.')
R[20, 5] = ('Si el Cocido subiera a 7.000, ¿cuál sería su valorStock?', '7.000 × 12 = 84.000.')
R[20, 6] = ('Formulá una consulta de selección que muestre nombre y precio de los productos que cuestan menos de 6.000, ordenados de menor a mayor precio.',
            'Campos nombre y precio ; criterio precio < 6000 ; orden ascendente por precio → Coquito 500 ; Chipa 3.000 ; Empanada 5.000.')
R[20, 7] = ('Formulá una consulta de totales que cuente, por categoría, los productos con stock menor a 30, e indicá el resultado.',
            'Criterio stock < 30, agrupado por categoría, Cuenta → salado 2 (Mixto, Sopa) ; bebida 2 (Gaseosa, Cocido). El grupo dulce no aparece: ningún registro dulce cumple el criterio. (La Empanada, con stock 30, no cumple «menor a 30».)')
R[20, 8] = ('La Empanada recibe 20 unidades más. Recalculá su valorStock y el total de valorStock de la tabla.',
            'Empanada: 5.000 × 50 = 250.000. Total: 798.000 + 100.000 = 898.000.')
R[20, 12] = ('Formulá cuatro consultas para el copetín —una de selección, una paramétrica, una de totales y una con campo calculado— distintas de las de la clase, e indicá el resultado de cada una con la tabla dada.',
             'Ejemplo de respuesta: selección categoria = "dulce" → Coquito ; paramétrica «¿precio máximo?» respondida con 6000 (precio <= [valor]) → Chipa, Empanada, Coquito, Cocido ; totales Máx de stock por categoría → salado 40, dulce 200, bebida 25 ; campo calculado faltan = 50 − stock para los salados → Chipa 10, Empanada 20, Mixto 42, Sopa 44. (Se aceptan consultas coherentes con resultados correctos.)')
# --- Clase 21
R[21, 2] = ('En una grilla categoría × stock con las columnas «25 o más» y «menos de 25», ¿cuántos productos salados caen en cada columna?',
            '25 o más: 2 (Chipa 40, Empanada 30) ; menos de 25: 2 (Mixto 8, Sopa 6).')
R[21, 3] = ('En esa misma grilla, ¿cuántos productos hay en total en la columna «menos de 25»?', '3: Sándwich mixto (8), Sopa paraguaya (6) y Cocido (12).')
R[21, 6] = ('Interpretá la grilla de referencias cruzadas categoría × precio de la clase: ¿qué categoría no tiene ninguna opción de hasta 5.000 y qué decisión podría tomar el copetín con ese dato?',
            'bebida: tiene 0 productos de hasta 5.000. El copetín podría sumar una bebida económica (por ejemplo, un jugo chico). Se acepta toda decisión coherente con el dato.')
R[21, 7] = ('Proponé una consulta de referencias cruzadas distinta de las de la clase (elegí qué va en filas y qué en columnas) y explicá qué mostraría.',
            'Respuesta abierta coherente. Ejemplo: filas = categoría, columnas = stock «menos de 25» / «25 o más»; mostraría cuántos productos de cada categoría están por debajo del nivel de pedido.')
R[21, 10] = ('Elegí: si una consulta de productos salados devuelve un dulce, el problema está en (el criterio / el orden de las columnas). Justificá.',
             'El criterio: el orden de las columnas cambia cómo se ve el resultado, no qué registros devuelve.')
R[21, 12] = ('Diseñá una consulta de referencias cruzadas que cruce categoría (filas) con tres tramos de stock (columnas: «menos de 10», «de 10 a 29», «30 o más») y completá la grilla con los datos de la tabla Productos, con totales.',
             'Menos de 10: Mixto 8, Sopa 6 (salado) ; de 10 a 29: Cocido 12, Gaseosa 25 (bebida) ; 30 o más: Chipa 40, Empanada 30 (salado) y Coquito 200 (dulce). Grilla: salado 2 / 0 / 2 ; dulce 0 / 0 / 1 ; bebida 0 / 2 / 0. Totales: 2 / 2 / 3 = 7. Los tramos no se solapan y cubren todo.')

# respuestas de la base que se ajustan sin cambiar el enunciado (notación o precisión)
RESP = {
 (16, 2): 'Para Escritura (o Para Agregar, si se quiere conservar lo que el archivo ya tenía).',
 (16, 3): 'Cerrar Archivo: vacía el buffer y deja todo grabado.',
}


def _fam(f):
    for k, v in FAM.items():
        if f.startswith(k):
            return v
    raise ValueError(f)


A = {}
for n in range(1, 22):
    lst = []
    for fam, k, enun, resp in BASE[str(n)]:
        nuevo = False
        if (n, k) in R:
            enun, resp = R[n, k]; nuevo = True
        if (n, k) in RESP:
            resp = RESP[n, k]; nuevo = True
        lst.append((_fam(fam), k, enun, resp, nuevo))
    A[n] = lst


def items(n):
    """Lista plana [(familia, número, enunciado, respuesta, nuevo)]."""
    return A[n]


if __name__ == '__main__':
    tot = 0
    for n in A:
        it = items(n)
        assert len(it) == 12, n
        tot += sum(1 for x in it if x[4])
    print('ítems', sum(len(A[n]) for n in A), 'nuevos o modificados', tot)
