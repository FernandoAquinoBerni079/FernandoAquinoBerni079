# Historia y Geografía 7.º: segunda muestra (contenido corregido y ampliado)

**Fecha:** 14 de octubre de 2026.

**Roles:** Claude edita, ChatGPT audita y Fernando aprueba.

**Estado:** muestra para revisión. No se construyeron los seis archivos comerciales, no se modificó ningún maestro y no se subió nada a las carpetas comerciales de Drive. No se declara apto ningún material.

## 1. Maestro del 3 de octubre

**Recuperación:**
- Las diez partes de la carpeta de ChatGPT se descargaron y verificaron una por una contra el `MANIFIESTO_SHA256.json`: las diez coinciden.
- El DOCX reconstruido tiene 27.294.901 bytes y SHA-256 `8dbc4f4480e7aa80e631fabcb8b5b6a210eb02204d881769599c2d435b179413`, igual al del manifiesto.

**Comparación con el DOCX de la rama usado en el primer piloto:**
- Mismas 1.740 piezas del cuerpo y mismo texto.
- Mismas 26 imágenes, byte a byte.
- Solo cambian los números de página del índice estático.

Desde esta muestra, la base es el maestro. El original de Drive no se tocó.

## 2. Programa del MEC

**Archivo provisto por Fernando:** *Programa de Estudio: Historia y Geografía, 7.º grado, Educación Escolar Básica*, MEC 2014.
- Ficha catalográfica en la pág. 2; autoridades: Cartes, Lafuente, Mello, Pereira de Jacquet y Giménez Sivulec.
- 92 págs.; SHA-256 `389190d3…c8d27e`.
- Copia en `datos/`, con el texto extraído.
- Es una reproducción hecha con Word en 2022, no el impreso. Por eso el cotejo se informa como **literal contra esta reproducción**. Para declararlo cotejado oficialmente falta el PDF o el ejemplar oficial.

**Lo que confirma:**
- **Carga horaria:** 3 horas semanales de **40 minutos** (pág. 46: «El tiempo estimado hace referencia a horas cátedras de 40 minutos»). Cada encuentro de 3 HC dura 120 minutos.
- **Capacidades:** dos unidades temáticas con 10 capacidades (págs. 55 a 57), transcriptas en la matriz.

**Cotejo de las 36 fichas del maestro:**

| Estado | Secciones |
|---|---|
| Literal | 15 (Clases 2 a 15 y Continuación B) |
| Truncada | 5 (Clases 16, 17, 18, 20 y 21) |
| Abreviada | 1 (Clase 19) |
| Editorial o variante | 6 (Clase 1 y Continuaciones A, D, E, F y G) |
| Sin ficha | Las 8 evaluaciones |

El detalle está en `datos/cotejo_capacidades.json` y en la matriz.

**Correcciones a mi diagnóstico del 14/10 (`01_diagnostico/DIAGNOSTICO.md`, §4):**
- **Clase 21.** Su capacidad («Describe las características de las regiones naturales…») sí es la del programa: la «Gestión ambiental desarrollada por el Estado paraguayo» figura como tema de esa capacidad. Lo que hay que corregir es que está truncada (le falta «de Paraguay y América»).
- **Clase 10.** El título «El derecho a la autonomía» toma la formulación literal del programa («Ejercicio del derecho a la autonomía»). La muestra conserva esa expresión en la ficha y la explica con su contexto, en lugar de eliminarla.

**Lo que no se pudo usar:** las direcciones de Scribd, del CONACYT y de mec.gov.py. La red del entorno las bloquea.

## 3. Qué tiene la muestra

**Secciones del tomo:**
- Clase 10 (Historia).
- Clase 18 (Geografía).
- Continuación F.
- Evaluación de la Unidad 5.
- Fichas reproducibles 18-A, F-A, F-B y F-C.

**Documentos que las acompañan:**
- Planes 15, 28, 29 y 30.
- Respuestas de las cuatro secciones.
- Matriz curricular de los 36 encuentros.
- Plan anual en oficio horizontal, segunda versión (solo maqueta).

| Archivo | Págs. | Formato |
|---|---|---|
| `tomo/TOMO_MUESTRA2_oficio.docx` / `.pdf` | 26 | Oficio, variante B: márgenes de 2 cm, cuerpo de 11,5 pt |
| `planes/PLANES_MUESTRA2_A4.docx` / `.pdf` | 10 | A4 vertical, márgenes de 2 cm, 10 a 10,5 pt |
| `solucionario/SOLUCIONARIO_MUESTRA2_A4.docx` / `.pdf` | 5 | A4 vertical, 10 a 10,5 pt |
| `matriz/MATRIZ_CURRICULAR_36_ENCUENTROS.docx` / `.pdf` | 7 | A4 horizontal |
| `plan_anual/PLAN_ANUAL_OFICIO_v2.docx` / `.pdf` | 8 | Oficio horizontal, 10 pt |
| `revision_liviana/*_REVISION.pdf` | — | Las mismas páginas, con imágenes reducidas para la revisión visual. El tomo pasa de 2,4 MB a 0,96 MB. |

**Páginas del tomo:**
- Portada, presentación e índice: págs. 1 a 3. El índice lleva números reales, estables en dos pasadas.
- Clase 10: págs. 4 a 10.
- Clase 18: págs. 11 a 16.
- Ficha 18-A: pág. 17.
- Continuación F: págs. 18 a 20.
- Fichas F-A, F-B y F-C: págs. 21 a 23.
- Evaluación U5: págs. 24 a 26.

Cada sección y cada ficha empieza en hoja nueva.

## 4. Correcciones y ampliaciones, por prioridad del pedido

| Prioridad | Estado en esta muestra |
|---|---|
| Real Provisión de 1537 | **Corregida en el tomo y en el solucionario.** Clase 10: <ul><li>contexto de 1534 a 1556 (Mendoza, Ayolas, fundación de Asunción);</li><li>fecha, lugar y firmantes;</li><li>llegada de Cabrera;</li><li>las tres condiciones de la elección;</li><li>dos fragmentos documentales con su referencia;</li><li>uso en 1539 (Irala) y en 1544 (Cabeza de Vaca);</li><li>cuadro «Elegir en 1537 y elegir hoy».</li></ul> Se eliminó la pregunta sobre un historiador sin identificar que la llamó «carta constitucional». El solucionario ya no dice que «el poder viene del pueblo». |
| Colonización de los siglos XVI y XVII | **Parcial, en la Clase 10:** <ul><li>esquema de autoridades (rey, Consejo de Indias, Virrey del Perú, Audiencia de Charcas, gobernador, Cabildo);</li><li>tipos de cabildo;</li><li>Obispado (1547);</li><li>tipos de encomienda (originaria y mitaya);</li><li>Leyes Nuevas;</li><li>reparto de 1556.</li></ul> Los siglos XVI y XVII en las Clases 8, 11, 12 y 13 quedan para la aplicación al año (matriz). |
| Hidrografía de Paraguay y América | **Ampliada en la Clase 18:** <ul><li>cuencas y vertientes;</li><li>el río Paraguay como límite, con su recorrido real;</li><li>afluentes por margen;</li><li>Paraná y Pilcomayo;</li><li>lagos, esteros, Pantanal y acuíferos (Guaraní y Patiño);</li><li>impactos de Itaipú;</li><li>hidrografía de América.</li></ul> Incluye dos mapas nuevos y la Ficha 18-A. |
| Planes 27 y 28 | **El 28 está reescrito** sobre la nueva Clase 18. La corrección del 27 (Tema e Indicadores de la ficha de la Clase 17) está definida en el diagnóstico y se aplica con el año completo. |
| Evaluaciones incompletas | **La Evaluación U5 está reescrita:** <ul><li>14 ítems en seis partes, 28 puntos y 70 minutos;</li><li>incluye mapa, fuente cartográfica, matriz de impactos y desarrollo;</li><li>en el solucionario: clave y rúbrica.</li></ul> La Parte C, antes un agregado del docente, ahora está en el tomo. |
| Opciones con varias respuestas y claves predecibles | **En las 18 opciones múltiples de la muestra:** <ul><li>una sola respuesta correcta en cada una;</li><li>distractores plausibles;</li><li>claves repartidas: a 5, b 5, c 5, d 3.</li></ul> |
| Clima de Paraguay y América (Clase 19), chinampas (Clase 5), Clase 6 y su fuente | **Fuera de esta muestra**, porque el pedido era una clase de Historia, una de Geografía, una continuación y una evaluación. Están en la matriz con la corrección prevista. |

**Criterios aplicados:**
- **Fuentes.** No se inventaron fuentes, citas, estadísticas ni mapas:
  - los fragmentos de la Real Provisión llevan la referencia de la transcripción de la que salen;
  - el caso de la Ficha F-A está rotulado como ficticio y no tiene cifras.
- **Mapas.** Se hicieron con geometrías de Natural Earth (dominio público), como las Figuras 4.1 y 20.1 del maestro. En esos datos el río Paraguay figura rotulado «Paraná»; aquí cada tramo se rotula según su ubicación. Natural Earth no trae el Apa ni los lagos Ypacaraí e Ypoá, así que no se dibujaron: el texto los nombra y el plan lo advierte.
- **Ilustraciones originales.** Se conservan las Figuras 10.1 y 18.1. La 10.1 tiene un título incorrecto dentro de la imagen («Las instituciones que gobernaban la colonia» incluye la encomienda). El epígrafe lo aclara y la clase propone compararla con el esquema correcto (Figura 10.2). Fernando decide si se reemplaza.

## 5. Datos que la auditoría debe cotejar antes de imprimir

| Sección | Dato | Qué hacer |
|---|---|---|
| Clase 10 | Fragmentos de la Real Provisión | Son dos transcripciones distintas (Rivarola Paoli; portal del MEC), citadas por separado y con su ortografía. Cotejar con una edición documental. |
| Clase 10 | Capitulación de Mendoza (1534), fundación de Buenos Aires (1536) y muerte de Mendoza en el viaje de regreso (1537) | Cotejar las fechas exactas si se agregan días. |
| Clase 10 | Llegada de Alonso Cabrera (1538) y reconocimiento de Irala como gobernador (1539) | Cotejar el año del reconocimiento con bibliografía paraguaya. |
| Clase 10 | Cabildo de Asunción (1541), Obispado (1547; primer obispo en 1556), Audiencia de Charcas (1559), Virreinato del Perú (1542) | Cotejar. |
| Clase 10 | Tipos de encomienda (originaria o de yanaconas; mitaya) y reparto de 1556 | Cotejar. |
| Clase 18 | Afluentes por margen; Acaray, Monday y Ñacunday; central del Acaray | Cotejar con un atlas del Paraguay (IGM o INE). |
| Clase 18 | Pilcomayo: cauce cambiante y caudal que en algunos años no llega a la desembocadura | Cotejar con bibliografía sobre la cuenca del Pilcomayo. |
| Clase 18 | Acuerdo de transporte fluvial de 1992 y extremos Cáceres-Nueva Palmira | Cotejar el texto del acuerdo. |
| Clase 18 | Titicaca a más de 3.800 m; la Cuenca del Plata es la segunda de América del Sur | Cotejar. |
| Mapas | Geometrías de Natural Earth; ciudades, represas y puertos en posición aproximada | Ver §4 (rótulo del río Paraguay; Apa, Ypacaraí e Ypoá sin dibujar). |

**Cómo se verificaron:**
- Los fragmentos de la Real Provisión y su contexto se contrastaron con los resultados de búsqueda (Portal Guaraní; portal del MEC), que confirman, entre otras cosas, el pasaje «según Dios y sus conciencias».
- No se pudo abrir el texto completo de esas páginas: el entorno solo accede a la búsqueda web.
- Las fechas y los datos geográficos son de manual. Igual se listan para que la auditoría los coteje.

## 6. Coherencia entre documentos

`scripts/verificar_muestra2.py` da **24 controles correctos y 0 fallos**:
- Las capacidades usadas figuran literalmente en el texto del programa.
- Cada ítem del tomo tiene su respuesta con el mismo número, y no hay respuestas sin ítem.
- Cada plan asigna todas las actividades de su sección, en clase o como tarea, y no cita actividades inexistentes.
- Las figuras y fichas que citan los planes existen en el tomo.
- Las claves están repartidas.

**Revisión visual:** hice una revisión visual completa del PDF, que corrigió tres defectos:
- renglones que se separaban de su recuadro;
- consignas que quedaban solas al pie de la página;
- cuadros sin bordes.

**Pendiente:** la revisión independiente de ChatGPT, página por página.

**Por qué los planes ya no compensan errores:** las precisiones para el docente amplían o sugieren; ya no compensan errores del libro, porque los errores de estas secciones se corrigieron en el tomo y en el solucionario.

## 7. Formato aplicado

| Documento | Formato | Observación |
|---|---|---|
| Tomo | Variante B (oficio mejorado) | Falta la inspección visual de ChatGPT; para eso está la versión liviana. |
| Planes | A4 vertical, márgenes de 2 cm, 10 a 10,5 pt | Portada e índice en hojas propias; cada plan empieza en hoja nueva y ocupa 2 páginas. |
| Plan anual | Oficio horizontal, segunda versión | Las bandas de etapa y de unidad ya no quedan solas al pie, y el bloque final va junto. Contenido sin cambios: sus capacidades de unidad todavía no son las literales del programa, y se actualiza al aplicar al año. |
| Solucionario | A4 vertical | Numeración del tomo, páginas de referencia, criterios y rúbricas. |

## 8. Decisiones para Fernando

1. **Profundidad:** aprobar o pedir ajustes al nivel de la Clase 10 (7 págs.) y de la Clase 18 (6 págs.). Si se aplica a las 21 clases, el tomo crece mucho; la estimación se hará con la matriz.
2. **Diseño:** confirmar la variante B del tomo y el plan anual en oficio.
3. **Figura 10.1:** mantenerla con el epígrafe aclaratorio o reemplazarla por el esquema 10.2.
4. **Continuación E:** es del siglo XVIII, fuera del alcance del programa (siglos XVI y XVII). Mantenerla como puente o reemplazarla por bandeirantes y Mbororé.
5. **Programa oficial:** conseguir el PDF o el ejemplar oficial para declarar el cotejo como oficial.
