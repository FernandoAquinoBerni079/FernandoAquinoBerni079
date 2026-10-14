# Historia y Geografía 7.º — Tercera muestra (corrección de la segunda)

**Estado: muestra correctiva en revisión. No es una versión comercial ni se declara apta.** Claude edita, ChatGPT audita y Fernando aprueba.

- **Origen:** commit congelado `31c8d406aad9992f9f03ebc67d13d4e53fc58401` (carpeta `03_muestra2/`, que no se modificó).
- **Dictamen de origen:** NO APTO, según el *Informe de auditoría independiente — segunda muestra* (Drive, carpeta `AUDITORIA_INDEPENDIENTE_MUESTRA2_31c8d406_2026-10-14`, archivo `INFORME_AUDITORIA_INDEPENDIENTE_MUESTRA2.md`, 14/10/2026). Ese informe tiene 20 hallazgos: 10 mayores y 10 menores.
- **Alcance:** solo el material auditado.
  - Clase 10, Clase 18, Ficha 18-A, Continuación F con sus fichas, y Evaluación de la Unidad 5.
  - Planes 15, 28, 29 y 30.
  - Solucionario, matriz curricular, plan anual y datos de trazabilidad.
  - No se reconstruyó el libro ni se empezaron los 36 encuentros.
- **Maestro:** `TOMO_OCTUBRE_MAESTRO.docx` del 03/10/2026 (SHA-256 `8dbc4f44…179413`), solo leído. Ya no se usa ninguna ilustración suya en la muestra.
- **Programa:** reproducción del *Programa de Estudio: Historia y Geografía, 7.º grado, EEB* (MEC, 2014), SHA-256 `389190d3…c8d27e`. Capacidades en las págs. 55 a 57; horas cátedra de 40 minutos en la pág. 46.

## 1. Entregables

| Documento | DOCX | PDF | Págs. |
|---|---|---|---:|
| Tomo de la muestra (oficio, variante B) | `tomo/TOMO_MUESTRA3_oficio.docx` | `tomo/TOMO_MUESTRA3_oficio.pdf` | 24 |
| Planes de clase 15, 28, 29 y 30 (A4) | `planes/PLANES_MUESTRA3_A4.docx` | `planes/PLANES_MUESTRA3_A4.pdf` | 10 |
| Solucionario docente (A4) | `solucionario/SOLUCIONARIO_MUESTRA3_A4.docx` | `solucionario/SOLUCIONARIO_MUESTRA3_A4.pdf` | 5 |
| Matriz curricular de los 36 encuentros (A4 horizontal) | `matriz/MATRIZ_CURRICULAR_36_ENCUENTROS_M3.docx` | `matriz/MATRIZ_CURRICULAR_36_ENCUENTROS_M3.pdf` | 8 |
| Plan anual (oficio horizontal) | `plan_anual/PLAN_ANUAL_OFICIO_M3.docx` | `plan_anual/PLAN_ANUAL_OFICIO_M3.pdf` | 9 |
| Trazabilidad curricular (reemplaza al cotejo de la muestra 2) | `datos/trazabilidad_curricular.json` | — | — |
| Resultados de los controles automáticos | `datos/controles_muestra3.json` | — | — |
| Copias livianas para revisión | — | `revision_liviana/*_REVISION.pdf` | — |

Solo se regeneraron los documentos afectados por los hallazgos.

Para reconstruir todo:

```
python3 scripts/construir_muestra3.py MAESTRO.docx GEOJSON SALIDA PLAN_ANUAL_ORIGINAL.docx
```

La carpeta SALIDA debe contener antes `cotejo_capacidades.json` y `estructura_maestro.json` de `03_muestra2/datos/`. Esos archivos se leen y no se modifican.

Para verificar:

```
python3 scripts/verificar_muestra3.py ../03_muestra2/datos/programa_MEC_2014_HyG7_texto_extraido.txt .
```

## 2. Resolución de los 20 hallazgos

Los códigos y la gravedad son los del informe de auditoría. «Resuelto» quiere decir que la corrección está hecha y documentada; la verificación independiente sigue a cargo del auditor. Las páginas citadas son las de los PDF de esta muestra.

### 2.1 Mayores

| Código | Hallazgo (resumen) | Estado | Qué se cambió y evidencia |
|---|---|---|---|
| A01 | La Figura 10.1 del maestro presenta la encomienda como institución de gobierno. | Resuelto | Se retiró la imagen del maestro. La nueva Figura 10.1 es una línea de tiempo propia (1534-1556), en la pág. 5 del tomo. La Figura 10.2 es un esquema de autoridades que aclara en el epígrafe: «La encomienda no era una institución de gobierno» (pág. 6). Control 8: ninguna figura del tomo viene del maestro. |
| A02 | Plan 15: tramo final sobrecargado; corrección de todo en 10 minutos. | Resuelto (falta probarlo en aula) | Actividades en clase:<br>• Esenciales: fuente, Ubicate y actividades 1, 2, 3, 4, 7, 13 y 15.<br>• Consolidación: 5, 8, 9 y 10.<br>• Domiciliarias: 6, 11, 12, 14, 16 y autoevaluación.<br>Cada bloque cierra con comprobación por parejas; el tramo 100-112 retoma solo los errores frecuentes. Se agregó el planisferio a los materiales (para la distancia con España). Tramos contiguos de 0 a 120 (controles 3, 4 y 5). Planes, págs. 3-4. |
| A03 | Plan 28: trabajo cartográfico sin tiempo suficiente. | Resuelto (falta probarlo en aula) | Distribución que propuso la auditoría (§6.2):<br>• El mapa tiene 25 minutos (25-50): el docente modela el primer paso y la revisión se hace dentro del bloque.<br>• La fuente americana tiene 20 minutos (70-90).<br>• Las fichas y los lápices se preparan antes del encuentro.<br>• Las actividades 2, 4, 6 y 9 pasan a consolidación.<br>Planes, págs. 5-6. |
| A04 | El JSON asigna H1 a las evaluaciones y G1 a la Continuación E. | Resuelto | Nuevo `datos/trazabilidad_curricular.json`. El de la muestra 2 queda congelado.<br>• Evaluaciones: «sin ficha» y «asociación curricular».<br>• Continuación E: «ampliación editorial», sin capacidad MEC asignada.<br>• Se separa el estado de la ficha del maestro del vínculo propuesto.<br>Conteo: 16 literales, 5 truncadas, 1 abreviada (Clase 19), 6 editoriales o variantes, 8 sin ficha (control 9). |
| A05 | Plan anual: Guerra Guaranítica «por requerimiento curricular» y «por priorización MEC». | Resuelto | Esas frases se eliminaron (control 9).<br>• Encabezado del plan anual: el programa abarca los siglos XVI y XVII; la Guerra Guaranítica es una ampliación editorial optativa.<br>• Banda de la Unidad 4 y fila 22: dicen lo mismo.<br>• Matriz: fila 22 «Ampliación editorial», con núcleo recomendado bandeirantes, Guairá y Mbororé (H5). |
| A07 | Consigna 4 de la Continuación F: la rúbrica califica cosas que la consigna no pide; no está claro qué producto se califica. | Resuelto | La consigna 4 (tomo, pág. 18) dice ahora que se califica solo la decisión de la Ficha F-C y transcribe los cuatro criterios con su puntaje.<br>El Plan 29 los lee en voz alta antes del taller (tramo 40-50).<br>El solucionario agrega un ejemplo completo y niveles 0/1/2 para cada criterio. Control 6: el criterio impreso y el del solucionario coinciden. |
| A08 | Parte F de la evaluación: el criterio «relieve con otro factor» no estaba en la consigna. | Resuelto | La consigna 14 enumera los cinco criterios, entre ellos «el relieve junto con otro factor» (tomo, pág. 24).<br>El solucionario da una respuesta modelo con un factor adicional desarrollado y un dato de cada clase, y explica el puntaje parcial. |
| A10 | Plan 30: la corrección pública empieza mientras un estudiante sigue con tiempo adicional. | Resuelto | Nueva secuencia:<br>• 0-10 encuadre.<br>• 10-80 prueba.<br>• 80-95 tiempo adicional supervisado; los demás pasan a una actividad sin claves.<br>• 95-120 reflexión escrita, sin corregir ni comentar respuestas.<br>La devolución con claves pasa a los primeros 20 minutos del encuentro 31, cuando todos terminaron. Control 10. Diferencia con la propuesta de la auditoría (devolver en el mismo encuentro): así quien necesite más de 15 minutos puede terminar al inicio del encuentro 31 sin haber oído claves. El Plan 31, fuera de esta muestra, debe reservar ese tiempo. |
| A18 | La matriz dice «literal» para la Evaluación de la Unidad 5, que no imprime ficha. | Resuelto | La fila 30 de la matriz dice ahora: «evaluación asociada a G1 y G2; las capacidades se explicitan en el Plan 30; sin ficha literal en el tomo». En el JSON, tipo «asociación curricular». |
| A20 | La integradora de la 2.ª etapa aparece con coberturas distintas. | Resuelto | Matriz, plan anual (fila 36) y JSON dicen lo mismo: H5, H6, G1, G2, G3 y G4 (Unidades 4 a 6). Se advierte que el ítem 3 del maestro evalúa la ampliación editorial y debe reemplazarse o quedar optativo. La integradora 1.ª figura como H1 a H4 (control 9). |

### 2.2 Menores

| Código | Hallazgo (resumen) | Estado | Qué se cambió y evidencia |
|---|---|---|---|
| A06 | Las bandas «Capacidades» del plan anual son síntesis editoriales. | Resuelto | Cada banda cita «Capacidad Hn/Gn (MEC 2014, literal)» con el texto completo; la Clase 1 se identifica como formulación editorial. El control 1 compara cada banda con el programa. |
| A09 | La clave cartográfica no fija tolerancias ni puntajes parciales. | Resuelto | Tolerancias para Asunción, Itaipú y Yacyretá; parciales de 0,5 por elemento ubicado y no nombrado, y por dos de los tres países; la vertiente suma 0,5 aunque falte el nombre. Se agregó un mapa de referencia para corregir (solucionario, pág. 5). |
| A11 | Los planes mencionan apoyos que no se entregan. | Resuelto | Plan 28: texto del banco de nombres para la Ficha 18-A.<br>Plan 15: las dos opciones de cada pregunta de la fuente.<br>Plan 29: las dos preguntas guía ya vienen impresas en las tarjetas de la Ficha F-B. |
| A12 | La figura de la Hidrovía del maestro tiene rótulos ilegibles y calados sin fecha. | Resuelto | Se reemplazó por un mapa propio con fuente (Figura 18.2, tomo pág. 12). La Continuación F remite a esa figura en lugar de repetirla. |
| A13 | El mapa de la Parte D tiene un número 4 que no se pregunta. | Resuelto | El mapa tiene solo los números 1 a 3. El control 7 compara el solucionario con `RIOS_NUMERADOS` de `figuras.py`, pero no lee la imagen: la revisión visual lo confirma (tomo, pág. 23). |
| A14 | Hojas con blanco sin función. | Resuelto en lo señalado | • Tomo: la actividad 16 ahora va con una autoevaluación de la clase (pág. 9).<br>• F-A: lleva renglones de notas.<br>• F-B: tarjetas recortables con zonas de escritura.<br>• Solucionario: se lee de corrido.<br>• Queda una hoja corta al final del Plan 30 (46 %), que es cierre de plan.<br>Control 11: ninguna hoja interior por debajo del 55 % y ninguna hoja final por debajo del 25 %. |
| A15 | Bandas de momento que quedan solas al pie; tabla de evaluación partida. | Resuelto | Cada banda de momento va unida a su primera fila, y la tabla de evaluación no se parte (`planes_m3.py`). Comprobado en el render. |
| A16 | No se dice dónde registrar los productos. | Resuelto | La fila nueva del cuadro de 1537 y las preguntas de las tres dimensiones van al cuaderno. F-B tiene columnas para lo que gana, lo que arriesga y el argumento; F-A tiene notas. |
| A17 | Mapas sin leyenda suficiente, rótulos sobre las líneas, Apa sin identificar, escala ambigua. | Resuelto en parte | Hecho:<br>• Leyenda.<br>• Límites internacionales en trazo discontinuo, legibles en copia monocroma.<br>• Escala gráfica aproximada.<br>• Nota de resolución de los datos («nivel de detalle 1:50 millones») separada de la escala.<br>• Halos blancos en los rótulos de ríos.<br>• Desembocadura del Apa marcada.<br>Pendiente: el curso del Apa no se dibuja porque Natural Earth no lo tiene, y falta cotejar con un atlas nacional. |
| A19 | Referencias documentales incompletas de la Real Provisión. | Resuelto en parte | Rivarola Paoli queda citado con la reproducción de portalguarani.com, la que leyó la auditoría.<br>La transcripción del portal del MEC no se pudo localizar: mec.gov.py no es accesible desde el entorno de edición, y una búsqueda web no la encontró. El tomo lo declara («enlace estable pendiente de verificación editorial»).<br>No se afirma cotejo paleográfico. Se corrigieron dos precisiones que señaló la auditoría (§8): Irala «reconocido como gobernador» en 1539, y «primer obispo nombrado» frente a «primero que llegó» (1556). |

### 2.3 Correspondencia con la reauditoría de ChatGPT (H7-M2)

| ChatGPT | Hallazgos A que lo cubren |
|---|---|
| H7-M2-01 Tiempo adicional y claves | A10 |
| H7-M2-02 Marcador 4 | A13 |
| H7-M2-03 Figura 10.1 | A01 |
| H7-M2-04 Tiempos de los Planes 15 y 28 | A02, A03 |
| H7-M2-05 Espacios residuales | A14, A15 |
| H7-M2-06 Cartografía | A12, A17 |
| H7-M2-07 Fuentes | A19 |
| H7-M2-08 Programa y capacidades del plan anual | A05, A06 |
| H7-M2-09 Ficha 18-A y autocorrección | A10 (la evaluación ya trae su mapa); autocorrección solo en el encuentro 31 |

## 3. Comparación entre la muestra 2 y la muestra 3

| Aspecto | Muestra 2 (31c8d40, congelada) | Muestra 3 |
|---|---|---|
| Figuras heredadas del maestro | 10.1 (errónea) y la de la Hidrovía | Ninguna; todas propias, con fuente |
| Numeración de figuras de la Clase 18 | 18.2 aparecía antes que 18.1 | Consecutiva en orden de lectura (control 8) |
| Plan 15 | Ocho ítems en 95-105; corrección total en 10 minutos | Actividades separadas por función; comprobación en cada bloque; cierre solo con errores frecuentes |
| Plan 28 | 20 minutos para lectura y ficha | 25 minutos de mapa con modelado y revisión; 20 minutos de fuente |
| Plan 29 | Dos lugares para escribir la decisión; rúbrica no comunicada | Una sola decisión calificada (Ficha F-C); criterios leídos antes del taller |
| Plan 30 | Corrección pública a los 80 minutos, con tiempo adicional en curso | Sin claves hasta el encuentro 31; tiempo adicional supervisado |
| Funciones de las actividades en los planes | No se distinguían | Esenciales, consolidación y complementarias o domiciliarias (control 4) |
| Vínculo curricular en los planes | No explícito | «Tipo de vínculo curricular» en cada plan |
| Criterios de corrección | El solucionario agregaba criterios que el tomo no anunciaba (A07, A08) | El solucionario repite los criterios impresos y agrega niveles y modelos (control 6) |
| Evaluación de la Unidad 5 | Dependía de la Ficha 18-A; mapa con un 4 sobrante | Trae sus dos mapas; números 1 a 3 |
| Trazabilidad (JSON) | H1 en ocho evaluaciones; G1 en la Continuación E | «Sin ficha» y «asociación curricular»; E como ampliación editorial |
| Matriz | Integradora 2.ª: G1-G4; Unidad 5 «literal» | Integradora 2.ª: H5, H6, G1-G4; Unidad 5 asociada a G1/G2; columna de tipo de vínculo |
| Plan anual | «Por priorización MEC» y «por requerimiento curricular»; capacidades resumidas | Capacidades literales con código; Guerra Guaranítica como ampliación optativa |
| Páginas: tomo / planes / solucionario / matriz / plan anual | 26 / 10 / 5 / 7 / 8 | 24 / 10 / 5 / 8 / 9 |
| Controles automáticos | 24 correctos, 0 fallos (no detectaban A07, A08 ni A13) | 185 correctos, 0 fallos (§4) |

## 4. Controles automáticos

Se corren con `scripts/verificar_muestra3.py`; el resultado completo está en `datos/controles_muestra3.json`.

| Control | Correctos | Fallos |
|---|---:|---:|
| 1. Capacidades literales: fichas, planes y bandas del plan anual contra el texto del programa | 10 | 0 |
| 2. Coherencia tomo ↔ solucionario (todos los ítems con respuesta, sin sobrantes) | 4 | 0 |
| 3. Coherencia tomo ↔ planes (todas las actividades asignadas y existentes) | 4 | 0 |
| 4. Función de cada actividad (una sola categoría de las tres pedidas) | 6 | 0 |
| 5. Duración de las secuencias (contiguas, de 0 a 120) | 4 | 0 |
| 6. Transparencia de rúbricas (criterio impreso = criterio del solucionario; sin rúbricas no anunciadas; los puntajes suman 28) | 62 | 0 |
| 7. Exactitud de respuestas (clave = opción impresa; claves balanceadas a5 b5 c5 d3; Parte D = ríos numerados) | 20 | 0 |
| 8. Figuras (numeración consecutiva; citas existentes; ninguna figura del maestro) | 18 | 0 |
| 9. Trazabilidad entre JSON, matriz y plan anual | 21 | 0 |
| 10. Evaluación equitativa (sin claves antes del encuentro 31; la prueba trae sus dos mapas) | 2 | 0 |
| 11. Integridad visual de las páginas modificadas (hojas con poco contenido) | 34 | 0 |
| **Total** | **185** | **0** |

Para comprobar que el verificador detecta errores, se introdujeron a propósito cinco fallas. Las cinco se detectaron:

- un criterio de rúbrica cambiado en el solucionario;
- un tramo del Plan 15 que termina en 125;
- una cita a una Figura 18.4 que no existe;
- una actividad asignada a dos funciones;
- una clave de opción múltiple equivocada.

Durante la construcción, el control 11 detectó dos veces una hoja residual (la firma del Plan 15 sola en una hoja). Se corrigió acortando el texto, sin quitar contenido de la clase.

Además se revisaron visualmente todas las páginas de los cinco PDF.

Lo que estos controles no prueban:

- la exactitud histórica o geográfica fuera de lo que se coteja;
- los tiempos reales en el aula;
- la legibilidad en una fotocopia física;
- el contenido de las imágenes (solo se revisó a ojo).

## 5. Pendiente de verificación independiente

1. **Transcripción del portal del MEC** (segundo fragmento de la Real Provisión): falta un enlace estable y la fecha de consulta. Si no se localiza, conviene tomar los dos fragmentos de la reproducción de Rivarola Paoli.
2. **Atlas nacional** (IGM o equivalente): falta cotejar afluentes, el curso del Apa, los lagos Ypacaraí e Ypoá y las posiciones de ciudades y represas, que en los mapas son aproximadas.
3. **Fechas institucionales sin localizador:** Audiencia de Charcas (1559) y la llegada de Alonso Cabrera (1538). La lista está en `VERIFICACION` dentro de `scripts/contenido_tomo.py`.
4. **Tiempos de los Planes 15 y 28:** responden a la distribución que propuso la auditoría, pero no se probaron en aula.
5. **Plan 31**, fuera de la muestra: tiene que reservar los 20 minutos de devolución de la Evaluación de la Unidad 5.
6. **Continuación E:** se mantiene en el maestro como ampliación optativa. Queda para decisión de Fernando si el encuentro 22 pasa a tener como núcleo bandeirantes, Guairá y Mbororé.
7. **Programa MEC:** sigue cotejado contra una reproducción, no contra el ejemplar oficial.
8. **Plan de la editorial Book Sellers:** sigue pendiente su cotejo con el programa 2014.

## 6. Preservación

- `03_muestra2/` y el commit `31c8d40` quedan intactos.
- No se modificaron archivos maestros, versiones comerciales ni carpetas comerciales de Drive.
- `04_muestra3/scripts/` copia y adapta los scripts de la muestra 2. Además reutiliza, sin modificarlos:
  - `02_piloto/scripts/tomo_piloto.py`;
  - `02_piloto/scripts/planes_piloto.py`;
  - `03_muestra2/scripts/plan_anual_oficio_v2.py`.

**No se inicia otra ronda de correcciones sin autorización expresa.**

## 7. SHA-256 de los archivos de esta carpeta

| Archivo | SHA-256 |
|---|---|
| `datos/controles_muestra3.json` | `0b67431937938cfcebdcabb7676af282dc29401762e83d9ffbe9c2ea32610835` |
| `datos/paginas_tomo.json` | `f7ac66af51b77e0a5bdc8b4a54794a0753958009da7c57d788efd4b79cf22b23` |
| `datos/trazabilidad_curricular.json` | `e76aceec79bc0da76e6195335a256280f874e3e44d4801cc404087ccb7d5fac9` |
| `figuras/eval_u5_rios_numerados.png` | `9bd938cd6dff00453f9378f69af8e2a33f6855eca1cc3d3f786147d3c49802a2` |
| `figuras/ficha_18A_mapa_mudo.png` | `0d3428b40dcf92e55d7526ba799dac4cc261031281c082e7e555a83a08cd021b` |
| `figuras/fig_10_2_autoridades.png` | `a5884ac1f7c63f2f5e2b49c9ca1eda580a94160d3cfb25950dc459ffe034a96f` |
| `figuras/fig_10_3_linea_tiempo.png` | `25a0d67718799a19ddfa5a378f6faf62e59fab4271046d3f730277e854d81ce9` |
| `figuras/fig_18_2_rios_paraguay.png` | `8ec41e3160d58b27b2efb40cd85f8351310fb0df0021209d26902efb267be71f` |
| `figuras/fig_18_3_rios_america.png` | `d1ab48edd67168f56c3ff270ecfbb3195dc0cfad5499393dac65d3fc4f062127` |
| `figuras/fig_F1_hidrovia.png` | `487ba24379e1a616cd2f35c8f70a1a4cd867dae83dab7c81004fd39f3362edd9` |
| `matriz/MATRIZ_CURRICULAR_36_ENCUENTROS_M3.docx` | `1881925e610c1d130839dcc2fead77f8c6d8338545eaa9ab5834e9276701399b` |
| `matriz/MATRIZ_CURRICULAR_36_ENCUENTROS_M3.pdf` | `9be8fdf0a2651e9eea32e0a982b68379f10fd25d401d084b6b497e0216c2a2a3` |
| `plan_anual/PLAN_ANUAL_OFICIO_M3.docx` | `ea365237b126aacaeceaaf2cb22d6de8e694be3d88be2b4f7daaa25436007037` |
| `plan_anual/PLAN_ANUAL_OFICIO_M3.pdf` | `b13a87022eac4bd93d1d6d4fb896e603ec57cf85cd2a71f949b8756f7e0e3979` |
| `planes/PLANES_MUESTRA3_A4.docx` | `16ff13cefcd634201b8c4b8454e04dbac005818098f8984e2b43af17c5600a73` |
| `planes/PLANES_MUESTRA3_A4.pdf` | `7b87b6639b26bf3617d3fff240cd8cb4a831e162f0f2fed332d40b59f2d0603d` |
| `revision_liviana/MATRIZ_CURRICULAR_36_ENCUENTROS_M3_REVISION.pdf` | `57f3fcbc71689b594f2264fe59fa8801b9e7d2ae245adaec0f68ab662a5e2608` |
| `revision_liviana/PLANES_MUESTRA3_A4_REVISION.pdf` | `5a368d8221bb092fe1e12bbf26a5a55a6e13bdc31c024bef82ab2d726059f148` |
| `revision_liviana/PLAN_ANUAL_OFICIO_M3_REVISION.pdf` | `07aeb65e04b14d9bfff813d388f1563047d6b1786f6eb8ef30e6c0fa5788f37e` |
| `revision_liviana/SOLUCIONARIO_MUESTRA3_A4_REVISION.pdf` | `dc45b5d47d26db5c7f92a5885f91dcbd8f22898d0f595c2e110213cfc3376be5` |
| `revision_liviana/TOMO_MUESTRA3_oficio_REVISION.pdf` | `261607adf7f50b9c628ea39f464a4d82e286d9963578162ca511b4977c12eb5e` |
| `scripts/construir_muestra3.py` | `aee480922c5cd4be4ac16fa362526351a2756ae44ada327e293afa361c008b21` |
| `scripts/construir_tomo_m3.py` | `79d8e588d075563a9ccb5858346c58c8f8e7ba9140682dbaa33170a1e2d9a159` |
| `scripts/contenido_matriz.py` | `229e93c0ef4ed4c7299309aa4096e8324add82625e1bde9a36acca32f6f87dc5` |
| `scripts/contenido_planes.py` | `364c871317f7489bc5f16133cc121cf9e5cc12b2442f99192d68c1ced99b5169` |
| `scripts/contenido_solucionario.py` | `4cdb206ed2c50a10f239d2efeb6964aa2535b2657beb3a7a9e0b71d908bf0f5f` |
| `scripts/contenido_tomo.py` | `5ec2906d07f67549acb4a613adf12d53419e3d068ce007b39f7c73d5d014196f` |
| `scripts/figuras.py` | `6c8b8357c89a80582682f063ca05dc5252341c4c0fdff143a7f5b9af9fdd680a` |
| `scripts/plan_anual_oficio_v3.py` | `f9a7a1b7ddacade72395c6093fbdb7c31b5a95869ea84c4fed66e2c6e8cf5224` |
| `scripts/planes_m3.py` | `543bcc1f7df64ecc64e142340d164e0e976112387a3cb161db507b322accd3b7` |
| `scripts/verificar_muestra3.py` | `e3db6a70dab4ffae9cbc09d98c36bf7548c020b76c0cb41c98fa2af2aaf09ad2` |
| `solucionario/SOLUCIONARIO_MUESTRA3_A4.docx` | `3cbb29e34fab2ea92c84ed07f3df273b332a96fb374fdd879448d18906e8fde6` |
| `solucionario/SOLUCIONARIO_MUESTRA3_A4.pdf` | `f08507a633b7417f3c540f9e7884835f97a47e136bafa18b2b141c30811de015` |
| `tomo/TOMO_MUESTRA3_oficio.docx` | `8218a8368cc9c244d9a61e35deeccf43c6a8faebb48ace0c4a382f8b8e1477dd` |
| `tomo/TOMO_MUESTRA3_oficio.pdf` | `167b5f2a3e33e48aefead7801b220f367ab587f59d942358adc7805c5ccb5986` |
