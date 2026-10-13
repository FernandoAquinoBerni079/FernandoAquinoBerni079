# Propuesta de integración del PEC en Desarrollo Personal y Social 7.º

Versión candidata para la auditoría de ChatGPT · 13/10/2026 · Constructor: Claude · Aprobación: Fer.
Fuente de la arquitectura: `build/curriculo.py`. Ningún original ni archivo de Drive se modificó: las copias de trabajo de los originales están en `originales/`, con sus SHA-256.

## 1. Matriz de capacidades oficiales y cobertura curricular

Fuente: programa de estudio de Desarrollo Personal y Social, 7.º grado, MEC (Drive `1EkkOgUbux0RQPwkw4GYGnUeDpb8_UldE`, págs. 55–57). Las capacidades se transcriben literalmente, incluidas la puntuación y las erratas del original. Los dos puntos con que el programa introduce los temas (capacidades 1, 3 y 18) se cierran con punto.

| # | Capacidad del programa MEC (literal) | Unidad | Temas MEC | Encuentros que la desarrollan | Talleres PEC que la movilizan |
|---|---|---|---|---|---|
| 1 | Valora la importancia de integrarse y pertenecer a la comunidad educativa. | 1. Sentido de pertenencia | Historia de la institución: fundador, primeros directivos, etc.; Identidad e integración a la comunidad educativa.; Proyecto Educativo Institucional. | 1 (Clase 1), 3 (Clase 3); evaluada en 4 (U1) | 17 (Taller 1), 19 (Taller 2), 24 (Taller 3), 35 (Taller 7) |
| 2 | Reconoce la organización interna de la institución educativa. | 1. Sentido de pertenencia | Organigrama de la institución.; Miembros de la institución educativa (directores, docentes, alumnos, otros). Funciones.; Dependencias de la institución. | 2 (Clase 2); evaluada en 4 (U1) | 17 (Taller 1), 19 (Taller 2) |
| 3 | Reconoce sus fortalezas, debilidades, intereses, habilidades y oportunidades para construir su proyecto de vida. | 2. Autoconocimiento | Autoconocimiento. Técnicas y procesos.; Autoestima; Autovaloración; Asertividad | 5 (Clase 4), 6 (Clase 5); evaluada en 8 (U2) | — |
| 4 | Expresa su habilidad de sentir, pensar y actuar como elementos que se observan en el proceso del autoconocimiento. | 2. Autoconocimiento | Pensamiento crítico y objetivo. | 7 (Clase 6); evaluada en 8 (U2) | 34 (Taller 6) |
| 5 | Valora la relación afectiva positiva entre los miembros de la familia y de su entorno. | 3. Vida afectiva | Relaciones afectivas saludables (en la familia, con los compañeros, con los amigos); Noviazgo: implicancia, compromiso. | 9 (Clase 7); evaluada en 12 (U3) | — |
| 6 | Analiza las causas y las consecuencias del uso y abuso de la tecnología como elemento que afecta la relación personal directa y afectiva (celulares, Internet, otros) en el marco de la convivencia familiar y/ social. | 3. Vida afectiva | Influencia emocional, positiva y negativa, de los teléfonos celulares y de Internet con sus redes sociales. | 10 (Clase 8); evaluada en 12 (U3) | — |
| 7 | Reconoce que los cambios que se generan en la pubertad y en la adolescencia forman parte de una etapa de la vida. | 3. Vida afectiva | Influencia de los cambios en su afectividad.; Formas de afrontar esos cambios. | 11 (Clase 9); evaluada en 12 (U3) | — |
| 8 | Analiza los artículos referentes a sus derechos y sus responsabilidades considerando su formación como ciudadano. | 4. Derechos y responsabilidades | Código de la Niñez y la Adolescencia.; Derechos Humanos.; Derechos sexuales y derechos reproductivos. | 13 (Clase 10); evaluada en 16 (U4) | — |
| 9 | Reflexiona sobre los principales artículos relacionados con la No discriminación, expresados en el Código de la Niñez y la Adolescencia, la convención de los Derechos Humanos y de los Derechos sexuales y Derechos reproductivos. | 4. Derechos y responsabilidades | El respeto como valor universal.; Respeto a la diversidad.; Tolerancia. | 14 (Clase 11); evaluada en 16 (U4) | — |
| 10 | Reconoce la importancia de conocer las leyes que protegen a los niños, las niñas y los adolescentes. y, además, que cada derecho lleva implícito una responsabilidad. | 4. Derechos y responsabilidades | Identificación de responsabilidades a partir de los derechos. | 15 (Clase 12); evaluada en 16 (U4) | — |
| 11 | Identifica los diferentes tipos de liderazgo. | 5. Organizaciones estudiantiles | Liderazgo: Concepto. Tipos. Características. | 20 (Clase 13); evaluada en 23 (U5) | 29 (Taller 4) |
| 12 | Participa con actitud democrática en el proceso de elección del Parlamento Escolar. | 5. Organizaciones estudiantiles | Parlamento Escolar: Concepto. Conformación. Deberes. Responsabilidades.; Conformación del Parlamento Escolar; Derecho a la participación; Participación protagónica. | 21 (Clase 14); evaluada en 23 (U5) | — |
| 13 | Valora la importancia de una correcta elección de autoridades y su incidencia en la vida del grupo. | 5. Organizaciones estudiantiles | Proceso electoral en el grado; Proceso electoral en la institución. | 22 (Clase 15); evaluada en 23 (U5) | — |
| 14 | Asume la responsabilidad de pertenecer a un grupo considerando sus habilidades y/o intereses. | 5. Organizaciones estudiantiles | Clubes: Concepto, Objetivos, Organización, Tipos. | 22 (Clase 15); evaluada en 23 (U5) | 24 (Taller 3), 29 (Taller 4), 32 (Taller 5), 34 (Taller 6), 35 (Taller 7) |
| 15 | Analiza las condiciones de organización para el estudio. | 6. Organización y planificación | Condiciones que afectan positiva o negativamente al estudio y al aprendizaje: psicológicas, fisiológicas, ambientales, materiales. | 25 (Clase 16); evaluada en 28 (U6) | — |
| 16 | Planifica adecuadamente su tiempo para el estudio. | 6. Organización y planificación | Organización del tiempo.; Concienciación del tiempo que se dedica al estudio. | 26 (Clase 17), 27 (Clase 18); evaluada en 28 (U6) | — |
| 17 | Identifica las medidas de prevención y mitigación en situaciones de riesgos. | 7. Gestión de riesgo | Físico: Violencia; Psicológico: Prevención. Mitigación. Emergencia.; Ambiental: Desastre. Factores de riesgo. Violencia. | 30 (Clase 19); evaluada en 33 (U7) | 32 (Taller 5) |
| 18 | Aplica normas de comportamiento en caso de riesgos. | 7. Gestión de riesgo | Físicos; Psicológicos; Ambientales: Incendio. Interrupción de energía eléctrica. Falta de suministro de agua potable. Tormenta. | 31 (Clase 20); evaluada en 33 (U7) | — |

**Resultado:** las 18 capacidades tienen al menos una clase temática y su evaluación de unidad.

**Cotejo con el libro anterior.** En 11 de sus 21 fichas, la capacidad no era literal:
- Clases 3, 5, 6, 8, 9, 11, 12, 14, 15, 18, 20 y 21: paráfrasis, fusiones o agregados («e inicia la construcción de su proyecto de vida», «y participa en la construcción de las normas de convivencia», «leyes e instituciones»).
- Clases 18 y 21: capacidades que no figuran en el programa («Planifica su tiempo y establece metas para su proyecto de vida», «Integra los aprendizajes del año en su proyecto de vida y reconoce su red de apoyo»).

En la versión candidata, todas las fichas citan la capacidad literal de `curriculo.CAP`.

**El PEC no tiene capacidades propias en el programa.** Por eso la ficha de cada taller muestra:
- el **propósito literal del componente**: «Con este componente, se pretende que niños, niñas y adolescentes desarrollen capacidades que les ayuden a planificar, implementar y evaluar proyectos de servicio social, con el fin de mejorar y transformar el entorno en el cual se desenvuelven en un marco de compromiso con la sociedad.»;
- las **capacidades del área vinculadas** (literales);
- **indicadores de logro rotulados como elaboración editorial**.

Así no se atribuye al MEC ninguna capacidad, indicador ni carga horaria que no figure en la fuente.

**Distribución horaria.** El área tiene 3 HC semanales («a ser distribuida conforme necesidades entre Orientación y Proyecto Educativo Comunitario»). No se agregan horas para el PEC.

**Programas de 8.º y 9.º.** En Drive no hay versión oficial completa: para 8.º solo hay un extracto de capacidades sin la sección del PEC, y para 9.º, un planeamiento de 2022. Quedan pendientes para los combos de 8.º y 9.º. No afectan a 7.º.

## 2. Propuesta de integración del PEC dentro de los 36 encuentros

Perspectiva de 7.º: **«La escuela como una comunidad»**. Siete talleres que acompañan un proyecto real del grado de **junio a noviembre**, el período del cronograma del esquema MEC. Las ocho etapas pedidas por Fernando quedan cubiertas:

| Taller | Encuentro | Mes | Etapa del proyecto | Producto (bitácora) |
|---|---|---|---|---|
| 1 | 17 | Junio | Introducción y comprensión del proyecto; identificación de necesidades | Guía de observación y encuesta breve aplicadas |
| 2 | 19 | Agosto | Diagnóstico participativo y priorización de problemas | Matriz de priorización y árbol de problemas |
| 3 | 24 | Agosto | Formulación I: eje, fundamentación, objetivos y beneficiarios | Ficha del proyecto (apartados 1 a 7) |
| 4 | 29 | Septiembre | Formulación II: actividades, cronograma, recursos; organización y responsabilidades | Cronograma, recursos y roles (apartados 8 a 12) |
| 5 | 32 | Octubre | Ejecución y seguimiento | Registro semanal de seguimiento con evidencias |
| 6 | 34 | Noviembre | Evaluación de resultados (L / NL / NM) | Evaluación con indicadores (apartado 13) |
| 7 | 35 | Noviembre | Socialización de aprendizajes y cierre del año | Presentación a la comunidad educativa e informe final |

**Entre talleres** la ejecución se hace en horario escolar (recreos, espacios institucionales), con autorización de la dirección y de las familias cuando corresponda. La docente registra las evidencias en la bitácora y en el portafolio del proyecto: no hay actividades sin seguimiento.

**Qué recibe la docente en el libro:**
- 7 talleres explicados;
- un proyecto modelo completo con los 13 apartados («Recreo en armonía», de la institución ficticia Colegio Arasa Poty);
- un banco de 6 proyectos para adaptar;
- fichas reproducibles de la bitácora.

**En el solucionario:**
- guía de conducción por taller;
- evidencias, rúbricas y listas de cotejo;
- modelo de nota a las familias;
- rúbrica final del proyecto.

**De dónde salen los siete encuentros, sin perder capacidades de Orientación:**
- **Seis continuaciones prácticas.** No tenían capacidad propia: profundizaban capacidades ya trabajadas. Su actividad se integra en la clase correspondiente:
  - C1 → Clase 2;
  - C2 → Clase 14;
  - C3 → Clase 15;
  - C4 → Clase 16;
  - C5 → Clase 18;
  - C6 → Clase 19.
- **La antigua Clase 21 «Cierre del año».** Su capacidad no figuraba en el programa. La red de apoyo pasa a la Clase 12 y el cierre del año y del proyecto de vida, al Taller PEC 7.

Las 18 capacidades conservan su clase y su evaluación. Las clases se amplían para absorber las actividades prácticas.

## 3. Comparación entre la planificación original y la nueva

| Rubro | Antes | Ahora |
|---|---|---|
| Clases temáticas (Orientación) | 21 | 20 |
| Continuaciones prácticas | 6 | 0 (integradas en sus clases) |
| Talleres del Proyecto Educativo Comunitario | 0 | 7 |
| Evaluaciones de unidad | 7 | 7 |
| Evaluaciones integradoras de etapa | 2 | 2 |
| Total de encuentros / HC | 36 / 108 | 36 / 108 |
| Primera etapa / segunda etapa | 18 / 18 | 18 / 18 |
| Horas del área dedicadas al PEC en el aula | 0 | 21 HC (7 encuentros), dentro de las 108 |

Encuentro por encuentro:

| N.º | Antes (paquete del 12/10/2026) | Ahora (versión candidata) | Componente | Capacidades MEC |
|---|---|---|---|---|
| 1 | Bienvenida al tercer ciclo: pertenecer | Clase 1 — Bienvenida al tercer ciclo: pertenecer | Orientación | 1 |
| 2 | Cómo se organiza mi colegio | Clase 2 — Cómo se organiza mi colegio | Orientación | 2 |
| 3 | El PEI y las normas de convivencia | Clase 3 — El PEI, los proyectos de la escuela y las normas de convivencia | Orientación | 1 |
| 4 | Continuación práctica — Mi horario y cómo me evaluarán este año | Evaluación de la Unidad 1 — Sentido de pertenencia | Evaluación de unidad | U1 |
| 5 | Evaluación de la Unidad 1 — Sentido de pertenencia | Clase 4 — ¿Quién soy? Fortalezas, debilidades, intereses y habilidades | Orientación | 3 |
| 6 | ¿Quién soy? Fortalezas y habilidades | Clase 5 — Autoestima, autovaloración y asertividad | Orientación | 3 |
| 7 | Autoestima, autovaloración y asertividad | Clase 6 — Sentir, pensar y actuar: el pensamiento crítico | Orientación | 4 |
| 8 | Sentir, pensar y actuar: mi proyecto de vida | Evaluación de la Unidad 2 — Autoconocimiento | Evaluación de unidad | U2 |
| 9 | Evaluación de la Unidad 2 — Autoconocimiento | Clase 7 — Relaciones afectivas saludables | Orientación | 5 |
| 10 | Relaciones afectivas saludables | Clase 8 — Tecnología, redes y convivencia | Orientación | 6 |
| 11 | Tecnología, redes y convivencia digital | Clase 9 — Los cambios de la pubertad y la adolescencia | Orientación | 7 |
| 12 | Los cambios de la adolescencia | Evaluación de la Unidad 3 — Vida afectiva | Evaluación de unidad | U3 |
| 13 | Evaluación de la Unidad 3 — Vida afectiva | Clase 10 — Mis derechos y mis responsabilidades | Orientación | 8 |
| 14 | Mis derechos y mis responsabilidades | Clase 11 — No discriminación, respeto y tolerancia | Orientación | 9 |
| 15 | No discriminación, respeto y tolerancia | Clase 12 — Las leyes que me protegen: cada derecho, una responsabilidad | Orientación | 10 |
| 16 | Quién me protege: mi red de protección | Evaluación de la Unidad 4 — Derechos y responsabilidades | Evaluación de unidad | U4 |
| 17 | Evaluación de la Unidad 4 — Derechos y responsabilidades | Taller PEC 1 — Nuestra escuela como comunidad: qué es un Proyecto Educativo Comunitario | Proyecto Educativo Comunitario | 1, 2 |
| 18 | Evaluación integradora de la 1.ª etapa | Evaluación integradora — Primera etapa (Unidades 1 a 4) | Evaluación de etapa | U1–U4 |
| 19 | Liderazgo: ser un líder proactivo | Taller PEC 2 — Diagnóstico participativo: conocer y priorizar las necesidades | Proyecto Educativo Comunitario | 1, 2 |
| 20 | El Parlamento Escolar | Clase 13 — Liderazgo: tipos y características | Orientación | 11 |
| 21 | Continuación práctica — Leer las reglas antes de participar | Clase 14 — El Parlamento Escolar y la participación protagónica | Orientación | 12 |
| 22 | Elecciones en el grado y clubes | Clase 15 — Elecciones en el grado y clubes | Orientación | 13, 14 |
| 23 | Continuación práctica — Simulación participativa conforme al reglamento | Evaluación de la Unidad 5 — Organizaciones estudiantiles | Evaluación de unidad | U5 |
| 24 | Evaluación de la Unidad 5 — Organizaciones estudiantiles | Taller PEC 3 — Elegir y fundamentar nuestro proyecto: eje, objetivos y beneficiarios | Proyecto Educativo Comunitario | 1, 14 |
| 25 | Las condiciones para estudiar | Clase 16 — Las condiciones para estudiar | Orientación | 15 |
| 26 | Continuación práctica — Auditoría de condiciones para estudiar | Clase 17 — Organizá tu tiempo: el estudio como hábito | Orientación | 16 |
| 27 | Organizá tu tiempo: el estudio como hábito | Clase 18 — Mi plan semanal de estudio y mis metas | Orientación | 16 |
| 28 | Mi plan y mis metas | Evaluación de la Unidad 6 — Organización y planificación | Evaluación de unidad | U6 |
| 29 | Continuación práctica — Una semana real: probar y ajustar mi plan | Taller PEC 4 — Planificar el proyecto: actividades, cronograma, recursos y responsables | Proyecto Educativo Comunitario | 11, 14 |
| 30 | Evaluación de la Unidad 6 — Organización y planificación | Clase 19 — Prevención y mitigación frente a los riesgos | Orientación | 17 |
| 31 | Prevención, mitigación/reducción y respuesta | Clase 20 — Normas de comportamiento en caso de riesgos | Orientación | 18 |
| 32 | Continuación práctica — Mapa de riesgos y simulación segura | Taller PEC 5 — Ejecutar con seguridad y hacer el seguimiento | Proyecto Educativo Comunitario | 14, 17 |
| 33 | Actuar en emergencias y frente a la violencia | Evaluación de la Unidad 7 — Gestión de riesgo | Evaluación de unidad | U7 |
| 34 | Cierre del año: mi red y mi proyecto de vida | Taller PEC 6 — Evaluar los resultados del proyecto | Proyecto Educativo Comunitario | 4, 14 |
| 35 | Evaluación de la Unidad 7 — Gestión de riesgo | Taller PEC 7 — Socializar lo aprendido y cerrar el año | Proyecto Educativo Comunitario | 1, 14 |
| 36 | Evaluación integradora de la 2.ª etapa | Evaluación integradora — Segunda etapa (Unidades 5 a 7) | Evaluación de etapa | U5–U7 |

Ajuste a fundamentar: la Unidad 5 se adelanta a agosto y el Taller PEC 2 queda en el encuentro 19. Así el diagnóstico participativo se hace al volver de las vacaciones de invierno, con los datos relevados en junio.
