# 03_RESPUESTA_CLAUDE_SOFTWARE_1_ESENCIAL_v2

**Respuesta del constructor a 02_AUDITORIA_CHATGPT_SOFTWARE_1_ESENCIAL_v2** · Protocolo v0.4, §3, paso 5

Gabinete de Informática – Software · 1.er Curso BTI · Edición Esencial · versión corregida **v2** (11/10/2026)

**Estado: corregido — vuelve a ChatGPT para la comprobación de cierre.** No se declara listo para la venta.

## Resumen

La v2 corrige los dos hallazgos MAYORES de maquetación (V2-01 y V2-02). Solo se intervinieron los .docx de **Planes de Clase** y **Plan Anual** y sus PDF; la **Muestra** se rearmó porque contenía las hojas viejas del Plan 1. Libro y Solucionario no se tocaron.

- **Planes de Clase:** de 60 a **38 páginas** (portada, índice y 36 planes, uno por hoja oficio).
- **Plan Anual:** de 12 a **10 páginas**; la última hoja tiene las estrategias de inclusión y la firma.
- **Texto:** idéntico al de la v1 (commit `61feba7`), párrafo por párrafo. En los Planes solo cambian los 35 números de página del índice.
- **Controles:** `build/control_v2.py` da **94 OK · 0 fallos**, y la auditoría de contenido `build/auditoria_v1.py` sigue en **117 OK · 0 fallos**.

## 1. Hallazgos y qué se hizo

| N.º | Gravedad | Qué se hizo |
|---|---|---|
| V2-01 | MAYOR | Cada uno de los 36 planes entra ahora en una hoja oficio. Detalle debajo de la tabla. |
| V2-02 | MAYOR | Plan Anual con márgenes de 1,27 cm y la tabla extendida al ancho útil completo de la hoja horizontal (de 26,7 a 30,5 cm). Las filas quedan más bajas y el documento pasa de 12 a 10 páginas. La firma ya no queda sola: comparte la última hoja con los criterios generales y las estrategias de inclusión, que ocupa en un 71 %. |
| V2-03 | MENOR / decisión de Fer | No se tocaron la portada ni la contraportada del Libro. Queda pendiente el criterio de Fer (y de Gemini, si Fer lo decide) sobre el lienzo ampliado de esas dos composiciones. |
| V2-04 | MENOR | No se borró ni se editó nada en Drive. Se propone a Fer rotular `_TRABAJO/03_NOTAS_PILOTO_SOFTWARE_1_ESENCIAL_v1` como «HISTÓRICA / SUPERSEDIDA». Las notas vigentes son `entrega/NOTAS_PILOTO_SOFTWARE_1_ESENCIAL_v2.md`. |

**V2-01 en detalle.** Cambios, todos de maquetación:
- **Márgenes:** de 1,6/2,0 cm a **1,27 cm**, el estándar de la colección. Encabezado y pie a 0,6 cm.
- **Tablas:** se extendieron al nuevo ancho útil.
- **Tipografía de las celdas:** de 9,5 a **9 pt**.
- **Espaciado:** el espacio posterior de los párrafos de tabla pasó de 2 pt a 0, y el de los separadores entre tablas de 2 a 1 pt.
- **Plan 36:** es la integradora, con las 13 capacidades de la etapa. Además, sus celdas dejan de heredar los 3 pt de espacio del estilo Normal.

No se quitó ningún indicador, actividad, criterio ni firma. El índice se regeneró y coincide con el PDF en las 36 entradas.

**Ajuste adicional (no estaba en el informe).** El Plan 36 era el único sin «primera página distinta», así que mostraba en su primera hoja el encabezado «… · continuación». Se le agregó, como en los otros 35 planes.

## 2. Páginas antes y después

| Documento | v1 | v2 |
|---|---|---|
| Planes de Clase | 60 (21 hojas de continuación con menos del 20 % ocupado) | **38** (cada plan en una hoja; ocupación de 69 % a 95 %) |
| Plan Anual | 12 (la última, solo con la firma) | **10** |
| Muestra | 14 (terminaba en el Plan 1 y su continuación) | **13** (termina en la portada de los Planes y el Plan 1 en una hoja) |
| Libro / Solucionario | 107 / 17 | sin cambios |

## 3. Controles (`build/control_v2.py`, 94 OK · 0 fallos)

- **Planes:**
  - 38 páginas.
  - Las páginas 3 a 38 abren los planes 1 a 36, en orden.
  - Ninguna hoja de continuación.
  - Firmas en cada hoja.
  - Oficio en todas.
- **Plan Anual:**
  - Como máximo 11 páginas (tiene 10).
  - La última hoja no tiene solo la firma.
  - Oficio horizontal.
- **Márgenes:** 1,27 cm en todas las secciones de los dos .docx.
- **Identidad textual con la v1:** se compara con el commit `61feba7`; solo cambian los números del índice.
- **Muestra:**
  - 13 páginas.
  - Plan 1 en una hoja.
  - Sin claves del solucionario.
- **Índice de los Planes contra el PDF:** 36 de 36 entradas (`build/tocchk.py`).

Revisé a ojo las 38 hojas de los Planes y las 10 del Plan Anual:
- Ningún plan pierde contenido.
- Las firmas quedan dentro de la hoja.
- La letra de 9 pt sigue siendo legible.

## 4. Limitaciones

- **Renderizado de los PDF:** se usó LibreOffice con la fuente Carlito, métricamente equivalente a Calibri. Es la misma vía de la v1, cuyos PDF se reprodujeron exactamente (60 y 12 páginas) antes de corregir. En Word la paginación puede variar levemente; si algún plan pasara a dos hojas, hay que actualizar el índice con F9.
- **Imágenes:** los .docx corregidos no tienen imágenes nuevas ni modificadas.
