# Cierre de observaciones — Fase 2, Análisis y Diseño de Sistemas 3.º BTI

**Commit de las correcciones:** `d20a657b3c7fb70e1fb3b8f183a55e89155f8cc7`, rama `claude/libros-5z31jx`.

**Base auditada:** commit `47475d3b083e5955407ab81fa641c54f4bbc65dd`.

**Alcance de la ronda:**
- El commit de correcciones **solo agrega archivos**: 48 nuevos y ningún archivo de commits anteriores modificado, según `git diff --name-status 47475d3 d20a657`.
- No se construyó el resto del libro, no se subió nada a Drive y no se declara aptitud comercial.
- La autorización para producir la colección sigue pendiente de Fernando.
- Se mantienen como provisionales la identidad verde BTI y las 5 HC semanales.

| N.º | Observación | Estado | Corrección y evidencia |
|---|---|---|---|
| 1 | Respaldo SQLite consistente antes de reiniciar | **Resuelta** | `prototipo_v2_1/src/respaldo.php`: `VACUUM INTO`, luego `integrity_check` y conteo de filas por tabla. Lo comparten `instalar.php` y `respaldar.php`. Si el respaldo falla, no se borra nada. **Defecto reproducido con el instalador v2:** de 2 préstamos confirmados, su respaldo tenía 0. **Prueba nueva `prueba_respaldo.php`: 15 de 15** (WAL, escritura sin confirmar, integridad, falla del respaldo con la base intacta, restauración). |
| 2 | Distinguir lo que garantiza SQLite de lo que verifica PHP | **Resuelta** | `ADENDA_PRUEBA_TECNICA_v2_1.md` §2 y `prueba_garantias.php`, con **14 de 14** clasificaciones confirmadas con SQL directo. **SQLite:** RN-01, RN-05, RN-06, CHECK, UNIQUE y claves foráneas (estas, solo con `foreign_keys = ON`). **PHP en transacción:** RN-02, RN-03, RN-04 y ejemplar dado de baja. |
| 3 | Correspondencia de los 15 requisitos con sus criterios en la guía | **Resuelta** | Guía docente v2.1, sección 3 (`A2_capitulo4_v2_1/`). **Origen de los criterios:** <ul><li>6 modelos resueltos en el libro;</li><li>3 trabajos del estudiante;</li><li>6 referencias para el docente.</li></ul> **`verificar_v2_1.py`: 31 correctos, 0 fallos.** El libro del estudiante v2 no cambia. |
| 4 | Proceso actual simplificado en la fusión 9+10 del plan de 28 | **Resuelta** | `C_informe_esfuerzo/v2_1/`: el encuentro 8 del plan conserva un diagrama simplificado del proceso actual (evidencia de C4). Hay un control nuevo en el script. Horas y totales sin cambios; la tabla de 36 es idéntica a la v2. |
| 5 | Preparar la integración del candidato al Capítulo 2 sin generarlo | **Resuelta** | `A1_candidato_capitulo2/integracion/`: plan y mapa comprobado por script. **Destino de los 31 elementos:** <ul><li>se conservan 8;</li><li>se adaptan 15;</li><li>se divide 1;</li><li>se trasladan 3 al Capítulo 1;</li><li>se retiran 4.</li></ul> Renumeración a 2.x, encuentros 3 y 4, capacidad C2. Los fragmentos de E1 y E3 que cita el Capítulo 4 están presentes en el candidato. El candidato v1.1 queda sin cambios. |
| 6 | Mantener documentadas las pruebas de Windows y equipos escolares | **Resuelta como documentación; las pruebas siguen pendientes** | `PRUEBAS_PENDIENTES_CAMPO.md`: 8 pruebas pendientes, procedimiento por equipo, acta y criterio para fijar el entorno. **PHP + SQLite sigue provisional; el entorno no es definitivo.** |

## Pruebas realizadas en esta ronda

**Entorno:** Ubuntu 24.04, PHP 8.3.6, SQLite 3.45.1. Salida completa en `B_prueba_tecnica/resultados_v2_1/salida_pruebas_linux.txt`.

| Prueba | Resultado |
|---|---|
| Reproducción del defecto de la v2 | Respaldo con 0 de 2 préstamos confirmados |
| `prueba_respaldo.php` (nueva) | 15 de 15 |
| `prueba_garantias.php` (nueva) | 14 de 14 |
| `prueba_reglas.php` (regresión) | 37 de 37 |
| `prueba_carrera.php` (regresión) | 10 de 10 |
| `prueba_http.sh` (regresión) | 32 de 32 |
| `verificar_v2_1.py` (guía del Capítulo 4) | 31 correctos, 0 fallos |
| `distribucion.py` v2.1 | Todos los controles correctos (36, 28, C1 a C10, H1 a H6 y C4 en la fusión 9+10) |
| `mapa_integracion.py` | Todos los controles correctos |

## Sigue pendiente

- **Pruebas de campo:** Windows, equipos escolares, PHP 7.4 a 8.2 y antivirus.
- **Identidad:** cotejo del verde BTI con el catálogo.
- **Decisiones de Fernando ya registradas:** permisos mínimos en el núcleo, reparto del tiempo, adaptación de 28 encuentros, traslado del mapa de interesados al Capítulo 1 y autorización de la producción.
