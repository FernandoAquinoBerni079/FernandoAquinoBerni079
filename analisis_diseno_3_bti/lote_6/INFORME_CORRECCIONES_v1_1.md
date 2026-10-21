# Lote 6 — correcciones de la versión 1.1

**Análisis y Diseño de Sistemas, 3.º BTI · 21 de octubre de 2026**

**Dictamen de partida:** «Apto con dos observaciones técnicas» sobre el commit `619056c` (v1.0).

**Qué se corrigió:** solo las dos observaciones. Los Capítulos 17 y 18, la Práctica 17 y sus cinco defectos, los instrumentos del H6, la defensa individual, la organización del cierre y la extensión no se reconstruyeron ni se ampliaron.

**Qué se conservó:**
- La v1.0 está intacta en `lote_6/version_1_0/`, con sus 44 archivos. El verificador los compara con su manifiesto SHA-256.
- Los lotes 1 a 5 y los planes no cambiaron. El verificador lo comprueba con git y con los manifiestos de los lotes 3, 4 y 5.
- El plan anual preliminar se volvió a generar y quedó igual, byte por byte.

## 1. Corrección 1 — Revisión segura del paquete de entrega

**El problema (v1.0).** El bloque C de `comprobar_entrega.php` ejecutaba los comandos que leía de `ENTREGA/LISTA_ENTREGA.md`. Además, el comprobador venía dentro del paquete que se estaba revisando. Así, un paquete ajeno podía hacer que se ejecutara su propio código para decidir si era confiable.

**Diseño nuevo.** El paquete ya no trae comprobador. El docente tiene dos herramientas propias, que no vienen en el paquete, en `lote_6/proyecto/herramientas/`.

| Parte | Herramienta | Qué hace | Qué no hace |
|---|---|---|---|
| Inspección estática | `inspeccionar_entrega.php` | Revisa los bloques A a F: comandos de la guía, archivos de la lista, pruebas declaradas, procedencia, mensajes y pantallas del manual, versiones. Informa comandos de forma desconocida, rutas que salen del paquete y enlaces simbólicos. | No ejecuta ni incluye nada del paquete. Lee `src/mensajes.php` como texto. |
| Ejecución de pruebas | `probar_en_aislamiento.php` | Corre solo su lista cerrada: `prueba_contratos`, `prueba_garantias` y `prueba_respaldo`. Arma cada comando como lista de argumentos y trabaja en una copia descartable que borra al terminar. Usa un entorno mínimo y un tiempo límite. | No ejecuta ningún texto del paquete ni usa la consola del sistema. No corre con una cuenta de administrador ni si el paquete tiene enlaces simbólicos. |
| Aislamiento | `herramientas/LEEME.md` | Procedimiento: primero la inspección. Después, las pruebas en un equipo aislado y sin red, con una cuenta estándar y una carpeta descartable. Se registra el resultado y se limpia. | — |

**Cómo corre el lote las herramientas.** Lo hace `build/herramientas_docente.py`, siguiendo el mismo procedimiento:
- el paquete se copia a una carpeta de la cuenta sin privilegios `nobody`;
- la herramienta corre con esa cuenta (`setpriv`) en un espacio de red aislado (`unshare -n`).

**La guía como prueba.** `build/prueba_guia.py` también quedó aislado:
- corre sin red y con la cuenta `nobody`;
- ya no usa la consola del sistema;
- solo ejecuta las formas `php <archivo>.php [argumentos]` y `php -S … -t …`; cualquier otra línea es un paso fallido que no se ejecuta.

**La regresión de la versión empaquetada** corre con la misma cuenta. Solo tiene la interfaz local, porque las pruebas HTTP la necesitan (`build/con_red_local.py`).

**Resultado con la Práctica 17.** La práctica y sus cinco defectos no cambiaron.

| Paquete | Inspección estática | Pruebas en aislamiento |
|---|---|---|
| Modelo | 0 incoherencias | 0 incoherencias |
| Mbokaja con defectos | 5: [A] DM-1, [B] DM-2, [D] DM-4 y [E] ×2 DM-5 | 1: [C] DM-3 |
| Mbokaja corregido con la clave | 0 | 0 |

Entre las dos herramientas se informan exactamente las 6 incoherencias esperadas. La clave (`caso/mbokaja_u6.py`) dice ahora qué herramienta informa cada una.

**Pruebas negativas nuevas** (`build/pruebas_negativas.py`): 10 de 10 correctas. Un «centinela» es un archivo que el contenido hostil intentaría crear; en ningún caso apareció.

| Caso | Qué se prueba | Resultado |
|---|---|---|
| N1 | Comando inyectado en la lista de entrega (`; touch …`) | Inspección: 2 × [C] «no está en la lista cerrada: no se ejecuta». Las pruebas corren solo la lista cerrada. |
| N2 | Líneas maliciosas en la guía (`touch`, `; touch`, `$(…)`) | Inspección: 3 comandos de forma desconocida. La guía como prueba rechaza los 3 pasos sin ejecutarlos. |
| N3 | `src/mensajes.php` con un efecto al incluirse | No se ejecutó: los mensajes se leen como texto. |
| N4 | Rutas que salen del paquete (`../`, absolutas) | [B] ×2 y [A]. |
| N5 | Enlace simbólico dentro del paquete | Inspección: [B]. Las pruebas en aislamiento se niegan (código 2, «No se ejecutó ninguna prueba»). |
| N6 | Pruebas con una cuenta de administrador | Se niegan antes de copiar nada. |
| N7 | Prueba de la lista que no termina | Se corta a los 2 s de límite. |
| N8 | El paquete recibido no cambia y la copia se borra | SHA-256 igual; no queda ninguna copia. |
| N9 | Prueba fuera de la lista cerrada | Se informa y no se ejecuta. |
| N10 | Una prueba de la lista intenta salir a la red y leer `/etc/shadow` | `red=NO admin=NO`. |

**Lo que se actualizó en los documentos.** Solo las instrucciones docentes y los pasajes afectados.

*Libro (Capítulo 17):*
- Práctica 17, nivel 1, punto 2.
- Párrafo de la sección 17.4: «un paquete recibido es código desconocido: no se ejecuta para decidir si es confiable».
- Tabla 17.4: el rótulo y la fila C.
- Tabla 17.6: inspección y pruebas en aislamiento, en filas separadas.
- Explicación de los Códigos 17.1 y 17.2.
- Hito H6: el texto y el punto 6 de la lista.

*Guía docente:*
- Secciones 0.1 y 0.4.
- Clave de la actividad 3 del Encuentro 34.
- Claves de la Práctica 17 por nivel: ahora 7 de 7 pasos.
- Tabla de la clave, con la herramienta de cada incoherencia.
- Resultados de las pruebas: incluyen las pruebas negativas.
- Condición de los resultados y procedencia de los recursos.

*Paquetes:*
- La guía de instalación tiene 7 pasos; se quitó el paso 8, «php comprobar_entrega.php».
- Se ajustaron `LEEME.txt`, la lista de entrega, el campo del acta y la ficha de procedencia.

*Fragmentos de código:*
- Códigos 17.1 y 17.2: los bloques D y A, leídos ahora de la inspección estática.
- R-8: el núcleo de las pruebas en aislamiento.
- R-9: el bloque C de la inspección.

**Retirado:** `lote_6/proyecto/comprobar_entrega.php` y sus copias en los paquetes. La versión anterior está en `version_1_0/proyecto/`.

## 2. Corrección 2 — Planilla de tiempos

**El problema (v1.0).** Los minutos que pasaban al Encuentro 36 eran los minutos que faltaban, no las defensas enteras que se trasladaban.

**Fórmula nueva:**
- minutos trasladados = defensas trasladadas × minutos por defensa;
- si las demostraciones solas superan el Encuentro 35, pasan además todas las defensas y los minutos de demostración que no entran, con un aviso.

Se aplicó en `caso/instrumentos_u6.py`, en la planilla y en el texto de la alternativa B.

**Ejemplo de control:** 6 equipos, 24 estudiantes, HC de 45, demostración de 12, cambio de 3, defensa de 6 y 5 recuperaciones de 15.
- Pasan 2 defensas: 12 minutos.
- Quedan **48 minutos** en el Encuentro 36 (no 51).
- La alternativa es la B.

**Validación de los datos:**
- Equipos, estudiantes y los minutos de la HC, la demostración y la defensa: enteros mayores que 0.
- Cambio y recuperaciones: enteros mayores o iguales que 0.
- Con datos inválidos, la función rechaza y la planilla no calcula (celda «¿Los datos son válidos?» y resultados «—»). No hay división por cero.
- Las celdas de entrada tienen validación de datos.

**Casos comprobados:** la planilla se recalculó con un evaluador independiente (pycel) y se comparó con la función. 11 de 11 casos correctos:
1. el ejemplo de control;
2. el límite A/B con diferencia 0;
3. el límite A/B con 1 minuto de falta;
4. el límite B/B+ con diferencia 0;
5. el límite B/B+ con 1 minuto de falta;
6. las demostraciones solas superan el Encuentro 35;
7. ceros permitidos;
8. 0 minutos por defensa (inválido);
9. estudiantes negativos (inválido);
10. HC de 0 minutos (inválido);
11. equipos con decimales (inválido).

**Lo que se volvió a generar:**
- `instrumentos/planilla_tiempos_encuentro_35.xlsx`; la de la v1.0 está en `version_1_0/instrumentos/`.
- La sección 0.6 de la guía: ejemplo, explicación de la fórmula y tabla de casos.

## 3. Controles repetidos

| Control | v1.0 | v1.1 |
|---|---|---|
| `build/reproducir.py` (pruebas de Mbokaja, guía, regresión) | 0 fallos | 0 fallos |
| `build/pruebas_negativas.py` | — | 10 de 10 |
| `build/planilla_tiempos.py` | 3 casos | 11 de 11 casos |
| `build/verificar.py` (con `ADS_V6` y `ADS_DR`) | 158 correctos, 0 fallos | 166 correctos, 0 fallos |
| `build/controles_finales.py` (impresión) | 21, 0 fallos | 22, 0 fallos |
| `build/prueba_fuentes.py` | 9, 0 fallos | 9, 0 fallos |
| `build/tomo.py` | 18 de 18 | 18 de 18 |
| Plan anual preliminar | 36 encuentros, 180 HC | sin cambios |
| Páginas: libro, guía y cuaderno | 20, 15 y 3 | 20, 15 y 3 |

Controles nuevos del verificador:
- ninguna herramienta ni comprobador dentro de los paquetes;
- la inspección no ejecuta ni incluye nada;
- la ejecución usa la lista cerrada, sin consola, con tiempo límite y negativa como administrador;
- el procedimiento de aislamiento está documentado;
- las pruebas negativas pasan y la guía como prueba corrió aislada;
- el ejemplo de control da 48 minutos y los datos inválidos se rechazan;
- la v1.0 está intacta.

Además, los controles de las herramientas y de la planilla se reescribieron.

**Entorno:** Linux 6.18.44-fc-v140 (x86_64), PHP 8.3.6, SQLite 3.45.1, en el contenedor de construcción, como root. Las herramientas bajan a la cuenta `nobody` con `setpriv` y cortan la red con `unshare -n`.

## 4. Lo que sigue pendiente

- Las herramientas y el procedimiento de aislamiento no se probaron en **Windows** ni en los **laboratorios escolares**. En Windows, la herramienta pide `--cuenta-sin-permisos-de-administrador` porque no puede comprobarlo sola, y el corte de red depende del procedimiento.
- También siguen pendientes la instalación por otro equipo (la hace el curso) y E-1 a E-12.
- El borrador de licencia sigue sin cerrar en lo jurídico.
- No se subió nada a Drive.
- No se declara aptitud comercial.
- Los datos DR y las variantes reservadas V6 siguen fuera del repositorio.

## 5. Diferencias frente a `619056c`

Fuera de `version_1_0/`, que es una copia nueva, cambiaron estos archivos de `lote_6/`.

**Corrección 1:**
- **Nuevos:**
  - `proyecto/herramientas/inspeccionar_entrega.php`, `probar_en_aislamiento.php` y `LEEME.md`;
  - `build/herramientas_docente.py`, `pruebas_negativas.py` y `con_red_local.py`.
- **Retirados:** `proyecto/comprobar_entrega.php` y sus copias en `paquete_entrega_modelo/` y `paquete_mbokaja/`.
- **Modificados:**
  - `caso/entrega_u6.py`, `caso/mbokaja_u6.py`;
  - `build/armar_paquetes.py`, `reproducir.py`, `prueba_guia.py`, `fragmentos_u6.py`, `cap17.py`, `guia_u6.py`;
  - de los dos paquetes: `LEEME.txt`, `ENTREGA/INSTALAR.md`, `LISTA_ENTREGA.md`, `ACTA_ENTREGA.md` y `PROCEDENCIA.md`.

**Corrección 2:**
- **Modificados:** `caso/instrumentos_u6.py` (también la rúbrica H6, por la Corrección 1), `build/planilla_tiempos.py` e `instrumentos/planilla_tiempos_encuentro_35.xlsx`.

**Comunes:**
- `build/verificar.py`;
- `build/piezas_u6.py`: versión «v1.1 (lote 6, cierre de auditoría)»;
- `build/manifiesto.py`.

**Regenerados:**
- los seis DOCX y PDF;
- `resultados_pruebas/`: los archivos `comprobador_*` se reemplazan por `inspeccion_*` y `aislamiento_*`, y se agrega `pruebas_negativas.txt`;
- `revision_visual/`;
- los JSON de control;
- `INFORME_LOTE_6.md`, solo en los puntos afectados;
- `MANIFIESTO_LOTE_6.json`.

La lista exacta sale de `git diff --stat 619056c -- analisis_diseno_3_bti/lote_6`.
