# Adenda al informe de cierre editorial — Colección ADS 3.º BTI v0.2

**Base:** commit `88c5cb5`, aprobado el 21 de octubre de 2026 como base editorial estable para la planificación docente.

Esta adenda corrige y aclara dos puntos del informe de cierre editorial. **No modifica ningún archivo de `coleccion/`:**
- los documentos aprobados, el informe y las evidencias de la v0.2 quedan tal como están, con sus huellas SHA-256;
- las cifras de esta adenda salen de `verificar_cierre_v0_2.py`, que solo lee esos archivos;
- el resultado está en `VERIFICACION_CIERRE_v0_2.json`.

Cuando una cifra de esta adenda no coincide con `INFORME_CIERRE_EDITORIAL.md`, vale la de esta adenda.

## 1. Instrumentos de la guía: 51 frente a 57

**Qué decía el informe.** «Los índices y los 51 instrumentos de la guía, en su página» (sección 3, Impresión). El informe de integración v0.1 usa la misma cifra.

**Qué dice el registro de controles.** `CONTROLES_IMPRESION.json`, control «4. Índice»: «los 57 instrumentos de la tabla «Instrumentos del año», cada uno en la página que indica».

**Qué se comprobó.** El control de impresión verificó **57 ubicaciones** en el PDF de la guía. Las 57 están en la página que indican.

| Grupo | Cantidad | Dónde se cita la página |
|---|---:|---|
| Instrumentos de evaluación de las seis partes: claves, listas de cotejo, rúbricas, planillas | 51 | Tabla «Instrumentos del año en esta guía» (parte general, sección 2) |
| Tablas de calendario de las seis partes, «Unidad … en 36 y en 28 encuentros» | 6 | Tabla «Secuencia ordinaria de 36 encuentros y adaptación alternativa a 28» (parte general, sección 1) |
| **Total comprobado por el control** | **57** | |

**Corrección.** Las dos cifras miden cosas distintas:
- 51 son las filas de la tabla «Instrumentos del año»;
- 57 son las ubicaciones que verificó el control: esas 51 más las 6 tablas de calendario.

El texto del control mezcla las dos al hablar de «57 instrumentos de la tabla». El renglón del informe queda así:

> Los índices, los 51 instrumentos de la tabla «Instrumentos del año» y las 6 tablas de calendario, cada uno en la página que indica (**57 ubicaciones comprobadas por el control de impresión, sin fallos**).

No cambia ningún resultado: los 57 controles de impresión siguen con 0 fallos. Que haya 57 controles y 57 ubicaciones es una coincidencia.

## 2. Archivos del manifiesto (160) y del ZIP de entrega (101)

| Concepto | Cantidad |
|---|---:|
| Archivos de `coleccion/` en `MANIFIESTO_COLECCION.json` (el manifiesto no se incluye a sí mismo) | 160 |
| … con el mismo SHA-256 que el archivo del repositorio en `88c5cb5` | 160 |
| Entradas del ZIP `ADS_3BTI_COLECCION_v0_2_CIERRE_EDITORIAL.zip` (las que lista `unzip -l`) | 101 |
| … carpetas (`evidencias/`, `revision_visual/`, `revision_visual/todas_las_paginas/`) | 3 |
| … archivos | 98 |
| Archivos del ZIP que están en el manifiesto, con el mismo SHA-256 | 97 |
| Archivo del ZIP que no está en el manifiesto: el propio `MANIFIESTO_COLECCION.json` | 1 |
| Archivos del manifiesto que no van en el ZIP | 63 |

**Qué son los 63 que no van en el ZIP.** Son todos de `coleccion/build/figs/`:
- 58 figuras PNG;
- 5 archivos `simbolos.json`, los datos de símbolos de los diagramas.

El armado los regenera con los scripts de cada lote, y la equivalencia comprueba que sus píxeles coincidan con los de los documentos aprobados. Son intermedios de construcción: las figuras ya están dentro de los DOCX y los PDF. Están en git, en el commit `88c5cb5`, y el manifiesto los registra para que la regeneración sea verificable.

| Carpeta | Archivos fuera del ZIP |
|---|---:|
| `build/figs/lote_1/figs` | 5 |
| `build/figs/lote_2` | 22 |
| `build/figs/lote_3` | 22 |
| `build/figs/lote_4` | 7 |
| `build/figs/lote_5` | 4 |
| `build/figs/lote_6` | 3 |

**Cuenta completa:** 97 en el ZIP + 63 intermedios = 160 del manifiesto. Además, el ZIP lleva el manifiesto y 3 carpetas: 97 + 1 + 3 = 101 entradas.

Todo lo que entra en el ZIP coincide byte por byte con el manifiesto. Para auditar la regeneración de las figuras se usa el repositorio, no el ZIP.

## 3. Otra observación encontrada al verificar

El campo `coleccion` de `MANIFIESTO_COLECCION.json` todavía dice «documentos anuales v0.1 (integración editorial, para auditoría)». El constructor del manifiesto no se actualizó en la v0.2.

Las huellas del manifiesto son las de la v0.2, porque coinciden con el commit `88c5cb5`. Solo el rótulo está desactualizado. No se corrige en el archivo, para no cambiar la v0.2 aprobada. Si se publica una v0.3, el rótulo se toma del constructor.

## 4. Conservación de la v0.2

- `git diff 88c5cb5 -- analisis_diseno_3_bti/coleccion analisis_diseno_3_bti/lote_*` está vacío en el commit de la planificación. El informe de planificación lo comprueba.
- La planificación se escribe en `analisis_diseno_3_bti/planificacion/`. Lee los documentos aprobados y no los regenera.
