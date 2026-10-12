# NOTAS_CIERRE_ALGORITMICA_3_FINAL_OFICIO_v2

**Algorítmica · 3.er Curso BTI · Edición Esencial Comercial 2026 — FINAL OFICIO v2**

**Estado: corregida según el Informe 03 (auditoría ChatGPT, 11/10/2026); vuelve a reauditoría.**

**No está aprobada para la venta.** Falta la reauditoría y el OK final de Fer.

Fecha: 12/10/2026. El detalle de cada hallazgo está en `03_RESPUESTA_CLAUDE_ALGORITMICA_3_ESENCIAL_FINAL_OFICIO_v2.md`.

## Archivos (`salida_FINAL_OFICIO_v2/`)

| Pieza | Archivo | Páginas |
|---|---|---|
| Libro | Algoritmica_3er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO_v2 (.docx y .pdf) | 117 |
| Solucionario | Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026_FINAL_OFICIO_v2 (.docx y .pdf) | 18 |
| Planes de Clase (comunes a ambas ediciones) | Algoritmica_3er_Curso_PLANES_DE_CLASE_COMERCIAL_2026_FINAL_OFICIO_v2 (.docx y .pdf) | 38 |
| Plan Anual (común a ambas ediciones) | Algoritmica_3er_Curso_PLAN_ANUAL_COMERCIAL_2026_FINAL_OFICIO_v2 (.docx y .pdf) | 6 |
| Muestra comercial | Algoritmica_3er_Curso_MUESTRA_COMERCIAL_2026_FINAL_OFICIO_v2.pdf | 15 |

## Cómo se regenera

Las rutas `/home/claude/alg3/` apuntan a la carpeta `algoritmica_3_esencial/`.

1. Libro y Solucionario, desde FINAL OFICIO:
   `python3 -I build/final_oficio/correcciones_v2.py <LIBRO_FO.docx> <SOL_FO.docx> <LIBRO_v2.docx> <SOL_v2.docx>`
   y después convertir a PDF con LibreOffice.
2. Comprobar el índice: `build/final_oficio/indice.py` (sin cambios: 54/54 y 53/53).
3. `python3 build/build_planes_fo_v2.py` hace la compactación selectiva y verifica el índice; escribe `build/indice_planes_v2.json`.
4. `python3 build/build_plan_anual_fo_v2.py`.
5. `python3 build/build_muestra_fo_v2.py`.
6. `python3 -I build/final_oficio/verificar_v2.py` → `build/verificacion_v2.txt` (**81 controles, 0 fallos**).

## Qué cambió respecto de FINAL OFICIO

| Pieza | Cambios |
|---|---|
| Libro | Capacidad transversal Conductual (Presentación y Proyecto Final) · Access fuera de soporte (Clase 18) · Práctica 3 con datos y semana propios · Evaluación U4, ítem 7, e Integradora 2, ítem 8, con datos nuevos · autoevaluación al cierre de las Clases 6 y 19 |
| Solucionario | Las claves correspondientes · nota de Access · orientación sobre la capacidad transversal |
| Planes | Solo maquetación: 13 planes compactados (los Planes 1, 26, 28 y 31 en 9 pt) · 51 → 38 páginas · nombre sin edición |
| Plan Anual | Solo el nombre del archivo |
| Muestra | El Plan N.º 1 en una sola hoja · se suma la primera página de la Clase 18 |

Lo demás no cambió: oficio, márgenes, figuras, portadas, índices, aritmética ya verificada, 21 clases y 21 prácticas, 36 encuentros (144 HC).
