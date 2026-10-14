# Piloto B, versión 2 — Prueba técnica PHP + SQLite ajustada al modelo de Work

**Proyecto:** Análisis y Diseño de Sistemas, 3.º BTI (Plan Optativo).
**Estado:** candidato para reauditoría. No es una decisión cerrada sobre el entorno.

**Archivos:**
- La versión 1, auditada en `5044b60`, queda sin cambios en `prototipo/` y `INFORME_PRUEBA_TECNICA_PHP_SQLITE.md`.
- La versión 2 está en `prototipo_v2/`; sus resultados, en `resultados_v2/`.

**Referencia:** informe de Work «BTI3_Analisis_Diseno_Diagnostico_Propuesta_v0.1.pdf» (22 págs., SHA-256 `3d4f5ab9daf3329f0dd34b13bc30b7001cb8e65780262c536346dbbea065069a`).

**Se cotejó con:**
- §7.2 Alcance mínimo de producto, reglas iniciales RN y modelo mínimo;
- §7.3 Ejemplo de trazabilidad: N-02, RN-01, RF-04, P-07;
- §4.4 Condiciones mínimas de aceptación del prototipo;
- encuentros 19 a 26.

## 1. Qué cambió respecto de la versión 1

| Observación de la reauditoría | Versión 1 | Versión 2 |
|---|---|---|
| Distinguir obra/edición, ejemplar y préstamo | Tabla `libros` con una cantidad de ejemplares | Tablas `obras` (descripción bibliográfica con edición) y `ejemplares` (libro físico con código único `EJ-0001`…) |
| Préstamo contra un ejemplar identificable | El préstamo apuntaba al libro | `prestamos.ejemplar_id` apunta a un ejemplar concreto |
| Sin préstamos activos incompatibles | Se comprobaba solo en el código PHP | **Dos barreras para RN-01.** (1) Comprobación dentro de una transacción `BEGIN IMMEDIATE`. (2) Índice único parcial de la base: `prestamos(ejemplar_id) WHERE fecha_devolucion IS NULL`. |
| RN-02: máximo dos préstamos activos por lector | No existía | Comprobación dentro de la misma transacción `BEGIN IMMEDIATE` |
| Conservar el historial | Nada impedía borrar | **Disparadores de la base que impiden:** <ul><li>borrar préstamos;</li><li>cambiar el ejemplar, el lector o la fecha de salida;</li><li>devolver dos veces;</li><li>borrar lectores o ejemplares con historial, que se inactivan (RN-05 y RN-06).</li></ul> |
| Proteger los datos ante el instalador | Borraba la base sin avisar | **Si la base existe:** se niega y no toca nada. **Para empezar de cero:** hace falta `--reiniciar` y escribir «REINICIAR». Antes de borrar guarda una copia en `datos/respaldos/`. |
| Permisos mínimos de Work | No tenía; los había trasladado a las ampliaciones | **Sin sesión:** solo el catálogo, sin formularios de modificación. **Con sesión «bibliotecaria»:** préstamo, devolución y consultas. **Seguridad:** <ul><li>clave guardada con `password_hash`;</li><li>ficha anti-falsificación (CSRF) en cada formulario;</li><li>sesión regenerada al ingresar.</li></ul> |
| Reenvío del formulario (encuentro 23) | Un reenvío intentaba otro préstamo | Patrón POST-redirección-GET. Un reenvío forzado lo rechaza RN-01. |
| Vencimientos con fecha de referencia (encuentro 25) | No existía | RN-03: plazo de 7 días; consulta de vencidos con una fecha de referencia explícita |
| Respaldo y restauración (§7.2) | No existía | `respaldar.php`, que hace una copia consistente con `VACUUM INTO`. La restauración es manual y está probada. |

**Sobre RN-01 a RN-06.** Work las presenta como reglas iniciales para negociar en clase, supuestos didácticos y no normas del MEC. El prototipo las fija como constantes y comentarios en `src/db.php` para que se puedan cambiar.

## 2. Discrepancia de permisos: resolución propuesta

En la versión 1 los permisos quedaron fuera del núcleo. Work, en cambio, los incluye en el alcance mínimo:
- encuentro 22: «Implementar lectores y permisos mínimos»;
- §7.2: «la consulta de catálogo no permite modificar préstamos; las operaciones requieren un rol autorizado».

**Propuesta, que requiere OK de Fernando:**

| Núcleo (permisos mínimos, como Work) | Ampliación (fuera del núcleo) |
|---|---|
| Separar la consulta pública de las operaciones | Varios roles con permisos distintos: docente, auxiliar, dirección |
| Una cuenta con rol de operación, con clave cifrada | Alta, baja y edición de cuentas desde la aplicación |
| Rechazo de operaciones sin sesión (403), comprobado en el servidor | Recuperación de clave, bloqueo por intentos fallidos, registro de auditoría por usuario |
| Protección CSRF y regeneración de la sesión | Sesiones con vencimiento configurable, HTTPS en un servidor real |

Con esto, la frase de la versión 1 «autenticación, permisos y concurrencia son ampliaciones» queda reemplazada por:
- los permisos **mínimos** son núcleo;
- la **gestión** de usuarios y roles es ampliación;
- la protección del núcleo frente a operaciones simultáneas también es núcleo (RN-01 y RN-02 en la base);
- una **evaluación de concurrencia** en condiciones reales es tarea pendiente (§5).

## 3. Qué demuestra el piloto y qué no implementa todavía

| Demuestra (con prueba automática) | No implementa o no demuestra |
|---|---|
| Separación obra/edición y ejemplar, y préstamo contra un ejemplar con código | Alta, edición y baja de obras, ejemplares y lectores desde la interfaz (encuentros 21 y 22). Hoy se cargan con el instalador; la inactivación existe como función, sin pantalla. |
| RN-01 a RN-06 en el código y en la base, con rechazos explicados | Reglas fuera del núcleo de Work: multas, reservas, renovaciones, lotes de varios ejemplares |
| Historial conservado: sin borrados, devolución única, datos del préstamo fijos | Consulta del historial completo de un ejemplar o de un lector en pantalla |
| Permisos mínimos: consulta pública y operación con sesión, CSRF, 403 | Gestión de usuarios y roles (ampliación, §2) |
| Persistencia entre ejecuciones; respaldo con el servidor en marcha; restauración manual | Restauración guiada desde la aplicación; guía de instalación para el estudiante (Capítulo 17) |
| Instalador que no destruye datos existentes | Migración de una base de la versión 1 a la 2: son esquemas incompatibles y no se migra |
| Vencidos respecto de una fecha de referencia | Informes agregados para la dirección (préstamos por curso o por mes) |
| Rechazo correcto de pedidos simultáneos **en una computadora, sobre disco local** | Ver §5 |

**Tamaño del núcleo:** 567 líneas de PHP (`src/`, `public/`, `instalar.php` y `respaldar.php`). Las pruebas suman 215 líneas aparte. En el libro, este código se entrega como base explicada (Work, §7.5). El estudiante analiza, completa y prueba; no escribe desde cero.

## 4. Resultados

**Entorno:** Ubuntu 24.04 (x86_64), PHP 8.3.6, SQLite 3.45.1. Salida completa en `resultados_v2/salida_pruebas_linux.txt`.

| Prueba | Qué comprueba | Resultado |
|---|---|---|
| `prueba_reglas.php` | Modelo, RN-01 a RN-06, validaciones, vencidos, catálogo e historial, sin servidor web | **37 de 37** |
| `prueba_carrera.php` | 5 rondas en procesos separados que largan a la vez: 12 pedidos del mismo ejemplar y 8 pedidos de un mismo lector | **10 de 10.** Siempre 1 préstamo en el primer caso y 2 en el segundo. Los demás pedidos recibieron el mensaje de la regla y ninguno quedó en «base ocupada». |
| `prueba_http.sh` | De punta a punta: permisos, CSRF, POST-redirección-GET, reenvío, RN-02 y RN-04, devolución, entradas hostiles, cierre de sesión, persistencia, instalador protegido, respaldo y restauración, 8 pedidos HTTP simultáneos | **32 de 32** |
| `verificar_entorno.php` | Versiones de PHP (≥ 7.4) y SQLite (≥ 3.27), extensiones, permisos de la carpeta | Todo correcto |

**Capturas:**
- `resultados_v2/captura_catalogo_publico.png`: consulta sin sesión;
- `resultados_v2/captura_operaciones.png`: operaciones con sesión, con el rechazo de RN-02 y la lista de vencidos.

## 5. Alcance de la verificación de concurrencia

Las pruebas de simultaneidad **no equivalen a una verificación completa de concurrencia de las reglas del negocio.**

**Lo que comprueban:**
- con varios procesos en la misma computadora y la base en disco local, RN-01 y RN-02 no se violan;
- con 8 pedidos HTTP en sesiones distintas, servidos por 4 a 8 procesos de `php -S`, queda un único préstamo activo.

**Lo que no comprueban:**
1. **Otros sistemas y almacenamientos:** Windows, carpetas de red o pendrives. La documentación de SQLite desaconseja la base sobre sistemas de archivos en red.
2. **Volumen:** cargas grandes ni pedidos sostenidos.
3. **Otras operaciones concurrentes:** devoluciones simultáneas a préstamos, ni modificaciones del catálogo.
4. **El servidor de Windows:** la variable `PHP_CLI_SERVER_WORKERS` solo funciona en Linux y macOS. En Windows, `php -S` atiende los pedidos de a uno.
5. **El razonamiento formal:** que ninguna combinación de operaciones viola las reglas.

La versión 1 mostraba solo el bloqueo de escritura de SQLite. Eso es un comportamiento del motor, no una prueba de las reglas.

## 6. Requisitos, instalación y limitaciones del entorno

**Instalación:** sin cambios respecto de la versión 1 (PHP en línea de comandos con `pdo_sqlite`). Se agregan dos verificaciones:
- SQLite 3.27 o superior, para índices parciales y `VACUUM INTO`;
- las extensiones `session` y las funciones de seguridad.

**Limitaciones que siguen abiertas:**
- No se probó en Windows ni en equipos escolares.
- No se probó PHP 7.4–8.2: el código evita funciones exclusivas de PHP 8, pero solo se ejecutó en 8.3.
- El servidor incorporado es para desarrollo.
- No se probaron antivirus ni políticas de equipos administrados.

## 7. Recomendación

PHP + SQLite se mantiene como **alternativa provisional**. No se fija para todo el libro hasta una prueba de campo en el laboratorio destino, en al menos dos máquinas, una de ellas con Windows:
1. correr `verificar_entorno.php`;
2. correr `prueba_reglas.php`;
3. hacer un recorrido manual de préstamo y devolución.

**Si el laboratorio usa otro entorno que domine,** Work (§7.5) admite reemplazarlo cuando produzca evidencias equivalentes: las mismas reglas, pruebas y entregables.
