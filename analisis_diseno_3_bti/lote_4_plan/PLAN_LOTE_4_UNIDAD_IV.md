# Plan detallado del lote editorial 4 — Unidad IV (Capítulos 10, 11, 12 y 13)

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · 21 de octubre de 2026**

**Estado:** plan para auditar. **No se construye ningún capítulo hasta que Fernando lo autorice**, después de auditar el cierre del lote 3 y este plan.
- No se escribió ningún capítulo de la Unidad IV.
- No se modificaron los lotes 1, 2 y 3 para preparar este plan.
- No se subió material a Drive.

**Base:**
- informe de Work v0.1 (`BTI3_Analisis_Diseno_Diagnostico_Propuesta_v0.1.pdf`, 22 págs., SHA-256 `3d4f5ab9…065069a`): §2.3, §3, §4.2, §4.3, §5.1, §5.2, §6, §7.2, §7.3, §7.4, §7.5 y §8.2;
- distribución de 180 HC v2.1 (`fase2_pilotos/C_informe_esfuerzo/v2_1/distribucion_36.csv` y `distribucion_28.csv`);
- catálogo v1.1 y diseño de la Unidad III, con los contratos corregidos en el cierre del lote 3 (`lote_3/caso/diseno.py`);
- pruebas previstas P-01 a P-15 (`lote_2/caso/requisitos.py`);
- prueba técnica del Piloto B (`fase2_pilotos/B_prueba_tecnica/`, versión 2.3) y su protocolo de campo pendiente (`PRUEBAS_PENDIENTES_CAMPO.md`).

**Sobre el entorno técnico:** HTML/CSS + PHP + SQLite sigue siendo una **referencia provisional**. Las pruebas automáticas del Piloto B corrieron solo en Ubuntu 24.04 con PHP 8.3.6 y SQLite 3.45.1. **No se probó en Windows ni en computadoras escolares.** El plan no lo presenta como entorno validado para todos los colegios.

## 1. La Unidad IV en Work

**Unidad IV — Construir el prototipo por incrementos.** Encuentros 19 a 26, **40 HC**.

**Resultado de la unidad (Work §5.1):** «Circuito funcional integrado y persistente».

**Índice de Work §6, textual:**

| Capítulo | Encuentros | Secciones | Cierre |
|---|---|---|---|
| 10. Del diseño a la primera operación funcional | 19 y 20 | 10.1. Preparación del entorno y estructura del proyecto. · 10.2. Versiones, bitácora y conjunto inicial de datos ficticios. · 10.3. Una operación completa: formulario, procesamiento y almacenamiento. · 10.4. Validación, consulta parametrizada y evidencia de persistencia. | Práctica: demostrar una operación y vincularla con su requisito y prueba. |
| 11. Catálogo, ejemplares y lectores | 21 y 22 | 11.1. Implementación de tareas priorizadas a partir de los bocetos. · 11.2. Datos obligatorios, códigos, duplicados y mensajes útiles. · 11.3. Permisos mínimos y comprobaciones del servidor. · 11.4. Edición y baja lógica sin pérdida de historial. | Práctica: registrar un lote distinto del ejemplo y resolver entradas inválidas. |
| 12. Préstamos y devoluciones consistentes | 23 y 24 | 12.1. Precondiciones y reglas de la operación de préstamo. · 12.2. Doble envío, disponibilidad y operaciones atómicas. · 12.3. Devolución, estado del ejemplar y conservación de historial. · 12.4. Fallos previsibles y comprobación de resultados. | Práctica: resolver dos solicitudes incompatibles y explicar la protección elegida. |
| 13. Información útil e integración | 25 y 26 | 13.1. Búsqueda de ejemplares disponibles y préstamos activos. · 13.2. Vencimientos y fecha de referencia. · 13.3. Integración de módulos y revisión del alcance mínimo. · 13.4. Demostración del incremento y registro de pendientes. | Revisión de unidad IV: circuito funcional completo; H4. |

**Lo que dice Work §7.5 (textual, extracto):**
- «Para el piloto se propone HTML/CSS + PHP + SQLite mediante PDO, con ejecución local y sin servicios de pago obligatorios. La elección es editorial».
- «La institución puede usar el entorno que ya domine si produce evidencias equivalentes».
- «Se recomienda entregar una base de proyecto breve y explicada que resuelva configuración y conexión, dejando al estudiante el análisis, reglas, operaciones y pruebas».
- «El servidor debe validar entradas, aplicar permisos y proteger las consultas; una validación visual en el navegador es insuficiente».
- Factibilidad: «un equipo utilizable por pareja, trabajo en equipos de tres o cuatro con turnos efectivos, materiales disponibles sin conexión durante el taller y coordinación docente. Estos recursos no fueron constatados en una institución concreta».
- «Si el diagnóstico muestra que no se dominan formularios y programación elemental, se requerirá apoyo de Laboratorio y simplificación del alcance; no se promete resolver esa brecha con una ficha breve».

**Acuerdo operativo (Work §3):** «antes del 19, Laboratorio confirma lenguaje, conexión a BD y entorno. Si la secuencia concurrente todavía no alcanzó esos puntos, se entrega […] una conexión preparada para revisar y completar».

**Condiciones mínimas de aceptación del prototipo (Work §4.3):** «circuito de préstamo/devolución ejecutable; persistencia comprobada; ninguna pérdida de historial en las operaciones acordadas; rechazo de préstamo simultáneo del mismo ejemplar; evidencia de pruebas; instalación y restauración reproducibles». Work aclara que son criterios del proyecto y no reglas automáticas de promoción.

## 2. Capacidades y secuencia en HC

**Capacidades** (Work §4.2; rotuladas siempre como **propuestas para el programa institucional, no oficiales del MEC**):

| Capacidad | En la Unidad IV |
|---|---|
| **C8.** Integra un prototipo funcional con persistencia. | Núcleo de los ocho encuentros. Indicadores de Work: «Ejecuta catálogo, lectores, préstamo y devolución; conserva datos al reiniciar; rechaza operaciones inválidas; relaciona módulos con requisitos». Criterio: «Funciona el circuito completo y las reglas se hacen cumplir más allá de la apariencia de las pantallas». |
| **C5.** Justifica el modelo de información y sus reglas de integridad. | Encuentros 21, 23 y 24: el modelo del Capítulo 7 se implementa y se comprueba. |
| **C6.** Diseña la interacción y la arquitectura del prototipo. | Encuentros 20 y 22: bocetos, mensajes y capas del Capítulo 9 llevados al código. |
| **C9.** Verifica y mejora la solución a partir de evidencia. | Encuentros 20, 23, 24 y 26: pruebas de cada incremento. La matriz de pruebas completa es de la Unidad V. |
| **C7.** Organiza y registra el trabajo colaborativo. | Encuentros 19 y 26: versiones, bitácora e incidencias. |
| **C3.** Especifica y prioriza requisitos verificables. | Encuentro 25: consultas ligadas a RF-07, RF-08 y RF-09. |

**Secuencia (Work §5.2 y distribución v2.1, encuentros 19 a 26):**

| Enc. | Foco (Work §5.2) | Evidencia (Work §5.2) | Capacidades | HC (v2.1) |
|---:|---|---|---|---|
| 19 | Preparar entorno, estructura de trabajo, versiones y datos ficticios. | Ejecución inicial reproducible; ficha de entorno. | C7, C8 | P 3, G 2 |
| 20 | Construir una operación mínima de extremo a extremo. | Formulario-servidor-BD; prueba de persistencia. | C6, C8, C9 | D 1, P 3, V 1 |
| 21 | Implementar catálogo y control de ejemplares. | Alta, consulta y edición con reglas de validación. | C5, C8 | D 1, P 3, V 1 |
| 22 | Implementar lectores y permisos mínimos. | Validación en servidor; rechazo de acceso indebido. | C6, C8 | D 1, P 3, V 1 |
| 23 | Implementar préstamo y prevención de duplicados. | Operación coherente ante reenvío o segunda solicitud. | C5, C8, C9 | D 1, P 3, V 1 |
| 24 | Implementar devolución e historial. | Devolución única, conservación de referencias y pruebas. | C5, C8, C9 | D 1, P 3, V 1 |
| 25 | Construir consultas de disponibilidad y vencimientos. | Reporte correcto con fecha de referencia definida. | C3, C8 | D 1, P 3, V 1 |
| 26 | Integrar y demostrar el incremento; revisar unidad IV. | H4: prototipo completo mínimo y lista de incidencias. | C7-C9 | P 2, V 1, E 2 |

Total: 40 HC (P 23, D 6, V 7, G 2, E 2).

**Estructura de cada encuentro:** el taller de Work (§5.1), con 1 HC de problema y explicación, 3 de práctica y 1 de revisión. En los encuentros 20 a 25, la hora de diseño repasa el requisito, el boceto y el contrato de la operación. La hora de verificación prueba lo construido con su prueba prevista (columna «criterio» de v2.1).

**Adaptación a 28 encuentros (`distribucion_28.csv`):**

| 28 | Reúne | Foco | Ajuste de alcance (v2.1, textual) |
|---:|---|---|---|
| 15 | 19+20 | Base de proyecto y primera operación. | «El docente entrega el entorno, la conexión y el inicio de sesión listos (base explicada, Work §7.5); el equipo hace la primera operación.» |
| 16 | 21+22 | Catálogo, ejemplares, lectores y permisos. | «Lectores por carga inicial; los permisos mínimos vienen en la base y el equipo los prueba.» |
| 17 | 23 | Préstamo y prevención de duplicados. | Sin cambios. |
| 18 | 24 | Devolución e historial. | Sin cambios. |
| 19 | 25+26 | Consultas mínimas, integración; H4. | «Solo disponibles, activos y vencidos con fecha de referencia.» |

Cada capítulo lleva su recuadro «Si el calendario se acorta» con estos ajustes.

## 3. Qué no repetir y con quién coordinar

Work §2.3 y §8.2 fijan qué ya enseñan otras materias del Diseño Curricular:

| Fuente (según Work §8.2) | Lo que ya trabaja | Uso en este lote (A/P) | Lo que no se hace (D) |
|---|---|---|---|
| Laboratorio 1.º, pp. 39-40 | HTML, CSS, formularios | Ficha breve de recuperación, sin unidad de iniciación web | — |
| Laboratorio 2.º, pp. 47-49 | Variables, funciones, GET/POST, controles, arreglos y archivos | «implementar una regla del dominio y validar entradas» | «un curso inicial de programación o de sintaxis PHP» |
| Laboratorio 2.º, pp. 50-52 | Redes, servidores, servidor web y seguridad | «operar el entorno preparado y describir sus dependencias» | «volver a desarrollar OSI/TCP/IP, DHCP, VPN o instalación completa de redes» |
| Algorítmica 2.º, pp. 74-76 | Modularización, parámetros, cadenas, archivos, filtros y consultas | «separar reglas, presentación y acceso a datos; diseñar validaciones» | «repetir ejercicios de vectores, ordenación o consultas de iniciación» |
| Laboratorio 3.º, pp. 54-55 | Conexión a BD, CRUD, SQL, restricciones | «integrar operaciones con requisitos y probar consistencia de extremo a extremo» | «duplicar un manual de SQL o las prácticas básicas de CRUD» |

**Algorítmica 3.º de la colección** (`algoritmica_3_esencial/`):
- trabaja la base en Access (Clase 18) y las consultas (Clases 19 a 21);
- este lote no usa Access ni repite esos ejercicios.

**Libros de Laboratorio:** no hay ninguno de la colección en el repositorio (Work §8.4 tampoco encontró «una colección de Laboratorio 1.º-3.º»). Por eso no se citan páginas propias; solo las del Diseño Curricular que cita Work.

**Tratamiento:**
- el código se presenta **como base explicada** (Work §7.5): el estudiante lee, completa y prueba, pero no escribe la configuración ni la conexión;
- cada fragmento de código del libro lleva el requisito, la regla o el contrato que cumple;
- la evaluación del optativo valora la justificación y la trazabilidad necesidad-requisito-modelo-prueba, no la sintaxis (Work §3: «Laboratorio, el funcionamiento técnico; el optativo, la justificación y la trazabilidad»).

## 4. Comprobación previa del entorno

Es una sección de la guía docente (lista de verificación) y una ficha de una página en el libro. **Se hace antes del Encuentro 19**, en las computadoras donde se va a trabajar, con el docente de Laboratorio (acuerdo de Work §3).

**Estado:**
- las pruebas reales en computadoras escolares **siguen pendientes**;
- las hacen el docente o el responsable técnico de cada institución, con el protocolo de `PRUEBAS_PENDIENTES_CAMPO.md`;
- antes de construir el Capítulo 10 hace falta al menos un acta de campo, registrada en el repositorio; si no la hay, el capítulo dice expresamente que el entorno no se probó en la institución;
- ningún resultado de esa prueba convierte al entorno en validado para todos los colegios: vale para los equipos probados.

**Lista para el docente (ficha de entorno, evidencia del Encuentro 19):**

| N.º | Qué se comprueba | Cómo | Qué se anota |
|---|---|---|---|
| E-1 | Sistema operativo | En cada equipo: edición y versión de Windows (u otro) y si es de 32 o 64 bits. **Se relevan, no se suponen.** | Versión exacta por equipo |
| E-2 | Funcionamiento sin internet | Desconectar la red y hacer el recorrido mínimo (paso E-6) | Si todo funcionó desconectado (P-13) |
| E-3 | Sin costos obligatorios | Revisar la licencia de cada componente: intérprete, base de datos, navegador y editor | Componente, versión, licencia y origen del instalador (P-15) |
| E-4 | Instalación reproducible | Un paquete fijo (carpeta con versiones anotadas, disponible sin conexión: pendrive o copia local) y pasos numerados; instalar en un segundo equipo siguiendo solo la ficha | Si el segundo equipo quedó igual sin ayuda; tiempo empleado |
| E-5 | Prueba mínima | Ejecutar el verificador del entorno de la base de proyecto y la prueba de reglas incluida | Línea de resultado de cada prueba |
| E-6 | Recorrido mínimo | Abrir el navegador local, consultar sin sesión, ingresar, prestar, intentar prestar el mismo ejemplar, devolver y salir | Si cada paso dio el resultado esperado |
| E-7 | Permisos del usuario de estudiante | Repetir E-5 y E-6 con la cuenta que usan los estudiantes, **sin permisos de administrador** | Si funcionó; qué carpeta necesitó escritura |
| E-8 | Si hace falta administrador | Lo resuelve una sola vez el responsable técnico, antes del Encuentro 19 | Qué se hizo, quién, cuándo |
| E-9 | Antivirus y políticas | Comprobar que no bloquean el intérprete ni el puerto local | Mensaje exacto si hubo bloqueo |
| E-10 | Ubicación de los datos | El archivo de datos en un disco local: no en carpeta de red ni pendrive abierto mientras funciona (riesgo señalado en el protocolo de campo) | Ruta usada |
| E-11 | Respaldo | Con el servidor detenido, hacer un respaldo y comprobar que el archivo existe | Ruta y tamaño |
| E-12 | Restauración probada | Cargar un préstamo, restaurar el respaldo anterior y comprobar que el estado es el del respaldo | Resultado (base de P-xx de la Unidad VI) |

**Si en Windows aparecen diferencias ya conocidas del Piloto B** (por ejemplo, la extensión `pdo_sqlite` desactivada en el archivo de configuración de ejemplo, o que el servidor incorporado atiende los pedidos de a uno), se documentan en la ficha, y no se modifica el contenido del libro para ocultarlas.

**Plan alternativo si el entorno de referencia no funciona:**
1. Usar el entorno que la institución ya domine en Laboratorio, si produce evidencias equivalentes: las mismas reglas, pruebas y entregables (Work §7.5). El libro da los contratos, las reglas y las pruebas independientes del lenguaje; la base de proyecto y los fragmentos de código quedan como ejemplo.
2. Si no hay ninguno que funcione en los equipos: trabajar con una sola computadora preparada por el docente para las demostraciones y las pruebas, y reducir el alcance según la adaptación de 28 encuentros. Se registra como limitación.
3. Ningún camino se declara validado. La guía pide registrar en la ficha de entorno el camino elegido y su resultado.

## 5. Contratos, restricciones y pruebas por capítulo

La Unidad IV implementa **el catálogo v1.1 y el diseño del lote 3 sin cambios de contenido**. Se aplican los contratos corregidos en el cierre del lote 3:
- PT-09 «Informe mensual por curso» está en la zona compartida **«Bibliotecaria o dirección»**, y OP-05 la pueden usar los dos roles. El servidor comprueba el rol en cada pedido.
- **ME-12 es solo autenticación:** usuario o contraseña incorrectos en PT-03.
- **ME-13 es autorización:** «acceso denegado» cuando la cuenta no tiene permiso. Es el error de permiso de OP-01, OP-02, OP-04, OP-05 y OP-06.
- **OP-03 es pública:** no pide sesión y nunca devuelve datos de lectores.

| Capítulo | Operaciones (contratos del Capítulo 9) | Restricciones (Capítulo 7) | Pantallas y mensajes (Capítulo 8) | Pruebas previstas que se preparan y ejecutan en el incremento |
|---|---|---|---|---|
| 10 | Base explicada: conexión, estructura y sesión. Una operación completa de ejemplo: OP-03 consultar disponibilidad (pública, solo lectura) o el alta de un ejemplar (decisión abierta, §10) | La que corresponda a la operación elegida | PT-01, PT-02, ME-08, ME-09 (si es OP-03); ME-11 en carga | P-08 y P-12 (consulta pública sin datos personales); prueba de persistencia: el dato sigue después de reiniciar |
| 11 | Alta, consulta, edición e inactivación de obras, ediciones, ejemplares y lectores; OP-06 inactivar | RI-03, RI-05, RI-06 (curso obligatorio para estudiantes); códigos únicos; tipo de lector (RF-11) | PT-03, PT-04, PT-08; ME-12 (ingreso), ME-13 (sin permiso) | P-10 (inactivar sin perder historial), P-11 (operación sin sesión de bibliotecaria: rechazo con ME-13) |
| 12 | OP-01 registrar préstamo y OP-02 registrar devolución | RI-01, RI-02, RI-03, RI-04, RI-07, RI-08 | PT-05, PT-06; ME-01 a ME-07, ME-11, ME-13 | P-01, P-02, P-03, P-05, P-06 (P-06a y P-06b por SC-01), **P-07** |
| 13 | OP-04 préstamos activos con fecha de referencia; OP-05 informe mensual por curso; OP-03 integrada | RI-07 (vencimiento guardado), RI-08 (curso al prestar) | PT-07, PT-09; ME-10, ME-13 | P-04, P-09, P-13 (sin internet) y una revisión del alcance mínimo de Work §7.2 |

**RI-01 ante pedidos simultáneos** (el Capítulo 9 lo remitió al 12):
- Se protege dos veces, como decidió el Capítulo 9.
  1. **Reglas de negocio:** la comprobación y el registro van en una misma operación atómica (transacción).
  2. **Persistencia:** una restricción de unicidad sobre los préstamos sin fecha de devolución de cada ejemplar.
- El Piloto B v2 lo implementó así (transacción `BEGIN IMMEDIATE` e índice único parcial). Su prueba de carrera solo corrió en Linux, y el protocolo de campo advierte que el servidor incorporado de Windows atiende los pedidos de a uno.
- El capítulo explica la protección con el contrato y la prueba P-07. No promete concurrencia verificada en Windows.
- La sección 12.2 trata también el doble envío del formulario: el patrón POST-redirección-GET y el botón desactivado (ME-11).

**Autorización en el servidor:**
- Cada operación protegida comprueba el rol en el servidor antes de hacer nada y, si falta permiso, devuelve ME-13 sin cambiar datos.
- Ocultar el botón no reemplaza esa comprobación (Work §7.5; Capítulo 9, Tabla 9.2).
- El inicio de sesión fallido devuelve ME-12 y no revela si el error estuvo en el usuario o en la contraseña.

**Lo que queda para la Unidad V:** la matriz completa de pruebas con datos independientes (encuentro 27), las pruebas de límite y entradas inválidas (28) y la regresión. En la Unidad IV solo se ejecutan las pruebas previstas de cada incremento.

## 6. Base de proyecto explicada

Work §7.5 recomienda «una base de proyecto breve y explicada que resuelva configuración y conexión». La v2.1 en 28 encuentros también la nombra.

**Propuesta:**
- partir del Piloto B v2.3 (`fase2_pilotos/B_prueba_tecnica/prototipo_v2_3/`), que tiene conexión, instalador que no destruye datos, sesión, CSRF, respaldo consistente y retiro seguro de la marca de mantenimiento;
- adaptarlo **al diseño del lote 3 (versión 1.1)** antes de usarlo en el libro.

**Diferencias que hay que resolver en esa adaptación (verificadas en el informe del Piloto B v2):**
- **Ediciones:** el piloto guarda la edición dentro de la obra; el diseño del lote 3 tiene una entidad Edición.
- **Máximos y tipo de lector:** el piloto fija las reglas como constantes; el diseño usa Parámetro y el tipo de lector (RF-11, RN-02 v1.1: dos y cinco).
- **Curso:** el piloto no guarda el curso al prestar (RI-08) ni exige curso a los estudiantes (RI-06).
- **Roles:** el piloto tiene una sola cuenta «bibliotecaria»; el diseño agrega dirección para PT-09 y OP-05, con ME-13.
- **Informe:** el piloto no tiene el informe mensual por curso.

**Reparto de la base:**
- la base trae: configuración, conexión, sesión, plantilla de pantalla y una operación de ejemplo;
- el estudiante hace: las reglas, el resto de las operaciones y las pruebas;
- se mide el tamaño final de la base (el piloto tenía 567 líneas de PHP en el núcleo, 215 de pruebas).

**Lo que la base no puede ser:** el prototipo resuelto. El libro no publica la solución completa de OP-01 y OP-02, que son la evidencia de los encuentros 23 y 24. La guía la trae como referencia para el docente.

## 7. Capítulo 10. Del diseño a la primera operación funcional (encuentros 19 y 20)

**Capacidades:** C7 y C8 (19); C6, C8 y C9 (20).

| Sección | Contenido previsto |
|---|---|
| 10.1. Preparación del entorno y estructura del proyecto. | La ficha de entorno de §4, completada en clase con lo que relevó el docente. Estructura de carpetas de la base y qué capa vive en cada una (presentación, reglas, persistencia: Figura 9.1). Dependencias del DT-01 y lo que todavía no se verificó. |
| 10.2. Versiones, bitácora y conjunto inicial de datos ficticios. | Primera versión identificable del prototipo y registro en la bitácora (C7). Datos ficticios iniciales: obras, ediciones, ejemplares, lectores de los dos tipos y cuentas de bibliotecaria y dirección, sin datos personales reales (Work §7.1). |
| 10.3. Una operación completa: formulario, procesamiento y almacenamiento. | Recorrido de una operación a través de las tres capas, del boceto (Capítulo 8) al contrato (Capítulo 9) y al dato guardado (Capítulo 7). |
| 10.4. Validación, consulta parametrizada y evidencia de persistencia. | Validación en el servidor (no solo en el navegador). Consulta parametrizada para que una entrada no altere la consulta. Evidencia de persistencia: el dato sigue después de cerrar y volver a abrir. |

**Figuras previstas:**
- recorrido de un pedido por las tres capas: reutiliza la notación de capas del Capítulo 9, sin símbolos nuevos;
- mapa de la estructura de carpetas: esquema didáctico.

**Práctica 10 — Mbokaja: demostrar una operación y vincularla con su requisito y prueba.** Decisión nueva: la escuela solo tiene la computadora donada sin internet (M-F7) y nadie que instale programas (M-F9).

**Niveles:**
1. demostrar una operación ya hecha y completar su ficha requisito-contrato-prueba (MR-xx);
2. además, agregar una validación del servidor que falte y mostrar el rechazo;
3. además, escribir la ficha de entorno de Mbokaja y decidir qué se instala, quién y cómo se respalda.

## 8. Capítulo 11. Catálogo, ejemplares y lectores (encuentros 21 y 22)

**Capacidades:** C5 y C8 (21); C6 y C8 (22).

| Sección | Contenido previsto |
|---|---|
| 11.1. Implementación de tareas priorizadas a partir de los bocetos. | El orden sale de los incrementos del Capítulo 6 y de los bocetos de PT-08. |
| 11.2. Datos obligatorios, códigos, duplicados y mensajes útiles. | Diccionario del Capítulo 7 llevado a validaciones: campos obligatorios, código de ejemplar único, curso obligatorio solo para estudiantes (RI-06), tipo de lector. Mensajes con la regla del Capítulo 8. |
| 11.3. Permisos mínimos y comprobaciones del servidor. | Zonas por rol de la Figura 8.1. Comprobación del rol en el servidor en cada pedido: **ME-13** si no hay permiso, **ME-12** solo si falla el ingreso. Evidencia de Work: «rechazo de acceso indebido». |
| 11.4. Edición y baja lógica sin pérdida de historial. | OP-06 inactivar: RI-05 y RN-06. Qué se puede editar y qué no (el código de un ejemplar con historia). |

**Práctica 11 — Mbokaja: registrar un lote distinto del ejemplo y resolver entradas inválidas.**
- **Datos nuevos:** un lote de libros donados con códigos repetidos, un lector sin grado y un título mal escrito. Hay que crearlos en `mbokaja_u4.py` sin repetir los códigos anteriores.
- **Nivel 3:** qué puede hacer el voluntario de 9.º en el sistema (permisos mínimos y supervisión, MS-5), comprobado en el servidor.

## 9. Capítulo 12. Préstamos y devoluciones consistentes (encuentros 23 y 24)

**Capacidades:** C5, C8 y C9.

| Sección | Contenido previsto |
|---|---|
| 12.1. Precondiciones y reglas de la operación de préstamo. | Contrato OP-01 implementado paso a paso: permiso (ME-13), lector activo (RI-03), máximo del tipo leído de Parámetro (RI-02), ejemplar disponible (RI-01), vencimiento calculado y guardado (RI-07), curso al prestar (RI-08). |
| 12.2. Doble envío, disponibilidad y operaciones atómicas. | Reenvío del formulario y doble clic (OBS-4 de Mbokaja). Operación atómica y restricción de unicidad para RI-01. P-07. |
| 12.3. Devolución, estado del ejemplar y conservación de historial. | Contrato OP-02: devolución única (no se devuelve dos veces), el préstamo no se borra (RI-04, RN-05) y el ejemplar vuelve a estar disponible. |
| 12.4. Fallos previsibles y comprobación de resultados. | Qué pasa si falla a mitad de camino: no queda medio préstamo. Comprobación del estado final con una consulta, como pide la evidencia de Work §7.3. |

**Práctica 12 — Mbokaja: resolver dos solicitudes incompatibles y explicar la protección elegida.** Decisión nueva: dos voluntarios cargan el mismo libro para lectores distintos al mismo tiempo, y un libro vuelve dañado (MS-1, M-N5, contrato de la Práctica 9).

## 10. Capítulo 13. Información útil e integración (encuentros 25 y 26)

**Capacidades:** C3 y C8 (25); C7 a C9 (26).

| Sección | Contenido previsto |
|---|---|
| 13.1. Búsqueda de ejemplares disponibles y préstamos activos. | OP-03 pública (disponibles como dato derivado, sin datos de lectores) y OP-04 para la bibliotecaria. |
| 13.2. Vencimientos y fecha de referencia. | La fecha de referencia como dato de entrada explícito (evidencia de Work: «fecha de referencia definida»), para que el resultado se pueda comprobar. |
| 13.3. Integración de módulos y revisión del alcance mínimo. | OP-05, informe mensual por curso, para bibliotecaria y dirección, con la autorización comprobada por el servidor. Revisión contra el alcance mínimo de Work §7.2 y la matriz de coherencia (Tabla 9.6). |
| 13.4. Demostración del incremento y registro de pendientes. | Demostración ante otro equipo; lista de incidencias para la Unidad V. |

**H4 — Revisión de unidad IV (Encuentro 26):** «circuito funcional completo; H4» (Work §6). Evidencia de Work §5.2: «H4: prototipo completo mínimo y lista de incidencias».
- **Qué se demuestra:** las condiciones mínimas de aceptación de Work §4.3 que corresponden a la unidad:
  - circuito de préstamo y devolución ejecutable;
  - persistencia comprobada;
  - historial sin pérdida;
  - rechazo del préstamo simultáneo del mismo ejemplar;
  - evidencia de las pruebas de cada incremento.
- **Lo que queda para la Unidad VI:** la instalación y la restauración reproducibles por otro equipo. En el H4 solo se muestra que el respaldo de E-11 y E-12 funciona.
- **Instrumento:** rúbrica con el formato del H1 al H3:
  - criterios que cubren C7, C8 y C9;
  - cuatro niveles;
  - 60 % de evidencia del equipo y 40 % individual (**propuesta editorial**, Work §4.3);
  - ausencia de evidencia registrada aparte;
  - planilla.
- **Evidencia individual:** cada estudiante resuelve una **variante** que propone el docente sobre el código (por ejemplo, un cambio de regla en Parámetro, un mensaje que falta o una validación nueva) y explica qué capa toca y qué prueba lo comprueba. Las variantes salen de un banco de la guía que no está en el dossier, en el buzón, en D3, en el banco del H3 ni en las prácticas.
- **Distribución:** según v2.1, 2 HC de integración (P), 1 de demostración (V) y 2 de revisión (E).

## 11. Fuente común y entregables

**Fuente** (sin tocar los módulos de los lotes 1 a 3):
- **`lote_4/caso/construccion.py`:**
  - incrementos y tareas;
  - casos de prueba de cada incremento (enlazados a P-xx);
  - banco de variantes del H4;
  - ficha de entorno E-1 a E-12.
  - Lee `lote_3/caso/diseno.py`.
- **`lote_4/caso/mbokaja_u4.py`:** datos nuevos de las Prácticas 10 a 12 (y 13 si se decide).
- **Base de proyecto adaptada:** en una carpeta propia del lote, con sus pruebas. El libro cita fragmentos leídos de esos archivos, no copiados a mano.
- **`lote_4/build/cap10.py` a `cap13.py`:** mismos atributos que los capítulos anteriores (lo comprueba `tomo.py`).
- **Maqueta O3 y controles:** los de los lotes anteriores.

**Entregables** (como en los lotes 2 y 3):
- libro del estudiante, guía docente con solucionario y cuaderno de prácticas;
- DOCX, PDF de control, scripts, informe, manifiesto SHA-256 y láminas.

**Extensión estimada en oficio O3:** libro de 40 a 50 págs. (cuatro capítulos); guía de 18 a 24; cuaderno de 8 a 12. Es una estimación; no se rellena para alcanzarla.

## 12. Controles nuevos previstos

1. **Índice de Work:** títulos, secciones, cierres, encuentros 19 a 26 y capacidades de §5.2, textuales.
2. **Contratos implementados:** cada operación OP-01 a OP-06 tiene su código, su prueba y los errores de su contrato, con los mismos mensajes.
3. **Autorización:**
   - ninguna operación usa ME-12;
   - toda operación protegida devuelve ME-13 sin cambiar datos;
   - los roles de cada operación coinciden con la zona de su pantalla (PT-09 y OP-05 para bibliotecaria y dirección).
4. **RI-01:** la base tiene las dos barreras (operación atómica y restricción de unicidad); la prueba P-07 corre y su resultado se registra con el entorno en que corrió.
5. **Historial:** ninguna operación borra préstamos, lectores ni ejemplares con historia.
6. **Pruebas de la base:** las del Piloto B adaptadas corren sin fallos en el entorno de construcción. El informe dice cuál es, y que no es una computadora escolar.
7. **Entorno:** el libro y la guía no llaman «validado» ni «probado en colegios» a ningún entorno, salvo que haya un acta de campo, y en ese caso solo para los equipos del acta.
8. **No duplicar:** sin unidad de sintaxis PHP ni manual de SQL; sin Access; sin los ejercicios de Algorítmica.
9. **Impresión:** los controles de los lotes 2 y 3, y además los fragmentos de código sin cortes de línea ni caracteres perdidos en el PDF.

## 13. Decisiones abiertas para Fernando

1. **Acta de campo:** ¿se construye el Capítulo 10 recién cuando haya al menos un acta en una computadora con Windows, o con la advertencia de «no probado en la institución»?
2. **Base de proyecto:**
   - ¿se aprueba partir del Piloto B v2.3 adaptado al diseño del lote 3 (Edición, Parámetro, tipo de lector, curso al prestar, dirección y ME-13)?
   - ¿qué tamaño máximo debe tener?
3. **Operación del Capítulo 10:** ¿consulta pública OP-03 (solo lectura, más simple) o alta de un ejemplar (escritura, prueba de persistencia más directa)?
4. **Código en el libro:** ¿fragmentos con su explicación al lado, o el listado completo de la base en un anexo de la guía?
5. **Práctica en el Capítulo 13:** Work no prevé una; los Capítulos 9 a 12 tienen la suya. ¿Se agrega una breve como complemento editorial, o el H4 alcanza?
6. **Concurrencia en Windows:** ¿se acepta explicar RI-01 con las dos barreras y P-07, aclarando que la prueba de carrera solo corrió en Linux?
7. **Entorno alternativo:** ¿la guía describe solo el criterio de evidencias equivalentes (Work §7.5), o también uno concreto si la institución lo informa?
