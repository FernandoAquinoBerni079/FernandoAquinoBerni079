# Plan del primer lote editorial — Capítulos 1 a 3 (Unidad I)

**Proyecto:** Biblioteca Comercial 2026 — Análisis y Diseño de Sistemas, 3.º BTI (Plan Optativo).

**Estado:** plan listo para aprobar. **No se construye nada hasta la autorización expresa de Fernando.** No se suben maestros a Drive.

**Fuentes:**
- informe de Work v0.1 (SHA-256 `3d4f5ab9…065069a`): §4.2 capacidades, §5.2 encuentros 1 a 6, §6 índice, §7 caso;
- `fase2_pilotos/A1_candidato_capitulo2/integracion/` (plan del Capítulo 2);
- el Capítulo 4 v2, cuyas fuentes el lote debe respetar.

## 1. Decisiones de base

Las recomendó la auditoría y se adoptan para planificar. Su aprobación formal corresponde a Fernando.

| Decisión | Consecuencia para el lote |
|---|---|
| 180 HC (36 encuentros de 5 HC), con la adaptación de 28 encuentros como opción | El lote cubre los encuentros 1 a 6 (30 HC). En el plan de 28, los encuentros 5 y 6 se unen y el Capítulo 3 se da en un encuentro. |
| Mapa de interesados en el Capítulo 1 | Se traslada desde el candidato (Ejemplo resuelto y Figura 4.1) a la sección 1.3 |
| Reglas RN-01 a RN-06 como supuestos didácticos | El lote no las usa todavía. El Capítulo 3 puede anticiparlas como «reglas a negociar» sin numerarlas. |
| Permisos mínimos en el núcleo | El Capítulo 3 los menciona en el alcance mínimo (Work §7.2) |
| Identidad verde BTI y 5 HC semanales | Siguen provisionales |
| Capacidades | Siempre «propuesta para el programa institucional; no es una capacidad oficial del MEC» |

## 2. Contenido del lote

### Capítulo 1. Un sistema comienza con una necesidad (encuentros 1 y 2)

- **Capacidades (Work):**
  - C1: «Delimita un problema y evalúa la factibilidad de una solución.»
  - C7, en parte: «Organiza y registra el trabajo colaborativo», solo en el acuerdo de trabajo y el mapa de apoyos.
- **Secciones (Work §6):**
  - 1.1 De la dificultad cotidiana al problema de información.
  - 1.2 Personas, procesos, datos, recursos y límites del sistema.
  - 1.3 Actores e interesados: necesidades diferentes, decisiones compartidas.
  - 1.4 Diagnóstico de conocimientos previos y plan de apoyo.
- **Práctica (Work):** describir una biblioteca y separar hechos, supuestos y soluciones anticipadas.
- **Evidencias:**
  - encuentro 1: resolución individual breve y mapa de apoyos;
  - encuentro 2: ficha de problema y mapa de actores.
- **Recursos que se reutilizan:**
  - el mapa de interés e influencia del candidato: Figura 4.1, Ejemplo resuelto 4.1 y su tabla, renumerados a 1.x;
  - la caja «El caso del libro».
- **Para no duplicar Algorítmica 3.º:**
  - en 1.2, «datos» se trata como qué información usa cada persona, no como tablas;
  - no se reusa el cuaderno de préstamos de la Práctica 5 de Algorítmica ni sus personas (Lucía Ortiz, Marcos Rojas, Ana Paula Vera) ni sus títulos.
- **Diagnóstico de entrada (1.4):** programación, formularios, datos y comunicación, según Work encuentro 1.
  - Sin nota.
  - Alimenta el mapa de apoyos y la coordinación con Laboratorio y Algorítmica (Work §3).

### Capítulo 2. Investigar antes de diseñar (encuentros 3 y 4)

- **Capacidad (Work):** C2. **Secciones 2.1 a 2.4** y práctica con roles de bibliotecario, lector y dirección.
- **Se construye según** `A1_candidato_capitulo2/integracion/PLAN_INTEGRACION_CAPITULO_2.md`:
  - 8 elementos se conservan, 15 se adaptan y 1 se divide;
  - 3 elementos se trasladan al Capítulo 1;
  - se retiran los 4 de redacción de requisitos, que ya están en el Capítulo 4.
- **Lo que falta escribir:**
  - análisis de documentos (2.2);
  - necesidades no expresadas (2.3);
  - autorización, anonimización y resguardo de datos (2.4);
  - la simulación con roles del encuentro 4.
- **Condición de coherencia.** El dossier del capítulo incluye los registros **E1, E3, E4 y E5** con las mismas líneas que cita el Capítulo 4 v2, y cierra con la lista de necesidades N-01, N-02… (N-02 = «evitar entregar a dos lectores el mismo ejemplar», fuente E4-L4).

### Capítulo 3. Elegir un alcance posible (encuentros 5 y 6)

- **Capacidades (Work):** C1, C2 y C7.
- **Secciones (Work §6):**
  - 3.1 Objetivos y resultados esperados.
  - 3.2 Comparación de alternativas y factibilidad básica.
  - 3.3 Recursos, riesgos, límites y exclusiones.
  - 3.4 Acuerdo de proyecto y organización del equipo.
- **Cierre:** revisión de la Unidad I, con la defensa del problema y del alcance (**hito H1**).
- **Evidencias (Work):**
  - encuentro 5: matriz de factibilidad y riesgos;
  - encuentro 6: H1, con el problema y el alcance defendidos, más las correcciones.
- **Alternativas que se comparan (Work, encuentro 5):** registro manual mejorado, herramienta existente y prototipo.
- **Para no duplicar Algorítmica 3.º** (atención especial). La Práctica 4 de Algorítmica ya hace una **matriz de decisión ponderada para elegir la tecnología** de la biblioteca: web, escritorio o app, con pesos 0,5, 0,3 y 0,2. Por eso el Capítulo 3:
  - **no** usa una matriz ponderada ni compara tecnologías;
  - compara **tipos de solución** con una factibilidad cualitativa (operativa, técnica, económica y de calendario) y una tabla de riesgos con probabilidad, impacto y mitigación;
  - remite a la Práctica 4 de Algorítmica para quien quiera ponderar.
- **Alcance mínimo y exclusiones:** se toman de Work §7.2.
  - **Núcleo:** catálogo y ejemplares, lectores, préstamo, devolución, consultas, permisos mínimos, persistencia y entrega.
  - **Fuera del núcleo:** pagos, códigos de barras, reservas en línea, app móvil, entre otras.
- **Rúbrica de H1** en la guía, con los niveles de desempeño de Work (Sólido, Logrado, En desarrollo, Inicial), con 60 % de evidencia grupal y 40 % individual (Work §4.3).

### Preliminares del libro (propuesta, a decidir)

Work (§6) prevé los preliminares del libro: presentación, cómo usar el libro, mapa de capacidades y evidencias, acuerdo de trabajo, diagnóstico de entrada, presentación del caso, uso responsable de datos y guía de consulta a otras asignaturas. **Se propone incluirlos en este lote**, porque el diagnóstico del encuentro 1 y el acuerdo de trabajo los necesitan. Requiere decisión.

## 3. Fuente única de los datos del caso

Antes de escribir, se crea un módulo único del caso (`caso/dossier.py`) con:
- la institución y las personas ficticias;
- los registros E1 a E5 y O1, numerados por línea;
- los documentos (reglamento e informe mensual);
- las necesidades N-xx.

Los Capítulos 1 a 3, y el Capítulo 4 en su próxima versión, toman sus fuentes de ahí. Un control comprueba que todo código citado (E1-L4, N-02…) exista y que las citas textuales coincidan.

## 4. Entregables del lote

| Entregable | Contenido | Extensión estimada |
|---|---|---|
| Libro del estudiante, Capítulos 1 a 3 (DOCX y PDF de control) | Por capítulo: <ul><li>ficha;</li><li>cuatro secciones;</li><li>al menos dos ejemplos resueltos y una figura original;</li><li>actividades en cuatro bloques;</li><li>práctica en tres niveles con datos distintos de los ejemplos;</li><li>evaluación opcional en página propia;</li><li>recuadro para calendario reducido.</li></ul> | 45 a 55 págs. (más 6 a 8 de preliminares, si se aprueban) |
| Guía docente, Capítulos 1 a 3 (DOCX y PDF de control) | Secuencia por encuentro en HC; claves; listas de cotejo; rúbrica de H1; procedencia de recursos | 18 a 22 págs. |
| Controles automáticos | <ul><li>alineación con el índice de Work;</li><li>rótulo de las capacidades;</li><li>trazabilidad de fuentes contra el módulo del caso;</li><li>voseo;</li><li>maqueta (filas no divisibles, anchos fijos, evaluación en página propia, sin renglones sueltos);</li><li>ningún dato del caso de Algorítmica 3.º, incluida la matriz ponderada de su Práctica 4;</li><li>prueba con tres fuentes de sustitución.</li></ul> | — |
| Informe de lote | Archivos, SHA-256, resultados de los controles y decisiones pendientes | — |

Se reutilizan los scripts de maqueta del piloto (`helpers.py`, `maqueta.py`) con su comportamiento actual: anchos fijos con `tblGrid`, encabezado repetido y consignas unidas a sus renglones.

## 5. Orden de trabajo y puntos de control

1. Módulo del caso y control de fuentes, incluido el control contra el Capítulo 4 v2.
2. Capítulo 1, que incorpora el mapa de interesados.
3. Capítulo 2, según el plan de integración.
4. Capítulo 3 con la rúbrica de H1.
5. Preliminares, si se aprueban.
6. Guía docente del lote.
7. Controles, PDF de control, prueba de fuentes, informe y commit.
8. Auditoría independiente de ChatGPT, con los DOCX y PDF a disposición.
9. Aprobación de Fernando.

## 6. Riesgos

| Riesgo | Tratamiento |
|---|---|
| Duplicar la matriz ponderada de Algorítmica 3.º en 3.2 | Comparación cualitativa de tipos de solución, más un control automático |
| Incoherencia de fuentes entre el Capítulo 2 y el Capítulo 4 | Módulo único del caso y control de citas |
| Que el diagnóstico de entrada (1.4) suponga saberes de 3.º | Se limita a los antecedentes de 1.º y 2.º (Work §3); los contenidos de 3.º se tratan como concurrentes |
| Que el H1 grupal oculte el desempeño individual | Rúbrica con 40 % de evidencia individual (Work §4.3) |
| Que la auditoría visual no pueda hacerse | Los DOCX y PDF se publican en la rama, con sus SHA-256, desde el primer commit del lote |

## 7. Decisiones que necesita Fernando para empezar

1. Autorizar la construcción del lote 1.
2. Incluir o no los preliminares del libro en este lote.
3. Confirmar el caso ficticio (Colegio Técnico Arapoty y sus personas) para toda la colección.
4. Confirmar la rúbrica de H1 con los niveles y la proporción 60/40 de Work.
