# Piloto B, versión 2.3 — Adenda: retiro seguro de la marca de mantenimiento

**Estado:** agregado pedido al autorizar la Fase 3 («Documentar también el procedimiento seguro para retirar una marca de mantenimiento después de un corte eléctrico»). **PHP + SQLite sigue provisional** hasta completar las pruebas de campo.

**Sin cambios:** `prototipo_v2/`, `prototipo_v2_1/`, `prototipo_v2_2/` y sus informes. La v2.3 es una copia de la v2.2 con estos cambios:

| Archivo | Cambio |
|---|---|
| `retirar_marca.php` | Nuevo. Diagnóstico y retiro seguro de una marca huérfana. |
| `pruebas/prueba_marca_huerfana.php` | Nuevo. Simula cortes con SIGKILL. |
| `pruebas/_corte.php` | Nuevo. Auxiliar de la prueba anterior. |
| `src/mantenimiento.php` | Solo cambia el mensaje cuando ya hay una marca: en lugar de «borralo a mano», remite a `retirar_marca.php`. |
| `LEEME.txt` | Pasos para después de un corte y la prueba nueva. |

**Procedimiento:** `PROCEDIMIENTO_RETIRO_MARCA_MANTENIMIENTO.md`.

**Resultados** (`resultados_v2_3/salida_pruebas_linux.txt`):

| Prueba | Resultado |
|---|---|
| `prueba_marca_huerfana.php` (nueva) | 19 de 19 |
| `prueba_mantenimiento.php` | 30 de 30 |
| `prueba_respaldo.php` | 18 de 18 |
| `prueba_garantias.php` | 14 de 14 |
| `prueba_reglas.php` | 37 de 37 |
| `prueba_carrera.php` | 10 de 10 |
| `prueba_http.sh` | 32 de 32 |

**Límites:** ver el procedimiento, §7. En particular:
- solo se probó en Linux;
- el corte se simula matando el proceso, no apagando el disco.
