# 04 · RESPUESTA DE CLAUDE A LA REAUDITORÍA DE LA v1.3 — Algorítmica 1.er Curso BTI · Esencial Comercial 2026

**Reauditoría respondida:** reauditoría independiente de la v1.3 (rama `claude/wizardly-newton-lzhifa`). Veredicto: **CORRECCIONES REQUERIDAS**, una sola obligatoria: restaurar la hoja propia de las 21 prácticas (y la de las 5 evaluaciones) y auditar sin la excepción `or nP in UNL['cp']`.
**Versión entregada:** **v1.3.1**, en `algoritmica_1_esencial/salida_v1_3_1/`. `salida/` (v1.2) y `salida_v1_3/` (v1.3) no se tocaron.
**Estado:** corregido y verificado. **No se declara aprobado para la venta**: solo Fer puede hacerlo, después de la inspección visual y la comparación de hashes que propone la reauditoría.

## Respuesta a cada observación

| Observación | Respuesta | Qué se hizo | Estado |
|---|---|---|---|
| H03 · Prácticas sin hoja propia (`"cp": [2, 3, 4, 5, 7, 11, 12, 15, 21]`) | Aceptada | **Se eliminó el mecanismo de uniones** (`uniones_libro.json` y el código que quitaba saltos). Las 21 prácticas vuelven a abrir página. También las 21 clases, que la v1.3 había unido a la práctica anterior en 9 casos (`"pc"`): el control original lo exigía igual («abre página o sigue a la apertura de unidad»). Las 5 evaluaciones siguen abriendo página. | CORREGIDO |
| H03 · Páginas casi vacías sin quitar saltos | Aceptada | El contenido se redistribuye **dentro de su propia sección**. Cuando la última hoja de una clase o una práctica quedaba casi vacía, se pasa a esa hoja un bloque completo de la hoja anterior de la misma sección. En 10 clases ese bloque es «Actividades de aplicación»; en las Prácticas 8, 17 y 21 es la «Actividad 2», y en la 14, la «Actividad 3». El corte arrastra el título y los párrafos que deben ir juntos, así que no quedan títulos huérfanos. Las evaluaciones mantienen lo de la v1.3: la integradora 1 tiene renglones de 0,58 cm; la U3 y la integradora 2 llevan la Parte B en hoja propia. Libro: **107 páginas** (v1.2: 108; v1.3: 97). **0 hojas bajo el 25 %**; la más baja mide 27 %. | CORREGIDO |
| Control automático modificado para aceptar la excepción | Aceptada | Los controles de salto vuelven a su forma original, **sin excepción**: «Práctica N abre página» (21/21), «Evaluación abre página» (5/5) y «Clase N abre página (o sigue a la apertura de unidad)» (21/21). Se suma un control que exige que el build **no tenga** mecanismo de unión. Otro verifica que cada corte quede dentro de su sección y no reemplace un salto obligatorio. | CORREGIDO |
| Control «3 renglones por consigna» que solo comprobaba `len(e['ab']) > 0` | Aceptada | El control ahora **cuenta en el PDF** las líneas grises de ancho útil en las hojas de cada evaluación y exige exactamente 3 por consigna de la Parte B: U1 15/15, U2 15/15, E1 18/18, U3 18/18, E2 21/21. También exige que la altura del renglón no baje de 0,58 cm. | CORREGIDO |
| H01, H02, H04, H05 | Sin reabrir | Sin cambios de contenido; se regeneraron en la salida nueva para que el paquete sea uno solo. | PASA (reauditoría) |
| H06, H07 | Cerrados por Fer | 37 encuentros; Figura 21.1 opcional. | CERRADO |

## Verificación (v1.3.1)

**820 controles · 0 fallos** (`build/auditoria_resultado.txt`). La lista completa de controles está en `build/auditoria_detalle.txt`.

| Verificación | Resultado |
|---|---|
| Prácticas que abren página | **21/21**, sin excepción |
| Evaluaciones que abren página | **5/5** |
| Clases que abren página (o siguen a la apertura de unidad) | **21/21**, sin excepción |
| Mecanismo de unión en el build | ninguno |
| Páginas bajo el 25 % | **0** en Libro (mín. 27 %), Solucionario (31 %), Planes (89 %), Plan Anual (28 %) y Muestra (36 %) |
| Renglones de respuesta en el PDF | 3 por consigna en las 5 evaluaciones (87 renglones) |
| 15/15 capacidades MEC | Libro, Planes y Plan Anual |
| Hojas de Planes con solo firmas | 0; los 37 planes en una hoja cada uno |
| Índices exactos | Libro 52/52, Solucionario 52/52, Planes 37/37 |
| DOCX ↔ PDF | todo párrafo de los 4 DOCX está en su PDF; páginas = índice |
| PSeInt 20250314 | 35 casos, 0 fallos |

Páginas v1.3.1: Libro 107 · Solucionario 19 · Plan Anual 8 · Planes 39 · Muestra 14.

## Pendiente antes del OK comercial de Fer

1. Inspección visual independiente del PDF final. Conviene mirar especialmente las 37 hojas de Planes, las evaluaciones y las hojas donde quedaron los 14 cortes, que se listan en `build/ajustes_libro.json`.
2. Comparación de hashes cuando la versión aprobada pase de `claude/wizardly-newton-lzhifa` a su ubicación definitiva.
3. **NO se declara APROBADO PARA VENTA.**
