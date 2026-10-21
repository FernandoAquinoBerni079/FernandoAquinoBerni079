# Plan anual preliminar — Análisis y Diseño de Sistemas, 3.º BTI (estructura)

**Biblioteca Comercial 2026 · Plan Optativo · 5 HC semanales · 36 encuentros · 180 HC**

> **Estado:** estructura preliminar para revisión. No es el plan anual maquetado ni está aprobado. Propuesta editorial para el programa institucional del Plan Optativo; no es programa ni capacidad oficial del MEC.

> Se genera con `plan_anual_preliminar.py` desde el informe de Work v0.1 (SHA-256 `3d4f5ab9…065069a`), la distribución de 180 HC (v2.1) y las fichas de los capítulos construidos. No editar a mano: corregir las fuentes y regenerar.

## 1. Competencia propuesta (Work §4.1)

Analiza necesidades de información de una organización de su entorno y diseña, construye y valida colaborativamente un prototipo de aplicación web, mediante requisitos verificables, modelos coherentes, decisiones técnicas justificadas y documentación de entrega, actuando con responsabilidad sobre los datos, los recursos y los acuerdos del proyecto.

## 2. Capacidades propuestas (Work §4.2)

Propuesta editorial para el programa institucional del Plan Optativo; no es programa ni capacidad oficial del MEC.

| Código | Capacidad | Contenidos esenciales | Indicadores observables y evidencia | Criterio de evaluación |
|---|---|---|---|---|
| C1 | Delimita un problema y evalúa la factibilidad de una solución. | Sistema, entorno, actores, alcance, alternativas, restricciones, costo y riesgo básicos. | Diferencia problema y solución; identifica actores y restricciones; compara al menos dos alternativas; presenta alcance y exclusiones. Evidencia: ficha de problema y factibilidad. | El alcance responde a una necesidad documentada y es realizable con los recursos disponibles. |
| C2 | Obtiene y contrasta información sobre necesidades de usuarios. | Entrevista, observación, revisión documental, registro de fuentes y resguardo de datos. | Formula preguntas abiertas; registra evidencia; separa hechos, opiniones y supuestos; contrasta dos fuentes o dos roles simulados. Evidencia: dossier de relevamiento. | Las conclusiones son rastreables a evidencia y respetan a las personas consultadas. |
| C3 | Especifica y prioriza requisitos verificables. | Funcionales, no funcionales, reglas, restricciones, aceptación, prioridad y cambios. | Identifica cada requisito; formula al menos ocho funcionales y cuatro no funcionales o restricciones; define aceptación y prioridad; registra una modificación. Evidencia: catálogo versionado. | Requisitos comprensibles, consistentes, necesarios y comprobables; distinción correcta entre requisito, regla y solución. |
| C4 | Modela procesos e interacciones del sistema. | Proceso actual y propuesto, contexto, casos de uso, escenarios y excepciones. | Representa límites y actores; desarrolla tres casos de uso prioritarios con flujo alternativo; mantiene coherencia con requisitos. Evidencia: modelos comentados. | Los diagramas ayudan a explicar el funcionamiento y permiten detectar omisiones, sin mezclar notaciones. |
| C5 | Justifica el modelo de información y sus reglas de integridad. | Entidades, ejemplares, relaciones, claves, diccionario, persistencia e historial; revisión aplicada de normalización. | Distingue obra/edición y ejemplar; vincula cada préstamo a un ejemplar; justifica claves y relaciones; detecta una anomalía y corrige el diseño. Evidencia: modelo y diccionario. | El modelo representa las reglas acordadas, conserva historial y evita referencias inválidas y duplicación de préstamos activos. |
| C6 | Diseña la interacción y la arquitectura del prototipo. | Tareas de usuario, bocetos, navegación, estados, accesibilidad básica y separación de responsabilidades. | Traza tres recorridos; muestra estados vacío/error/éxito; identifica presentación, reglas y datos; justifica una decisión con alternativas. Evidencia: bocetos y esquema de arquitectura. | El diseño permite completar tareas, es legible y resulta coherente con alcance, datos y entorno. |
| C7 | Organiza y registra el trabajo colaborativo. | Iteraciones, tareas, responsables, estimación, versiones, cambios, autoría y revisión entre pares. | Mantiene tareas y decisiones al día; produce al menos tres versiones identificables; registra aportes de cada integrante y el origen de recursos. Evidencia: bitácora y revisiones. | El proceso es verificable, el equipo responde a cambios y cada estudiante demuestra participación sustantiva. |
| C8 | Integra un prototipo funcional con persistencia. | Formularios, validación del servidor, consultas parametrizadas, reglas, transacciones y reportes mínimos. | Ejecuta catálogo, lectores, préstamo y devolución; conserva datos al reiniciar; rechaza operaciones inválidas; relaciona módulos con requisitos. Evidencia: prototipo y demostración. | Funciona el circuito completo y las reglas se hacen cumplir más allá de la apariencia de las pantallas. |
| C9 | Verifica y mejora la solución a partir de evidencia. | Casos normales y límite, integración, usabilidad, aceptación, incidencias y regresión. | Ejecuta al menos doce casos identificados; registra esperado/obtenido; incluye seis rechazos o límites; corrige y vuelve a probar; realiza dos sesiones de uso. Evidencia: matriz de pruebas e incidencias. | La evidencia permite reproducir resultados; las correcciones responden a hallazgos y no introducen regresiones conocidas. |
| C10 | Documenta, entrega y defiende el prototipo. | Instalación, uso, respaldo/restauración, límites, pendientes, aceptación y comunicación técnica. | Otro equipo instala con la guía; recupera un respaldo; cada integrante explica una decisión y una prueba; comunica limitaciones. Evidencia: paquete de entrega y defensa individual. | La entrega es reproducible, comprensible, honesta sobre sus límites y utilizable por una persona ajena al desarrollo. |

## 3. Unidades (Work §5.1)

| Unidad | Encuentros | HC | Resultado de unidad |
|---|---|---:|---|
| I. Comprender el problema y su contexto | 1-6 | 30 | Problema, relevamiento y alcance viable. |
| II. Especificar qué debe resolver el sistema | 7-12 | 30 | Requisitos, procesos y trazabilidad inicial. |
| III. Diseñar una solución coherente | 13-18 | 30 | Modelo de datos, interacción y arquitectura revisados. |
| IV. Construir el prototipo por incrementos | 19-26 | 40 | Circuito funcional integrado y persistente. |
| V. Verificar, validar y mejorar | 27-32 | 30 | Evidencia de pruebas, correcciones y aceptación. |
| VI. Entregar y comunicar | 33-36 | 20 | Paquete reproducible, defensa y recuperación. |

## 4. Secuencia por capítulo y encuentro

HC por categoría (distribución v2.1): A análisis · D diseño · P programación · V verificación y validación · Doc documentación · G gestión · E evaluación.

### Capítulo 1. Un sistema comienza con una necesidad (Unidad I; encuentros 1-2)

- **Capacidades del capítulo:** C1, C7 (propuestas).
- **Secciones (Work §6):** 1.1. De la dificultad cotidiana al problema de información. 1.2. Personas, procesos, datos, recursos y límites del sistema. 1.3. Actores e interesados: necesidades diferentes, decisiones compartidas. 1.4. Diagnóstico de conocimientos previos y plan de apoyo.
- **Cierre:** Práctica: describir una biblioteca y separar hechos, supuestos y soluciones anticipadas.
- **Indicadores:** Distingue una dificultad cotidiana del problema de información que la explica y de una solución anticipada. | Describe un sistema de información con sus personas, procesos, datos, recursos y límites. | Identifica actores e interesados, con sus necesidades y su influencia en las decisiones. | Separa hechos, supuestos y soluciones anticipadas en la descripción de una situación. | Reconoce sus conocimientos previos y acuerda un plan de apoyo y las reglas de trabajo del equipo. _(de lote_1/build/cap1.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Algorítmica 1.º, pp. 70-73 (reglas sin ambigüedad); Laboratorio 1.º, pp. 41-47 (documentos colaborativos, ética).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | Presentación del reto y diagnóstico de programación, formularios, datos y comunicación. | C1, C7 | Resolución individual breve; mapa de apoyos. | 3 | 0 | 0 | 0 | 0 | 0 | 2 |
| 2 | Sistema de biblioteca, actores, límites y situación problemática. | C1 | Ficha de problema; mapa de actores. | 5 | 0 | 0 | 0 | 0 | 0 | 0 |

### Capítulo 2. Investigar antes de diseñar (Unidad I; encuentros 3-4)

- **Capacidades del capítulo:** C2 (propuestas).
- **Secciones (Work §6):** 2.1. Entrevistar para comprender tareas y problemas. 2.2. Observar un proceso y analizar documentos. 2.3. Contrastar fuentes, contradicciones y necesidades no expresadas. 2.4. Registrar evidencia con respeto por las personas y sus datos.
- **Cierre:** Práctica: dossier de relevamiento con roles de bibliotecario, lector y dirección.
- **Indicadores:** Prepara una entrevista con objetivo y guion de preguntas abiertas, sin preguntas inductoras, dobles ni técnicas. | Elige la técnica de relevamiento (entrevista, observación, análisis de documentos) según lo que necesita averiguar. | Registra la evidencia numerada y separa hechos, opiniones y supuestos. | Contrasta dos fuentes o dos roles, registra las contradicciones y detecta necesidades no expresadas. | Resguarda la información: pide autorización, anonimiza y limita el uso de los datos. _(de lote_1/build/cap2.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Laboratorio 1.º, pp. 41-47 (documentos colaborativos, seguridad y ética).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 3 | Preparar entrevista, observación y revisión de registros. | C2 | Guion y criterios para resguardar información. | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | Realizar relevamiento real autorizado o simulación con roles. | C2 | Notas, fuentes y registro de contradicciones. | 5 | 0 | 0 | 0 | 0 | 0 | 0 |

### Capítulo 3. Elegir un alcance posible (Unidad I; encuentros 5-6)

- **Capacidades del capítulo:** C1, C2, C7 (propuestas).
- **Secciones (Work §6):** 3.1. Objetivos y resultados esperados. 3.2. Comparación de alternativas y factibilidad básica. 3.3. Recursos, riesgos, límites y exclusiones. 3.4. Acuerdo de proyecto y organización del equipo.
- **Cierre:** Revisión de unidad I: defensa del problema y del alcance; H1.
- **Indicadores:** Formula objetivos y resultados esperados comprobables, cada uno vinculado a necesidades del dossier. | Compara al menos dos tipos de solución según su factibilidad operativa, técnica, económica y de calendario. | Identifica recursos y riesgos, con su probabilidad, su impacto y una mitigación, y delimita el alcance con sus exclusiones. | Justifica cada decisión de alcance con evidencia del dossier y marca lo que todavía hay que verificar. | Organiza el equipo con roles, tareas, un acuerdo de proyecto y versiones identificables de sus documentos. _(de lote_1/build/cap3.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Administración Financiera 2.º-3.º, pp. 80-87 (factibilidad básica y evidencia); Matemática Aplicada, pp. 88-94 (estimaciones; articulación condicional, ver Work §3).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 5 | Comparar alternativas: registro manual mejorado, herramienta existente y prototipo. | C1, C2 | Matriz de factibilidad y riesgos. | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| 6 | Delimitar alcance, exclusiones y equipo; revisión de unidad I. | C1, C2, C7 | H1: problema y alcance defendidos; correcciones. | 2 | 0 | 0 | 0 | 0 | 1 | 2 |

### Capítulo 4. Requisitos que se pueden comprobar (Unidad II; encuentros 7-8)

- **Capacidades del capítulo:** C3, C9 (propuestas).
- **Secciones (Work §6):** 4.1. Necesidad, requisito, regla de negocio y solución técnica. 4.2. Requisitos funcionales, calidad y restricciones. 4.3. Identificación, fuente, prioridad y criterios de aceptación. 4.4. Ambigüedades frecuentes y cómo corregirlas.
- **Cierre:** Práctica: convertir pedidos de usuarios en requisitos verificables.
- **Indicadores:** Distingue necesidad, requisito, regla de negocio y solución técnica en pedidos de usuarios. | Formula requisitos funcionales, de calidad y restricciones, cada uno con identificador y fuente que lo respalda. | Define para cada requisito un criterio de aceptación comprobable y una prioridad justificada. | Detecta ambigüedades frecuentes y reescribe el requisito en forma verificable. | Revisa los requisitos de otro equipo con una lista de verificación y propone correcciones concretas. _(de lote_2/build/cap4.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Algorítmica 1.º, pp. 70-73 (reglas de préstamo sin ambigüedad).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 7 | Formular requisitos funcionales y reglas de préstamo. | C3 | Catálogo con identificadores y fuente. | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| 8 | Definir calidad, restricciones y criterios de aceptación. | C3, C9 | Requisitos comprobables; revisión entre pares. | 4 | 0 | 0 | 1 | 0 | 0 | 0 |

### Capítulo 5. Procesos, contexto y casos de uso (Unidad II; encuentros 9-10)

- **Capacidades del capítulo:** C3, C4 (propuestas).
- **Secciones (Work §6):** 5.1. Proceso actual y proceso propuesto. 5.2. Diagrama de contexto y límites de intercambio de información. 5.3. Actores, casos de uso y escenarios principales. 5.4. Excepciones, decisiones y flujos alternativos.
- **Cierre:** Práctica: modelar préstamo y devolución con situaciones problemáticas nuevas.
- **Indicadores:** Representa el proceso actual y el proceso propuesto con un diagrama de actividades con carriles, y señala qué problema del dossier resuelve cada cambio. | Delimita el sistema con un diagrama de contexto: entidades externas y la información que entra y sale. | Identifica actores como roles y desarrolla tres casos de uso prioritarios con su escenario principal. | Describe al menos un flujo alternativo por caso de uso, con su punto de decisión y su resultado. | Mantiene la coherencia entre los modelos y el catálogo: cada requisito citado existe y cada notación se usa sola. _(de lote_2/build/cap5.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Dibujo Técnico 1.º, pp. 35-38 (legibilidad y convenciones; la semántica del diagrama de contexto y de casos de uso es aporte nuevo).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 9 | Representar proceso actual y proceso propuesto. | C4 | Flujos comentados y decisiones justificadas. | 3 | 2 | 0 | 0 | 0 | 0 | 0 |
| 10 | Desarrollar casos de uso y excepciones. | C3, C4 | Préstamo, devolución y consulta con alternativas. | 5 | 0 | 0 | 0 | 0 | 0 | 0 |

### Capítulo 6. Priorizar y mantener la coherencia (Unidad II; encuentros 11-12)

- **Capacidades del capítulo:** C3, C4, C7 (propuestas).
- **Secciones (Work §6):** 6.1. Alcance mínimo y funcionalidades postergables. 6.2. Trazabilidad entre necesidad, requisito, modelo y prueba. 6.3. Iteraciones, tareas, dependencias y responsabilidades. 6.4. Solicitud de cambio y análisis de impacto.
- **Cierre:** Revisión de unidad II: nueva necesidad del usuario y actualización del dossier; H2.
- **Indicadores:** Distingue el alcance mínimo de las funcionalidades postergables y justifica cada prioridad con criterios explícitos. | Construye una matriz de trazabilidad entre necesidad, regla, requisito, caso de uso, criterio de aceptación y prueba prevista, y detecta omisiones. | Planifica incrementos con tareas, responsables, dependencias, estimaciones y versiones identificables. | Tramita una solicitud de cambio con su análisis de impacto, su decisión y la nueva versión del catálogo y de los modelos. | Actualiza el dossier del equipo y explica individualmente el impacto de un cambio acotado. _(de lote_2/build/cap6.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Matemática Aplicada, pp. 88-94 (dependencias y cronograma sencillo; articulación condicional); Laboratorio 3.º, p. 58 (iteraciones y metodologías).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 11 | Priorizar, planificar incrementos y establecer trazabilidad. | C3, C7 | Requisito-modelo-prueba; tareas y responsables. | 2 | 0 | 0 | 0 | 0 | 3 | 0 |
| 12 | Resolver una solicitud de cambio; revisión de unidad II. | C3, C4, C7 | H2: requisitos y modelos funcionales versionados. | 3 | 0 | 0 | 0 | 0 | 0 | 2 |

### Capítulo 7. Datos que representan las reglas (Unidad III; encuentros 13-14)

- **Capacidades del capítulo:** C5 (propuestas).
- **Secciones (Work §6):** 7.1. Recuperación aplicada de modelos de Algorítmica. 7.2. Obra/edición, ejemplar, lector y préstamo: identidad y responsabilidad. 7.3. Relaciones, restricciones, historial y diccionario de datos. 7.4. Revisión de normalización con ejemplos del proyecto.
- **Cierre:** Práctica: justificar el modelo frente a pérdida, devolución y duplicación de solicitudes.
- **Indicadores:** Distingue obra, edición y ejemplar, y vincula cada préstamo a un ejemplar físico. | Justifica las claves y las relaciones del modelo con las reglas y los requisitos del catálogo v1.1. | Expresa las reglas de préstamo como restricciones de integridad y conserva el historial sin borrar registros. | Documenta cada dato en un diccionario con su significado, su obligatoriedad y el requisito que lo pide. | Detecta una anomalía en datos del proyecto y corrige el diseño. _(de lote_3/build/cap7.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Algorítmica 3.º, pp. 77-79 (DER, integridad, normalización; concurrente).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 13 | Revisar antecedentes de Algorítmica y modelar el dominio. | C5 | Obras/ediciones, ejemplares, lectores y préstamos. | 0 | 5 | 0 | 0 | 0 | 0 | 0 |
| 14 | Validar integridad, historial y diccionario de datos. | C5 | Revisión del modelo con ejemplos y contraejemplos. | 0 | 4 | 0 | 1 | 0 | 0 | 0 |

### Capítulo 8. Diseñar para las tareas de las personas (Unidad III; encuentros 15-16)

- **Capacidades del capítulo:** C6, C9 (propuestas).
- **Secciones (Work §6):** 8.1. Recorridos de usuario y organización de pantallas. 8.2. Bocetos y prototipo de baja fidelidad. 8.3. Estados vacío, carga, error y confirmación. 8.4. Etiquetas, navegación por teclado y lectura comprensible.
- **Cierre:** Práctica: observar el uso del boceto y modificarlo con evidencia.
- **Indicadores:** Traza tres recorridos completos a partir de los casos de uso prioritarios y organiza las pantallas en un mapa de navegación con zonas por rol. | Dibuja bocetos de baja fidelidad que muestran qué va en cada pantalla y qué requisito lo pide. | Muestra los estados vacío, carga, error y confirmación, con mensajes que dicen qué pasó, por qué y qué hacer. | Aplica una lista de accesibilidad: etiquetas visibles, uso con teclado, foco visible y mensajes que no dependen del color. | Observa el uso del boceto con usuarios simulados, registra los problemas con evidencia y corrige el diseño. _(de lote_3/build/cap8.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Laboratorio 1.º, pp. 39-40 (HTML/CSS, formularios).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 15 | Diseñar recorridos y bocetos de pantallas. | C6 | Tres tareas completas en prototipo de baja fidelidad. | 0 | 5 | 0 | 0 | 0 | 0 | 0 |
| 16 | Revisar accesibilidad, mensajes y estados con usuarios simulados. | C6, C9 | Registro de problemas y bocetos corregidos. | 0 | 3 | 0 | 2 | 0 | 0 | 0 |

### Capítulo 9. Arquitectura y revisión del diseño (Unidad III; encuentros 17-18)

- **Capacidades del capítulo:** C1, C2, C3, C4, C5, C6, C7 (propuestas).
- **Secciones (Work §6):** 9.1. Presentación, reglas de negocio y persistencia. 9.2. Responsabilidades, entradas, salidas y contratos de operaciones. 9.3. Entorno, dependencias y decisiones técnicas justificadas. 9.4. Coherencia entre requisitos, datos e interfaces.
- **Cierre:** Evaluación integradora de la primera etapa: defensa y corrección del dossier; H3.
- **Indicadores:** Identifica qué hace la presentación, qué deciden las reglas de negocio y qué guarda la persistencia, y ubica cada regla del caso. | Escribe el contrato de una operación con sus entradas, precondiciones, resultado, errores y requisitos vinculados. | Registra una decisión técnica con su contexto, las condiciones excluyentes, las opciones, la decisión y sus consecuencias. | Comprueba la coherencia entre requisitos, datos, pantallas, operaciones y pruebas, y corrige los huecos. | Defiende el dossier de las Unidades I a III y resuelve individualmente una variante no vista. _(de lote_3/build/cap9.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Laboratorio 3.º, pp. 52-54 (ciclo de vida, responsabilidades); Laboratorio 2.º, pp. 50-52 (servidor web).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 17 | Diseñar responsabilidades, conexiones y entorno de ejecución. | C5, C6 | Esquema de arquitectura y decisión técnica. | 0 | 5 | 0 | 0 | 0 | 0 | 0 |
| 18 | Evaluación intermedia: defender análisis y diseño; corregir. | C1-C7 | H3: dossier consistente y evidencia individual. | 0 | 1 | 0 | 0 | 0 | 0 | 4 |

### Capítulo 10. Del diseño a la primera operación funcional (Unidad IV; encuentros 19-20)

- **Capacidades del capítulo:** C6, C7, C8, C9 (propuestas).
- **Secciones (Work §6):** 10.1. Preparación del entorno y estructura del proyecto. 10.2. Versiones, bitácora y conjunto inicial de datos ficticios. 10.3. Una operación completa: formulario, procesamiento y almacenamiento. 10.4. Validación, consulta parametrizada y evidencia de persistencia.
- **Cierre:** Práctica: demostrar una operación y vincularla con su requisito y prueba.
- **Indicadores:** Completa la ficha de entorno de su equipo con lo que se comprobó y lo que queda pendiente, sin dar por probado lo que no se probó. | Ubica cada archivo de la base en su capa y explica qué trae la base y qué construye el equipo. | Registra la primera versión del prototipo en la bitácora, con los datos ficticios con que se instaló. | Construye el alta de un ejemplar desde el formulario hasta la base, con validación en el servidor y consultas parametrizadas. | Demuestra que el dato sigue después de cerrar y volver a abrir la base, y vincula la operación con su requisito, su contrato y su prueba. _(de lote_4/build/cap10.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Laboratorio 2.º, pp. 47-49 (variables, funciones, GET/POST); Algorítmica 2.º, pp. 74-76 (modularización, validación).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 19 | Preparar entorno, estructura de trabajo, versiones y datos ficticios. | C7, C8 | Ejecución inicial reproducible; ficha de entorno. | 0 | 0 | 3 | 0 | 0 | 2 | 0 |
| 20 | Construir una operación mínima de extremo a extremo. | C6, C8, C9 | Formulario-servidor-BD; prueba de persistencia. | 0 | 1 | 3 | 1 | 0 | 0 | 0 |

### Capítulo 11. Catálogo, ejemplares y lectores (Unidad IV; encuentros 21-22)

- **Capacidades del capítulo:** C5, C6, C8 (propuestas).
- **Secciones (Work §6):** 11.1. Implementación de tareas priorizadas a partir de los bocetos. 11.2. Datos obligatorios, códigos, duplicados y mensajes útiles. 11.3. Permisos mínimos y comprobaciones del servidor. 11.4. Edición y baja lógica sin pérdida de historial.
- **Cierre:** Práctica: registrar un lote distinto del ejemplo y resolver entradas inválidas.
- **Indicadores:** Ordena las tareas del incremento a partir de los bocetos de PT-08 y de sus dependencias. | Lleva cada regla del diccionario a una validación del servidor y a una restricción de la base, con su mensaje. | Construye el alta y la corrección de obras, ediciones y lectores, y rechaza los códigos repetidos sin cambiar datos. | Comprueba en el servidor el permiso de cada pantalla y operación, y demuestra el rechazo de un acceso indebido. | Corrige datos y da de baja lectores y ejemplares sin borrar nada ni alterar el historial. _(de lote_4/build/cap11.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Laboratorio 3.º, pp. 54-55 (CRUD, SQL, restricciones; concurrente).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 21 | Implementar catálogo y control de ejemplares. | C5, C8 | Alta, consulta y edición con reglas de validación. | 0 | 1 | 3 | 1 | 0 | 0 | 0 |
| 22 | Implementar lectores y permisos mínimos. | C6, C8 | Validación en servidor; rechazo de acceso indebido. | 0 | 1 | 3 | 1 | 0 | 0 | 0 |

### Capítulo 12. Préstamos y devoluciones consistentes (Unidad IV; encuentros 23-24)

- **Capacidades del capítulo:** C5, C8, C9 (propuestas).
- **Secciones (Work §6):** 12.1. Precondiciones y reglas de la operación de préstamo. 12.2. Doble envío, disponibilidad y operaciones atómicas. 12.3. Devolución, estado del ejemplar y conservación de historial. 12.4. Fallos previsibles y comprobación de resultados.
- **Cierre:** Práctica: resolver dos solicitudes incompatibles y explicar la protección elegida.
- **Indicadores:** Construye el préstamo comprobando, en el orden del contrato, el permiso, el lector, el máximo de su tipo y el ejemplar. | Explica las dos protecciones de RI-01 y por qué hacen falta las dos. | Evita el doble envío del formulario y prueba la simultaneidad con procesos independientes, registrando el entorno. | Construye la devolución única, que cierra el préstamo correcto y conserva el historial. | Comprueba con una consulta que, después de cada prueba, no quedó ningún dato a medias ni dos préstamos activos de un ejemplar. _(de lote_4/build/cap12.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Laboratorio 3.º, pp. 54-55 (conexión a BD y consistencia; concurrente).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 23 | Implementar préstamo y prevención de duplicados. | C5, C8, C9 | Operación coherente ante reenvío o segunda solicitud. | 0 | 1 | 3 | 1 | 0 | 0 | 0 |
| 24 | Implementar devolución e historial. | C5, C8, C9 | Devolución única, conservación de referencias y pruebas. | 0 | 1 | 3 | 1 | 0 | 0 | 0 |

### Capítulo 13. Información útil e integración (Unidad IV; encuentros 25-26)

- **Capacidades del capítulo:** C3, C7, C8, C9 (propuestas).
- **Secciones (Work §6):** 13.1. Búsqueda de ejemplares disponibles y préstamos activos. 13.2. Vencimientos y fecha de referencia. 13.3. Integración de módulos y revisión del alcance mínimo. 13.4. Demostración del incremento y registro de pendientes.
- **Cierre:** Revisión de unidad IV: circuito funcional completo; H4.
- **Indicadores:** Construye la consulta pública de disponibilidad sin datos de lectores y la lista de préstamos activos para la bibliotecaria. | Calcula los vencidos respecto de una fecha de referencia escrita, para que el resultado se pueda comprobar. | Construye el informe mensual por curso al prestar y comprueba que la suma de los grupos coincide con el total. | Integra los módulos y revisa el prototipo contra el alcance mínimo, con la prueba de cada función. | Demuestra el circuito completo, registra las incidencias con su gravedad y destino, y resuelve individualmente una variante. _(de lote_4/build/cap13.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Laboratorio 3.º, pp. 54-55; Algorítmica 2.º, pp. 74-76 (filtros y consultas).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 25 | Construir consultas de disponibilidad y vencimientos. | C3, C8 | Reporte correcto con fecha de referencia definida. | 0 | 1 | 3 | 1 | 0 | 0 | 0 |
| 26 | Integrar y demostrar el incremento; revisar unidad IV. | C7-C9 | H4: prototipo completo mínimo y lista de incidencias. | 0 | 0 | 2 | 1 | 0 | 0 | 2 |

### Capítulo 14. Probar con criterios y datos independientes (Unidad V; encuentros 27-28)

- **Capacidades del capítulo:** C8, C9 (propuestas).
- **Secciones (Work §6):** 14.1. Verificación, validación y aceptación. 14.2. Casos normales, límites, excepciones y rechazos. 14.3. Resultado esperado, resultado obtenido y evidencia. 14.4. Cobertura de requisitos y reporte de defectos.
- **Cierre:** Práctica: elaborar y ejecutar una batería nueva de pruebas.
- **Indicadores:** Distingue verificar, validar y aceptar, y dice contra qué se compara cada una. | Diseña al menos doce casos identificados desde las reglas, seis de ellos de límite o de rechazo. | Prepara una copia descartable con datos independientes y comprueba su estado antes de probar. | Ejecuta los casos y registra requisito, esperado, obtenido, entorno y evidencia, sin dar por bueno lo que no se probó. | Encuentra los huecos de cobertura y reporta cada defecto con pasos para reproducirlo y su condición. _(de lote_5/build/cap14.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Laboratorio 3.º, p. 58 (TDD e integración continua como antecedentes concurrentes).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 27 | Diseñar cobertura y datos independientes de prueba. | C9 | Matriz con resultados esperados y requisitos cubiertos. | 0 | 0 | 0 | 5 | 0 | 0 | 0 |
| 28 | Ejecutar pruebas funcionales, límites y entradas inválidas. | C8, C9 | Resultados obtenidos e incidencias reproducibles. | 0 | 0 | 0 | 5 | 0 | 0 | 0 |

### Capítulo 15. Probar el sistema completo con usuarios (Unidad V; encuentros 29-30)

- **Capacidades del capítulo:** C3, C6, C8, C9, C10 (propuestas).
- **Secciones (Work §6):** 15.1. Pruebas de integración y persistencia. 15.2. Permisos, recuperación de datos y manejo de errores. 15.3. Sesiones de uso y observación de dificultades. 15.4. Aceptación por criterios acordados y prioridad de correcciones.
- **Cierre:** Práctica: revisión cruzada entre equipos con datos reservados para evaluación.
- **Indicadores:** Prueba el circuito completo y la persistencia entre ejecuciones, con la consulta del estado final. | Ejecuta todas las operaciones con las tres cuentas y comprueba que cada rechazo sea ME-13 sin cambiar datos. | Restaura un respaldo y comprueba que el estado es el del respaldo y que quedó la copia previa. | Conduce o registra una sesión de uso con tareas nuevas, anotando lo que la persona hace y no opiniones. | Marca cada criterio de aceptación con su evidencia y prioriza las correcciones dentro del alcance. _(de lote_5/build/cap15.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Laboratorio 3.º, pp. 54-55 (persistencia); Hardware 2.º, pp. 66-69 (respaldos y entorno).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 29 | Probar integración, permisos, persistencia y restauración. | C8-C10 | Evidencia del circuito completo y recuperación. | 0 | 0 | 0 | 5 | 0 | 0 | 0 |
| 30 | Realizar sesiones de uso y prueba de aceptación. | C3, C6, C9 | Observaciones de dos usuarios/roles y prioridades. | 1 | 0 | 0 | 4 | 0 | 0 | 0 |

### Capítulo 16. Corregir y volver a comprobar (Unidad V; encuentros 31-32)

- **Capacidades del capítulo:** C7, C8, C9 (propuestas).
- **Secciones (Work §6):** 16.1. Diagnóstico de incidencias e impacto de cambios. 16.2. Corrección, revisión entre pares y regresión. 16.3. Actualización de modelos, pruebas y documentación. 16.4. Recuperación técnica y versión candidata.
- **Cierre:** Revisión de unidad V: evidencia de calidad y límites conocidos; H5.
- **Indicadores:** Reproduce una incidencia con pasos que se repiten y distingue el síntoma de la causa y la capa. | Estima el impacto de una corrección con la trazabilidad y elige las pruebas de regresión. | Corrige con el cambio mínimo, hace revisar la corrección por otro integrante y ejecuta la regresión. | Actualiza requisitos, contratos, mensajes, pruebas y bitácora cuando se aprueba un cambio, con su versión. | Presenta una versión candidata con sus límites conocidos y revisa una por una las condiciones mínimas. _(de lote_5/build/cap16.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Laboratorio 3.º, p. 58 (revisión entre pares y mejora).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 31 | Corregir problemas y repetir pruebas afectadas. | C7-C9 | Registro de regresión; trazabilidad actualizada. | 0 | 0 | 2 | 3 | 0 | 0 | 0 |
| 32 | Recuperación técnica y revisión de unidad V. | C8, C9 | H5: versión candidata con límites conocidos. | 0 | 0 | 2 | 1 | 0 | 0 | 2 |

### Capítulo 17. Preparar una entrega reproducible (Unidad VI; encuentros 33-34)

- **Capacidades del capítulo:** C7, C10 (propuestas).
- **Secciones (Work §6):** 17.1. Guía de instalación, configuración y ejecución. 17.2. Manual breve basado en tareas. 17.3. Respaldo, restauración, licencias y registro de procedencia. 17.4. Prueba de instalación por otro equipo y acta de entrega simulada.
- **Cierre:** Práctica: entregar código, datos, pruebas y documentación coherentes; H6.
- **Indicadores:** Escribe una guía de instalación con requisitos, comandos exactos, resultado esperado y qué hacer si falla, y la prueba al pie de la letra en una carpeta limpia. | Escribe un manual por tareas que una persona ajena al desarrollo puede seguir, con el significado de cada mensaje. | Documenta el respaldo y la restauración como tareas y registra la procedencia y la licencia de cada recurso. | Instala el paquete de otro equipo sin ayuda, registra cada paso con su mensaje y completa el acta de entrega. | Corrige el paquete con lo observado y entrega código, datos, pruebas y documentación coherentes, con sus límites. _(de lote_6/build/cap17.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Software 1.º, pp. 59-63 (licencias, procedencia); Hardware 2.º, pp. 66-69 (instalación y respaldos).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 33 | Redactar guía de uso, instalación, respaldo y límites. | C10 | Documentación probada por el propio equipo. | 0 | 0 | 0 | 0 | 5 | 0 | 0 |
| 34 | Entregar a otro equipo para instalación y revisión. | C7, C10 | H6: paquete reproducible; ajustes finales. | 0 | 0 | 0 | 2 | 2 | 0 | 1 |

### Capítulo 18. Demostrar, defender y aprender del proyecto (Unidad VI; encuentros 35-36)

- **Capacidades del capítulo:** C1, C2, C3, C4, C5, C6, C7, C8, C9, C10 (propuestas).
- **Secciones (Work §6):** 18.1. Demostración organizada por requisitos y evidencias. 18.2. Defensa individual de decisiones y resolución de una variante. 18.3. Recuperación de aprendizajes pendientes. 18.4. Retrospectiva y mejoras futuras justificadas.
- **Cierre:** Evaluación integradora de la segunda etapa y cierre del proyecto.
- **Indicadores:** Demuestra el sistema con un guion que va de cada requisito imprescindible a su evidencia, en el tiempo acordado. | Explica, solo, una decisión del proyecto y una prueba, con su evidencia. | Resuelve una variante nueva: ubica el cambio en el requisito, el modelo, los contratos y las capas, y elige las pruebas. | Comunica qué está aceptado, qué no y qué queda pendiente, sin exagerar ni ocultar. | Propone mejoras futuras apoyadas en límites, incidencias u observaciones registradas, con su prioridad. _(de lote_6/build/cap18.py)_
- **Antecedentes MEC con los que se articula** (páginas según Work §3; asignación al capítulo propuesta por esta estructura): Orientaciones de evaluación por competencias, pp. 95-106 (evidencia individual).

| Encuentro | Foco (Work §5.2) | Capacidades | Evidencia o evaluación (Work §5.2) | A | D | P | V | Doc | G | E |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 35 | Demostración y defensa individual del proyecto. | C1-C10 | Rúbrica de producto y preguntas de transferencia. | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| 36 | Recuperación individual, retrospectiva y cierre. | C7, C9, C10 | Evidencia faltante, balance y propuesta de continuidad. | 0 | 0 | 0 | 0 | 0 | 2 | 3 |

## 5. Totales

| A | D | P | V | Doc | G | E | Total |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 48 | 31 | 27 | 36 | 7 | 8 | 23 | 180 |

## 6. Evaluación (Work §4.3)

- Evaluación continua basada en evidencias, con diagnóstico inicial, revisiones de unidad (H1, H2, H4, H5), evaluación intermedia (H3, encuentro 18), entrega (H6, encuentro 34) y defensa individual (encuentro 35).
- Ponderación editorial sugerida: problema y relevamiento 15 %; requisitos y trazabilidad 20 %; modelos y diseño 20 %; prototipo e integración 20 %; pruebas y mejora 15 %; documentación y defensa 10 %. No es una escala oficial del MEC.
- En cada criterio, 60 % de evidencia del producto compartido y 40 % de evidencia individual (propuesta editorial).
- Niveles de desempeño: 4 Sólido, 3 Logrado, 2 En desarrollo, 1 Inicial; la ausencia de evidencia se registra aparte.

## 7. Lo que falta para el plan anual definitivo

- Indicadores: los 18 capítulos ya tienen su ficha; el plan definitivo los revisa contra el tomo unificado aprobado.
- Procedimientos e instrumentos por encuentro, con unicidad dentro del año (como en el formato canónico de la colección).
- Calendario por etapas del año escolar y adaptación de 28 encuentros (distribución v2.1, `distribucion_28.csv`).
- Maquetación en oficio con el formato canónico de la colección, y cotejo con las fichas del libro aprobado.
