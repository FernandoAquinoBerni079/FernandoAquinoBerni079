# Notas del piloto — Gabinete de Informática – Software · 1.er Curso BTI · Edición Esencial Comercial 2026 (v1)

Estado: **v3 — corregida según la conciliación de las dos auditorías v2 de ChatGPT (H02 y H15; detalle en 03_RESPUESTA_CLAUDE_SOFTWARE_1_ESENCIAL_v3 y 06_CONCILIACION_AUDITORIAS_SOFTWARE_1_ESENCIAL_v2). Vuelve a ChatGPT para la auditoría de cierre. No está aprobada para la venta.**
Integrada al repositorio el 11/10/2026 en `software_1_esencial/`, rama `claude/libros-5z31jx`.
Reemplaza a `_TRABAJO/03_NOTAS_PILOTO_SOFTWARE_1_ESENCIAL_v1` de Drive (02/10/2026), que todavía dice «137 páginas» y describe la versión anterior a la auditoría.

## Archivos del combo (`salida/`)

| Archivo | Páginas | Papel |
|---|---|---|
| Gabinete_Informatica_Software_1er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026 (.docx 23,3 MB y .pdf) | 107 | Oficio, márgenes de 1,27 cm |
| Gabinete_Informatica_Software_1er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026 (.docx y .pdf) | 17 | Oficio, márgenes de 1,27 cm |
| Gabinete_Informatica_Software_1er_Curso_PLAN_ANUAL_COMERCIAL_2026 (.docx y .pdf) | 11 | Oficio, márgenes de 1,27 cm (portada vertical; tabla apaisada) |
| Gabinete_Informatica_Software_1er_Curso_PLANES_DE_CLASE_COMERCIAL_2026 (.docx y .pdf) | 38 (36 planes, uno por hoja) | Oficio, márgenes de 1,27 cm |
| Gabinete_Informatica_Software_1er_Curso_MUESTRA_COMERCIAL_2026 (.pdf) | 13 | Oficio |

El Plan Anual y los Planes de Clase **no llevan edición en el nombre**, porque se comparten entre la Esencial y la Completa (§3bis). Así lo pidió el hallazgo 13 de la auditoría v1.

## Qué tiene esta versión

- Libro unificado (§3quater): cada Práctica N va después de su Clase N, en página propia; las Fichas A–K están en las semanas de continuidad; el Proyecto Final cierra el libro.
- Correcciones de la auditoría v1 (14 hallazgos; detalle en `05_RESPUESTA…md`):
  - las 20 capacidades MEC, textuales, en el Libro, los Planes y el Plan Anual, más la capacidad que faltaba;
  - la Ley 7593/2025 presentada en *vacatio legis* hasta el 27/11/2027;
  - datos de almacenamiento y operandos binarios sin repetir;
  - Windows no genuino y grooming;
  - figuras, erratas y nombres.
- Siete correcciones que no estaban en la auditoría. Las principales: operaciones inversas repetidas en la Unidad 3 y capacidades mal asignadas en los Planes 10, 15, 17 y 21.
- Formato oficio con márgenes estrechos y tablas ajustadas a la ventana (decisión de Fer del 02/10/2026) en el Libro y el Solucionario. El Plan Anual y los Planes de Clase se pasaron a oficio en otra sesión, el 02/10 a las 16:40. **La 05_RESPUESTA dice que esos dos «siguen en A4»; eso ya no es así.**
- Índices poblados, con números de página verificados contra el PDF y sin la leyenda «Ctrl+E/F9».
- Imágenes: 26 de las 28 del Libro son idénticas, byte a byte, al original de Fer. Las otras 2 son la portada y la contraportada (composiciones con una foto de Gemini adentro): se agrandó el lienzo a la proporción de oficio agregando filas del mismo verde. No se recortó ni se estiró nada.

## Controles técnicos (11/10/2026, sobre `salida/`)

Los resultados completos están en `build/auditoria_resultado.txt`.

- Auditoría de contenido (`build/auditoria_v1.py`): **117 controles, 0 fallos** (repetida sobre la v3). Cubre capacidades, fusiones, unicidad de datos, aritmética, coherencia entre Libro y Solucionario, Ley 7593, erratas, figuras y papel oficio. Controles de la v3 contra la v2 (`build/control_v3.py`): **657 OK · 0 fallos**.
- Sincronía DOCX↔PDF: cada .docx se volvió a renderizar con LibreOffice. Libro, Solucionario y Plan Anual dan el mismo texto que su PDF. En los Planes solo cambia el largo de los puntos del índice (el PDF original salió de LibreOffice 25.2), y la cantidad de páginas es la misma.
- Índices: Libro 61 entradas, Solucionario 65 y Planes 36. En los tres, 0 diferencias con el PDF.
- Páginas interiores ocupadas en menos del 25 %: Libro 0; Solucionario 0 (la p. 2 es la Presentación); Plan Anual 0.
- Muestra: las 13 páginas son idénticas a la página correspondiente de su documento de origen.
- Metadatos: autor «Equipo editorial» en los cuatro .docx; el .docx del Libro pesa 23,3 MB, por debajo del límite de 25 MB.

## Pendiente de auditoría o de decisión

1. **Comprobación de cierre de ChatGPT.** La auditoría v2 (02_AUDITORIA_CHATGPT_SOFTWARE_1_ESENCIAL_v2) dio «APTO CON CORRECCIONES MAYORES»: 12 de 14 hallazgos de la v1 cerrados y los MAYORES V2-01 y V2-02 de maquetación, corregidos en esta v2.
2. **Gemini y Fer: portada y contraportada.** Se alargó el lienzo de las dos composiciones para llevarlas a oficio. Hay que confirmar que eso cumple la regla de imágenes (§3ter).
3. **Planes de Clase y Plan Anual:** resuelto. Cada plan ocupa una hoja (38 páginas). El Plan Anual tiene 11 páginas en la v3, porque las filas 18 y 36 transcriben ahora las capacidades MEC literales (H02), y no deja hoja de firma suelta.
4. **Pictogramas:** desde la v3 no hay ✓ ✗ ✅ ✔ en el texto de ningún documento (H15). Las imágenes no se modificaron.
4. **Libro en Drive:** hay que reemplazarlo por este (.docx de 23.332.109 bytes). El de Drive es la revisión anterior, sin los párrafos ancla de las evaluaciones.
5. **Drive `03_NOTAS`:** actualizar las páginas a 107, o reemplazar ese documento por este.
6. **Protocolo v0.4:** sigue en BORRADOR; sus pendientes (§8) siguen abiertos: sello de colección, mínimos de la Completa y paquetes MEC_/POTY_.
7. **Aprobación final de Fer** y alta en el catálogo (LISTO PARA VENTA, VERSION_CANONICA, MUESTRA_LISTA). **No se hizo.**
