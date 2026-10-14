# Historia y Geografía 7.º grado: diagnóstico editorial y pedagógico

**Fecha:** 14 de octubre de 2026.

**Roles:** Claude edita, ChatGPT audita y Fernando aprueba.

**Estado:** diagnóstico y piloto. No se modificó ninguna versión comercial ni ningún maestro de Drive, y no se subió nada a Drive. Este informe no declara apto ningún material.

## 1. Archivos revisados

| Archivo | Origen | Formato | SHA-256 |
|---|---|---|---|
| Tomo, PDF del 3 de octubre (`PROPIO_…_TOMO_COMPLETO_VF_OFICIO.pdf`) | Drive `16nQxDmrx_EDe6bja1PRCLsYv82NWQsbr` | Oficio, 83 págs. | `127cac9882c2112d58bf5c08472348a7e7d119748cac01d3f29e0a7bb50def3f` |
| Tomo, PDF de agosto (`…_TOMO_COMPLETO_VF.pdf`) | Drive `1lkKG6S5a7MqNmD0bm_COJAEt3pdDzV8w` | A4, 90 págs. | `7c87e3cc41745ca31452b2bbc3a06dd86e404a72d2ab1ce26d5da6a77ca22608` |
| Tomo DOCX de octubre (27,3 MB) | Drive `1IhvHzOf1eEemsco2MICTo3q2RUza80xY` | — | **No se pudo descargar:** la conexión con Drive no baja archivos de más de 10 MB (ver §2) |
| Tomo DOCX de la rama `claude/trusting-hawking-13gfsj` | `Pedido_2026-10-03_Edicion_Oficio/02_HyG_7mo_Grado/` | Oficio | `039d47aefb584a294afb23608cc21edf877fd5c807542e43c31c8c79e4c21373` |
| Planes de clase | Drive `1-4vfJvADb4XvRWLw09QuNNrlspoRCpjL` (igual al de la rama) | A4 vertical | `dff2e39431635227c331d0ac98e6a36ce85c18213c309869b3068965b386ef34` |
| Plan anual | Drive `1CslgfPePNWEOXZRlz94uJHDjLBnPTNwg` (igual al de la rama) | A4 horizontal | `fc53ee4c1c240718721f1e31a6fc1725f649ab3c4697596995168a5866ebaeb2` |
| Solucionario DOCX | Drive `1oehlC8DLXCqTS7wUaPHtI-hh2NI5oU85` | A4 | `0c61186486a5521d8f9c02a3400b7ba2cefad4333b931779bdb3f9f93ccd339e` |
| Solucionario PDF | Drive `1tT789c-vk5DeCqv_fexsdx4cif9srvGF` | A4 | `253f371a6f080926db6f40d5e842fddb217497e989cc7f30cc76cf184d047aaf` |

El solucionario de la rama (`00aef5d8…`) es la versión oficio del de Drive. Difiere solo en el papel y en una línea del encabezado.

## 2. Base usada para el piloto

El DOCX de octubre de Drive no se pudo descargar. Comparé el DOCX de la rama con el PDF de octubre de Drive:

- **Texto.** Las 19.589 palabras del cuerpo coinciden en el mismo orden, sección por sección. La única diferencia es el índice, que en octubre ya incluye las continuaciones y tiene otros números de página.
- **Imágenes.** Las 26 imágenes son las mismas: igual tamaño en píxeles y la misma imagen reducida.
- **Páginas.** La diferencia (72 contra 83) viene del programa con que se generó cada PDF, no del contenido.

**Conclusión:** el DOCX de la rama sirve como base del piloto sin perder ilustraciones ni mejoras. Para producir el tomo definitivo conviene usar el DOCX de octubre. Fernando puede pasarlo en partes de menos de 10 MB o dejarlo en el repositorio.

## 3. Las diez observaciones de Fernando, verificadas

| N.º | Observación | ¿Se confirma? | Evidencia | Causa | Propuesta en el piloto |
|---|---|---|---|---|---|
| 1 | Clases que empiezan a mitad de página | **Sí** | PDF de octubre: las Clases 4, 6, 9, 14, 16 y 19 empiezan entre el 53 % y el 83 % de la altura de la página. Las Evaluaciones U1, U2, U3, U5 y U6 y la integradora de la 1.ª etapa también, partidas entre dos páginas. Las Unidades 2, 3, 5 y 6 empiezan a mitad de página. | En el DOCX: <ul><li>las Unidades 2, 3, 5 y 6 no tienen salto de página;</li><li>las Clases 9 y 14, que siguen a una continuación, tampoco;</li><li>las 8 evaluaciones son una tabla (la banda de color) sin salto antes.</li></ul> | Regla única: cada unidad, clase, continuación y evaluación empieza en hoja nueva; la clase que abre una unidad comparte la hoja con el título de la unidad. Medido: en las tres variantes, cada sección empieza en el 4 % al 8 % superior de su página. |
| 2 | Portada, índice y planes mezclados | **Sí** | Planes: la portada y el índice comparten la página 1. | — | Portada sola, índice solo y cada plan en hoja nueva. |
| 3 | Planes demasiado escuetos para 3 HC | **Sí** | Inicio, Desarrollo y Cierre suman entre 114 y 227 palabras en las clases. Las evaluaciones de unidad suman entre 40 y 73: «resolución individual, 80 min» para una prueba de 8 ítems. Los 36 planes usan el mismo esquema 20 + 80 + 20, sin tiempos parciales, agrupamientos ni producto por fase. Varios planes mandan completar cuadros que el tomo trae completos, y muchos asignan solo una parte de las actividades. | — | Secuencia minuto a minuto, con lo que hace el docente, lo que hacen los alumnos y el producto de cada fase. También: atención a la diversidad, evaluación con criterios y precisiones para el docente. Cada plan ocupa 2 páginas. |
| 4 | Letra chica, sobre todo en tablas | **Sí** | Planes: el 73 % del texto está en 7,5 a 8,5 pt. Plan anual: el 93 % en 8,5 pt. Solucionario: el 74 % en 9,5 pt. | — | Planes en 10 a 10,5 pt; plan anual en 9,5 pt (A4) o 10 pt (oficio); solucionario en 10 a 10,5 pt; tomo mejorado con el cuerpo en 11,5 pt. |
| 5 | Grandes espacios vacíos y rellenos artificiales | **Espacios vacíos, sí; rellenos, no encontré** | PDF de octubre: 19 páginas con más de la mitad inferior vacía; 11 de ellas, con más del 80 % (fin de clase antes del salto). Las 3 cajas «Nota de precisión» (págs. 16, 41 y 53) son contenido, no relleno. Los planes ocupan media página con la otra mitad en blanco. | La página en blanco al final de una clase es el precio de empezar cada clase en hoja nueva. En los planes, la causa es la letra chica. | No se agregan rellenos. Lo que reduce el blanco en el tomo son las opciones múltiples agrupadas en uno o dos renglones y los renglones para responder. Se informa el blanco de cada página (`02_piloto/tomo/medicion_tomo.json`). |
| 6 | Márgenes de los planes demasiado estrechos | **No, en los costados** | Planes: 2,0 cm a los lados y 1,6 cm arriba y abajo. Lo que se ve apretado es la letra chica. | — | Se mantienen 2,0 cm a los lados y se pasa a 1,8 cm arriba y abajo. |
| 7 | Nunca se estudió A4 contra oficio | **Sí** | Las entregas pasaron todas a oficio sin comparar. | — | Se comparan A4 y oficio para el tomo y para el plan anual (§9). |
| 8 | Tablas del plan anual mal ajustadas | **Sí** | Las 7 columnas tienen el mismo ancho (3,82 cm). «N.º» y «Tiempo» desperdician 5 cm, y «Observación», casi siempre vacía, ocupa lo mismo que «Indicadores». | Anchos iguales por defecto. | Columnas proporcionales (0,9 / 5,0 / 6,3 / 1,7 / 5,2 / 4,2 / 3,4 de cada 26,7), encabezado repetido y filas que no se parten. |
| 9 | No se evaluó si el contenido alcanza para el año | **Sí** | Ver §5. | — | — |
| 10 | Los controles automáticos dejaron pasar defectos evidentes | **Sí** | No tengo el script de control de la entrega anterior. Los defectos que pasaron indican que no medía estos datos: <ul><li>dónde empieza cada sección en el PDF;</li><li>el tamaño real de la letra;</li><li>la correspondencia entre los campos de cada plan y su clase.</li></ul> | Esos datos no se ven leyendo el DOCX: se miden en el PDF. | Los scripts del piloto miden en el PDF dónde empieza cada sección y el tamaño de la letra, y comprueban palabra por palabra que no se perdió texto ni imágenes. Estos controles **no reemplazan** la revisión visual página por página. |

## 4. Programa oficial del MEC

**No pude identificar ni cotejar la edición del programa de Historia y Geografía de 7.º.**

**Lo que hay en Drive no corresponde a 7.º:**
- «MEC — Ciencias Sociales — Programa de Estudio» y «MEC — Temas Historia y Geografía — Extracto» son de la *Actualización curricular del Bachillerato Científico* (Educación Media).
- «programa de estudio 3 ciclo Básica Bilingüe» es el programa para Personas Jóvenes y Adultas (4.ª edición, 2019).
- «3 Ciencias Sociales ok» es del segundo ciclo (4.º a 6.º).

**Lo único oficial que sirve para 7.º** es la distribución horaria del tercer ciclo (`tercer_ciclo_distribucion_horaria.pdf`, pág. 47 de su programa): Historia y Geografía, **3 horas semanales** en 7.º, 8.º y 9.º. No indica cuántos minutos dura la hora cátedra.

**Dónde está el programa correcto.** La búsqueda web lo ubica en el repositorio del CONACYT: `dspacereva.conacyt.gov.py/jspui-repo/bitstream/123456789/75/1/histygeog7.pdf`. Según su índice, las capacidades de 7.º están en la página 51. El entorno de trabajo no puede llegar a ese servidor (conexión rechazada).

**Lo que necesito:** que Fernando lo descargue y lo suba a Drive, o al repositorio, para hacer el cotejo literal e identificar la edición (año y autoridades).

**Mientras tanto:**
- Las capacidades de los planes del piloto se copian de la ficha del tomo, sin atribuirlas al MEC.
- La portada de los planes actuales dice «Programa de Estudio del Ministerio de Educación y Ciencias»: no se puede sostener hasta hacer el cotejo.

**Incoherencias que ya se ven, sin el programa:**

| Dónde | Problema |
|---|---|
| Clase 21 (gestión ambiental) | Su capacidad es «Describe las características de las regiones naturales» (en el tomo y en el plan). No corresponde al tema. |
| Clase 10 | El plan agrega «e instituciones» a la capacidad del tomo. |
| Continuaciones A, B, D, E, F y G | La capacidad del plan no coincide con la de la ficha del tomo. |
| Las 8 evaluaciones | Sus capacidades («Integra…») son editoriales. |
| Unidad 5 | Se llama «posición y relieve» en el tomo y en los planes 26 a 28, y «posición, relieve e hidrografía» en el plan anual y en los planes 29 y 30. |

## 5. ¿Alcanza el contenido para el año?

**Cantidad de encuentros:** sí. Son 36 encuentros de 3 HC (21 clases, 7 continuaciones, 6 evaluaciones de unidad y 2 integradoras). El tomo, el plan anual, los planes y el solucionario coinciden en la secuencia.

**Profundidad:** no, en la mayoría de los encuentros. Lo que hay hoy por tipo de encuentro:

| Tipo | Lo que trae hoy |
|---|---|
| Clases | 577 a 796 palabras de teoría y actividades, con 0 a 3 imágenes. La lectura lleva 10 a 15 minutos. Las 12 actividades de cada clase son casi todas de recuerdo literal. |
| Continuaciones | Una página (314 a 386 palabras). Varias piden mapas, tablas o fichas que no trae ni el tomo ni el plan. |
| Evaluaciones de unidad | 167 a 191 palabras, 8 ítems y 12 puntos, para 120 minutos. Varios ítems copian actividades de la unidad, y los planes anuncian tareas (mapa, matriz, análisis de caso) que la prueba no tiene. |
| Integradoras | Unas 300 palabras y 11 ítems. Reciclan ítems de las pruebas de unidad y no tienen escala. |

**Veredicto de los revisores sobre los 36 encuentros:** ninguno queda como «suficiente». La mayoría queda como «ampliar», y varios como «reescribir»: el 17, el 19, el 28, el 30, el 31 y el 35, entre otros. Detalle en `revision_contenido/`.

## 6. Contenido: hallazgos principales

La revisión completa de los 36 encuentros está en tres informes, cada uno con una tabla resumen y hallazgos numerados con cita, corrección y gravedad:
- `revision_contenido/encuentros_01_a_12.md`
- `revision_contenido/encuentros_13_a_24.md`
- `revision_contenido/encuentros_25_a_36.md`

Los datos marcados «a verificar» hay que cotejarlos con una fuente antes de corregir. **La auditoría independiente debe revisar estos informes.**

### Gravedad alta

| Encuentro | Hallazgo |
|---|---|
| Solucionario, Clase 10 | Dice que la Real Provisión de 1537 «estableció por ley la idea de que el poder viene del pueblo» y la llama «antecedente de las elecciones». Contradice al tomo, que la presenta como una elección excepcional, en caso de vacancia y dentro del orden monárquico. |
| Clase 5 | La chinampa aparece como «cantero flotante». Era una parcela construida con barro y plantas, fijada al fondo del lago. El error pasa a la Evaluación U2. |
| Clase 5 y Continuación B | Ni la clase ni la continuación dan fechas de mayas, mexicas o incas, pero la continuación pide una línea de tiempo comparativa. |
| Clase 6 | El «diario de un navegante (adaptado)» es una fuente inventada. |
| Clase 7 | La opción múltiple 3 tiene dos respuestas correctas. El absolutismo se explica de forma contradictoria. El V/F sobre Tordesillas se da como Verdadero, contra lo que dice el propio texto. |
| Clase 8 | Falta el contexto de la fundación de Asunción: Mendoza, Ayolas, Irala y el Cabildo de 1541. |
| Clase 11 | Atribuye la mediterraneidad a la división de 1617. Lo que cambió con la división fue la dependencia del puerto; Asunción siempre estuvo lejos del mar. |
| Clase 13 | Afirma que las reducciones protegían de la encomienda. Vale solo para las jesuíticas. |
| Evaluación U3 | No tiene ítems de cronología ni de resistencia, aunque el plan los exige. |
| Plan 27 (Clase 17, relieve) | Trae el Tema y los Indicadores de la hidrografía. |
| Plan 28 (Clase 18, hidrografía) | Trae el Tema, los Indicadores y el **Desarrollo** del clima: ni un minuto sobre la hidrografía. Comprobé los 36 planes por similitud de texto con su clase: el corrimiento afecta solo a los Planes 27 y 28. |
| Clase 18 | Faltan la Cuenca del Plata, los afluentes, los lagos y esteros, el Acuífero Guaraní y toda la hidrografía de América. Además, dice que el río Paraguay «cruza» el país, cuando en parte es límite con Brasil y con Argentina. |
| Clase 19 | <ul><li>El «Ubicate» es geográficamente incorrecto: usa el Trópico de Capricornio para separar la zona húmeda de la seca, pero el contraste es de oeste a este.</li><li>La clave de la fuente es errónea («de diciembre a marzo»).</li><li>La «fuente estadística» no tiene datos.</li><li>Faltan los tipos de clima de América.</li></ul> |
| Clase 16 | Falta la posición de América, aunque la capacidad la pide. |
| Evaluaciones U5 y U6 | No evalúan lo que anuncian sus planes. En la Parte A de la U6, las cuatro respuestas correctas son «b». |

### Contenidos que faltan

- **Siglo XVI:** Pedro de Mendoza y la primera Buenos Aires, Ayolas, Irala explicado, Cabeza de Vaca.
- **Siglo XVII:** Hernandarias, las Ordenanzas de Alfaro (1611), los bandeirantes y la pérdida del Guairá, Mbororé.
- **Continuación E:** el canje de los siete pueblos por Colonia del Sacramento.
- **Clase 15:** la colonización portuguesa.
- **Geografía:** la posición de América, el relieve de América con nombres, la hidrografía de América, los tipos de clima de América y las serranías del Paraguay con nombres.

### Problemas que se repiten

- **Claves predecibles.** En las opciones múltiples de las clases, la respuesta correcta es casi siempre «b» y nunca «d». Lote 1: b 23 veces, c 15, a 2, d 0. Lote 2: 28 de 38 en «b».
- **Distractores absurdos:** «Potosí» como represa, «Escorpio» como trópico, «Ruta 2» como vía navegable.
- **Fuentes inventadas o paráfrasis sin autor** presentadas como «fuente» o «dato estadístico».
- **Numeración distinta.** El solucionario numera los bloques de completar y de V/F de 1 a 3, y el tomo de corrido. Las claves de las continuaciones están al final, separadas de su lugar en la secuencia.
- **Respuestas abiertas sin espacio.** El tomo no deja renglones para responder las preguntas abiertas.
- **A verificar antes de imprimir:** el año y la denominación de la inscripción de la guarania en la UNESCO (Clase 9).

## 7. Planes de clase

| Aspecto | Hallazgo |
|---|---|
| Secuencia | Están los 36, en el orden correcto. |
| Corrimiento de campos | Solo en los Planes 27 y 28 (ver §6). La corrección propuesta para el 28 está en el piloto. Para el 27: <ul><li>**Tema:** «La orografía: el relieve del Paraguay y de América y su influencia en las actividades humanas».</li><li>**Indicadores:** los tres de la ficha de la Clase 17 del tomo.</li></ul> |
| Hora cátedra | La portada dice «hora cátedra de 40 minutos». Coincide con lo que indicó Fernando (3 HC = 120 min), pero no está en el programa del MEC que tengo. |
| Índice | Estático, sin números de página y con la leyenda «Actualizar el índice: Ctrl+E → F9». |

## 8. Plan anual y solucionario

**Plan anual:**
- tiene 36 filas, coherentes con los planes;
- en el plan anual, el Tema y los Indicadores de las filas 27 y 28 son correctos: el corrimiento ocurrió solo en los planes;
- tiene 9 páginas en A4 horizontal, con letra de 8,5 pt y columnas iguales.

**Solucionario:**
- cubre la prueba diagnóstica, las 21 clases, las 7 continuaciones (al final), las 6 evaluaciones de unidad y las 2 integradoras;
- errores confirmados: Clase 10 (1537) y Clase 19 (clave de la fuente);
- no tiene criterios de corrección para las respuestas abiertas ni escala para las evaluaciones.

## 9. Formatos comparados en el piloto

Los archivos, las mediciones y lo que hay que decidir están en `../02_piloto/DECISIONES_DEL_PILOTO.md`.

## 10. Pendientes

1. **Programa MEC de 7.º.** Hace falta el archivo (§4) para el cotejo literal y para identificar la edición.
2. **DOCX del tomo de octubre**, en partes de menos de 10 MB o en el repositorio.
3. **Decisión de formato** de Fernando, con el piloto.
4. **Decisión sobre la profundidad del contenido:** ampliar el tomo (nuevo texto, fuentes reales, mapas) o corregir solo los errores. Es la decisión que más trabajo implica.
5. **Auditoría independiente de ChatGPT,** página por página, del piloto y de los informes de `revision_contenido/`.
