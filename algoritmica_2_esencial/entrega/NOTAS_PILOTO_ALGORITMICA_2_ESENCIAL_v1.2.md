# NOTAS DEL PILOTO — Algorítmica 2.º Curso BTI · Edición Esencial Comercial 2026 · v1.2

**Estado: listo para reauditoría independiente de ChatGPT.** No se declara listo para la venta: la aprobación comercial es exclusiva de Fer.

La v1.2 corrige los ocho hallazgos del Informe 02 del compendio de auditorías del 11/10/2026. El detalle por hallazgo está en `03_RESPUESTA_CLAUDE_ALGORITMICA_2_ESENCIAL_v1.2.md`.

## Qué se entrega (`salida_v1_2/`)

| Pieza | Archivo | Páginas v1.1 → v1.2 |
|---|---|---|
| Libro del estudiante con prácticas | Algoritmica_2do_Curso_LIBRO_ESENCIAL_COMERCIAL_2026.docx + .pdf | 127 → 113 |
| Solucionario docente | Algoritmica_2do_Curso_SOLUCIONARIO_DOCENTE_ESENCIAL_COMERCIAL_2026.docx + .pdf | 19 → 18 |
| Plan Anual (36 encuentros) | Algoritmica_2do_Curso_PLAN_ANUAL_COMERCIAL_2026.docx + .pdf | 8 → 7 |
| Planes de Clase (36) | Algoritmica_2do_Curso_PLANES_DE_CLASE_COMERCIAL_2026.docx + .pdf | 65 → 38 |
| Muestra comercial | Algoritmica_2do_Curso_MUESTRA_COMERCIAL_2026.pdf | 17 → 15 |

- La v1.1 sigue intacta en `salida/`.
- Todo el paquete está en oficio 21,6 × 33 cm, con márgenes de 1,27 cm. El Plan Anual va en horizontal.
- La estructura curricular no cambió:
  - 4 unidades, 21 clases y 21 prácticas;
  - capacidades MEC textuales e indicadores;
  - 6 evaluaciones en el mismo lugar;
  - 36 encuentros de 4 HC;
  - 3 talleres del PFI;
  - rúbrica 30/25/20/15/10.

## Cambios de la v1.2

| Hallazgo | Corrección | Archivo/página | Estado |
|---|---|---|---|
| 01 · Planes con 27 continuaciones casi vacías | Un plan por hoja, a 9,5 pt y sin quitar contenido: interlineado sencillo en celdas, márgenes de celda menores, separadores de 2 pt, y observaciones y firmas en un bloque. | Planes de Clase, pp. 3–38 | CORREGIDO |
| 02 · Libro con 17 hojas casi vacías | Ajuste por sección medido en el PDF (`build/ajustes_paginacion.json`), con la misma letra:<br>• compactación en 15 secciones;<br>• 8 Clases o Prácticas suben a la última hoja de la sección anterior;<br>• las evaluaciones y el PFI empiezan en hoja propia;<br>• renglones de respuesta proporcionales a la tarea (6 para algoritmos, procedimientos, ordenamientos, consultas y pruebas de escritorio). | Libro, 113 págs. | CORREGIDO |
| 03 · Plan Anual con p. 8 solo de firmas | Criterios e inclusión en dos columnas; firmas en la tabla de cierre. | Plan Anual, p. 7 | CORREGIDO |
| 04 · Muestra con hoja residual y díptico incompleto | Documentos íntegros: Clase 1 y Práctica 1 completas, hoja del Plan Anual, Plan N.º 1 en una hoja; sin claves. | Muestra, 15 págs. | CORREGIDO |
| 05 · Tabla Insumos repetida entre U4 e Integradora 2 | Integradora 2 con HEL-11 a HEL-16 e ítems 6 (Harina) y 9 (Queso). Claves: 120; Queso y Galleta; 36/46/38; Queso 16.000; 210.000 y 128.000. U4 sin cambios. | Libro, pp. 109–110; Solucionario, p. 17 | CORREGIDO |
| 06 · Access 2016 sin advertencia | Fin de soporte en octubre de 2025 y recomendación de Access para Microsoft 365 o Access 2024. Se comprueban rutas y separadores, y se mantiene la alternativa en papel. No se afirma una verificación en Access que no se hizo. | Libro, pp. 95, 97, 102, 106; Solucionario, p. 2 | CORREGIDO |
| 07 · Nombres de la planificación | PLAN_ANUAL_COMERCIAL_2026 y PLANES_DE_CLASE_COMERCIAL_2026; los maestros no se renombraron. | `salida_v1_2/` | CORREGIDO (identidad con la Completa: decisión de Fer) |
| 08 · Reporte de QA ambiguo | Reporte v1.2 con commit, rama y SHA-256; separa la comprobación automática de la revisión visual; bloques K–N nuevos. Los controles se validaron contra la v1.1. | `build/auditoria_resultado.txt` | CORREGIDO |
| Extra · Solucionario p. 4 casi vacía | La Primera parte sigue en la hoja de la diagnóstica. | Solucionario, p. 4 | CORREGIDO |

## Auditoría automática

894 controles y 0 fallos, en 14 bloques:

| Bloque | Qué controla |
|---|---|
| A | Estructura |
| B | Paginación e índices |
| C | Aritmética y PSeInt 20250314 re-ejecutado |
| D | Libro ↔ solucionario |
| E | Duplicados |
| F | Figuras |
| G | Planificación |
| H | Lengua y cobertura |
| I | Lecciones de 3.º |
| J | T1–T20 |
| K | Hojas casi vacías y de firmas |
| L | Independencia entre evaluaciones |
| M | Access 2016 |
| N | Nombres |

- **Commit auditado:** `673a5b7`, con el árbol limpio.
- **Validación de los controles nuevos** contra la v1.1, que debía fallar: detectan las 27 hojas de Planes, 20 hojas del Libro (las 17 del informe y 3 más), la p. 8 del Plan Anual, las pp. 10 y 17 de la Muestra, la p. 4 del Solucionario y la tabla Insumos repetida.
- **0 fallos automáticos no equivale a APTO editorial.**

## Revisión visual de esta sesión

Se miraron sobre el PDF renderizado:
- un plan cargado (N.º 17);
- la última hoja del Plan Anual;
- la Evaluación U1 y la Integradora 2;
- una Clase que empieza a mitad de hoja (Clase 10);
- una Práctica que sube a la hoja anterior (Práctica 21).

No se vieron tablas ni figuras cortadas, ni títulos solos al pie.

Ocupación por hoja interior (texto e imágenes, sin encabezado ni pie):

| Documento | Mínimo | Máximo |
|---|---|---|
| Libro | 33 % | 99 % |
| Planes de Clase | 73 % | 94 % |
| Plan Anual | 85 % | 96 % |
| Solucionario | 40 % | 99 % |

## Cómo regenerar

Desde `algoritmica_2_esencial/build/`, ejecutar en este orden:

1. `python3 build_libro.py`
2. `python3 build_solucionario.py`
3. `python3 build_plan_anual.py`
4. `python3 build_planes.py`
5. `python3 build_muestra.py`
6. `PSEINT_DIR=<carpeta de PSeInt 20250314> python3 auditoria.py`

La salida va a `salida_v1_2/`; para otra carpeta, usar la variable `SALIDA`. Requisitos: python-docx, PyMuPDF y LibreOffice.

## Pendiente de comprobación manual

- **Word:** abrir los DOCX y confirmar que ningún plan pasa a dos hojas y que el Libro no deja hojas casi vacías. La medición se hizo con LibreOffice.
- **Access (versión del laboratorio):**
  - rótulos de la fila Total (Cuenta);
  - asistente de referencias cruzadas;
  - aviso de clave duplicada;
  - aceptación de SiInm([stock]<20;"reponer";"ok") con el separador regional.
- **Explorador de archivos y Bloc de notas:** opción para mostrar extensiones y archivo de solo lectura (Prácticas 15 y 17).
- **PSeInt en Windows:** los programas se ejecutaron en PSeInt 20250314 para Linux.

## Decisiones para Fer

- **Planificación compartida (hallazgo 07):** confirmar si el Plan Anual y los Planes de Clase se usan también con una edición Completa de Algorítmica 2.º.
- **Libro:** las ocho Clases o Prácticas que ahora empiezan a mitad de hoja (Clases 10, 14, 18 y 21; Prácticas 9, 11, 19 y 21) se pueden volver a hoja propia. Alternativa: quitar la sección de `sin_salto` en `build/ajustes_paginacion.json`. Eso vuelve a dejar una hoja casi vacía antes de esa sección.

**Estado final: listo para reauditoría independiente. No aprobado para la venta.**
