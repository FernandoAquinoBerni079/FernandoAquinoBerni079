# Lote 5 — Unidad V (Capítulos 14 a 16), versión 1.0

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · 21 de octubre de 2026**

**Estado:** lote para auditoría independiente. No está aprobado para la venta ni para uso en aula, y no está validado en laboratorios escolares. La aprobación para comercializar corresponde a Fernando y se hará sobre la colección completa.

**Límites respetados:**
- No se modificaron los lotes 1 a 4 ni el plan del lote 5. El verificador lo comprueba con git, con el commit de la v1.1 del lote 4 (`45bc5e9`) y con los manifiestos SHA-256 de los lotes 3 y 4.
- No se construyeron los Capítulos 17 y 18 ni la Unidad VI.
- No se generaron los 36 planes de clase.
- No se subió nada a Drive.
- Los datos reservados DR no están en el repositorio (sección 4).

**Próximo paso:** el lote se detiene acá para la auditoría independiente, antes de pasar a la Unidad VI.

## 1. Qué se entrega

| Documento | Páginas (oficio O3) | Estimación del plan |
|---|---|---|
| Libro del estudiante (`ADS_3BTI_LOTE5_ESTUDIANTE_OFICIO_O3`) | 30 | 32 a 40 |
| Guía docente con solucionario (`ADS_3BTI_LOTE5_GUIA_DOCENTE_OFICIO_O3`) | 18 | 16 a 22 |
| Cuaderno de prácticas (`ADS_3BTI_LOTE5_CUADERNO_PRACTICAS_OFICIO_O3`) | 4 | 6 a 10 |

Cada documento está en DOCX (el entregable) y en PDF (para control).

El libro y el cuaderno quedaron por debajo de la estimación, y no se rellenaron para alcanzarla (el plan lo dice así):
- el libro tiene tres capítulos, no cuatro como el lote 4;
- el cuaderno tiene solo dos prácticas, porque el Capítulo 16 no tiene práctica (decisión 5).

**Proyecto (`lote_5/proyecto/`):** todo trabaja sobre copias.
- `referencia_docente_v2/`: copia de la referencia del lote 4 con la corrección de IN-02 y su prueba nueva, `pruebas/prueba_in02.sh`.
- `referencia_docente_v2_sc02/`: la v2 más el cambio aprobado SC-02.
- `DIFERENCIAS_v2.md`: el diff de cada archivo que cambia en las dos copias.
- `cargador_dp/`: el cargador `cargar_dp.php`, el conjunto DP (`dp.json`) y la carga de la Práctica 14 (`mbokaja_p14.json`).
- `matriz/`: la ejecución de la matriz C-01 a C-20 (`ejecutar_matriz.php`) y la integración (`integracion.php`: permisos de la Tabla 11.3 y persistencia entre procesos).

**Otros archivos:**
- resultados de las pruebas con su entorno (`resultados_pruebas/`, 31 archivos y `resumen.json`);
- láminas de revisión (`revision_visual/`, 18);
- controles (`verificacion_resultado.json`, `CONTROLES_FINALES.json`, `prueba_fuentes_resultado.json`);
- este informe y `MANIFIESTO_LOTE_5.json`.

**Plan anual preliminar:** se regeneró con los indicadores leídos de las fichas de los Capítulos 14 a 16 (`lote_5/build/cap14.py` a `cap16.py`). Los pendientes pasan a ser los Capítulos 17 y 18.

**Índice del tomo:** `lote_5/build/tomo.py` agrega los Capítulos 14 a 16 al índice de la fuente editable. Comprueba que el Capítulo 16 tenga sus atributos de práctica vacíos, para que el tomo unificado no genere una «Práctica 16».

## 2. Cómo se aplicaron las seis decisiones

### Decisión 1. IN-02 como ejemplo central; IN-03 como mejora SC-02

**IN-02, en el Capítulo 16, recorre el ciclo completo de la Figura 16.1:**

- **Reproducción.**
  - `prueba_in02.sh` da 5 de 7 sobre la referencia del lote 4.
  - Falla justo en lo que dice el reporte: el tipo elegido y lo escrito se pierden.
- **Diagnóstico.**
  - Separa el síntoma, la causa y la capa (presentación: el patrón POST-redirección-GET no guardaba lo escrito).
  - La Tabla 16.1 muestra el impacto: `_plantilla.php` lo usan todas las pantallas.
- **Corrección mínima.**
  - Si la operación falló, se guarda también lo escrito, sin la ficha CSRF ni la contraseña.
  - El formulario lo muestra una sola vez y escapado.
  - Ninguna regla cambia.
- **Revisión entre pares:** la Tabla 16.2 tiene siete preguntas, cada una con su comprobación.
- **Regresión (Tabla 16.3).**
  - Pasan todas las pruebas del lote 4 y la prueba nueva.
  - La matriz da 20 de 20.

**IN-03 es el ejemplo complementario, como solicitud de mejora SC-02.**
- No se presenta como incumplimiento. Las tres frases del lote que usan «incumplimiento» lo niegan, y el verificador lo comprueba.
- La Tabla 16.4 tiene el formato de SC-01. Dice qué cambia cuando se aprueba:
  - el criterio de RF-09;
  - el contrato de OP-05 (v1.2);
  - la Tabla 8.6, con el mensaje nuevo ME-14;
  - la pantalla PT-09;
  - la prueba P-09.
- Las versiones v1.1 se conservan.
- La regresión de SC-02 está en la Tabla 16.5: contratos 93 de 93 y matriz 20 de 20, con C-19 esperando ME-14.

**El libro y la guía muestran partes distintas del código:**
- el libro trae solo los fragmentos necesarios (Códigos 16.1 a 16.3);
- la guía trae la solución completa (Referencias R-4 a R-7).

### Decisión 2. Cargador DP y conjunto reservado DR

**El cargador `cargar_dp.php`:**
- Valida el archivo de datos y rechaza un destino existente antes de copiar nada. Si se niega, termina con «No se cambió nada».
- Copia el código sin `datos/` y crea la base en una sola transacción.
- Comprueba el estado esperado e informa una huella SHA-256 reproducible. La huella es la misma desde la v2 y desde la base del estudiante del lote 4: `b9b9e76c…0769`.
- Marca la copia como descartable. Los programas de la matriz se niegan a correr sin esa marca.
- La base de la clase y las referencias no cambian.

**Carga manual:** una parte de DP se carga a mano con las operaciones del equipo (Tabla 14.4: OA-02, dos veces OA-01 y OA-03), y esa carga también se prueba.

**DR es exclusivo del docente y no está en el repositorio.**
- `lote_5/caso/dr_plantilla.py` tiene solo la estructura y un generador.
- El generador pide la semilla como argumento y no la guarda.
- Se niega a escribir dentro del repositorio y a sobrescribir un `dr.json`.
- Después de generar, comprueba los casos sobre una copia de la v2.
- La guía trae el procedimiento y la plantilla sin datos.
- El conjunto que generé para Fernando se entrega por separado (sección 4).

### Decisión 3. Referencia docente v2

- La referencia del lote 4 quedó intacta. El verificador lo comprueba con git contra `45bc5e9`.
- La corrección de IN-02 está en `referencia_docente_v2/` y el cambio SC-02, en `referencia_docente_v2_sc02/`, por separado.
- `DIFERENCIAS_v2.md` registra el diff de cada archivo:
  - en la v2 cambian 4 archivos;
  - en SC-02 cambian 5.
- El verificador comprueba que el informe de diferencias esté al día y que solo cambien esos archivos.

### Decisión 4. Sesiones de uso

- Son dos sesiones (S1 y S2), con compañeros en roles distintos: la bibliotecaria y la dirección.
  - Las tareas son nuevas.
  - Se registra lo que la persona hizo, la dificultad y el requisito (Tabla 15.3).
- Las del equipo modelo son una simulación del libro, rotulada como tal. Las del equipo son reales.
- El recuadro «Si participa alguien de la biblioteca real» fija las condiciones:
  - autorización institucional;
  - copia descartable con datos ficticios;
  - sin fotografiar ni grabar caras ni pantallas con datos personales;
  - sin anotar el nombre.
- El libro y la guía dicen que no es la revisión de bocetos del Capítulo 8.

### Decisión 5. Capítulo 16 sin práctica

- El H5 es la actividad integradora.
- Se conservan las 2 HC de evaluación del Encuentro 32.
- La rúbrica tiene seis criterios (C8 y C9) y cuatro niveles.
- La proporción 60/40 está rotulada como propuesta editorial.
- La ausencia de evidencia (AE) se registra aparte, y los pendientes del entorno no cuentan como falla.
- El banco V5 tiene cinco reportes de defecto nuevos para la evidencia individual.

### Decisión 6. Adaptación de 28 encuentros

- Los Encuentros 20 a 23 quedan sin cambios.
- El 24 reúne el 31 y el 32 («Sin encuentro de reserva para recuperación técnica.»).
- Se priorizan:
  - las condiciones mínimas;
  - los doce casos con seis límites o rechazos;
  - permisos, persistencia y restauración;
  - las dos sesiones;
  - la corrección de mayor prioridad con su regresión;
  - la defensa del H5.
- Pasan a lectura los ejemplos 14.1 y 15.2, los niveles 3, SC-02 y el Desafío. Cada cambio de alcance se anota en la bitácora del curso.
- **Recuperación técnica:**
  - Si un equipo no cumple una condición mínima, no se lo declara aprobado: se registra la recuperación y se le ofrece el procedimiento (guía, sección 4, con su planilla).
  - En todo el lote: «No se suponen horas extraordinarias de docentes ni de estudiantes que la institución no haya dispuesto».
  - **Corrección al plan:** el plan del lote 5 (`lote_5_plan/PLAN_LOTE_5_UNIDAD_V.md`, §2 y §8) proponía «recuperación específica fuera del horario» en el calendario de 28. La decisión 6 lo reemplazó. El plan no se modificó, porque está en el commit anterior, y el verificador comprueba que «fuera del horario» no aparezca en los documentos.

## 3. Requisitos de calidad

| Requisito | Cómo se cumple | Control |
|---|---|---|
| Títulos, secciones, capacidades y encuentros 27 a 32 de Work | Textuales, comparados con el informe de Work (`work.txt`); las evidencias de §5.2 en la apertura | Verificador, bloques A y B |
| 12 casos y 6 rechazos o límites por equipo | Consigna del Encuentro 27, punto de control, H5; la matriz modelo tiene 20 casos, 13 de límite o rechazo | Bloque M |
| Requisito, esperado, obtenido, entorno y evidencia en cada prueba | Matriz ejecutada (Tabla 14.6), con nota de entorno; el obtenido sale de la ejecución real | Bloques M y V |
| Comprobados, reproducidos, simulados y pendientes | Tabla 14.5; condición en cada fila y en la Tabla 14.9; sesiones del modelo rotuladas como simulación | Bloque N |
| Permisos, persistencia, restauración, trazabilidad y regresión | Ejecutados sobre copias: 32 de 32 permisos en el lote 4 y en la v2, persistencia entre procesos, restauración con copia previa, Tabla 16.6, regresión v2 y v2 con SC-02 | Bloques P y S |
| Lotes 1 a 4 intactos | git y manifiestos SHA-256 | Bloque Q |
| O3, fuente común y controles de tablas, figuras y código | Maqueta del lote 1, perfil O3 del lote 2 y piezas del lote 4 sin copias; 22 controles de impresión | Bloques G y H; `controles_finales.py` |
| DOCX y PDF, scripts, informe, manifiesto y láminas | Sección 1 | `MANIFIESTO_LOTE_5.json` |
| Plan anual desde las fichas 14 a 16 | `plan_anual_preliminar.py` las importa | Sus propios controles |

## 4. Datos reservados DR (fuera de GitHub)

- El repositorio es público. Por eso DR no está:
  - ni en el repositorio;
  - ni en la guía;
  - ni en el manifiesto;
  - ni en ningún resultado versionado.
- El verificador lo comprueba de tres maneras:
  - no hay ningún `dr.json` ni `comprobacion_dr.txt` en el repositorio;
  - el único archivo con la marca del conjunto es la plantilla;
  - el generador se niega a escribir adentro.
- Con la variable `ADS_DR` apuntando al archivo privado, el verificador comprueba además que ninguno de sus 22 códigos aparezca en el repositorio ni en los documentos, sin imprimirlos.
- Generé un conjunto DR con una semilla al azar que no se imprimió ni se guardó. Está fuera del repositorio, en `/home/user/ADS_LOTE5_RESERVADO_DOCENTE/`:
  - `dr.json`;
  - `comprobacion_dr.txt`: carga correcta, 8 de 8 casos sobre la v2.
- Se entrega a Fernando por separado, como archivo aparte de este envío. Si prefiere generar el suyo, el procedimiento está en la guía, sección 0.2.
- **Límite conocido de la plantilla:** la estructura de los casos (qué reglas se prueban) es pública. Los datos (códigos, títulos, cursos y fechas) no lo son. La guía recomienda agregar en la copia privada uno o dos casos propios que no estén en la plantilla.

## 5. Qué es real, qué es simulado y qué queda pendiente

**Comprobado en el entorno de construcción.**
- Entorno: Linux 6.18.44-fc-v140 x86_64, PHP 8.3.6, SQLite 3.45.1 (contenedor). No es una computadora escolar ni Windows.
- Resultados de la última ejecución de `build/reproducir.py`:

  | Prueba | Resultado |
  |---|---|
  | Cargador | estado esperado y misma huella desde la v2 y la base del estudiante; se niega a sobrescribir |
  | Matriz C-01 a C-20, lote 4 | 19 de 20 (C-20 es IN-02) |
  | Matriz, v2 | 20 de 20 |
  | Matriz, v2 con SC-02 | 20 de 20 |
  | Práctica 14 | 6 de 6 |
  | `prueba_in02.sh`, lote 4 | 5 de 7 |
  | `prueba_in02.sh`, v2 | 7 de 7 |
  | Regresión v2 | contratos 90/90, operaciones 17/17, carrera 15/15, garantías 20/20, respaldo 20/20, mantenimiento 30/30, marca 19/19, HTTP 32/32 |
  | Regresión SC-02 | contratos 93/93 y el resto igual |
  | Integración, lote 4 y v2 | permisos 32/32, persistencia y restauración correctas |

**Reproducido.**
- **IN-02:** es un defecto real y se corrigió.
- **IN-01 bis:** «La fecha  no es válida», con un espacio doble. Queda como límite conocido.
- **IN-03:** el comportamiento se reprodujo y cumple el contrato. Por eso se trata como mejora.

**Simulado.**
- Las sesiones de uso del equipo modelo.
- Los datos de Mbokaja.
- IN-01 tal como estaba escrita: no se reproduce, porque el mensaje sí da el formato.

**Pendiente.**
- La prueba de campo en las computadoras del colegio y en Windows: E-1 a E-12, P-13 y concurrencia.
- La instalación por otro equipo (Capítulo 17).

## 6. Controles

| Control | Resultado |
|---|---|
| `build/verificar.py` (con `ADS_DR`) | 219 correctos, 0 fallos (217 sin la variable: no corre los 2 controles privados) |
| `build/controles_finales.py` | 22 controles, 0 fallos (filas de tablas, párrafos, palabras, figuras, índice, márgenes espejados, cortes de tabla, bloques de código del libro y de la guía) |
| `build/prueba_fuentes.py` | 9 combinaciones (Carlito, Liberation Sans, DejaVu Sans × 3 documentos), 0 fallos |
| `build/tomo.py` | Capítulos 1 a 16 con sus atributos; pendientes 17 y 18 |
| `plan_anual/plan_anual_preliminar.py` | Controles correctos; 36 encuentros, 180 HC |

**Cómo reproducir todo**, desde `analisis_diseno_3_bti/`:

```
python3 -B lote_5/build/reproducir.py      # pruebas reales sobre copias temporales (unos 3 minutos)
python3 -B lote_5/build/diferencias.py
python3 -B lote_5/build/construir.py
ADS_DR=<ruta privada>/dr.json python3 -B lote_5/build/verificar.py
python3 -B lote_5/build/controles_finales.py
python3 -B lote_5/build/prueba_fuentes.py
```

## 7. Para la auditoría

Te sugiero revisar estos puntos:
1. Si el ritmo del Encuentro 30 entra en 5 HC: dos sesiones de uso, la revisión cruzada con DR y el acta. La guía lo reparte en 2 + 2 + 1 HC.
2. Si la extensión del libro (30 págs.) y la del cuaderno (4 págs.) alcanzan, o si conviene ampliar alguna sección. No se amplió para llegar a la estimación.
3. Si la estructura pública de los casos de DR es aceptable, con la recomendación de agregar casos privados.
4. Si los límites conocidos de la versión candidata (Tabla 16.8) son los que corresponde declarar. Entre ellos está que los otros formularios de PT-08 todavía no conservan lo escrito.
