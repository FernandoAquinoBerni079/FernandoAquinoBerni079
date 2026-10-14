# Piloto B, versión 2.2 — Adenda: reinicio sin conexiones activas

**Estado:** corrección técnica pedida en el cierre de la Fase 2.

**Archivos sin cambios:** `prototipo_v2/`, `prototipo_v2_1/` y sus informes. La versión corregida está en `prototipo_v2_2/` y las evidencias, en `resultados_v2_2/salida_pruebas_linux.txt`.

**Cambios respecto de la v2.1:**
- `src/mantenimiento.php` (nuevo);
- `src/db.php`: conexiones rechazadas durante el mantenimiento y respuesta 503 en el servidor web;
- `instalar.php`: el reinicio usa el mantenimiento, y la carga de datos pasa a una función;
- `respaldar.php`: se niega durante el mantenimiento;
- `pruebas/prueba_mantenimiento.php` y `pruebas/reproducir_defecto_v2_1.php` (nuevos);
- `pruebas/prueba_respaldo.php`, adaptado (ver §3);
- `LEEME.txt`.

## 1. El defecto

El instalador de la v2.1:
1. hacía el respaldo con `VACUUM INTO`, que lee una instantánea aunque otra conexión esté escribiendo;
2. seguía adelante;
3. borraba el archivo de la base.

**Reproducción** (`pruebas/reproducir_defecto_v2_1.php`, sobre la v2.1 sin modificar):
- otra conexión tiene un préstamo sin confirmar;
- `instalar.php --reiniciar` termina con código 0;
- la otra conexión **no puede confirmar** («disk I/O error»);
- la base queda con 0 préstamos: **el préstamo se perdió**.

**El mismo caso con la v2.2:**
- el reinicio se niega con código 1;
- la otra conexión confirma sin error;
- el préstamo se conserva.

## 2. El procedimiento de mantenimiento (`src/mantenimiento.php`)

1. **Marca de mantenimiento.** Se crea el archivo `biblioteca.sqlite.mantenimiento` en forma exclusiva: si ya existe, el reinicio se niega. Mientras existe:
   - `conectar()` rechaza conexiones nuevas;
   - el sitio responde **503** con un aviso;
   - `respaldar.php` se niega.
2. **Sin conexiones activas.**
   - **Base en modo WAL:** primero se la pasa a modo DELETE. SQLite solo lo permite si ninguna otra conexión la tiene abierta, aunque esté inactiva. La base queda en modo DELETE, el predeterminado del prototipo, y el instalador lo informa.
   - **Bloqueo:** se obtiene la transacción exclusiva y, dentro de ella, se activa `locking_mode = EXCLUSIVE`, que retiene el bloqueo hasta el final.
   - **Espera:** hasta 5 segundos, con intentos cortos que sueltan el bloqueo entre uno y otro, para que una operación en curso pueda terminar.
   - **Si no se obtiene:** el reinicio se niega y no toca nada.
3. **Con el bloqueo tomado**, ninguna otra conexión puede leer ni escribir:
   - respaldo consistente y verificado, con el mismo procedimiento de la v2.1;
   - reinicio **dentro del mismo archivo**: se eliminan y recrean las tablas en una sola transacción, y si algo falla se revierte.
   - **El archivo no se borra ni se reemplaza.** Una conexión inactiva que hubiera quedado abierta en modo DELETE ve después la base nueva y escribe en ella, no en un archivo huérfano.
4. **Siempre** se libera el bloqueo y se quita la marca, salga bien o mal.

## 3. Pruebas

**Prueba nueva: `pruebas/prueba_mantenimiento.php`, 30 de 30.** Repetida cuatro veces con el mismo resultado.

| Caso | DELETE | WAL |
|---|---|---|
| Otra conexión con una escritura sin confirmar | Se niega tras 5 s. Sin respaldo ni marca sobrantes. La otra conexión confirma sobre la base intacta. | Igual |
| Otra conexión con una lectura en curso | Se niega y la base queda igual | Igual |
| La otra transacción termina durante la espera | Reinicia después, y el respaldo incluye lo confirmado | Igual |
| Durante la ventana de mantenimiento | Otra conexión no puede leer ni escribir; `conectar()` rechaza | Igual |
| Otra conexión abierta e inactiva que ya leyó la base | El reinicio se hace en el mismo archivo (mismo inodo). Esa conexión ve la base nueva y lo que escribe queda en ella. | El reinicio se niega |
| Marca de mantenimiento presente | `conectar()` rechaza; otro reinicio se niega con la base idéntica; `respaldar.php` se niega; el sitio responde 503 y vuelve a 200 al quitar la marca | — |

**Regresión sobre la v2.2:**

| Prueba | Resultado | Nota |
|---|---|---|
| `prueba_respaldo.php` | 18 de 18 | Adaptada |
| `prueba_garantias.php` | 14 de 14 | |
| `prueba_reglas.php` | 37 de 37 | |
| `prueba_carrera.php` | 10 de 10 | |
| `prueba_http.sh` | 32 de 32 | |

**Adaptación de `prueba_respaldo.php`.** En la v2.1 esperaba que el reinicio se hiciera con otra conexión en plena transacción; ahora comprueba que se niegue. El respaldo con esa conexión abierta se prueba con `respaldar.php`, que solo lee una instantánea.

**Hallazgo durante las pruebas.** La primera versión de `prueba_respaldo.php` copiaba el archivo de la base con `copy()` dentro del mismo proceso que tenía la otra conexión abierta. En Linux eso suelta los bloqueos POSIX de esa conexión (es una advertencia documentada de SQLite), y el reinicio la encontraba «libre». La copia ahora se hace en otro proceso.

**Consecuencia práctica, ya en el `LEEME.txt`:** no copiar ni mover el archivo de la base con otros programas mientras esté abierta; usar `respaldar.php`.

## 4. Límites

- **Solo Linux.** Windows usa otro mecanismo de bloqueo; el reinicio en Windows se agrega a las pruebas de campo pendientes (`PRUEBAS_PENDIENTES_CAMPO.md`, punto 8).
- **Marca huérfana.** Si un corte de energía deja el archivo de marca, el sistema queda «en mantenimiento» hasta borrarlo a mano. Es intencional: es preferible a reabrir una base cuyo reinicio no se sabe si terminó.
- **Herramientas externas.** El procedimiento no puede impedir que otro programa copie o reemplace el archivo de la base por su cuenta.
- **Entorno provisional.** PHP + SQLite sigue sin declararse definitivo.
