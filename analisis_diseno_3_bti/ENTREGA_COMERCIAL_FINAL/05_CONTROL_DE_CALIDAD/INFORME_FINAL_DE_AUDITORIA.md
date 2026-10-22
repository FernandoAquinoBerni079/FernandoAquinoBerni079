# Informe final de auditoría — edición comercial v1.0

Fecha: 22 de octubre de 2026. Rama `claude/libros-5z31jx`.

## Resultado

- Auditoría de la entrega: **79 controles, 0 fallos**.
- Auditoría de la planificación: **83 controles, 0 fallos**.
- Cierre de la entrega y ZIP: **20 controles, 0 fallos**.

| Bloque | Controles | Correctos | Fallos |
|---|---|---|---|
| 1. Productos | 25 | 25 | 0 |
| 2. Fidelidad | 7 | 7 | 0 |
| 3. Numeración | 7 | 7 | 0 |
| 4. Paginación | 21 | 21 | 0 |
| 5. Ortografía | 1 | 1 | 0 |
| 6. Reservados | 7 | 7 | 0 |
| 7. Avisos | 11 | 11 | 0 |

## Productos

| Producto | Páginas | Hojas | Lomo (mm) | Formatos |
|---|---|---|---|---|
| Libro del estudiante | 211 | 106 | 10.6 | PDF de impresión (interior y cubierta), PDF digital |
| Cuaderno de prácticas | 36 | 18 | 1.8 | PDF de impresión (interior y cubierta), PDF digital |
| Guía docente con solucionario | 109 | 55 | 5.5 | PDF de impresión (interior y cubierta), PDF digital y DOCX editable |
| Plan anual | 23 | 12 | 1.2 | PDF de impresión (interior y cubierta), PDF digital y DOCX editable |
| Planes de clase | 73 | 37 | 3.7 | PDF de impresión (interior y cubierta), PDF digital y DOCX editable |

## Correcciones hechas en esta corrida

- Página 1 del libro y del cuaderno: se explica qué es «Work», porque el texto lo cita (secuencia y evidencias). Desde la página 2, el texto es idéntico al de v0.2.
- Instrumento del encuentro 1: el «Mapa de apoyos del curso (modelo)» se cita aparte de las claves del diagnóstico (79 referencias).
- Cuaderno: un renglón más por respuesta, interlineado exacto de 8 mm, índice actualizado.
- Rótulo «Biblioteca Comercial 2026» reemplazado por «Edición 2026»; datos de edición con campos «[a completar por el titular]».

## Discrepancias

Ver RESOLUCION_DE_DISCREPANCIAS.pdf: ninguna era un error de contenido.

## ZIP de entrega

Una carpeta por ZIP, más el LEEME. El SHA-256 de cada ZIP está en SHA256SUMS.txt, junto a los ZIP (no puede figurar acá: este informe va dentro del ZIP 05).

| ZIP | Entradas |
|---|---|
| ADS_3BTI_v1_0_01_ESTUDIANTE.zip | 4 |
| ADS_3BTI_v1_0_02_DOCENTE.zip | 266 |
| ADS_3BTI_v1_0_03_COLECCION_COMPLETA.zip | 282 |
| ADS_3BTI_v1_0_04_PRESENTACION_COMERCIAL.zip | 28 |
| ADS_3BTI_v1_0_05_CONTROL_DE_CALIDAD.zip | 26 |

## Controles del cierre

- ok: ADS_3BTI_v1_0_01_ESTUDIANTE.zip: íntegro (testzip) y con los 3 archivos de la carpeta, byte a byte
- ok: ADS_3BTI_v1_0_01_ESTUDIANTE.zip: sin archivos reservados, temporales ni bases de datos
- ok: ADS_3BTI_v1_0_01_ESTUDIANTE.zip: ninguno de los 34 textos o códigos DR/V6 en su contenido
- ok: ADS_3BTI_v1_0_01_ESTUDIANTE.zip: menos de 95 MB (límite de GitHub: 100 MB por archivo)
- ok: ADS_3BTI_v1_0_02_DOCENTE.zip: íntegro (testzip) y con los 265 archivos de la carpeta, byte a byte
- ok: ADS_3BTI_v1_0_02_DOCENTE.zip: sin archivos reservados, temporales ni bases de datos
- ok: ADS_3BTI_v1_0_02_DOCENTE.zip: ninguno de los 34 textos o códigos DR/V6 en su contenido
- ok: ADS_3BTI_v1_0_02_DOCENTE.zip: menos de 95 MB (límite de GitHub: 100 MB por archivo)
- ok: ADS_3BTI_v1_0_03_COLECCION_COMPLETA.zip: íntegro (testzip) y con los 281 archivos de la carpeta, byte a byte
- ok: ADS_3BTI_v1_0_03_COLECCION_COMPLETA.zip: sin archivos reservados, temporales ni bases de datos
- ok: ADS_3BTI_v1_0_03_COLECCION_COMPLETA.zip: ninguno de los 34 textos o códigos DR/V6 en su contenido
- ok: ADS_3BTI_v1_0_03_COLECCION_COMPLETA.zip: menos de 95 MB (límite de GitHub: 100 MB por archivo)
- ok: ADS_3BTI_v1_0_04_PRESENTACION_COMERCIAL.zip: íntegro (testzip) y con los 27 archivos de la carpeta, byte a byte
- ok: ADS_3BTI_v1_0_04_PRESENTACION_COMERCIAL.zip: sin archivos reservados, temporales ni bases de datos
- ok: ADS_3BTI_v1_0_04_PRESENTACION_COMERCIAL.zip: ninguno de los 34 textos o códigos DR/V6 en su contenido
- ok: ADS_3BTI_v1_0_04_PRESENTACION_COMERCIAL.zip: menos de 95 MB (límite de GitHub: 100 MB por archivo)
- ok: ADS_3BTI_v1_0_05_CONTROL_DE_CALIDAD.zip: íntegro (testzip) y con los 25 archivos de la carpeta, byte a byte
- ok: ADS_3BTI_v1_0_05_CONTROL_DE_CALIDAD.zip: sin archivos reservados, temporales ni bases de datos
- ok: ADS_3BTI_v1_0_05_CONTROL_DE_CALIDAD.zip: ninguno de los 34 textos o códigos DR/V6 en su contenido
- ok: ADS_3BTI_v1_0_05_CONTROL_DE_CALIDAD.zip: menos de 95 MB (límite de GitHub: 100 MB por archivo)

## Pendiente (no técnico)

La venta no está habilitada: falta identificar al titular y al editor, la revisión jurídica y el ISBN. Ver DERECHOS_Y_REQUISITOS_LEGALES.pdf y VALIDACIONES_REALIZADAS.md.
