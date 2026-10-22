# Cierre de revisión R3 · Informática 2.º BTC

R3 se construye a partir de R2 con `build/r3_2btc.py`.
- **R2 queda intacta.** Comprobé las huellas SHA-256 de los cinco DOCX R2 antes y después de construir R3.
- Cada cambio queda en `build/registro_r3_2btc.json` y en `BITACORA_R2_R3_2BTC.md`.
- Páginas R3: tomo 75 · laboratorio 26 (R2: 23) · plan anual 4 · solucionario 23 · planes 37.
- Se mantienen las 116 claves de opción múltiple, verificadas otra vez sobre R3.

Ninguno de estos cambios declara aptitud comercial. La validación institucional, las pruebas en software y la
aprobación final siguen pendientes.

## A. Resueltas en R3 (ajustes editoriales)

| ID | Origen | Qué cambió | Dónde | Estado |
|---|---|---|---|---|
| R3-2-01 | Pedido de revisión (legibilidad) y O-2-09 | Las figuras del laboratorio ya no bajan de 7 pt (antes llegaban a 4,5 pt). Cada figura va al ancho más grande con el que su práctica entra en una página, sin bajar de su ancho mínimo para 7 pt. Las Prácticas 1, 10 y 14 pasan a dos páginas, y su segunda página lleva renglones de anotaciones de 8 mm hasta el pie. Las Prácticas 10 y 14 recuperan los tres renglones de anotaciones que R2 les había quitado | Laboratorio | Resuelto en el archivo; falta la prueba de impresión |
| R3-2-02 | O-2-05 | Figura 1: el ícono verde parecido al de una planilla comercial pasa a ser una cuadrícula neutra en el azul de la colección | Tomo Clase 1 y Práctica 1 | Resuelto; requiere aprobación de Fernando (comparación, pág. 1) |
| R3-2-03 | O-2-01 | Unificación del nombre del libro: el caso tiene un solo libro, `Honorarios_Arandu_2026`, y Sueldos es una hoja de ese libro. La actividad 4.2 de la Clase 2 pedía nombrar «el libro de sueldos», que no existe. Nueva consigna: nombrar un libro aparte para los sueldos de 2027. La clave queda como `Sueldos_Arandu_2027` | Tomo Clase 2, 4.2; Solucionario Clase 2, 4.2 | Resuelto |
| R3-2-04 | Hallazgo nuevo de esta revisión | Figura 2: la celda B3 mostraba «900.000», pero en el caso la columna B es Régimen y el importe está en C. Ahora muestra «SIMPLE» en la celda y en el rango | Tomo Clase 2 y Práctica 2 | Resuelto; requiere aprobación de Fernando (comparación, pág. 2) |
| R3-2-05 | O-2-02 | Las orientaciones de los desafíos estaban dos veces en el solucionario: un bloque breve (P4, P5, P9, P10, P14, P16, P17 y P18) y otro completo de las veinte prácticas. Quedó un solo bloque. Comprobé que cada orientación eliminada figura con igual o mayor detalle en el que queda | Solucionario, «Orientaciones sobre los desafíos» | Resuelto |
| R3-2-06 | O-2-04 | Nota de alcance en la Clase 16: el primer ejemplo de SI, con dos resultados, también rotularía como SIMPLE a los clientes GENERAL; para tres categorías hace falta el SI anidado | Tomo Clase 16 | Resuelto |
| R3-2-07 | Hallazgo nuevo de esta revisión | El punto de control de la Práctica 20 exige mencionar el buzón tributario, pero ningún paso lo pedía. El paso 7 ahora lo pide | Laboratorio Práctica 20, paso 7 | Resuelto |
| R3-2-08 | O-2-03 | El Plan 16 citaba como instrumento la Evaluación de la Unidad 3, que se aplica en el Plan 17. Su instrumento ahora es una lista de cotejo de la hoja Resultado | Planes de clase, Plan 16 | Resuelto |

## B. Decisiones de Fernando (editoriales, no institucionales)

| ID | Tema | Situación | Opciones |
|---|---|---|---|
| D-2-01 | Figuras incorporadas y reconstruidas | Las 13 figuras están en la comparación `COMPARACION_PARA_APROBACION_2BTC.pdf`, con casillas de aprobación | Aprobar, aprobar con cambios o rechazar cada una |
| D-2-02 | Encuentros 33-35 | Redistribución hecha en R2 y que se mantiene en R3, sin cambiar 36 encuentros ni 72 HC. Ver las páginas de los planes y del plan anual en la comparación | Aprobar o volver a la distribución R1 |
| D-2-03 | Evaluaciones de unidad en dos páginas (O-2-06) | Las seis pasan su última pregunta abierta (4.2) a una segunda página. Probé con dos renglones en vez de tres por pregunta: siguen en dos páginas. Achicar más quitaría espacio de respuesta | a) Mantener: cada evaluación es una hoja doble faz (recomendado). b) Pasar 4.2 a una pregunta de completar. c) Reducir la letra de las consignas |
| D-2-04 | Laboratorio de 26 páginas | Tres prácticas pasan a dos páginas para conservar la legibilidad | Aceptar, o aprobar figuras simplificadas para esas tres prácticas |
| D-2-05 | Renglones de escritura del cuaderno (hallazgo nuevo) | Los tres renglones de «Anotaciones» de cada práctica vienen de R1 con un paso de 3,2 mm: no alcanzan para escribir a mano. Los renglones agregados en R3 ya tienen 8 mm. Pasar también los originales a 8 mm suma unos 15 mm por práctica, y varias prácticas más pasarían a dos páginas | a) Pasar todos a 8 mm y aceptar más páginas (recomendado). b) Mantenerlos y pedir las anotaciones en hoja aparte |

## C. Requieren decisión institucional o verificación externa (no se cierran)

| ID | Tema | Quién | Qué se necesita |
|---|---|---|---|
| O-2-07 | Hora cátedra de 40 minutos y 36 encuentros | Institución | Ratificación escrita del calendario y de la duración |
| O-2-08 | RG DNIT 54/2026 y demás referencias legales | Verificación desde otro entorno | Ver `VERIFICACION_LEGAL_PENDIENTE_2BTC.md`: lista exacta de normas, afirmaciones y páginas |
| O-2-10 | Prácticas en software real | Docente de laboratorio | Ver `PRUEBAS_PRACTICAS_2BTC.md` |
| O-2-11 | Programa vigente (edición de 2014) | Institución | Confirmar que el programa BTC de Informática de 2.º sigue vigente |
| O-2-09 (impresión) | Prueba física | Imprenta o institución | Imprimir y verificar según `PRUEBAS_PRACTICAS_2BTC.md` |
