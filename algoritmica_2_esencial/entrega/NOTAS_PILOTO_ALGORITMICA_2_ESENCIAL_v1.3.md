# NOTAS DEL PILOTO — Algorítmica 2.º Curso BTI · Edición Esencial Comercial 2026 · v1.3

**Estado: listo para la reauditoría breve de ChatGPT.** No se declara listo para la venta: la aprobación comercial es exclusiva de Fer.

La v1.3 responde a `04_REAUDITORIA_CHATGPT_ALGORITMICA_2_ESENCIAL_v1.2`. El detalle está en `04_RESPUESTA_CLAUDE_REAUDITORIA_ALGORITMICA_2_ESENCIAL_v1.3.md`. Las notas de la v1.2 siguen valiendo para todo lo que no se menciona aquí.

## Qué se entrega (`salida_v1_3/`)

| Pieza | Archivo | Páginas |
|---|---|---|
| Libro del estudiante con prácticas | Algoritmica_2do_Curso_LIBRO_ESENCIAL_COMERCIAL_2026.docx + .pdf | 114 |
| Solucionario docente | Algoritmica_2do_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026.docx + .pdf | 18 |
| Plan Anual (36 encuentros) | Algoritmica_2do_Curso_PLAN_ANUAL_COMERCIAL_2026.docx + .pdf | 7 |
| Planes de Clase (36) | Algoritmica_2do_Curso_PLANES_DE_CLASE_COMERCIAL_2026.docx + .pdf | 38 |
| Muestra comercial | Algoritmica_2do_Curso_MUESTRA_COMERCIAL_2026.pdf | 15 |

- **Commit:** `b5003f72c41cd637280246483b12b9f4b992928f` (rama `claude/zen-meitner-kes7dg`).
- **Huellas SHA-256 completas** de los 9 archivos: en `build/auditoria_resultado.txt`.
- **Versiones anteriores intactas:** `salida_v1_2/` y `salida/`.

## Cambios de la v1.3

| Hallazgo | Corrección | Archivo/página | Estado |
|---|---|---|---|
| 09 · Promesa «Práctica N empieza en página propia y se puede fotocopiar suelta» falsa en 4 prácticas (7 según el control nuevo) | Ninguna sección sube a la hoja anterior. Las 21 Prácticas abren y cierran en hoja propia. Las hojas residuales se resuelven con el nivel 4 de compactación (márgenes internos de cajas y tablas), con la misma letra. | Libro, pp. 47, 56, 97, 106 y todas las Prácticas; Presentación p. 2 (texto sin cambios, ahora verdadero) | CORREGIDO |
| 08 · Huellas de 16 caracteres rotuladas «sha256» | SHA-256 completo de 64 hexadecimales y hash Git completo del commit. | `build/auditoria_resultado.txt` | CORREGIDO |
| B.6 · Verificación visual de márgenes y letra | Medición con PyMuPDF sobre los PDF: Planes ≥ 9,5 pt (salvo el pie); márgenes de 1,27 cm; ocupación ≥ 33 %. Revisión visual de las páginas pedidas. | Ver 04_RESPUESTA §2 | HECHO en LibreOffice; Word pendiente |

## Auditoría automática

916 controles y 0 fallos.

- **Bloque K nuevo:** 22 controles de Práctica suelta y un control de «ninguna sección sube».
- **Validación:** sobre la v1.2, el control detecta las Prácticas 9, 11, 19 y 21 (no abren hoja) y 13, 17 y 20 (comparten su última hoja).

## Ajustes de paginación del Libro (`build/ajustes_paginacion.json`)

| Nivel | Secciones |
|---|---|
| Compacto (1) | 14 secciones |
| Nivel 2 | 9 secciones |
| Nivel 3 | Clases 9 y 11, Prácticas 17, 20 y 21, PFI |
| Nivel 4 | Clase 11, Prácticas 17, 20 y 21 |
| `sin_salto` | vacío |

Ningún nivel cambia el tamaño de letra.

## Pendiente de comprobación manual

- **Word**, que no está disponible en este entorno. Abrir:
  - los Planes 17 y 36;
  - la p. 7 del Plan Anual;
  - las evaluaciones de dos hojas;
  - las Prácticas 9, 11, 19 y 21.

  Confirmar que no hay desbordes.
- **Access y Windows:** igual que en las notas v1.2.

## Decisiones para Fer

- **Planificación compartida:** confirmar si el Plan Anual y los Planes de Clase acompañan también a la Edición Completa (hallazgo 07).
- **Merge:** autorizar el merge o PR de `claude/zen-meitner-kes7dg` hacia `claude/libros-5z31jx`.

**Estado final: listo para la reauditoría breve. No aprobado para la venta.**
