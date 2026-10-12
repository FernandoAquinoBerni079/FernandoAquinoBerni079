# 03 · RESPUESTA DE CLAUDE A LA AUDITORÍA DE ChatGPT — Algorítmica 1.er Curso BTI · Esencial Comercial 2026

**Informe respondido:** Informe 01 del `COMPENDIO_AUDITORIAS_ALGORITMICA_1_2_3_ESENCIAL_2026` (auditoría del 11/10/2026 sobre la **v1.2 oficio**; 7 hallazgos: 1 CRÍTICO, 3 MAYORES, 3 MENORES).
**Versión entregada:** **v1.3**, en `algoritmica_1_esencial/salida_v1_3/` (las salidas anteriores quedan intactas en `salida/`).
**Decisiones de Fer (12/10/2026):** se mantienen **37 encuentros (148 HC)** (H06); la **Figura 21.1 queda como mejora opcional** (H07).
**Estado:** corregido y verificado con la auditoría automática. **No se declara aprobado para la venta**: esa decisión es solo de Fer, previa reauditoría independiente de ChatGPT.

## Matriz de conciliación

| N.º | Gravedad | Respuesta | Qué se hizo | Estado |
|---|---|---|---|---|
| 01 | CRÍTICO | Aceptado | Las 3 capacidades transversales MEC se transcriben **literalmente** en el Libro y en los Planes, con el encabezado «Capacidad transversal MEC». **Libro:** (a) caja en la apertura de cada unidad, con la capacidad, su indicador de logro y dónde se trabaja; (b) en la Práctica 5 (U1), la 9 (U2) y la 20 (U3), caja con la capacidad, un **paso 4 evaluable** (ficha de equipo / ficha de fuentes / nota del equipo) y su ampliación del punto de control. **Planes:** una fila «Capacidad transversal MEC» (capacidad + indicador), una actividad en Desarrollo y un criterio, en los planes N.º 8 (Unidad 1), 15 (Unidad 2) y 34 (Unidad 3). **Solucionario:** clave de cada indicador en la Práctica 5, 9 y 20. Las 12 capacidades cognitivas no se tocan. Resultado: **15/15 en Libro, Planes y Plan Anual** (verificado sobre los tres PDF). | CORREGIDO |
| 02 | MAYOR | Aceptado | Se recompusieron los planes 8, 15, 35 y 36 (más el 34, que pasó a desbordar al sumar H01). Cada plan ocupa **una sola hoja** con criterios, observaciones y firmas «Docente / Dirección — Visto bueno». Solo se ajustó espaciado y bordes de tabla (texto nunca por debajo de 9 pt) y, en los planes 8 y 15, los puntos de control se remiten a la Práctica del libro en vez de citarse completos. No se quitó ninguna capacidad ni indicador. Planes: 43 → **39 páginas**; 0 hojas con solo firmas; índice 37/37 verificado. | CORREGIDO |
| 03 | MAYOR | Aceptado | Se reajustaron los saltos: la Práctica N sigue a su Clase (en 9 casos) o la Clase N+1 sigue a la Práctica N (en 9 casos) cuando la hoja anterior quedaba casi vacía; en la Práctica 12 y la 21 se pone un salto antes de la Actividad 2 para repartir mejor las hojas; en las evaluaciones, los renglones de la integradora 1 se compactan y las de la Unidad 3 y la integradora 2 llevan la **Parte B en hoja propia** (espacio de respuesta completo: 3 renglones por consigna, sin recortar). Cuadros, figuras y tipografía no se comprimen. Libro: 108 → **97 páginas**; **0 páginas bajo el 25 %** (la más baja mide 28 %); sin hojas en blanco. Las 17 hojas señaladas por el auditor desaparecen o quedan integradas a hojas con contenido. | CORREGIDO — ver «Decisión para Fer» sobre prácticas |
| 04 | MAYOR | Aceptado | Integradora de la 2.ª etapa, Parte A n.º 3: «una venta de **G. 86.000** se cobra: a) 86.000; b) 94.600; c) 77.400». Solucionario: **3. c) 77.400** (86.000 − 8.600). Se verificó que 86.000, 8.600 y 77.400 no aparecen en la Clase 17. Se conservan los otros ítems. | CORREGIDO — ver nota sobre la letra |
| 05 | MENOR | Aceptado | Archivos renombrados a `Algoritmica_1er_Curso_PLAN_ANUAL_COMERCIAL_2026` y `Algoritmica_1er_Curso_PLANES_DE_CLASE_COMERCIAL_2026` (.docx y .pdf), sin «ESENCIAL» en el nombre ni en los metadatos. La planificación es una sola para las ediciones Esencial y Completa. Libro y Solucionario conservan «ESENCIAL_COMERCIAL». No se movieron ni renombraron los maestros. | CORREGIDO |
| 06 | MENOR | Decidido por Fer | **Se mantienen 37 encuentros (148 HC).** Sin cambios en Plan Anual, Planes, portadas ni carga horaria. | CERRADO por decisión de Fer |
| 07 | MENOR | Decidido por Fer | La Figura 21.1 **queda como está**; el rediseño es una mejora opcional pendiente de la decisión de Fer. | NO APLICADO (opcional) |

## Notas sobre dos decisiones de implementación (para que ChatGPT las contraste)

- **H04, letra de la clave.** El informe propone «3. a) G.77.400». Se usó **c)** porque la integradora de la 2.ª etapa ya tenía la clave distribuida b–a–c y la v1.1 pidió que las opciones correctas no quedaran todas en la misma posición. El importe y el resultado son los que propone el informe.
- **H01, dónde se trabaja.** Se eligió la transferencia entre pares de las Prácticas 5, 9 y 20 porque ya es un trabajo en equipo evaluable (30 a 40 minutos) dentro de cada unidad; así la actividad evaluable no agrega páginas ni encuentros. Si ChatGPT prefiere otra ubicación, es un cambio en `ediciones.TRANSV`.

## Verificaciones pedidas

| Verificación | Resultado |
|---|---|
| 15/15 capacidades MEC textuales | **15/15** en Libro, Planes y Plan Anual (búsqueda literal normalizada sobre los PDF) |
| Hojas que solo tengan firmas | **0** (Planes: 39 páginas, cada plan en una hoja con su «Visto bueno») |
| Páginas por debajo del 25 % | **0** en Libro (mín. 28 %), Solucionario, Planes, Plan Anual y Muestra |
| Índices exactos | Libro 52/52, Solucionario 52/52, Planes 37/37: el número impreso en el índice coincide con la página real del PDF |
| DOCX ↔ PDF sincronizados | Todo párrafo de los 4 DOCX figura en su PDF; el PDF es posterior al DOCX; el total de páginas de cada PDF coincide con su índice |
| Claves de las 5 evaluaciones | 15/15 correspondencias letra ↔ opción impresa, con el cambio de H04 |
| Ejecución en PSeInt | PSeInt 20250314 (Linux, perfil Flexible): los 35 casos de las prácticas y del Puente pasan, 0 fallos |
| Auditoría automática | **796 controles · 0 fallos** (`build/auditoria_resultado.txt`) |

Páginas v1.3: Libro 97 · Solucionario 19 · Plan Anual 8 · Planes 39 · Muestra 14.

## Qué queda para ChatGPT y para Fer

1. Reauditoría independiente de la v1.3 (hashes, 15/15, páginas reales y claves), como pide el informe.
2. Fer conserva en exclusiva la **aprobación comercial**: **NO se declara APROBADO PARA VENTA.**
3. Decisión pendiente de Fer: si acepta que algunas Prácticas ya no abren en hoja propia (ver notas v1.3).
4. Mejora opcional: Figura 21.1 (H07).
