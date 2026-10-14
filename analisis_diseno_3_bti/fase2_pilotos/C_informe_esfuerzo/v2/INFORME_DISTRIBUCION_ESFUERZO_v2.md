# Piloto C, versión 2 — Distribución del esfuerzo sobre la secuencia de Work

**Proyecto:** Análisis y Diseño de Sistemas, 3.º BTI (Plan Optativo, 5 HC semanales).
**Estado:** candidato para reauditoría.

**Archivos:**
- La versión 1 (`../INFORME_DISTRIBUCION_ESFUERZO.md`) queda sin cambios y **reemplazada** por esta. Usaba una estructura supuesta que no coincidía con la de Work.

**Base:** informe de Work «BTI3_Analisis_Diseno_Diagnostico_Propuesta_v0.1.pdf» (SHA-256 `3d4f5ab9…065069a`):
- §5.1, distribución por unidad;
- §5.2, secuencia de 36 encuentros con foco, capacidades e hitos;
- §6, índice.

## 1. Qué se conservó y qué se calculó

**Se conservó sin cambios** la secuencia de Work:

| Unidad | Encuentros | HC (Work) |
|---|---|---|
| I. Comprender el problema y su contexto | 1–6 | 30 |
| II. Especificar qué debe resolver el sistema | 7–12 | 30 |
| III. Diseñar una solución coherente | 13–18 | 30 |
| IV. Construir el prototipo por incrementos | 19–26 | 40 |
| V. Verificar, validar y mejorar | 27–32 | 30 |
| VI. Entregar y comunicar | 33–36 | 20 |
| **Total** | **36** | **180** |

También se conservaron:
- el foco de cada encuentro;
- las capacidades C1 a C10;
- los hitos H1 a H6.

**Se calculó** cuánto de cada encuentro corresponde a cada actividad. La asignación sigue la estructura de taller de Work (1 HC de problema y explicación, 3 HC de práctica, 1 HC de revisión), redistribuida según el foco que Work declara. Cada encuentro tiene su criterio escrito.

**Cómo verificarlo:** el cálculo está en `distribucion.py`. El script comprueba:
- que cada encuentro sume 5 HC;
- que cada unidad sume lo que indica Work;
- que los hitos estén en los encuentros de Work;
- en la adaptación, que cada encuentro de Work aparezca una sola vez y que se conserven C1 a C10 y H1 a H6.

Si algún control falla, el script no escribe resultados. Genera `distribucion_36.csv`, `distribucion_28.csv` y `tablas_generadas.md`, que trae la tabla encuentro por encuentro con el criterio de cada asignación.

**Categorías:**
- **análisis (A);**
- **diseño (D);**
- **programación (P);**
- **verificación y validación (V);**
- **documentación de entrega (Doc);**
- **gestión del proyecto (G);**
- **evaluación (E):** diagnóstico, hitos, defensa y recuperación.

El encargo pedía análisis, diseño, programación y evaluación. Las otras tres se informan por separado para no esconder tiempo dentro de las cuatro pedidas: verificación, por ejemplo, no es evaluación de los estudiantes.

## 2. Resultado

Tabla copiada de `tablas_generadas.md`:

| Categoría | HC en 36 | % en 36 | HC en 28 | % en 28 |
|---|---|---|---|---|
| Análisis | 48 | 26,7 % | 37 | 26,4 % |
| Diseño | 31 | 17,2 % | 24 | 17,1 % |
| Programación | 27 | 15,0 % | 16 | 11,4 % |
| Verificación y validación | 36 | 20,0 % | 30 | 21,4 % |
| Documentación de entrega | 7 | 3,9 % | 7 | 5,0 % |
| Gestión del proyecto | 8 | 4,4 % | 4 | 2,9 % |
| Evaluación | 23 | 12,8 % | 22 | 15,7 % |
| **Total** | **180** | **100 %** | **140** | **100 %** |

**Lectura:**
- **Análisis y diseño** suman 79 HC (43,9 %). Es la parte mayor, pero no las tres cuartas partes que estimaba la versión 1. Aquella estimación se apoyaba en una estructura que no era la de Work.
- **Programación:** 27 HC (15,0 %).
  - Son menos que las 40 HC de la Unidad IV. Work dice que la construcción «ocupará 40 HC de trabajo intensivo»; esas 40 HC son la duración de la unidad, no tiempo de escribir código.
  - **Dentro de la Unidad IV:** 23 HC de programación, 6 de revisión del requisito y del diseño de cada operación antes de programarla, 7 de pruebas inmediatas, 2 de gestión (versiones y bitácora) y 2 del hito H4.
  - **Fuera de ella:** 4 HC de corrección en la Unidad V.
- **Verificación y validación:** 36 HC (20,0 %). Es la segunda categoría. Coincide con lo que Work presenta como valor diferencial: demostrar que la solución responde al problema.
- **El alcance no cambia.** El cálculo solo describe cómo se usa el tiempo de la secuencia de Work.

**Comparación con la ponderación de Work (§4.3).** Esa ponderación no es un reparto del tiempo: es el peso en la calificación (problema y relevamiento 15 %, requisitos 20 %, modelos y diseño 20 %, prototipo 20 %, pruebas 15 %, documentación y defensa 10 %). Las dos cosas no tienen por qué coincidir y no se las forzó a coincidir. Por ejemplo, el prototipo pesa 20 % en la nota y ocupa 15 % del tiempo como programación pura. El resto de la Unidad IV se reparte en revisión de diseño, pruebas, gestión y el hito H4.

## 3. Adaptación a 28 encuentros (140 HC)

**Criterio, tomado de Work (§5.1):** ante la reducción de semanas, se recortan extensiones y se ajusta el alcance, preservando análisis, validación y entrega.

**Cómo se reduce:** se unen ocho pares de encuentros. Cada encuentro de Work queda dentro de uno de los 28, sin suprimir ninguno, y los ajustes de alcance quedan escritos en la tabla. La tabla completa está en `tablas_generadas.md`.

| Se unen (Work) | En la adaptación | Ajuste de alcance declarado |
|---|---|---|
| 05 + 06 | 5 | Factibilidad con dos alternativas en lugar de tres; H1 como defensa breve por equipo |
| 09 + 10 | 8 | Proceso actual tomado del dossier sin diagramarlo; se mantienen los tres casos de uso con un flujo alternativo |
| 11 + 12 | 9 | Plan de incrementos como lista breve; la solicitud de cambio se resuelve en la revisión H2 |
| 15 + 16 | 12 | Tres recorridos en baja fidelidad; una sola sesión de revisión entre equipos |
| 19 + 20 | 15 | El docente entrega una base con entorno, conexión e inicio de sesión (Work §7.5); el equipo hace la primera operación |
| 21 + 22 | 16 | Lectores por carga inicial; los permisos mínimos vienen en la base y el equipo los prueba |
| 25 + 26 | 19 | Consultas mínimas: disponibles, activos y vencidos con fecha de referencia |
| 31 + 32 | 24 | Sin encuentro de reserva para recuperación técnica |

**Qué se preserva, comprobado por el script:**
- las diez capacidades C1 a C10;
- los seis hitos H1 a H6;
- los dos encuentros del Capítulo 4 (requisitos);
- los cuatro de pruebas (27 a 30);
- los cuatro de entrega (33 a 36).

**Qué cambia en la proporción.** El análisis se mantiene (26,4 %), el diseño también (17,1 %) y la verificación sube (21,4 %). La programación baja de 15,0 % a 11,4 %: es la categoría que más se reduce (11 de las 40 HC que se quitan), porque la base de proyecto entregada absorbe la preparación del entorno.

**Riesgo declarado:**
- **Recuperación técnica:** la adaptación no deja encuentro de reserva para ella. Si además hay otras interrupciones, Work indica ajustar el alcance; esta adaptación no garantiza cubrirlas.
- **Base de proyecto:** reemplaza la preparación del entorno por los estudiantes. Esa evidencia de C8 queda limitada a usar y probar la base, no a armarla.

## 4. Recomendaciones para estudiantes de nivel técnico medio

1. **Código base explicado** (Work §7.5). El equipo analiza, completa y prueba; no escribe desde cero. El Piloto B v2 muestra una base posible y el tamaño real del núcleo: 567 líneas.
2. **Cada operación empieza por su requisito.** La hora de diseño de cada encuentro de construcción (20 a 25) revisa el requisito, la regla y el criterio de aceptación antes de abrir el editor.
3. **Pruebas en el mismo encuentro.** La hora de verificación de los encuentros 20 a 25 ejecuta la prueba del criterio de aceptación de la operación construida.
4. **Diagnóstico y coordinación** (Work §3). Antes del encuentro 13, Algorítmica informa qué modelado ya trabajó. Antes del 19, Laboratorio confirma lenguaje, conexión a base de datos y entorno. Si no se llegó a esos puntos, se entrega un esquema inicial y la base preparada.
5. **Ruta sin computadora** para los encuentros de construcción cuando falle el laboratorio:
   - leer el código impreso;
   - predecir el resultado;
   - escribir el caso de prueba.

   Es la misma evidencia de trazabilidad, sin el funcionamiento técnico, que se recupera después.

## 5. Pendiente de decisión

- La asignación por encuentro es editorial. Fernando, o el docente piloto, puede ajustar filas y volver a correr el script.
- La adaptación a 28 supone ocho fusiones concretas. Otra institución podría preferir otras; el script comprueba cualquier alternativa con los mismos controles.
