# NOTAS DEL PILOTO — Algorítmica 1.er Curso BTI · Edición Esencial Comercial 2026 · v1.3.1

**Estado: listo para la inspección visual final y la aprobación de Fer. NO se declara aprobado para la venta.**

La v1.3.1 responde a la reauditoría de la v1.3. El veredicto fue «correcciones requeridas»: toda práctica debe abrir en hoja propia. Reemplaza a la v1.3 solo en eso. H01, H02, H04 y H05 pasaron la reauditoría y no cambian; H06 y H07 están cerrados por decisión de Fer. Salida: `salida_v1_3_1/`. Las versiones anteriores (`salida/` = v1.2, `salida_v1_3/` = v1.3) quedan intactas.

## Qué se entrega

| Pieza | Archivo (`salida_v1_3_1/`) | Páginas |
|---|---|---|
| Libro del estudiante con prácticas | Algoritmica_1er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026.docx + .pdf | 107 |
| Solucionario docente | Algoritmica_1er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026.docx + .pdf | 19 |
| Plan Anual (37 encuentros) | Algoritmica_1er_Curso_PLAN_ANUAL_COMERCIAL_2026.docx + .pdf | 8 |
| Planes de Clase (37) | Algoritmica_1er_Curso_PLANES_DE_CLASE_COMERCIAL_2026.docx + .pdf | 39 |
| Muestra comercial | Algoritmica_1er_Curso_MUESTRA_COMERCIAL_2026.pdf | 14 |

## Qué cambió respecto de la v1.3

- **Página propia restaurada.** Cada clase, cada práctica y cada evaluación abre página, como en la v1.2. Se quitó del build el mecanismo que unía secciones.
- **Páginas casi vacías.** Se resuelven redistribuyendo contenido dentro de cada sección (`build/ajustes_libro.json`, clave `cortes`). Un bloque completo de la hoja anterior pasa a la última hoja de la clase o la práctica:
  - en las Clases 2, 3, 4, 7, 8, 9, 11, 12, 15 y 21, el bloque es «Actividades de aplicación»;
  - en las Prácticas 8, 17 y 21, la «Actividad 2»; en la Práctica 14, la «Actividad 3».

  El corte sube con el título y los párrafos que deben ir juntos. No se comprimen cuadros, figuras ni tipografía. `build/ajustar_libro.py` elige los cortes y prefiere los bordes de bloque.
- **Evaluaciones.** Igual que en la v1.3: la integradora 1 tiene renglones de 0,58 cm; la Unidad 3 y la integradora 2 llevan la Parte B en hoja propia. Siempre son 3 renglones por consigna.
- **Auditoría.** Los controles de salto vuelven a ser estrictos. Hay controles nuevos:
  - el build no tiene mecanismo de unión;
  - cada corte queda dentro de su sección;
  - los renglones de respuesta se cuentan en el PDF.

  La lista completa de controles está en `build/auditoria_detalle.txt`.

## Verificación

**820 controles · 0 fallos.**
- Prácticas 21/21, evaluaciones 5/5 y clases 21/21 abren página, sin excepción.
- 0 páginas bajo el 25 % en los cinco PDF (la más baja del Libro mide 27 %).
- Renglones: 3 por consigna en las 5 evaluaciones (87 en total, contados en el PDF).
- 15/15 capacidades MEC; 0 hojas de Planes con solo firmas; índices exactos (52 + 52 + 37); DOCX ↔ PDF sincronizados.
- PSeInt 20250314: 35 casos, 0 fallos.

## Pendiente para Fer

- Inspección visual final del PDF, especialmente Planes, evaluaciones y las 14 hojas con cortes, y comparación de hashes en la ubicación definitiva.
- Figura 21.1 (mejora opcional) y la pasada en PSeInt para Windows.
- **Aprobación comercial: solo Fer. No aprobado para la venta.**
