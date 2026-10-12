@@H1 Práctica 2 — La fuente de alimentación
Nombre y Apellido: _______________________________  Curso: ______  Fecha: ____ / ____ / ____
Competencia de la práctica: Interpretar la etiqueta de una fuente y calcular rangos de tolerancia en Excel.
[[IMG L_image2.jpg|10.9]]
Figura 2.3 — Referencia visual de una fuente ATX. En esta práctica de Software no se abre ni manipula la fuente.
## Lo que necesitás saber
• La etiqueta de toda fuente declara sus líneas de voltaje y su potencia. La tolerancia ATX es de ±5 % sobre el valor nominal.
• En Excel, el rango se calcula multiplicando el nominal por 0,95 y por 1,05.
## Actividades
Actividad 1 — Objetivo: Construir en Excel la tabla de tolerancias de una fuente ATX.
[[CAJA Ejemplo — Modelo a reproducir]]
Tabla con columnas: Línea | Voltaje nominal | Mínimo aceptado | Máximo aceptado. Filas: +12; +5; +3,3; +5 VSB (usar los nominales 12, 5, 3,3 y 5).
[[/CAJA]]
   1. Abrí Microsoft Excel y creá un libro en blanco.
   2. Escribí los encabezados del modelo en la fila 1 (celdas A1 a D1).
   3. Cargá las cuatro líneas con su voltaje nominal en las columnas A y B.
   4. En C2 escribí la fórmula =B2*0,95 y presioná Enter.
   5. En D2 escribí =B2*1,05 y presioná Enter.
   6. Seleccioná C2:D2 y arrastrá el controlador de relleno hasta la fila 5.
   7. Seleccioná B2:D5, andá a Inicio → grupo Número y dejá dos decimales.
   8. Guardá el libro como Tolerancias_fuente_[apellido].xlsx.
Punto de control: Cada mínimo queda por debajo y cada máximo por encima de su nominal, y al cambiar un nominal su fila se recalcula sola.
Actividad 2 — Objetivo: Decidir con la tabla si mediciones dadas están dentro de tolerancia.
[[CAJA Ejemplo — Modelo a reproducir]]
Casos a evaluar (agregalos debajo de la tabla): 12,7 V en la línea de +12; 4,9 V en la de +5; 3,1 V en la de +3,3.
[[/CAJA]]
   1. Debajo de la tabla escribí «Caso», «Medición» y «¿Aceptada?» como nuevos encabezados.
   2. Cargá los tres casos del modelo.
   3. En ¿Aceptada? escribí una fórmula que compare la medición con el mínimo y el máximo de su línea, por ejemplo =SI(Y(B8>=C2;B8<=D2);"SÍ";"NO"), ajustando las celdas a cada caso.
   4. Pintá de verde los aceptados y de rojo los rechazados con Inicio → Color de relleno.
Punto de control: Cada caso muestra SÍ o NO calculado con fórmula, y la decisión cambia sola si modificás una medición.
[[CAJA Desafío final (si terminás antes)]]
Agregá una columna «% de desvío» que calcule cuánto se aleja cada medición de su nominal, con la fórmula =(medición-nominal)/nominal y formato de porcentaje.
[[/CAJA]]
