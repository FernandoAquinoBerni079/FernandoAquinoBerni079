# Notas del piloto — Gabinete de Informática – Software · 1.er Curso BTI · Edición Esencial Comercial 2026 (v1)

Estado: **v1 corregida, lista para la auditoría v2 de ChatGPT. No está aprobada para la venta.**
Integrada al repositorio el 11/10/2026 en `software_1_esencial/`, rama `claude/libros-5z31jx`.
Reemplaza a `_TRABAJO/03_NOTAS_PILOTO_SOFTWARE_1_ESENCIAL_v1` de Drive (02/10/2026), que todavía dice «137 páginas» y describe la versión anterior a la auditoría.

## Archivos del combo (`salida/`)

| Archivo | Páginas | Papel |
|---|---|---|
| Gabinete_Informatica_Software_1er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026 (.docx 23,3 MB y .pdf) | 107 | Oficio, márgenes de 1,27 cm |
| Gabinete_Informatica_Software_1er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026 (.docx y .pdf) | 17 | Oficio, márgenes de 1,27 cm |
| Gabinete_Informatica_Software_1er_Curso_PLAN_ANUAL_COMERCIAL_2026 (.docx y .pdf) | 12 | Oficio (portada vertical; tabla apaisada) |
| Gabinete_Informatica_Software_1er_Curso_PLANES_DE_CLASE_COMERCIAL_2026 (.docx y .pdf) | 60 (36 planes) | Oficio |
| Gabinete_Informatica_Software_1er_Curso_MUESTRA_COMERCIAL_2026 (.pdf) | 14 | Oficio |

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

- Auditoría de contenido (`build/auditoria_v1.py`): **117 controles, 0 fallos**. Cubre capacidades, fusiones, unicidad de datos, aritmética, coherencia entre Libro y Solucionario, Ley 7593, erratas, figuras y papel oficio.
- Sincronía DOCX↔PDF: cada .docx se volvió a renderizar con LibreOffice. Libro, Solucionario y Plan Anual dan el mismo texto que su PDF. En los Planes solo cambia el largo de los puntos del índice (el PDF original salió de LibreOffice 25.2), y la cantidad de páginas es la misma.
- Índices: Libro 61 entradas, Solucionario 65 y Planes 36. En los tres, 0 diferencias con el PDF.
- Páginas interiores ocupadas en menos del 25 %: Libro 0; Solucionario 0 (la p. 2 es la Presentación); Plan Anual 0.
- Muestra: las 14 páginas son idénticas a la página correspondiente de su documento de origen.
- Metadatos: autor «Equipo editorial» en los cuatro .docx; el .docx del Libro pesa 23,3 MB, por debajo del límite de 25 MB.

## Pendiente de auditoría o de decisión

1. **Auditoría v2 de ChatGPT** sobre esta versión. Corresponde porque la v1 tuvo hallazgos críticos (§3, paso 5).
2. **Gemini y Fer: portada y contraportada.** Se alargó el lienzo de las dos composiciones para llevarlas a oficio. Hay que confirmar que eso cumple la regla de imágenes (§3ter).
3. **Planes de Clase: 21 páginas de «continuación» quedan ocupadas en menos del 25 %**, porque cada plan pasa a hoja propia el bloque de evaluación y recursos. Es el diseño del generador. En otra sesión (`claude/vigilant-einstein-9wbdg0`, `oficio_planes.py`) se aplicó a otras materias un formato de «cada plan en hoja propia»; está pendiente decidir si se aplica acá.
4. **Libro en Drive:** hay que reemplazarlo por este (.docx de 23.332.109 bytes). El de Drive es la revisión anterior, sin los párrafos ancla de las evaluaciones.
5. **Drive `03_NOTAS`:** actualizar las páginas a 107, o reemplazar ese documento por este.
6. **Protocolo v0.4:** sigue en BORRADOR; sus pendientes (§8) siguen abiertos: sello de colección, mínimos de la Completa y paquetes MEC_/POTY_.
7. **Aprobación final de Fer** y alta en el catálogo (LISTO PARA VENTA, VERSION_CANONICA, MUESTRA_LISTA). **No se hizo.**
