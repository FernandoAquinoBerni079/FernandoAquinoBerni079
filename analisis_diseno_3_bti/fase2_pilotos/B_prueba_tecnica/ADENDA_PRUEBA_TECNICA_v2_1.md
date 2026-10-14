# Piloto B, versión 2.1 — Adenda: respaldo consistente y garantías de las reglas

**Estado:** corrección acotada pedida en la última ronda de auditoría.

**Archivos sin cambios:** `prototipo_v2/` y `INFORME_PRUEBA_TECNICA_v2.md` (commit `47475d3`). La versión corregida está en `prototipo_v2_1/` y las evidencias, en `resultados_v2_1/salida_pruebas_linux.txt`.

**Cambios respecto de la v2:**
- `src/respaldo.php` (nuevo);
- `instalar.php` y `respaldar.php`, que ahora usan ese procedimiento;
- `src/db.php`: se agrega `cerrar_conexion()`;
- dos pruebas nuevas y una reproducción del defecto;
- `LEEME.txt`.

Nada más cambió.

## 1. Respaldo antes de reiniciar

**Defecto de la v2.** `instalar.php --reiniciar` copiaba el archivo de la base con `copy()`. Eso no garantiza una copia consistente:
- **En modo WAL**, lo último confirmado puede estar todavía en el archivo `-wal`, que la copia no incluye.
- **Si otra conexión está confirmando una escritura**, la copia puede quedar a mitad de camino.

**Reproducción con el instalador v2 sin modificar** (`pruebas/reproducir_defecto_v2.php`): había 2 préstamos confirmados y el respaldo que dejó el instalador tenía **0**.

**Corrección.** `instalar.php` y `respaldar.php` usan ahora la misma función, `respaldar_base()` en `src/respaldo.php`:
1. hace la copia con `VACUUM INTO`, que lee una instantánea consistente a través de SQLite;
2. abre el respaldo por separado y exige `PRAGMA integrity_check = ok` y la misma cantidad de filas que la base en cada tabla;
3. si algo falla, borra el respaldo incompleto y el instalador **no toca la base**;
4. recién con el respaldo verificado, el instalador borra la base y sus archivos auxiliares (`-wal`, `-shm`, `-journal`) antes de crear la nueva.

**Prueba nueva, `pruebas/prueba_respaldo.php`: 15 de 15.**

| Caso | Resultado |
|---|---|
| Método anterior (`copy()`) con datos en `-wal` | 2 de 4 préstamos: el defecto se reproduce |
| `instalar.php --reiniciar` con otra conexión abierta en modo WAL | El respaldo tiene los 4 préstamos confirmados |
| Escritura sin confirmar durante el respaldo | No aparece en el respaldo |
| Integridad del respaldo | `integrity_check = ok` |
| Archivos auxiliares de la base anterior | No quedan junto a la base nueva |
| El respaldo no se puede crear (carpeta bloqueada) | El instalador se niega (código 1) y la base queda idéntica, con el mismo SHA-256 |
| `respaldar.php` | Mismo procedimiento, respaldo verificado |
| Restauración del respaldo previo | Vuelven los 4 préstamos |

**Sin regresiones**, con las pruebas de la v2 corridas sobre la v2.1:

| Prueba | Resultado |
|---|---|
| Reglas | 37 de 37 |
| Rondas simultáneas | 10 de 10 |
| De punta a punta (HTTP) | 32 de 32 |

**Límite.** La restauración sigue siendo manual: con el servidor detenido, se borran `-wal` y `-shm` si existen y se copia el respaldo.

## 2. Quién garantiza cada regla

La v2 decía «RN-01 a RN-06 en la base», y eso no es exacto. La prueba nueva `pruebas/prueba_garantias.php` intenta violar cada regla con SQL directo, sin pasar por las funciones PHP, y clasifica el resultado. **14 de 14 clasificaciones confirmadas.**

| Regla | Garantizada por | Mecanismo | Qué pasa si se escribe en la base sin pasar por PHP |
|---|---|---|---|
| RN-01: un préstamo activo por ejemplar | **SQLite** (y también PHP, para dar el mensaje) | Índice único parcial | Rechazado |
| RN-05: la devolución no borra; devolución única; datos del préstamo fijos | **SQLite** | Disparadores | Rechazado |
| RN-06: no borrar lectores ni ejemplares con historial | **SQLite** | Disparadores | Rechazado |
| Fechas coherentes, códigos únicos, valores permitidos | **SQLite** | CHECK y UNIQUE | Rechazado |
| Referencias a ejemplares y lectores existentes | **SQLite, con una condición** | Claves foráneas, activas solo si la conexión ejecuta `PRAGMA foreign_keys = ON`, como hace `conectar()` | Rechazado con el pragma activo; **aceptado** desde una conexión que no lo activa |
| RN-02: máximo de préstamos activos por lector | **PHP**, dentro de una transacción `BEGIN IMMEDIATE` | `registrar_prestamo()` | **Aceptado** |
| RN-03: plazo de 7 días | **PHP** (la base solo exige vencimiento ≥ salida) | `registrar_prestamo()` calcula el vencimiento | **Aceptado** |
| RN-04: lector inactivo | **PHP**, dentro de la transacción | `registrar_prestamo()` | **Aceptado** |
| Ejemplar dado de baja | **PHP**, dentro de la transacción | `registrar_prestamo()` | **Aceptado** |
| Permisos, CSRF y validación de entradas | **PHP** (aplicación) | `auth.php` y las páginas | No aplica |

**Consecuencia.** RN-02, RN-03 y RN-04 solo se cumplen si toda escritura pasa por las funciones del núcleo. Un docente que edite la base con una herramienta externa puede violarlas. Las de SQLite, en cambio, se sostienen igual.

**Posibilidad para la Unidad IV, no implementada:** llevar RN-02 y RN-04 a la base con disparadores. Es una decisión de diseño que el libro puede plantear como ejercicio del Capítulo 12.

## 3. Pruebas pendientes y estado del entorno

El entorno **no es definitivo**: PHP + SQLite sigue como alternativa provisional. El protocolo de las pruebas que faltan está en `PRUEBAS_PENDIENTES_CAMPO.md`:
- Windows;
- equipos escolares;
- PHP 7.4 a 8.2;
- antivirus y políticas de equipos administrados;
- carpetas de red o pendrives.
