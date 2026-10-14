# Análisis y Diseño de Sistemas, 3.º BTI — Fase 2: pilotos

**Biblioteca Comercial 2026 · Plan Optativo · 5 HC semanales · proyecto conductor: Sistema de Gestión de Biblioteca Escolar**

**Estado: candidatos para la auditoría independiente de ChatGPT.**
- Nada de esto está aprobado para la venta ni para producción.
- La continuación depende de la aprobación expresa de Fernando.

**Lo que no se hizo, por indicación del encargo:**
- no se construyó ningún otro capítulo;
- no se reemplazó ningún archivo maestro;
- no se subió nada a Drive.

## 0. Advertencia principal: falta el documento base

«BTI3_Analisis_Diseno_Diagnostico_Propuesta_v0.1.pdf» no llegó a este entorno. No estaba entre los adjuntos de la sesión, y las búsquedas en Drive por título y por texto no lo encontraron. Por eso:

1. **El tema del Capítulo 4 es una hipótesis de trabajo.**
   - Con 6 unidades de 3 capítulos y la secuencia necesidades → requisitos → modelado → diseño → validación → documentación, el Capítulo 4 abre la Unidad 2 (Ingeniería de requisitos).
   - Se lo desarrolló como **«Elicitación de requisitos: escuchar antes de diseñar»**.
   - Si el documento base asigna otro tema al Capítulo 4, el formato del piloto se conserva y se rehace el contenido.
2. La estructura de 18 capítulos del Piloto C también es supuesta y está rotulada así.
3. **Pedido:** subir el PDF base a Drive o al chat para cotejar antes de la auditoría o junto con ella.

## 1. Entregables

| Piloto | Archivo | Bytes | SHA-256 |
|---|---|---|---|
| A | `A_piloto_capitulo4/ADS_3BTI_PILOTO_CAP4_ESTUDIANTE.docx` (16 págs.) | 187077 | `768347b90b21e88e495431e2eb3d2eff921e8deb236f04378a0a73c3107a9807` |
| A | `A_piloto_capitulo4/ADS_3BTI_PILOTO_CAP4_GUIA_DOCENTE.docx` (6 págs.) | 45160 | `469e1b18211929be1cb0231644cb96218170fcd4e9cfdf14a79b1630a4735777` |
| A | `A_piloto_capitulo4/ADS_3BTI_PILOTO_CAP4_ESTUDIANTE.pdf` (renderización de control) | 357400 | `b4215df26759edb2bc0a15ee0850cae88b9a57296606d44c014cc9cdb053f663` |
| A | `A_piloto_capitulo4/ADS_3BTI_PILOTO_CAP4_GUIA_DOCENTE.pdf` (renderización de control) | 129434 | `109e2c11f23d580da09a1b621d170dc8b1c0a482e4823a6392b63ee0ea3ff7d2` |
| B | `B_prueba_tecnica/INFORME_PRUEBA_TECNICA_PHP_SQLITE.md` | — | `b0be0069fb95f8c84e14157b7bb65f1c5433ce481178d855c18ba9fc6b68892d` |
| B | `B_prueba_tecnica/prototipo/` (6 archivos PHP, pruebas y LEEME) | — | `src/db.php` `352bdd066f44338621dc8a1ff6374a93a0616450eeb12251f143064103a1bc79` · `public/index.php` `a19bba7edd7881e3a9e68a1aa3dcf7faf59bad05afce98c579e06f9e41e244b3` |
| C | `C_informe_esfuerzo/INFORME_DISTRIBUCION_ESFUERZO.md` | — | `cb9a3b2070ea4e4273dff5d05fb6844043353bb7ec73ef4feb2eb26a75621615` |

Los DOCX se regeneran con `python3 A_piloto_capitulo4/build/build_capitulo4.py`.

## 2. Piloto A — Capítulo 4

**Libro del estudiante:**

| Parte | Contenido |
|---|---|
| Portada del piloto | Recuadro de estado: no aprobado; capacidad institucional; ubicación provisional |
| Apertura | Ficha con capacidad, tema, cuatro indicadores y tiempo; caso del libro; articulación con Algorítmica 3.º y con el prototipo |
| Encuentro 7: «A quién escuchar y cómo preguntar» | Secciones 4.1 a 4.4; ejemplos resueltos 4.1 (mapa de interesados) y 4.2 (guion de entrevista); figuras 4.1 y 4.2; tablas 4.1 a 4.4; seis actividades en cuatro bloques: Ejercitá, Resolvé, Pensá y decidí, Desafío |
| Encuentro 8: «Del registro al requisito candidato» | Secciones 4.5 a 4.8; registro E1 numerado por línea; ejemplos resueltos 4.3 a 4.5 (hallazgos, requisitos candidatos con trazabilidad, conflicto); cinco actividades |
| Práctica 4 diferenciada | Un registro de entrevista y uno de observación; tres niveles (guiado, intermedio, ampliación) sobre los mismos datos; punto de control |
| Cierre | «Para repasar»; recuadro «Si el capítulo se da en un solo encuentro» (observación 4) |
| Evaluación del capítulo | En página propia; 9 ítems, 15 puntos; claves repartidas en d, c, a, b |

**Guía docente:**
- secuencia de cada encuentro en HC, sin suponer la duración de la hora cátedra;
- claves y errores frecuentes de las 11 actividades;
- claves por nivel de la práctica y criterio para asignar niveles;
- lista de cotejo vinculada a los indicadores;
- clave de la evaluación y criterios de puntaje parcial;
- versión para calendario reducido;
- inventario de procedencia y derechos de los recursos (observación 8).

**Controles automáticos.** `build/verificar.py` da **31 correctos y 0 fallos** (`build/verificacion_resultado.txt`). Comprueba:
- voseo en las 28 consignas y que no haya formas de tú;
- que no haya símbolos prohibidos ni identificadores de modelos;
- que la capacidad no se presente como oficial del MEC;
- que las filas no se dividan;
- que los anchos de tabla sean fijos, con `tblGrid`;
- que el material del estudiante no tenga claves;
- coherencia de la opción múltiple entre el libro y la guía;
- el puntaje total;
- que la Figura 4.1 y la Tabla 4.2 usen las mismas cifras y cuadrantes;
- la tinta de las figuras;
- la trazabilidad: registro → hallazgos → requisitos;
- que no se repitan personas ni datos del caso de Algorítmica 3.º;
- las páginas y la evaluación en página propia.

**Robustez de la maqueta.** Se renderizó el libro del estudiante con tres fuentes de sustitución:

| Fuente | Páginas | Evaluación en página propia | Renglones sueltos al comienzo de una página |
|---|---|---|---|
| Carlito | 16 | Sí | Ninguno |
| Liberation Sans | 16 | Sí | Ninguno |
| DejaVu Sans | 17 | Sí | Ninguno |

**Cómo responde a las observaciones de auditoría:**

| Obs. | Tratamiento en el piloto |
|---|---|
| 1. No ser otro curso de programación | El capítulo no tiene código. Las consignas prohíben nombrar tecnologías en los requisitos. |
| 2. Núcleo y ampliaciones | En el capítulo, el Nivel 3 es ampliación y no suma puntaje. En lo técnico, autenticación, permisos y concurrencia quedan fuera del núcleo (Piloto B, §7). |
| 3. No suponer dominado lo de Algorítmica y Laboratorio | No se requiere ningún saber de programación ni de bases de datos. |
| 4. Calendario con menos encuentros | Recuadro para el estudiante y apartado 5 de la guía: actividad central, lectura domiciliaria y evaluación reducida a 10 puntos. |
| 5. No duplicar los ejercicios de biblioteca de Algorítmica 3.º | Aquel libro trabaja la biblioteca como datos: tablas, claves, integridad y la matriz de tecnología. Este capítulo trabaja con personas: entrevistas, observación y requisitos. Personas, libros y datos distintos, con control automático. |
| 6. Validar el entorno | Piloto B. |
| 7. Capacidades institucionales y oficiales del MEC | El rótulo de la ficha dice «Capacidad institucional (propuesta editorial; no es una capacidad oficial del MEC)», y la guía lo explica. |
| 8. Procedencia y derechos | Todo es original. Las figuras se generan por código y el caso es ficticio. La única referencia externa es la paráfrasis del art. 140 de la Constitución Nacional. Inventario en la guía, apartado 6. |

**Decisiones provisionales que necesitan OK:**
- **Identidad visual:** familia verde BTI del estándar gráfico (#1B5E20, #2E7D32, #43A047, #E8F5E9), sin deconflicto contra el inventario del catálogo.
- **Unidad de tiempo:** 1 encuentro = la carga semanal de 5 HC.

## 3. Piloto B — Prueba técnica PHP + SQLite

**Entorno de la prueba:** PHP 8.3.6, SQLite 3.45.1, Ubuntu 24.04.

**Resultados:**
- reglas del núcleo: 15 de 15 correctas;
- de punta a punta por HTTP: 10 de 10 correctas;
- concurrencia: un solo escritor a la vez, el comportamiento documentado de SQLite;
- falla simulada: falta `pdo_sqlite`, detectada por `verificar_entorno.php`.

**Hallazgo útil:** sin zona horaria fijada, PHP usa UTC y fecharía mal los préstamos nocturnos. Quedó corregido en el código.

**Lo que no se probó:** Windows ni el laboratorio real, y PHP anterior a 8.3. La recomendación es adoptar este entorno **de forma provisional**, con una prueba de campo en al menos dos máquinas del laboratorio antes de fijarlo para el libro.

## 4. Piloto C — Distribución del esfuerzo

Sobre la estructura supuesta:
- **análisis y diseño:** 75 % (27 encuentros);
- **programación:** 12,5 % (4,5 encuentros, concentrados en la Segunda Etapa);
- **evaluación:** 12,5 %.

**Calendario de 28 encuentros:** análisis y diseño sube al 79 %.

**Recomendaciones:**
- código dado y andamiado;
- cada cambio de código atado a un requisito;
- tres niveles de práctica;
- ruta sin computadora;
- prueba de campo en julio.

## 5. Encargo para la auditoría de ChatGPT

> Auditá los tres pilotos de la Fase 2 de Análisis y Diseño de Sistemas 3.º BTI en la carpeta `analisis_diseno_3_bti/fase2_pilotos/` del commit indicado por Claude.
>
> A. Revisá en tu propia renderización los dos DOCX del Capítulo 4:
> - registro intermedio y suficiencia de la teoría;
> - corrección conceptual de la elicitación;
> - calidad de los ejemplos resueltos;
> - progresión real entre los tres niveles de la práctica;
> - coherencia entre los indicadores, las actividades, la evaluación y la guía;
> - voseo;
> - maqueta: tablas, figuras, evaluación en página propia.
>
> B. Ejecutá o revisá el prototipo y el informe técnico. Evaluá:
> - si las limitaciones están bien declaradas;
> - si la recomendación es prudente.
>
> C. Evaluá si la distribución del esfuerzo respeta las observaciones 1 a 4.
>
> Indicá en todos los casos qué depende del documento base, que Claude no recibió: el tema del Capítulo 4 y la estructura de 18 capítulos.
