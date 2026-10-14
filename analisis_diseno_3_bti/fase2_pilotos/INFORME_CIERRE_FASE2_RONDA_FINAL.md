# Cierre de la Fase 2 — Ronda final (reinicio de SQLite y evidencia de C3)

**Commit de esta ronda:** `08b46f915c8c6d098c13fc8e0d02ba76dc342adc`, rama `claude/libros-5z31jx`.

**Base revisada:** `d20a657` y `bdee2ed`.

**Alcance:**
- El commit **solo agrega archivos**: 28 nuevos y ninguno anterior modificado, según `git diff --name-status bdee2ed 08b46f9`.
- No se rehicieron los pilotos ni se iniciaron los 18 capítulos.
- No se subió nada a Drive y no se declara aptitud comercial.

| N.º | Ajuste pedido | Estado | Corrección y evidencia |
|---|---|---|---|
| 1 | El reinicio de SQLite no debe sustituir la base con conexiones activas | **Resuelto** | **Nueva versión** `B_prueba_tecnica/prototipo_v2_2/`, con `src/mantenimiento.php`: <ul><li>marca de mantenimiento que rechaza conexiones nuevas (503 en el sitio);</li><li>salida de WAL, que solo es posible sin otras conexiones abiertas;</li><li>bloqueo exclusivo con espera limitada;</li><li>respaldo verificado;</li><li>reinicio **dentro del mismo archivo**, sin borrarlo ni reemplazarlo.</li></ul> **Defecto reproducido en la v2.1:** el reinicio siguió con otra conexión en plena transacción y el préstamo de esa conexión se perdió (I/O error). En la v2.2 el reinicio se niega y el préstamo se conserva. **Prueba nueva `prueba_mantenimiento.php`: 30 de 30**, repetida. **Regresión:** 18/18, 14/14, 37/37, 10/10 y 32/32. Detalle en `ADENDA_PRUEBA_TECNICA_v2_2.md`. |
| 2 | Todos los alumnos redactan al menos un criterio de aceptación sobre un requisito de calidad | **Especificado para la próxima versión** | `A2_capitulo4_proxima_version/ESPECIFICACION_EVIDENCIA_C3.md`: <ul><li>consigna común obligatoria en la Práctica 4 (RNF-04 a partir del pedido B-03, con su criterio);</li><li>ajustes en los Niveles 2 y 3 y en el tiempo;</li><li>clave, fila de la lista de cotejo y fila de correspondencia en la guía;</li><li>control automático que se agregará.</li></ul> No se rehizo el capítulo, por indicación. |
| — | Plan del primer lote editorial (Capítulos 1 a 3) | **Listo; no se construye** | `../lote_1_plan/PLAN_LOTE_1_CAPITULOS_1_A_3.md`. Detecta y evita una duplicación con la matriz de decisión ponderada de la Práctica 4 de Algorítmica 3.º en la sección 3.2. |

## Pruebas de esta ronda

**Entorno:** Ubuntu 24.04, PHP 8.3.6, SQLite 3.45.1. Salida completa en `B_prueba_tecnica/resultados_v2_2/salida_pruebas_linux.txt`.

| Prueba | Resultado |
|---|---|
| Reproducción del defecto con la v2.1 | Reinicio con código 0; préstamo de la otra conexión perdido |
| El mismo caso con la v2.2 | Reinicio con código 1; préstamo conservado |
| `prueba_mantenimiento.php` (nueva) | 30 de 30 |
| `prueba_respaldo.php` (adaptada) | 18 de 18 |
| `prueba_garantias.php` | 14 de 14 |
| `prueba_reglas.php` | 37 de 37 |
| `prueba_carrera.php` | 10 de 10 |
| `prueba_http.sh` | 32 de 32 |

**Hallazgo de proceso.** Copiar el archivo de la base con otro programa mientras está abierta suelta los bloqueos de SQLite en Linux. La prueba se corrigió y el `LEEME.txt` lo advierte.

## Decisiones editoriales recomendadas (pendientes de la aprobación formal de Fernando)

Se toman como base de planificación:
- permisos mínimos en el núcleo;
- 180 HC del programa;
- adaptación de 28 encuentros como opción;
- mapa de interesados en el Capítulo 1;
- reglas RN-01 a RN-06 como supuestos didácticos;
- plan de integración del Capítulo 2 conservado.

La identidad verde BTI sigue provisional.

## Binarios para la auditoría visual independiente

Enlaces de descarga directa fijados a su commit: el contenido no cambia aunque la rama avance. Se comprobó la descarga del primero: el SHA-256 coincide.

| Archivo (en `fase2_pilotos/`) | SHA-256 | Enlace |
|---|---|---|
| `A2_capitulo4_v2/ADS_3BTI_CAP4_v2_ESTUDIANTE.docx` | `52ddb6d8cc0f1f04b6e2a6a0988eb0176429e71e1eece7f4e30ab45d66c9a46a` | [descargar](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/47475d3b083e5955407ab81fa641c54f4bbc65dd/analisis_diseno_3_bti/fase2_pilotos/A2_capitulo4_v2/ADS_3BTI_CAP4_v2_ESTUDIANTE.docx) |
| `A2_capitulo4_v2/ADS_3BTI_CAP4_v2_ESTUDIANTE.pdf` | `68b566e8914031119c8bb75e1eae103db60af6a84fb080ae0e2bd43caffb3972` | [descargar](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/47475d3b083e5955407ab81fa641c54f4bbc65dd/analisis_diseno_3_bti/fase2_pilotos/A2_capitulo4_v2/ADS_3BTI_CAP4_v2_ESTUDIANTE.pdf) |
| `A2_capitulo4_v2/ADS_3BTI_CAP4_v2_GUIA_DOCENTE.docx` | `1031d3b3f57d8ed33d8107186acf024ba7a8c1ac163d6e94d3f7925c932c30c0` | [descargar](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/47475d3b083e5955407ab81fa641c54f4bbc65dd/analisis_diseno_3_bti/fase2_pilotos/A2_capitulo4_v2/ADS_3BTI_CAP4_v2_GUIA_DOCENTE.docx) |
| `A2_capitulo4_v2/ADS_3BTI_CAP4_v2_GUIA_DOCENTE.pdf` | `90aa78d66844055c186f4589e504005fe93f0f84ba44e0489fefc33ce2a82d36` | [descargar](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/47475d3b083e5955407ab81fa641c54f4bbc65dd/analisis_diseno_3_bti/fase2_pilotos/A2_capitulo4_v2/ADS_3BTI_CAP4_v2_GUIA_DOCENTE.pdf) |
| `A2_capitulo4_v2_1/ADS_3BTI_CAP4_v2_1_GUIA_DOCENTE.docx` | `e1217c93fc6de5426d8d37dadff0fdcdd0a8cf35ea5c03a97a5b2be7ddfc5786` | [descargar](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/d20a657b3c7fb70e1fb3b8f183a55e89155f8cc7/analisis_diseno_3_bti/fase2_pilotos/A2_capitulo4_v2_1/ADS_3BTI_CAP4_v2_1_GUIA_DOCENTE.docx) |
| `A2_capitulo4_v2_1/ADS_3BTI_CAP4_v2_1_GUIA_DOCENTE.pdf` | `fc3a210af4cc7c60bb1fa5a46a94cd7c2bc03fcbef6891825c967e083ea5b8b0` | [descargar](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/d20a657b3c7fb70e1fb3b8f183a55e89155f8cc7/analisis_diseno_3_bti/fase2_pilotos/A2_capitulo4_v2_1/ADS_3BTI_CAP4_v2_1_GUIA_DOCENTE.pdf) |
| `A1_candidato_capitulo2/ADS_3BTI_CANDIDATO_CAP2_v1_1_ESTUDIANTE.docx` | `410fcb5c07d63ff903b6d3096337441886fbca285d8995a86ec05629d9d6158c` | [descargar](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/47475d3b083e5955407ab81fa641c54f4bbc65dd/analisis_diseno_3_bti/fase2_pilotos/A1_candidato_capitulo2/ADS_3BTI_CANDIDATO_CAP2_v1_1_ESTUDIANTE.docx) |
| `A1_candidato_capitulo2/ADS_3BTI_CANDIDATO_CAP2_v1_1_GUIA_DOCENTE.docx` | `ba9447ead6e1619bca370ffb0e2cb030b9f91fb382d5e728e0244eef2db10515` | [descargar](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/47475d3b083e5955407ab81fa641c54f4bbc65dd/analisis_diseno_3_bti/fase2_pilotos/A1_candidato_capitulo2/ADS_3BTI_CANDIDATO_CAP2_v1_1_GUIA_DOCENTE.docx) |
## Sigue pendiente

- **Pruebas de campo:** Windows y equipos escolares, incluido el reinicio en Windows (`PRUEBAS_PENDIENTES_CAMPO.md`).
- **Auditoría visual independiente** de los DOCX y PDF, con los enlaces de arriba.
- **Autorización de Fernando:**
  - el lote 1 y sus cuatro decisiones de arranque;
  - la versión siguiente del Capítulo 4 con la especificación de C3.
