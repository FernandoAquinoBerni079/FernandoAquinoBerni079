# 03_RESPUESTA_CLAUDE_ALGORITMICA_3_ESENCIAL_FINAL_OFICIO_v2

**Respuesta del constructor a 02_AUDITORIA_CHATGPT_ALGORITMICA_3_ESENCIAL_FINAL_OFICIO** (Informe 03 del compendio, 11/10/2026) · Protocolo v0.4, §3, paso 5

Algorítmica · 3.er Curso BTI · Edición Esencial Comercial 2026 · versión corregida **FINAL OFICIO v2** (12/10/2026)

**Estado: corregido — vuelve a ChatGPT para reauditar.** No se declara aprobado para la venta: esa decisión es solo de Fer.

## Resumen

Se atendieron los **9 hallazgos** del informe (3 CRÍTICOS, 5 MAYORES y 1 MENOR).

**Ubicación:**
- Rama `claude/libros-5z31jx`, carpeta `algoritmica_3_esencial/salida_FINAL_OFICIO_v2/`: 4 DOCX y 5 PDF.
- La carpeta `salida_FINAL_OFICIO/` queda intacta como base de comparación.

**Fuente única:** los .docx de `salida_FINAL_OFICIO/`.
- El Libro y el Solucionario se corrigieron sobre esos mismos archivos con `build/final_oficio/correcciones_v2.py`. Cada reemplazo exige encontrar su texto exactamente una vez; si no lo encuentra, el script se detiene.
- Planes y Plan Anual se regeneraron con `build_planes_fo_v2.py` y `build_plan_anual_fo_v2.py`.
- La Muestra se regeneró con `build_muestra_fo_v2.py`.

## 1. Hallazgos y qué se hizo

| N.º | Gravedad | Qué se hizo |
|---|---|---|
| 01 | CRÍTICO | **Libro:** la frase oficial «Reconoce la importancia de la práctica Conductual en el desarrollo de las actividades.» se agregó **en dos lugares**: <br>• **Presentación (pág. 2):** «Capacidad transversal del programa MEC: …» seguida de la frase de desarrollo que propuso el auditor. <br>• **Proyecto Final (pág. 116):** nuevo apartado «Capacidad transversal del programa», con su evidencia en el proyecto (procedimientos, roles, resguardo de datos, control cruzado y registro de cambios). <br>**Solucionario:** se suma una orientación docente para observar esa capacidad con evidencias concretas. Es una apreciación cualitativa y **no cambia los pesos de la rúbrica**. <br>La frase es idéntica, letra por letra, en Libro, Plan Anual, Planes y Solucionario. |
| 02 | CRÍTICO | **Evaluación de la Unidad 4, ítem 7:** se reemplazó por el texto exacto propuesto («En una jornada distinta…»). <br>Clave nueva: Panificados 3 × 4.000 + 2 × 7.000 = **26.000**; Salados 4 × 8.000 + 2 × 16.000 = **64.000**; Bebidas 3 × 4.500 + 2 × 8.500 = **30.500**; total **G. 120.500**. <br>Ninguno de esos resultados aparece en el libro del estudiante. |
| 03 | CRÍTICO | **Integradora de la 2.ª etapa, ítem 8:** se reemplazó por el texto exacto propuesto (ventas F1 a F5 de un nuevo local). <br>Clave nueva: Rosa 17.000 + 39.000 = **56.000**; Luis **22.000**; Ana **18.000**; Miguel **57.000**; total **G. 153.000**; promedio **G. 30.600**. <br>Los Planes y el Plan Anual no citaban estas cifras, así que no hubo que tocarlos. |
| 04 | MAYOR | **Planes de Clase: de 51 a 38 páginas** (portada, «Cómo se usa» con índice y 36 planes, **uno por hoja**). Criterios, observaciones y las dos firmas quedan en la misma hoja de cada plan. **No queda ninguna «continuación».** <br>El ajuste se hizo **solo en los 13 planes que desbordaban**: <br>• Primero se redujo el espaciado entre filas y párrafos. <br>• Si no alcanzaba, la letra pasó de 9,5 a 9 pt: así quedaron los Planes 1, 26, 28 y 31. Los otros nueve (2, 7, 9, 15, 17, 18, 30, 32 y 36) entraron solo con menos espaciado. <br>• Ningún plan baja de 9 pt. <br>El texto es idéntico al de FINAL OFICIO; solo cambian los números del índice, verificado contra el PDF. |
| 05 | MAYOR | **Libro (Clase 18, pág. 93) y Solucionario (pág. 2):** se reemplazó la mención a «Office 2016 … Click-to-Run» por el texto propuesto. Dice que Office 2016 está fuera de soporte desde el 14/10/2025, recomienda Access incluido en Microsoft 365 o Access 2024 con licencia y soporte vigentes, y aclara que el docente verifica las rutas en su instalación. <br>En los dos documentos ya no queda ninguna mención a «Click-to-Run». |
| 06 | MAYOR | **Muestra (15 págs.):** el Plan N.º 1 ocupa **una sola página íntegra** (pág. 15). <br>La hoja liberada se usa para la **primera página de la Clase 18** (pág. 9: ficha, Access y la nueva nota de versión). <br>No hay continuaciones ni claves del docente. |
| 07 | MAYOR | Plan Anual y Planes llevan nombres **sin edición**: <br>• `Algoritmica_3er_Curso_PLAN_ANUAL_COMERCIAL_2026_FINAL_OFICIO_v2` <br>• `Algoritmica_3er_Curso_PLANES_DE_CLASE_COMERCIAL_2026_FINAL_OFICIO_v2` <br>El sufijo `_v2` distingue esta entrega de la anterior; Fer puede quitarlo al aprobar. <br>Tampoco dicen «Esencial» ni en el texto ni en las propiedades del archivo. El **contenido del Plan Anual no cambió** (0 diferencias). <br>**Pendiente de Fer:** confirmar que esta misma planificación es la que acompaña a la Edición Completa. Desde este paquete no se puede comprobar. |
| 08 | MAYOR | **Práctica 3:** se adoptó la corrección principal del auditor. <br>• Importes nuevos: 15.000 · 21.000 · 27.000 · 24.000 · 18.000 · 39.000. <br>• La semana pasa a ser **del 16 al 18 de marzo**. La del 9 al 11 es la segunda semana de Access de las Prácticas 18 a 21; dejarla habría puesto dos recaudaciones distintas en la misma semana. <br>• Clave: traza 15.000 → 36.000 → 63.000 → 87.000 → 105.000 → 144.000; total **G. 144.000**; promedio **G. 24.000**; desafío: **4 ventas** mayores a G. 20.000. El error de inicializar dentro del ciclo ahora muestra 39000. <br>• **Ejecutado en PSeInt 20250314, perfil Flexible**, con los tres programas de `pseint_v2/`: imprime «Total: 144000», «Promedio: 24000», «Mayores a 20000: 4» y, con la inicialización dentro del ciclo, «39000». <br>• La Práctica 3 no tiene captura de pantalla de PSeInt, así que no hubo imagen que rehacer. <br>• La Práctica 21 y la base de Access no se tocaron. |
| 09 | MENOR | **Págs. 33 y 102** (cierre de las Clases 6 y 19): se probó primero compactar el espaciado, que no alcanzó (quedaban al 16 % y 14 %). Se descartó. <br>En su lugar, se integró al final de cada clase una **«Autoevaluación antes de la Práctica N»**: <br>• Tabla «Puedo… / Sí / Todavía no» con los **tres indicadores literales de la ficha** de la clase, leídos del propio libro. <br>• No repite ejercicios ni da respuestas. <br>• La práctica siguiente sigue empezando en hoja propia. <br>**Métrica:** altura del contenido más bajo, sin contar el pie, dividida por el alto de la hoja. Con esa métrica, el Libro **no tiene ninguna página por debajo del 25 %**: las 33 y 102 quedan alrededor del 35 %, y las 27 y 49, en 26 %. Si Fer prefiere otro cierre para esas dos clases, se registra como excepción consciente. |

## 2. Controles (`build/verificacion_v2.txt`)

`build/final_oficio/verificar_v2.py` lee los nueve entregables y rehace las cuentas a partir de los enunciados. Resultado: **81 controles, 0 fallos.**

| Control | Resultado |
|---|---|
| Frase Conductual literal en Libro, Plan Anual, Planes y Solucionario (docx y pdf) | Presente en los cuatro; 2 veces en el Libro |
| Ítems U4-7 e Integradora-8 recalculados desde el enunciado | Coinciden con la clave y con la propuesta del auditor; sus resultados no figuran en el libro |
| Práctica 3 recalculada desde el modelo | Traza, total, promedio, desafío y error frecuente coinciden; los importes difieren de los de la Práctica 21 |
| Planes | 36 planes en 38 páginas · 0 continuaciones · firmas en la hoja de cada plan · 0 diferencias de texto · índice verificado |
| Plan Anual | 6 páginas · 0 diferencias de texto con FINAL OFICIO |
| Índices | Libro 54/54 · Solucionario 53/53 |
| Páginas | Libro 117 · Solucionario 18 · Planes 38 · Plan Anual 6 · Muestra 15 (total 194) |
| Papel y márgenes | Oficio 612 × 936 pt en todas las páginas (apaisado en el Plan Anual y en su hoja de la muestra) · márgenes de 1,27 cm en los 4 DOCX |
| ✓ ✗ ✅ ✔ en los 5 PDF | 0 |
| Libro: páginas por debajo del 25 % | 0 |
| Diferencias de texto con FINAL OFICIO | Libro 29 líneas · Solucionario 11 líneas. Revisadas una por una: todas son de esta corrección |

Revisión ocular, sobre los PDF renderizados:
- **Libro:** págs. 2, 33, 102, 113 y 116.
- **Planes:** Plan 1 a mayor tamaño y hoja de contacto de las 38 páginas.
- **Muestra:** completa.

No se vieron tablas cortadas, superposiciones ni firmas fuera de hoja.

## 3. Notas técnicas

- **Plantilla de Planes y Plan Anual.** `maqueta.py` apunta a `src/…TOMO_COMPLETO.docx`, que no está en el repositorio. Se reemplazó por los .docx FINAL OFICIO de cada pieza, vaciados (`build/plantilla_*_fo.docx`). Antes de usarla se validó: reconstruidos sin ajustes, los Planes dan el mismo texto y las mismas 51 páginas, con los mismos 13 desbordes que señaló el auditor.
- **Fuentes del generador anterior.** `build/practicas.py` y `build/evaluaciones.py` se actualizaron con los mismos textos nuevos, para que no conserven los datos reemplazados.
- **Auditoría vieja.** `auditoria.py`, de la v2.2, depende de `src/` y no se corrió. La verificación de esta ronda es `verificar_v2.py`.

## 4. Pendiente

- Reauditoría de ChatGPT sobre `salida_FINAL_OFICIO_v2/`.
- Decisión de Fer sobre el 07: que la misma planificación acompañe a la Edición Completa.
- **Aprobación para la venta: solo Fer.** Este paquete **no** está aprobado para la venta.
