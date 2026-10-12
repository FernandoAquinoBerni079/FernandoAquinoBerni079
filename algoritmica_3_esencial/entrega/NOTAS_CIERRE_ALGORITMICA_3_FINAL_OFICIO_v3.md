# NOTAS_CIERRE_ALGORITMICA_3_FINAL_OFICIO_v3

**Algorítmica · 3.er Curso BTI · Edición Esencial Comercial 2026 — FINAL OFICIO v3**

**Estado: corregida según la reauditoría 04 (ChatGPT, 12/10/2026); vuelve a reauditoría.**

**No está aprobada para la venta.** Falta la reauditoría y el OK final de Fer.

Fecha: 12/10/2026. El detalle está en `05_RESPUESTA_CLAUDE_ALGORITMICA_3_ESENCIAL_FINAL_OFICIO_v3.md`.

## Archivos (`salida_FINAL_OFICIO_v3/`)

| Pieza | Archivo | Páginas | Cambio frente a v2 |
|---|---|---|---|
| Libro | Algoritmica_3er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO_v3 (.docx y .pdf) | 117 | Hallazgos 10 (Clase 21) y 11 (Proyecto Final) |
| Solucionario | Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO_v3 (.docx y .pdf) | 18 | Ninguno (idéntico byte a byte) |
| Planes de Clase (comunes a ambas ediciones) | Algoritmica_3er_Curso_PLANES_DE_CLASE_COMERCIAL_2026_FINAL_OFICIO_v3 (.docx y .pdf) | 38 | Ninguno (idéntico byte a byte) |
| Plan Anual (común a ambas ediciones) | Algoritmica_3er_Curso_PLAN_ANUAL_COMERCIAL_2026_FINAL_OFICIO_v3 (.docx y .pdf) | 6 | Ninguno (idéntico byte a byte) |
| Muestra comercial | Algoritmica_3er_Curso_MUESTRA_COMERCIAL_2026_FINAL_OFICIO_v3.pdf | 15 | Regenerada; misma composición |

## Cómo se regenera

1. `python3 -I build/final_oficio/correcciones_v3.py <LIBRO_v2.docx> <LIBRO_v3.docx>` y después convertir a PDF con LibreOffice.
2. Comprobar el índice: `build/final_oficio/indice.py` (54/54, sin cambios).
3. Copiar Solucionario, Planes y Plan Anual de la v2 con el sufijo `_v3`.
4. `python3 build/build_muestra_fo_v3.py`.
5. `python3 -I build/final_oficio/verificar_v3.py` → `build/verificacion_v3.txt` (**99 controles, 0 fallos**).
6. `python3 -I build/final_oficio/revision_visual_v3.py` → `build/revision_visual_v3/` (medidas e imágenes).
