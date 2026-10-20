# Análisis y Diseño de Sistemas, 3.º BTI — Inventario de la colección y entrega del lote 1 para auditoría

**Biblioteca Comercial 2026 · Plan Optativo · 20 de octubre de 2026**

**Base revisada:** rama `claude/libros-5z31jx`, commit `cdc96a6334d11577c19e6e89621d926d63ada618`, carpeta `analisis_diseno_3_bti/` completa (221 archivos), y búsqueda en Drive.

**Alcance de este documento:**
- Solo inventaría. No se modificó ningún archivo existente, no se construyó nada nuevo y no se subió nada a Drive.
- No declara aptitud comercial: la aprobación es de Fernando.

## 1. Paquete para la auditoría independiente del lote 1

**Archivo:** `ADS_3BTI_LOTE1_AUDITORIA_cdc96a6.zip`. Se entregó en el chat, no en el repositorio.

| Dato | Valor |
|---|---|
| Tamaño | 1 212 402 bytes |
| SHA-256 | `a299ebeb569a861b6eabb5c09ccdc4ab318449bc0fa066ee53d45de69ef808dd` |

Los seis archivos se extrajeron con `git cat-file blob` desde el commit `cdc96a6`, sin pasar por el árbol de trabajo. Conservan sus nombres y sus bytes. Se comprobó, además, que al descomprimir el ZIP cada archivo tiene el mismo SHA-256.

| Archivo | Bytes | SHA-256 | Contra `MANIFIESTO_LOTE_1.json` |
|---|---:|---|---|
| `ADS_3BTI_LOTE1_ESTUDIANTE.docx` | 468 587 | `333e9baa…cd245f8e7` | Coincide (hash y bytes) |
| `ADS_3BTI_LOTE1_ESTUDIANTE.pdf` | 1 179 252 | `4b41eeae…52864aa8` | Coincide (hash y bytes) |
| `ADS_3BTI_LOTE1_GUIA_DOCENTE.docx` | 60 546 | `8c8741d0…a6bff1e` | Coincide (hash y bytes) |
| `ADS_3BTI_LOTE1_GUIA_DOCENTE.pdf` | 398 083 | `2aa15064…7f9ac0` | Coincide (hash y bytes) |
| `INFORME_LOTE_1.md` | 15 339 | `c891d59e5647deb26b8ed1e2dd3876e223519e0ceeb95f0d1862c3f75c4f06ed` | No figura en el manifiesto |
| `MANIFIESTO_LOTE_1.json` | 9 583 | `5483b03659695a158c48b0fd6efcdeeb01973780f08b4f8fa623810e77ca8536` | No puede figurar en sí mismo |

Las cuatro huellas de los documentos coinciden también con la tabla del §10 de `INFORME_LOTE_1.md`.

El informe y el manifiesto no tienen una huella previa con la cual cotejarlos. Su garantía es que son los objetos de git del commit `cdc96a6`, y que la punta actual de la rama no los modificó.

### 1.1 Observación para la auditoría: formato de página

Los dos PDF del lote 1 están en **A4 (21,0 × 29,7 cm)**, no en oficio:

| PDF | Páginas | Tamaño |
|---|---:|---|
| Libro | 56 | 21,0 × 29,7 cm |
| Guía | 19 | 21,0 × 29,7 cm |

También el Capítulo 4 v2 está en A4 (16 págs.). El informe del lote no menciona el papel. La maqueta (`helpers.py` y `maqueta.py`, idénticos a los del Capítulo 4 v2.1) fija la página en 21,0 × 29,7 cm, con márgenes de 2,2 cm a los lados y 2,0 cm arriba y abajo, y tablas de 16,6 cm.

Si la colección debe ir en oficio, hay que decidirlo **antes del lote 2**. El cambio afecta la paginación de todo el lote 1 y el índice estático. No se cambió nada.

### 1.2 Puntos que la auditoría puede revisar

Sin orden de prioridad:
- adecuación pedagógica;
- correspondencia con el informe de Work v0.1 (índice §6, encuentros §5.2, capacidades §4.2 y caso §7);
- progresión de los contenidos;
- teoría, ejemplos resueltos y prácticas en tres niveles;
- evaluaciones de 15 puntos y sus claves;
- figuras, tablas y diagramas;
- márgenes, paginación y formato (ver §1.1);
- coherencia entre el libro y la guía docente.

**El informe de Work no está en el repositorio ni en Drive** (se buscó por título y por texto). Solo se conoce su SHA-256: `3d4f5ab9daf3329f0dd34b13bc30b7001cb8e65780262c536346dbbea065069a`. Quien audite la correspondencia con Work necesita ese PDF.

## 2. Inventario de la colección

| Componente | Estado | Qué existe | Qué falta |
|---|---|---|---|
| **Plan anual** | **Falta** | Solo la **distribución de las 180 HC** (`fase2_pilotos/C_informe_esfuerzo/v2/` y `v2_1/`): <ul><li>36 encuentros y su adaptación a 28;</li><li>foco de Work, capacidades C1 a C10 e hitos H1 a H6 por encuentro;</li><li>HC por categoría.</li></ul> | El plan anual propiamente dicho, que la distribución no es: <ul><li>capacidades, temas e indicadores por capítulo;</li><li>procedimientos e instrumentos de evaluación;</li><li>etapas del año y calendario;</li><li>formato canónico.</li></ul> |
| **Planes de clase** | **Falta (0 de 36)** | **Secuencias por encuentro en HC**, no planes de clase: <ul><li>en la guía del lote 1, para los encuentros 1 a 6;</li><li>en la guía del Capítulo 4, para los encuentros 7 y 8;</li></ul> cada una con tramos y actividades. Son insumo para 8 planes. | Los 36 planes de clase individuales en formato de plan (datos, capacidad e indicadores, inicio, desarrollo y cierre, evaluación con instrumento). Ninguno está hecho. |
| **Libro del estudiante** | **Parcial (4 de 18 capítulos, ninguno aprobado)** | <ul><li>**Preliminares y Capítulos 1 a 3** (lote 1): 56 págs. A4, candidato a auditoría.</li><li>**Capítulo 4 v2:** 16 págs. A4. Es un piloto separado, con portada propia; falta aplicarle la especificación C3 e integrarlo.</li><li>**Históricos reemplazados**, que no son parte del libro: Capítulo 2 candidato v1.1 (absorbido por el lote 1) y piloto v1 del Capítulo 4.</li></ul> | <ul><li>Capítulos 5 a 18. La estructura de 18 capítulos y seis unidades se cita en los pilotos; hay que confirmarla con el §6 de Work.</li><li>Las aperturas de las Unidades II a VI.</li><li>El libro unificado: hoy hay dos documentos separados.</li></ul> |
| **Guía docente y solucionario** | **Parcial** | <ul><li>**Guía del lote 1** (19 págs.). Incluye las claves de las 32 actividades, de las 3 prácticas y de las 3 evaluaciones, además de la rúbrica del H1 con su planilla. Hace también de solucionario.</li><li>**Guía del Capítulo 4 v2.1**, con la sección 3 de requisitos y criterios.</li></ul> | <ul><li>La guía de los Capítulos 4 a 18.</li><li>Un **solucionario separado**, si la colección comercial lo exige como entregable propio: hoy las claves van dentro de la guía, por decisión de los lotes.</li></ul> |
| **Cuadernos de prácticas** | **Falta como documento propio** | <ul><li>Prácticas 1 a 4 dentro del libro, en tres niveles. Las de los Capítulos 1 a 3 usan el caso Mbokaja.</li><li>Prototipo técnico PHP + SQLite v2.3, con sus pruebas. Es material del docente y del entorno, no un cuaderno del estudiante.</li></ul> | <ul><li>Decidir si las prácticas de la Unidad IV (construcción, encuentros 19 a 26) van en un cuaderno aparte o dentro del libro.</li><li>Pruebas de campo en Windows y en equipos escolares (`PRUEBAS_PENDIENTES_CAMPO.md`).</li></ul> |
| **Evaluaciones** | **Parcial** | <ul><li>Diagnóstico de entrada sin nota (preliminares).</li><li>Evaluaciones opcionales de 15 puntos de los Capítulos 1 a 4, en página propia y con claves.</li><li>Rúbrica del H1: 5 criterios × 4 niveles, 60/40 rotulado como propuesta editorial.</li></ul> | <ul><li>Instrumentos de los hitos H2 a H6, incluida la evaluación intermedia del H3 (encuentro 18).</li><li>Defensa individual (encuentro 35) y recuperación (encuentro 36).</li><li>Evaluaciones de los Capítulos 5 a 18.</li></ul> |
| **Versiones DOCX y PDF** | **Existen para lo hecho** | Cada libro y cada guía tiene su DOCX y su PDF de control (renderizado con Carlito): lote 1, Capítulo 4 v2, guía del Capítulo 4 v2.1 y los dos históricos. | Las de todo lo que falta. |
| **Paquetes de entrega** | **Falta** | Solo el ZIP de auditoría del §1, entregado en el chat. Nada en Drive. | <ul><li>Paquete comercial: libro, guía y solucionario, plan anual, planes de clase y cuaderno, si corresponde.</li><li>Inventario y planilla de la Biblioteca 2026.</li></ul> |

### 2.1 Lo que no hay que confundir

- **La distribución de las 180 HC no es un plan anual.** Reparte el tiempo de los 36 encuentros por categoría (análisis, diseño, programación, verificación, documentación, gestión y evaluación). No trae indicadores, procedimientos ni instrumentos.
- **La guía docente no son los 36 planes de clase.** Trae secuencias de los encuentros 1 a 8, con tramos en HC, más las claves y los instrumentos. No tiene el formato de plan de clase, y faltan 28 encuentros.

### 2.2 Insumos que faltan o no están verificados

| Insumo | Situación |
|---|---|
| Informe de Work v0.1 | No está en el repositorio ni en Drive. Solo se conoce su SHA-256. Se necesita para los títulos y secciones de los Capítulos 5 y 6 (§6), y para auditar la correspondencia. |
| Diseño curricular (mayo de 2026, p. 29) | La afirmación de que permite el programa institucional del Plan Optativo se toma del informe de Work. No se verificó por separado. |
| Identidad «verde BTI» | Provisional. No se cotejó el color contra el catálogo. |
| Constitución, art. 140 | Se usa en paráfrasis. No se cotejó contra una edición oficial. |
| Formato de página (oficio o A4) | Decisión pendiente (§1.1). |

## 3. Qué hay que producir, por orden de dependencia

1. **Ahora:** la auditoría independiente del lote 1 y la aprobación de Fernando, con la decisión sobre el formato de página.
2. **Lote 2:** Unidad II, con el Capítulo 4 integrado más la especificación C3, y los Capítulos 5 y 6. Preparación en `../lote_2_plan/PREPARACION_LOTE_2_UNIDAD_II.md`.
3. **Lotes 3 a 6:** Unidades III a VI, Capítulos 7 a 18.
4. **Plan anual**, a partir de las fichas de los capítulos aprobados. Puede adelantarse con la distribución de 180 HC y las capacidades de Work si se acepta que lo que falte quede como pendiente.
5. **36 planes de clase**, a partir del plan anual. Los 8 primeros pueden partir de las secuencias existentes.
6. **Solucionario separado y cuaderno de prácticas**, si se deciden.
7. **Paquete comercial** y actualización del inventario de la Biblioteca 2026.
