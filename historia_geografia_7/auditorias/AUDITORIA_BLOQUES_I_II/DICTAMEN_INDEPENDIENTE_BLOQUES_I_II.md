# Dictamen independiente — Bloques I y II

Historia y Geografía · 7.º grado · Colección 2026. Fecha de cierre: 15/10/2026. Auditoría documental, pedagógica, curricular y visual independiente del productor.

## Decisión

| Alcance | Dictamen | Fundamento determinante |
|---|---|---|
| Bloque I, encuentros 1–9 | **NO APTO en esta versión congelada** | BI-01: una tarea cartográfica esencial exige dos lugares que quedan fuera del mapa entregado. |
| Bloque II, encuentros 10–18 | **NO APTO en esta versión congelada** | BII-01: una respuesta modelo de la integradora contradice el límite temporal exigido al alumno. |
| Conjunto de 18 encuentros | **NO APTO para cierre y aplicación íntegra sin ajustes** | Deben cerrarse ambos defectos mayores y revalidar las partes afectadas. |

Estos dictámenes se refieren a los paquetes completos tal como están, no descalifican todas sus páginas. Se registran **11 hallazgos: 2 mayores y 9 menores; 0 bloqueantes**. Bloqueante se reserva para impedimento general de inspección/uso del conjunto; mayor afecta una actividad esencial, exactitud evaluativa o calificación y exige corrección previa; menor admite uso localizado con aclaración y no decide por sí solo el rechazo. La regla de decisión es explícita: un mayor abierto impide APTO/APTO CON OBSERVACIONES para el paquete congelado.

**Continuidad de Claude:** se recomienda que continúe la producción de los Bloques III y IV bajo el modelo actual, con correcciones localizadas y controles semánticos añadidos. No se requiere reconstruir los 18 encuentros. Antes de consolidar/aplicar estos dos bloques deben cerrarse BI-01 y BII-01; antes de replicar Clase 10, cerrar A19/N04. Es una recomendación técnica de continuidad, no autorización comercial ni aprobación del anual; Fernando decide.

## Versión, alcance e independencia

Repositorio `FernandoAquinoBerni079/FernandoAquinoBerni079`. Se resolvió ea3cf5f a **`ea3cf5f6349f4de2e1f3c495b92707b641e6d37e`** y se trabajó exclusivamente sobre ese estado para ambos bloques. Comparación cartográfica anterior: `755d7adbd0a4b57f0b91a95c85cd8b9ac978c705`. Modelo Muestra 3: `841f5bc9e4a4fec11af63cc821fc3062a6587de8`; dictamen previo consultado en la publicación `faf10e8fe9183bfbb75d784135b409e9494b9662` y copia local de auditoría. La rama `claude/libros-5z31jx` no se modifica ni se usa como referencia móvil.

Se descargaron 90 fuentes con identidad Git verificada: 83 archivos actuales de producción (12 PDF,28 figuras y 43 archivos de datos/código/informes), el programa MEC aportado y 6 archivos anteriores para contraste. Se excluyeron DOCX editables porque la inspección visual solicitada corresponde a PDF. Los originales descargados se preservaron; no se ejecutó generación de libros ni se produjo material comercial corregido.

Se renderizaron los 12 PDF a 100 ppp: **280 páginas**,140 originales y 140 livianas. Originales: tomo I: 41, planes I: 20, solucionario I: 10; tomo II: 39, planes II: 20, solucionario II: 10. Se inspeccionaron todas las páginas originales, con ampliaciones de páginas críticas; se cotejaron las 140 páginas livianas: texto idéntico en todas,112 rasterizados exactamente iguales y 28 con imágenes comprimidas revisadas visualmente. Sin pérdida funcional advertida en las versiones livianas. El registro individual siguiente cubre las 140 páginas originales y se aplica al par liviano correspondiente.

No hubo impresión/fotocopia física, ensayo con estudiantes ni contraste exhaustivo de todo itinerario de exploración con archivos históricos. La revisión de tiempos es estimación razonada. Las simulaciones de grises se identifican como digitales. Los informes del productor (1.626/1.655 controles,0 fallos) se trataron como declaraciones que requieren contraste.

## Hallazgos y correcciones localizadas

### BI-01 — MAYOR

**Archivo:** `historia_geografia_7/05_produccion_anual/bloque_1/TOMO_BLOQUE_I_oficio.pdf`. **Página:** 36–37; planes 17–18; solucionario 8. **Origen:** Nuevo en esta producción.

La Ficha B-1 no permite ubicar Beringia ni Monte Verde, exigidos en la consigna esencial 1.

**Evidencia:** El mapa termina aproximadamente en 34° N y 40° S. scripts/figuras/bloque1.py: mapa_civilizaciones usa marco(-118,-32,-40,34), también en la ficha. Beringia (~168° O,66° N) y Monte Verde (~73,2° O,41,5° S) quedan fuera. Dos pruebas independientes de encuadre fallan.

**Causa:** Reutilización de un mapa de civilizaciones para una actividad que además exige poblamiento continental; el control verifica existencia, no encuadre de los lugares pedidos.

**Corrección propuesta:** Ampliar el mapa para incluir los cinco puntos o separar poblamiento y civilizaciones en dos mapas explícitamente disponibles. Ajustar consigna, clave y 30 minutos esenciales del Plan 8; comprobar coordenadas antes de congelar.

**Imagen:** [página examinada](EVIDENCIAS_VISUALES/bloque_1_TOMO_BLOQUE_I_oficio_p37.png).

### BI-02 — MENOR

**Archivo:** `historia_geografia_7/05_produccion_anual/bloque_1/TOMO_BLOQUE_I_oficio.pdf`. **Página:** 38; 32; solucionario 8. **Origen:** Nuevo en esta producción.

La cronología rotulada en años d. C. comienza en 0; el solucionario dice que empieza en el año 0, mientras la Clase 1 explica que no existe ese año.

**Evidencia:** Contraste tomo p 6 (del 1 a. C. al 1 d. C.) con ejes de Figura 5.2 y Ficha B-2 y clave de consigna 3.

**Causa:** Traslado del origen numérico de un gráfico al calendario histórico sin aclaración.

**Corrección propuesta:** Rotular el inicio 1 d. C. o declarar que 0 es solo origen gráfico sin año del calendario; alinear figura, ficha y clave.

**Imagen:** [página examinada](EVIDENCIAS_VISUALES/bloque_1_TOMO_BLOQUE_I_oficio_p38.png).

### BI-03 — MENOR

**Archivo:** `historia_geografia_7/05_produccion_anual/bloque_1/TOMO_BLOQUE_I_oficio.pdf`. **Página:** 28–29; solucionario 6–7. **Origen:** Nuevo en esta producción.

La discusión de White Sands queda centrada en 2021 y omite la corroboración independiente publicada en 2023.

**Evidencia:** La fuente y F3 piden explicar la duda; la clave permite dejar White Sands aparte. Pigati et al., Science 2023, DOI 10.1126/science.adh 5007: polen terrestre y luminiscencia corroboran 21–23 mil años.

**Causa:** Actualización científica incompleta en edición 2026.

**Corrección propuesta:** Añadir la corroboración de 2023 y reformular F3 como evaluación de pruebas y métodos; admitir respuestas que mencionen esa actualización. No afirmar unanimidad académica.

**Imagen:** [página examinada](EVIDENCIAS_VISUALES/bloque_1_TOMO_BLOQUE_I_oficio_p29.png).

### BI-04 — MENOR

**Archivo:** `historia_geografia_7/05_produccion_anual/bloque_1/SOLUCIONARIO_BLOQUE_I_A4.pdf`. **Página:** 9, ítem 13 U2. **Origen:** Nuevo en esta producción.

La respuesta modelo enlaza la antigüedad de Monte Verde con la refutación del origen autóctono de Ameghino sin explicar la evidencia pertinente.

**Evidencia:** El modelo pasa de un campamento de 14.500 años a «Esto muestra que Ameghino se equivocaba al pensar que la humanidad se originó en América». Esa fecha prueba presencia pre-Clovis; por sí sola no prueba el continente de origen humano.

**Causa:** Inferencia causal comprimida en el ejemplo de respuesta.

**Corrección propuesta:** Comparar Monte Verde con una llegada exclusivamente tardía, o fundamentar la refutación de Ameghino en evidencia del origen africano humano y procedencia asiática expuesta en la Clase 4. Conservar los cinco criterios anunciados.

**Imagen:** [página examinada](EVIDENCIAS_VISUALES/bloque_1_TOMO_BLOQUE_I_oficio_p41.png).

### BII-01 — MAYOR

**Archivo:** `historia_geografia_7/05_produccion_anual/bloque_2/SOLUCIONARIO_BLOQUE_II_A4.pdf`. **Página:** 10, ítem 15; tomo 38. **Origen:** Nuevo en esta producción.

La respuesta modelo de la integradora rebasa el período que exige la consigna.

**Evidencia:** El ítem 15 pide cambios desde 1500 hasta mediados del siglo XVI; el ejemplo termina con la rebelión de Oberá de 1579. Una de las seis unidades de puntaje exige resistencia.

**Causa:** La clave usa un ejemplo de toda la Clase 9 sin verificar el límite temporal específico del ítem.

**Corrección propuesta:** Mantener el período y usar resistencia documentada de 1542–1543 o una forma no armada situada en ese período; alternativamente ampliar de forma explícita el período en consigna y criterios. Revalidar la clave sin penalizar respuestas cronológicamente correctas.

**Imagen:** [página examinada](EVIDENCIAS_VISUALES/bloque_2_SOLUCIONARIO_BLOQUE_II_A4_p10.png).

### BII-02 — MENOR

**Archivo:** `historia_geografia_7/05_produccion_anual/bloque_2/TOMO_BLOQUE_II_oficio.pdf`. **Página:** 26; e15.py; CONDICIONES_PRODUCCION.md. **Origen:** Heredado de Muestra 3: A19/N04, parcialmente resuelto.

El segundo fragmento de 1537 no reproduce literalmente la transcripción citada, pese a presentarse «con su ortografía».

**Evidencia:** Portal Guaraní imprime «a persona, que, según Dios, y sus conciencias pareciere más suficiente, para el dicho cargo». El tomo imprime «la persona que según Dios y sus conciencias pareciere mas suficiente para el dicho cargo». Cambian artículo, tilde y comas.

**Causa:** A19/N04 se marcó cumplida con referencia completa, manteniendo en VERIFICACION la grafía pendiente de cotejo.

**Corrección propuesta:** Restituir literalmente la edición indicada, señalando los cortes con puntos suspensivos, o declarar adaptación y normalización ortográfica/puntuación. No marcar A19 cerrada hasta cotejar ambos fragmentos.

**Imagen:** [página examinada](EVIDENCIAS_VISUALES/bloque_2_TOMO_BLOQUE_II_oficio_p26.png).

### BII-03 — MENOR

**Archivo:** `historia_geografia_7/05_produccion_anual/bloque_2/TOMO_BLOQUE_II_oficio.pdf`. **Página:** 22; planes 12; e14.py. **Origen:** Nuevo en esta producción.

Tabaré se sitúa solo «hacia 1542» sin distinguir los episodios de Aracaré y Tabaré de 1542–1543 ni identificar una referencia precisa.

**Evidencia:** Roulet (1990), Cuadernos Americanos 2(20),205–228, registra ambos episodios 1542/43. La precisión del productor sigue «fechas y lugares habituales; cotejar». No se considera falso el aproximativo «hacia».

**Causa:** Síntesis histórica apoyada en una referencia genérica no cerrada.

**Corrección propuesta:** Presentar el ciclo 1542–1543, distinguir a Aracaré y Tabaré y documentar el contexto regional del norte de Asunción (Ypané/Jejuí). Incorporar referencia verificable; admitir ambas fechas contextualizadas.

**Imagen:** [página examinada](EVIDENCIAS_VISUALES/bloque_2_TOMO_BLOQUE_II_oficio_p22.png).

### BII-04 — MENOR

**Archivo:** `historia_geografia_7/05_produccion_anual/bloque_2/SOLUCIONARIO_BLOQUE_II_A4.pdf`. **Página:** 9, ítem 14 integradora. **Origen:** Nuevo en esta producción.

La casilla de autoridad agrupa gobernador y encomenderos sin distinguir poder político formal y dominio sobre el trabajo.

**Evidencia:** El modelo dice «autoridades españolas (gobernador, encomenderos)»; tomo p 27 y U3 ítem 8 distinguen expresamente encomienda de gobierno de la ciudad.

**Causa:** Uso amplio de autoridad social sin explicitar la diferencia institucional enseñada.

**Corrección propuesta:** Indicar gobernador y Cabildo como gobierno colonial; encomenderos como poder económico/social y caciques como intermediarios con persistencias de autoridad local. Aceptar la distinción bien razonada.

**Imagen:** [página examinada](EVIDENCIAS_VISUALES/bloque_2_SOLUCIONARIO_BLOQUE_II_A4_p09.png).

### COM-01 — MENOR

**Archivo:** `historia_geografia_7/05_produccion_anual/bloque_2/SOLUCIONARIO_BLOQUE_II_A4.pdf`. **Página:** 10, matriz integradora; planes 20. **Origen:** Nuevo en esta producción.

La matriz muestra cobertura H1–H4, pero no permite calcular el peso exacto de cada capacidad en las filas compartidas.

**Evidencia:** Ítem 13: H2,H3,H4=3 puntos; 14 y 15: H1,H3=10 puntos. El Plan 18 afirma que la matriz muestra el peso de cada una. Sumar esos puntos a todas las capacidades duplicaría el total.

**Causa:** Se confunde cobertura múltiple con distribución numérica de puntaje.

**Corrección propuesta:** Repartir los subpuntos entre capacidades, o identificar puntaje compartido y retirar la afirmación de peso individual exacto. Mantener total 28 sin doble conteo.

**Imagen:** [página examinada](EVIDENCIAS_VISUALES/bloque_2_SOLUCIONARIO_BLOQUE_II_A4_p10.png).

### COM-02 — MENOR

**Archivo:** `historia_geografia_7/05_produccion_anual/bloque_1/TOMO_BLOQUE_I_oficio.pdf`. **Página:** 16–17,21,29,33; bloque II 6,11,23. **Origen:** Heredado parcialmente: A19 en el manejo general de fuentes; extensión nueva.

Varias síntesis y adaptaciones no incluyen edición o localizador suficiente para rehacer el cotejo.

**Evidencia:** Fuente A del taller: «bibliografía regional» sin título; esquema guaraní: ejemplo B. Melià sin obra/página; testamento resumido sin edición. La atribución y el tipo de fuente se declaran, pero la trazabilidad bibliográfica es desigual.

**Causa:** Referencia abreviada sin bibliografía docente consolidada.

**Corrección propuesta:** Añadir al solucionario una lista breve de ediciones, páginas y enlaces identificables para arqueología regional, Cortés, Colón, Requerimiento, Schmidl, testamento y síntesis guaraníes. Distinguir texto, transcripción, adaptación e interpretación.

### COM-03 — MENOR

**Archivo:** `historia_geografia_7/05_produccion_anual/bloque_1/PLANES_BLOQUE_I_A4.pdf`. **Página:** 10,16,18,20; bloque II planes 8,18,20; tomo II 39. **Origen:** Heredado de Muestra 3: A14, parcialmente resuelto.

Persisten remanentes cortos de algunos planes y una hoja de autoevaluación con amplio blanco inferior.

**Evidencia:** Inspección visual: algunas segundas hojas contienen solo diversidad/precisiones/tarea. La página 39 del tomo II tiene función de autoevaluación, por lo que no se trata como hoja inútil ni se exige igual paginación por clase.

**Causa:** Saltos automáticos conservadores con secciones docentes breves al final.

**Corrección propuesta:** Evaluar compactación de cada remanente con la hoja anterior manteniendo letra y encabezados; conservar fichas y espacio de respuesta útiles. La autoevaluación puede compartir espacio si resulta legible. Prioridad menor.

## Cotejo histórico y de fuentes

### Real Provisión: control literal solicitado

Se abrió la reproducción de Rivarola Paoli en Portal Guaraní, capítulo «La Cédula Real del 12 de setiembre de 1537», *La economía colonial*,1986, nota 105. Se coteja esa edición declarada, no el manuscrito original de 1537. Fecha del documento 12/09/1537 correcta.

| Segmento | Resultado literal |
|---|---|
| Primer fragmento, «elijan por Gobernador…Capitán general…provincia» | La secuencia interior coincide con la transcripción consultada; los puntos suspensivos señalan recorte. |
| Inicio del segundo | Fuente: «a persona, que,»; tomo: «la persona que». No coincide artículo ni puntuación. |
| Invocación | Fuente: «según Dios, y sus conciencias»; tomo elimina la coma después de Dios. |
| Calificación y cierre | Fuente: «pareciere más suficiente, para el dicho cargo»; tomo imprime «mas suficiente para», sin tilde ni coma. |

La atribución, edición, enlace y nota 105 mejoran respecto de Muestra 3; **A19/N04 sigue parcialmente resuelta**, no cerrada. No es aceptable decir «con su ortografía» si se adapta. El sentido de autoridad provisional en nombre del rey se enseña correctamente.

### Tabaré, Oberá y testamento

La ficha académica UNAM de Florencia Roulet (1990), *Cuadernos Americanos*2(20),205–228, identifica el ciclo Aracaré/Tabaré 1542/43. Se verificó la ficha bibliográfica; el enlace al artículo completo no respondió. Por eso se recomienda precisar ese ciclo y verificar el detalle regional en la edición antes del cierre, sin imputar como error absoluto el aproximativo «hacia 1542» (BII-03).

Se descargó y leyó el capítulo de Bartomeu Melià, «Oberá, una respuesta profética contra la opresión colonial», *El guaraní conquistado y reducido*, pp 31–40 (en el escaneo hay pliegos duplicados). Corrobora Guarambaré y hacia 1579. Presenta resistencia profética, rechazo al servicio y contrabautismo; reproduce también un testimonio colonial que habla de gente de guerra. Por ello no se considera sin más falsa la clave «resistencia armada» del ítem 12, aunque conviene enseñar su dimensión religiosa y discutir la perspectiva de la crónica. Oberá/Overá son variantes, no personajes diferentes. El problema inequívoco es usar 1579 para una respuesta limitada a mediados del siglo XVI (BII-01).

Se consultó *El testamento de Domingo Martínez de Irala*, edición de Enrique de Gandía en el repositorio del Instituto de Investigaciones Históricas UBA, pp 54–77: declaración de hijos y madres en pp 74–75, herencia y tutores p 75. El resumen escolar de 1556 es sustancialmente fiel y se declara no textual. No afirma que todas las mujeres consintieran ni que la herencia aboliera el dominio colonial. Debe agregarse la edición consultable al aparato docente (COM-02).

### Otros contrastes

Colón: el pasaje de buenos servidores/ingenio/conversión aparece en el Diario transmitido por Las Casas, edición digital BVMC, entrada de 11–12 octubre 1492, p 31. El tomo declara versión modernizada; no lo presenta como autógrafo conservado de Colón. Requerimiento: resumen escolar compatible con exigencia de obediencia a Corona/Iglesia y amenaza de violencia; conviene identificar edición del documento de 1513, en lugar de sostener una reproducción textual que no se ofrece. Cortés: la descripción del mercado y comparación con Salamanca corresponde a la Segunda Carta de 1520; modernización declarada y perspectiva del conquistador trabajada en las preguntas.

Tordesillas: PARES, Ministerio de Cultura de España, registro de 1494, confirma 7 dejunio y 370 leguas al oeste de Cabo Verde. El esquema aproximado 46°O es aceptable si no se pide precisión geodésica. Fundación de Asunción 1537, Cabildo 1541, llegada de Cabeza de Vaca 1542 y deposición 1544, Obispado 1547 y reparto deencomiendas 1556 son coherentes dentro de las secuencias examinadas. La encomienda se distingue correctamente del gobierno municipal en el tomo y U3; afinar la clave social del ítem 14 integrador (BII-04).

Prehistoria: se evita atribuir los 8.000 años regionales a un sitio paraguayo no fechado; las fechas son aproximadas. Se distingue origen africano de la humanidad, procedencia asiática del poblamiento y teorías historiográficas antiguas. Monte Verde 14.500 y Clovis 13.000 sirven al nivel escolar; White Sands requiere incorporar la corroboración 2023, sin convertir «consenso» en unanimidad (BI-03). Cultura guaraní: la diversidad regional y actual se reconoce, con reciprocidad, parentesco y papel de las mujeres; los esquemas no se presentan como descripción uniforme de todos los pueblos.

La tabla de 2012 identifica censo y cinco familias; es una lectura de fuente fechada, no una estadística actual 2026. La Constitución 1992,art 140, fue cotejada con edición institucional: el extracto sobre idiomas conserva su sentido y texto sustantivo. Los códigos H/G pertenecen a la editorial, no al MEC.

## Currículo y trazabilidad

El PDF del programa MEC2014 aportado y su texto extraído se cotejaron con `scripts/curriculo.py`, los 18 módulos y el estado anual. Las 10 capacidades H1–H6/G1–G4 reproducen literalmente el texto aportado, comprobación necesaria pero insuficiente: se verificó además el vínculo de tareas y evaluaciones.

| Encuentros | Núcleo curricular y alcance |
|---|---|
|1|Introducción editorial de Historia/Geografía, fuentes, cronología y mapas; no se le atribuye una capacidad MEC inexistente.|
|2–5|H1: prehistoria paraguaya, formas de vida, regiones, pueblos, organización guaraní y fuentes; U1=23 puntos H1 pertinentes al contenido.|
|6–9|H2: poblamiento americano, teorías y civilizaciones; mapas y cronologías como herramientas. U2=22 puntos H2. BI-01 perjudica una práctica de esa capacidad.|
|10–11|H4: avances y llegada europea, efectos y reparto/gobierno; nombres y fechas son selección didáctica dentro del tema.|
|12–16|H3: conquista y sociedad paraguaya del XVI, Asunción, instituciones, autonomía colonial limitada y resistencia.|
|17|U3: H3=18/H4=7; ya no se etiqueta indiscriminadamente H1.|
|18|Integradora H1–H4 efectiva; cobertura demostrada y puntaje compartido pendiente de desagregar COM-01.|

La relación capacidad–indicador–contenido–actividad es defendible: preguntas de fuentes exigen evidencia y límites; mapas no se usan como adorno; desarrollo exige causas y no solo fechas. «Investiga» H3 se trabaja mediante documentos y contraste guiado apropiado al nivel, aunque podría ampliarse con consultas opcionales supervisadas. No se atribuyen al MEC, como literal, nombres de personajes seleccionados por la editorial. H5/H6 y G1–G4 todavía no desarrolladas se registran como futuras, no como incumplimiento de los primeros 18 encuentros.

## Factibilidad de los 120 minutos

Los 18 planes suman 120 minutos sin huecos ni superposición. Se revisaron productos, lectura, escritura, agrupamiento, apoyos y consolidación; la suma aritmética por sí sola no demuestra factibilidad. La estimación presume fichas ya fotocopiadas y materiales listos, sin transcribir en el pizarrón textos largos.

| Encuentro | Carga examinada | Juicio de factibilidad |
| --- | --- | --- |
| 1 | Lectura guiada, fuente breve, cronología y orientación | Viable con lectura acompañada; se distingue trabajo en cuaderno. |
| 2 | Comparación de sociedades, fuente censal, cuadro y cierre | Viable; las fechas aproximadas no exigen memorización exhaustiva. |
| 3 | Parentesco, mapa, fuente y legado lingüístico | Viable si consolidación se selecciona; vocabulario guaraní explicado. |
| 4 | Cuatro fuentes y matriz en grupos con roles | Viable con reparto de lectura y ejemplo; no pedir copia de todas las fuentes. |
| 5 | U1: 70 min+15, cierre sin claves | Viable; claves recién cuando toda prueba está custodiada/entregada. |
| 6 | 20 min devolución U1 y 100 min nueva clase | Ajustado pero plausible: priorizar fuente/ruta y llevar consolidación al hogar. |
| 7 | Tres civilizaciones, cuadro y fuente | Viable con cuadro preparado y lectura en parejas; evitar copiar todo. |
| 8 | Mapa esencial 20–50, cronología y revisión | No ejecutable íntegramente por BI-01; resolver encuadre antes de validar tiempos. |
| 9 | U2: 70 min+15 y reflexión sin claves | Viable con mapa impreso y devoluciones diferidas. |
| 10 | Devolución U2 de 0–20 y avances/viajes en 100 | Viable con esenciales seleccionadas; devolución sí incluida. |
| 11 | Tordesillas, instituciones y fuente colonial | Viable mediante esquema preparado y comparación guiada. |
| 12 | Rutas regionales, fuente y centralidad Asunción | Viable con apoyo de color/trazado, sin exigir itinerario exacto. |
| 13 | Mapa 28 min, comparación 20 min, causalidad y revisión | Ajustado pero viable en parejas; no añadir copia completa del contenido. |
| 14 | Parentesco, resistencia, fuente 20 min y cierre 22 min | Viable; tratar violencia con respeto y sin detalles innecesarios. |
| 15 | Fuente 33–48, cronología 48–60, instituciones 76–96 | Mejora N02: 12 min para ordenar; consolidación 5,8,9,10 en casa, revisión al abrir 16. |
| 16 | Facultades, evidencia y comparación 1537/actualidad | Viable con cuadros y rúbrica explícita; uso de fuentes ya conocidas. |
| 17 | U3: 70 min+15 y cierre sin claves | Viable; resolver eventual prórroga excepcional antes de devolución 18. |
| 18 | Devolución 0–20; encuadre 20–30; prueba 30–100; extra 100–115; cierre 115–120 | Viable con clave corregida BII-01 y lectura silenciosa disponible; Plan 19 debe reservar 20 min de devolución. |

Los apoyos incluyen lectura oral de consignas sin explicar respuestas, roles lector/secretario/portavoz, puntos de mapa previamente señalados y consolidación para ritmos rápidos. No se exige que todo el tomo se complete presencialmente. Fichas A/B/C y cuaderno resuelven la mayor parte del espacio de respuesta; la imposibilidad de la Ficha B-1 no se corrige dando más tiempo.

## Comprobaciones independientes y límites de los verificadores

Se inspeccionaron `verificar.py`, los informes del productor y las salidas JSON. El verificador comprueba correspondencias, presencia de actividades,120 min, literales, opciones distintas, puntajes y algunas condiciones visuales. Su propio encabezado reconoce que no reemplaza revisión histórica/geográfica. No se reejecutó el programa completo porque esta instalación no tiene Py Mu PDF; no se alteró ni reconstruyó el entorno de producción para aparentar el mismo resultado.

Se ejecutaron 85 pruebas independientes: **83 correctas y 2 fallos**, ambos de encuadre de Beringia/Monte Verde. Incluyen 10 literales,18 secuencias de 120 min,18 correspondencias de ítems/respuestas,4 sumas de matriz,26 claves contra opciones,4 controles de opciones distintas y 5 localizaciones en ficha. Además se compararon 140 pares PDF y se revisaron límites de caracteres: 0 fuera de la página en 280 páginas. Esto no equivale a ausencia de filas mal dimensionadas; las tablas se inspeccionaron visualmente.

Los 2 defectos mayores pasan los controles del productor porque tener archivo de mapa y respuesta no garantiza que el punto entre en el mapa, y tener rúbrica coincidente no valida la fecha del ejemplo. Añadir: prueba de encuadre por cada lugar pedido, y control temporal consigna–ejemplo–rúbrica; revisión humana sigue necesaria.

## Estado respecto de Muestra 3

| Condición heredada | Resultado independiente actual |
|---|---|
|A19/N04, dos fragmentos 1537|Parcial: referencia completa, pero segundo fragmento no literal BII-02.|
|N02, Plan 15|Resuelta en diseño: tramo 48–60 de 12 min y consolidación domiciliaria; falta validación real en aula.|
|A10/N03, equidad|Aplicada en 5,9,17,18; devoluciones 6,10,18 previstas; encuentro 19 pendiente obligatorio.|
|A14, remanentes|Parcial: buena separación de fichas, persisten algunos remanentes breves COM-03.|
|A17, cartografía|Cinco escalas mejoradas sin desplazamientos; legibilidad digital aceptable; defecto nuevo funcional BI-01 en otro mapa.|
|A05/N05, núcleo XVII en 22|Condición futura obligatoria, no evaluable como material producido aquí.|
|N01, acuífero Patiño/río|Condición futura del 28; no afirmar corrección comprobada en estos bloques.|

## Registro de revisión página por página

Páginas físicas, contando portada. «Sin incidencia» significa sin defecto visual relevante en la inspección digital, no certificación física de imprenta. Las observaciones de cada página se aplican también al PDF liviano de igual paginación y contenido; las 28 páginas con compresión distinta se comprobaron por separado.

### TOMO_BLOQUE_I_oficio.pdf

| Página | Revisión visual/pedagógica |
| --- | --- |
| 1 | Portada: imagen y banda completas; título legible. |
| 2 | Presentación y diagnóstico: jerarquía clara; renglones útiles. |
| 3 | Índice: entradas y números legibles, sin invasión del pie. |
| 4 | Clase 1: ficha de propósito editorial y texto de Historia legibles. |
| 5 | Historia/Geografía, tabla y fuentes: columnas íntegras; esquema legible. |
| 6 | Fuente constitucional y cronología: recuadro con espacio; explica ausencia de año 0 (contrastar BI-02). |
| 7 | Herramientas y mapa de orientación: escala corregida, ríos y ciudades íntegros. |
| 8 | Aplicación de Clase 1: opciones y numeración claras; no cortes de letras. |
| 9 | Línea personal y fundamentación: espacio adecuado para cuaderno; cierre limpio. |
| 10 | Clase 2: capacidad H1, texto y cronología regional con fechas aproximadas; no se atribuye certeza a sitios paraguayos sin fechar. |
| 11 | Cazadores y formaciones tribales: contraste comprensible; cuadro sin filas cortadas. |
| 12 | Regiones: mapa íntegro, escala separada; evita identificar cada región con un único modo de vida. |
| 13 | Fuente censal 2012: fecha y cinco familias visibles; no presentada como censo 2026. |
| 14 | Aplicación y desarrollo: consignas completas y respuestas remitidas al cuaderno. |
| 15 | Clase 3: H1 y organización guaraní; inicio legible. |
| 16 | Esquema y área guaraní: títulos, leyenda y escala íntegros; geografía expresamente aproximada. |
| 17 | Agricultura y fuente de Schmidl: adaptación reconocible; bibliografía necesita localizador (COM-02). |
| 18 | Legado, lengua y actividades: contraste de fuentes; uso actual sin convertir pueblos actuales en fósiles. |
| 19 | Fundamentación de parentesco/mujeres: criterios explícitos y cierre de sección legible. |
| 20 | Continuación A: objetivos del taller y funciones visibles; no repite una clase expositiva. |
| 21 | Cuatro fuentes: soportes y épocas comparables; síntesis arqueológica sin bibliografía precisa (COM-02). |
| 22 | Consignas del taller: evidencia y límite diferenciados; respuestas se preparan para la ficha. |
| 23 | Ficha A: matriz reproducible independiente; casillas y ejemplo permiten escribir. |
| 24 | U1: datos, tiempo, puntaje y partes A/B claros; opciones completas. |
| 25 | U1 mapa y fuente: espacio utilizable para cuatro elementos; escala corregida; renglones legibles. |
| 26 | U1 desarrollo: seis–ocho líneas y cinco criterios anunciados; espacio suficiente. |
| 27 | Clase 4: H2 y teorías clásicas diferenciadas de explicación actual. |
| 28 | Pre-Clovis y mapa continental: rutas aproximadas; actualización White Sands pendiente BI-03. |
| 29 | Fuente de sitios/fechas y F1–F3: lectura posible; actualizar contexto científico BI-03. |
| 30 | Aplicación Clase 4: instrucciones y fundamentación completas; criterio no oculto. |
| 31 | Clase 5: mapa de civilizaciones íntegro y leyenda fuera del área de datos. |
| 32 | Cronología, mayas y mexicas: tipografía legible; origen 0 requiere aclaración BI-02. |
| 33 | Incas y Cortés: fuente modernizada declarada; cifra del mercado se atribuye al conquistador, no a un censo. |
| 34 | Aplicación Clase 5: opciones, cuadro y desarrollo legibles. |
| 35 | Continuación B: propósito y comparación de duraciones claros. |
| 36 | Taller B consigna 1 pide Beringia y Monte Verde fuera de ficha: BI-01. |
| 37 | Ficha B-1: buena superficie de escritura y leyenda vacía, pero encuadre impide dos respuestas esenciales BI-01. |
| 38 | Ficha B-2: blanco funcional para trazar cuatro bandas; eje d.C. con 0: BI-02. |
| 39 | U2: datos,70 min y 22 puntos; partes A/B completas. |
| 40 | U2 mapa/cuadro: tres ciudades en encuadre; casillas y puntuación parcial explícitas. |
| 41 | U2 desarrollo: cinco criterios y renglones suficientes; inferencia del modelo docente pendiente BI-04. |

### TOMO_BLOQUE_II_oficio.pdf

| Página | Revisión visual/pedagógica |
| --- | --- |
| 1 | Portada íntegra; título y pie 2026 legibles. |
| 2 | Presentación/diagnóstico: organización clara; no exige contenido todavía no enseñado como nota sumativa. |
| 3 | Índice: numeración y jerarquías legibles. |
| 4 | Clase 6: ficha H4, avances náuticos y esquema legibles. |
| 5 | Viajes: rutas aproximadas y leyenda completas; cuadro de consecuencias sin cortes. |
| 6 | Colón: versión modernizada y mediación de Las Casas declaradas; preguntas permiten criticar perspectiva. |
| 7 | Aplicación Clase 6: opciones y V/F claros; espacios acordes al cuaderno. |
| 8 | Posición sobre descubrimiento/encuentro: criterios anunciados; no se impone una sola etiqueta. |
| 9 | Clase 7: Tordesillas,370 leguas y línea aproximada; Castilla oeste y Portugal este correctos. |
| 10 | Absolutismo y gobierno: esquema legible; simplificación declarada. No confundir con administración contemporánea. |
| 11 | Colonialismo/Requerimiento: síntesis escolar reconocida; falta edición docente verificable COM-02. |
| 12 | Aplicación Clase 7: comparación con actualidad y criterios visibles. |
| 13 | Clase 8: H3, expediciones y conquista regional comprensibles. |
| 14 | Mapa Río Plata y cronología: ríos y fechas legibles; rutas declaradas aproximadas. |
| 15 | Asunción y fuente: se explica alianza desigual y alimentos; no presenta conquista como acuerdo pacífico general. |
| 16 | Aplicación Clase 8: fechas, causalidad y párrafo con criterios visibles. |
| 17 | Continuación C: taller de rutas/decisiones con propósito claro. |
| 18 | Consignas C: puntos y recorridos pedidos contenidos en Ficha C; tabla permite comparar. |
| 19 | Revisión entre pares: criterios útiles; la ficha continúa en hoja siguiente con encabezado completo. |
| 20 | Ficha C: mapa de tamaño suficiente, leyenda vacía y título; Santa Catalina/Asunción/Buenos Aires incluidos. |
| 21 | Clase 9: parentesco, reciprocidad desigual y mestizaje; esquema social legible y simplificado. |
| 22 | Encomienda/resistencia: exposición respetuosa de violencia; precisar ciclo Aracaré/Tabaré 1542–1543 BII-03. |
| 23 | Testamento 1556: resumen declarado no textual, coherente en hechos; referencia de edición pendiente COM-02. |
| 24 | Aplicación Clase 9: consignas y comparación de formas de resistencia claras. |
| 25 | Clase 10: H3, autonomía provisional y no independencia; tabla inicial legible. |
| 26 | Real Provisión y cronología: buena superficie de respuesta; segundo fragmento no literal BII-02. |
| 27 | Comparación electoral y gobierno: encomienda expresamente no gubernamental; esquema legible. |
| 28 | Obispado, encomienda y actividades: 1547/1556 diferenciados; tipos de trabajo explicados. |
| 29 | Aplicación Clase 10: opciones y desarrollo completos; rúbrica anunciada. |
| 30 | Actividades 16–17: espacio/criterios explícitos; consolidación al hogar según Plan 15. |
| 31 | Continuación D: 1537–1544 y revisión de autonomía con límites. |
| 32 | Cuadro de facultades y fuentes: casillas suficientes; no convierte excepción en democracia actual. |
| 33 | Párrafo comparativo y autoevaluación: extensión y criterio claros; cierre funcional. |
| 34 | U3: 70 min/25 puntos; selección y V/F íntegros. |
| 35 | U3 mapa y encomienda: tres puntos resolubles; tabla y criterios parciales visibles. |
| 36 | U3 desarrollo y consecuencias: rúbrica comunicada y espacio suficiente. |
| 37 | Integradora: 70 min/28 puntos; ocho opciones y cuatro V/F legibles; Oberá exige lectura histórica contextual. |
| 38 | Integradora: línea/cuadro/desarrollo con criterios visibles; discrepancia temporal en clave BII-01. |
| 39 | Autoevaluación sin nota: blanco inferior amplio pero funcional; compactación opcional COM-03. |

### PLANES_BLOQUE_I_A4.pdf

| Página | Revisión visual/pedagógica |
| --- | --- |
| 1 | Portada A4: denominación, bloque y referencia al MEC legibles. |
| 2 | Índice: nueveplanes y páginas coherentes. |
| 3 | Plan 1: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Viable con lectura acompañada; se distingue trabajo en cuaderno. |
| 4 | Plan 1: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. |
| 5 | Plan 2: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Viable; las fechas aproximadas no exigen memorización exhaustiva. |
| 6 | Plan 2: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. |
| 7 | Plan 3: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Viable si consolidación se selecciona; vocabulario guaraní explicado. |
| 8 | Plan 3: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. |
| 9 | Plan 4: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Viable con reparto de lectura y ejemplo; no pedir copia de todas las fuentes. |
| 10 | Plan 4: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. Remanente corto a compactar si no afecta letra ni función (COM-03). |
| 11 | Plan 5: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Viable; claves recién cuando toda prueba está custodiada/entregada. |
| 12 | Plan 5: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. Tiempo excepcional custodiado y sin claves simultáneas explícito. |
| 13 | Plan 6: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Ajustado pero plausible: priorizar fuente/ruta y llevar consolidación al hogar. |
| 14 | Plan 6: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. |
| 15 | Plan 7: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Viable con cuadro preparado y lectura en parejas; evitar copiar todo. |
| 16 | Plan 7: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. Remanente corto a compactar si no afecta letra ni función (COM-03). |
| 17 | Plan 8: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. No ejecutable íntegramente por BI-01; resolver encuadre antes de validar tiempos. |
| 18 | Plan 8: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. Remanente corto a compactar si no afecta letra ni función (COM-03). |
| 19 | Plan 9: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Viable con mapa impreso y devoluciones diferidas. |
| 20 | Plan 9: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. Remanente corto a compactar si no afecta letra ni función (COM-03). Tiempo excepcional custodiado y sin claves simultáneas explícito. |

### PLANES_BLOQUE_II_A4.pdf

| Página | Revisión visual/pedagógica |
| --- | --- |
| 1 | Portada A4: denominación, bloque y referencia al MEC legibles. |
| 2 | Índice: nueveplanes y páginas coherentes. |
| 3 | Plan 10: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Viable con esenciales seleccionadas; devolución sí incluida. |
| 4 | Plan 10: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. |
| 5 | Plan 11: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Viable mediante esquema preparado y comparación guiada. |
| 6 | Plan 11: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. |
| 7 | Plan 12: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Viable con apoyo de color/trazado, sin exigir itinerario exacto. |
| 8 | Plan 12: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. Remanente corto a compactar si no afecta letra ni función (COM-03). |
| 9 | Plan 13: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Ajustado pero viable en parejas; no añadir copia completa del contenido. |
| 10 | Plan 13: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. |
| 11 | Plan 14: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Viable; tratar violencia con respeto y sin detalles innecesarios. |
| 12 | Plan 14: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. |
| 13 | Plan 15: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Mejora N02: 12 min para ordenar; consolidación 5,8,9,10 en casa, revisión al abrir 16. |
| 14 | Plan 15: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. Cronología 48–60 y consolidación al hogar resuelven N02. |
| 15 | Plan 16: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Viable con cuadros y rúbrica explícita; uso de fuentes ya conocidas. |
| 16 | Plan 16: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. |
| 17 | Plan 17: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Viable; resolver eventual prórroga excepcional antes de devolución 18. |
| 18 | Plan 17: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. Remanente corto a compactar si no afecta letra ni función (COM-03). Tiempo excepcional custodiado y sin claves simultáneas explícito. |
| 19 | Plan 18: ficha, capacidad/vínculo, indicadores y primera secuencia; filas legibles. Viable con clave corregida BII-01 y lectura silenciosa disponible; Plan 19 debe reservar 20 min de devolución. |
| 20 | Plan 18: Continuación de tabla con encabezado; cierre, diversidad y tarea legibles. Remanente corto a compactar si no afecta letra ni función (COM-03). Tiempo excepcional custodiado y sin claves simultáneas explícito. |

### SOLUCIONARIO_BLOQUE_I_A4.pdf

| Página | Revisión visual/pedagógica |
| --- | --- |
| 1 | Clase 1: tablas de respuestas, fuente constitucional y U orientación completas; sin texto cortado. |
| 2 | Cierre Clase 1 y Clase 2: ejemplos y criterios legibles; respuestas coherentes con tomo. |
| 3 | Cierre Clase 2 y Clase 3: organización guaraní, parcialidades y fuente identificables. |
| 4 | Clase 3 y taller A: evidencia/límite diferenciados; tabla admite lectura; COM-02 bibliografía. |
| 5 | U1: claves A/B y rúbricas C–E concordantes; 23 puntos. |
| 6 | Clavecartográfica U1 y matriz completas; abre Clase 4; White Sands requiere BI-03. |
| 7 | Clase 4: ubicaciones y respuestas; BI-03 actualización; resto de tabla legible. |
| 8 | Clase 5 y taller B: respuestas suficientes; corregir encuadre BI-01 y año 0 BI-02. |
| 9 | Taller B y U2: 22 puntos; inferencia del ítem 13 requiere BI-04. |
| 10 | Clavecartográfica U2 y matriz H2: filas y leyendas legibles, no recortes. |

### SOLUCIONARIO_BLOQUE_II_A4.pdf

| Página | Revisión visual/pedagógica |
| --- | --- |
| 1 | Clase 6: claves, fuente y mapa; respuestas y criterios dentro de tabla. |
| 2 | Clase 6/7: posiciones razonadas aceptadas; instituciones y fuente legibles. |
| 3 | Clase 7/8: tabla íntegra; cronología y mapa vinculados a enseñanza. |
| 4 | Continuación C: recorridos/decisiones y criterios; respuestas suficientes. |
| 5 | Clase 9 y apertura Clase 10: revisar precisión Tabaré BII-03; tablas legibles. |
| 6 | Clase 10: fuente, Cabildo y cronología; distinguir clave conceptual correcta y cita no literal BII-02. |
| 7 | Continuación D y U3: casillas y criterios completos; autonomía con límites. |
| 8 | U3: rúbricas, mapa gráfico y comienzo de matriz íntegros; 25 puntos. |
| 9 | Finmatriz U3 e integradora A–D: 28 puntos previstos; separar autoridad/trabajo BII-04. |
| 10 | Integradora E/F y matriz: modelo 15 fuera de período BII-01; pesos compartidos COM-01; sin recorte visual. |

## Fuentes consultadas y localizadores

Las referencias siguientes sustentan los contrastes indicados; no sustituyen el manifiesto de archivos de origen. Consulta 15/10/2026.

1. MEC, *Programa de Estudio, Historia y Geografía,7.º grado*,2014, PDF aportado al proyecto y extracción textual en `datos/`; identidad en manifiesto. No se infiere equivalencia de códigos editoriales y códigos oficiales.
2. [Rivarola Paoli, capítulo y nota 105 en Portal Guaraní](https://www.portalguarani.com/1067_juan_bautista_rivarola_paoli__/12674_la_cedula_real_del_12_de_setiembre_de_1537_por_juan_bautista_rivarola_paoli_.html): cotejo literal de ambos segmentos de 1537.
3. [Roulet 1990, ficha académica UNAM](https://repositorio.unam.mx/contenidos/5054882): título, año, revista, páginas y ciclo 1542/43; acceso al artículo completo no logrado. No se atribuye lectura integral.
4. [Melià, *El guaraní conquistado y reducido*, escaneo en Acervo Socioambiental](https://acervo.socioambiental.org/sites/default/files/documents/gml00001.pdf), capítulo Oberá pp 31–40: consulta directa del escaneo descargado, Guarambaré 1579 y carácter profético; también testimonio bélico colonial.
5. [De Gandía, *El testamento de Domingo Martínez de Irala*, repositorio UBA](https://repositoriouba.sisbi.uba.ar/gsdl/collect/bolravi3/index/assoc/bihaar_1/_n043_04/4-5-biha/ar_1_n04.dir/bihaar_1_n043_044-04-ap054_077ao.pdf), pp 54–77, especialmente 74–75. La copia institucional permite comprobar el resumen escolar; no se inventa año de edición del artículo.
6. [Diario del primer viaje, Biblioteca Virtual Miguelde Cervantes](https://www.cervantesvirtual.com/s3/BVMC_OBRAS/ff8/3a3/be8/2b1/11d/fac/c70/021/85c/e60/64/mimes/ff83a3be-82b1-11df-acc7-002185ce6064_4.html), entrada 11–12 octubre 1492, p 31.
7. [Tratado de Tordesillas, registro PARES](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/autoridad/100803),7/06/1494,370 leguas; [ratificación documental](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/121026).
8. [Pigati etal 2023, publicación científica USGS](https://www.usgs.gov/publications/independent-age-estimates-resolve-controversy-ancient-human-footprints-white-sands), *Science*, DOI10.1126/science.adh 5007: polen terrestre y luminiscencia como corroboración independiente. [Sitio institucional White Sands,NPS](https://www.nps.gov/whsa/learn/nature/fossilized-footprints.htm), actualización 5/08/2026.
9. [INE, resultados Censo Indígena 2012](https://www.ine.gov.py/Publicaciones/Biblioteca/indigena2012/Pueblos%20indigenas%20en%20el%20Paraguay%20Resultados%20Finales%20de%20Poblacion%20y%20Viviendas%202012.pdf), apartado 2.2 familias y pueblos; fuente fechada pertinente para lectura escolar.
10. [Constitución Nacional, edición Cámarade Diputados](https://www.diputados.gov.py/pdf/ConstitucionNacional_2024.pdf), artículo 140; cotejo de fuente reproducida, no asesoría jurídica.
11. [Cortés, extracto Primario difundido por UNAM/Noticonquista](https://www.noticonquista.unam.mx/listado-historicas/1838/1838): descripción del mercado en Segunda Carta 1520. [Testimonio sobre Requerimiento y Palacios Rubios, BVMC](https://www.cervantesvirtual.com/obra-visor/vidas-de-los-espanoles-celebres--0/html/fee59b24-82b1-11df-acc7-002185ce6064_80.htm): consulta como contraste de atribución; falta en el libro una edición precisa propia de ese resumen.

## Publicación e integridad

Se publica en carpeta separada de control: [AUDITORIA_BLOQUES_I_II_2026_10](https://drive.google.com/drive/folders/1NBbYcUP-qs2Pfme29q-weR_Mvbo20c8w), con [evidenciasvisuales](https://drive.google.com/drive/folders/1vN9WNo2oTIAvm8JzFYDIpO3ee9kTG4CP). Copia técnica en rama independiente `codex/auditoria-bloques-i-ii-ea3cf5f`, carpeta `historia_geografia_7/auditorias/AUDITORIA_BLOQUES_I_II/`. La verificación final separada registra el commit de publicación, enlaces, tamaños remotos y hashes; se separa para no crear una autorreferencia circular en el manifiesto.

El paquete contiene este dictamen,CSV,PDF ejecutivo,control de 57 ítems,comparación de 5 mapas,manifiesto y evidencias seleccionadas. Las 280 páginas renderizadas se usaron en el trabajo local; se publican las imágenes relevantes, no se duplican los libros ni se suben versiones comerciales nuevas. No se modificó ningún documento maestro ni carpeta comercial.
