# Matriz de hallazgos · Informática 2.º BTC · R1 → R2

Auditoría independiente del 22 de octubre de 2026 sobre los cinco documentos R1 (tomo, laboratorio, plan anual,
solucionario y planes de clase). Leí los cinco documentos completos. Las afirmaciones de la bitácora R1 las volví a
verificar sin darlas por buenas. Cada corrección está en `build/r2_2btc.py` y queda registrada, con su cantidad de
apariciones, en `BITACORA_R1_R2_2BTC.md`.

Gravedad:
- **Bloqueante**: enseña algo incorrecto, impide resolver una actividad o hace inviable la planificación.
- **Importante**: error de contenido, de sincronía entre documentos o de maquetación con efecto en el uso.
- **Menor**: redacción, coherencia fina o presentación.

## Hallazgos corregidos en R2

| ID | Gravedad | Archivo | Clase / sección | Evidencia en R1 | Corrección R2 | Estado |
|---|---|---|---|---|---|---|
| H-2-01 | Bloqueante | Tomo, Solucionario | Clase 4 (texto, Tabla 4, actividad 1.1); Sol. Clase 4 1.1 d) | El honorario se calcula con `=B4*12` y `=B4/2`. En la planilla del caso la columna B es Régimen (texto) y el honorario está en C. La fórmula devuelve #¡VALOR! | Referencias a `C2` en el texto, la tabla, las opciones y la clave. Rótulos «honorario anual del cliente de la fila 2» y «mitad del honorario mensual» | Corregido |
| H-2-02 | Importante | Tomo | Clase 7, texto y actividad 1.3 | `=C2+C3+…+B17` mezcla columnas en el mismo rango | `=C2+C3+…+C17` (2 apariciones) | Corregido |
| H-2-03 | Bloqueante | Laboratorio | Práctica 16 (figura) y Práctica 9 (figura) | La figura de la P16 usaba `=SI(B2>=…)`, que contradice la estructura (C = honorario). La figura de la P9 estaba desactualizada | Figuras 10 y 9 reemplazadas por las R2, ya cotejadas con la estructura A/B/C | Corregido |
| H-2-04 | Importante | Tomo, Laboratorio, Solucionario | Clase 20 (circuito, concepto clave, pie de la Fig. 13); Práctica 20 (modelo y paso 5); Sol. Clase 20 4.1 y U6 4.1 | «El receptor recibe el KuDE» presentado como regla general. No distinguía el receptor electrónico (recibe el XML) del no electrónico o consumidor final (recibe el KuDE). Tampoco mencionaba el envío diferido ni el CDC | Circuito reescrito: e-Kuatia diferido, transmisión dentro de 72 h desde la firma, XML al receptor electrónico, KuDE en papel o digital al no electrónico o consumidor final, CDC + QR. El KuDE no reemplaza al DE | Corregido |
| H-2-05 | Bloqueante | Plan anual, Planes, Laboratorio | Filas 19-20 del plan anual; planes 33-35 | El encuentro 35 juntaba Clase 20 + Práctica 20 + Evaluación de la Unidad 6 en 80 min (2 HC). No entra | Redistribución sin cambiar los 36 encuentros ni las 72 HC. Plan 33 = Clase 19 + P19 integrada. Plan 34 = teoría de la Clase 20. Plan 35 = P20 (50 min) + Eval. U6 (20 min). Plan anual: fila 19 → 2 h con P19 integrada; fila 20 → 4 h con P20 en encuentro propio. Prácticas integradas: «1, 4, 9, 11, 15 y 19» | Corregido |
| H-2-06 | Importante | Tomo | Clase 9, Figura 5 | La figura de tipos de gráfico usaba cifras que no salen del caso | Figura reconstruida en vector con los datos reales del estudio (honorarios por régimen, 12 meses, torta 33,3/37,0/29,6 con nota de redondeo, egresos ordenados). Pie actualizado | Corregido |
| H-2-07 | Importante | Plan anual | Bandas de unidad | El plan anual no mostraba las capacidades del programa | Cada banda UNIDAD lleva su capacidad, tomada del programa MEC BTC 2.º | Corregido |
| H-2-08 | Importante | Tomo | Clase 19, texto y actividad 2.3 | Atribuía el cambio del Ministerio de Hacienda a la ley de la DNIT | Oración sobre la Ley 7158/2023 (MEF). Consigna: «Las funciones del ex Ministerio de Hacienda las ejerce hoy el ____» | Corregido |
| H-2-09 | Importante | Laboratorio | Práctica 9, paso 5 | El autofiltro se aplicaba con la fila de total contigua. La planilla la toma como dato y la oculta al filtrar | Paso 5: seleccionar A1:C17 antes de activar el autofiltro | Corregido |
| H-2-10 | Importante | Solucionario | Tabla A, P14 | El punto de control de la P14 no coincidía con el del laboratorio | Sincronizado con el laboratorio | Corregido |
| H-2-11 | Importante | Solucionario | Doctrina legal aplicada | Fechada en agosto de 2026, sin la entrega por receptor ni el salario mínimo vigente | Rótulo «revisada el 22 de octubre de 2026». Fila de facturación con XML/KuDE (RG 54/2026 marcada como pendiente de verificación). Salario ₲ 3.044.000 desde el 1/7/2026 | Corregido |
| H-2-12 | Importante | Tomo | Clase 3, caja «En Paraguay» | «G. 3.044.000 es el salario mínimo vigente», sin fecha ni norma | Agrega «desde el 1 de julio de 2026 (Decreto 6225/2026)» | Corregido |
| H-2-13 | Menor | Tomo | Clase 5, ficha | El indicador no nombraba AHORA() ni horas, que el plan anual y los planes sí evalúan | «Usa HOY(), AHORA() y cálculos entre fechas y horas…» | Corregido |
| H-2-14 | Menor | Tomo | Clase 13 | Un párrafo largo («Descomponer un trazado…») tenía estilo Título 3: aparecía en la navegación y quedaba fuera de orden | Pasa a estilo Normal con entrada en negrita, ubicado después de «Un rectángulo convertido…» | Corregido |
| H-2-15 | Menor | Tomo, Laboratorio | Clase 14; Etapa 2 2.1; Práctica 14 | «PDF para imprenta para la imprenta» (redundancia). La consigna presentaba la conversión a curvas como obligatoria | «PDF preparado para la imprenta». Consignas: «Si la imprenta lo solicita, las tipografías del PDF se convierten a ____» | Corregido |
| H-2-16 | Importante | Plan anual | Párrafo de criterios | El programa de referencia nombra la página web de la SET sin aclarar el cambio institucional | Nota: desde 2024 esas funciones corresponden a la DNIT (Ley 7143/2023). La decisión es editorial y no se atribuye al MEC | Corregido |
| H-2-17 | Menor | Solucionario | Evaluación de la Etapa 1, 3.1 | La justificación se basaba en la alineación de la celda, que no prueba el tipo de dato | Justificación con ESNUMERO, coherente con la Clase 2 y la P2 | Corregido |
| H-2-18 | Menor | Planes de clase | Celdas «Desarrollo» de 3 planes | Dos viñetas pegadas en un mismo párrafo («…contenido• Desarrollo…») | Una viñeta por párrafo | Corregido |
| H-2-19 | Menor | Tomo | Clase 2, actividad 1.x | Los distractores B2-B17, B2..B17 y B2;B17 cambiaban de columna además de separador | C2-C17, C2..C17 y C2;C17: solo cambia lo que se evalúa (el separador) | Corregido |
| H-2-20 | Importante | Tomo | Todas las preguntas abiertas | El estudiante trabaja sobre el tomo, pero las abiertas no tenían espacio para responder | 180 renglones: 3 por pregunta en clases y evaluaciones de unidad, 4 en las de etapa. Pregunta y renglones se mantienen juntos | Corregido |
| H-2-21 | Importante | Tomo | 9 saltos de página manuales | Página en blanco cuando una clase terminaba justo al pie | Salto manual convertido en «salto de página anterior» | Corregido |
| H-2-22 | Importante | Planes de clase | Los 36 planes | Cuerpo de 7,5-8 pt; cada plan ocupaba un tercio de la página de oficio | Cuerpo de 9,5 pt. Renglón del docente 30 → 22 guiones para que no se parta. Cada plan sigue en su página | Corregido |

## Observaciones abiertas (no corregidas en R2)

| ID | Gravedad | Archivo | Clase / sección | Observación | Qué falta / quién decide |
|---|---|---|---|---|---|
| O-2-01 | Menor | Tomo, Laboratorio | Clases 1-9 | El libro del caso se llama «Honorarios_Arandu_2026» en unas consignas y «libro de sueldos» en otras | Unificar el nombre en la R3. No cambia cifras |
| O-2-02 | Menor | Solucionario | Orientaciones de los desafíos | Hay orientaciones de desafíos repetidas entre la Tabla A y el texto | Depurar en la R3 |
| O-2-03 | Menor | Planes de clase | Plan 16 | El instrumento menciona la Evaluación de la Unidad 3 en un encuentro que no la aplica | Revisar con Fernando el criterio de los instrumentos en continuaciones |
| O-2-04 | Menor | Tomo | Clase 16 | El ejemplo inicial `=SI(C2>=900000;"SIMPLE";"RESIMPLE")` también rotula como SIMPLE a clientes GENERAL. El texto aclara después que es una relación interna del estudio y que el SI anidado resuelve los tres casos | Aceptable como paso didáctico. Conviene una nota de alcance |
| O-2-05 | Menor | Tomo / figuras | Figura 1 | El ícono verde de planilla se parece a la marca de un programa comercial | Decidir si se reemplaza por un ícono neutro |
| O-2-06 | Importante | Tomo | Evaluaciones de unidad | Con los renglones agregados, algunas evaluaciones de unidad pasan a dos páginas con la última abierta en la segunda | Aceptable para impresión doble faz. Si se quiere una sola hoja, reducir renglones o reorganizar el bloque |
| O-2-07 | Importante | Todos | Organización anual | La equivalencia de 40 minutos por hora cátedra no está verificada en fuente oficial. Los 36 encuentros son una distribución editorial | Debe ratificarla la institución |
| O-2-08 | Importante | Solucionario, Tomo | Facturación electrónica | No se pudo leer el contenido de la RG DNIT 54/2026: el portal de la DNIT no respondió desde este entorno | Verificar en el portal antes de liberar |
| O-2-09 | Importante | Figuras | Rasters de las propuestas | Las figuras raster quedan a unos 250 ppi efectivos a 15,5 cm. Títulos y cifras miden 7 pt o más; las notas secundarias, unos 6 pt en el tomo y 4,5-5 pt en el laboratorio | Prueba de impresión física |
| O-2-10 | Importante | Laboratorio | Todas las prácticas | No se probó ninguna práctica en software real (planilla, editor vectorial, portal) | Prueba de laboratorio con el software de la institución |
| O-2-11 | Importante | Plan anual | Programa | El programa BTC 2.º consultado es la publicación de 2014. No encontré una edición más reciente | Ratificación del programa vigente por la institución |

## Verificado sin hallazgos

- Aritmética del caso: honorarios 12.150.000; 759.375; 7.650.000; 54.000.000; 51.600.000 con alquiler 2.300.000;
  IPS 306.000 / 561.000; 6.720.000; balance 6.000.000.
- 116 claves de opción múltiple, letra y texto, entre tomo y solucionario. Distribución a/b/c/d = 29/29/29/29.
- 72 HC en 36 encuentros: suma de tiempos del plan anual y de los 36 planes.
- Cobertura de las 4 unidades temáticas y de las 7 capacidades del programa MEC BTC 2.º.
