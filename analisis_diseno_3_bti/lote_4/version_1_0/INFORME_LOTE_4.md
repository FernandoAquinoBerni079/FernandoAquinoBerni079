# Lote 4 — Unidad IV (Capítulos 10 a 13), versión 1.0

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · 21 de octubre de 2026**

**Estado:** lote para auditoría independiente. No está aprobado para la venta ni para uso en aula. La aprobación para comercializar corresponde a Fernando y se hará sobre la colección completa.

**Límites respetados:**
- No se modificaron los lotes 1, 2 y 3. El verificador lo comprueba con git y con el manifiesto del lote 3 v1.1.
- No se construyeron los Capítulos 14 a 18.
- No se generaron los 36 planes de clase.
- No se subió nada a Drive.

**Próximo paso:** el lote se detiene acá para la auditoría, antes de pasar a la Unidad V.

## 1. Qué se entrega

| Documento | Páginas (oficio O3) | Plan |
|---|---|---|
| Libro del estudiante (`ADS_3BTI_LOTE4_ESTUDIANTE_OFICIO_O3`) | 44 | 40 a 50 |
| Guía docente con solucionario (`ADS_3BTI_LOTE4_GUIA_DOCENTE_OFICIO_O3`) | 23 | 18 a 24 |
| Cuaderno de prácticas (`ADS_3BTI_LOTE4_CUADERNO_PRACTICAS_OFICIO_O3`) | 9 | 8 a 12 |

Cada documento está en DOCX (el entregable) y en PDF (para control).

**Base de proyecto (`lote_4/proyecto/`), en dos distribuciones:**
- `referencia_docente/`: el sistema completo, con sus pruebas.
- `base_estudiante/`: la estructura, la conexión, el ingreso y los permisos preparados, y los componentes esenciales. No trae ninguna operación resuelta.

**Otros archivos:**
- resultados de las pruebas con su entorno (`resultados_pruebas/`);
- láminas (`revision_visual/`, 15);
- este informe y `MANIFIESTO_LOTE_4.json`.

**Plan anual preliminar:** se regeneró con los indicadores leídos de las fichas de los Capítulos 10 a 13. Los pendientes pasan a ser los Capítulos 14 a 18.

## 2. Cómo se aplicaron las siete decisiones

### Decisión 1. Pruebas de campo

- No hay acta de campo. Todo el lote lo dice:
  - la portada;
  - la apertura de la unidad;
  - un recuadro «Estado del entorno: no probado en la institución» al principio de cada capítulo;
  - la guía, en la sección 0.2.
- La guía trae la ficha de entorno completa (E-1 a E-12) para hacer la prueba de campo antes del Encuentro 19. Cubre:
  - la versión de Windows;
  - una cuenta sin permisos de administrador;
  - el funcionamiento sin internet;
  - la instalación;
  - la persistencia;
  - el respaldo y la restauración.
- La guía trae también las diferencias ya conocidas en Windows. Salen del protocolo de campo del Piloto B: `pdo_sqlite` desactivado, `php -S` que atiende de a un pedido, archivos abiertos y `posix_kill`.
- No se inventó ningún resultado escolar. Lo que no se probó figura como pendiente.

### Decisión 2. Base de proyecto

**Origen:** se adaptó el Piloto B v2.3 al diseño del lote 3 v1.1:
- Edición como entidad propia;
- Parámetro, con máximos 2 y 5;
- tipo de lector y curso obligatorio para estudiantes (RI-06);
- curso al prestar (RI-08);
- dos roles: bibliotecaria y dirección;
- ME-12 solo para el ingreso y ME-13 para la falta de permiso;
- PT-09 en la zona compartida.

**Garantías que se conservan:**
- una instalación no borra una base existente;
- `--reiniciar` pide confirmación y guarda antes un respaldo verificado;
- respaldo consistente;
- modo mantenimiento;
- retiro seguro de marcas huérfanas;
- CSRF, sesiones y contraseñas con hash.

**Nuevo:** `restaurar.php`. Antes de tocar nada:
1. valida el respaldo;
2. muestra lo que contiene;
3. pide escribir RESTAURAR;
4. guarda una copia verificada de la base actual.

Se niega si se le pasa la base misma.

**Dos distribuciones:** los archivos comunes son idénticos en las dos. Solo difieren:
- `src/reglas.php`, que en la base trae los contratos y responde PENDIENTE;
- las páginas `index.php`, `inicio.php` y `lectores.php`;
- `LEEME.txt`.

Las páginas de préstamo, devolución, activos e informe están solo en la referencia.

**Tamaño de la base del estudiante, en PHP propio:**

| Parte | Líneas | Líneas de código | Qué incluye |
|---|---|---|---|
| Arranque | 519 | **384** | conexión, sesión y permisos, operaciones pendientes con sus contratos, páginas e instalador |
| Herramientas heredadas del piloto | 580 | 467 | mantenimiento, respaldo, restauración, retiro de marcas y verificación del entorno |

- **Arranque:** está por debajo de 400 líneas de código. Las líneas de más (519 en total) son comentarios: los contratos y los pasos que el equipo completa.
- **Herramientas heredadas:** no se recortaron, porque son las garantías de instalación y restauración. Los estudiantes las usan, pero no las modifican.
- La guía explica este exceso.
- **No se cuentan:** los mensajes, los datos, el esquema y las pruebas.

### Decisión 3. Primera operación

- La primera operación es **OA-01, «dar de alta un ejemplar»**: un ejemplar físico en una edición ya cargada.
- Está documentada como operación auxiliar de PT-08, con su propio contrato y su prueba **PA-01**. No se atribuye a OP-06 ni a otro contrato.
- El Capítulo 10 la recorre completa:
  - el formulario;
  - el procesamiento en la página;
  - la validación en el servidor;
  - las consultas parametrizadas;
  - el guardado;
  - la persistencia, comprobada con otra conexión.
- **Reproducción del ejemplo:** `reproducir.py` copió el código de la referencia en una copia de la base. Los 5 casos de PA-01 dieron correctos.
- El Capítulo 11 extiende el catálogo y los lectores sin rehacer el ejemplo:
  - OA-02 registra una obra y su edición;
  - OA-03 registra un lector;
  - OA-04 corrige un lector;
  - OA-05 corrige una obra;
  - OP-06 da de baja (baja lógica).
- **OA-05 es nueva en este lote.** La evidencia de Work para el Encuentro 21 dice «alta, consulta y edición», y el catálogo no tenía edición.

### Decisión 4. Fragmentos de código

- **Libro:** 15 fragmentos breves, de 4 a 19 líneas cada uno y 135 líneas en total. Cada uno se lee del proyecto, no se copia a mano.
- **Ficha de cada fragmento:** archivo, propósito, requisito o contrato, entradas, resultado y prueba, más una explicación.
- **Lo que el libro no publica:** no publica resueltas las actividades de los equipos. Las comprobaciones del préstamo (`comprobar_prestamo`), las validaciones del lector y la consulta del informe están solo en la guía, como Referencias R-1 a R-3.
- **Lo que el libro sí da:**
  - la especificación de esas actividades (Tablas 11.2 y 12.1, contratos);
  - las protecciones que explica el texto: las dos barreras de RI-01, la devolución en una sola sentencia y las consultas.
- **Impresión:** ninguna línea pasa de 96 caracteres. El control 7 comprueba que cada línea se imprima entera, en la página de su rótulo.

### Decisión 5. Práctica 13

- Se titula «Una semana en Mbokaja: integración e incidencias (complemento editorial)».
- Usa datos nuevos: MI-01 a MI-07.
- Exige descubrir tres cosas:
  - una devolución que no se registró, que explica el «0 disponibles»;
  - un vencimiento del mismo día marcado como vencido, que es una incidencia de OP-04;
  - un informe que sí coincide.
- Va en el Encuentro 25 o como actividad complementaria. El Encuentro 26 conserva sus 2 HC de evaluación (P2 V1 E2).

### Decisión 6. Préstamo doble

- **Las dos protecciones de RI-01:**
  - `BEGIN IMMEDIATE` con la comprobación y el registro en una sola operación (Código 12.1);
  - un índice único parcial sobre los préstamos activos (Código 12.2).
- Si actúa la segunda barrera, la operación deshace todo y responde ME-03 (Código 12.4).
- **Resultado de la prueba de carrera** (Tabla 12.2): procesos independientes, en 5 rondas.
  - RI-01: 5 préstamos registrados y 55 rechazos ME-03, nunca dos préstamos activos.
  - RI-02: nunca más del máximo de cada tipo.
- **Entorno de esa prueba:** Linux 6.18.44, PHP 8.3.6 y SQLite 3.45.1, en el contenedor de construcción.
- **Windows:** queda «Pendiente — no se declara aprobado».
- **Protocolo para Windows en la guía:** dos procesos o conexiones independientes, nunca el servidor incorporado como prueba de simultaneidad, y una planilla para registrar cada ronda.

### Decisión 7. Entorno alternativo

- HTML/CSS, PHP y SQLite siguen como referencia editorial provisional.
- La guía (sección 0.3) lista las evidencias equivalentes que tiene que producir otro entorno:
  - formularios;
  - validaciones del servidor;
  - permisos;
  - transacciones;
  - restricciones en la base;
  - persistencia;
  - consultas seguras;
  - pruebas;
  - respaldo y restauración.
- No se construyó una segunda colección.

## 3. Precisiones de producción

**E-6 separada en dos:**
- **E-6a:** el recorrido completo del prototipo docente (`prueba_http.sh`, 32 de 32).
- **E-6b:** la comprobación de la base del estudiante (`prueba_base.sh`, 15 de 15). No exige las operaciones que el curso todavía construye.

**Datos y claves:**
- Los datos son solo ficticios.
- Las cuentas de demostración tienen una clave al azar que se muestra una sola vez.
- No hay contraseñas en ningún material.

**Instalación y restauración seguras:** el verificador las comprueba en vivo sobre una copia de la base:
- una segunda instalación no toca la base;
- `--reiniciar` sin confirmación no cambia nada;
- un respaldo inválido se rechaza;
- restaurar la base sobre sí misma se rechaza.

**El diseño del lote 3 v1.1 no cambia:**
- Los contratos, los roles y los mensajes son los mismos. Los textos ME-01 a ME-13 del código reproducen la Tabla 8.6.
- Ninguna operación usa ME-12.
- Cada operación protegida comprueba primero el rol con los roles de su contrato.
- Cada página exige la zona de la Figura 8.1.

**Mensajes nuevos:** los errores de entrada que los contratos de la Unidad III no preveían tienen sus propios mensajes:
- MV-01 a MV-12 para la validación;
- MA-01 a MA-09 para las operaciones auxiliares.

**Secuencia:**
- se mantienen las 40 HC y las categorías de la v2.1 en cada encuentro;
- cada capítulo tiene su recuadro con la adaptación a 28 encuentros (15 = 19 + 20, 16 = 21 + 22, 17, 18 y 19 = 25 + 26).

**H4:**
- seis criterios que cubren C7, C8 y C9, con cuatro niveles;
- 60/40 como propuesta editorial;
- la ausencia de evidencia (AE) se registra aparte;
- los pendientes del entorno se separan de las fallas del equipo;
- planilla y banco de variantes V4-1 a V4-5, que no están en el dossier, en el buzón, en el banco del H3 ni en las prácticas.

## 4. Resultados de las pruebas

**Entorno de todas las pruebas:**
- Linux 6.18.44-fc-v140, x86_64;
- PHP 8.3.6 con PDO y pdo_sqlite;
- SQLite 3.45.1;
- curl 8.5.0.

Es el contenedor de construcción del lote. **No es una computadora escolar ni Windows.** Cada archivo de `resultados_pruebas/` registra su entorno.

| Distribución | Prueba | Resultado |
|---|---|---|
| Referencia docente | contratos (OP-01 a OP-06, OA-01 a OA-05, persistencia) | 90 de 90 |
| Referencia docente | mis operaciones | 17 de 17 |
| Referencia docente | carrera (P-07, RI-02) | 15 de 15 |
| Referencia docente | garantías de la base | 20 de 20 |
| Referencia docente | respaldo | 20 de 20 |
| Referencia docente | mantenimiento | 30 de 30 |
| Referencia docente | marca huérfana | 19 de 19 |
| Referencia docente | HTTP, E-6a | 32 de 32 |
| Base del estudiante | E-6b | 15 de 15 |
| Base del estudiante | garantías de la base | 20 de 20 |
| Base del estudiante | respaldo | 20 de 20 |
| Base del estudiante | mantenimiento | 30 de 30 |
| Base del estudiante | marca huérfana | 19 de 19 |
| Base del estudiante | mis operaciones | 1 de 1; 16 pendientes, que no cuentan como falla |
| Ejemplo del Capítulo 10 | PA-01 en una copia de la base | 5 de 5 |

**Pendientes del entorno (no se declaran aprobados):**
- E-1 a E-12 en computadoras escolares;
- la prueba de concurrencia en Windows;
- las versiones de PHP anteriores a 8.3.

## 5. Controles

| Programa | Resultado |
|---|---|
| `build/verificar.py` | **274 correctos, 0 fallos** |
| `build/controles_finales.py` | **26 controles, 0 fallos** |
| `build/prueba_fuentes.py` | **9 combinaciones, 0 fallos** |
| `build/reproducir.py` | **0 fallos** |
| `build/tomo.py` | Capítulos 1 a 13 con todos sus atributos; pendientes 14 a 18 |
| `plan_anual/plan_anual_preliminar.py` | Controles correctos |

### Bloques del verificador

**Bloques de los lotes anteriores:**
- A: índice de Work textual;
- B: capacidades;
- C: trazabilidad de códigos;
- E: no duplicar Laboratorio ni Algorítmica;
- F: voseo y residuos;
- G y H: maqueta;
- I: evaluaciones, prácticas y H4;
- J: numeración;
- L: notaciones;
- Q: lotes 1 a 3 intactos.

**Bloques nuevos:**
- K: contratos implementados, con todos sus errores;
- R: autorización;
- S: las dos barreras de RI-01, el historial y las garantías de instalación y restauración, probadas en vivo;
- T: los 18 fragmentos (15 del libro y 3 de la guía), tal cual el archivo, con su ficha y sin publicar las actividades;
- U: distribuciones idénticas, la base sin operaciones resueltas y su tamaño;
- V: pruebas con su entorno, ningún entorno declarado validado.

### Controles de impresión

- Las cuatro figuras, cada una con su imagen sobre su epígrafe.
- Todas las filas de todas las tablas, en los tres PDF.
- Ninguna tabla deja una sola fila al pasar de página.
- El índice es estable.
- Los márgenes son espejados.
- **Control nuevo, 7:** cada línea de código se imprime entera y dentro de los márgenes, y cada bloque queda en la página de su rótulo.

## 6. Láminas (`revision_visual/`)

| N.º | Lámina |
|---|---|
| 01 | Índice y apertura |
| 02 | Entorno, estructura y datos |
| 03 | Primera operación y código |
| 04 | Catálogo, permisos y baja lógica |
| 05 | Préstamo y dos protecciones de RI-01 |
| 06 | Devolución y fallos previsibles |
| 07 | Consultas y fecha de referencia |
| 08 | Prácticas |
| 09 | Evaluaciones |
| 10 | Integración y H4 |
| 11 | Guía: rúbrica del H4 y banco de variantes |
| 12 | Guía: ficha de entorno y base |
| 13 | Márgenes espejados |
| 14 | Tablas repartidas |
| 15 | Cuaderno de prácticas |

## 7. Decisiones propias para revisar en la auditoría

1. **OA-05, «corregir una obra»:** se agregó para cumplir la evidencia de Work del Encuentro 21 («alta, consulta y edición»).
2. **El informe mensual (OP-05)** se construye en el Encuentro 25 y se explica en la sección 13.2, como consulta con un período definido. El plan lo ubicaba en la 13.3. La sección 13.3 queda para la integración y la revisión contra Work §7.2.
3. **La Práctica 11** supone que el sistema de prueba de Mbokaja ya acepta las etiquetas MB- (la decisión del nivel 3 de la Práctica 10).
4. **Las referencias R-1 a R-3** (código resuelto de actividades de los equipos) están solo en la guía docente, que no se entrega a los estudiantes.
