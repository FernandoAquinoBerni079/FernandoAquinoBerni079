# NOTAS_PILOTO_ALGORITMICA_3_ESENCIAL_v2_2

**Algorítmica · 3.er Curso BTI · Edición Esencial Comercial 2026 — Formato oficio v2.2**

**Estado: CORREGIDO — pendiente de comprobación manual de Access/PSeInt y aprobación de Fer.**

El paquete no está declarado listo para la venta.

Fecha: 07/10/2026. Esta versión cambia **solo el formato**: el contenido es idéntico al de la v2.1, con sus cuatro correcciones de cierre (capacidad de la Clase 15, recuadro «En Paraguay — integridad y facturación», Práctica 6 Actividad 3 y punto de control de la Práctica 19 Actividad 2). Las versiones v1, v2 y v2.1 (A4) se conservan; los archivos nuevos llevan el sufijo `_v2_2`.

## 1. Archivos

| Pieza | Archivo v2.2 | Páginas (v2.1 → v2.2) |
|---|---|---|
| Libro | Algoritmica_3er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026_v2_2 (.docx y .pdf) | 154 → **125** |
| Solucionario | Algoritmica_3er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026_v2_2 (.docx y .pdf) | 24 → **18** |
| Planes de Clase | Algoritmica_3er_Curso_PLANES_DE_CLASE_ESENCIAL_COMERCIAL_2026_v2_2 (.docx y .pdf) | 75 → **51** |
| Plan Anual | Algoritmica_3er_Curso_PLAN_ANUAL_ESENCIAL_COMERCIAL_2026_v2_2 (.docx y .pdf) | 8 → **6** |
| Muestra comercial | Algoritmica_3er_Curso_MUESTRA_COMERCIAL_2026_v2_2.pdf | 18 → **16** |

## 2. Formato oficio

Por decisión de Fer, todo el paquete pasa a **oficio 21,6 × 33 cm** para bajar el costo de impresión de docentes y estudiantes; no queda nada en A4:
- libro, solucionario y Planes de Clase en vertical; Plan Anual en horizontal (33 × 21,6 cm);
- márgenes estrechos de 1,27 cm por lado (ancho útil de 19,06 cm; 30,46 cm en el Plan Anual);
- tablas, cajas, fichas, bandas de evaluación y renglones al 100 % del ancho de la página, con las columnas escaladas en proporción;
- figuras hasta un 10 % más grandes (máximo 17,5 cm);
- portadas y contraportada regeneradas en proporción oficio. Se quitó además el «✓» que tenía la lámina de la portada («G. 134.000»).

Los índices se rearmaron y se verificaron contra el PDF.

## 3. Auditoría automática

**891 controles · 0 fallos.** A los 874 de la v2.1 se suman 16 controles de formato y 1 del retoque de la Figura 9.1: tamaño de hoja y márgenes de todas las secciones, tablas al 100 % y PDF en oficio. Detalle en `build/auditoria_resultado.txt`.

## 4. Figura 9.1

Por pedido de Fer, la Figura 9.1 (imagen del tomo) se retocó como en 1.º: se quitaron el ✓ de «ACEPTA» y las ✗ de los dos «RECHAZA», en una copia (`build/figs_ret/image12.jpg`, script `build/retoques.py`). El original se conserva sin cambios y las otras 27 imágenes del tomo van byte a byte.

## 5. Pendiente

- Siguen vigentes las comprobaciones manuales de Access y PSeInt de la v2.1.
