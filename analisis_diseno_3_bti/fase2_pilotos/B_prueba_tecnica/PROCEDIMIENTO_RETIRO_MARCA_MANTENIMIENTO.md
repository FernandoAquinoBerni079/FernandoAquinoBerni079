# Procedimiento seguro para retirar una marca de mantenimiento después de un corte de energía

**Prototipo:** `prototipo_v2_3/` (PHP + SQLite, **entorno provisional** hasta completar las pruebas de campo).
**Herramienta:** `retirar_marca.php`. **Prueba automática:** `pruebas/prueba_marca_huerfana.php`, 19 de 19 en Linux.
**Pedido:** documentar el retiro seguro de la marca que deja un corte (límite «Marca huérfana» de `ADENDA_PRUEBA_TECNICA_v2_2.md` §4).

## 1. Qué es la marca y por qué no se borra a mano

Durante un reinicio de la base (`php instalar.php --reiniciar`), el sistema crea el archivo `datos/biblioteca.sqlite.mantenimiento`. Mientras ese archivo existe:
- nadie puede abrir la base desde el sistema;
- el sitio responde «en mantenimiento» (503);
- `respaldar.php` y otro reinicio se niegan.

Si se corta la luz en medio del reinicio, la marca queda puesta y el sistema sigue bloqueado. **Es intencional:** después de un corte no se sabe en qué estado quedó la base.

Borrar la marca a mano reabre el sistema sin saber si la base está sana. Puede pasar que:
- la base tenga una transacción a medio hacer;
- falten tablas o disparadores;
- haya un respaldo cortado que alguien use después para restaurar.

Por eso el retiro se hace con una herramienta que primero comprueba.

## 2. Quién lo hace y cuándo

- **Quién:** la persona a cargo del equipo (encargado de informática o docente). La bibliotecaria trabaja con el registro manual de contingencia mientras tanto (Capítulo 3, riesgo R-02).
- **Cuándo:** con la energía restablecida y la computadora encendida normalmente, nunca durante el corte.

## 3. Pasos

| Paso | Qué se hace | Por qué |
|---:|---|---|
| 1 | Detener el servidor (Ctrl+C en la ventana de `php -S`) y cerrar cualquier programa que tenga abierta la base | Si otra conexión la tiene tomada, la herramienta se niega |
| 2 | **No** copiar, mover ni borrar a mano `biblioteca.sqlite`, `biblioteca.sqlite-journal`, `-wal` ni `-shm` | El diario y el `-wal` son lo que SQLite usa para dejar la base consistente |
| 3 | Ejecutar `php retirar_marca.php` (diagnóstico) | No cambia nada; ver §4 |
| 4 | Leer el informe en pantalla (queda también en `datos/incidentes/marca_<fecha>/informe.txt`) | Indica si la base pasó las comprobaciones y qué pasó con el reinicio |
| 5 | Si dice «se puede retirar la marca»: ejecutar `php retirar_marca.php --retirar` | Quita la marca y prueba una conexión |
| 6 | Si dice que la base **no** pasó las comprobaciones: restaurar (§5). La marca queda puesta mientras tanto | Nadie usa una base dañada |
| 7 | Iniciar el servidor y comprobar en el navegador que el catálogo responde | Cierre del incidente |
| 8 | Anotar en la bitácora fecha, informe y decisión; si el reinicio no llegó a confirmarse y todavía se quiere, repetirlo | Trazabilidad |

## 4. Qué comprueba `retirar_marca.php`

1. **¿Hay marca?** Si no hay, no hace nada (código 0).
2. **¿El mantenimiento sigue en curso?**
   - La marca guarda la fecha y el número del proceso que la creó.
   - Si ese proceso PHP sigue vivo, se niega (código 1).
   - Si el número pertenece a otro programa, lo toma como reutilizado por el sistema.
3. **Copia del estado** en `datos/incidentes/marca_<fecha>/`:
   - incluye la base, el diario (`-journal`), `-wal`, `-shm` y la marca;
   - se hace **antes** de abrir la base con SQLite, para conservar evidencia del momento del corte.
4. **Bloqueo exclusivo sin esperar.**
   - Si otra conexión tiene la base tomada, se niega (código 1).
   - Al abrir la base, SQLite deshace la transacción que el corte dejó a medias (diario «caliente») o recupera lo confirmado en el `-wal`. Es su mecanismo normal de recuperación.
5. **Comprobaciones** (si alguna falla, la marca queda puesta y sale con código 2):
   - `integrity_check`;
   - claves foráneas;
   - versión del esquema;
   - las cinco tablas;
   - el índice único de RN-01;
   - los disparadores del historial (RN-05, RN-06);
   - al menos una cuenta de bibliotecaria.
6. **Respaldos posteriores a la marca** (los del reinicio interrumpido):
   - los verificados se informan y se comparan con la base: indican si el reinicio llegó a confirmarse o no;
   - los incompletos se **apartan** a la carpeta del incidente con la extensión `.incompleto`, para que nadie los use.
7. **Solo con `--retirar` y todo correcto:**
   - se libera el bloqueo;
   - se quita la marca;
   - se prueba `conectar()`.

## 5. Si la base no pasa las comprobaciones

1. La marca queda puesta; no la borres.
2. Elegí el respaldo más reciente que la herramienta informó como verificado, o el último de `datos/respaldos/` tomado **antes** de la fecha de la marca.
   - Nunca uses los archivos `.incompleto`.
3. Con el servidor detenido, reemplazá `datos/biblioteca.sqlite` por una copia de ese respaldo.
   - Los archivos `-journal`, `-wal` y `-shm` de la base dañada se quitan antes de copiar: ya están guardados en la carpeta del incidente.
4. Ejecutá de nuevo `php retirar_marca.php`.
   - Si el respaldo pasa las comprobaciones, seguí con el paso 5 de §3.
5. Los préstamos registrados entre ese respaldo y el corte se recuperan de la planilla manual de contingencia.

## 6. Evidencia

`pruebas/prueba_marca_huerfana.php` simula cortes reales: mata con SIGKILL el proceso que hace el mantenimiento. Resultado: **19 de 19** (salida en `resultados_v2_3/salida_pruebas_linux.txt`).

| Caso | Resultado esperado y obtenido |
|---|---|
| Sin marca | No hace nada |
| Proceso del mantenimiento vivo | Se niega; marca y base intactas |
| Corte durante la espera del reinicio | Marca huérfana; `conectar()` rechaza. El diagnóstico no cambia nada y guarda copia e informe. `--retirar` quita la marca y la conexión funciona. Los préstamos siguen. |
| Corte a mitad del reinicio (tablas borradas y recreadas sin confirmar, con diario caliente) | SQLite deshace la transacción al abrir; vuelven los préstamos originales; no queda la tabla a medias; la copia del incidente conserva el diario |
| Corte con la base en modo WAL | El préstamo confirmado antes del corte aparece |
| Otra conexión con la base tomada | Se niega; la marca sigue |
| Respaldo cortado posterior a la marca | Se aparta como `.incompleto` |
| Base dañada | Código 2; la marca queda; el sistema sigue bloqueado; indica restaurar |
| Falta el disparador del historial | Código 2; la marca queda |

Regresión de la v2.3 en la misma corrida:

| Prueba | Resultado |
|---|---|
| `prueba_mantenimiento.php` | 30 de 30 |
| `prueba_respaldo.php` | 18 de 18 |
| `prueba_garantias.php` | 14 de 14 |
| `prueba_reglas.php` | 37 de 37 |
| `prueba_carrera.php` | 10 de 10 |
| `prueba_http.sh` | 32 de 32 |

## 7. Límites

- **Solo se probó en Linux** (Ubuntu, PHP 8.3.6, SQLite 3.45.1).
  - En Windows, la comprobación del proceso vivo usa `posix_kill`, que no existe. La herramienta sigue funcionando, pero ese control queda en manos de la persona (paso 1).
  - El bloqueo de archivos es distinto. Se agrega a las pruebas de campo pendientes (`PRUEBAS_PENDIENTES_CAMPO.md`, punto 8).
- La simulación del corte mata el proceso, pero no apaga el disco.
  - Un corte real puede perder escrituras que el sistema operativo todavía no había pasado al disco.
  - Para eso están `integrity_check` y la restauración de §5. La prueba con daño intencional de la base cubre ese caso, pero no reproduce un apagado físico.
- El indicio «el reinicio llegó o no a confirmarse» compara la cantidad de préstamos con el respaldo del reinicio. Es una ayuda para decidir, no una prueba.
- La herramienta no impide que otro programa copie o reemplace la base por su cuenta.
- **PHP + SQLite sigue siendo provisional.**
