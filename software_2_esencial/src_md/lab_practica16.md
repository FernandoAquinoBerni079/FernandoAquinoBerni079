@@H1 Práctica 16 — Materiales de red
Nombre y Apellido: _______________________________  Curso: ______  Fecha: ____ / ____ / ____
Competencia de la práctica: Elaborar en Excel la planilla de materiales de una red con cantidades, subtotales y verificación contra el plano.
[[IMG L_image21.jpg|10.9]]
Figura 16.3 — Selección y planificación de materiales de red.
Para esta práctica, tené a mano la Figura 16.2 de la Clase 16.
## Lo que necesitás saber
• Cada punto de red consume: un recorrido de cable, 1 roseta con jack, 1 boca de panel y 2 patch cords.
• El cable se calcula sumando los tendidos y agregando un 10 % de margen.
• Caso de esta práctica: la Farmacia Tajy de las Prácticas 14 y 15. Sus 8 puntos de red tienen tendidos de 7, 11, 14, 19, 23, 28, 41 y 52 metros.
## Actividades
Actividad 1 — Objetivo: Calcular las cantidades y armar la planilla de materiales con fórmulas.
[[CAJA Ejemplo — Modelo a reproducir]]
Tabla: Material | Cantidad | Precio unitario (G.) | Subtotal. Filas: cable UTP cat. 6 (cajas de 305 m); roseta + jack; patch panel; patch cord; canaleta (m); rack de pared; etiquetas. Las cantidades las calculás vos; los precios los provee el docente.
[[/CAJA]]
   1. En una hoja aparte, cargá los ocho tendidos y calculá el total de cable con =SUMA(...)*1,1.
   2. Calculá cuántas cajas de 305 m hacen falta con =REDONDEAR.MAS(total/305;0).
   3. Calculá los patch cords: puntos × 2 más el enlace switch–router.
   4. En la hoja principal cargá los siete materiales con sus cantidades y precios; en Subtotal usá =B2*C2 y arrastrá.
   5. Agregá la fila TOTAL con =SUMA sobre la columna de subtotales y aplicá formato de moneda.
Punto de control: Las cantidades de cable, cajas y patch cords salen de fórmulas; al cambiar un tendido, el total se actualiza solo.
Actividad 2 — Objetivo: Verificar la coherencia de las cantidades con el plano de la farmacia.
[[CAJA Ejemplo — Modelo a reproducir]]
Verificaciones: puntos de red del plano = rosetas de la planilla; bocas del patch panel ≥ puntos; patch cords = puntos × 2 + enlaces del rack; puertos del switch ≥ puntos + enlace al router.
[[/CAJA]]
   1. Abrí tu plano de la Práctica 14 y contá los puntos de red.
   2. Verificá cada regla del modelo contra tu planilla y corregí si hace falta.
   3. Agregá al pie una celda «Verificado contra plano: SÍ/NO».
   4. Guardá como Materiales_farmacia_[apellido].xlsx.
Punto de control: Cada una de las cuatro verificaciones está escrita con el número del plano y el de la planilla, y la celda final refleja el resultado.
[[CAJA Desafío final (si terminás antes)]]
Agregá una columna «% del total» que muestre el peso de cada material sobre el total general, con formato de porcentaje, y señalá cuál es el material que más pesa.
[[/CAJA]]
