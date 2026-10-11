# 03_RESPUESTA_CLAUDE_SOFTWARE_2_ESENCIAL_v1

**Respuesta del constructor a 02_AUDITORIA_CHATGPT_SOFTWARE_2_ESENCIAL_v1** · Protocolo v0.4, §3, paso 5

Gabinete de Informática – Software · 2.º Curso BTI · Edición Esencial · versión corregida **v2** (11/10/2026)

**Estado: corregido — vuelve a ChatGPT para una nueva auditoría (paso 4).** No se declara listo para la venta.

## Resumen

**Resultado:** 10 de 10 hallazgos aplicados.
- **Críticos:** 2.
- **Mayores:** 5.
- **Menores:** 3.

**Ubicación:**
- Los archivos corregidos están en la rama `claude/libros-5z31jx`, carpeta `software_2_esencial/salida/`, con los mismos nombres de la v1.
- Las fuentes editables están en `software_2_esencial/src_md/`.

## 1. Hallazgos y qué se hizo

| N.º | Gravedad | Estado | Qué se hizo |
|---|---|---|---|
| 01 | CRÍTICO | Aplicado | Solucionario, Ficha E: mínimo 550 ÷ 0,80 = 687,5 GB; se acepta 688 GB o más. Se eliminó «aceptar 660 GB» y se explica por qué no cumple (110 ÷ 660 ≈ 16,7 % libre). |
| 02 | MAYOR | Aplicado | Clase 10, ejemplo «La impresora de la biblioteca»: los cálculos se hacen sin redondear el costo por página. Uso anual: A = G. 152.000 y B ≈ G. 803.077. Primer año: A = G. 1.252.000 y B ≈ G. 2.253.077. Se agrega el desembolso por envases enteros (A = G. 1.290.000 y B = G. 2.320.000) y se aclara que son dos medidas distintas. Ningún ítem del solucionario usaba los totales anteriores. |
| 03 | CRÍTICO | Aplicado | Práctica 20, Actividad 2: pasa a ser el «Informe técnico — Red de la Farmacia Tajy», con las Prácticas 14, 15, 16 y 19 y un plan de direcciones IP nuevo, propio de la farmacia. Se prohíbe pegar la configuración del equipo del laboratorio y se suman el resumen de riesgos y la conclusión. Se actualizaron la competencia, el desafío, el punto de control, el solucionario (con un plan de direcciones de ejemplo) y el Plan 33. |
| 04 | MAYOR | Aplicado | Práctica 19 con datos propios: un nuevo local de la Farmacia Tajy con tendidos de 9, 12, 17, 20, 25, 31, 43 y 55 m y el punto de prueba de 93 m. Solucionario: canales de 14, 17, 22, 25, 30, 36, 48 y 60 m, todos SÍ; prueba NO (93 m > 90 m de tendido fijo); margen mínimo 40 m. |
| 05 | MAYOR | Aplicado | Práctica 9: el tamaño del archivo se escribe una sola vez en H1; las fórmulas pasan a ser =REDONDEAR.MAS($H$1/B2;0) y =$H$1\*1000/D2/3600. El punto de control pide comprobar que al cambiar solo H1 se recalculan los tres formatos. Los resultados para 61 GB no cambian. |
| 06 | MAYOR | Aplicado con alcance mayor | Secuencias 18 y 36: en lugar de dos capacidades, se transcriben todas las de la etapa que la integradora evalúa. En la 18, las 9 de la Unidad 1; en la 36, las 7 de la Unidad 2, incluida la de abstracción, análisis y síntesis. Se ve en la Evaluación integradora de la 2.ª etapa: sus ítems cubren red, principios, equipos, medios, cableado y regulación, y el caso exige analizar y sintetizar. Se reproducen en los Planes 18 y 36. |
| 07 | MENOR | Aplicado | Práctica 12: el punto de control usa el texto propuesto (dirección observada, clasificación privada, pública, de enlace local o ausente; ante 169.254.x.x, registrar y consultar sin cambiar nada). Se agregó ese caso al solucionario. |
| 08 | MENOR | Aplicado | Clase 19, ítem 4 b): «Conviene usar y documentar un esquema uniforme; en cada enlace directo, los dos extremos se terminan igual». La letra correcta sigue siendo b. La clave del V/F 11 de la integradora 2 usa la misma formulación. |
| 09 | MENOR | Aplicado | Se documenta en NOTAS_PILOTO v2 (§4) la excepción autorizada por Fer con el texto propuesto: el .docx del libro pesa unos 27,6 MB, se distribuye por enlace, el PDF va por el canal habitual y no se alteran las imágenes originales. |
| 10 | MAYOR | Aplicado | La auditoría automática ahora incluye dos controles nuevos, descritos debajo de la tabla. |

Controles nuevos de la auditoría automática (hallazgo 10):
1. **Matriz trazable** (`build/verif_trazable.py` y `build/verificacion_trazable.md`): lee los datos del enunciado en las fuentes del libro, rehace la operación y busca el resultado en la clave. Cubre la Ficha E, las Prácticas 2, 4, 9, 10, 15, 16 y 19, la Clase 10 y los dos casos integradores.
2. **Prueba de reutilización de datos:** compara cada clase, actividad, práctica, ficha y evaluación, y da fallo si dos bloques comparten tres o más datos que no sean constantes técnicas.

Se deja expresamente asentado, como pide el auditor, que la auditoría automática es un control interno de integridad y no una verificación independiente. La correspondencia entre pregunta y letra de opción múltiple sigue a cargo del auditor; en la v1 ChatGPT la revisó sin encontrar discrepancias.

## 2. Verificación

Auditoría automática de la v2: **402 controles · 0 fallos**, incluidas las 23 filas de la matriz trazable. Ver `build/auditoria_resultado.txt` y `build/verificacion_trazable.md`.

Páginas de la v2: libro 104, solucionario 12, plan anual 9, planes de clase 38 (36 planes) y muestra 14. Todos los PDF están en oficio y los índices se verificaron contra el PDF.

## 3. Pedido al auditor

- Volver a auditar la v2, con revisión visual independiente de los cinco PDF: índice impreso, páginas vacías, tablas y tamaño de hoja. En la v1 no se pudo hacer.
- Si el entorno no abre los PDF desde GitHub, Fer los adjunta directamente.
