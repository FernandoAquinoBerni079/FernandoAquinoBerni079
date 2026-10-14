# DICTAMEN INDEPENDIENTE — MUESTRA 3

**Resultado: APTO CON OBSERVACIONES, como modelo de desarrollo.**

**¿Puede Claude iniciar los 36 encuentros utilizando esta muestra como modelo? SÍ, con las condiciones locales de este informe y la autorización de Fernando para la siguiente fase.** La recomendación técnica permite preparar el año; no autoriza imprimir, comercializar ni declarar aprobada la colección completa. No se produjo ni corrigió ningún material de enseñanza durante esta auditoría.

Fecha de revisión: **14 de octubre de 2026**. Repositorio: `FernandoAquinoBerni079/FernandoAquinoBerni079`. Rama solicitada para publicar: `claude/libros-5z31jx`. Versión examinada exclusivamente: **`841f5bc9e4a4fec11af63cc821fc3062a6587de8`**, carpeta `historia_geografia_7/04_muestra3/`. El antecedente A01–A20 es el informe independiente de Muestra 2, commit `31c8d406aad9992f9f03ebc67d13d4e53fc58401`; se consultó su texto original, no solo el informe del editor.

## 1. Fundamento del dictamen y límites

Se verificaron **15 hallazgos resueltos y 5 parcialmente resueltos**: A05, A10, A14, A17 y A19. No queda un hallazgo completamente pendiente. La gravedad original se conserva en el CSV para la trazabilidad; los residuos actuales de los cinco parciales son **menores y delimitados**, sin exigir rehacer la arquitectura. Ningún error bloqueante o mayor vigente fue demostrado en la estructura de las secciones incluidas. La fuente MEC pendiente no se considera autenticada, aunque su contenido sustantivo puede cotejarse en una edición documental identificable.

Se descarta APTO sin observaciones porque falta cerrar referencias, legibilidad cartográfica y dos decisiones operativas de planificación. Se descarta NO APTO como modelo porque la imagen conceptual errónea se retiró, las actividades esenciales tienen tiempo diferenciado, las rúbricas ya se comunican antes de evaluar y los registros curriculares dejaron de contradecirse en códigos y literalidad. Las observaciones requieren cambios locales, no repetir el diseño de tomo, planes y solucionario.

Este resultado **no certifica 36 encuentros terminados**: el paquete contiene solo Clase 10, Clase 18, F, U5 y planes 15/28/29/30. La matriz y el anual describen el conjunto, pero las otras clases y siete evaluaciones no están materialmente desarrolladas aquí. Tampoco se certifica correspondencia de todos los ítems futuros, autenticidad paleográfica, vigencia de leyes, exactitud topográfica de atlas nacional ni resultados de aprendizaje observados en aula. Se revisó una reproducción del programa MEC aportada, no se autentica como ejemplar oficial por estar en el repositorio.

## 2. Método y corpus comprobado

Se descargaron los diez PDF, siete imágenes, tres JSON, informe editorial y diez scripts de la muestra; también PDF y texto MEC del mismo árbol congelado: **33 archivos**, todos verificados contra su SHA-1 de blob Git y SHA-256 local. El manifiesto detalla cada archivo. Los cinco DOCX no forman parte de los 33: no fueron necesarios para la inspección solicitada de PDF y no se generaron versiones nuevas.

Se renderizaron los **112 folios** de los diez PDF a 100 dpi: 56 originales y 56 livianos. Se inspeccionaron visualmente las 56 páginas originales en vistas completas agrupadas, ampliando las figuras y páginas controvertidas. Se compararon las 56 parejas página por página: texto extraído idéntico en todas; 47 renderizados idénticos píxel a píxel; nueve diferencias de imagen en portada/figuras (tomo 1, 5, 6, 11, 12, 13, 16, 23 y solucionario 5), también inspeccionadas. La diferencia media de imagen no acredita por sí sola legibilidad: se usó solo para localizar esas revisiones visuales.

No se observaron caracteres fuera de la página, filas cortadas, superposiciones de títulos ni pérdida de renglones. La pequeña diferencia decimal de MediaBox de los A4 livianos no cambia el tamaño renderizado; no es un cambio de formato. Se conserva oficio vertical en tomo, A4 vertical en planes/solucionario, matriz horizontal y anual oficio horizontal. **No hubo impresión física ni aplicación con estudiantes.** La lectura digital a tamaño nativo indica qué etiquetas necesitan ampliación; las miniaturas de contacto no sustituyen ese juicio.

Se leyeron los contenidos de generación, organización de figuras, planes, matriz, anual y verificador. `controles_muestra3.json` declara 185 controles y cero fallos: es evidencia del productor, no resultado de una ejecución independiente de esos 185. No se ejecutó su verificador porque escribe ese JSON y exige DOCX/PyMuPDF; se realizaron comprobaciones propias sobre copias: diez capacidades literales, ocho asociaciones de evaluación, E sin asociación MEC, cuatro secuencias contiguas de 120 minutos y comparación de las 56 parejas. El archivo adicional `COMPROBACIONES_INDEPENDIENTES_M3.json` conserva los resultados.

El control editorial de «ocupación» calcula la posición vertical del último bloque, no el área realmente utilizada; además admite umbral menor en últimas hojas y no revisa la matriz ni el anual. Por eso 185 resultados correctos no cierran A14, A17, A19 ni prueban factibilidad en aula. El control de equidad reconoce ausencia de claves en Plan 30, pero no comprueba el conflicto temporal del futuro Plan 31.

## 3. Control individual A01–A20

La página es la del PDF original de Muestra 3, salvo referencia expresa al antecedente. «Resuelto» cierra el problema identificado; recomendaciones de mantenimiento o validación futura no significan que se haya inspeccionado un documento ausente.

### A01 — RESUELTO

**Gravedad original:** mayor. **Localización actual:** tomo/TOMO_MUESTRA3_oficio.pdf, pp. 5–6; planes/PLANES_MUESTRA3_A4.pdf, pp. 3–4.

**Problema anterior:** La imagen conserva «Las instituciones que gobernaban la colonia» e incluye la encomienda. Su jerarquía visual induce a tratarla como órgano de gobierno. El epígrafe y el plan lo corrigen verbalmente, pero no eliminan la afirmación gráfica errónea.

**Modificación y evidencia comprobada:** La antigua imagen errónea desaparece. La Figura 10.1 es una cronología de 1534–1556; la Figura 10.2 distingue autoridades civiles, Obispado y encomienda. La encomienda queda sin flecha de autoridad y rotulada «NO gobernaba». Las fechas de creación del Virreinato y Audiencia evitan proyectar toda la estructura a 1537. Es una síntesis simplificada admisible.

**Acción / condición:** Conservar la separación conceptual al reutilizar la figura; mejorar el tamaño de la nota de la figura según A17.

### A02 — RESUELTO

**Gravedad original:** mayor. **Localización actual:** planes/PLANES_MUESTRA3_A4.pdf, pp. 3–4; tomo, pp. 4–9.

**Problema anterior:** Ocho ítems (1, 2, 3, 6 y 11–14), con dos justificaciones, se asignan a 95–105; cinco más se hacen dentro de una explicación extensa de 20 minutos. Luego se pretende corregir en diez minutos y resolver oralmente la actividad 15 en cinco. La suma llega a 120, pero no asegura trabajo y devolución suficientes para un grupo heterogéneo.

**Modificación y evidencia comprobada:** Plan 15: fuente, Ubicate y actividades 1, 2, 3, 4, 7, 13 y 15 esenciales; 5, 8, 9, 10 de consolidación; restantes domiciliarias. La fuente recibe 14 minutos, instituciones 18 y cierre 20; ya no concentra ocho ítems y justificaciones en diez minutos. El bloque de consolidación de 12 minutos sirve como margen real.

**Acción / condición:** Validar en aula el bloque 47–55; si contar días y ordenar seis hechos supera ocho minutos, utilizar parte de 88–100 y dejar consolidación para casa. No añadir toda la tarea a los 120 minutos.

### A03 — RESUELTO

**Gravedad original:** mayor. **Localización actual:** planes, pp. 5–6; tomo, pp. 10–16.

**Problema anterior:** El tramo 25–45 combina lectura, entrega de ficha, tres ríos a repasar y nombrar, tres lugares, dos tramos limítrofes, tres países y cuatro actividades. El tramo 75–90 añade lectura de América, tres respuestas de fuente y otras tres actividades. Se concentra mucho trabajo cartográfico nuevo sin reserva para orientación o revisión de la ficha.

**Modificación y evidencia comprobada:** Plan 28 prepara copias y colores antes del encuentro, modela el primer paso y dedica 25 minutos al mapa con revisión. La fuente recibe 20 minutos sin las tres actividades adicionales anteriores; 2, 4, 6 y 9 son consolidación.

**Acción / condición:** Pilotar el mapa con un grupo heterogéneo; comprobar que la proyección o dibujo de referencia esté preparado. La factibilidad es una estimación pedagógica, no un ensayo de aula.

### A04 — RESUELTO

**Gravedad original:** mayor. **Localización actual:** datos/trazabilidad_curricular.json, encuentros 5, 9, 17, 18, 22, 25, 30, 35 y 36; matriz, pp. 1–8.

**Problema anterior:** El JSON asigna H1 a las ocho evaluaciones con `cap_tomo` vacío y `ratio` 0; asigna G1 a la Continuación E. Son emparejamientos sin fundamento suficiente y difieren de la matriz nueva. El archivo tampoco diferencia claramente diagnóstico del maestro y estado de la muestra.

**Modificación y evidencia comprobada:** Las ocho evaluaciones son asociación curricular y sin ficha: H1; H2; H3/H4; H1–H4; H5/H6; G1/G2; G3/G4; H5/H6/G1–G4. E tiene capacidades_mec vacío y ampliación editorial. Se separan ficha histórica del maestro, asociación y presencia en muestra3. Ya no hay asignación automática H1 a todos los vacíos ni G1 a E.

**Acción / condición:** Usar este JSON como trazabilidad vigente. Mantener el antiguo cotejo como diagnóstico histórico identificado. La corrección de códigos no verifica los ítems de las otras siete pruebas, ausentes de esta muestra.

### A05 — PARCIALMENTE RESUELTO

**Gravedad original:** mayor. **Localización actual:** plan_anual/PLAN_ANUAL_OFICIO_M3.pdf, pp. 1, 4–5; matriz, p. 5, encuentro 22; datos JSON, encuentro 22.

**Problema anterior:** El plan anual afirma «por requerimiento curricular» y «por priorización MEC» respecto de la Guerra Guaranítica. La reproducción aportada, pp. 54–57, delimita prehistoria y siglos XVI–XVII y no incluye ese tema en su lista. La matriz, en cambio, lo reconoce como puente del XVIII pendiente de decisión. H5 puede dar un antecedente sobre misiones del XVII, pero no convierte el conflicto de 1754–1756 en contenido literal de esa capacidad.

**Modificación y evidencia comprobada:** Se elimina la atribución a requerimiento o priorización MEC y se identifica el XVIII como ampliación editorial optativa. Sin embargo, el tema, indicadores y procedimiento de la fila 22 siguen centrados en Tratado de Madrid y Guerra Guaranítica; bandeirantes, Guairá y Mbororé aparecen como núcleo recomendado en observaciones, no como secuencia efectivamente desarrollada.

**Acción / condición:** Antes de producir el encuentro 22, convertir el núcleo del XVII en tema, indicadores, fuente y actividades; dejar 1754–1756 en recuadro optativo y alinear matriz/JSON. Residuo actual menor y localizado; la falsa atribución mayor original ya está retirada.

### A06 — RESUELTO

**Gravedad original:** menor. **Localización actual:** plan anual, pp. 1, 3, 4, 6–7; matriz, p. 1; datos JSON.

**Problema anterior:** Varias bandas llamadas «Capacidades» contienen síntesis editoriales, mezclan capacidades y temas o eliminan «Paraguay y América». La Unidad 2 sí usa una formulación literal. La distinción entre transcripción y adaptación no es explícita en el PDF.

**Modificación y evidencia comprobada:** Las bandas distinguen capacidades literales, con H1–H6/G1–G4, de la formulación editorial de la Clase 1. Los diez textos normalizados coinciden con el programa aportado. Temas e indicadores ocupan campos distintos.

**Acción / condición:** Mantener etiquetas de literalidad; los códigos H/G son identificadores editoriales de esta matriz, no códigos oficiales impresos por el MEC.

### A07 — RESUELTO

**Gravedad original:** mayor. **Localización actual:** tomo, p. 18 y ficha F-C p. 21; planes, pp. 7–8; solucionario, p. 3.

**Problema anterior:** La consigna 4 pide decisión y un argumento por dimensión. La rúbrica otorga 2 de 8 puntos por mediterraneidad y 2 por una medida coherente. La medida se trabajó en la consigna 3 y la mediterraneidad aparece en la autoevaluación, pero no se exige incorporarlas en la decisión ni se explica si se calificará el conjunto de productos.

**Modificación y evidencia comprobada:** La consigna 4 anuncia 8 puntos y solo califica la decisión F-C: mediterraneidad 2, tres argumentos 3, medida 2 y claridad 1. El solucionario aporta ejemplo completo y niveles 0/1/2 para los componentes de dos puntos. El plan lee los criterios antes de trabajar.

**Acción / condición:** Preservar los mismos criterios si se admite respuesta oral. La matriz de análisis y el borrador personal sirven para aprender; no añadirles una segunda nota oculta.

### A08 — RESUELTO

**Gravedad original:** mayor. **Localización actual:** tomo, p. 24, ítem 14; solucionario, p. 5; planes, pp. 9–10.

**Problema anterior:** La consigna pide relacionar posición, relieve y ríos con la economía y usar datos de cada clase. La rúbrica exige, además, «relieve con otro factor» para obtener ese punto. No está explicitado en el ítem; la respuesta modelo menciona «junto con otros factores», pero no desarrolla uno.

**Modificación y evidencia comprobada:** El ítem comunica relieve junto con otro factor y los cinco criterios de un punto. El modelo desarrolla suelo y lluvia, posición, transporte y energía; identifica datos de Clases 16, 17 y 18. Se explica la puntuación 1/0 por criterio.

**Acción / condición:** Antes de aplicar la prueba anual, comprobar que las versiones finales de Clases 16 y 17 realmente hayan enseñado esos factores. No están incluidas en el tomo de esta muestra.

### A09 — RESUELTO

**Gravedad original:** menor. **Localización actual:** solucionario, pp. 2, 4–5; tomo, pp. 16, 23–24.

**Problema anterior:** La clave cartográfica está solo en prosa. No define tolerancia para Asunción e Itaipú, diferencia entre río bien nombrado y bien ubicado, ni crédito cuando se ubican uno o dos países. En D define medio punto por solo el nombre, pero no por solo la vertiente. El mapa docente resuelto facilitaría una corrección consistente.

**Modificación y evidencia comprobada:** Hay mapa docente de referencia y tolerancia semántica para Asunción y de 1 cm para represas; C concede 0,5 por ubicación sin nombre y 0,5 por dos países; D concede 0,5 por la vertiente aunque falte el nombre. Total conservado en 28. La clave del mapa identifica los tres ríos correctos.

**Acción / condición:** Aplicar la tolerancia a tamaño real del mapa del estudiante y aclarar su ajuste si se reduce la fotocopia. No usar el tamaño en pantalla como regla de medición.

### A10 — PARCIALMENTE RESUELTO

**Gravedad original:** mayor. **Localización actual:** planes, pp. 9–10; plan anual, p. 7, encuentro 31; matriz, p. 7.

**Problema anterior:** Se ofrece tiempo adicional de 15 minutos, pero a los 80 minutos se retiran pruebas y comienza una corrección pública de A, B, C y D. Un estudiante que continúe hasta el minuto 95 puede oír respuestas, usar tiempo remanente en otras partes o trabajar sin condiciones equivalentes.

**Modificación y evidencia comprobada:** En el encuentro 30 ya no se divulgan claves durante el tiempo adicional 80–95. Devolución prevista en los primeros 20 minutos del 31. Pero también se permite terminar al inicio del 31 a quien necesite más de 15 adicionales, sin duración máxima ni orden explícito respecto de esos primeros 20 minutos. El Plan 31 no está incluido.

**Acción / condición:** Definir el apoyo excepcional antes de la devolución, con pruebas custodiadas y sin acceso a claves; reservar 20 minutos efectivos de devolución y al menos 100 para G3 en el caso ordinario. Si hace falta más apoyo, programarlo aparte o redistribuir de forma explícita sin recortar G3. Residuo menor de implementación; contaminación de claves original corregida.

### A11 — RESUELTO

**Gravedad original:** menor. **Localización actual:** planes, pp. 4, 6, 8; tomo, pp. 16 y 20.

**Problema anterior:** Se mencionan una Ficha 18-A con banco de nombres y tarjetas con dos preguntas guía para apoyo. Las fichas impresas no contienen esas adaptaciones. El docente puede prepararlas, pero el plan no lo indica como preparación ni ofrece el texto de las preguntas.

**Modificación y evidencia comprobada:** El Plan 28 imprime el banco exacto de nueve nombres y encarga escribirlo antes de clase en algunas copias. No afirma que ya esté en la ficha. F-B trae preguntas de ganancia y riesgo y espacio para argumento; Plan 15 ofrece dos opciones por pregunta de fuente.

**Acción / condición:** Preparar copias de apoyo antes del encuentro; no confundir la ficha estándar con una versión ya adaptada.

### A12 — RESUELTO

**Gravedad original:** menor. **Localización actual:** tomo, p. 12, Figura 18.2; p. 17; scripts/figuras.py.

**Problema anterior:** El recorrido general se reconoce, pero los nombres de puertos, kilómetros y la leyenda de calados son demasiado pequeños para una lectura cómoda en el tamaño impreso. El original ya tiene el problema; no es solo degradación de la copia liviana. El epígrafe no identifica la fuente ni la fecha de ese mapa heredado.

**Modificación y evidencia comprobada:** Se retira el mapa heredado de calados y kilómetros ilegibles/sin fecha. El sustituto propio muestra la ruta Cáceres–Nueva Palmira y cita Natural Earth. Continuación F remite a esa figura; no duplica una figura obsoleta.

**Acción / condición:** Conservar carácter aproximado y ausencia de datos operativos de calado. La letra pequeña del sustituto se registra en A17 como mejora residual.

### A13 — RESUELTO

**Gravedad original:** menor. **Localización actual:** tomo, pp. 23–24; figuras/eval_u5_rios_numerados.png; solucionario, p. 4.

**Problema anterior:** El mapa contiene cuatro números, pero el ítem, la tabla y la clave solo evalúan 1, 2 y 3. El script incluye San Lorenzo como 4.

**Modificación y evidencia comprobada:** El mapa de D solo contiene 1, 2 y 3; consigna, tabla y clave coinciden. Amazonas, Mississippi y Paraná son los ríos señalados.

**Acción / condición:** Mantener consistencia si se añade otro río: cambiar mapa, tabla, consigna, clave y puntaje conjuntamente.

### A14 — PARCIALMENTE RESUELTO

**Gravedad original:** menor. **Localización actual:** tomo, pp. 9, 19–21, 24; solucionario, pp. 1–5; planes, pp. 8 y 10; plan anual, p. 9.

**Problema anterior:** Hay hojas cuyo contenido ocupa solo la parte superior. En p. 10 del tomo queda un ítem con ocho renglones; en pp. 21–22 el caso y los roles no utilizan la mayor parte de la hoja; p. 26 deja gran blanco después de diez renglones. El solucionario p. 2 tiene solo dos respuestas.

**Modificación y evidencia comprobada:** Mejora el aprovechamiento: actividad 16 acompañada de autoevaluación; F-A agrega 12 renglones de notas; F-B ofrece tarjetas amplias; solucionario ya ocupa cinco páginas funcionales. Persisten remanentes de planes y hoja final del anual muy corta. La mitad inferior de F-C está libre, pero matriz/decisión y separación para fotocopia justifican una hoja propia.

**Acción / condición:** Compactar remanentes de planes y criterios generales del anual si se mantiene legibilidad. No llenar fichas con tareas innecesarias: blanco para responder y separación reproducible tienen función. Residuo menor editorial.

### A15 — RESUELTO

**Gravedad original:** menor. **Localización actual:** planes, pp. 3–4 y 7–8.

**Problema anterior:** La banda «Cierre (15 min)» queda sola al pie de p. 3 y sus acciones pasan a p. 4. La tabla de evaluación del Plan 29 comienza al pie de p. 7 y «Criterios» continúa en p. 8 sin título de continuidad.

**Modificación y evidencia comprobada:** La banda Cierre del Plan 15 está junto a su primera acción en p. 4. La tabla de evaluación del Plan 29 queda íntegra en p. 8. Las tablas de secuencia que continúan repiten encabezados.

**Acción / condición:** Conservar controles de salto al producir los demás planes.

### A16 — RESUELTO

**Gravedad original:** menor. **Localización actual:** planes, pp. 4 y 7; tomo, pp. 19–20.

**Problema anterior:** Los planes piden agregar una fila al cuadro de elecciones, una pregunta en cada fila del cuadro de dimensiones y notas individuales por rol. Los cuadros están cerrados y las tarjetas no tienen zonas de notas o recorte individual. No se dice dónde registrar esos productos.

**Modificación y evidencia comprobada:** Fila nueva del cuadro de elecciones y preguntas por dimensión van explícitamente en el cuaderno. F-A ofrece notas y F-B tiene ganancia, riesgo y argumento en filas recortables.

**Acción / condición:** Las copias por equipo deben permitir que cada estudiante recorte su fila sin perder instrucciones. Mantener la indicación de dónde escribir.

### A17 — PARCIALMENTE RESUELTO

**Gravedad original:** menor. **Localización actual:** tomo, pp. 6, 11–13, 16 y 23; solucionario, p. 5; figuras y script.

**Problema anterior:** Los mapas nuevos tienen norte y coordenadas, pero carecen de una leyenda suficientemente explícita para límites, ríos y símbolos de ciudades/represas. Algunos rótulos de ríos se apoyan directamente sobre líneas. El Apa no está identificado, aunque es el extremo que usa la clave para un tramo limítrofe. En p. 14, «Escala de 1:50 millones» puede confundirse con la escala física de impresión, cuando corresponde al conjunto de datos.

**Modificación y evidencia comprobada:** Se incorporan límites discontinuos, halos, leyenda paraguaya, escala gráfica aproximada y marca textual del Apa. «1:50 millones» se explica como nivel de detalle de datos. Pero la Figura 18.3 y mapa americano de evaluación no tienen una leyenda de símbolos completa; notas de fuente, Apa, puertos y texto del esquema quedan muy pequeños al tamaño colocado.

**Acción / condición:** Ampliar o depurar rótulos imprescindibles, dar leyenda a mapas americanos y símbolo del Apa en leyenda. Objetivo editorial: 8–9 pt efectivos para rótulos que el alumno debe leer; comprobar original al 100 % y prueba física posterior. No cambiar precisión del mapa por decorar.

### A18 — RESUELTO

**Gravedad original:** mayor. **Localización actual:** matriz, p. 7, encuentro 30; datos JSON, encuentro 30; planes, p. 9; tomo, pp. 22–24.

**Problema anterior:** La columna «Capacidad en el tomo (maestro)» afirma «en la muestra 2: literal» para U5. El PDF del tomo no imprime una ficha de capacidad en esa evaluación. Los textos completos G1/G2 están en el Plan 30, no en el tomo. Una asociación pertinente no prueba una transcripción literal presente.

**Modificación y evidencia comprobada:** La matriz dice sin ficha en tomo y G1/G2 explicitadas en el Plan 30. Desaparece la falsa afirmación de ficha literal en la evaluación del tomo. El JSON la registra como asociación curricular.

**Acción / condición:** Mantener diferencia entre pertinencia curricular y texto efectivamente impreso.

### A19 — PARCIALMENTE RESUELTO

**Gravedad original:** menor. **Localización actual:** tomo, p. 5; INFORME_MUESTRA3.md, sección de fuentes; scripts/contenido_tomo.py.

**Problema anterior:** La segunda transcripción de la Real Provisión se atribuye a un portal MEC sin URL, página, identificador o fecha de consulta. La referencia a Rivarola no señala página. El informe editorial declara que no se abrió el texto completo de las fuentes. La auditoría sí pudo leer una transcripción documental de Rivarola, pero eso no autentica la ortografía de la otra versión.

**Modificación y evidencia comprobada:** Rivarola queda identificado con título y libro de 1986 y sus palabras se comprueban en Portal Guaraní. La segunda transcripción sigue atribuida a portal MEC con enlace estable pendiente, sin identificador verificable. La búsqueda no localizó ese recurso oficial; ello no prueba que nunca existiera. La reproducción de Rivarola también contiene la expresión necesaria para la pregunta 2.

**Acción / condición:** Usar ambos fragmentos de una edición documental identificable, por ejemplo Rivarola/Portal Guaraní con URL completa y nota 105; o aportar URL y copia comprobable de la versión MEC. Mantener aviso de transcripción actualizada y no afirmar cotejo paleográfico. Cerrar antes de replicar Clase 10.

### A20 — RESUELTO

**Gravedad original:** mayor. **Localización actual:** matriz, p. 8, encuentro 36; plan anual, p. 8; datos JSON, encuentro 36.

**Problema anterior:** La matriz asigna únicamente G1–G4 a la integradora de segunda etapa. El plan anual dice que integra Unidades 4–6 y relaciona historia colonial con geografía: la Unidad 4 corresponde a H5/H6. Los dos documentos definen coberturas distintas para la misma evaluación.

**Modificación y evidencia comprobada:** Los tres registros incluyen H5, H6, G1, G2, G3 y G4 para Unidades 4–6. Identifican el ítem sobre Guerra Guaranítica como ampliación que debe reemplazarse o tratarse como optativa.

**Acción / condición:** Al construir la integradora definitiva, aportar matriz ítem–capacidad–puntaje y sustituir o separar el ítem 3 de ampliación. La prueba completa futura no queda auditada por corregir el registro.

## 4. Revisión visual página por página

Las observaciones también son aplicables al PDF liviano correspondiente, con las diferencias de compresión señaladas en §2. «Conforme» significa ausencia de defecto material visible en ese folio dentro del alcance digital, no certificación de impresión física. Los nombres siguientes corresponden a archivos del commit fijo.

### [TOMO_MUESTRA3_oficio.pdf](https://github.com/FernandoAquinoBerni079/FernandoAquinoBerni079/blob/841f5bc9e4a4fec11af63cc821fc3062a6587de8/historia_geografia_7/04_muestra3/tomo/TOMO_MUESTRA3_oficio.pdf) — 24 páginas

| Página | Inspección y resultado |
|---|---|
| 1 | Portada sin recortes; imagen ilustrativa, no fuente cartográfica. Texto de identificación visible. |
| 2 | Presentación legible; mucho blanco intencional de apertura. No confundir con página de actividades residual. |
| 3 | Índice correcto: Clase 10 p. 4; Clase 18 p. 10; 18-A p. 16; F p. 17; fichas 19–21; U5 p. 22. |
| 4 | Ficha H3 completa y texto histórico. Márgenes y párrafos completos; diferencia 1537/1539 explicada. |
| 5 | Dos fragmentos, seis renglones, cronología 10.1 y concepto. A01 corregido; referencia MEC pendiente A19. Cronología pequeña pero reconocible. |
| 6 | Comparación 1537/actual, autoridades 10.2 y Cabildo. Tablas completas. Nota dentro del esquema pequeña: A17. |
| 7 | Obispado 1547/primer llegado 1556 distinguidos. Tabla de encomienda completa; Ubicate con tres renglones. Actividades 1–4 visibles. |
| 8 | Actividades 5–15, ordenamiento y V/F con espacios. Actividad 15 tiene cinco renglones adecuados para respuesta breve. |
| 9 | Actividad 16 con ocho renglones y rúbrica de cuatro puntos; autoevaluación completa. Blanco final admisible, mejor que M2. |
| 10 | Ficha G2 y desarrollo hidrográfico legibles. Texto distingue cuenca/vertiente y márgenes; no se observaron recortes. |
| 11 | Mapa 18.1 y cuadro de tres ríos. Leyenda, límites y ríos diferenciados; Apa marcado. Notas y símbolos necesitan ampliación A17. |
| 12 | Ruta 18.2 simplificada y atribuida, sin calados antiguos. Leyenda comprimida y puertos pequeños: A17. Cajas no se superponen. |
| 13 | Mapa americano 18.3, agua renovable y cuidado. Halos mejoran nombres; fuente de datos se distingue de escala impresa. Falta leyenda de símbolos A17. |
| 14 | Fuente cartográfica con seis renglones; Ubicate remite a ficha; actividades 1–10. Lectura y respuestas no invaden márgenes. |
| 15 | Actividades 11–15: renglones para falsas, cinco para usos y cuatro para medidas. Se exige ejemplo paraguayo de cada uso; clave merece precisión N01. |
| 16 | Ficha 18-A autónoma para fotocopia, con campos personales y mapa grande. Límites discontinuos, norte y barra. No contiene banco de palabras: plan explica cómo añadirlo. |
| 17 | F: ficha G2, dimensiones, EIA y primera consigna. Tabla íntegra. Referencia a Figura 18.2 correcta. Ley 294 citada como contenido, sin autenticar vigencia normativa en esta auditoría. |
| 18 | Consignas 2–4; rúbrica explícita de ocho puntos; borrador personal y autoevaluación. No hay criterio oculto ni salto dentro de la consigna 4. |
| 19 | F-A: caso ficticio identificado, información sin cifras inventadas como reales y doce renglones de notas. Hoja separada funcional. |
| 20 | F-B: cuatro filas amplias, ganancia/riesgo/argumento. Recorte por rol posible; encabezado no se repite en cada tarjeta, conservar instrucciones del taller. |
| 21 | F-C: matriz de nueve casillas y ocho renglones de decisión. Espacios suficientes; gran blanco inferior útil para notas, no motivo para cargar el taller. |
| 22 | U5: 70 minutos/28 puntos; A y B completas. B comunica crédito parcial para falsas; renglones permiten justificar. |
| 23 | U5 C: mapa incluido, cinco elementos y países. D: solo tres números y 3 puntos. Mapa de D queda aquí y respuesta en siguiente página; referencia clara, leve costo de pasar hoja. |
| 24 | U5 D–F: tablas completas; E permite un ejemplo por casilla; F diez renglones y cinco criterios explícitos. Blanco final no impide responder. |

### [PLANES_MUESTRA3_A4.pdf](https://github.com/FernandoAquinoBerni079/FernandoAquinoBerni079/blob/841f5bc9e4a4fec11af63cc821fc3062a6587de8/historia_geografia_7/04_muestra3/planes/PLANES_MUESTRA3_A4.pdf) — 10 páginas

| Página | Inspección y resultado |
|---|---|
| 1 | Portada institucional A4 con carga 3 HC/120 minutos; sin problemas visuales. |
| 2 | Índice: planes 15 p. 3, 28 p. 5, 29 p. 7 y 30 p. 9; páginas coinciden. |
| 3 | Plan 15: ficha, funciones y secuencia hasta 47–55. Tabla cercana al pie pero no corta contenido ni invade pie. |
| 4 | Plan 15 continúa con encabezado repetido; cierre acompañado de filas. Apoyos concretos, criterios y tarea. A02/A15/A16 corregidos. |
| 5 | Plan 28: mapa 25–50 sin cuatro actividades adicionales. Tabla y ficha completas; materiales preparados. |
| 6 | Plan 28: fuente 70–90 y cierre; banco de nueve nombres impreso en instrucciones docentes. Márgenes correctos. |
| 7 | Plan 29: caso/roles y matriz disponen de bloques separados. Preguntas nuevas van al cuaderno. Tabla continúa con encabezado. |
| 8 | Plan 29: decisión 18 minutos, dos exposiciones 14, autoevaluación 8. Evaluación íntegra, espacios de firma. Remanente inferior menor A14. |
| 9 | Plan 30: test 70 y apoyo 15; actividad sin claves. No devolución mientras se resuelve. Consignas de diversidad continúan en p. 10. |
| 10 | Plan 30: apoyo excepcional al 31 y devolución primeros 20, sin pauta temporal compatible: A10. Hoja aproximadamente medio vacía A14. |

### [SOLUCIONARIO_MUESTRA3_A4.pdf](https://github.com/FernandoAquinoBerni079/FernandoAquinoBerni079/blob/841f5bc9e4a4fec11af63cc821fc3062a6587de8/historia_geografia_7/04_muestra3/solucionario/SOLUCIONARIO_MUESTRA3_A4.pdf) — 5 páginas

| Página | Inspección y resultado |
|---|---|
| 1 | Fuente, Ubicate y claves Clase 10: respuestas correctas; 28 días entre fechas. Aceptar 27 con explicación de conteo es tolerancia didáctica, no cambio de fecha. |
| 2 | Respuestas 15–16, Clase 18 fuente/Ubicate y claves. Tolerancias cartográficas impresas; V/F continúa con encabezado en p. 3. |
| 3 | Clase 18 y F: respuestas abiertas suficientes y niveles 0/1/2. Ejemplo de consumo mediante acuífero no responde precisamente a uso de ríos: N01 menor. |
| 4 | U5 A–E: claves coherentes, C/D parciales explícitos y E admite respuestas alternativas. Tablas sin fragmentar filas. |
| 5 | U5 F: modelo desarrollado con otro factor; mapa docente completo. A08/A09 corregidos. Nota Apa pequeña A17. |

### [MATRIZ_CURRICULAR_36_ENCUENTROS_M3.pdf](https://github.com/FernandoAquinoBerni079/FernandoAquinoBerni079/blob/841f5bc9e4a4fec11af63cc821fc3062a6587de8/historia_geografia_7/04_muestra3/matriz/MATRIZ_CURRICULAR_36_ENCUENTROS_M3.pdf) — 8 páginas

| Página | Inspección y resultado |
|---|---|
| 1 | Diez capacidades y tipos de vínculo. Diferencia maestro/muestra y códigos editoriales. Tabla clara al tamaño nativo. |
| 2 | Encuentros 1–5. Clase 1 editorial, A vinculada H1 y U1 asociación sin ficha. Tabla densa pero íntegra. |
| 3 | Encuentros 6–13. H2 y H4/H3, U2 H2 sin ficha. Filas completas; recursos del maestro no equivalen a fuentes ya verificadas. |
| 4 | Encuentros 14–17. Clase 10 literal en muestra, D variante en maestro; U3 H3/H4. Sin recortes. |
| 5 | Encuentros 18–24. Integradora H1–H4. E XVIII como ampliación y núcleo XVII recomendado; todavía no desarrollado A05. |
| 6 | Encuentros 25–29. U4 H5/H6; Clase 18/F G2 corregidas y resaltadas. Fuente y rúbrica referenciadas. |
| 7 | Encuentros 30–34. U5 sin ficha en tomo y capacidad en Plan 30, A18 corregido. G3 del 31 sin reserva de devolución en esta fila: A10. |
| 8 | Encuentros 35–36. U6 G3/G4 e integradora H5/H6/G1–G4: A20 corregido. Poca carga final por fin de tabla, admisible. |

### [PLAN_ANUAL_OFICIO_M3.pdf](https://github.com/FernandoAquinoBerni079/FernandoAquinoBerni079/blob/841f5bc9e4a4fec11af63cc821fc3062a6587de8/historia_geografia_7/04_muestra3/plan_anual/PLAN_ANUAL_OFICIO_M3.pdf) — 9 páginas

| Página | Inspección y resultado |
|---|---|
| 1 | Oficio horizontal. Arquitectura 21+6+7+2=36 y 108 HC. Alcance XVI–XVII y XVIII editorial. Capacidades literales identificadas. |
| 2 | Encuentros 4–9, Unidad 2 H2; bandas junto a primeras filas. U1/U2 asociación compatible con JSON. |
| 3 | Unidad 3 H4/H3 y encuentros 10–14; tablas completas y indicadores concretos. |
| 4 | Encuentros 15–19 y segunda etapa. Clase 10 coherente con plan/tomo. Unidad 4 H5/H6; ampliación XVIII separada. |
| 5 | Encuentros 20–24. Fila 22 aún desarrollada sobre Guerra Guaranítica, núcleo XVII solo recomendado: A05 parcial. |
| 6 | Encuentros 25–29, Unidad 5 G1/G2. Clase 18 y F alineadas; tabla legible sin romper filas. |
| 7 | Encuentros 30–33. U5 y Unidad 6 G3/G4. Encuentro 31 no descuenta 20 minutos de devolución en sus productos: condición A10. |
| 8 | Encuentros 34–36. Cobertura H5/H6/G1–G4 e ítem XVIII optativo: A20 corregido en definición. |
| 9 | Criterios generales/inclusión y firma. Hoja muy corta: compactación menor A14; no añadir tareas por llenar papel. |

## 5. Factibilidad, evaluación y equidad

**Plan 15: factible como secuencia diferenciada, con margen estrecho en 47–55.** La cronología exige encontrar dos fechas, contar 28 días, explicar demora de noticias y ordenar seis hechos. Estimación prudente: 8–12 minutos si la línea está localizada; el tramo da ocho. El bloque 88–100 de consolidación permite absorber unos cuatro minutos sin quitar esenciales. Fuente de tres respuestas breves en 14 minutos y actividad 15 de cinco renglones en ocho son razonables con lectura acompañada. Las esenciales no incluyen todas las 16 actividades. La tarea domiciliaria agrega trabajo fuera de clase; no debe prometerse que el tomo completo se acaba dentro de 120 minutos.

**Plan 28: factible con preparación y apoyo.** Mapa en 25 minutos: explicación/modelado 5–7, trazo y nombres 13–15, revisión 3–5; total estimado 21–27. Si la orientación cartográfica es nueva, reducir consolidación y acompañar, no acelerar arbitrariamente. Fuente en 20 minutos: lectura de América 5–7, preguntas 8–10, comprobación 2–3. Las preguntas no exigen leer rótulos accesorios de tamaño diminuto; los ríos esenciales siguen reconocibles. El banco se prepara antes. Actividad 14 oral admite usos locales y ejemplos distintos de los de la clave.

**Plan 29: factible.** Caso, roles y reparto tienen diez minutos con copias listas; tres dimensiones y matriz reciben 30, decisión 18, dos exposiciones 14 y autoevaluación 8. Evitar repetir íntegramente la decisión en dos lugares: tomo es borrador, F-C producto calificado. No calificar dos veces. La rúbrica debe evaluar calidad de argumentos, no premiar de antemano aceptar o rechazar dragado. El caso se identifica como ficticio y solicita datos faltantes; es adecuado para argumentar sin fingir un estudio técnico real.

**U5 y Plan 30: prueba de 70 minutos plausible, a pilotar.** Una distribución orientativa es A 6–8, B 7–10, C 12–15, D 4–6, E 7–10, F 15–18 y lectura/revisión 5–8: 56–75 minutos. El mapa y diez renglones de desarrollo explican variación de velocidad; los 15 adicionales son coherentes. Los puntos suman 6+4+6+3+4+5=28. Claves cerradas correctas; falsas 8/10 justificadas; C/D distinguen componentes; E admite ejemplos alternativos; F ofrece respuesta desarrollada. La preparación de Clases 16/17 y exposición de escala institucional deben comprobarse antes de aplicar la versión anual.

**Plan 31: trasladar devolución es pedagógicamente adecuado**, porque permite corregir con rúbrica sin contaminar a quienes siguen rindiendo. Reservar **20 minutos efectivos**, dejando **100 para G3** en el encuentro ordinario de 120. El tema climático requiere conservar Paraguay **y América**, interpretación y relación con actividades humanas; no basta mencionar clima al final. Elaborar una secuencia verificable y un producto G3. Si alguien continúa la prueba al empezar el 31, esa continuación no puede ocurrir a la vez que se comunican respuestas: resolver el apoyo individual bajo supervisión antes de esa devolución, custodiar pruebas y pautar tiempo. Si no entra, organizar apoyo separado o redistribución explícita; no declarar cumplidas simultáneamente dos acciones incompatibles.

## 6. Currículo y fuentes

Se cotejaron los textos completos H1–H6/G1–G4 con la reproducción MEC, pp. 55–57, y el alcance histórico con p. 54. La carga de tres HC semanales de 40 minutos está en p. 46; los 36 encuentros son arquitectura editorial, no un número atribuido automáticamente al programa. Los códigos H/G también son de organización interna. Evaluaciones no tienen capacidad propia literal: integran capacidades de las clases. El JSON y matriz ahora lo explican correctamente.

**Continuación E:** bandeirantes, pérdida del Guairá y Mbororé son un núcleo histórico pertinente del XVII para contextualizar misiones, resistencia indígena y aportes de jesuitas bajo H5. Es una **selección didáctica inferida de la capacidad y tema**, no una lista de nombres explícitamente exigida por las páginas MEC aportadas. Guerra Guaranítica 1754–1756 queda en el XVIII y puede servir como ampliación optativa claramente señalada. El modelo debe permitir que se omita sin perder un aprendizaje obligatorio ni penalizar al alumno en la integradora. El actual anual todavía no convierte la recomendación en secuencia: A05 parcial. No se afirma haber visto una nueva Continuación E desarrollada, ausente de estos PDF.

**Real Provisión:** se comprobó el pasaje del primer fragmento en [Rivarola Paoli, «La Cédula Real del 12 de setiembre de 1537», reproducción de La economía colonial (1986), Portal Guaraní](https://www.portalguarani.com/1067_juan_bautista_rivarola_paoli__/12674_la_cedula_real_del_12_de_setiembre_de_1537_por_juan_bautista_rivarola_paoli_.html). Su nota 105 identifica una versión literal actualizada por Rivarola Bogarín y un localizador archivístico; no es una lectura paleográfica efectuada aquí. El mismo texto contiene el criterio de aptitud necesario para la segunda pregunta. No se encontró la página oficial MEC atribuida al segundo fragmento; búsquedas por título/frase no autentican esa atribución. Recomiendo tomar ambos fragmentos de una edición identificable y conservar URL, fecha y localizador, o aportar el recurso MEC recuperado. No copiar sin revisión el resto del artículo: contiene una fecha errónea «1587» en un comentario posterior, fuera del fragmento usado.

**Cartografía y datos:** archivos de figuras y `figuras.py` concuerdan con lo visible: coordenadas aproximadas de ciudades/represas, selección de geometrías y rotulación por ubicación del río Paraguay, límites discontinuos y nivel de detalle Natural Earth. No están aportados en esta carpeta los GeoJSON de entrada ni una validación nacional de cada afluente; se verifica coherencia interna, no se certifica precisión de atlas. El Apa se explica como desembocadura aproximada y no se dibuja su curso; no presentar la ausencia como inexistencia del río. Paraguay/Paraná/Pilcomayo, los países, represas y vertientes exigidas son reconocibles y las claves coinciden con esos objetivos. El mapa Hidrovía y extremos generales concuerdan con [el acuerdo de transporte fluvial de la Hidrovía Paraguay–Paraná, ALADI](https://www2.aladi.org/sitioAladi/documentos/facilitacionComercio/Libro_AcuerdoSantaCruzSierra_Hidrovia_V1.pdf); no representa calado disponible ni garantía operativa actual.

## 7. Observaciones adicionales y acciones de cierre

| ID | Archivo y página | Gravedad actual | Evidencia y corrección propuesta |
|---|---|---|---|
| N01 | Solucionario p. 3, Clase 18 actividad 14; tomo p. 15 | Menor | Se pregunta por importancia de los **ríos**, pero el ejemplo de agua para consumo es Acuífero Patiño. Es agua subterránea, no uso de un río. Sustituir ese ejemplo por abastecimiento o riego a partir de un río identificado, o ampliar expresamente consigna a recursos hídricos. Energía/transporte/pesca ya ofrecen alternativas correctas; no invalida toda la clave. |
| N02 | Planes pp. 3–4, Plan 15; tomo p. 7 Ubicate | Menor | Línea de tiempo + cálculo + explicación + seis hechos en ocho minutos es el punto de mayor tensión. Usar el margen de consolidación y verificar tiempo en aula. No presentar la suma aritmética como prueba de factibilidad. |
| N03 | Planes p. 10; anual p. 7; matriz p. 7 | Menor, vinculado A10 | La reserva del 31 todavía es una instrucción de futuro y la continuación excepcional no tiene duración/orden. Escribir la secuencia compatible antes de aplicar U5, sin sacrificar G3. |
| N04 | Tomo p. 5 y referencias editoriales | Menor, vinculado A19 | «Enlace estable pendiente» no es referencia final utilizable por docente. Cerrar con fuente identificable antes de reproducir esta clase en serie. |
| N05 | Anual p. 5; matriz p. 5; JSON encuentro 22 | Menor, vinculado A05 | Observaciones proponen un núcleo que tema/indicadores no implementan. Reescribir únicamente la planificación del 22 antes de desarrollarlo; no atribuir al MEC nombres que son selección editorial. |

Estas observaciones no se suman como cinco problemas independientes a A01–A20: N03–N05 concretan residuos ya registrados. A17 añade legibilidad de rótulos/leyendas y A14 compactación opcional. No hay recomendación de crear una cuarta muestra ni de alterar los archivos auditados.

## 8. Condiciones de la recomendación SÍ

1. Antes de replicar Clase 10: cerrar ambos fragmentos documentales y ampliar rótulos esenciales del esquema/mapas. Mantener rúbricas explícitas.
2. Antes de desarrollar encuentro 22: pasar el núcleo al XVII y dejar guerra del XVIII optativa; alinear tema, indicadores, fuente, evaluación, matriz y JSON.
3. Antes de aplicar U5: corregir el ejemplo N01, verificar preparación en Clases 16/17 y escribir Plan 31 con veinte minutos de devolución y capacidad G3 conservada, incluyendo apoyo excepcional sin claves simultáneas.
4. En los 36 planes: diferenciar esenciales/consolidación/tarea, preparar apoyos, mantener tablas y encabezados, relacionar cada evaluación con capacidades y criterios visibles.
5. Antes de autorización comercial: auditar el libro anual, los 36 planes, solucionario y ocho pruebas completos; realizar prueba física de impresión/fotocopia al tamaño previsto y una validación de tiempos en aula. Esta reauditoría no sustituye esas comprobaciones.

## 9. Evidencias, integridad y disponibilidad

`EVIDENCIAS_VISUALES/` conserva las 56 páginas originales renderizadas, cuatro páginas MEC de contraste y nueve páginas livianas con diferencias de imagen. Son **capturas de auditoría de las versiones existentes**, sin correcciones ni sustitución de documentos. Los nombres indican archivo y página; el índice HTML adicional permite abrirlas. El CSV incluye los veinte registros y distingue gravedad original de residual. El manifiesto registra fuentes, SHA-1 Git y SHA-256, alcance y evidencia.

Destino Drive de esta auditoría: [carpeta independiente](https://drive.google.com/drive/folders/1TThWvM3ynM-ZrAzTUsmuW9hQbutilZ1h), dentro de `00_CATALOGO_Y_CONTROL/HISTORIA_GEOGRAFIA_7_CONTROL_Y_AUDITORIAS/`. No se colocan versiones comerciales corregidas ni se reemplazan maestros. Copia GitHub solicitada: `historia_geografia_7/auditorias/AUDITORIA_MUESTRA3_841f5bc9/`, en un nuevo commit de documentación. Los identificadores de archivos publicados y comprobaciones posteriores se conservan en `VERIFICACION_PUBLICACION_M3.json`; su existencia y tamaños deben verificarse después de la subida, sin confundir el commit de publicación con el commit auditado.
