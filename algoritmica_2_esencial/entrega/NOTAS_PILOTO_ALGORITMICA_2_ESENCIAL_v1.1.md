# NOTAS DEL PILOTO — Algorítmica 2.º Curso BTI · Edición Esencial Comercial 2026 · v1.1

**Estado: Listo para auditoría independiente de ChatGPT y aprobación de Fer.** No se declara listo para venta.

## Qué se entrega

| Pieza | Archivo | Páginas |
|---|---|---|
| Libro del estudiante con prácticas | Algoritmica_2do_Curso_LIBRO_ESENCIAL_COMERCIAL_2026.docx + .pdf | 127 |
| Solucionario docente | Algoritmica_2do_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026.docx + .pdf | 19 |
| Plan Anual (36 encuentros) | Algoritmica_2do_Curso_PLAN_ANUAL_ESENCIAL_COMERCIAL_2026.docx + .pdf | 8 |
| Planes de Clase (36) | Algoritmica_2do_Curso_PLANES_DE_CLASE_ESENCIAL_COMERCIAL_2026.docx + .pdf | 65 |
| Muestra comercial | Algoritmica_2do_Curso_MUESTRA_COMERCIAL_2026.pdf | 17 |

Los originales de Drive no se modificaron. Estructura curricular sin cambios: 4 unidades, 21 clases con sus títulos, indicadores de las fichas, ubicación de las 6 evaluaciones, 36 encuentros con las continuaciones del Plan Anual vigente (Prácticas 7, 10, 14 y 15–21), 3 talleres del PFI y pesos de la rúbrica.

## Auditoría automática

Controles: 860 · Fallos: 0 (bloques A–J: estructura, paginación e índices verificados contra el PDF, aritmética, re-ejecución en PSeInt, libro ↔ solucionario, duplicados, figuras, planes, lengua y cobertura del programa, lecciones del piloto de 3.º y correcciones T1–T20). Detalle en `build/auditoria_resultado.txt`.

## Hallazgos y correcciones

| Hallazgo | Corrección | Archivo/página | Estado |
|---|---|---|---|
| Las 21 fichas parafraseaban las capacidades del programa. | Capacidades reproducidas textualmente del programa MEC (Diseño Curricular de Informática, mayo 2026, págs. 74–76); la Clase 14 lleva sus dos capacidades (modularización y cadenas). Indicadores sin cambios. | Libro, fichas de las 21 clases; Plan Anual; Planes de Clase | CORREGIDO |
| El Plan Anual no aclaraba la naturaleza de los indicadores. | Nota acordada en el piloto: «Las capacidades se reproducen textualmente del programa MEC vigente. Los indicadores de logro de este plan son operativizaciones observables…». 2.º no tiene capacidad conductual en el programa: no se agrega una transversal. | Plan Anual, pág. 2 | CORREGIDO |
| Faltaban contenidos del programa: comentarios, sangría, sentencia de color, restricciones del lenguaje. | Nueva sección «Del pseudocódigo al lenguaje de programación» con el mismo algoritmo en PSeInt y en Python (exportado con PSeInt y verificado) y tabla de equivalencias. | Libro, Clase 2, págs. 13–18 | CORREGIDO |
| Conceptos «programa» y «sistema» del programa no definidos. | Definidos en la Clase 1. | Libro, Clase 1, pág. 6 | CORREGIDO |
| T1: el código de la «burbuja optimizada» no tenía bandera: nunca cortaba antes. | Reemplazado por la versión con la bandera hubo (Repetir … Hasta Que NO hubo O i > 5); 4 pasadas en lugar de 5, verificado. | Libro, Clase 11, pág. 73 | CORREGIDO |
| T2: el método de selección se explicaba sin pseudocódigo. | Pseudocódigo del método de selección agregado (verificado en PSeInt). | Libro, Clase 11 | CORREGIDO |
| T3: montos Entero con 10 % de descuento no exacto detienen PSeInt (ERROR 314). | Recuadro «En Paraguay — guaraníes sin céntimos» con trunc/redon; los ejemplos usan montos donde el 10 % es exacto; Práctica 2 lo hace experimentar en el desafío. | Libro, Clase 2 y Práctica 2 | CORREGIDO |
| T4: fila «Confundir = con <-» de la tabla de errores incorrecta para el perfil Flexible. | Fila corregida. | Libro, Clase 2 | CORREGIDO |
| T5: superlativos no verificables («la más usada»…). | Reemplazados por formulaciones neutras. | Libro, Clases 12, 18 y 20 | CORREGIDO |
| T6/T7: recuadros con la Ley 6534/2020 (es de datos crediticios) y tramos de IRP. | Eliminados. | Libro, Unidad 3 | CORREGIDO |
| T8: IIf/SiInm en Access. | Se usa SiInm(condición;sí;no) en la cuadrícula y se aclara que la vista SQL muestra IIf. | Libro, Clase 21 y Práctica 21 | CORREGIDO — pendiente de verificación manual en Access |
| T9/T10: la práctica de Access no fijaba tipos de datos ni pedía guardar la tabla con nombre. | Práctica 19 con diseño explícito (Texto corto / Número Entero largo, clave principal) y paso «Guardá la tabla con el nombre Articulos». | Libro, Práctica 19, pág. 134 | CORREGIDO |
| T11: notación de archivos inconsistente (Escribir En Archivo, Cerrar…). | Notación conceptual única de la Unidad 3 documentada en un Concepto clave: Abrir … Para Lectura/Escritura/Agregar, Escribir Archivo, Leer Archivo, FinDeArchivo, Cerrar Archivo. | Libro, Clase 16, pág. 109 | CORREGIDO |
| T12: se hablaba de variables globales, que PSeInt no tiene. | Aclaración con ejemplo ejecutado (dentro: 99 / fuera: 5). | Libro, Clase 13 | CORREGIDO |
| T13: faltaba la relación (comparación) entre cadenas. | Sección «Comparar cadenas: la relación entre textos» con resultados verificados en PSeInt ("Zapallo" < "anana", "10" < "9") y recuadro de errores frecuentes. | Libro, Clase 14 | CORREGIDO |
| T14: tres imágenes sin epígrafe y un párrafo partido por una imagen. | Imágenes retiradas; párrafo reparado; toda figura numerada por clase (N.M), anunciada en el texto y con epígrafe. | Libro | CORREGIDO |
| Siete clases sin ninguna figura (2, 4, 5, 9, 12, 16, 17). | Siete diagramas nuevos (Si simple, condición compuesta, Si anidado frente a Segun, recorrido del máximo, rango de Azar, modos de apertura, buffer). Las 17 figuras originales se conservan byte a byte. | Libro, Figuras 2.1, 4.1, 5.1, 9.1, 12.1, 16.1, 17.1 | CORREGIDO |
| T15: envío con enBarrio 1/0 en lugar de una variable lógica. | Condiciones con variables lógicas (Verdadero/Falso) en clase, práctica y evaluaciones. | Libro | CORREGIDO |
| T16: segundo <- 0 sin justificar. | Nota que explica por qué funciona aquí (ventas no negativas) y qué hacer si no. | Libro, Clase 9 | CORREGIDO |
| Clases 18 y 21 por debajo de 750 palabras. | Ampliadas: propiedades de un archivo y búsqueda con comodines (18); referencia cruzada en Access paso a paso con rutas de Access 2016 (21). | Libro, Clases 18 y 21 | CORREGIDO |
| Carpeta raíz del caso mezclada (C:\Copetin y C:\Karumbe). | Unificada en C:\Karumbe. | Libro, Clase 18 | CORREGIDO |
| T20: 29 recuadros «En Paraguay», la mayoría genéricos. | Política del piloto: se conservan 2 con contenido paraguayo concreto (guaraníes sin céntimos; el RUC); el resto pasa a «Ejemplo cotidiano» o «Aplicación profesional», se integra como texto o se elimina. No se inventaron datos. | Libro | CORREGIDO |
| Access: «la versión más usada» y rutas sin versión. | Una sola referencia general a Access 2016 en castellano; rutas de menú del asistente de referencias cruzadas según la documentación oficial. | Libro, Clase 19 | CORREGIDO — pendiente de verificación manual de rótulos de interfaz |
| Las actividades copiaban los ejemplos resueltos (misma semana, mismo vector, mismo código MIX-01). | 75 de 252 actividades reescritas con datos nuevos: semana 2 (4.480.000), matriz de bebidas (181 unidades; 1.313.000), vector del ranking unid2, códigos SOP-07/COC-12, consultas nuevas sobre la tabla Productos. Respuestas recalculadas. | Libro, Actividades de aplicación; Solucionario, Primera parte | CORREGIDO |
| Prácticas del cuaderno: una actividad, mismos datos que la clase y «Deberías ver: …» en el punto de control. | 21 prácticas nuevas en la Librería escolar Arandu (2 actividades; 3 en las 10 que continúan en encuentro propio), puntos de control que contrastan con lo anticipado sin revelar cifras, transferencia y revisión entre pares solo en 7, 10 y 14. | Libro, Prácticas 1–21 | CORREGIDO |
| El código de las prácticas no estaba verificado. | Los 37 programas de las Prácticas 1–14 se ejecutaron en PSeInt 20250314 (perfil Flexible); la auditoría los re-ejecuta y compara con el solucionario. Hallazgos documentados: un SubProceso sin parámetros no lleva paréntesis; una variable no puede llamarse igual que el algoritmo (ERROR 48). | pseint/*.psc; Solucionario, Segunda parte | CORREGIDO |
| Evaluaciones con la respuesta en la consigna (E1-9 «(resultado 54.000)», U2-7 y E2-5 «(Coquito=200)») y datos de los ejemplos de clase. | Seis evaluaciones con la misma ubicación, alcance y forma (3 + 6 ítems), datos propios (heladería Yvoty, fotocopiadora Ñandutí) y sin resultados en las consignas. | Libro, págs. 52, 99, 101, 127, 148, 150 | CORREGIDO |
| T18: el solucionario no traía respuestas de las prácticas. | Resultado esperado y errores frecuentes de las 21 prácticas y de las 3 transferencias; claves de las 6 evaluaciones (21 puntos). | Solucionario | CORREGIDO |
| PFI: figura del flujograma con texto cortado y superpuesto; rúbrica holística. | Flujograma redibujado (Figura PFI.1); rúbrica analítica con los mismos criterios y pesos 30/25/20/15/10 y niveles 100/60/30/0 %; extensión recomendada con la fórmula acordada (tabla Ventas y ticket en archivo). | Libro, Proyecto Final Integrador; Solucionario | CORREGIDO |
| T17: Plan Anual con el PFI en una sola fila de 12 h y referencias al Cuaderno. | 36 filas (una por encuentro), 18 por etapa, PFI en tres talleres; procedimientos e instrumentos únicos; remite al libro. | Plan Anual | CORREGIDO |
| T19: no había Planes de Clase vigentes de 2.º. | 36 planes nuevos (21 clases, 10 continuaciones, 3 talleres, 2 integradoras) derivados del libro y del Plan Anual; hora cátedra de 40 min declarada; alternativa en papel en los planes con equipamiento. | Planes de Clase | CORREGIDO |
| E2 declaraba «Unidades 1 a 4». | Se respeta el alcance vigente; las capacidades listadas son las que efectivamente evalúan sus ítems. | Plan Anual; Planes de Clase | CORREGIDO |

## Formato oficio — v1.1

Por decisión de Fer, todo el paquete pasa a **oficio 21,6 × 33 cm** para bajar el costo de impresión de docentes y estudiantes; no queda nada en A4:
- libro, solucionario y Planes de Clase en vertical; Plan Anual en horizontal (33 × 21,6 cm);
- márgenes estrechos de 1,27 cm por lado (ancho útil de 19,06 cm; 30,46 cm en el Plan Anual);
- tablas, cajas, fichas, bandas de evaluación y renglones al 100 % del ancho de la página, con las columnas escaladas en proporción;
- figuras hasta un 10 % más grandes (máximo 17,5 cm);
- portadas y contraportada regeneradas en proporción oficio.

Páginas: libro de 156 a 127; solucionario de 24 a 19; Plan Anual de 9 a 8; Planes de Clase de 75 a 65; muestra de 19 a 17. Los índices se rearmaron y se verificaron contra el PDF. La auditoría suma 16 controles de formato (860 en total, 0 fallos). El contenido no cambió.

## Pendiente de comprobación manual

- Access 2016 en castellano: rótulos de la fila Total (Cuenta), del asistente de referencias cruzadas y el aviso de clave duplicada (Prácticas 19–21, Clase 21). Las rutas de menú siguen la documentación oficial; los resultados de las consultas se verificaron por cálculo.
- Access: aceptación de SiInm([stock]<20;"reponer";"ok") con separador punto y coma en la configuración regional del laboratorio.
- Explorador de archivos: rótulo de la opción para mostrar extensiones y el comportamiento del Bloc de notas al guardar un archivo de solo lectura (Prácticas 15 y 17); varía con la versión de Windows.
- PSeInt en Windows: los programas se ejecutaron en PSeInt 20250314 para Linux con el perfil Flexible; conviene una pasada en la versión instalada en el colegio.

## Decisiones para Fer

- Contexto de prácticas: Librería escolar Arandu; evaluaciones: heladería Yvoty y fotocopiadora Ñandutí. Las clases siguen con el Copetín Karumbé.
- Capacidades de las integradoras: E1 = A2–A6 y E2 = A5, A6, A9, A12, A13 (las que miden sus ítems). Si preferís listar todas las de la etapa, es un cambio de una línea.
- Hora cátedra de 40 minutos en los Planes de Clase (como en 3.º); la institución reajusta si usa otra duración.

**Estado final: Listo para auditoría independiente de ChatGPT y aprobación de Fer.**
