# Plan detallado del lote editorial 6 — Unidad VI (Capítulos 17 y 18)

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · 21 de octubre de 2026**

**Estado:** plan para aprobar. **No se construye ningún capítulo hasta que Fernando lo autorice.**
- No se escribió ningún capítulo de la Unidad VI.
- No se modificaron los lotes 1 a 5 ni sus planes.
- No se generaron el tomo anual ni los 36 planes de clase, y no se subió nada a Drive.

**Base:**
- el informe de Work v0.1 (`BTI3_Analisis_Diseno_Diagnostico_Propuesta_v0.1.pdf`, SHA-256 `3d4f5ab9…065069a`): §4.2, §4.3, §5.1, §5.2, §6, §7.4 y §7.5;
- la distribución de 180 HC v2.1: `fase2_pilotos/C_informe_esfuerzo/v2_1/distribucion_36.csv` y `distribucion_28.csv`;
- el lote 5 (`b2aed1b`), aprobado como versión de referencia:
  - la versión candidata del equipo modelo;
  - sus límites conocidos (Tabla 16.8);
  - las condiciones mínimas (Tabla 16.7);
  - el cargador DP;
  - el procedimiento DR;
- los hitos H1 a H5 ya construidos (Capítulos 3, 6, 9, 13 y 16), con la misma lógica de rúbrica: cuatro niveles, 60/40 y AE aparte.

**Sobre el entorno:** HTML/CSS, PHP y SQLite siguen siendo una referencia provisional.
- **Siguen pendientes**, y el lote 6 no los declara satisfechos:
  - las pruebas institucionales en Windows;
  - la instalación en un laboratorio escolar;
  - la restauración en esos equipos;
  - la concurrencia real.
- Lo que el lote 6 pueda ejecutar se ejecutará en el contenedor de construcción y se rotulará así.

## 1. La Unidad VI en Work

**Unidad VI — Entregar y comunicar.** Encuentros 33 a 36, **20 HC**.

**Resultado de la unidad (Work §5.1):** «Paquete reproducible, defensa y recuperación».

**Índice (Work §6, textual):**

| Capítulo | Encuentros | Secciones | Cierre |
|---|---|---|---|
| 17. Preparar una entrega reproducible | 33 y 34 | 17.1. Guía de instalación, configuración y ejecución. · 17.2. Manual breve basado en tareas. · 17.3. Respaldo, restauración, licencias y registro de procedencia. · 17.4. Prueba de instalación por otro equipo y acta de entrega simulada. | Práctica: entregar código, datos, pruebas y documentación coherentes; H6. |
| 18. Demostrar, defender y aprender del proyecto | 35 y 36 | 18.1. Demostración organizada por requisitos y evidencias. · 18.2. Defensa individual de decisiones y resolución de una variante. · 18.3. Recuperación de aprendizajes pendientes. · 18.4. Retrospectiva y mejoras futuras justificadas. | Evaluación integradora de la segunda etapa y cierre del proyecto. |

**Secuencia (Work §5.2 y distribución v2.1):**

| Enc. | Foco (Work §5.2) | Evidencia (Work §5.2) | Capacidades | HC (v2.1) | Criterio v2.1 |
|---:|---|---|---|---|---|
| 33 | Redactar guía de uso, instalación, respaldo y límites. | Documentación probada por el propio equipo. | C10 | Doc 5 | Documentación |
| 34 | Entregar a otro equipo para instalación y revisión. | H6: paquete reproducible; ajustes finales. | C7, C10 | V 2, Doc 2, E 1 | Ajustes de la guía (Doc), instalación por otro equipo (V), hito H6 (E) |
| 35 | Demostración y defensa individual del proyecto. | Rúbrica de producto y preguntas de transferencia. | C1 a C10 | E 5 | Defensa |
| 36 | Recuperación individual, retrospectiva y cierre. | Evidencia faltante, balance y propuesta de continuidad. | C7, C9, C10 | G 2, E 3 | Recuperación (E), retrospectiva (G) |

**Totales de la unidad:** 20 HC = Doc 7 + V 2 + G 2 + E 9. Es la unidad con más HC de evaluación del año (9 de 20).

**Adaptación a 28 encuentros (`distribucion_28.csv`):**

| 28 | Reúne | Foco | Ajuste de alcance (v2.1, textual) |
|---:|---|---|---|
| 25 | 33 | Guía de uso, instalación y respaldo. | Sin cambios. |
| 26 | 34 | Entrega a otro equipo; H6. | Sin cambios. |
| 27 | 35 | Demostración y defensa individual. | Sin cambios. |
| 28 | 36 | Recuperación individual y cierre. | Sin cambios. |

La Unidad VI conserva sus 20 HC en las dos versiones. En la de 28, el Encuentro 28 recibe además las recuperaciones que antes iban al encuentro de reserva del 32, que en esa versión no existe (Unidad V, decisión 6). La sección 7 dice cómo se ordenan.

## 2. Capacidades propuestas

Son capacidades propuestas para el programa institucional; no son capacidades oficiales del MEC. Se rotulan así en cada ficha.

| Capacidad (Work §4.2) | Dónde se trabaja | Indicador de Work que se evidencia |
|---|---|---|
| **C10.** Documenta, entrega y defiende el prototipo. | Núcleo de la unidad (Encuentros 33 a 36) | «Otro equipo instala con la guía; recupera un respaldo; cada integrante explica una decisión y una prueba; comunica aceptación y limitaciones.» Evidencia: paquete de entrega y defensa individual. |
| **C7.** Organiza y registra el trabajo colaborativo. | Encuentros 34 y 36 | «Registra aportes de cada integrante y el origen de recursos»: registro de procedencia (17.3), acta de entrega (17.4), retrospectiva (18.4). |
| **C9.** Verifica y mejora la solución a partir de evidencia. | Encuentro 36 | Mejoras futuras justificadas con la evidencia de las pruebas y de los límites conocidos (18.4). |
| **C1 a C10** | Encuentro 35 | La defensa recorre todo el proyecto: la demostración se organiza por requisitos (C3) y evidencias (C8, C9), y la variante pide transferir decisiones de análisis y diseño (C1, C2, C4 a C6). |

**Criterio de C10 (Work §4.2):** «La entrega es reproducible, comprensible, honesta sobre sus límites y utilizable por una persona ajena al desarrollo.» Es el criterio rector del Capítulo 17.

## 3. Capítulo 17 — Preparar una entrega reproducible (Encuentros 33 y 34)

**Capacidades:** C10 (33); C7 y C10 (34).

| Sección | Qué se enseña y qué hace el equipo |
|---|---|
| 17.1. Guía de instalación, configuración y ejecución. | Una guía es una secuencia de pasos que otra persona puede seguir sin preguntar: requisitos del entorno, comandos exactos, resultado esperado de cada paso y qué hacer si falla. Se parte del LEEME de la base, de la ficha de entorno E-1 a E-12 y de los límites conocidos del H5. El equipo **prueba su propia guía**: la sigue al pie de la letra en una carpeta limpia (evidencia de Work, Encuentro 33). |
| 17.2. Manual breve basado en tareas. | Un manual se organiza por lo que la persona quiere hacer, no por pantallas: «prestar un libro», «registrar una devolución», «ver los vencidos», «sacar el informe del mes». Cada tarea tiene pasos, el mensaje que aparece y qué hacer si aparece un error. Se escribe desde los recorridos de las sesiones de uso del Capítulo 15. |
| 17.3. Respaldo, restauración, licencias y registro de procedencia. | El respaldo y la restauración se documentan como tareas, con su prueba (la del Ejemplo resuelto 15.1). La ficha de procedencia registra cada recurso del paquete: autor, licencia, de dónde salió y cómo se puede usar. Se separan el código propio, las herramientas de terceros, los datos ficticios y los recursos ajenos, como imágenes o iconos. Lo que no tiene licencia conocida no se incluye. |
| 17.4. Prueba de instalación por otro equipo y acta de entrega simulada. | Otro equipo instala el paquete con la guía, sin ayuda, y registra cada paso: hecho, con dificultad o fallido, con el mensaje exacto. Después recupera un respaldo. Con eso se firma un acta de entrega simulada: qué se entrega, versión, pruebas que acompañan, límites conocidos y pendientes, y observaciones del equipo receptor. El equipo autor ajusta la guía con lo observado (Doc 2) y vuelve a probar el paso que falló. |

**Lo que se completa en esta unidad:** la condición mínima «instalación y restauración reproducibles» (Work §4.3), que en el H5 quedó como «Pendiente: instalación por otro equipo».
- Se comprueba en la instalación por otro equipo del Encuentro 34.
- En el laboratorio del colegio la hacen los estudiantes. Esa evidencia vale para el equipo y para esas computadoras.
- La del equipo modelo del libro se ejecuta en el contenedor de construcción y se rotula así.

**Ejemplos resueltos:** equipo modelo Arapoty, versión candidata del H5 (ver la decisión D-1).
- **17.1** Corregir una guía: un paso dice «ejecutá el instalador» sin el comando ni el resultado esperado.
- **17.2** Escribir la tarea «registrar una devolución» con sus mensajes ME-07 y ME-06.
- **17.3** Completar la ficha de procedencia del paquete: PHP, SQLite, el código del proyecto, los datos ficticios y las fuentes del sistema.
- **17.4** Un acta de entrega con un paso fallido y su corrección.

**Práctica 17 (Work: «entregar código, datos, pruebas y documentación coherentes»)**
- **Caso Mbokaja, datos nuevos:** la escuela recibe un paquete de un voluntario para la computadora donada, sin internet (M-F4 y M-F7, del lote 4). El paquete tiene incoherencias reales, en archivos:
  - la guía nombra un comando que no existe;
  - los datos de prueba se refieren a un archivo que falta;
  - una prueba espera un mensaje que el código ya no da;
  - una imagen no tiene procedencia;
  - el manual describe una pantalla que cambió.
- **Archivos:** el paquete se arma en `lote_6/proyecto/paquete_mbokaja/`, y un comprobador registra qué incoherencias existen, para que la clave no sea inventada.
- **Niveles:**
  - **Nivel 1:** encontrar las incoherencias con una lista de verificación.
  - **Nivel 2:** corregirlas en una copia y comprobar que el paquete se instala siguiendo la guía corregida.
  - **Nivel 3, en papel:** escribir el acta de entrega a la escuela, con lo que el profesor vecino tiene que comprobar en su visita mensual (M-F9).
- **H6:** el equipo entrega su propio paquete. Es el hito de la unidad, no se reemplaza con la práctica.

**Hito H6 (Encuentro 34, 1 HC de evaluación): «H6: paquete reproducible; ajustes finales».**
- **Rúbrica propuesta,** seis criterios con cuatro niveles; capacidades C7 y C10:
  1. **guía de instalación reproducible:** probada por el propio equipo y por otro;
  2. **manual por tareas:** comprensible para una persona ajena al desarrollo;
  3. **respaldo y restauración documentados y comprobados;**
  4. **procedencia y licencias completas,** sin recursos de origen desconocido;
  5. **coherencia del paquete:** código, datos, pruebas y documentación de la misma versión;
  6. **honestidad sobre límites y pendientes,** con el acta de entrega.
- **Ponderación:** 60 % de evidencia del equipo (el paquete y el acta) y 40 % individual (la parte del paquete que cada integrante redactó o probó, registrada en la bitácora, y la observación del docente). Es una propuesta editorial.
- **Ausencias y pendientes:** la AE se registra aparte, y un pendiente del entorno no se cuenta como falla.

**Evaluación del Capítulo 17:** opcional, de 15 puntos, como en los capítulos anteriores. La propongo con un texto base nuevo: préstamo de equipos audiovisuales, un proyecto alternativo de Work §7.4 que todavía no se usó en las evaluaciones. Decisión D-3.

## 4. Capítulo 18 — Demostrar, defender y aprender del proyecto (Encuentros 35 y 36)

**Capacidades:** C1 a C10 (35); C7, C9 y C10 (36).

| Sección | Qué se enseña y qué hace el equipo |
|---|---|
| 18.1. Demostración organizada por requisitos y evidencias. | La demostración no es un paseo por pantallas: es un guion que va de cada requisito imprescindible a su evidencia y a una ejecución en vivo (o a la evidencia registrada, si el entorno no lo permite). Se prepara con la matriz de trazabilidad y el acta de aceptación del Capítulo 15. Tiene un tiempo fijo, y el guion dice qué se muestra si un paso falla en vivo. |
| 18.2. Defensa individual de decisiones y resolución de una variante. | Cada estudiante explica una decisión de diseño y una prueba (indicador de C10) y resuelve una variante nueva: un cambio acotado de regla o de requisito. Dice qué capa toca, qué cambia en el modelo y en los contratos, y qué pruebas habría que agregar. No programa en el momento: se evalúa el razonamiento, como en los H4 y H5. |
| 18.3. Recuperación de aprendizajes pendientes. | Con la planilla anual (H1 a H6 y defensa), cada estudiante con ausencia de evidencia o con un criterio en nivel Inicial tiene una tarea de recuperación específica y acotada, que se resuelve en las 3 HC de evaluación del Encuentro 36. Lo que no se recupera se registra con su procedimiento; no se suponen horas extraordinarias. |
| 18.4. Retrospectiva y mejoras futuras justificadas. | En las 2 HC de gestión, el equipo revisa la bitácora del año: qué funcionó, qué no y por qué, con evidencia. Propone mejoras futuras, y cada una tiene que apoyarse en un límite conocido, una incidencia o una observación de uso, con su prioridad (evidencia de Work: «balance y propuesta de continuidad»). |

**Cierre (Work): «Evaluación integradora de la segunda etapa y cierre del proyecto».**
- **Sin práctica independiente,** como el Capítulo 16 con el H5. La actividad integradora es la demostración y la defensa. Decisión D-4.
- **Composición propuesta de la evaluación integradora de la segunda etapa** (Encuentros 34 a 36):
  - el H6;
  - la rúbrica de producto final, con los seis aspectos de la ponderación editorial de Work §4.3: problema y relevamiento 15 %, requisitos y trazabilidad 20 %, modelos y diseño 20 %, prototipo e integración 20 %, pruebas y mejora 15 %, documentación y defensa 10 %;
  - la defensa individual.
- Es una propuesta editorial: la conversión a calificación la decide la institución.
- **Instrumentos del capítulo:**
  - guion de demostración, como plantilla;
  - rúbrica de producto final;
  - rúbrica de defensa individual, con cuatro niveles: explicación de una decisión, explicación de una prueba, resolución de la variante y comunicación de límites;
  - banco V6 de variantes, en la guía, que no repiten las de los bancos H3, H4 y H5 ni los textos de evaluación;
  - preguntas de transferencia con los proyectos alternativos de Work §7.4;
  - planilla anual consolidada H1 a H6 + defensa, con la columna AE;
  - ficha de recuperación;
  - registro de retrospectiva.
- **Evaluación escrita:** no propongo una «Evaluación del Capítulo 18» escrita. Los Encuentros 35 y 36 son de evaluación, y Work §4.3 dice que «no todo necesita una prueba escrita adicional». Decisión D-3.

## 5. Distribución de las 20 HC por encuentro

| Enc. | Momento | HC (categoría v2.1) | Qué se hace |
|---:|---|---|---|
| 33 | Problema y explicación | 1 (Doc) | Qué hace reproducible una entrega; 17.1 y su ejemplo. |
| 33 | Redacción | 2 (Doc) | Guía de instalación (17.1) y manual por tareas (17.2) del propio equipo. |
| 33 | Prueba de la propia guía | 1 (Doc) | Seguirla al pie de la letra en una carpeta limpia y corregirla. |
| 33 | Procedencia | 1 (Doc) | 17.3: respaldo y restauración documentados; ficha de procedencia. Práctica 17, nivel indicado por el docente. |
| 34 | Instalación por otro equipo | 2 (V) | 17.4: el equipo receptor instala y restaura con la guía, sin ayuda, y registra cada paso. |
| 34 | Ajustes | 2 (Doc) | Corrección de la guía con lo observado y nueva prueba del paso fallido. |
| 34 | H6 | 1 (E) | Acta de entrega simulada y revisión con la rúbrica del H6. |
| 35 | Demostraciones | aprox. 2 (E) | 18.1: demostración por requisitos y evidencias de cada equipo, con su guion y tiempo fijo. |
| 35 | Defensas individuales | aprox. 3 (E) | 18.2: decisión, prueba y variante V6, para cada estudiante. |
| 36 | Recuperación | 3 (E) | 18.3: tareas de recuperación específicas. |
| 36 | Retrospectiva y cierre | 2 (G) | 18.4: balance, mejoras futuras justificadas, cierre del proyecto. |

**El riesgo de la unidad está en el Encuentro 35.** No se sabe de antemano si una demostración por equipo y una defensa por estudiante entran en 5 HC: depende del tamaño del curso y de la duración de la HC, que fija cada institución.

**La guía va a traer:**
- una planilla de tiempos expresada en fracciones de HC, para que el docente la calcule con su curso;
- la preparación previa a cargo del docente, como pidió la auditoría para el Encuentro 30: variantes impresas, guion, planillas y copias listas;
- dos alternativas documentadas, sin omitir evidencias esenciales:
  - estaciones de demostración simultáneas con un segundo evaluador que la institución designe (por ejemplo, el docente de Laboratorio);
  - completar defensas dentro de las HC de evaluación del Encuentro 36, con una recuperación más breve.

**No se suponen horas extraordinarias** que la institución no disponga.

## 6. Relación con los hitos H1 a H6

| Hito | Encuentro | Capítulo | Qué se evaluó | Cómo llega a la Unidad VI |
|---|---:|---|---|---|
| H1 | 6 | 3 | Problema y alcance defendidos | La demostración (18.1) empieza por el problema y el alcance acordado. |
| H2 | 12 | 6 | Requisitos y modelos funcionales versionados | El guion de demostración se ordena por los requisitos imprescindibles del catálogo. |
| H3 | 18 | 9 | Dossier consistente y evidencia individual (evaluación integradora de la primera etapa) | Es el modelo de la evaluación integradora de la segunda etapa: producto más defensa individual. |
| H4 | 26 | 13 | Circuito funcional completo y lista de incidencias | Las incidencias abiertas pasan a los límites conocidos del paquete. |
| H5 | 32 | 16 | Evidencia de calidad y límites conocidos | La versión candidata es la que se empaqueta; sus límites van al acta de entrega. La condición mínima pendiente (instalación por otro equipo) se completa en el H6. |
| H6 | 34 | 17 | Paquete reproducible; ajustes finales | Hito de la unidad. |
| Defensa | 35 | 18 | Rúbrica de producto y preguntas de transferencia | Cierra la evaluación integradora de la segunda etapa. |
| Recuperación | 36 | 18 | Evidencia faltante | Usa la planilla anual consolidada de H1 a H6. |

## 7. Adaptación a 28 encuentros

- Los cuatro encuentros quedan sin cambios (25 = 33, 26 = 34, 27 = 35, 28 = 36), con las mismas HC.
- **El Encuentro 28 tiene más presión.** En esa versión no hubo encuentro de reserva en la Unidad V, así que recibe también las recuperaciones técnicas pendientes del H5.
- **Orden de prioridad en el Encuentro 28:**
  1. las condiciones mínimas de Work §4.3 que falten;
  2. la evidencia individual ausente (AE);
  3. los criterios en nivel Inicial.
- **Lo que no se recupera** se registra con su procedimiento, sin declarar aprobada la condición, y se informa a la coordinación.
- **Lo que se reduce:**
  - la retrospectiva se condensa en una ficha del equipo (G 2 se conservan, con menos producción escrita);
  - los niveles 3 de la Práctica 17 pasan a lectura.
- **Lo que no se reduce:**
  - la instalación por otro equipo;
  - el H6;
  - la defensa individual.
- Cada capítulo lleva su recuadro «Si el calendario se acorta», y la guía, la tabla de 36 y 28 encuentros.

## 8. Proyecto y evidencia del lote 6

**No se modifican** las referencias de los lotes 4 y 5.

**Todo lo nuevo va en `lote_6/proyecto/`:**
- **`paquete_entrega_modelo/`:** una copia de la versión candidata del equipo modelo (decisión D-1), con los documentos de entrega:
  - guía de instalación;
  - manual por tareas;
  - límites y pendientes;
  - ficha de procedencia y licencias;
  - acta de entrega;
  - lista de entrega.
- **`comprobar_entrega.php`:** un comprobador breve, de menos de 100 líneas, que verifica que el paquete tenga lo que dice la lista de entrega y que sus pruebas pasen. Los estudiantes lo pueden usar. Es código nuevo en la copia nueva.
- **`paquete_mbokaja/`:** el paquete con incoherencias de la Práctica 17, con un registro de las incoherencias que existen.

**Pruebas reales, en el contenedor de construcción** (con `build/reproducir.py`, como en los lotes 4 y 5):
- **La guía como prueba:**
  - se extraen los comandos de la guía de instalación del paquete modelo;
  - se ejecutan en una carpeta limpia, en otro proceso y sin nada más que la guía;
  - se comprueban instalación, verificación del entorno, recorrido HTTP, respaldo y restauración.
  - Así se demuestra que la guía, no solo el código, es reproducible.
- **El paquete de Mbokaja:** el comprobador encuentra exactamente las incoherencias registradas, y la versión corregida de la clave se instala.
- **La regresión de la versión candidata,** sin cambios respecto del lote 5.

**Rotulado:** cada resultado lleva su condición (comprobado, reproducido, simulado o pendiente), como en la Unidad V.
- La instalación por otro equipo en el libro es del equipo modelo, en el contenedor, y se rotula así.
- La del laboratorio queda pendiente.

**Licencias de terceros:** se verifican con fuentes primarias al construir, no de memoria. Entre ellas:
- la licencia de PHP, que tuvo cambios recientes de redacción;
- el dominio público de SQLite.

La ficha de procedencia cita la fuente y la fecha de consulta.

## 9. Controles previstos (verificador del lote 6)

Mismos bloques que los lotes 4 y 5, extendidos a los Capítulos 17 y 18, y bloques nuevos:
- **A:** índice de Work, con títulos, secciones, práctica y cierre textuales.
- **B:** capacidades de §5.2 por encuentro, rotuladas como propuestas.
- **R, reproducibilidad:**
  - la guía del paquete modelo se ejecuta tal cual, sin pasos fuera de la guía;
  - el comprobador de entrega da los resultados esperados;
  - el paquete de Mbokaja tiene exactamente las incoherencias de la clave.
- **L, licencias y procedencia:**
  - cada recurso del paquete tiene autor, licencia y fuente;
  - ningún recurso sin licencia conocida;
  - las licencias de terceros citan su fuente primaria.
- **H6 y cierre:**
  - seis criterios, cuatro niveles, 60/40 rotulado y AE aparte;
  - la condición mínima de instalación se completa solo con la evidencia de otro equipo;
  - pendientes del entorno separados de las fallas.
- **W, calendario:**
  - tabla de 28 encuentros «Sin cambios»;
  - prioridades de recuperación del Encuentro 28;
  - ninguna mención de horas extraordinarias que no esté negada.
- **I, instrumentos:**
  - claves de todas las actividades;
  - banco V6 sin repeticiones de los bancos anteriores ni de los textos de evaluación;
  - planilla anual H1 a H6.
- **Q:** lotes 1 a 5 intactos (git y manifiestos SHA-256) y referencias de los lotes 4 y 5 sin cambios.
- **Maqueta e impresión:** controles de impresión O3, prueba con tres fuentes de sustitución y láminas de revisión.

**Extensión estimada en oficio O3:** libro de 26 a 34 págs., guía de 18 a 24 y cuaderno de 3 a 6, con una sola práctica. Es una estimación y no se rellena para alcanzarla.

## 10. Decisiones que necesito antes de construir

| N.º | Decisión | Mi propuesta |
|---|---|---|
| D-1 | Qué versión empaqueta el equipo modelo. | La **v2 con SC-02** (`lote_5/proyecto/referencia_docente_v2_sc02/`): es la versión candidata con la mejora aprobada. La copia del paquete se hace en `lote_6/proyecto/`, sin tocar la del lote 5. |
| D-2 | Qué licencia declara el paquete del equipo modelo, y qué se recomienda a los equipos para su propio código. | Es una decisión de derechos de la editorial y de la institución. Necesito que la fijes vos. Mi propuesta: el código de referencia, «uso educativo en la institución que adquiere el material; todos los derechos reservados», y para los equipos, que registren autoría y elijan una licencia solo si la institución lo autoriza. Por defecto: sin licencia de publicación, uso escolar. |
| D-3 | Evaluaciones escritas. | Capítulo 17: evaluación opcional de 15 puntos, como los anteriores. Capítulo 18: sin evaluación escrita, porque sus encuentros ya son de evaluación. |
| D-4 | Práctica del Capítulo 18. | Sin práctica independiente: la evaluación integradora de la segunda etapa es la actividad, como el H5 en el Capítulo 16. |
| D-5 | Encuentro 35 si no alcanza el tiempo. | Las dos alternativas de la sección 5, documentadas en la guía, para que elija la institución. |
| D-6 | Anexos propuestos por Work (glosario, plantillas, diccionario de datos, matriz de trazabilidad, registro de pruebas, rúbrica del proyecto, ficha de procedencia, lista de entrega, proyectos alternativos, fichas de recuperación de HTML/CSS y programación). | El lote 6 construye solo la ficha de procedencia y la lista de entrega, porque las usa el Capítulo 17. Los demás anexos se arman en el cierre de la colección desde las tablas ya aprobadas, sin redactarlos de nuevo (ver la estrategia de cierre). |

## 11. Lo que se entregará con el lote 6

- Libro, guía docente con solucionario y cuaderno de prácticas en DOCX y PDF, desde la fuente común y en oficio O3.
- El proyecto de la sección 8, con sus pruebas y los resultados con su entorno.
- Los scripts: construcción, verificador, controles de impresión, prueba de fuentes, manifiesto e índice del tomo.
- El plan anual preliminar regenerado con las fichas de los Capítulos 17 y 18, que completa los 18 capítulos.
- El informe, el manifiesto SHA-256 y las láminas de revisión.
- Al terminar, el lote se detiene para la auditoría, antes del cierre de la colección.
