@@H1 Práctica 17 — Medios de transmisión guiados
Nombre y Apellido: _______________________________  Curso: ______  Fecha: ____ / ____ / ____
Competencia de la práctica: Resolver escenarios de selección de medio guiado y presentar la decisión en una tabla comparativa.
[[IMG L_image23.jpg|10.9]]
Figura 17.3 — Referencia visual de cable y conector RJ-45. En esta práctica de Software no se realiza crimpado ni certificación física.
## Lo que necesitás saber
• La decisión de medio combina distancia, interferencia, velocidad requerida y costo.
• Una tabla de decisión hace visible el criterio, no solo el resultado.
## Actividades
Actividad 1 — Objetivo: Completar en Excel la tabla de decisión de cuatro escenarios.
[[CAJA Ejemplo — Modelo a reproducir]]
Tabla: Escenario | Distancia (m) | ¿Interferencia? | Velocidad requerida | Medio elegido | Justificación (una línea). Escenarios: (1) consultorio a 45 m del rack; (2) lavandería industrial con motores grandes, a 70 m; (3) unión de dos sucursales vecinas a 230 m; (4) cámaras analógicas que ya funcionan con su cable.
[[/CAJA]]
   1. Abrí Excel y cargá los encabezados y los cuatro escenarios con sus datos.
   2. Decidí el medio de cada escenario con la tabla de la clase.
   3. Escribí la justificación de una línea por escenario.
   4. Aplicá ajuste de texto a la columna de justificación: Inicio → Ajustar texto.
Punto de control: Los cuatro escenarios tienen medio elegido y justificación, y cada justificación nombra el criterio que decidió (distancia, interferencia, velocidad o costo).
Actividad 2 — Objetivo: Verificar las decisiones con la regla de los 100 metros.
[[CAJA Ejemplo — Modelo a reproducir]]
Columna extra «¿Supera 100 m?» con la fórmula =SI(B2>100;"SÍ";"NO").
[[/CAJA]]
   1. Agregá la columna del modelo después de Distancia.
   2. Escribí la fórmula en la primera fila y arrastrá.
   3. Revisá que ningún escenario marcado SÍ tenga UTP como medio elegido; si lo tiene, corregí la decisión.
   4. Guardá como Medios_guiados_[apellido].xlsx.
Punto de control: La columna se calcula con fórmula y ningún escenario marcado SÍ queda resuelto con par trenzado en un único tramo.
[[CAJA Desafío final (si terminás antes)]]
Agregá un quinto escenario de tu invención donde la mejor respuesta sea un cable apantallado y no la fibra, y justificalo.
[[/CAJA]]
