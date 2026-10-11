@@H1 Práctica 15 — Equipos de red
Nombre y Apellido: _______________________________  Curso: ______  Fecha: ____ / ____ / ____
Competencia de la práctica: Armar una ficha comparativa de switches y justificar la elección para la red de un cliente.
Para esta práctica, tené a mano las Figuras 15.1 y 15.2 de la Clase 15.
## Lo que necesitás saber
• Los switches se comparan por puertos, velocidad por puerto, si son administrables y si tienen puertos PoE.
• Las bocas necesarias se calculan sumando los equipos cableados, los access points y el enlace al router, más una reserva de al menos 20 %.
• Caso de esta práctica: la red de la Farmacia Tajy de la Práctica 14 (6 computadoras, 1 impresora de red, 1 access point en el techo y el router).
## Actividades
Actividad 1 — Objetivo: Cargar en Excel la comparativa de tres switches (precios provistos por el docente o tomados de publicaciones impresas).
[[CAJA Ejemplo — Modelo a reproducir]]
Tabla: Modelo | Puertos | Velocidad por puerto | ¿PoE? | Precio (G.). Tres filas: 8 puertos Gigabit sin PoE; 16 puertos Gigabit sin PoE; 16 puertos Gigabit con 4 puertos PoE.
[[/CAJA]]
   1. Abrí Excel y cargá los encabezados y las tres opciones con los datos provistos.
   2. Agregá la columna «G. por puerto» con la fórmula =E2/B2 y arrastrá.
   3. Aplicá formato de moneda a los precios.
   4. Ordená la tabla por precio: seleccioná los datos y usá Datos → Ordenar.
Punto de control: La columna G. por puerto se calcula sola y la tabla queda ordenada por precio.
Actividad 2 — Objetivo: Elegir el switch de la farmacia y justificarlo por escrito.
[[CAJA Ejemplo — Modelo a reproducir]]
Debajo de la tabla, tres líneas: cuenta de bocas ocupadas con su reserva; switch elegido y por qué; opciones descartadas y por qué.
[[/CAJA]]
   1. Contá en tu plano de la Práctica 14 las bocas que se ocupan en el switch, incluido el enlace al router.
   2. Calculá la reserva del 20 % con una fórmula en Excel y redondeá hacia arriba.
   3. Decidí si el access point del techo necesita PoE y tenelo en cuenta en la elección.
   4. Escribí la elección justificada en las tres líneas del modelo y resaltá con relleno verde la fila elegida.
   5. Guardá como Switch_farmacia_[apellido].xlsx.
Punto de control: La cuenta de bocas y la reserva se calculan con fórmula, y la justificación menciona la cantidad de puertos y la alimentación del access point.
[[CAJA Desafío final (si terminás antes)]]
La farmacia planea abrir dos cajas más el año próximo. Recalculá las bocas y explicá en una línea si tu elección sigue sirviendo.
[[/CAJA]]
