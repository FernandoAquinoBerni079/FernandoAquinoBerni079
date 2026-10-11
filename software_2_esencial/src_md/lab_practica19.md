@@H1 Práctica 19 — Cableado estructurado
Nombre y Apellido: _______________________________  Curso: ______  Fecha: ____ / ____ / ____
Competencia de la práctica: Verificar en planilla el cumplimiento de la regla de los 100 metros para todos los puntos de una instalación y documentar el esquema de conexión.
Para esta práctica, tené a mano las Figuras 19.1 y 19.2 de la Clase 19.
## Lo que necesitás saber
• Canal = tendido fijo + patch cords. El tendido fijo no debe superar 90 m y el canal no debe superar 100 m: se verifican las dos condiciones.
• La función SI combinada con Y marca automáticamente los cumplimientos.
• Caso de esta práctica: la ampliación de la Farmacia Tajy en su nuevo local, con ocho puntos de 9, 12, 17, 20, 25, 31, 43 y 55 metros de tendido fijo, cordones de 2 m en el puesto y 3 m en el rack, y un punto de prueba que agrega tu docente.
## Actividades
Actividad 1 — Objetivo: Armar la planilla de canales de la farmacia.
[[CAJA Ejemplo — Modelo a reproducir]]
Tabla: Punto | Tendido fijo (m) | Cordones (m) | Canal (m) | ¿Cumple? Ocho puntos con los tendidos del nuevo local y un punto de prueba de 93 m de tendido fijo.
[[/CAJA]]
   1. Abrí Excel y cargá encabezados, los ocho puntos y el punto de prueba.
   2. Cargá 5 en la columna Cordones para todos los puntos (2 m + 3 m).
   3. En Canal usá =B2+C2 y arrastrá.
   4. En ¿Cumple? usá =SI(Y(B2<=90;D2<=100);"SÍ";"NO") y arrastrá.
   5. Aplicá formato condicional: seleccioná la columna ¿Cumple?, Inicio → Formato condicional → Resaltar reglas → Es igual a NO, relleno rojo.
Punto de control: La fórmula evalúa las dos condiciones y, si cambiás un tendido, el resultado y el color se actualizan solos.
Actividad 2 — Objetivo: Documentar el esquema de conexión y explicar el punto de prueba.
[[CAJA Ejemplo — Modelo a reproducir]]
Debajo de la tabla: «Esquema adoptado: T568B en toda la instalación», una línea que explique por qué no se mezclan esquemas y otra que explique qué condición falla en el punto de prueba.
[[/CAJA]]
   1. Escribí la declaración del modelo debajo de la tabla.
   2. Agregá las dos líneas de justificación con tus palabras.
   3. Verificá ortografía con Revisar → Ortografía.
   4. Guardá como Canales_farmacia_[apellido].xlsx.
Punto de control: La planilla cierra con el esquema declarado y la explicación del punto de prueba nombra la condición que no se cumple.
[[CAJA Desafío final (si terminás antes)]]
Agregá una columna «Margen (m)» = 100 − canal y detectá qué punto real del nuevo local tiene el menor margen.
[[/CAJA]]
