# Lote 1 en oficio O3 — versión candidata editorial

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · 20 de octubre de 2026**

**Estado:** candidata editorial para auditoría independiente. **No es un libro aprobado para comercialización.** La aprobación es de Fernando.

**Decisiones aplicadas (Fernando, 20 de octubre de 2026):**
- **Perfil O3** como estándar de maquetación de la asignatura:
  - oficio de 21,59 × 33,02 cm;
  - interior de 2,5 cm, exterior de 1,8 cm, superior e inferior de 1,5 cm;
  - márgenes espejados para impresión a doble cara.
- **El PDF A4 del lote 1 queda como histórico:** no se usa como versión comercial ni para imprimir, por el defecto bloqueante de su Tabla 3.5. No se regenera.
- **Sin cambios de contenido:** se corrigen solo maquetación y controles.

**Lo que no se tocó** (se comprobó con el SHA-256 de sus archivos):
- `lote_1/`: maestros A4, commit `cdc96a6`;
- `lote_1_oficio/`: pruebas O1, O2 y O3, commit `18bb2ba`.

## 1. Archivos de la candidata

| Archivo | Páginas |
|---|---:|
| `ADS_3BTI_LOTE1_ESTUDIANTE_OFICIO_O3_CANDIDATA.docx` y `.pdf` | 49 |
| `ADS_3BTI_LOTE1_GUIA_DOCENTE_OFICIO_O3_CANDIDATA.docx` y `.pdf` | 14 |

**Reconstrucción:**

```
python3 lote_1_oficio_candidata/build/construir_candidata.py
python3 lote_1_oficio_candidata/build/verificar_candidata.py
python3 lote_1_oficio_candidata/build/controles_finales.py
```

El constructor importa las fuentes de `lote_1/build/` sin modificarlas. Parte del constructor de la prueba (`lote_1_oficio/build/construir_oficio.py`), que se copió y no se modificó.

## 2. Correcciones respecto de la prueba O3

| N.º | Pedido | Corrección | Evidencia |
|---:|---|---|---|
| 1 | Control de impresión que compruebe las filas de las tablas, sin depender de encontrar fragmentos de texto en cualquier página | **Control nuevo** `build/controles_impresion.py` → `filas_de_tablas`. Cada fila de cada tabla de 2 o más columnas del DOCX se busca **en orden** entre las filas que el detector de tablas de PyMuPDF reconoce en el PDF, página por página. Se registran las filas impresas, las páginas y los encabezados repetidos. Además, entra en el ciclo de construcción: si una tabla queda incompleta, su rótulo abre hoja nueva y se reconstruye. | Libro: 38 tablas y 252 filas, todas impresas. Guía: 36 tablas y 226 filas, todas impresas. El mismo control, aplicado al A4 original, encuentra la Tabla 3.5 con **2 de 8 filas**. |
| 2 | Verificar la Tabla 3.5 y todas las tablas repartidas entre páginas | Control específico de la Tabla 3.5 y detalle de cada tabla que ocupa más de una página | **Tabla 3.5:** 8 de 8 filas, en la pág. 41. **Repartidas en el libro (3):** Tablas 1.6, 2.1 y 3.2. **En la guía (5):** claves de los Encuentros 1 y 5, listas de cotejo de las Prácticas 1 y 3, y niveles de desempeño. Todas completas y con el encabezado repetido en la página siguiente. |
| 3 | Corregir las palabras partidas en columnas estrechas | **Ajuste de anchos por palabra:** ninguna palabra de una celda queda más ancha que su columna. Se mide con la métrica de Carlito (la de Calibri), al tamaño y peso reales del texto, más 0,44 cm de márgenes de celda. El ancho que falta se toma de la columna con más holgura y **el ancho total de la tabla no cambia**. Control nuevo: `palabras_partidas`. | **3 columnas ensanchadas:**<ul><li>libro, tabla «Fragmento», columna 1: de 1,67 a 1,86 cm;</li><li>guía, tabla de resultados del diagnóstico por estudiante, columna 2: de 2,08 a 2,27 cm («Programación»);</li><li>la misma tabla, columna 5: de 2,29 a 2,30 cm («Comunicación»).</li></ul>Palabras partidas: 0 en el libro y 0 en la guía. En la prueba O3 había 1 y 1. |
| 4 | Confirmar a la vista el índice, los diagramas, las evaluaciones y los márgenes espejados | Láminas en `revision_visual/`, revisadas una por una, más los controles automáticos 3 a 5 | Ver §4 |
| 5 | Mantener los controles de correspondencia pedagógica y trazabilidad | Se ejecuta el verificador del lote 1 completo (bloques A a J) con las sustituciones de geometría y ruta ya declaradas para la prueba | **118 correctos, 0 fallos** |
| 6 | Versión candidata en archivos nuevos, con informe y SHA-256 | Carpeta `lote_1_oficio_candidata/` y `MANIFIESTO_CANDIDATA_O3.json` | §5 |

## 3. Resultados de los controles

### 3.1 Verificador del lote 1

`verificar_candidata.py` da **118 correctos y 0 fallos**. El detalle está en `verificacion_resultado.txt` y `.json`. Comprueba:
- **A.** Índice de Work.
- **B.** Rótulo de las capacidades.
- **C.** Trazabilidad de las fuentes contra el caso, incluido el control contra el Capítulo 4.
- **D.** Integración del Capítulo 2.
- **E.** Sin duplicar Algorítmica 3.º.
- **F.** Voseo y residuos.
- **G.** Maqueta del DOCX: filas «no dividir», tablas al ancho útil (17,29 cm), encabezados repetidos, y `helpers.py` y `maqueta.py` idénticos a los del Capítulo 4 v2.1.
- **H.** Maqueta del PDF: sin páginas en blanco, prácticas y evaluaciones en página propia, índice estable y extensión.
- **I.** Evaluaciones e instrumentos.
- **J.** Numeración.

### 3.2 Controles finales

`controles_finales.py` da **23 controles y 0 fallos**. El detalle está en `CONTROLES_FINALES.txt` y `.json`.

| Control | Resultado |
|---|---|
| 1. Texto idéntico | Libro (1721 párrafos con texto) y guía (721), iguales al A4 original y a la prueba O3, salvo los números del índice y la línea de versión |
| 2. Filas de tablas | Todas las filas de todas las tablas impresas, en libro y guía |
| 2. Tablas repartidas | 3 en el libro y 5 en la guía, completas y con el encabezado repetido |
| 2. Tabla 3.5 | 8 de 8 filas, pág. 41 |
| 2. Párrafos impresos | Ningún párrafo del DOCX falta en el PDF |
| 2. Palabras enteras | Ninguna palabra de celda partida |
| 3. Figuras | 5 figuras con las mismas dimensiones que las del lote 1, cada una con su epígrafe en la misma página: 1.1 (pág. 12), 1.2 (14), 2.1 (25), 2.2 (29) y 3.1 (40) |
| 4. Índice | 37 entradas, cada una en la página que indica |
| 5. Márgenes espejados | **Impares** (págs. 11, 13, 15): interior de 2,5 cm a la izquierda. **Pares** (págs. 10, 12, 14, 16): interior a la derecha. Medidos sobre el texto en las págs. 10 a 17. |

## 4. Revisión visual

Láminas en `revision_visual/`, revisadas una por una:

| Lámina | Qué se confirmó |
|---|---|
| `01_indice.png` | Índice de una página, con niveles, puntos guía y números alineados al margen |
| `02_diagramas.png` | Las 5 figuras completas, legibles y con su epígrafe |
| `03_evaluaciones.png` | Las 3 evaluaciones en página propia (págs. 20, 35 y 48), con banda, datos, texto base, ítems y renglones |
| `04_tabla_3_5.png` | Tabla 3.5 con sus 8 filas, seguida del recuadro de reglas y de la Tabla 3.6 |
| `05_margenes_espejados_pags_10_11.png` | Páginas enfrentadas con el margen ancho del lado del lomo |
| `06_tablas_repartidas_libro.png` y `07_tablas_repartidas_guia.png` | Cada tabla repartida continúa en la página siguiente con su encabezado |

## 5. Archivos y huellas

`MANIFIESTO_CANDIDATA_O3.json` trae el SHA-256 y el tamaño de cada archivo de esta carpeta, y los de los cuatro originales A4 (histórico) como referencia.

| Archivo | Contenido |
|---|---|
| `build/` | `construir_candidata.py`, `perfiles.py`, `controles_impresion.py`, `verificar_candidata.py`, `controles_finales.py` y las figuras regeneradas |
| Raíz | Los cuatro archivos de la candidata, `resultado_construccion.json` (con las columnas ensanchadas y las tablas en hoja nueva: ninguna), `verificacion_resultado.*`, `CONTROLES_FINALES.*`, `revision_visual/`, este informe y el manifiesto |

## 6. Limitaciones

- **Tipografía.** El PDF de control se renderiza con Carlito, que tiene las métricas de Calibri, como en todo el lote. En Word la paginación puede variar levemente.
- **Detección de tablas.** El control de filas usa el detector de tablas de PyMuPDF, que se apoya en los bordes. Todas las tablas de 2 o más columnas del lote tienen bordes y fueron detectadas. Los recuadros de una sola columna se controlan con el control de párrafos.
- **Impresión.** Los márgenes espejados suponen impresión a doble cara.
- **Otros pendientes del lote 1.** Siguen los del `INFORME_LOTE_1.md` (§9): no se agregó contenido nuevo.
