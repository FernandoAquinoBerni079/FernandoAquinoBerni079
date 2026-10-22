# Cierre de revisión R3 · Informática 3.º BTC

R3 se construye a partir de R2 con `build/r3_3btc.py`.
- **R2 queda intacta.** Comprobé las huellas SHA-256 de los cinco DOCX R2 después de construir R3.
- Cada cambio queda en `build/registro_r3_3btc.json` y en `BITACORA_R2_R3_3BTC.md`.
- Páginas R3: tomo 77 (igual que R2) · laboratorio 33 (R2: 22) · plan anual 7 · solucionario 22 · planes 37.
- Se mantienen las 119 claves de opción múltiple, verificadas otra vez sobre R3.

Ninguno de estos cambios declara aptitud comercial. La validación institucional, las pruebas en software y la
aprobación final siguen pendientes.

## A. Resueltas en R3 (ajustes editoriales)

| ID | Origen | Qué cambió | Dónde | Estado |
|---|---|---|---|---|
| R3-3-01 | Pedido de revisión (legibilidad) y O-3-03 | Tomo: las 20 figuras pasan de 14,2 a 15,5 cm y ningún texto queda debajo de 7 pt (antes había textos de 6,0-6,7 pt). Laboratorio: figuras de 11,5 a 15,5 cm, cuando antes iban a 9,6 cm (texto de 3-7 pt); once prácticas pasan a dos páginas, con renglones de registro de 8 mm hasta el pie. Detalle en `LEGIBILIDAD_R3_3BTC.md` | Tomo y Laboratorio | Resuelto en el archivo. Figuras 12 y 18 justo en 7 pt (D-3-01). Falta la prueba de impresión |
| R3-3-02 | O-3-03 | Figura 2: la nota de 6 pt sale de la imagen y pasa al pie de figura | Tomo Clase 2; Práctica 2 | Resuelto; requiere aprobación (comparación, pág. 2) |
| R3-3-03 | O-3-03 y criterio de marcas | Figura 19: nota «Esquema didáctico…» de 6,4 a 8,8 pt; «WhatsApp» pasa a «Mensajería», como dice el texto de la Clase 19 | Tomo Clase 19; Práctica 19 | Resuelto; requiere aprobación (comparación, pág. 19) |
| R3-3-04 | O-3-06 | Nota de alcance en la Clase 2: los registros que exige la ley dependen del régimen. San Blas lleva contabilidad completa para practicar todos los libros, y el profesional verifica en cada caso real qué registros corresponden | Tomo Clase 2, «El régimen tributario en la configuración» | Resuelto |
| R3-3-05 | O-3-07 | El recuadro de la Clase 3 menciona también la Ley 7593/2025: «ya fue publicada y amplía ese marco cuando entre en vigor (ver Clase 20)» | Tomo Clase 3, p. 12 | Resuelto en redacción; la afirmación legal sigue en la lista de verificación (L3-06) |
| R3-3-06 | Hallazgo nuevo de esta revisión | En «Fuentes y alcance» del solucionario, el enlace «bacn.gov.py/leyes-paraguayas/2538/del-» venía truncado desde R1. Ahora remite a la ficha de la Ley 4924/2013 en bacn.gov.py, sin dirección inventada | Solucionario p. 22 | Resuelto |

## B. Decisiones de Fernando (editoriales, no institucionales)

| ID | Tema | Situación | Opciones |
|---|---|---|---|
| D-3-01 | Figuras | Las 20 figuras están en `COMPARACION_PARA_APROBACION_3BTC.pdf` (R1 → R3), con casillas de aprobación. Las figuras 12 y 18 quedan justo en el piso de 7 pt al ancho máximo | Aprobar, aprobar con cambios o rechazar cada una. Para la 12 y la 18: aceptar o pedir que se redibujen con letra más grande o con menos texto |
| D-3-02 (O-3-01) | Encuentros de cierre (clases 3, 7, 10, 14, 17 y 20) | Teoría, práctica integrada (75 min) y evaluación de unidad (30 min) en 120 min. Es ajustado; no se reestructuró | Mantener y validarlo con un grupo, o pasar la evaluación al encuentro siguiente (requiere rehacer el plan anual y los planes) |
| D-3-03 (O-3-02) | Paginación de evaluaciones y actividades | Sin cambios respecto de R2: la última pregunta abierta pasa a otra página en las Evaluaciones de las Unidades 1, 2 y 4 (p. 15, 29 y 55). La pregunta 12 de la Clase 12 queda sola en la p. 47. En 3.º no probé reducir renglones; en 2.º esa prueba no alcanzó | a) Mantener: hoja doble faz (recomendado). b) Pasar la última pregunta a completar. c) Reducir renglones o letra |
| D-3-04 | Laboratorio de 33 páginas | Once prácticas en dos páginas para conservar la legibilidad: +11 páginas de impresión por ejemplar | Aceptar, o aprobar figuras simplificadas o recortadas para esas prácticas |
| D-3-05 | RUC ficticio 4.812.907-6 | El dígito verificador calculado con el algoritmo de módulo 11 da 0, no 6. Es útil que no sea un RUC válido, pero un sistema contable que lo valide puede rechazarlo en la Práctica 2 | Mantener y avisar en la guía docente, o cambiar a un RUC de prueba que indique el proveedor del sistema |
| D-3-06 | Renglones de escritura del cuaderno (hallazgo nuevo) | Las líneas «Qué hice», «Qué me costó» y «Qué aprendí» del registro vienen de R1 con un paso de 3,2 mm: no alcanzan para escribir a mano. Los renglones agregados en R3 ya tienen 8 mm. Pasar también los originales a 8 mm alarga cada práctica y puede llevar más prácticas a dos páginas | a) Pasar todos a 8 mm y aceptar más páginas (recomendado). b) Mantenerlos y usar los renglones agregados o una hoja aparte |

## C. Requieren decisión institucional o verificación externa (no se cierran)

| ID | Tema | Quién | Qué se necesita |
|---|---|---|---|
| O-3-04, O-3-05 y demás referencias legales | Verificación del texto oficial | Desde otro entorno con acceso a bacn.gov.py y dnit.gov.py | `VERIFICACION_LEGAL_PENDIENTE_3BTC.md`: lista exacta de normas, afirmaciones y páginas |
| O-3-08 | Prácticas en software real | Docente de laboratorio | `PRUEBAS_PRACTICAS_3BTC.md` |
| O-3-09 | Hora cátedra de 40 min y 36 encuentros | Institución | Ratificación escrita |
| Programa | Vigencia del programa BTC (edición de 2014) | Institución | Confirmar que sigue vigente para 3.º |
| Impresión | Prueba física en oficio | Imprenta o institución | Ver `PRUEBAS_PRACTICAS_3BTC.md` |
