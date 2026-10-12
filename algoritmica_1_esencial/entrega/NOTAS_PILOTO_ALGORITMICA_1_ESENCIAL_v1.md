# NOTAS DEL PILOTO — Algorítmica 1.er Curso BTI · Edición Esencial Comercial 2026 · v1

**Estado: Listo para auditoría independiente de ChatGPT y aprobación de Fer.** No se declara listo para venta.

## Qué se entrega

| Pieza | Archivo | Páginas |
|---|---|---|
| Libro del estudiante con prácticas | Algoritmica_1er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026.docx + .pdf | 129 |
| Solucionario docente | Algoritmica_1er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026.docx + .pdf | 24 |
| Plan Anual (37 encuentros) | Algoritmica_1er_Curso_PLAN_ANUAL_ESENCIAL_COMERCIAL_2026.docx + .pdf | 9 |
| Planes de Clase (37) | Algoritmica_1er_Curso_PLANES_DE_CLASE_ESENCIAL_COMERCIAL_2026.docx + .pdf | 77 |
| Muestra comercial | Algoritmica_1er_Curso_MUESTRA_COMERCIAL_2026.pdf | 17 |

Los originales de Drive no se modificaron. La estructura curricular no cambia:
- 3 unidades y 21 clases con sus títulos e indicadores;
- 13 actividades por clase y 3 actividades por práctica;
- las 5 evaluaciones en su lugar (U1 tras la Clase 5; U2 y E1 tras la 12; U3 y E2 tras la 21);
- los 37 encuentros (148 HC) del Plan Anual vigente;
- los criterios y pesos de la rúbrica del PFI.

## Auditoría automática

**733 controles · 0 fallos** (detalle en `build/auditoria_resultado.txt`). Cubre:
- estructura;
- paginación e índices verificados contra el PDF;
- aritmética y tablas de verdad recalculadas;
- re-ejecución en PSeInt de 35 casos;
- libro ↔ solucionario;
- duplicados contra los ejemplos de clase;
- figuras;
- Plan Anual y planes;
- lengua y cobertura del programa;
- lecciones del piloto de 3.º;
- correcciones T1–T9.

## Hallazgos y correcciones

| Hallazgo | Corrección | Archivo/página | Estado |
|---|---|---|---|
| Fichas casi textuales pero no idénticas (punto final, minúsculas). | Las 21 fichas reproducen textualmente la capacidad del programa (Diseño Curricular de Informática, mayo 2026, págs. 70–73). Los indicadores no cambian. | Libro, fichas; Plan Anual; Planes | CORREGIDO |
| La Clase 2 trabaja la clasificación de conjuntos pero solo declaraba la capacidad de subconjuntos. | Lleva las dos capacidades. | Libro, Clase 2, pág. 11 | CORREGIDO |
| «Analiza las características de los algoritmos cualitativos y cuantitativos» no figuraba en ninguna ficha. | Se suma a la Clase 13, que la desarrolla. | Libro, Clase 13, pág. 72 | CORREGIDO |
| La Clase 10 (De Morgan, adjunción, simplificación) declaraba «Emplea la lógica proposicional…». | Pasa a la capacidad bajo la cual el programa ubica esas leyes («Construye proposiciones que contengan cuantificadores…»). | Libro, Clase 10, pág. 53 | CORREGIDO — decisión para Fer |
| Las 3 capacidades actitudinales no aparecían en ninguna pieza. | Figuran en la banda de cada unidad del Plan Anual. | Plan Anual | CORREGIDO |
| Las 21 clases estaban por debajo de 750 palabras (entre 344 y 549). | Ampliadas con contenido real: nuevos ejemplos resueltos, errores frecuentes, casos límite y apartados del programa. Ejemplos: tres conjuntos y «Juegos lógicos con diagramas» en la Clase 3; árbol de evaluación y operador mod en la Clase 15; variable auxiliar en la 16; Si sin Sino en la 17; condiciones compuestas con tabla de pruebas en la 18; Para con paso en la 19; contador condicional en la 20; «Una mejora resuelta: el total de descuentos» en la 21. Ahora el mínimo es 752. | Libro, Clases 1–21 | CORREGIDO |
| Diez clases sin figura (1, 2, 4, 6, 7, 9, 11, 12, 15, 18). | 11 diagramas nuevos: pertenencia, inclusión, unión e intersección, clasificación de proposiciones, condicional, árbol de 8 filas, De Morgan, cuantificadores, reglas de inferencia, árbol de evaluación de una expresión y decisión anidada. Todas las figuras están numeradas por clase (N.M), anunciadas en el texto y con epígrafe. | Libro, Figuras 1.1, 2.1, 4.1, 6.1, 7.1, 9.1, 10.1, 11.1, 12.1, 15.1, 18.1 | CORREGIDO |
| La figura de De Morgan del tomo era una imagen generada con texto poco legible. | Redibujada como tabla de verdad con las columnas resaltadas. | Libro, Figura 10.1 | CORREGIDO |
| Imágenes del tomo con marcas ✓ (Figuras 5.1, 14.2 y 21.1), marca de agua (14.2), artefacto «blend» (3.1) y `Escribir «sin ventas»` dentro del código (21.1). | Retoques mínimos en copias (`build/figs_ret/`, script `retoques.py`): se quitan las marcas y el artefacto, y las comillas pasan a rectas. Las otras 7 imágenes del tomo se conservan byte a byte. | Libro, Figuras 3.1, 5.1, 14.2, 21.1 | CORREGIDO — conviene una mirada de Fer a la 21.1, que sigue siendo densa |
| T1: montos con punto de miles dentro del código (`Si total >= 50.000`). En PSeInt eso vale 50, así que una compra de 30.000 recibía el descuento. | Ningún número del código lleva separador de miles. La Clase 15 explica por qué, con la prueba en PSeInt (30000 → 27000). | Libro, Clases 15–21 y Prácticas 14–21 | CORREGIDO |
| T2: comillas «» en el código (PSeInt: ERROR 68). | Comillas rectas en el código de clases, prácticas, actividades y evaluaciones. | Libro, Clases 18–21 | CORREGIDO |
| T3: promedio «≈ 11.667» sin decir qué hace el algoritmo. | Se escribe el desarrollo (11.666,67 periódico; PSeInt muestra 11666.6666666667). Las actividades nuevas usan promedios exactos. No queda ningún ≈. | Libro, Clase 20, pág. 110 | CORREGIDO |
| T4: «Puente a PSeInt» como título suelto con el programa en un solo párrafo. | Es un apartado de la Clase 21, con el programa en una caja de código. Se ejecutó: 54000 y frontera 45000. | Libro, Clase 21, pág. 116 | CORREGIDO |
| T5: 21 recuadros «En Paraguay» con tramos de IRP, una afirmación inexacta sobre factura/boleta, superlativos y títulos que no correspondían. | Política v2: queda un solo «En Paraguay» verificable (17 departamentos, capital Asunción, 33 letras del achegety). Dos pasan a «Aplicación profesional», uno a «Ejemplo cotidiano», uno se integra como texto y el resto se elimina. No se inventaron datos. | Libro, Clases 1, 3, 4, 8, 13 | CORREGIDO |
| T6: puntuación de las opciones («b) 55.000. c) 45.000.») en los 21 ítems «Elegí y justificá». | Forma única: «a) X; b) Y; c) Z.». En las evaluaciones, las opciones se componen como lista. | Libro, Actividades de aplicación | CORREGIDO |
| Las actividades copiaban los ejemplos resueltos (menú M, fritos F, turnos del lunes, encuesta 30/18/15/8, harina-queso-chipa, la promesa de las dos chipas, caja del mediodía, día real…). | 108 de 273 actividades modificadas: 87 reescritas con datos nuevos o corregidas (respuestas recalculadas), incluidos los ítems de las Clases 17 y 21 que repetían la tabla de pruebas de la clase, y 21 con las opciones normalizadas (T6). | Libro, Actividades; Solucionario, Primera parte | CORREGIDO |
| Prácticas: puntos de control que revelaban el resultado («n(T) = 4 y n(P) = 3», «debe escribir 70», «Deben darte 3 V»). | Los 63 puntos de control se reescribieron: piden contrastar con lo anticipado o con un control cruzado y no dan cifras. | Libro, Prácticas 1–21 | CORREGIDO |
| Prácticas con datos de los ejemplos de clase (P7 harina-queso-chipa; P8 promo QR/vaso; P10 la tabla de De Morgan de la Figura 10.1; P13 «preparar el mostrador»; P18 cadena mayorista/frecuente; P16 pago 20.000; P17 umbral 60.000; P20 venta 12.000). | Datos nuevos: cocido y yerba (P7), feria o partido (P8), contrarrecíproco (P10), cocido quemado (P13), pedidos para eventos (P18), pago 25.000 (P16), umbral 70.000 (P17), ventas 7.000 · 13.000 · 4.000 (P20). La auditoría compara cada práctica con los ejemplos de su clase. | Libro, Prácticas 7, 8, 10, 13, 16, 17, 18, 20 | CORREGIDO |
| Transferencia y revisión entre pares. | Solo donde aporta, en prácticas con encuentro de continuación (30 a 40 min): P5 (encuesta de la biblioteca), P9 (reglas del sistema de pedidos) y P20 (rifa de la promoción). | Libro, págs. 29, 51, 114 | CORREGIDO |
| Pseudocódigo de las prácticas sin verificar. | Los algoritmos de las Prácticas 14–21 se tradujeron a PSeInt 20250314 (perfil Flexible) y se ejecutaron con los datos de cada actividad. En total son 22 programas más el del Puente; la auditoría re-ejecuta 35 casos. | `pseint/pr/*.psc`; Solucionario, Segunda parte | CORREGIDO |
| Evaluaciones: E2-8 copiaba el ejemplo de la Clase 18; E1 A1 era ambigua («contando desde 2»); E1-6, E1-8, E1-9, U1-6, U2-7 y U2-8 repetían ejemplos o prácticas; varias opciones múltiples copiaban actividades; U3 tenía 6.000 y «» dentro del código. | Ítems reemplazados con datos propios, misma forma (3 de opción múltiple de 3 opciones + 5 a 7 de resolución) y la opción correcta en distinta posición. | Libro, págs. 31, 68, 70, 122, 124 | CORREGIDO |
| T8: el solucionario no traía las respuestas de las prácticas y la rúbrica era holística. | Resultado esperado y errores frecuentes de las 21 prácticas y de las 3 transferencias; claves de las 5 evaluaciones con puntaje sugerido. Rúbrica analítica con los mismos criterios y pesos (30/25/20/15/10) y niveles al 100/60/30/0 %. | Solucionario | CORREGIDO |
| PFI sin figura ni requisitos verificables. | Diagrama de flujo del algoritmo de caja básico (Figura PFI.1), requisitos mínimos (algoritmo con 3 casos de prueba y PSeInt, conjuntos, lógica, presentación) y extensión recomendada con la fórmula acordada (sistema de caja completo de la Clase 21). | Libro, pág. 126 | CORREGIDO |
| T7: Plan Anual con 23 filas (14 de 8 h), capacidades resumidas y sin instrumento por encuentro. | 37 filas, una por encuentro (20 en la 1.ª etapa y 17 en la 2.ª): cada clase de 8 h se divide en clase y continuación. Capacidades textuales y actitudinales en las bandas; procedimientos e instrumentos únicos; remite al libro. | Plan Anual | CORREGIDO |
| T9: no había Planes de Clase. | 37 planes (21 clases, 14 continuaciones y 2 integradoras) derivados del libro y del Plan Anual. Hora cátedra de 40 min declarada; alternativa en papel en los 2 planes con PSeInt. | Planes de Clase | CORREGIDO |
| El tomo y el cuaderno se nombraban «tomo» y «cuadernillo». | Pieza única: «libro». | Todas | CORREGIDO |

## Pendiente de comprobación manual

- **PSeInt en Windows.** Los programas se ejecutaron en PSeInt 20250314 para Linux con el perfil Flexible; conviene una pasada en la versión instalada en el colegio. En 1.º solo afecta al «Puente a PSeInt» de la Clase 21 y al PFI.
- **Figura 21.1.** Es la imagen original retocada. Sigue siendo densa; si Fer prefiere, se redibuja con el estilo de las figuras nuevas.

## Decisiones para Fer

- **37 encuentros (148 HC)**, como el Plan Anual vigente de 1.º. 2.º y 3.º usan 36: si se quiere homogeneizar la colección, hay que decidir qué continuación se elimina.
- **Clase 10** pasa a la capacidad bajo la cual el programa agrupa las leyes lógicas (ver la tabla). Si se prefiere conservar la del tomo, es un cambio de una línea.
- **Capacidades actitudinales:** solo en las bandas de unidad del Plan Anual, no en las fichas de clase.
- **Silogismo disyuntivo:** se conserva la convención del tomo (p ∨ q, p → r, q → s ⊢ r ∨ s), con la aclaración de que otros textos llaman así al MTP.
- **Capacidades de las integradoras:** se listan las que miden sus ítems (E1 = 5, E2 = 6). Si se prefieren todas las de la etapa, es un cambio de una línea.
- **Proyecto Final Integrador:** se trabaja en las continuaciones de las Clases 17, 19, 20 y 21, porque el Plan Anual vigente no tiene filas propias para el proyecto.

**Estado final: Listo para auditoría independiente de ChatGPT y aprobación de Fer.**
