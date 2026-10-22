# Bitácora R1 → R2 · Informática 2.º BTC

Generada automáticamente desde `registro_r2_2btc.json`. Cada fila es un cambio aplicado por el constructor sobre la copia R1 (solo lectura); «Apariciones» es la cantidad verificada: si el texto de origen no aparecía exactamente esas veces, la construcción se detenía.

| N.º | Documento | Antes (R1) | Después (R2) | Apariciones | Motivo / hallazgo |
|---|---|---|---|---|---|
| 1 | Tomo | Revisión de contenido octubre de 2026. | Revisión R2, 22 de octubre de 2026. | 1 | Identificación de la versión |
| 2 | Tomo | Si escribís B4*12 la planilla lo toma como texto; si escribís =B4*12 lo calcula. | Si escribís C2*12 la planilla lo toma como texto; si escribís =C2*12 lo calcula. | 1 | H-2-01: la columna C guarda el honorario (A=Cliente, B=Régimen); B4 contenía una etiqueta de régimen |
| 3 | Tomo | =B4*12 | =C2*12 | 2 | H-2-01: la columna C guarda el honorario (A=Cliente, B=Régimen); B4 contenía una etiqueta de régimen |
| 4 | Tomo | =B4/2 | =C2/2 | 1 | H-2-01: la columna C guarda el honorario (A=Cliente, B=Régimen); B4 contenía una etiqueta de régimen |
| 5 | Tomo | honorario anual | honorario anual del cliente de la fila 2 | 1 | H-2-01: la columna C guarda el honorario (A=Cliente, B=Régimen); B4 contenía una etiqueta de régimen |
| 6 | Tomo | honorario quincenal | mitad del honorario mensual | 1 | H-2-01: la columna C guarda el honorario (A=Cliente, B=Régimen); B4 contenía una etiqueta de régimen |
| 7 | Tomo | a) B4*12 | a) C2*12 | 1 | H-2-01: la columna C guarda el honorario (A=Cliente, B=Régimen); B4 contenía una etiqueta de régimen |
| 8 | Tomo | b) fórmula B4*12 | b) fórmula C2*12 | 1 | H-2-01: la columna C guarda el honorario (A=Cliente, B=Régimen); B4 contenía una etiqueta de régimen |
| 9 | Tomo | c) 12*B4= | c) 12*C2= | 1 | H-2-01: la columna C guarda el honorario (A=Cliente, B=Régimen); B4 contenía una etiqueta de régimen |
| 10 | Tomo | b) B2-B17 | b) C2-C17 | 1 | H-2-19: los distractores usaban la columna B; ahora solo cambia el separador, que es lo que se evalúa |
| 11 | Tomo | c) B2..B17 | c) C2..C17 | 1 | H-2-19: los distractores usaban la columna B; ahora solo cambia el separador, que es lo que se evalúa |
| 12 | Tomo | d) B2;B17 | d) C2;C17 | 1 | H-2-19: los distractores usaban la columna B; ahora solo cambia el separador, que es lo que se evalúa |
| 13 | Tomo | =C2+C3+…+B17 | =C2+C3+…+C17 | 2 | H-2-02: el rango de honorarios termina en C17 |
| 14 | Tomo | G. 3.044.000 es el salario mínimo vigente. | G. 3.044.000 es el salario mínimo mensual vigente desde el 1 de julio de 2026 (Decreto 6225/2026). | 1 | H-2-12: fecha y norma del dato que más rápido cambia |
| 15 | Tomo | Usa HOY() y cálculos entre fechas en documentos del estudio. | Usa HOY(), AHORA() y cálculos entre fechas y horas en documentos del estudio. | 1 | H-2-13: indicador sincronizado con plan anual y planes de clase |
| 16 | Tomo | Párrafo «Descomponer un trazado…» con estilo Título 3, antes del texto | Párrafo normal con entrada en negrita, después de «Un rectángulo convertido a curvas…» | 1 | H-2-14: un párrafo largo aparecía como título en la navegación |
| 17 | Tomo | PDF para imprenta para la imprenta | PDF preparado para la imprenta | 1 | H-2-15: redundancia y consigna demasiado absoluta (la conversión a curvas depende de la imprenta) |
| 18 | Tomo | PDF para imprenta (imprenta) | PDF para imprenta | 2 | H-2-15: redundancia y consigna demasiado absoluta (la conversión a curvas depende de la imprenta) |
| 19 | Tomo | 2.2 Para la imprenta se exporta en PDF con las tipografías convertidas a __________. | 2.2 Si la imprenta lo solicita, las tipografías del PDF se convierten a __________. | 1 | H-2-15: redundancia y consigna demasiado absoluta (la conversión a curvas depende de la imprenta) |
| 20 | Tomo | 2.1 Para la imprenta se exporta un PDF con las tipografías convertidas a __________. | 2.1 Si la imprenta lo solicita, las tipografías del PDF se convierten a __________. | 1 | H-2-15: redundancia y consigna demasiado absoluta (la conversión a curvas depende de la imprenta) |
| 21 | Tomo | que unificó tributos internos y aduanas; el Ministerio de Hacienda pasó a llamarse Ministerio de Economía y Finanzas (MEF). | que unificó tributos internos y aduanas. Por su parte, la Ley 7158/2023 creó el Ministerio de Economía y Finanzas (MEF), que absorbió al Ministerio de Hacienda. | 1 | H-2-08: el MEF fue creado por la Ley 7158/2023, no por la ley de la DNIT |
| 22 | Tomo | 2.3 El ex Ministerio de Hacienda hoy se llama __________. | 2.3 Las funciones del ex Ministerio de Hacienda las ejerce hoy el __________. | 1 | H-2-08: el MEF fue creado por la Ley 7158/2023, no por la ley de la DNIT |
| 23 | Tomo | recién ahí tiene efecto fiscal. El receptor recibe el KuDE, la representación gráfica con código QR que permite verificar el documento en el portal. El KuDE no es la factura: es su imagen verificable. | recién ahí tiene efecto fiscal. En e-Kuatia el envío es diferido: el emisor firma el DE y debe transmitirlo al SIFEN dentro del plazo que fija la normativa técnica (hasta 72 horas desde la firma, según la DNIT). La entrega depende del receptor: si también es … | 1 | H-2-04: la entrega depende del receptor (XML al electrónico; KuDE al no electrónico o consumidor final); envío diferido |
| 24 | Tomo | útil para entregar y verificar, pero no reemplaza al documento electrónico. | que se entrega al receptor no electrónico o al consumidor final y sirve para verificar, pero no reemplaza al documento electrónico. | 1 | H-2-04: la entrega depende del receptor (XML al electrónico; KuDE al no electrónico o consumidor final); envío diferido |
| 25 | Tomo | Figura 13. El recorrido de una factura electrónica: de DE a DTE y KuDE. | Figura 13. Recorrido simplificado de una factura electrónica: del DE al DTE y su entrega según el receptor. | 1 | H-2-04: la entrega depende del receptor (XML al electrónico; KuDE al no electrónico o consumidor final); envío diferido |
| 26 | Tomo | Figura 5. Cuatro tipos de gráfico, cuatro historias con los mismos datos del estudio. | Figura 5. Cuatro tipos de gráfico, cada uno para una pregunta distinta, con datos del estudio (millones de guaraníes). | 1 | H-2-06: figura reconstruida con los datos reales del caso |
| 27 | Tomo | Salto de página manual en párrafo propio antes de cada evaluación | Salto de página anterior en ese párrafo | 9 | H-2-21: evita páginas en blanco cuando la clase termina justo al pie |
| 28 | Tomo | Preguntas abiertas sin espacio para responder | 180 renglones (3 por pregunta en clases y evaluaciones de unidad, 4 en las de etapa) | 180 | H-2-20: el estudiante trabaja sobre el tomo; las abiertas llevan renglones |
| 29 | Laboratorio | Revisión de contenido octubre de 2026. | Revisión R2, 22 de octubre de 2026. | 1 | Identificación de la versión |
| 30 | Laboratorio | las Prácticas 1, 4, 9, 11, 15 y 20 se integran | las Prácticas 1, 4, 9, 11, 15 y 19 se integran | 1 | H-2-05: la Práctica 20 pasa a encuentro propio y la 19 se integra a su clase |
| 31 | Laboratorio | 5. Activá el filtro automático sobre la fila 1. | 5. Seleccioná A1:C17, sin la fila 18 del total, y activá el filtro automático: así la fila del total no queda dentro del filtro. | 1 | H-2-09: con la fila 18 contigua, el autofiltro la incluye y la oculta al filtrar |
| 32 | Laboratorio | ▸ Exportación: PDF para imprenta para imprenta · PNG para redes | ▸ Exportación: PDF para imprenta · PNG para redes | 1 | H-2-15 |
| 33 | Laboratorio | ▸ DE → validación del SIFEN → DTE → KuDE con QR | ▸ DE → validación del SIFEN → DTE → entrega: XML al receptor electrónico o KuDE con QR al no electrónico | 1 | H-2-04: entrega según el receptor |
| 34 | Laboratorio | 5. Rotulá cada caja con su nombre técnico: DE, validación SIFEN, DTE y KuDE. | 5. Rotulá cada caja con su nombre técnico: DE, validación SIFEN, DTE y entrega (XML o KuDE, según el receptor). | 1 | H-2-04: entrega según el receptor |
| 35 | Laboratorio | Figuras a 12 cm y tres renglones de anotaciones en todas las prácticas | Práctica 10: figura a 8 cm; Práctica 14: 9,5 cm; un renglón de anotaciones en ambas | 2 | Las figuras R2 (3:2) son más altas: se conserva una práctica por página |
| 36 | Laboratorio | Imágenes 9 y 10 de una versión anterior (la 10 con =SI(B2>=…)) | Figuras R2 9 y 10, iguales a las del tomo | 2 | H-2-03: la figura de la Práctica 16 contradecía la estructura (C = honorario) |
| 37 | Plan_anual | Revisión de contenido octubre de 2026. | Revisión R2, 22 de octubre de 2026. | 1 | Identificación de la versión |
| 38 | Plan_anual | (Prácticas 1, 4, 9, 11, 15 y 20) | (Prácticas 1, 4, 9, 11, 15 y 19) | 1 | H-2-05 |
| 39 | Plan_anual | Las tasas de Sueldos se guardan en G1 y G2. | Las tasas de Sueldos se guardan en G1 y G2. El programa de referencia nombra la página web de la SET; desde 2024 esas funciones corresponden a la DNIT (Ley 7143/2023). | 1 | H-2-16: aclarar la actualización institucional sin atribuirla al MEC |
| 40 | Plan_anual | UNIDAD 1 · La planilla electrónica del estudio | Banda de unidad con la capacidad del programa | 1 | H-2-07: el plan anual no mostraba las capacidades |
| 41 | Plan_anual | UNIDAD 2 · Fórmulas, referencias y configuración de hojas | Banda de unidad con la capacidad del programa | 1 | H-2-07: el plan anual no mostraba las capacidades |
| 42 | Plan_anual | UNIDAD 3 · Informes financieros con datos estadísticos y gráficos | Banda de unidad con la capacidad del programa | 1 | H-2-07: el plan anual no mostraba las capacidades |
| 43 | Plan_anual | UNIDAD 4 · Editor de imágenes vectoriales y plan promocional | Banda de unidad con la capacidad del programa | 1 | H-2-07: el plan anual no mostraba las capacidades |
| 44 | Plan_anual | UNIDAD 5 · Planilla avanzada administrativo-contable | Banda de unidad con la capacidad del programa | 1 | H-2-07: el plan anual no mostraba las capacidades |
| 45 | Plan_anual | UNIDAD 6 · El portal tributario de la DNIT | Banda de unidad con la capacidad del programa | 1 | H-2-07: el plan anual no mostraba las capacidades |
| 46 | Plan_anual | Fila 19 | Tiempo y procedimiento redistribuidos | 1 | H-2-05: la Clase 20, la Práctica 20 y la evaluación de la Unidad 6 no caben en 80 min |
| 47 | Plan_anual | Fila 20 | Tiempo y procedimiento redistribuidos | 1 | H-2-05: la Clase 20, la Práctica 20 y la evaluación de la Unidad 6 no caben en 80 min |
| 48 | Solucionario | Revisión de contenido octubre de 2026. | Revisión R2, 22 de octubre de 2026. | 1 | Identificación de la versión |
| 49 | Solucionario | 1.1 d) =B4*12 | 1.1 d) =C2*12 | 1 | H-2-01 |
| 50 | Solucionario | 1.1 b) una esquina con la proporción bloqueada | 1.1 b) una esquina | 1 | Clave igual al texto de la opción impresa |
| 51 | Solucionario | 4) el receptor recibe el KuDE con QR para verificarlo. | 4) se entrega al receptor: el XML si es facturador electrónico, o el KuDE con QR si no lo es o si es consumidor final. | 1 | H-2-04 |
| 52 | Solucionario | → entrega del KuDE con QR al receptor. | → entrega al receptor (XML al receptor electrónico; KuDE con QR al no electrónico o al consumidor final). | 1 | H-2-04 |
| 53 | Solucionario | El volante exportado en PDF conserva su apariencia y el PNG del logo tiene fondo transparente. Los círculos soldados forman una sola figura; los agrupados siguen siendo dos. | Hay tres PDF (volante A4, tarjeta 90 × 50 mm y banner 2000 × 800 mm), un PNG transparente y sus originales editables. La unión es una geometría y el grupo conserva dos objetos. | 1 | H-2-10: punto de control igual al del laboratorio |
| 54 | Solucionario | 3.1 V — Y por lo tanto no entra en las sumas. | 3.1 V — Suele indicarlo con la alineación predeterminada; se confirma con ESNUMERO y, si es texto, no entra en las sumas. | 1 | H-2-17: coherencia con la Clase 2 (la alineación no prueba el tipo de dato) |
| 55 | Solucionario | Doctrina legal aplicada (verificada en agosto de 2026) | Doctrina legal aplicada (verificada en agosto de 2026; revisada el 22 de octubre de 2026) | 1 | H-2-11 |
| 56 | Solucionario | RG 41/2025 para contratos estatales desde 2/1/2026 y cronograma progresivo, ampliado por RG 52/2026. | RG 41/2025 para contratos estatales desde 2/1/2026 y cronograma progresivo, ampliado por RG 52/2026. Entrega: XML al receptor electrónico; KuDE al no electrónico o al consumidor final. Pendiente: confirmar si la RG 54/2026 modifica la RG 41/2025. | 1 | H-2-11 |
| 57 | Solucionario | Salario mínimo vigente por Decreto 6225/2026; | Salario mínimo mensual G. 3.044.000 desde el 1/7/2026 (Decreto 6225/2026); | 1 | H-2-12 |
| 58 | Planes_de_clase | Revisión de contenido octubre de 2026. | Revisión R2, 22 de octubre de 2026. | 1 | Identificación de la versión |
| 59 | Planes_de_clase | Plan 33 Clase 19 · Plan 34 Práctica 19 · Plan 35 Clase 20 + Práctica 20 + evaluación U6 en 80 min | Plan 33 Clase 19 + Práctica 19 · Plan 34 Clase 20 · Plan 35 Práctica 20 + evaluación U6 | 3 | H-2-05: redistribución sin cambiar los 36 encuentros ni las 72 HC |
| 60 | Planes_de_clase | Cuerpo de 7,5 pt en las tablas de los planes | Cuerpo de 9,5 pt; cada plan sigue en su página | 1731 | H-2-22: legibilidad; cada plan ocupaba un tercio de la página de oficio |
| 61 | Planes_de_clase | Renglón de 30 guiones en la celda Docente | 22 guiones | 36 | H-2-22: evitar que el renglón se parta en dos líneas |
| 62 | Planes_de_clase | Viñetas pegadas («…contenido• Desarrollo…») y salto final | Una viñeta por párrafo | 3 | H-2-18: maquetación de la celda Desarrollo |

## Índices estáticos recalculados

Números de página buscados en el PDF renderizado de R2 (segunda pasada; la primera ya había corregido los desplazamientos).

- **tomo**: 28 entradas verificadas contra el render.
- **lab**: 20 entradas verificadas contra el render.
- **sol**: 28 entradas verificadas contra el render.
- **planes**: 36 entradas verificadas contra el render.
