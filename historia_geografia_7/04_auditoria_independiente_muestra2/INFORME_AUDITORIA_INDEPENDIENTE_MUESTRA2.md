# INFORME DE AUDITORÍA INDEPENDIENTE — SEGUNDA MUESTRA

**Colección:** Historia y Geografía, 7.º grado, edición 2026.  
**Fecha de revisión:** 14 de octubre de 2026, America/Asuncion.  
**Repositorio:** FernandoAquinoBerni079/FernandoAquinoBerni079.  
**Commit obligatorio y único origen de los materiales:** `31c8d406aad9992f9f03ebc67d13d4e53fc58401`.  
**Carpeta examinada:** `historia_geografia_7/03_muestra2/`.  
**Dictamen del conjunto congelado: NO APTO para liberación comercial o impresión definitiva.**

La muestra permite reconocer avances importantes: capacidades completas en las clases auditadas, fuentes históricas identificadas, distinción explícita entre autonomía colonial y democracia, actividades cartográficas reproducibles, un caso de decisión con roles y una evaluación de 28 puntos con clave. Sin embargo, permanecen errores en una imagen, discrepancias de trazabilidad curricular, exigencias de puntuación no explicitadas y problemas en la planificación del tiempo. El dictamen se refiere a este conjunto y a este commit; no certifica ni rechaza las secciones del tomo anual que no están incluidas.

## 1. Alcance, independencia y preservación

Se descargaron 32 archivos del commit: los diez PDF de la muestra, la reproducción del programa MEC, siete figuras, tres JSON, el texto extraído del programa, nueve scripts y el informe editorial. Se comprobó para cada archivo el SHA-1 de objeto Git calculado a partir de sus bytes contra el árbol del commit. **32 de 32 coincidencias.** También se registraron tamaño y SHA-256 en [MANIFIESTO_VERIFICADO.json](MANIFIESTO_VERIFICADO.json).

Los documentos originales no se editaron, reconstruyeron ni reemplazaron. No se generó ninguna nueva versión comercial, no se creó un commit y no se escribió en Drive. Las copias exactas están en `origen_commit/`, dentro de esta carpeta de auditoría; los PNG y las hojas de contacto son evidencias de lectura, no documentos comerciales.

Se inspeccionaron visualmente **204 páginas**: 56 de los cinco originales, 56 de sus copias livianas y 92 de la reproducción del programa. Todas fueron renderizadas con Poppler a 100 dpi. Se visualizaron hojas de contacto de todas las páginas y se ampliaron las páginas cartográficas, las figuras y las páginas con incidencias. La extracción de texto, el examen de tamaños tipográficos y la lectura de los datos se usaron como controles complementarios, no como sustitutos de la inspección visual.

| Documento original | Copia de `revision_liviana/` | Páginas por archivo | Resultado del contraste |
|---|---|---:|---|
| `tomo/TOMO_MUESTRA2_oficio.pdf` | `TOMO_MUESTRA2_oficio_REVISION.pdf` | 26 | Texto y paginación iguales; imágenes comprimidas en la copia liviana |
| `planes/PLANES_MUESTRA2_A4.pdf` | `PLANES_MUESTRA2_A4_REVISION.pdf` | 10 | Texto y paginación iguales |
| `solucionario/SOLUCIONARIO_MUESTRA2_A4.pdf` | `SOLUCIONARIO_MUESTRA2_A4_REVISION.pdf` | 5 | Texto y paginación iguales |
| `matriz/MATRIZ_CURRICULAR_36_ENCUENTROS.pdf` | `MATRIZ_CURRICULAR_36_ENCUENTROS_REVISION.pdf` | 7 | Texto y paginación iguales |
| `plan_anual/PLAN_ANUAL_OFICIO_v2.pdf` | `PLAN_ANUAL_OFICIO_v2_REVISION.pdf` | 8 | Texto y paginación iguales |
| `datos/MEC_2014_Programa_Historia_y_Geografia_7mo_reproduccion.pdf` | No aplica | 92 | Fuente curricular aportada; inspección visual completa y cotejo focalizado |

En A4, las diferencias numéricas de dimensiones entre original y liviano son inferiores a 0,001 puntos y no constituyen un cambio de formato. El control de texto dio coincidencia página por página en los cinco pares. La revisión visual no encontró páginas faltantes, tablas desaparecidas o alteraciones de orden por la compresión. Véase [COMPARACION_ORIGINAL_LIVIANO.json](COMPARACION_ORIGINAL_LIVIANO.json).

**Límites de la conclusión:** la factibilidad es una estimación pedagógica de escritorio; no se realizó una clase piloto con estudiantes ni una prueba de impresión física. La reproducción MEC aportada no se autenticó contra un ejemplar oficial. Las búsquedas externas se utilizaron exclusivamente para contrastar afirmaciones del material congelado y se citan en el apartado 8; no incorporan versiones posteriores de los documentos auditados. La ausencia de las Clases 16 y 17 completas en esta carpeta impide certificar que todos los datos requeridos por la Evaluación U5 hayan sido enseñados en el tomo anual.

## 2. Criterios de gravedad y decisión

- **Bloqueante:** impide ejecutar o corregir una actividad esencial, por ejemplo una página ausente, un mapa inutilizable sin alternativa o una clave inequívocamente falsa que invalida la prueba.
- **Mayor:** afecta aprendizaje, equidad de evaluación, viabilidad de la secuencia o veracidad de la atribución curricular; requiere corrección antes de una liberación comercial.
- **Menor:** afecta presentación, aprovechamiento del papel, claridad local o comodidad de uso y admite una solución sencilla.

**APTO:** sin problemas esenciales pendientes. **APTO CON OBSERVACIONES:** utilizable con ajustes menores, sin cambios necesarios en conceptos esenciales, criterios de calificación o secuencia didáctica. **NO APTO:** tiene problemas mayores o bloqueantes que requieren una nueva revisión antes de liberarse. No es necesario que exista un bloqueante para emitir NO APTO.

## 3. Resumen y registro de hallazgos

**20 hallazgos: 0 bloqueantes, 10 mayores y 10 menores.** Cada fila corresponde a una incidencia; las menciones en las tablas de páginas no vuelven a contabilizarla. Las páginas son las físicas del PDF, contadas desde la primera hoja. Todos los hallazgos de los cinco originales se observan también en sus respectivas copias livianas, con la misma página.

| ID | Archivo y página | Descripción y efecto | Gravedad | Corrección propuesta |
|---|---|---|---|---|
| A01 | Tomo, p. 7, Figura 10.1; Planes, p. 4 | La imagen conserva «Las instituciones que gobernaban la colonia» e incluye la encomienda. Su jerarquía visual induce a tratarla como órgano de gobierno. El epígrafe y el plan lo corrigen verbalmente, pero no eliminan la afirmación gráfica errónea. | **Mayor** | Corregir el título y la organización de la imagen o retirarla y conservar la Figura 10.2. Si se usa como documento para detectar errores, rotularla inequívocamente como esquema incorrecto y formular la consigna junto a ella. No presentarla como síntesis válida. |
| A02 | `planes/PLANES_MUESTRA2_A4.pdf`, pp. 3–4, Plan 15 | Ocho ítems (1, 2, 3, 6 y 11–14), con dos justificaciones, se asignan a 95–105; cinco más se hacen dentro de una explicación extensa de 20 minutos. Luego se pretende corregir en diez minutos y resolver oralmente la actividad 15 en cinco. La suma llega a 120, pero no asegura trabajo y devolución suficientes para un grupo heterogéneo. | **Mayor** | Redistribuir tiempos, corregir parcialmente durante cada bloque y explicitar qué se espera por escrito y qué oralmente. Reservar unos 20 minutos para los ocho ítems del tramo final. Mantener la actividad 16 como tarea y comprobar la secuencia en aula. Propuesta concreta en §6. |
| A03 | Planes, p. 5, Plan 28; Tomo, pp. 12, 15 y 17 | El tramo 25–45 combina lectura, entrega de ficha, tres ríos a repasar y nombrar, tres lugares, dos tramos limítrofes, tres países y cuatro actividades. El tramo 75–90 añade lectura de América, tres respuestas de fuente y otras tres actividades. Se concentra mucho trabajo cartográfico nuevo sin reserva para orientación o revisión de la ficha. | **Mayor** | Preparar fichas y materiales antes del encuentro, modelar un ejemplo, asignar al menos 25 minutos efectivos al mapa y redistribuir correcciones. Reducir repetición entre preguntas cerradas y fuente o indicar cuáles son de consolidación domiciliaria. Validar con estudiantes. |
| A04 | `datos/cotejo_capacidades.json`, sin página: ocho registros de evaluaciones y Continuación E; Matriz, pp. 2–7 | El JSON asigna H1 a las ocho evaluaciones con `cap_tomo` vacío y `ratio` 0; asigna G1 a la Continuación E. Son emparejamientos sin fundamento suficiente y difieren de la matriz nueva. El archivo tampoco diferencia claramente diagnóstico del maestro y estado de la muestra. | **Mayor** | Marcar los vacíos como «sin ficha / no cotejable», no como H1 ni capacidad truncada. Separar asociación propuesta de coincidencia textual. Versionar el alcance del diagnóstico y actualizar la relación con la matriz. Para E, distinguir ampliación histórica del XVIII de cobertura literal de H5. |
| A05 | `plan_anual/PLAN_ANUAL_OFICIO_v2.pdf`, pp. 1, 4 y 5; Matriz, p. 5 | El plan anual afirma «por requerimiento curricular» y «por priorización MEC» respecto de la Guerra Guaranítica. La reproducción aportada, pp. 54–57, delimita prehistoria y siglos XVI–XVII y no incluye ese tema en su lista. La matriz, en cambio, lo reconoce como puente del XVIII pendiente de decisión. H5 puede dar un antecedente sobre misiones del XVII, pero no convierte el conflicto de 1754–1756 en contenido literal de esa capacidad. | **Mayor** | Suprimir la atribución no sustentada al MEC o aportar el documento de priorización con fecha y página. Si se conserva, identificarla como ampliación editorial del XVIII y explicar qué antecedentes del XVII se evalúan. Alinear plan anual, matriz y datos. |
| A06 | Plan anual, pp. 1, 3, 4, 6 y 7 | Varias bandas llamadas «Capacidades» contienen síntesis editoriales, mezclan capacidades y temas o eliminan «Paraguay y América». La Unidad 2 sí usa una formulación literal. La distinción entre transcripción y adaptación no es explícita en el PDF. | Menor | Rotular las síntesis como «Propósitos de la unidad» y añadir los códigos y textos MEC completos, o identificar de forma visible que son formulaciones editoriales. Conservar por separado los indicadores específicos. |
| A07 | Tomo, pp. 19–20 y 23; `solucionario/SOLUCIONARIO_MUESTRA2_A4.pdf`, p. 4 | La consigna 4 pide decisión y un argumento por dimensión. La rúbrica otorga 2 de 8 puntos por mediterraneidad y 2 por una medida coherente. La medida se trabajó en la consigna 3 y la mediterraneidad aparece en la autoevaluación, pero no se exige incorporarlas en la decisión ni se explica si se calificará el conjunto de productos. | **Mayor** | Mostrar antes del taller los criterios y aclarar si se evalúan consignas 1–4 y matriz como un solo producto. Si la rúbrica es de la decisión, exigir expresamente relación con mediterraneidad y una medida en ese texto. Definir qué obtiene 0, 1 o 2 puntos. |
| A08 | Tomo, p. 26, ítem 14; Solucionario, p. 5, Parte F | La consigna pide relacionar posición, relieve y ríos con la economía y usar datos de cada clase. La rúbrica exige, además, «relieve con otro factor» para obtener ese punto. No está explicitado en el ítem; la respuesta modelo menciona «junto con otros factores», pero no desarrolla uno. | **Mayor** | Incorporar en la consigna «explicá el relieve junto con otro factor» o ajustar el criterio. Dar una respuesta completa de ejemplo, con un factor adicional desarrollado y los tres datos identificados, y describir puntuaciones parciales. |
| A09 | Solucionario, pp. 3 y 5, mapa 18-A y Partes C–D | La clave cartográfica está solo en prosa. No define tolerancia para Asunción e Itaipú, diferencia entre río bien nombrado y bien ubicado, ni crédito cuando se ubican uno o dos países. En D define medio punto por solo el nombre, pero no por solo la vertiente. El mapa docente resuelto facilitaría una corrección consistente. | Menor | Añadir un mapa resuelto separado de la prueba y criterios de tolerancia acordes al mapa aproximado. Precisar crédito parcial para cada componente, países y vertientes, sin alterar el total de 28. |
| A10 | Planes, p. 9, Plan 30 | Se ofrece tiempo adicional de 15 minutos, pero a los 80 minutos se retiran pruebas y comienza una corrección pública de A, B, C y D. Un estudiante que continúe hasta el minuto 95 puede oír respuestas, usar tiempo remanente en otras partes o trabajar sin condiciones equivalentes. | **Mayor** | Programar devolución colectiva después de finalizar todas las pruebas, o evaluar al grupo con apoyo en un espacio y horario que aseguren independencia. Reasignar los 40 minutos de cierre para que el apoyo quede dentro del encuentro de 120 minutos. |
| A11 | Planes, pp. 6–7; Tomo, pp. 17 y 22 | Se mencionan una Ficha 18-A con banco de nombres y tarjetas con dos preguntas guía para apoyo. Las fichas impresas no contienen esas adaptaciones. El docente puede prepararlas, pero el plan no lo indica como preparación ni ofrece el texto de las preguntas. | Menor | Aportar las adaptaciones en un anexo docente o señalar de forma explícita cómo prepararlas antes de clase. Proporcionar las dos preguntas por rol y el banco de palabras, sin confundirlos con material ya incluido. |
| A12 | Tomo, p. 13, Figura 18.1 | El recorrido general se reconoce, pero los nombres de puertos, kilómetros y la leyenda de calados son demasiado pequeños para una lectura cómoda en el tamaño impreso. El original ya tiene el problema; no es solo degradación de la copia liviana. El epígrafe no identifica la fuente ni la fecha de ese mapa heredado. | Menor | Usar una versión simplificada con rótulos legibles y fuente explícita, o ampliar y depurar la imagen. Evitar que los calados sin fecha se interpreten como datos operativos actuales. La Figura F.1 es una alternativa más clara para el recorrido general. |
| A13 | Tomo, p. 25, Parte D; `figuras/eval_u5_rios_numerados.png` | El mapa contiene cuatro números, pero el ítem, la tabla y la clave solo evalúan 1, 2 y 3. El script incluye San Lorenzo como 4. | Menor | Eliminar el 4 de ese mapa de evaluación o incluirlo explícitamente en pregunta, tabla, clave y puntaje. No dejar un elemento aparentemente evaluable sin instrucción. |
| A14 | Tomo, pp. 10, 21, 22 y 26; Solucionario, p. 2; Planes, pp. 8 y 10 | Hay hojas cuyo contenido ocupa solo la parte superior. En p. 10 del tomo queda un ítem con ocho renglones; en pp. 21–22 el caso y los roles no utilizan la mayor parte de la hoja; p. 26 deja gran blanco después de diez renglones. El solucionario p. 2 tiene solo dos respuestas. | Menor | Ajustar paginación y tamaño funcional de cajas. Mantener fichas separadas cuando favorezca fotocopia, pero aprovechar el espacio con notas por rol o apoyo. Compactar el solucionario y los remanentes de planes sin reducir legibilidad. No confundir blanco para escribir con blanco sin función. |
| A15 | Planes, pp. 3–4 y 7–8 | La banda «Cierre (15 min)» queda sola al pie de p. 3 y sus acciones pasan a p. 4. La tabla de evaluación del Plan 29 comienza al pie de p. 7 y «Criterios» continúa en p. 8 sin título de continuidad. | Menor | Mantener cada banda de fase con su primera fila. Repetir encabezado/título de continuación o mover la tabla de evaluación íntegra. |
| A16 | Tomo, pp. 6, 19 y 22; Planes, pp. 3 y 7 | Los planes piden agregar una fila al cuadro de elecciones, una pregunta en cada fila del cuadro de dimensiones y notas individuales por rol. Los cuadros están cerrados y las tarjetas no tienen zonas de notas o recorte individual. No se dice dónde registrar esos productos. | Menor | Señalar «en el cuaderno» o aportar zonas de escritura y tarjetas realmente separables, con espacio «qué gana / qué arriesga / argumento». Aprovechar el blanco de F-A/F-B. |
| A17 | Tomo, pp. 12, 14 y 17 | Los mapas nuevos tienen norte y coordenadas, pero carecen de una leyenda suficientemente explícita para límites, ríos y símbolos de ciudades/represas. Algunos rótulos de ríos se apoyan directamente sobre líneas. El Apa no está identificado, aunque es el extremo que usa la clave para un tramo limítrofe. En p. 14, «Escala de 1:50 millones» puede confundirse con la escala física de impresión, cuando corresponde al conjunto de datos. | Menor | Añadir leyenda, separar rótulos con líneas guía y marcar el Apa o explicar cómo reconocer la confluencia. Distinguir resolución de los datos de escala del mapa y explicitar la proyección o el carácter esquemático. |
| A18 | Matriz, p. 6, encuentro 30; Tomo, pp. 24–26; Planes, p. 9 | La columna «Capacidad en el tomo (maestro)» afirma «en la muestra 2: literal» para U5. El PDF del tomo no imprime una ficha de capacidad en esa evaluación. Los textos completos G1/G2 están en el Plan 30, no en el tomo. Una asociación pertinente no prueba una transcripción literal presente. | **Mayor** | Cambiar a «Evaluación asociada a G1/G2; capacidad explicitada en Plan 30; sin ficha literal en el tomo» o incorporar la ficha en una futura revisión autorizada. Distinguir correspondencia curricular y literalidad documental. |
| A19 | Tomo, p. 5; `INFORME_MUESTRA2.md`, §5 | La segunda transcripción de la Real Provisión se atribuye a un portal MEC sin URL, página, identificador o fecha de consulta. La referencia a Rivarola no señala página. El informe editorial declara que no se abrió el texto completo de las fuentes. La auditoría sí pudo leer una transcripción documental de Rivarola, pero eso no autentica la ortografía de la otra versión. | Menor | Completar referencias y conservar copia o enlace estable de cada transcripción. Señalar diferencias de edición; no afirmar cotejo paleográfico o autenticación del original si no se realizaron. |
| A20 | Matriz, p. 7, encuentro 36; Plan anual, p. 8 | La matriz asigna únicamente G1–G4 a la integradora de segunda etapa. El plan anual dice que integra Unidades 4–6 y relaciona historia colonial con geografía: la Unidad 4 corresponde a H5/H6. Los dos documentos definen coberturas distintas para la misma evaluación. | **Mayor** | Incluir H5/H6 junto a G1–G4 si se evalúan Unidades 4–6, o modificar la definición de cobertura en ambos documentos. Al revisar la prueba anual, relacionar cada ítem con su capacidad. |

### 3.1 Comprobación de los cuatro hallazgos previos

| Hallazgo previo | Estado independiente en este commit |
|---|---|
| H1 en las ocho evaluaciones | **Confirmado en el JSON diagnóstico; no confirmado como asociación de las ocho evaluaciones en la matriz nueva.** La matriz contiene U1 H1, U2 H2, U3 H3/H4, integradora 1 H1–H4, U4 H5/H6, U5 G1/G2, U6 G3/G4 e integradora 2 G1–G4. La última tiene el problema A20. El tomo de esta muestra solo incluye U5: no permite inspeccionar las otras siete pruebas. A04 y A18. |
| G1 en Continuación E | **Confirmado en el JSON; corregido a H5 en la matriz.** La pertinencia de una vinculación directa a H5 sigue sin quedar resuelta para un conflicto del XVIII. La atribución a una exigencia MEC en el plan anual carece de sustento en la reproducción aportada. A04 y A05. |
| Factibilidad del Plan 15 | **Observación vigente.** El plan asigna todas las actividades existentes, pero esa cobertura formal no prueba que alcancen los tiempos. A02. |
| Error conceptual de Figura 10.1 | **Confirmado y vigente dentro de la imagen.** El texto y la clave lo reconocen; el recurso gráfico no está corregido. A01. |

## 4. Inspección visual y pedagógica página por página

Las siguientes tablas cubren las **56 páginas distintas** de la muestra. Se vieron ambas representaciones de cada página; «O+L» significa original y liviano. Para consultar cada PNG, abrir [INDICE_EVIDENCIAS.html](INDICE_EVIDENCIAS.html), donde están los 204 renderizados y sus hojas de contacto.

### 4.1 Tomo — 26 páginas, O+L

| Pág. | Contenido y observación independiente | Gravedad / acción |
|---:|---|---|
| 1 | Portada rasterizada; título y grado claros, imagen sin cortes ni invasión del pie. No lleva rótulo destacado de «segunda muestra», aunque el índice la identifica por su selección. | Sin incidencia esencial. Para circulación de revisión, sería útil identificar la muestra en cubierta. |
| 2 | Presentación legible, párrafos cortos, márgenes amplios. Describe la colección completa, no únicamente las secciones presentes. Blanco inferior propio de preliminar. | Aceptable como presentación de colección; no se cuenta como página defectuosa por su blanco. |
| 3 | Índice de ocho entradas, puntos guía y páginas correctas: 4, 11, 17, 18, 21, 22, 23 y 24. Sin solapamiento. | Conforme. |
| 4 | Clase 10: capacidad H3 completa, tema y tres indicadores. Texto de contexto y condiciones de elección legibles; caja y márgenes correctos. La vacancia y gobierno en nombre de la Corona están explicitados. | Conforme en contenido principal; A19 afecta la trazabilidad documental de la fuente posterior. |
| 5 | Dos fragmentos con vocabulario y tres preguntas; seis renglones utilizables, contenidos en la caja. Contexto Irala/Cabeza de Vaca legible y sin salto defectuoso. | Menor A19: completar localizadores de transcripciones. |
| 6 | Figura 10.3, concepto de autonomía y cuadro 1537/actualidad. La secuencia cronológica se lee; distinción democracia/monarquía clara. El cuadro ocupa todo su ancho y no tiene una fila vacía. | Menor A16: explicitar dónde agregar la fila del Plan 15. |
| 7 | Figura 10.2 y Figura 10.1, seguidas de Cabildo y Obispado. Epígrafes pequeños pero visibles; no se superponen a los párrafos. La imagen heredada contradice la explicación. | Mayor A01. La Figura 10.2 permite distinguir funciones; no resuelve por sí sola la contradicción visual de 10.1. |
| 8 | Encomienda y tabla de tipos; caja de Leyes Nuevas; Ubicate con tres líneas; seis opciones múltiples. Página densa, pero ítems y opciones permanecen dentro de márgenes y sin cortes. | Conforme en clave y espacio. A02 para el tiempo de resolución. |
| 9 | Ordenamiento de seis hechos, tres completamientos, cuatro V/F y actividad 15. Renglones suficientes para justificaciones breves y cinco para la respuesta abierta. | Conforme visualmente. Para la actividad 15, el plan debe aclarar que la puesta en común es oral, aunque el tomo ofrece respuesta escrita. A02. |
| 10 | Actividad 16 sola: pide 6–8 líneas y ofrece ocho. Consigna legible y espacio suficiente. Mayor parte de la hoja sin función. | Menor A14: mejorar reparto de pp. 9–10; mantener espacio de redacción. |
| 11 | Clase 18: capacidad G2 completa; ficha, definiciones y red hidrográfica nacional legibles. Texto denso pero ordenado. No se equipara «renovable» con «inagotable». | Conforme en alcance. La dinámica del Pilcomayo está simplificada: no debe interpretarse como cauce continuo estable en todos los años. |
| 12 | Figura 18.2 con países, principales ríos y represas; cuadro de tres ríos; lagos/acuíferos y ejemplo. Las tablas son legibles. El mapa permite una orientación general; los rótulos sobre cauces y falta de leyenda dificultan lectura precisa. | Menor A17. No se considera un atlas de precisión. A03 para el uso temporal de la ficha. |
| 13 | Usos del agua, Hidrovía, Figura 18.1 y síntesis americana. Párrafos legibles; mapita con varios rótulos demasiado pequeños. La advertencia de impactos de Itaipú es pertinente. | Menor A12: mejorar imagen y referencia. El recorrido Cáceres–Nueva Palmira y acuerdo de 1992 se corroboraron. |
| 14 | Figura 18.3 con ríos/lagos de América, preservación y concepto de recurso. Norte visible; incluye Mackenzie, Amazonas, Mississippi y Paraná, entre otros. Rotulación fina, sin una escala física inequívoca. Amplio blanco inferior. | Menor A17. El blanco no impide la actividad; podría utilizarse para ampliar el mapa. |
| 15 | Fuente cartográfica con tres preguntas y seis renglones; consigna de ficha 18-A; actividades 1–10. Alternativas distribuidas, algunas en dos líneas, sin truncamiento. | Conforme visualmente. A03: tiempo insuficientemente reservado para lectura y cartografía. |
| 16 | Continuación de V/F; actividades 14 y 15 con cinco y cuatro líneas. Hay espacio para usos y medidas; los falsos admiten justificación breve. | Conforme. La actividad 15 es tarea en el plan; criterio de corrección suficiente. |
| 17 | Ficha 18-A, datos personales y mapa mudo de buen tamaño. No da las respuestas ni marca ciudades/represas, como corresponde a una ficha de localización. Norte y coordenadas visibles. Límites secundarios muy tenues frente a los ríos. | Menor A17: leyenda y mejor contraste en fotocopia. A11: no incluye la versión con banco de nombres que menciona el plan. |
| 18 | Continuación F: capacidad G2, indicadores, texto y Figura F.1. Recorrido principal y extremos identificables; tramo hacia Cáceres diferenciado en la leyenda como continuación aproximada. | Conforme para análisis escolar. No se juzga como carta de navegación. |
| 19 | Cuadro económico/social/ecológico, concepto de EIA y consignas 1–3. Dos líneas por respuesta breve, tabla y cajas completas. Falta zona para las preguntas extra del plan. | Mayor A07 y menor A16. Dos líneas alcanzan para una respuesta breve; no para un desarrollo extenso. |
| 20 | Consigna 4, ocho renglones y autoevaluación con columnas claras. La autoevaluación exige relación con mediterraneidad, pero la consigna escrita no la incorpora de forma explícita. | Mayor A07: hacer visibles los criterios del producto antes de calificar. |
| 21 | F-A: caso rotulado ficticio y sin cifras reales. Explica sequía, dragado, pescadores y humedal. Legible; mucho blanco y sin zona de notas. | Menor A14/A16. Caso suficiente para discusión cualitativa; no permite calcular costo-beneficio numérico y no lo solicita. |
| 22 | F-B: cuatro roles en tabla legible. Son descripciones de preocupación, no cuatro tarjetas independientes con guías y notas. | Menor A11/A14/A16: preparar apoyo y formato de roles utilizables. |
| 23 | F-C: nueve celdas de trabajo en tres dimensiones y ocho líneas de decisión. Celdas admiten frases breves. Puede faltar un beneficio ecológico positivo en el caso; la clave acepta «ninguno claro». | Conforme visualmente; mayor A07 para criterios de puntuación. Aclarar que «no se identifica» es respuesta válida cuando se justifica. |
| 24 | U5: título claro, tiempo/puntaje, seis alternativas y cuatro V/F con renglones. Requiere ficha 18-A explícitamente. No imprime ficha de capacidad G1/G2. | Conforme en clave cerrada; mayor A18 en el registro de literalidad de matriz. |
| 25 | C usa ficha externa incluida; D aporta mapa numerado y tres filas; E tiene cuatro casillas amplias. Aparece un cuarto número no solicitado. | Menor A13/A09. Sin superposición de tablas, pies o consignas. |
| 26 | F pide 8–10 líneas y ofrece diez. Redacción y extensión claras; queda gran blanco inferior. | Mayor A08 y menor A14. No falta espacio de respuesta. |

### 4.2 Planes — 10 páginas, O+L

| Pág. | Inspección y coherencia | Gravedad / acción |
|---:|---|---|
| 1 | Portada identifica planes 15, 28, 29 y 30, 36 encuentros y 120 minutos. Texto centrado, legible y sin cortes. | Conforme. 108 HC equivalen a 72 horas reloj en 36 encuentros. |
| 2 | Índice correcto: comienzos en 3, 5, 7 y 9. Blanco propio de preliminar. | Conforme. |
| 3 | Plan 15: datos, H3, tema, indicadores y secuencia. Texto principal de 10–10,5 pt, tablas legibles; fase de cierre queda al pie separada de sus acciones. Sobrecarga en 95–105. Además, dice mostrar distancia con España en «un mapa de América del Sur»: requiere un mapamundi o mapa atlántico que no está listado. | Mayor A02, menor A15/A16. Precisar mapa adicional entre materiales. |
| 4 | Cierre, diversidad, criterios, precisiones y tarea. Explicita el error de 10.1, pero mantiene el recurso en el tomo. Corrección de muchos productos en diez minutos. | Mayor A01/A02. Márgenes y firma adecuados. |
| 5 | Plan 28: secuencia íntegra en una página y cierre identificado. Todo ítem 1–15 queda asignado, con 14 oral y 15 tarea. No hay desbordamiento. Cartografía y fuente americana sobrecargan dos tramos. | Mayor A03. |
| 6 | Diversidad, lista de criterios, limitaciones de mapas y tarea. Material de apoyo mencionado, no suministrado. Página utiliza principalmente mitad superior. | Menor A11. El blanco puede aprovecharse para la lista de cotejo docente y preparación. |
| 7 | Plan 29: secuencia de grupos y productos razonable. Fichas existentes y referencias correctas. Tabla de evaluación continúa en página siguiente. Las dos preguntas guía de apoyo no están en F-B. | Menor A11/A15/A16. Mayor A07 en relación con rúbrica. |
| 8 | Criterios de tabla anterior, precisiones de respuesta abierta y tarea. Blanco amplio sin recurso adicional. | Menor A14/A15. El criterio «no se califica la decisión tomada» es acertado. |
| 9 | Plan 30: G1/G2 completos, tiempos 10+70+40, criterios y total coherentes. Tiempo de apoyo se superpone con corrección pública. No se dedica una devolución específica a Parte E. | Mayor A10. Añadir devolución breve de E dentro del cierre redistribuido. |
| 10 | Precisión sobre Clases 16–17, tarea y firmas en parte superior. La dependencia de esas clases se declara, pero el material completo no está en esta carpeta. | Menor A14. No se certifica la preparación anual para ítems de esas clases. |

### 4.3 Solucionario — 5 páginas, O+L

| Pág. | Inspección y comprobación | Gravedad / acción |
|---:|---|---|
| 1 | Fuente, Ubicate y actividades 1–14 de Clase 10. Tablas claras, sin cortes de respuesta. Orden correcto de seis hechos. Clave b/c/a/d/c/b. Diferencia de fechas de 28 días correcta; aceptar 27 exige explicar el criterio de conteo como indica la clave. | Conforme en respuestas principales. La referencia documental de p. 5 del tomo requiere A19. |
| 2 | Respuestas 15–16 con criterios y rúbrica de cuatro puntos; solo tabla superior. El modelo no equipara autonomía con democracia y explica la explotación. | Conforme en contenido; menor A14. |
| 3 | Clase 18: tres preguntas de fuente, Ubicate y actividades 1–15, en una hoja densa pero legible. Clave c/a/d/b/c/a; V/F y justificaciones correctos respecto del texto. Respuestas abiertas dan ejemplos y mínimos. | Menor A09: mapa resuelto y tolerancias. |
| 4 | Taller F: cuatro respuestas, rúbrica de ocho puntos y ejemplo de matriz. Admite distintas decisiones; medidas coherentes. Mediterraneidad puntuada y medida en producto requieren aclaración de consigna. | Mayor A07. El ejemplo ecológico «ninguno claro» evita inventar un beneficio. |
| 5 | U5: clave a/b/c/d/b/a; V/F V/F/V/F; C seis puntos; D Amazonas/Mississippi/Paraná y vertiente atlántica; E cuatro; F cinco. Total 28 correcto. Criterio extra sobre relieve no está en consigna. | Mayor A08; menor A09. Mayor A10 se origina en aplicación del plan. |

### 4.4 Matriz curricular — 7 páginas, O+L

| Pág. | Inspección y contraste | Gravedad / acción |
|---:|---|---|
| 1 | Diez capacidades con textos completos; localiza MEC pp. 55–57 y carga p. 46. Declara cotejo con reproducción, no autenticación oficial. Tabla amplia y legible. | Conforme. H1–H6 y G1–G4 son códigos editoriales de la matriz, no códigos impresos en el programa. |
| 2 | Encuentros 1–6. Tabla con ocho columnas, cuerpo 8,5 pt y encabezados visibles. Sin pérdida de filas. U1 se asocia a H1 y se indica ausencia de ficha en maestro. | Mayor A04 en los datos contradictorios, no en la asociación de U1. Legible al tamaño nativo; exige no reducir en fotocopia. |
| 3 | Encuentros 7–15. U2 H2; Clase 10 H3 marcada como ampliada. Renglones completos y resaltado visible. | Conforme en asociación actual; A04 para diferenciar del JSON. |
| 4 | Encuentros 16–20. U3 H3/H4 e integradora 1 H1–H4. No se finge ficha literal de evaluaciones del maestro. Tabla con encabezado repetido y filas íntegras. | Conforme como planificación/diagnóstico. No prueba corrección del contenido de evaluaciones ausentes. |
| 5 | Encuentros 21–26. E se asocia a H5 y reconoce siglo XVIII fuera del alcance literal. U4 H5/H6; Clase 16 truncada en maestro. | Mayor A05 por discrepancia con plan anual. H5 para E debe presentarse como relación contextual indirecta y no cumplimiento literal por la guerra. |
| 6 | Encuentros 27–32. Clase 18 y F pasan a G2 completo; U5 G1/G2. Afirma capacidad literal en tomo para U5, aunque no se imprime allí. Filas resaltadas completas. | Mayor A18; A04 en datos. |
| 7 | Encuentros 33–36. Clase 21 y gestión ambiental se vinculan adecuadamente a G4; U6 G3/G4; integradora 2 omite historia de U4. Tabla sin cortes. | Mayor A20. |

### 4.5 Plan anual — 8 páginas, O+L

| Pág. | Inspección y coherencia | Gravedad / acción |
|---:|---|---|
| 1 | Oficio horizontal, arquitectura 21+6+7+2 = 36. Etapa y Unidad 1 acompañadas de sus primeras filas. Tabla legible de 10 pt. Atribución de Guerra Guaranítica al currículo sin documento de respaldo. | Mayor A05; menor A06. |
| 2 | U1 evaluación y Unidad 2, encuentros 5–9. Banda de unidad junto a filas; sin títulos huérfanos. Capacidad de U2 coincide con H2. | Conforme visualmente. Fuentes/fichas del resto del año son planificación, no recursos comprobados en esta muestra. |
| 3 | Unidad 3, encuentros 10–14. Tabla ordenada, márgenes y columnas adecuados. Capacidad es síntesis editorial de H3/H4. | Menor A06. |
| 4 | Encuentros 15–20, cierre de etapa y apertura de Unidad 4. Banda de segunda etapa junto al nuevo bloque. Reitera priorización MEC de guerra del XVIII. | Mayor A05; menor A06. |
| 5 | Encuentros 21–25. Guerra Guaranítica fechada correctamente en XVIII, pero rotulada «Profundización sin contenido extracurricular», mientras matriz reconoce tema fuera de alcance. | Mayor A05: explicitar ampliación editorial y sustento. Diseño de filas conforme. |
| 6 | Unidad 5, encuentros 26–30. Capacidad resumida sin alcance Paraguay/América completo; Plan 28 anual enfatiza matriz de impactos, mientras plan detallado usa fuente/mapa y ubica el caso en 29. | Menor A06. Sin contradicción conceptual grave entre 28–29, pero conviene actualizar evidencias y nombres a fichas 18-A/F-A/F-B/F-C. |
| 7 | Unidad 6, encuentros 31–35; capacidades resumidas. Se incluyen clima y regiones de América en términos generales, pero encuentro 31 enfatiza Paraguay. | Menor A06. La matriz prevé completar clima americano: cobertura anual no certificada por esta muestra. |
| 8 | Integración Unidades 4–6, criterios generales, inclusión y firma. Bloque final unido y legible. | Mayor A20: discrepancia con códigos de matriz. Diseño conforme. |

### 4.6 Programa MEC aportado — registro visual completo de 92 páginas

Este PDF es una **fuente de contraste**, no un producto comercial sometido al mismo dictamen de diseño. Se vieron todas sus páginas renderizadas. El cotejo específico se concentra en pp. 2, 46, 51–60 y 76–84. El resto fue examinado para legibilidad, continuidad e integridad de la reproducción; no se declara validada cada afirmación general del programa ni su transcripción oficial.

| Páginas físicas examinadas | Resultado de inspección |
|---|---|
| 1, 2, 3, 4 | P. 1 en blanco; ficha catalográfica en 2, portada de área en 3 y aclaración editorial en 4. La hoja blanca forma parte del archivo descargado. |
| 5, 6, 7, 8 | Autoridades, índice y presentación legibles. El índice no coincide siempre con las páginas físicas posteriores; para esta auditoría se usan páginas físicas. |
| 9, 10, 11, 12 | Presentación en guaraní, fines y objetivos legibles; sin pérdida visible de párrafos. |
| 13, 14, 15, 16 | Perfil y principios; blancos amplios por distribución de secciones; columnas continuas. |
| 17, 18, 19, 20 | Características curriculares y comienzo de competencia/capacidad legibles. Algunas bandas quedan cerca de fin de página. |
| 21, 22, 23, 24 | Definiciones y bilingüismo. P. 22 tiene bloque de planificación muy ancho y margen derecho estrecho; no se utilizó ese bloque para transcribir capacidades específicas del grado. |
| 25, 26, 27, 28 | Propuestas lingüísticas y componente fundamental; columnas completas y legibles. |
| 29, 30, 31, 32 | Componente fundamental y diversidad; continuidad visual correcta. |
| 33, 34, 35, 36 | Igualdad y diversidad; títulos/columnas visibles; textos de estrategias no son ficha de capacidades del grado. |
| 37, 38, 39, 40 | Componente local y adecuación; blancos de final de sección y continuidad visibles. |
| 41, 42, 43, 44 | Adecuación y percepción docente; recuadros y columnas legibles. |
| 45, 46, 47, 48 | Esquema curricular y tabla de carga. P. 46 confirma 3 HC para Historia y Geografía y 40 minutos por HC, excluido receso. P. 47 casi vacía, p. 48 portada de área. |
| 49, 50, 51, 52 | Fundamentación y descripción. Se admite incluir otros temas sin reemplazar ni restar relevancia a los establecidos. Eso no equivale a declarar que la Guerra Guaranítica esté exigida. |
| 53, 54, 55, 56 | Orientación y alcance: p. 54 delimita prehistoria y siglos XVI–XVII; pp. 55–56 incluyen capacidades de historia y comienzo de geografía. Textos legibles para el cotejo. |
| 57, 58, 59, 60 | P. 57 completa geografía; 58–60 explican metodología y trabajo colaborativo. La fuente incluye explícitamente impacto ecológico, social y económico de Hidrovía. |
| 61, 62, 63, 64 | Estrategias de música, paisaje y fuentes; imágenes y cajas visibles. |
| 65, 66, 67, 68 | Investigación, problema, marco y metodología; columnas legibles. |
| 69, 70, 71, 72 | Investigación y componente fundamental; continuidad visible. Se observa referencia a Trabajo y Tecnología en estrategias generales: no se usa para inferir contenidos propios de Historia. |
| 73, 74, 75, 76 | Diversidad, visitas y evaluación; cajas y texto legibles. |
| 77, 78, 79, 80 | Coherencia aprendizaje/evaluación e instrumentos; tablas partidas con continuidad visible. P. 77 pide claridad de lo que se espera; pertinente a A07/A08. |
| 81, 82, 83, 84 | Lista de cotejo, matriz y prueba; indicadores/criterios visibles. P. 83 recomienda informar temas, condiciones y criterios de puntuación. |
| 85, 86, 87, 88 | Glosario y comienzo de bibliografía; blanco de distribución editorial. |
| 89, 90, 91, 92 | Bibliografía y créditos legibles. No se encuentra en estas páginas una lista adicional de capacidades que sustente la exigencia de Guerra Guaranítica. |

## 5. Coherencia de datos, capacidades y solucionario

### 5.1 Datos y procedencia

`datos/paginas_tomo.json` coincide con los comienzos y finales del PDF: Clase 10 4–10, Clase 18 11–16, ficha 17, F 18–20, fichas 21–23 y evaluación 24–26. El índice del tomo coincide con esas páginas.

`datos/estructura_maestro.json` conserva títulos del maestro, como «El derecho a la autonomía» y «Posición, ríos e Hidrovía», que difieren de títulos nuevos. Es admisible como inventario histórico del maestro, pero no debe interpretarse como inventario literal actualizado de la muestra. La matriz distingue contenido maestro y ampliación; el JSON de cotejo requiere la corrección A04 para no propagar asociaciones falsas por un campo vacío.

Se volvió a ejecutar el verificador del commit en modo de lectura: **24 controles correctos, 0 fallos**; claves totales a=5, b=5, c=5, d=3. Eso prueba presencia de números, asignación nominal y coincidencias de texto en los datos. No prueba corrección conceptual de imágenes, factibilidad de los minutos, legibilidad ni equidad de rúbricas. Por ejemplo, el verificador acepta el número 4 adicional del mapa porque no inspecciona numerales dentro de imágenes, y no detecta A07/A08.

### 5.2 Cotejo con reproducción MEC 2014

| Elemento | Resultado |
|---|---|
| Clase 10 y Plan 15 | Capacidad H3 completa, coincidente con p. 55. Real Provisión, Cabildo, Obispado y encomienda corresponden a sus temas. |
| Clase 18 y Plan 28 | G2 completa, coincidente con p. 57. Paraguay/América, Hidrovía, impactos y preservación están dentro del programa. |
| Continuación F y Plan 29 | G2 completa. Caso y roles desarrollan impactos; relación con mediterraneidad también se vincula a G1. Una ficha G2 no impide articular otra capacidad, pero debe explicitarse si se puntúa. |
| Plan 30 | G1 y G2 completos, pertinentes para U5. No aparecen como ficha literal en páginas de la prueba del tomo: A18. |
| Matriz, capacidades H1–H6/G1–G4 | Textos completos concordantes con reproducción pp. 55–57. Los códigos son de organización editorial. |
| Guerra Guaranítica | No está en la lista de capacidades/temas de pp. 55–57. La ampliación puede justificarse pedagógicamente; no puede atribuirse sin prueba a una exigencia MEC. |
| Clase 21 / gestión ambiental | Su vinculación a G4 sí tiene fundamento: p. 57 incluye gestión estatal, instituciones y normas bajo esa capacidad. No corresponde declararla fuera del currículo. |
| Carga horaria | 3 HC × 40 = 120 minutos; receso y formaciones no están incluidos en esa carga. La planificación necesita 120 minutos efectivos, no un bloque de reloj que incluya recreo. |

### 5.3 Corrección y suficiencia de respuestas

Se cotejaron los **16 ítems de Clase 10, 15 de Clase 18, cuatro consignas de F y 14 ítems de U5**, además de las seis preguntas de fuente, los dos Ubicate y la matriz F-C. No se encontró una alternativa cerrada con dos respuestas correctas ni una letra de clave diferente de la respuesta sustentada por el texto.

| Bloque | Comprobación de clave |
|---|---|
| Clase 10, 1–6 | b, c, a, d, c, b. Encomienda originaria y fecha 1547 coherentes con explicación. |
| Clase 10, 7 | Paréntesis: 5, 2, 6, 1, 4, 3, en el orden de hechos impresos. |
| Clase 10, 8–10 | españoles/indios; mitayos; alcaldes/regidores. |
| Clase 10, 11–14 | F, V, F, V; las dos justificaciones explican límites de elección y función del Cabildo. |
| Clase 10, fuente y 15–16 | Respuestas suficientes para gobierno en nombre de Corona, criterio de aptitud y autonomía limitada. La argumentación de encomienda exige datos y no una opinión sin sustento. |
| Clase 18, 1–6 | c, a, d, b, c, a. |
| Clase 18, 7–9 | afluente; vertiente; izquierda. |
| Clase 18, 10–13 | V, F, F, V; clave distingue tramos limítrofes e inagotabilidad. |
| Clase 18, fuente, Ubicate y 14–15 | Correctos en orientación general. Da medidas de distintos actores. Falta resolución gráfica/tolerancias A09. |
| F, 1–4 y matriz | Admite beneficios, impactos y varias decisiones. La matriz puede contener «sin beneficio ecológico identificado». Rúbrica de 8 puntos aritméticamente correcta, pero su objeto de evaluación debe aclararse: A07. |
| U5, 1–6 y 7–10 | a, b, c, d, b, a; V, F, V, F. |
| U5, 11–13 | C 6, D 3, E 4. Identificación solicitada de 1 Amazonas, 2 Mississippi y 3 Paraná coincide con clave. El número 4 no solicitado es A13. |
| U5, 14 | Rúbrica de 5 puntos suma correctamente. Necesita coherencia con consigna y un modelo desarrollado: A08. |

La clave ya no sostiene que la Real Provisión otorgara poder independiente o democracia universal. La suficiencia general del solucionario es buena para ítems cerrados y respuestas breves, y **insuficiente para calificar sin ajustes los productos afectados por A07/A08**. La recomendación A09 mejora consistencia entre docentes, especialmente en la parte cartográfica de la prueba.

## 6. Factibilidad de los 120 minutos

El presupuesto de minutos de los cuatro planes suma exactamente 120. Eso es un control aritmético, no una observación de aula. Las estimaciones siguientes consideran lectura guiada, ubicación, escritura breve y transición de tareas; son intervalos de juicio profesional y deben confirmarse con una prueba piloto.

| Plan | Evaluación independiente | Decisión |
|---|---|---|
| 15 / Clase 10 | No exige redactar las 16 actividades en clase: la 15 se hace oral y la 16 es tarea. Aun así, 95–105 contiene ocho ítems con dos justificaciones y deja escasa reserva. Estimación del tramo: aproximadamente 12–18 minutos, con mayor variación para lectores que necesiten volver al texto. Explicación institucional + cinco ítems en 75–95 también es ajustada. | **Factibilidad no demostrada en su distribución actual.** Mayor A02. Requiere reorganizar, no simplemente extender todo el encuentro. |
| 28 / Clase 18 | La ficha solicita 11 localizaciones/identificaciones agrupadas más cuatro actividades cerradas, dentro de 20 minutos con lectura y distribución. Para un grupo que aprende la red fluvial, ese bloque puede necesitar aproximadamente 25–35 minutos. Fuente americana + seis respuestas en 15 minutos carece de reserva suficiente. | **Factibilidad no demostrada sin andamiaje y preparación.** Mayor A03. |
| 29 / Continuación F | Hay 55 minutos entre lectura/roles y resolución/matriz/decisión (45–100), más 20 de devolución y autoevaluación. Caso corto y cualitativo, cuatro roles, dos equipos exponen. Es una carga razonable para 120 minutos si materiales están preparados y la consigna se unifica. | **Viable con observaciones.** Resolver A07; evitar escribir dos decisiones completas en tomo y ficha. Preparar apoyos A11. |
| 30 / U5 | Prueba de 70 minutos para 14 ítems heterogéneos; tiempo plausible para grupo preparado. Estimación orientativa: A 7, B 6, C 12, D 8, E 10, F 17, revisión 10 = 70. Son asignaciones propuestas, no tiempos medidos. | **Viable para grupo ordinario; aplicación con apoyo requiere corrección A10.** La preparación de Clases 16–17 no puede certificarse con esta muestra. |

### 6.1 Redistribución propuesta para Plan 15, sin aumentar 120 minutos

| Minutos | Trabajo propuesto | Evidencia |
|---|---|---|
| 0–10 | Activación del problema de vacancia | Respuestas orales |
| 10–25 | Contexto de provincia y ubicación con mapa atlántico/mapamundi | Problema en dos líneas |
| 25–45 | Lectura de condiciones y dos fragmentos | Tres respuestas de fuente; comprobación inmediata |
| 45–55 | Cronología, Ubicate y actividad 7 | Secuencia y diferencia de fechas |
| 55–65 | Comparación 1537/actualidad | Fila adicional en cuaderno; devolución breve |
| 65–90 | Instituciones, explicación crítica de imagen y actividades 4, 5, 8–10 | Cinco respuestas; comprobación por parejas dentro del bloque |
| 90–110 | Actividades 1–3, 6 y 11–14 | Ocho respuestas, incluidas justificaciones |
| 110–120 | Corregir errores prioritarios; actividad 15 oral; asignar 16 | Síntesis de autonomía y tarea |

La propuesta depende de corregir durante los bloques, preparar mapa y glosario y seleccionar errores para el cierre. **No promete corregir oralmente todas las respuestas al final.** Si el grupo necesita más apoyo, el plan debe declarar un núcleo obligatorio y actividades de consolidación; no evaluar como incompleto un trabajo que la secuencia no permitió desarrollar.

### 6.2 Ajuste recomendado de Planes 28, 29 y 30

Para Plan 28, preparar copias y colores, dedicar 25 minutos efectivos al trabajo de ficha y permitir revisión guiada. Una distribución posible: inicio 10; conceptos 15; ríos/mapa 25; lagos/acuíferos 10; energía/Hidrovía 10; América/fuente 20; cuidado 10; cierre 20 = 120. Las comprobaciones breves se integran en cada bloque. Si el mapa requiere 35 minutos, decidir de antemano qué ítems repetitivos pasan a consolidación; no recortar la interpretación cartográfica nueva.

Para Plan 29, usar F-C como única decisión escrita del equipo; los renglones del tomo pueden quedar como preparación individual o copia opcional. Hacer visibles mediterraneidad, medida y rúbrica antes de comenzar. Dos exposiciones en 13 minutos son plausibles si se asignan aproximadamente cuatro minutos por equipo y cinco de síntesis.

Para Plan 30 con apoyo: 0–10 organización; 10–95 aplicación (grupo general acaba en 80 y hace una actividad silenciosa sin clave); 95–110 devolución de A–E, especialmente mapas e impactos; 110–120 ejemplo y rúbrica de F. Si se exige la devolución original de 40 minutos, habrá que ofrecer el apoyo en otro horario/espacio previsto. La corrección pública no debe empezar mientras alguien aún responde la prueba.

## 7. Legibilidad, diseño y uso del papel

Los formatos son: tomo 612 × 936 pt (oficio vertical); planes y solucionario A4 vertical; matriz A4 horizontal; plan anual 936 × 612 pt (oficio horizontal). El cuerpo del tomo se concentra en 11–11,5 pt; planes 10–10,5; solucionario 10–10,5; matriz 8,5; plan anual 10. Los tamaños se midieron en el texto vectorial del PDF, no por apariencia de miniaturas. Los rótulos rasterizados de mapas no se incluyen en esas mediciones.

No se observó texto principal fuera de página, superposición general de tablas, cajas negras, pies tapados o renglones de respuesta separados de sus recuadros. Las tablas del tomo y evaluación mantienen bordes; los índices y pies son estables. Los márgenes laterales de la muestra son adecuados. La p. 3 de planes está muy ajustada en el pie y presenta la banda de cierre huérfana; la matriz es legible al tamaño nativo, pero su reducción a A4 vertical o fotocopia disminuida sería inadecuada.

Las páginas con mucho blanco se valoraron por función: preliminares 2–3 del tomo, portada/índice de planes y espacio de redacción son defendibles. En cambio, p. 2 del solucionario y pp. 8/10 de planes son remanentes que conviene compactar. Las fichas F-A/F-B separadas facilitan reproducción, pero deberían convertir blanco en notas y guías. P. 26 ofrece diez renglones para 8–10 líneas y no tiene insuficiencia de respuesta; su blanco inferior es una observación de economía editorial, no razón aislada de NO APTO.

Los mapas requieren conservar tamaño, color y contraste adecuados. La ficha 18-A es utilizable para orientación y evaluación escolar aproximada. No se hizo una fotocopia física: la recomendación de mejorar límites y leyenda es preventiva basada en su contraste visual, no una afirmación de que haya fallado una prueba de imprenta.

## 8. Contrastación factual y fuentes externas

Se contrastaron las afirmaciones centrales con la reproducción curricular y con fuentes documentales/institucionales. «Corroborado» no significa autenticación paleográfica de un original de 1537. Los puntos sin respaldo suficiente se mantienen como pendientes documentales, no se convierten automáticamente en errores conceptuales.

| Afirmación del material | Resultado y fuente |
|---|---|
| Elección por vacancia y gobierno en nombre de Corona | Corroborados en la transcripción documental reproducida por [Rivarola Paoli, Real Cédula de 1537](https://www.portalguarani.com/1067_juan_bautista_rivarola_paoli__/12674_la_cedula_real_del_12_de_setiembre_de_1537_por_juan_bautista_rivarola_paoli_.html). El texto respalda carácter condicionado y autoridad real. No se certifica la ortografía de la transcripción atribuida al portal MEC sin localizarla. |
| Reconocimiento de Irala en 1539; despoblamiento y Cabildo de 1541 | Corroborados con estudio que reproduce actuaciones y acta: [Peña Villamil, La fundación del Cabildo de la Asunción](https://www.portalguarani.com/2026_manuel_pena_villamil__/19245_la_fundacion_del_cabildo_de_la_asuncion_1969__por_manuel_pena_villamil.html). La condición de lugarteniente de Ayolas explica por qué es más preciso hablar de reconocimiento que de elección libre sin contexto. |
| Creación del Obispado en 1547 | Corroborada en [Arzobispado de Asunción, aniversario de la diócesis](https://arzobispado.org.py/aniversario-de-creacion-de-la-primera-diocesis-del-rio-de-la-plata-y-dedicacion-de-la-catedral-metropolitana/). El primer obispo nombrado no llegó; «primero en llegar» debe distinguirse de «primero nombrado». |
| Llegada de Fernández de la Torre en 1556 | Corroborada por investigación con testimonio y referencia al Archivo General de Indias: [Ruiz Jiménez, Ministriles en la catedral de Asunción (1556)](https://www.historicalsoundscapes.com/pdf/999/asuncion). La nota del Arzobispado dice «ocho años después», dato que no debe usarse para fijar el año sin este contraste adicional. |
| Reparto de encomiendas de 1556, originarios y mitayos | Corroboración documental en [Rivarola Paoli, El sistema de las encomiendas](https://www.portalguarani.com/1067_juan_bautista_rivarola_paoli__/12698_el_sistema_de_las_encomiendas_por_juan_b_rivarola_paoli_.html), que reproduce cartas/padrones y diferencia trabajo de casa/chacra y pueblos. La tabla del tomo es una simplificación escolar, no un inventario de todas las variantes coloniales. |
| Cuenca del Plata, cinco países y segunda extensión sudamericana | Corroborados en [CIC, Información general de la Cuenca del Plata, archivo institucional](https://archive.iwlearn.net/cicplata.org/indexf01d.html?id=lc_infogen). Se conserva el carácter aproximado del mapa escolar. |
| Dinámica del Pilcomayo y sedimentos | Corroborada en estudios de la Comisión Trinacional: [Sistema fluvial de embocadura](https://www.pilcomayo.net/media/uploads/biblioteca/libro_1470055328.pdf) y [Pilcomayo medio o zona de divagación](https://www.pilcomayo.net/media/uploads/biblioteca/libro_991_SE-015.pdf). Es más preciso explicar taponamiento, desbordes y diferencia entre cursos superior e inferior que una conexión permanente continua. |
| Central nacional Acaray | Corroborada en documentación de [ANDE, Central Hidroeléctrica Acaray](https://www.ande.gov.py/documentos/CH-ACARAY-WEB.pdf). No se agregaron cifras nuevas al tomo. |
| Cuatro países del Acuífero Guaraní | Corroborados en [MADES, Comisión del Acuífero Guaraní](https://www.mades.gov.py/2024/09/27/paraguay-presente-en-la-primera-reunion-de-la-comision-del-acuifero-guarani/). Referencia institucional al Patiño disponible en [MADES, recursos hídricos](https://www.mades.gov.py/resultados-de-proyectos-proteccion-y-conservacion-de-recursos-hidricos/). |
| Itaipú: inundación de Saltos del Guairá y afectación de población | Corroboradas en la historia institucional de [Itaipú](https://www.itaipu.gov.py/institucional/sobre-itaipu/nuestra-historia). El texto de clase reconoce beneficios y costos; no presenta la obra como beneficio exclusivo. |
| Acuerdo Hidrovía de 1992 y extremos Cáceres–Nueva Palmira | Corroborados en [ALADI, Acuerdo de Santa Cruz de la Sierra, tomo I](https://www2.aladi.org/sitioAladi/documentos/facilitacionComercio/Libro_AcuerdoSantaCruzSierra_Hidrovia_V1.pdf), p. física 7 para reseña de firma en junio de 1992. El acuerdo entró en vigor en 1995: el tomo dice firmado en 1992, por lo que no hay error en ese punto. |
| EIA y ley de 1993 | La finalidad preventiva coincide con [Ley 294/1993, BACN](https://www.bacn.gov.py/leyes-paraguayas/2374/ley-n-294-evaluacion-de-impacto-ambiental), especialmente arts. 3–4 y 7–12, y la referencia institucional se encuentra en [Normativa del MADES](https://www.mades.gov.py/normativa-control-de-calidad-ambiental-y-recursos-naturales/). El caso ficticio sirve para razonar; no es un procedimiento legal completo de autorización de dragado. |

**Pendientes documentales delimitados:** la literalidad/ortografía de la segunda transcripción MEC de la Real Provisión; un atlas nacional identificado para auditar la totalidad de afluentes y localizaciones menores; un localizador bibliográfico para cada fecha institucional adicional, como Charcas 1559; autenticación de la reproducción MEC frente a edición oficial. No se identificó con la evidencia disponible un dato inequívocamente falso en esos pendientes. No se declara que hayan pasado una comprobación documental completa.

Las figuras 18.2/18.3/F.1 y los datos de construcción permiten controlar qué nombres y puntos se dibujaron, pero el commit no incluye en esta carpeta el conjunto geográfico de Natural Earth utilizado. Se cotejaron imagen y código del mismo commit; no se reconstruyó el mapa con una versión actual del conjunto de datos ni se afirmó precisión topográfica. El rótulo de fuente y la indicación de posición aproximada son correctos como advertencia, pero necesitan las mejoras de lectura A17.

## 9. Dictámenes por documento y decisión del conjunto

| Documento / componente | Dictamen | Fundamento |
|---|---|---|
| Tomo: Clase 10, pp. 4–10 | **NO APTO** | A01 introduce una afirmación gráfica falsa en una síntesis didáctica. El tratamiento textual de la Real Provisión y las claves muestran mejora sustancial; requieren conservarse al corregir la imagen. |
| Tomo: Clase 18 y ficha, pp. 11–17 | **APTO CON OBSERVACIONES** en contenido y diseño | Actividades, respuestas y mapa permiten trabajar el contenido; A12/A17 son ajustes de lectura, leyenda y procedencia. Este dictamen no aprueba el tiempo del Plan 28, que tiene A03. |
| Tomo: Continuación F y fichas, pp. 18–23 | **NO APTO para calificar con la rúbrica actual** | Caso y roles son pedagógicamente útiles, pero A07 afecta la transparencia de la evaluación. A11/A16 son ajustes operativos menores. |
| Tomo: U5, pp. 24–26 | **NO APTO para evaluación sumativa en su forma coordinada actual** | A08 añade una exigencia no explicitada y A10 compromete la aplicación con apoyo. Total y claves cerradas correctos; A13 es menor. |
| Planes 15, 28, 29 y 30 | **NO APTO** | A02/A03 impiden asegurar factibilidad de dos secuencias; A10 requiere resolver equidad de aplicación. Plan 29 es viable con criterios y preparación explícitos. |
| Solucionario | **NO APTO como clave definitiva de calificación** | A07/A08 afectan criterios de productos puntuados. No se detectó clave cerrada falsa; A09 requiere aclaraciones adicionales. |
| Matriz curricular | **NO APTO como registro definitivo de conformidad** | A18 confunde asociación con literalidad presente en tomo; A20 altera cobertura de integración de segunda etapa; A04 exige resolver contradicciones del paquete de datos. |
| Plan anual | **NO APTO como planificación curricular definitiva** | A05 atribuye exigencia MEC sin respaldo y contradice la matriz; A20 define integración diferente. El diseño horizontal es utilizable; A06 es menor. |
| Reproducción MEC | **Fuente de contraste aceptada con límite de autenticación** | Permite cotejar textos y 120 minutos; no se emite aprobación comercial ni se certifica edición oficial. |

**Dictamen final: NO APTO.** No se recomienda liberar este conjunto congelado para impresión comercial ni usar sus rúbricas como calificación definitiva sin corregir los hallazgos mayores. No se emite APTO porque hay problemas esenciales pendientes; tampoco APTO CON OBSERVACIONES porque varios ajustes afectan conceptos, secuencia y puntuación, y exceden una mejora estética.

### Condiciones concretas para una nueva revisión

1. Resolver A01 en la imagen y comprobar su nueva impresión al tamaño real.
2. Hacer viable el tiempo de Planes 15/28 y documentar una prueba de aula o, como mínimo, una secuencia con tiempos de lectura, escritura, cartografía y devolución explícitos.
3. Alinear consignas, productos y rúbricas en F y U5; eliminar exigencias ocultas y resolver el tiempo adicional sin difusión anticipada de respuestas.
4. Alinear el JSON diagnóstico, la matriz y el plan anual; distinguir maestro, muestra, asociación propuesta y literalidad. Corregir la atribución MEC de Guerra Guaranítica y cobertura de integradora 2.
5. Atender hallazgos menores de mapa, paginación, apoyos, referencias y espacio de escritura. Renderizar nuevamente las páginas modificadas y comprobar tanto PDF original como copia liviana.

Estas son propuestas de corrección; **ninguna se aplicó a los documentos de origen**. Una nueva revisión debe identificar su propio commit y no sustituir retroactivamente la evidencia de esta muestra.

## 10. Evidencias y entrega

- [Índice visual de las 204 páginas](INDICE_EVIDENCIAS.html), con acceso a PNG individuales y hojas de contacto.
- [Manifiesto de los 32 archivos verificados](MANIFIESTO_VERIFICADO.json), con ruta original, blob Git, SHA-256 y tamaño.
- [Comparación de los cinco pares original/liviano](COMPARACION_ORIGINAL_LIVIANO.json), página por página.
- `origen_commit/`: copias exactas de los PDF, datos y fuentes examinados, conservando la estructura de `03_muestra2/`.
- `evidencias/`: un subdirectorio por PDF, con un PNG por página. Los nombres `p-XX.png` o `p-XXX.png` remiten directamente a la página física.

El informe y todas las evidencias se guardaron en una carpeta local separada de auditoría. El repositorio remoto, el commit de origen y las carpetas comerciales de Drive permanecen sin modificaciones por esta auditoría.
