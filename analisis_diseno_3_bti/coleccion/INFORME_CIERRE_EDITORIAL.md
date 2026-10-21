# Informe de cierre editorial — Colección ADS 3.º BTI, versión candidata v0.2

**Análisis y Diseño de Sistemas, 3.er curso BTI · Biblioteca Comercial 2026 · 21 de octubre de 2026**

**Base:** commit `43de4bcc5df7e8a114e1bfdf8aced71385fe26e2` (v0.1, integración editorial).

**Estado:** versión candidata para autorización.
- No está aprobada para la venta ni para uso en aula. No se declara apta para comercialización.
- No se subió nada a Google Drive.
- No se generaron el plan anual definitivo ni los 36 planes de clase.

## 1. Decisiones aplicadas

| Decisión aprobada | Cómo se cumple |
|---|---|
| Un único tomo anual | El libro sigue en un solo documento de 211 páginas (EVALUACION_ENCUADERNACION.md) |
| Oficio O3, márgenes espejados, paginación continua | Medidos en el DOCX y en cada página del PDF (INFORME_LEGIBILIDAD_IMPRESION.md, CONTROLES_IMPRESION.json) |
| Libro, guía y cuaderno separados | Tres documentos, con un índice cada uno |
| Sin modificar las fuentes de los seis lotes | Solo cambiaron los constructores de `coleccion/build/`; la coherencia comprueba los 855 archivos de los manifiestos de los lotes y git |
| Contenidos curriculares, prácticas, solucionarios, rúbricas y evaluaciones intactos | La equivalencia los compara bloque por bloque con los lotes: 0 fallos |

## 2. Correcciones C-01 a C-04

| Corrección | Qué se hizo | Dónde | Diferencia registrada |
|---|---|---|---|
| **C-01.** Presentación | «organizados en seis unidades de tres capítulos» → «organizados en seis unidades y 18 capítulos: tres capítulos en cada una de las Unidades I, II, III y V, cuatro en la Unidad IV y dos en la Unidad VI» | Libro, pág. 6 | D-18 (R-08) |
| **C-02.** Instrucciones de uso | Se agregó que los Capítulos 16 y 18 no tienen práctica (el 16 cierra la Unidad V con el H5; el 18 cierra el año con la demostración, la defensa individual y la evaluación integradora) y que el Capítulo 18 no tiene evaluación escrita. Las decisiones D-3 y D-4 no cambian | Libro, pág. 6 | D-19 y D-20 (R-09 y R-10) |
| **C-03.** Guía docente | La parte general aclara que hay 36 encuentros ordinarios (180 HC) y una adaptación alternativa a 28, que no reemplaza a la ordinaria. Una tabla reúne los encuentros de cada parte en las dos secuencias (6+6+6+8+6+4 = 36 y 5+4+5+5+5+4 = 28) y la página de cada tabla de calendario. Los calendarios reducidos de las partes no cambian | Guía, pág. 4 | D-22 |
| **C-04.** Rutas de código | Se unificó la celda «Archivo» de las 18 fichas del lote 4 (15 del libro, 3 de la guía) con la notación de los lotes 5 y 6: `referencia_docente/…` → `lote_4/proyecto/referencia_docente/…` (y lo mismo con `base_estudiante/…`) | Libro, Capítulos 10 a 13; guía, Referencias R-1 a R-3 | D-21 |

**Garantías de C-04:**
- El armado comprueba que cada ruta nueva exista y sea el mismo archivo real que la anterior.
- La coherencia comprueba que las 29 fichas impresas usen la misma notación y que cada ruta sea el archivo del que se lee su fragmento.
- No cambiaron:
  - el código;
  - las pruebas;
  - las instrucciones de ejecución, como `php pruebas/…`, que se dan desde la carpeta del proyecto;
  - las rutas que aparecen dentro del texto.

La lista cerrada pasa de 17 a **22 diferencias** (`DIFERENCIAS.md`). Los identificadores anteriores no cambiaron.

## 3. Auditoría

| Control | Resultado |
|---|---|
| Regeneración de los tres DOCX y sus PDF | Libro 211 págs., guía 109, cuaderno 33; ninguna tabla perdió filas |
| Equivalencia con los seis lotes (25 segmentos del libro, 6 partes de la guía, 16 prácticas) | 0 fallos; solo las 22 diferencias autorizadas, con su cantidad exacta |
| Impresión de las 353 páginas (57 controles) | 0 fallos |
| Coherencia (45 controles) | 0 fallos |
| Fuentes de sustitución (9 combinaciones) | 0 fallos |
| Pruebas negativas de las herramientas del lote 6, en el entorno aislado | 10 de 10 |
| Inspección estática de los paquetes | Modelo: 0 incoherencias. Mbokaja: las 5 esperadas (defectos de la Práctica 17) |
| Revisión visual de las 353 páginas (31 hojas de contacto) | Sin defectos (REVISION_VISUAL.md) |

**Impresión** (detalle en CONTROLES_IMPRESION.json):
- Filas de las 513 tablas impresas, tablas repartidas con su encabezado y sin filas sueltas.
- Párrafos y palabras enteras.
- Las 29 figuras con su epígrafe.
- Los 29 bloques de código enteros y dentro de los márgenes.
- Los índices y los 51 instrumentos de la guía, en su página.
- Paginación continua y márgenes espejados en cada página.
- Ninguna hoja en blanco.
- Ningún título solo al pie.
- Los 908 renglones de respuesta impresos y ninguno separado de su consigna.
- Capítulos, prácticas, unidades y partes al comienzo de su página.
- Las 6 rúbricas de los hitos y las 17 tablas de claves completas.
- Ningún texto por debajo de 7,5 pt.

**Coherencia:**
- Los lotes, sin cambios.
- Las referencias cruzadas correctas: 229 citas del libro, 211 de la guía y 9 del cuaderno.
- Las claves de los 153 ítems.
- Las 39 rutas de archivos citadas existen.
- C-01 a C-04 aplicados.
- Ninguna capacidad presentada como oficial del MEC.
- Los pendientes declarados.
- DR y V6, ausentes: se comprobó con las rutas privadas.

**Fuentes de sustitución.** No hubo hojas en blanco, renglones sueltos ni evaluaciones fuera de su página. El libro tiene:
- 211 págs. con Carlito;
- 213 con Liberation Sans;
- 236 con DejaVu Sans.

**Seguridad.** Las herramientas del lote 6 v1.1 no se modificaron.
- Las pruebas negativas corrieron solo en el entorno aislado autorizado: espacio de red aislado y cuenta sin privilegios.
- No se ejecutó ningún código de los paquetes fuera de ese entorno.

Las salidas de cada control están en `evidencias/`.

## 4. Legibilidad e impresión (INFORME_LEGIBILIDAD_IMPRESION.md)

**Formato medido:**
- Página de 215,9 × 330,2 mm en los tres PDF.
- Interior 2,5 cm, exterior 1,8 cm, superior e inferior 1,5 cm, con márgenes espejados declarados en los tres DOCX.
- Carlito y Liberation Mono incrustadas en el PDF.

**Tamaño de letra.** Ningún tamaño es menor que en los lotes aprobados: no se redujo la letra para resolver la distribución.

**Doble faz:**

| Documento | Hojas | Páginas que faltan para completar el pliego de 4 · 8 · 16 |
|---|---|---|
| Libro | 106 | 1 · 5 · 13 |
| Guía | 55 | 3 · 3 · 3 |
| Cuaderno | 17 | 3 · 7 · 15 |

- Las páginas en blanco que haga falta agregar van todas al final, nunca intercaladas.
- A la imprenta se le entrega el PDF.

**Observaciones de legibilidad, para decidir con la prueba impresa** (no se cambiaron: son parte del formato aprobado):
1. **Renglón largo.** Unos 112 caracteres por renglón de texto corrido, cuando lo cómodo suele estar por debajo de 90.
2. **Renglones de respuesta juntos.** Están a 5,2 mm uno de otro, con dos renglones por consigna. Para escribir a mano suele recomendarse de 7 a 8 mm.
3. **Código en 7,5 pt.** Hay que confirmar su lectura y el contraste del fondo en papel.
4. **Páginas con mucho blanco al pie.** Hay 12 con menos del 12 % ocupado, antes de una práctica, evaluación, capítulo o parte que empieza en hoja nueva por diseño. No son hojas en blanco.

## 5. Limitaciones de la auditoría

- Es una auditoría en pantalla, sobre los PDF de LibreOffice, con Carlito en lugar de Calibri. No hubo prueba en papel ni en la máquina de la imprenta.
- Los DOCX no se abrieron en Microsoft Word ni en Windows. La paginación con Calibri se espera igual a la de Carlito, que tiene las mismas medidas, pero no se comprobó.
- Si el DOCX se abre en un equipo sin Calibri ni Carlito, la paginación cambia: el índice y la página que cita la guía hay que regenerarlos desde los constructores.

## 6. Pendientes

- Pruebas del prototipo y de las herramientas en Windows y en los laboratorios escolares.
- Instalación y restauración en el laboratorio.
- Concurrencia real.
- Instalación por otro equipo, que hace el curso.
- Revisión jurídica del borrador de licencia de la Unidad VI.
- Prueba impresa completa del libro antes del tiraje (punto 7 de las instrucciones para la imprenta).
- Plan anual definitivo y 36 planes de clase: no se elaboran hasta tu autorización.

## 7. Entregables

| Entregable | Archivo |
|---|---|
| Libro anual del estudiante | `ADS_3BTI_LIBRO_ANUAL_ESTUDIANTE_OFICIO_O3.docx` y `.pdf` |
| Guía docente anual | `ADS_3BTI_GUIA_DOCENTE_ANUAL_OFICIO_O3.docx` y `.pdf` |
| Cuaderno anual de prácticas | `ADS_3BTI_CUADERNO_ANUAL_PRACTICAS_OFICIO_O3.docx` y `.pdf` |
| Informe de cierre editorial | `INFORME_CIERRE_EDITORIAL.md` (este archivo) |
| Registro de diferencias aprobadas | `DIFERENCIAS.md` |
| Informe de legibilidad e impresión | `INFORME_LEGIBILIDAD_IMPRESION.md` y `LEGIBILIDAD_IMPRESION.json` |
| Revisión visual | `REVISION_VISUAL.md`, `revision_visual/` (22 láminas) y `revision_visual/todas_las_paginas/` (31 hojas de contacto) |
| Evidencias de las pruebas | `EQUIVALENCIA.json`, `CONTROLES_IMPRESION.json`, `COHERENCIA.json`, `PRUEBA_FUENTES.json`, `resultado_construccion.json` y `evidencias/` |
| Inventario y encuadernación | `INVENTARIO.md` y `EVALUACION_ENCUADERNACION.md` |
| Manifiesto SHA-256 | `MANIFIESTO_COLECCION.json` |

`INFORME_INTEGRACION.md` queda como registro de la v0.1.

Me detengo acá, a la espera de tu autorización.
