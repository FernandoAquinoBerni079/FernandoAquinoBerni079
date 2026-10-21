# Lista cerrada de diferencias con los seis lotes

**Colección ADS 3.º BTI · documentos anuales v0.1 de la colección (integración editorial, para auditoría) · oficio O3**

Estas son **todas** las diferencias admitidas entre los documentos anuales y los documentos aprobados de los lotes. La equivalencia (`build/equivalencia.py`) compara cada capítulo, cada parte de la guía y cada práctica, bloque por bloque: el texto, el estilo y el formato de cada párrafo, cada celda de cada tabla, los anchos de columna, el sombreado y los píxeles de cada imagen. Cualquier diferencia que no esté en esta lista es un fallo.

Resultado de la equivalencia: **0 fallos**, en 25 segmentos del libro, 6 partes de la guía y 16 prácticas.

| Id. | Documento | Categoría | Qué cambia | Dónde | Cómo se controla |
|---|---|---|---|---|---|
| D-01 | Los tres | Portada | Una sola portada por documento, con la versión de la colección y su estado, en lugar de las portadas de los lotes. | Primera página | Las portadas de los lotes no se comparan. |
| D-02 | Los tres | Índice | Un índice general con las páginas del documento anual, en lugar de los índices de cada lote (la guía y el cuaderno de los lotes no tenían índice). El índice sigue el orden real de los títulos: en el del lote 1, la sección 3.3 figuraba bajo el Encuentro 6, aunque en el texto está en el Encuentro 5. En el cuaderno, los títulos de unidad agrupan las prácticas y llevan la página de su primera práctica. | Después de la portada | Los índices no se comparan; el control de impresión comprueba cada entrada en su página y el orden creciente. |
| D-03 | Los tres | Paginación | Paginación continua; las tablas que empiezan en hoja nueva para no perder filas se recalculan sobre el documento anual; el encadenado de tablas largas de los lotes 3 a 6 se aplica también a las Unidades I y II. | Todo el documento | Solo cambian saltos de página y «conservar con el siguiente»: el texto, los estilos y los anchos de las tablas se comparan igual. |
| D-04 | Libro | Apertura de unidad | Las seis aperturas de unidad, cada una de su lote, en un solo libro. | Antes del primer capítulo de cada unidad | Se comparan con la de su lote; solo admiten R-05. |
| D-05 | Libro | Remisión (alcance) | R-01: «Esta edición de control contiene los preliminares y la Unidad I (Capítulos 1 a 3, Encuentros 1 a 6).» → «Este tomo anual contiene los preliminares y las seis unidades (Capítulos 1 a 18, Encuentros 1 a 36).» (1 aparición). | Preliminares (Presentación y alcance) | Alcance del documento: el libro del lote 1 contenía solo la Unidad I. |
| D-06 | Libro | Referencia editorial | R-02: «(lote 3 v1.1)» → «(diseño de la Unidad III, v1.1)» (1 aparición). | Capítulo 11 (ficha de un bloque de código) | Referencia editorial: la versión del diseño se nombra por su unidad. |
| D-07 | Libro | Referencia editorial | R-03: «prototipo del lote 4» → «prototipo de la Unidad IV» (3 apariciones). | Capítulo 14 (rótulo de la Tabla 14.6) y Capítulo 16 (dos párrafos) | Referencia editorial: el prototipo se nombra por la unidad que lo construye. |
| D-08 | Libro | Referencia editorial | R-04: «la del lote 4 queda como estaba» → «la de la Unidad IV queda como estaba» (1 aparición). | Capítulo 16 | Referencia editorial. |
| D-09 | Libro | Referencia editorial | R-05: «la del lote anterior no cambian» → «la de la Unidad IV no cambian» (1 aparición). | Apertura de la Unidad V (caja «Las copias descartables») | Referencia editorial: «lote anterior» no tiene sentido en el tomo anual. |
| D-10 | Libro | Referencia editorial | R-06: «Referencia docente del lote 4;» → «Referencia docente de la Unidad IV;» (1 aparición). | Capítulo 14 (tabla de resultados) | Referencia editorial. |
| D-11 | Libro | Referencia editorial | R-07: «la referencia del lote 4 (falla)» → «la referencia de la Unidad IV (falla)» (1 aparición). | Capítulo 14 (tabla de resultados) | Referencia editorial. |
| D-12 | Guía | Referencia editorial | Parte general nueva: organización, versión de cada parte, dónde está cada instrumento, seguridad del código recibido, datos reservados y pendientes. | Después del índice | Texto nuevo de coleccion/build/guia_general.py; no se compara con ningún lote. |
| D-13 | Guía | Referencia editorial | El título «Guía docente — Lote N» de cada guía pasa a ser el título de su parte («Parte N — …»), en hoja nueva. | Primer título de cada parte | Se admite solo ese título. |
| D-14 | Guía | Referencia editorial | Nota de integración de la Parte V: preparación del Encuentro 30 y conjunto reservado (observaciones de la auditoría del lote 5, previstas en la estrategia de cierre). | Después del título de la Parte V | Se admite solo esa caja. |
| D-15 | Guía | Referencia editorial | Nota de integración de la Parte VI: las pruebas de código recibido requieren una máquina virtual o un equipo aislado, y la lista cerrada no vuelve confiable el código. | Después del título de la Parte VI | Se admite solo esa caja. |
| D-16 | Guía | Remisión | La página del diagnóstico de entrada en el libro («libro, pág. N») es la del libro anual. | Parte I, sección 1 | Se admite solo el número. |
| D-17 | Cuaderno | Referencia editorial | Las Prácticas 1 a 3, que estaban solo en el libro del lote 1, se agregan al cuaderno con la misma función de práctica de los lotes 2 a 6; el estado de la portada resume lo que decían las portadas de los cuadernos de los lotes. | Prácticas 1 a 3 y portada | Cada práctica se compara con la del libro anual y con la versión aprobada de su lote. |

## Apariciones de los reemplazos del libro (D-05 a D-11)

| Reemplazo | Apariciones esperadas | Apariciones en el armado |
|---|---|---|
| R-01 | 1 | 1 |
| R-02 | 1 | 1 |
| R-03 | 3 | 3 |
| R-04 | 1 | 1 |
| R-05 | 1 | 1 |
| R-06 | 1 | 1 |
| R-07 | 1 | 1 |

## Qué no cambió

- Ningún texto de teoría, ejemplo, práctica, consigna, evaluación, puntaje, indicador ni solución.
- Ninguna figura: se generaron otra vez con los scripts de cada lote y sus píxeles coinciden con los de los documentos aprobados.
- Ningún bloque de código: se leen de los archivos del proyecto, igual que en los lotes.
- Las menciones a «lote» de la guía docente se conservan: remiten a las carpetas del repositorio (la parte general de la guía lo explica). Las del libro del estudiante que eran referencias editoriales son D-05 a D-11; las demás nombran un lote de libros donados (Práctica 11) o los lotes del plan lector (caso Arapoty) y no son referencias editoriales.
- Las rutas de archivos del prototipo (por ejemplo, lote_5/proyecto/…) se conservan: los archivos siguen en esas carpetas y el verificador de coherencia comprueba que existan.
