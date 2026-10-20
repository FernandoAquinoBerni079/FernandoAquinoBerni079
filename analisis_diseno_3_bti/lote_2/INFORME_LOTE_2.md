# Lote editorial 2 — Unidad II (Capítulos 4, 5 y 6) en oficio O3

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · 20 de octubre de 2026**

**Estado:** lote para auditoría independiente. **No está aprobado para comercialización.** La aprobación comercial definitiva la hace Fernando, sobre el conjunto completo.

**Autorización (Fernando, 20 de octubre de 2026):**
- iniciar el lote 2, según `lote_2_plan/PLAN_LOTE_2_UNIDAD_II.md` y `lote_2_plan/NOTACIONES_CAPITULO_5.md`;
- formato oficio O3, con márgenes espejados y todas las tablas comprobadas contra el PDF;
- lote independiente, pero construido sobre una fuente editable que sirva para el tomo anual.

**Lo que no se hizo:**
- No se tocaron el lote 1 ni sus versiones: `lote_1/` (31 archivos, mismo SHA-256), `lote_1_oficio/` y `lote_1_oficio_candidata/`.
- No se modificaron los pilotos del Capítulo 4, los planes del lote 2 ni el plan anual preliminar.
- No se produjeron los 36 planes de clase.
- No se empezaron los Capítulos 7 a 18.
- No se subió nada a Drive.

## 1. Entregables

| Archivo | Páginas |
|---|---:|
| `ADS_3BTI_LOTE2_ESTUDIANTE_OFICIO_O3.docx` y `.pdf` — libro del estudiante | 39 |
| `ADS_3BTI_LOTE2_GUIA_DOCENTE_OFICIO_O3.docx` y `.pdf` — guía docente con solucionario | 16 |
| `ADS_3BTI_LOTE2_CUADERNO_PRACTICAS_OFICIO_O3.docx` y `.pdf` — cuaderno de prácticas | 7 |

**El libro incluye:**
- la apertura de la Unidad II;
- los Capítulos 4 a 6, cada uno con:
  - ficha;
  - las secciones de Work §6, textuales;
  - ejemplos resueltos, figuras y actividades en cuatro bloques;
  - práctica en tres niveles;
  - «Para repasar» y «Si el calendario se acorta»;
  - evaluación opcional de 15 puntos en página propia;
- la revisión de la Unidad II con el hito H2.

**La guía incluye:**
- la secuencia de cada encuentro en HC;
- las claves de todas las actividades, prácticas y evaluaciones;
- las listas de cotejo;
- la leyenda de notaciones con los errores frecuentes;
- la rúbrica del H2, con su planilla y un banco de necesidades nuevas;
- el calendario de 28 encuentros;
- la procedencia de los recursos.

**El cuaderno** reúne las Prácticas 4, 5 y 6, extraídas de la misma fuente que el libro.

**Reconstrucción:**

```
python3 lote_2/build/construir.py          # libro, guía y cuaderno (DOCX y PDF)
python3 lote_2/build/verificar.py          # bloques A a M
python3 lote_2/build/controles_finales.py  # impresión y láminas de revisión visual
python3 lote_2/build/prueba_fuentes.py     # tres fuentes de sustitución
python3 lote_2/build/tomo.py               # índice de la fuente del tomo anual
```

## 2. Fuente editable común (para el tomo anual)

| Pieza | Dónde | Cómo se comparte |
|---|---|---|
| Maqueta | `lote_1/build/helpers.py` y `maqueta.py` | Se importan sin cambios. Siguen idénticos a los del Capítulo 4 v2.1 (control G). |
| Perfil O3 | `lote_2/build/oficio.py` | Es la capa de la candidata O3 aprobada, reunida en un módulo: página y márgenes espejados, anchos ajustados por palabra, índice, sin hojas en blanco y tablas en hoja nueva. Se aplica al importarse. |
| Control de filas | `lote_1_oficio_candidata/build/controles_impresion.py` | Se importa sin cambios. Entra en el ciclo de construcción y en los controles finales. |
| Caso Arapoty | `lote_1/caso/dossier.py` (sin cambios), más `lote_2/caso/requisitos.py` y `modelos.py` | Fuente única. Contiene: catálogo, buzón, criterios, pruebas previstas, trazabilidad, D3, SC-01 y catálogo v1.1; procesos, contexto y casos de uso. |
| Caso Mbokaja | `lote_1/caso/mbokaja.py` (sin cambios), más `lote_2/caso/mbokaja_u2.py` | Datos nuevos de las Prácticas 5 y 6 |
| Contenido | `lote_2/build/cap4.py` a `cap6.py` | Mismos atributos que `cap1.py` a `cap3.py` (lo comprueba `tomo.py`) |
| Armado | `lote_2/build/construir.py` | Funciones `capitulo4` a `capitulo6`, como `capitulo1` a `capitulo3` del lote 1. `tomo.py` registra de dónde sale cada capítulo. |
| Figuras | `lote_2/build/diagramas.py` | Se dibujan desde los datos del caso. Hay una función por símbolo y por notación. |

## 3. Capítulo 4: integración del piloto con la especificación C3

`cap4.py` **carga el Capítulo 4 v2.1 del piloto y conserva todos sus textos**, salvo los 15 cambios declarados en `CAMBIOS`. El control D comprueba que las otras 39 piezas son idénticas al piloto.

| Cambio | Motivo |
|---|---|
| Rótulo, capacidades (C3 y C9) y un indicador de C9 | Formato del lote 1. Work §5.2 asigna C9 al Encuentro 8, por la revisión entre pares que el capítulo ya tenía. |
| Título de 4.2: «Requisitos funcionales, calidad y restricciones» | Es el texto de Work §6. **El piloto decía «de calidad»**, y su control no lo detectó. Los párrafos de la sección no cambian. |
| Extracto del dossier, reglas, catálogo, postergados y buzón | Se leen de la fuente única. El extracto muestra ahora cada línea completa. El catálogo y el buzón son idénticos al piloto (control D). |
| Consigna común RNF-04 (B-03), antes de los niveles | Especificación C3, §2 |
| Nivel 2 desde RNF-05 y solo con B-08; Actividad 1 (d) del Encuentro 8 como tarea | Especificación C3, §2 |
| Guía: clave de la consigna común, fila de cotejo (indicador 3), fila RNF-04 en la correspondencia y nota de evidencia mínima | Especificación C3, §3 |
| Recuadro del calendario y articulación | Se quitan el nombre interno «Piloto C» y la remisión a «la página siguiente» |

**Lo que se conserva sin cambios:**
- la semilla `ADS3-C4v2-2` y los ítems de la evaluación;
- las claves de los Encuentros 7 y 8;
- la correspondencia de los 15 requisitos.

**El control K** comprueba:
- las cuatro comprobaciones del §4 de la especificación;
- los ajustes de numeración;
- que la consigna común está antes de los tres niveles.

## 4. Capítulos 5 y 6

**Capítulo 5. Procesos, contexto y casos de uso (encuentros 9 y 10)**
- **Notaciones:** las aprobadas, una por modelo.
  - 5.1: diagrama de actividades UML con carriles.
  - 5.2: diagrama de contexto.
  - 5.3 y 5.4: diagrama de casos de uso UML, con plantilla de texto.
- **Figuras:** cuatro.
  - 5.1: proceso actual de préstamo y devolución, en siete acciones, con los problemas del dossier marcados (1) a (3) y explicados en la Tabla 5.2.
  - 5.2: proceso propuesto, con el carril «Sistema». Cada acción del sistema cita su requisito.
  - 5.3: contexto, con tres entidades externas y nueve flujos con su fuente en el dossier.
  - 5.4: casos de uso, con cinco casos.
- **Leyenda:** cada notación tiene su tabla de símbolos en el libro (Tablas 5.1, 5.4 y 5.6), dibujados con las mismas funciones que las figuras.
- **Casos de uso prioritarios:** CU-01 a CU-03, con plantilla completa y flujos alternativos.
  - Entre los tres cubren RF-01 a RF-08.
  - Los de préstamo cubren RF-04, RF-05 y RF-06.
- **Práctica 5:** caso Mbokaja.
  - Datos nuevos: una computadora donada (M-F7), el relato del proceso actual (MP-1 a MP-6) y los requisitos MR-01 a MR-08.
  - Dos situaciones que no aparecen en ningún ejemplo: un libro devuelto dañado (MS-1) y una estudiante del turno mañana (MS-2).
- **No duplica Algorítmica 3.º:** no hay tablas, diagramas de datos ni personas o títulos de ese libro (control E).

**Capítulo 6. Priorizar y mantener la coherencia (encuentros 11 y 12)**
- **6.1:** la prioridad se decide con cuatro preguntas (circuito, reglas, valor y dependencias), sin puntajes. La Tabla 6.1 trata los pedidos fuera del núcleo.
- **6.2:** la Figura 6.1 extiende la cadena de Work §7.3 (N-02, RN-01, RF-04, P-07) con el flujo alternativo 5a de CU-01. La Tabla 6.2 es la matriz de los 15 requisitos, con las pruebas previstas P-01 a P-15. La matriz deja a la vista las omisiones reales: criterios que escribe el equipo y casos de uso sin desarrollar.
- **6.3:** incrementos de la Unidad IV y tareas con responsable, estimación en HC, dependencia y estado. Sin PERT ni grafos (control E).
- **6.4:** la nota D3 de la dirección da lugar a la solicitud SC-01:
  - RN-02 cambia;
  - RF-05 no cambia de texto, porque dice «máximo vigente»;
  - aparece RF-11 (tipo de lector);
  - P-06 se desdobla.
  
  El resultado es el catálogo v1.1, y la v1.0 se conserva.
- **Revisión de la Unidad II, H2:**
  - lista de verificación;
  - cinco criterios en cuatro niveles, con 60 % de evidencia del equipo y 40 % individual, como propuesta editorial;
  - la ausencia de evidencia se registra aparte.
  
  La guía trae la rúbrica, la planilla y un banco de cuatro necesidades nuevas que no están en el dossier, en el buzón ni en D3.
- **Práctica 6:** Mbokaja, con una solicitud de la directora (MC-1) distinta de SC-01. Pide trazar, priorizar, planificar y tramitar el cambio.

## 5. Controles

| Control | Resultado |
|---|---|
| `verificar.py`, bloques A a M | **198 correctos, 0 fallos** (`verificacion_resultado.txt` y `.json`) |
| `controles_finales.py`: impresión | **25 controles, 0 fallos** (`CONTROLES_FINALES.txt` y `.json`) |
| `prueba_fuentes.py`: Carlito, Liberation Sans y DejaVu Sans | **9 combinaciones, 0 fallos**. Sin páginas en blanco ni renglones sueltos, y evaluaciones en página propia. |
| `tomo.py` | Los seis capítulos construidos tienen los atributos del armado |

**Bloques del verificador:**

| Bloque | Qué controla | Correctos |
|---|---|---:|
| A | Índice de Work: títulos, encuentros, secciones textuales, prácticas y H2 | 14 |
| B | Capacidades de Work §5.2, rotuladas como propuestas y no oficiales | 11 |
| C | Fuentes citadas que existen, citas textuales, catálogo, buzón, D3, Mbokaja y `verificar_caso` del lote 1 | 14 |
| D | El Capítulo 4 coincide con el piloto salvo los cambios declarados, y el piloto no se modificó | 12 |
| K | Especificación de evidencia C3 | 7 |
| L | Notaciones: sin mezcla, reglas de forma, responsabilidad, coherencia con el catálogo y entre diagramas, excepciones, leyenda, y una prueba del propio control | 27 |
| M | Trazabilidad entre capítulos, pruebas previstas, SC-01, incrementos y tareas | 15 |
| E | Sin duplicar Algorítmica 3.º (personas, títulos, matriz ponderada, datos) ni Matemática Aplicada (PERT, grafos) | 4 |
| F | Voseo, sin identificadores de modelos ni residuos, y sin declarar aptitud ni aprobación | 15 |
| G | Oficio O3 con márgenes espejados, filas «no dividir», tablas a 17,29 cm y encabezados repetidos | 14 |
| H | Sin páginas en blanco, evaluaciones y prácticas en página propia, índice estable y extensión | 20 |
| I | Evaluaciones de 15 puntos con claves repartidas, semillas nuevas, prácticas en tres niveles, rúbrica del H2, secuencia en HC, claves completas y cuaderno idéntico al libro | 26 |
| J | Numeración de tablas, figuras y ejemplos, y referencias que existen | 19 |

**Impresión (control de filas de la candidata O3):**
- **Libro:** 32 tablas y 200 filas, todas impresas. Cuatro tablas pasan a la página siguiente (4.3, 4.5, 5.2 y 6.2); todas están completas y repiten el encabezado.
- **Guía:** 41 tablas y 251 filas, todas impresas. Ocho tablas repartidas, todas completas y con el encabezado repetido.
- **Cuaderno:** 8 tablas y 45 filas, todas impresas.
- **Párrafos y palabras:** ningún párrafo sin imprimir y ninguna palabra partida, en los tres documentos.
- **Ajustes de maquetación:** ninguna tabla necesitó hoja nueva y ninguna columna se ensanchó.
- **Figuras:** las 8 figuras tienen su imagen encima del epígrafe. Hay 21 imágenes dibujadas: 8 figuras y 13 símbolos.
- **Índice:** 29 entradas, cada una en su página.
- **Márgenes espejados:** el interior de 2,5 cm queda en el lado del lomo, medido en las págs. 4 a 11.

## 6. Revisión visual

Láminas en `revision_visual/`, revisadas una por una:

| Lámina | Qué se confirmó |
|---|---|
| `01_indice_y_apertura.png` | Índice de una página y apertura de la Unidad II |
| `02_diagramas_capitulo_5.png` | Las cuatro figuras del Capítulo 5, legibles, cada una con su notación y su epígrafe |
| `03_leyendas_de_notacion.png` | Las tres tablas de símbolos, con el símbolo dibujado |
| `04_plantillas_de_casos_de_uso.png` | CU-01 a CU-03 con escenario principal y flujos alternativos numerados |
| `05_trazabilidad_y_solicitud_de_cambio.png` | Matriz, Figura 6.1, registro D3, SC-01, Figura 6.2 y Tabla 6.6 |
| `06_practicas.png` y `12_cuaderno_de_practicas.png` | Cada práctica empieza en hoja nueva; el cuaderno repite el texto del libro |
| `07_evaluaciones.png` | Las tres evaluaciones, cada una entera en una página (15, 28 y 39) |
| `08_revision_unidad_II_H2.png` y `09_guia_rubrica_H2_y_banco.png` | Revisión de la unidad, rúbrica, planilla y banco de necesidades |
| `10_margenes_espejados_pags_6_7.png` | Páginas enfrentadas, con el margen ancho del lado del lomo |
| `11_tablas_repartidas.png` | Las tablas repartidas, completas y con el encabezado repetido |

## 7. Decisiones editoriales tomadas en el lote (para revisar en la auditoría)

1. **C9 en el Capítulo 4,** por Work §5.2. Agrega un indicador de C9 sobre la revisión entre pares, que el piloto ya tenía.
2. **Evaluaciones más breves en los Capítulos 5 y 6,** para que cada una entre en una página. Se acortaron los enunciados, sin cambiar los ítems ni los puntajes.
3. **Identificadores de los ejercicios.** En las actividades, RF-11, RN-07 y similares son el «próximo libre» de cada ejercicio, no del caso. En el caso, RF-11 es el de SC-01. La guía lo aclara donde puede confundir (Encuentro 10, Actividad 4).
4. **El encargado de informática no es entidad externa del contexto,** porque no intercambia información de préstamos (Ejemplo resuelto 5.3).

## 8. Limitaciones y pendientes

- **Tipografía.** El PDF de control se renderiza con Carlito, como en el lote 1; en Word la paginación puede variar levemente. La prueba con tres fuentes no encontró problemas de maqueta.
- **Plan anual.** Sigue preliminar. `plan_anual_preliminar.py` todavía lee los indicadores del Capítulo 4 del piloto; para que lea las fichas de los Capítulos 4 a 6 del lote 2 hay que actualizarlo, y eso queda para cuando se autorice.
- **Tomo anual unificado.** La fuente está lista y registrada en `tomo.py`, pero el constructor del tomo no se escribió: depende de los capítulos 7 a 18.
- **Capacidades.** Las de Work se rotulan como propuestas para el programa institucional; la lectura del diseño curricular que cita Work no se verificó por separado.
