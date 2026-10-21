# Informe de legibilidad e impresión

**Colección ADS 3.º BTI · documentos anuales v0.2 (candidata del cierre editorial) · oficio O3**

Todo lo que sigue se midió sobre los DOCX y los PDF generados (`build/legibilidad.py`; datos en `LEGIBILIDAD_IMPRESION.json`). Es una auditoría técnica en pantalla: no reemplaza una prueba de imprenta en papel.

## 1. Página, márgenes y fuentes

| | Libro | Guía | Cuaderno |
|---|---|---|---|
| Páginas | 211 | 109 | 33 |
| Tamaño de página en el PDF (mm) | 215,9 × 330,2 | 215,9 × 330,2 | 215,9 × 330,2 |
| Papel y márgenes del DOCX (cm) | 21,6 × 33,0; interior 2,5, exterior 1,8, superior 1,5, inferior 1,5 | 21,6 × 33,0; interior 2,5, exterior 1,8, superior 1,5, inferior 1,5 | 21,6 × 33,0; interior 2,5, exterior 1,8, superior 1,5, inferior 1,5 |
| Márgenes espejados en el DOCX | sí | sí | sí |
| Fuentes que pide el DOCX | Calibri, Courier, Courier New | Calibri, Courier, Courier New | Calibri, Courier |
| Fuentes incrustadas en el PDF | Carlito-Bold, Carlito-Italic, Carlito-Regular, LiberationMono | Carlito-Bold, Carlito-Italic, Carlito-Regular, LiberationMono | Carlito-Bold, Carlito-Regular |

En el entorno de construcción no está Calibri: LibreOffice la reemplaza por Carlito, que tiene las mismas medidas letra por letra, y Courier New por Liberation Mono, que tiene las mismas medidas que Courier New. El PDF lleva las fuentes incrustadas: **a la imprenta se le entrega el PDF**, no el DOCX.

## 2. Tamaños de letra (puntos)

| Documento | Función | Mínimo | Más usado | Mínimo en los lotes aprobados |
|---|---|---|---|---|
| Libro del estudiante | código | 7,5 | 7,5 | 7,5 |
| Libro del estudiante | texto y tablas | 8,0 | 10,0 | 8,0 |
| Libro del estudiante | títulos | 12,0 | 13,0 | 12,0 |
| Guía docente | código | 7,5 | 7,5 | 7,5 |
| Guía docente | texto y tablas | 8,0 | 9,0 | 8,0 |
| Guía docente | títulos | 12,0 | 13,0 | 12,0 |
| Cuaderno de prácticas | texto y tablas | 9,0 | 9,0 | 9,0 |
| Cuaderno de prácticas | títulos | 12,0 | 16,0 | 12,0 |

- Ningún tamaño es menor que el de los lotes aprobados: sí en los tres documentos. La integración no redujo la letra para resolver la distribución, y la equivalencia lo confirma tramo por tramo, porque compara el tamaño de cada uno.
- Los párrafos de texto corrido van en 10,5 pt y las consignas en 10 pt (el tamaño más usado); las tablas, entre 8 y 9,5 pt; el código, en 7,5 pt, en letra monoespaciada (96 caracteres por renglón). Es lo aprobado en los lotes.
- La auditoría de impresión comprueba que no haya ningún texto por debajo de 7,5 pt.

## 3. Medida del renglón y espacios de respuesta

| Documento | Caracteres por renglón de texto (mediana) | Renglones de respuesta | Separación entre renglones (mediana y mínima) | Largo del renglón |
|---|---|---|---|---|
| Libro del estudiante | 112 | 692 | 5,2 mm y 5,2 mm | 139,1 mm |
| Guía docente | 112 | 0 | None mm y None mm | None mm |
| Cuaderno de prácticas | 111 | 216 | 5,2 mm y 5,2 mm | 139,1 mm |

**Observaciones de legibilidad (no se cambiaron: son parte del formato aprobado):**
- **Renglón largo.** En los 17,3 cm de ancho útil entran unos 112 caracteres por renglón. Para un libro de texto, lo cómodo suele estar por debajo de los 90. Lo compensan los párrafos breves, las tablas y las cajas, pero conviene revisarlo en la prueba impresa. Acortarlo exigiría cambiar el perfil O3 aprobado (márgenes o dos columnas).
- **Renglones de respuesta juntos.** Están a 5,2 mm uno de otro y miden 139,1 mm de largo. Para escribir a mano suele recomendarse de 7 a 8 mm, y en dos renglones por consigna el espacio para responder es breve. Es el diseño aprobado en todos los lotes: ampliarlo agregaría páginas al libro y al cuaderno. Se propone decidirlo con la prueba impresa.
- **Código en 7,5 pt.** Es el tamaño aprobado para que cada renglón de código entre completo (96 caracteres). En pantalla se lee bien; la prueba impresa tiene que confirmar el contraste del fondo gris.
- La auditoría comprueba que todos los renglones de respuesta estén impresos y que ninguno quede separado de su consigna.

## 4. Impresión a doble faz e instrucciones para la imprenta

| Documento | Páginas | Hojas | Páginas en blanco para completar el pliego de 4 · 8 · 16 |
|---|---|---|---|
| Libro del estudiante | 211 | 106 | 1 · 5 · 13 |
| Guía docente | 109 | 55 | 3 · 3 · 3 |
| Cuaderno de prácticas | 33 | 17 | 3 · 7 · 15 |

Comienzo de cada unidad en el libro: Unidad I, pág. 12, par (izquierda); Unidad II, pág. 54, par (izquierda); Unidad III, pág. 91, impar (derecha); Unidad IV, pág. 124, par (izquierda); Unidad V, pág. 166, par (izquierda); Unidad VI, pág. 194, par (izquierda).

**Instrucciones para la imprenta:**
1. Imprimir el PDF, no el DOCX: lleva las fuentes incrustadas y la paginación controlada.
2. Papel oficio de 216 × 330 mm, vertical, a doble faz, con volteo por el borde largo. La página 1 va en el frente de la primera hoja.
3. Los márgenes son espejados: el interior (2,5 cm) está a la izquierda en las páginas impares y a la derecha en las pares. Por eso no se puede saltear ni agregar una página en medio sin desplazar el lomo de todas las siguientes.
4. Las páginas en blanco que haga falta agregar para completar el pliego de la máquina van todas al final, después de la última página. La cantidad depende del pliego: está en la tabla de arriba. En la página 1 no hay contratapa ni página de cortesía: si la imprenta quiere agregarlas, van antes de la portada, en número par (2), para no invertir las caras.
5. Los documentos no tienen hojas en blanco intercaladas: la auditoría lo comprueba página por página. Las unidades y los capítulos empiezan en hoja nueva, pero no siempre en página impar, como en los lotes aprobados.
6. Encuadernación recomendada: el libro, en rústica fresada con cola PUR o anillado; la guía, anillada o en rústica; el cuaderno, anillado, para que abra plano (ver EVALUACION_ENCUADERNACION.md).
7. Antes del tiraje, una prueba impresa completa del libro: comprobar en papel el margen interior después del fresado o del anillado, el contraste de los fondos de color de las cajas y la legibilidad del código en 7,5 pt.

## 5. Compatibilidad con las fuentes previstas

| Fuente que reemplaza a Calibri | Libro | Guía | Cuaderno | Resultado |
|---|---|---|---|---|
| Carlito | 211 | 109 | 33 | correcto |
| Liberation Sans | 213 | 111 | 33 | correcto |
| DejaVu Sans | 236 | 122 | 35 | correcto |

- **Carlito tiene las mismas medidas que Calibri:** con Calibri (Word en Windows) la paginación esperada es la de Carlito, que es la de los PDF entregados. La medida exacta en Word con Calibri sigue pendiente: en este entorno no hay Word ni Calibri.
- Con Liberation Sans el libro gana 2 páginas, y con DejaVu Sans, una fuente más ancha, 25. En las tres no aparecen hojas en blanco ni renglones sueltos, y cada evaluación sigue en su página. Pero el índice y la página del diagnóstico que cita la guía corresponden a la paginación con Carlito: si el DOCX se abre en un equipo sin Calibri ni Carlito, hay que regenerar el PDF desde los constructores, no reimprimir el DOCX.
- Por eso, para imprimir, el archivo de referencia es el PDF.

## 6. Límites de esta auditoría

- Se midió en pantalla, sobre el PDF de LibreOffice. No hay prueba en papel ni en la máquina de la imprenta.
- No se abrió el DOCX en Microsoft Word ni en Windows: la compatibilidad con Word queda pendiente, igual que las pruebas del prototipo en Windows y en los laboratorios.
- El contraste de los fondos de color de las cajas se juzgó a la vista en las láminas, no con un instrumento.
