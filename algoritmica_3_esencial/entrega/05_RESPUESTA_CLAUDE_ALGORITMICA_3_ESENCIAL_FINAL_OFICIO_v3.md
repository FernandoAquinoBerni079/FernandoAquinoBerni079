# 05_RESPUESTA_CLAUDE_ALGORITMICA_3_ESENCIAL_FINAL_OFICIO_v3

**Respuesta del constructor a 04_REAUDITORIA_CHATGPT_ALGORITMICA_3_ESENCIAL_FINAL_OFICIO_v2** (12/10/2026) · Protocolo v0.4, §3, paso 5

Algorítmica · 3.er Curso BTI · Edición Esencial Comercial 2026 · versión corregida **FINAL OFICIO v3** (12/10/2026)

**Estado: corregido — vuelve a ChatGPT para reauditar los hallazgos 10 y 11 y la revisión visual.** No se declara aprobado para la venta: esa decisión es solo de Fer.

## Resumen

- **Hallazgos 01 a 09:** el auditor los dio por resueltos. No se tocaron.
- **Hallazgos nuevos 10 (MAYOR) y 11 (MENOR):** se corrigieron en el Libro con los textos propuestos. Es la única pieza que cambia de contenido.
- **Verificación visual binaria** (pendiente del informe 04, B.8): se hizo sobre los PDF renderizados y queda en `build/revision_visual_v3/` con medidas e imágenes (ver §2).

**Ubicación:**
- Rama `claude/libros-5z31jx`, carpeta `algoritmica_3_esencial/salida_FINAL_OFICIO_v3/`: 4 DOCX y 5 PDF.
- Las carpetas `salida_FINAL_OFICIO_v2/` y `salida_FINAL_OFICIO/` quedan intactas para comparar.

**Qué cambia en cada pieza de la v3:**
- **Libro:** sale de `build/final_oficio/correcciones_v3.py`, aplicado sobre el Libro v2.
- **Solucionario, Planes de Clase y Plan Anual:** son **copias idénticas byte a byte** de la v2; solo cambia el sufijo del nombre.
- **Muestra:** se regeneró con `build_muestra_fo_v3.py`, con la misma composición que la v2.

## 1. Hallazgos y qué se hizo

| N.º | Gravedad | Qué se hizo |
|---|---|---|
| 10 | MAYOR | **Clase 21, pág. 110 — «La consulta de referencias cruzadas, paso a paso».** <br>• **Paso 5:** se reemplazó por el texto exacto propuesto. Solo se agregó entre paréntesis la cifra del caso, «(en el Copetín, G. 134.000)», para que el paso siga leyendo la tabla de la Figura 21.2. <br>• **Concepto clave:** el título «la esquina que audita» pasa a «**coherencia no es exactitud**», con el texto propuesto («Una tabla cruzada facilita comprobar la coherencia de sus subtotales. La exactitud de cada importe exige además validarlo contra los datos de origen.»). <br>• **Introducción del paso a paso:** adelantaba la misma idea con «y su doble control»; ahora dice «y su **control de sumas**». <br>• **Figura 21.2:** se revisó la imagen y no afirma que la tabla detecte errores. No se tocó. <br>• **Búsqueda de la misma idea en el resto del paquete:** en el Libro (PDF y DOCX) ya no quedan «auditor incorporado», «las dos sumas no coincidirían», «la esquina que audita» ni «doble control». <br>• **Los demás controles cruzados quedaron como estaban,** porque comparan consultas o caminos independientes y no la cruzada consigo misma: el punto de control de la Práctica 21 («la cruzada coincide con TotPorCliente y TotPorCategoria») y las orientaciones del Solucionario y del Proyecto Final. Aun así, ver §3. |
| 11 | MENOR | **Proyecto Final Integrador, pág. 116:** ahora hay **un solo encabezado**, «Capacidad transversal del programa MEC». <br>Debajo van, en un párrafo propio, la frase oficial sin cambios («Reconoce la importancia de la práctica Conductual en el desarrollo de las actividades.») y, en otro párrafo, la evidencia en el proyecto. <br>El rótulo «Capacidad transversal MEC:» ya no aparece en el Libro. La frase oficial sigue figurando dos veces: Presentación y Proyecto Final. |

## 2. Revisión visual binaria (`build/revision_visual_v3/`)

`build/final_oficio/revision_visual_v3.py` abre los cinco PDF de la v3 con pymupdf, mide cada página y deja dos cosas:
- **Imágenes:** 18 hojas de contacto JPG (12 páginas por hoja, todas de menos de 600 KB) y páginas sueltas a mayor resolución: Planes 1, 26, 28 y 31 (los compactados a 9 pt) y Libro 33, 102, 110 y 116.
- **Medidas:** la tabla en `revision_visual_v3.md`.

| Documento | Págs. | Papel (cm) | Texto: izq. / der. / sup. / inf. (cm) | Letra mín. |
|---|---|---|---|---|
| Libro | 117 | 21,59 × 33,02 | 1,27 / 1,27 / 1,28 / 1,29 | 8,5 pt |
| Solucionario | 18 | 21,59 × 33,02 | 1,27 / 1,28 / 1,28 / 1,31 | 8,0 pt |
| Planes de Clase | 38 | 21,59 × 33,02 | 1,27 / 1,28 / 1,29 / 1,50 | 9,0 pt |
| Plan Anual | 6 | vertical y 33,02 × 21,59 apaisado | 1,27 / 1,29 / 1,29 / 2,05 | 8,0 pt |
| Muestra | 15 | vertical y una apaisada | 1,27 / 1,28 / 1,28 / 1,75 | 8,0 pt |

**Cómo se midió:**
- **Texto:** se toma la caja de cada letra, sin los espacios, y se dejan fuera el encabezado y el pie. Encabezado y pie van a 0,6 cm del borde por diseño.
- **Portadas y contraportadas** a página completa no se miden.
- **Corrección de la propia medición:** una primera versión usaba la caja de cada renglón, que en los renglones justificados incluye el espacio final. Daba 1,16 cm a la derecha, pero medido letra por letra el texto termina a 1,27–1,28 cm.

**Resultado:**
- **Texto:** en los cinco PDF, ningún texto entra en el margen de 1,27 cm.
- **Letra:** no hay texto de menos de 8 pt.
- **Planes 1, 26, 28 y 31:**
  - Cuerpo en 9 pt.
  - Firmas «Docente» y «Dirección — Visto bueno» dentro de la hoja.
  - Entre 2,8 y 3,3 cm libres al pie.
- **Revisión ocular:** revisé las hojas de contacto de los cinco PDF y las páginas sueltas.
  - Sin tablas cortadas, superposiciones, figuras deformadas ni hojas residuales.
  - En la Muestra, el Plan N.º 1 está entero en la pág. 15.
  - En la Muestra no hay claves.

**Observación que se informa, no se corrige:** dos elementos **gráficos** (no el texto) entran unos milímetros en el margen.
- **Recuadros «Punto de control» de las Prácticas** (Libro, 27 págs., y la pág. 8 de la Muestra): el fondo y el filete llegan a **1,06 cm** del borde izquierdo. Son párrafos con borde y sombreado: Word y LibreOffice dibujan ese borde por fuera de la sangría del texto. El texto del recuadro sigue alineado a 1,27 cm.
- **Borde izquierdo de la tabla del Plan Anual:** llega a **1,14 cm**.
- Ambos ya estaban en FINAL OFICIO y quedan muy dentro del área imprimible de cualquier impresora.
- **Por qué no lo corregí:** hacerlo obliga a angostar esos recuadros y podría correr la paginación del libro. Lo dejo a decisión de Fer (ver §4).

## 3. Controles (`build/verificacion_v3.txt`)

`build/final_oficio/verificar_v3.py` repite los 81 controles de la v2 sobre la v3 y suma 18. Resultado: **99 controles, 0 fallos.**

| Control | Resultado |
|---|---|
| Hallazgo 10 | Sin las cuatro frases retiradas, en DOCX y PDF · los tres textos nuevos presentes · paso 5 y concepto clave en la pág. 110, junto a la Figura 21.2 |
| Hallazgo 11 | Un solo encabezado en el Proyecto Final · frase oficial en párrafo propio, seguida de la evidencia · ningún «Capacidad transversal MEC:» |
| Libro v3 frente a v2 | 13 líneas distintas, todas de los hallazgos 10 y 11 |
| Solucionario, Planes y Plan Anual | Idénticos byte a byte a la v2 (6 archivos) |
| Índices | Libro 54/54 · Solucionario 53/53 (la paginación no cambió: 117 págs.) |
| Controles de la v2 (hallazgos 01 a 09) | Todos se mantienen |

**Sobre el alcance del hallazgo 10:**
- Los controles que siguen en el libro igualan dos agrupaciones de las mismas filas. Por ejemplo, el total por cliente con el total por categoría.
- Sirven para encontrar errores de las consultas: un filtro mal puesto, un renglón contado dos veces, una relación mal hecha.
- No sirven para encontrar un importe mal cargado en DetalleVenta. Para eso, el texto nuevo de la Clase 21 manda a contrastar con el origen.
- Si el auditor quiere el mismo matiz en la orientación del Solucionario («Exigir un control cruzado por consulta»), es un agregado de una línea.

## 4. Pendiente

- Reauditoría de ChatGPT sobre `salida_FINAL_OFICIO_v3/`: hallazgos 10 y 11, y revisión visual con el material de `build/revision_visual_v3/`.
- **Decisiones de Fer:**
  - (a) que Plan Anual y Planes sean los mismos para la Edición Completa;
  - (b) quitar o conservar el sufijo `_v3` al aprobar;
  - (c) conservar la autoevaluación de las Clases 6 y 19;
  - (d) aceptar o mandar a corregir los recuadros «Punto de control» y el borde de la tabla del Plan Anual que entran unos milímetros en el margen.
- **Aprobación para la venta: solo Fer.** Este paquete **no** está aprobado para la venta.
