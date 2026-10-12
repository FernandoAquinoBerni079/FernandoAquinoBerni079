# NOTAS DEL PILOTO — Algorítmica 1.er Curso BTI · Edición Esencial Comercial 2026 · v1.3

**Estado: listo para reauditoría independiente de ChatGPT y aprobación de Fer. NO se declara aprobado para la venta.**

v1.3 corrige el Informe 01 del compendio de auditorías (sobre la v1.2 oficio). Se regeneró con el pipeline de `build/`, sin rehacer desde cero. Las versiones anteriores (`salida/`, v1.2 y previas) **no se tocaron**; la v1.3 está en `salida_v1_3/`.

## Qué se entrega

| Pieza | Archivo (`salida_v1_3/`) | Páginas |
|---|---|---|
| Libro del estudiante con prácticas | Algoritmica_1er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026.docx + .pdf | 97 (v1.2: 108) |
| Solucionario docente | Algoritmica_1er_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026.docx + .pdf | 19 |
| Plan Anual (37 encuentros) | Algoritmica_1er_Curso_PLAN_ANUAL_COMERCIAL_2026.docx + .pdf | 8 |
| Planes de Clase (37) | Algoritmica_1er_Curso_PLANES_DE_CLASE_COMERCIAL_2026.docx + .pdf | 39 (v1.2: 43) |
| Muestra comercial | Algoritmica_1er_Curso_MUESTRA_COMERCIAL_2026.pdf | 14 |

**Plan Anual y Planes de Clase ya no llevan «ESENCIAL» en el nombre:** son piezas compartidas por las ediciones Esencial y Completa (H05). Libro y Solucionario conservan «ESENCIAL_COMERCIAL».

Sin cambios: 3 unidades, 21 clases, 13 actividades por clase, 3 por práctica, las 5 evaluaciones en su lugar, la rúbrica del PFI, el formato oficio y **los 37 encuentros (148 HC), por decisión de Fer (H06)**.

## Cambios de la v1.3

| Hallazgo | Cambio | Dónde |
|---|---|---|
| H01 (CRÍTICO) | Las 3 capacidades transversales MEC, textuales, con el encabezado «Capacidad transversal MEC», un indicador observable y una actividad evaluable por unidad. | Libro: apertura de cada unidad y Prácticas 5, 9 y 20 (paso 4 + punto de control). Planes N.º 8, 15 y 34 (fila propia, actividad y criterio). Solucionario: clave del indicador en esas tres prácticas. |
| H02 | Cada plan en una sola hoja, con criterios, observaciones y firmas. Texto ≥ 9 pt; solo se ajustó espaciado y bordes; en los planes 8 y 15 los puntos de control remiten a la Práctica del libro. | Planes N.º 8, 15, 34, 35, 36 |
| H03 | Reajuste de saltos para que ningún ítem o desafío quede solo en una hoja. | Libro, ver abajo |
| H04 | Integradora 2, Parte A n.º 3: G. 86.000 → c) G. 77.400. | Libro p. 94 (Evaluación integradora de la 2.ª etapa), Solucionario |
| H05 | Renombre de Plan Anual y Planes. | `salida_v1_3/` |
| H06 | Decisión de Fer: 37 encuentros. | — |
| H07 | Decisión de Fer: Figura 21.1 queda como mejora opcional. | — |

### H03 en detalle

- Se une la Práctica N a la Clase N (Clases 2, 3, 4, 5, 7, 11, 12, 15 y 21) o la Clase N+1 a la Práctica N (Prácticas 2, 3, 4, 7, 8, 11, 14, 15 y 17) cuando la hoja anterior quedaba casi vacía. Las uniones están en `build/uniones_libro.json`.
- Salto de página antes de la Actividad 2 en las Prácticas 12 y 21, para repartir mejor el contenido.
- Evaluaciones: la integradora de la 1.ª etapa usa renglones de menor altura (siguen siendo 3 por consigna); la **Unidad 3** y la **integradora de la 2.ª etapa** llevan la Parte B en una hoja propia, con espacio de respuesta completo.
- Medición: `build/ocupacion.py` mide el borde inferior del último contenido (texto, imágenes y renglones) sobre el alto útil. Con ese método la v1.2 reproduce las 17 hojas del informe; la v1.3 tiene **0 hojas bajo el 25 %** (la más baja es del 28 %).

## Verificación

**796 controles · 0 fallos** (`build/auditoria_resultado.txt`), con el bloque K nuevo para este informe:
- 15/15 capacidades MEC literales en Libro, Planes y Plan Anual;
- las 3 transversales en Libro (unidad + práctica), Solucionario y 3 planes;
- 0 hojas de Planes con solo firmas; los 37 planes en una hoja cada uno, texto ≥ 9 pt;
- 0 páginas por debajo del 25 % en Libro, Solucionario, Planes, Plan Anual y Muestra; sin hojas en blanco;
- E2 n.º 3 con 86.000 / 94.600 / 77.400, clave c), sin aparecer resuelto en la Clase 17;
- índices exactos (número impreso = página real): Libro 52, Solucionario 52, Planes 37;
- DOCX ↔ PDF: cada párrafo de los cuatro DOCX figura en su PDF, el PDF es posterior al DOCX y el total de páginas coincide con el índice;
- los 35 casos de PSeInt 20250314 (perfil Flexible) se re-ejecutaron: 0 fallos.

## Cómo se regeneró

`build_libro.py` (con `ajustar_libro.py` para los saltos) → `build_solucionario.py` → `build_plan_anual.py` → `build_planes.py` (compactación automática de planes que desbordan) → `build_muestra.py` → `auditoria.py`. Fuentes únicas nuevas: `ediciones.TRANSV` (capacidades transversales) y `uniones_libro.json` (saltos).

Dos precisiones técnicas del entorno de esta sesión: los estilos del DOCX se tomaron del Libro v1.2 (`build/plantilla_estilos_v1_2.docx`) porque el DOCX fuente de 3.º que usaba `maqueta.py` no está en el repositorio; y PSeInt 20250314 se bajó de la fuente oficial para volver a correr los programas.

## Decisiones y pendientes para Fer

- **Prácticas sin hoja propia.** Para eliminar hojas casi vacías, 18 secciones de práctica/clase ya no abren página (ver H03). Si preferís que cada práctica abra siempre en hoja propia, hay que aceptar más hojas con poco contenido: es un cambio en `uniones_libro.json`.
- **Letra de la clave de H04:** c) en lugar de a) (propuesta del informe) para mantener la distribución b–a–c de la integradora.
- **Figura 21.1:** sigue como en la v1.2 (densa); el rediseño es opcional (H07).
- **PSeInt en Windows:** sigue pendiente la pasada en la versión instalada en el colegio.
- **Aprobación comercial:** solo Fer. Falta la reauditoría independiente de la v1.3.

**Estado final: listo para reauditoría independiente de ChatGPT y aprobación de Fer. No aprobado para la venta.**
