# Informe técnico de control — Bloque I (encuentros 1 a 9)

**Estado: desarrollado, verificado automáticamente e inspeccionado visualmente. Pendiente de auditoría.** No es versión comercial. Modelo: muestra 3, commit `841f5bc9`.

## 1. Contenido del bloque

| N.º | Sección | Capacidad (vínculo) | Tomo, págs. |
|---:|---|---|---|
| 1 | Clase 1 — La Historia y la Geografía: mirar el tiempo y el espacio | Formulación editorial (clase introductoria) | 4-9 |
| 2 | Clase 2 — Los primeros pobladores del actual Paraguay | H1, literal | 10-14 |
| 3 | Clase 3 — Los guaraníes: pueblo, cultura y legado | H1, literal | 15-19 |
| 4 | Continuación A — Taller de fuentes sobre los guaraníes (y Ficha A) | H1, literal | 20-23 |
| 5 | Evaluación de la Unidad 1 | Asociación curricular: H1 | 24-26 |
| 6 | Clase 4 — El poblamiento de América | H2, literal | 27-30 |
| 7 | Clase 5 — Mayas, aztecas e incas | H2, literal | 31-34 |
| 8 | Continuación B — Mapa y línea de tiempo (Fichas B-1 y B-2) | H2, literal | 35-38 |
| 9 | Evaluación de la Unidad 2 | Asociación curricular: H2 | 39-41 |

Entregables (las copias livianas para revisión están en `revision_liviana/`):

| Documento | Páginas |
|---|---:|
| `tomo/TOMO_BLOQUE_I_oficio.docx` y `.pdf` | 41 |
| `planes/PLANES_BLOQUE_I_A4.docx` y `.pdf` | 20 |
| `solucionario/SOLUCIONARIO_BLOQUE_I_A4.docx` y `.pdf` | 10 |
| `figuras/` | 16 figuras propias |
| `datos/trazabilidad.json` | — |
| `datos/paginas_tomo.json` | — |
| `datos/controles.json` | — |

## 2. Qué corrige respecto del maestro

Cada punto responde a un hallazgo del diagnóstico (`01_diagnostico/revision_contenido/encuentros_01_a_12.md`).

**Clase 1**
- La regla del siglo cubre los años terminados en 00 y los años a. C.
- Se explica que no existe el año 0.
- Se agregan los tipos de fuentes, la periodización y las herramientas del mapa.
- La fuente es el art. 140 de la Constitución, que sí es verificable. Se eliminó la cita de Villoro, que no tenía referencia.

**Clase 2**
- Las fechas son aproximadas y regionales, con la advertencia de que los sitios paraguayos están poco fechados.
- Se quitó la dicotomía «Oriental agricultores / Chaco cazadores».
- Se agregaron las cinco familias lingüísticas del censo de 2012.
- Se corrigió el tuteo de la actividad 12.

**Clase 3**
- Territorio y parcialidades, con un mapa aproximado declarado como esquema.
- Mujeres y niños.
- Religión.
- Antropofagia ritual en su contexto.
- Bilingüismo bien caracterizado.
- La crónica de Schmidl aparece como versión escolar resumida, con autor y advertencia de que no es cita textual.

**Continuación A**
- El taller incluye las cuatro fuentes impresas y la matriz afirmación-evidencia-límite (Ficha A).

**Clase 4**
- Teorías clásicas (Ameghino, Hrdlička, Rivet, Mendes Correia) y lo que se sabe hoy.
- La presencia anterior a Clovis aparece como posición mayoritaria; White Sands, como dato en discusión.

**Clase 5**
- La chinampa no flotaba.
- Cronología de las tres civilizaciones, organización social y aclaración sobre Mesoamérica.
- Problema del nombre «prehistoria»: se explica por qué muchos historiadores prefieren «América prehispánica».
- La fuente es el fragmento de Cortés (1520), en versión modernizada.

**Continuación B**
- El tomo trae el cuadro de datos con fechas, el mapa mudo y el eje en blanco (Fichas B-1 y B-2).

**Evaluaciones U1 y U2**
- Criterios de puntaje en cada parte y mapa incluido.
- Clave gráfica docente con reglas de puntuación parcial.
- Matriz ítem-capacidad-puntaje.
- Autoevaluación de la unidad al terminar.

## 3. Condiciones del dictamen aplicadas desde este bloque

| Condición | Aplicación en el Bloque I |
|---|---|
| **A10 (equidad en evaluaciones)** | Las dos evaluaciones tienen tiempo adicional supervisado (80-95) y una actividad sin claves (95-120). El apoyo excepcional (más de 15 minutos) se administra antes del encuentro siguiente, en un horario acordado con la dirección y con la prueba custodiada. La devolución con claves se hace en los primeros 20 minutos del encuentro siguiente: el Plan 6 ya la reserva (100 minutos para H2). **El Plan 10 (Bloque II) deberá reservarla para la Evaluación U2.** |
| **A14 (maquetación)** | Letra sin reducir. Control 11 reforzado: mide la cobertura real de cada hoja (unión de bloques), detecta títulos solos al pie y exige que las hojas finales no sean residuales. Las fichas reproducibles van en hoja propia. La tercera hoja de cada evaluación lleva la autoevaluación de la unidad, que tiene función. |
| **A17 (cartografía)** | Las figuras se dibujan al tamaño de impresión, así que los tamaños de letra son efectivos: rótulos de 8 a 9,5 pt y notas de 7 pt. El control 8 comprueba que el ancho impreso coincida con el del lienzo. Hay leyenda completa en todos los mapas, escala aproximada, límites discontinuos, halos en los rótulos y nota de fuente que declara el carácter aproximado. |
| **Rúbricas visibles** | El tomo anuncia todos los criterios y el solucionario los repite sin agregar ninguno (control 6). |

## 4. Resultados de los controles automáticos

Se corren con `python3 scripts/verificar.py 1`. El resultado completo está en `datos/controles.json`.

| Control | Correctos | Fallos |
|---|---:|---:|
| 1. Capacidades y temas literales; fichas | 84 | 0 |
| 2. Tomo ↔ solucionario | 9 | 0 |
| 3. Tomo ↔ planes | 9 | 0 |
| 4. Funciones de las actividades | 14 | 0 |
| 5. Secuencias de 120 minutos | 9 | 0 |
| 6. Rúbricas, puntajes y matriz ítem-capacidad | 151 | 0 |
| 7. Claves de opción múltiple | 81 | 0 |
| 8. Figuras (numeración, citas, letra efectiva) | 44 | 0 |
| 9. Trazabilidad | 18 | 0 |
| 10. Equidad en evaluaciones | 2 | 0 |
| 11. Integridad visual (tomo, planes, solucionario) | 132 | 0 |
| 12. Voseo | 1064 | 0 |
| 13. Numeración de actividades | 9 | 0 |
| **Total** | **1626** | **0** |

**Claves de opción múltiple:** a 7, b 9, c 9, d 7. No hay tres claves iguales seguidas ni una letra con más de la mitad de las claves de una sección.

**Defectos que los controles detectaron durante la producción, ya corregidos:**
- Hoja de la Clase 3 con 45 % en blanco antes del mapa. Se reubicó la figura y se renumeró para que la numeración siga el orden de lectura.
- Ficha B-1 partida en dos hojas.
- Cita a figuras de otra clase que el verificador no reconocía (se ajustó el control).
- Formas verbales que el control confundió con tuteo (se ajustó el control).

## 5. Inspección visual

Se renderizaron y revisaron todas las páginas:

| Documento | Páginas revisadas |
|---|---:|
| Tomo | 41 |
| Planes | 20 |
| Solucionario | 10 |

No hay texto fuera de márgenes, tablas partidas sin encabezado ni renglones separados de su consigna.

Observaciones menores que quedan:
- La página 9 del tomo (fin de la Clase 1) y la 22 (fin del taller) son hojas finales cortas pero funcionales.
- Algunos planes terminan con media hoja en su última página (planes 4, 5 y 9).

## 6. Pendiente de verificación independiente

Lo que figura en `VERIFICACION` de cada `scripts/contenido/eNN.py` y en `datos/trazabilidad.json`. Esta sesión no tiene acceso a las páginas web de origen: solo a búsquedas, cuyos resultados se registran como fuentes secundarias.

**Textos citados**
- Art. 140 de la Constitución: cotejar con la edición oficial (BACN).
- Ley 4251/2010.
- Fragmento de Cortés: versión modernizada; cotejar con una edición.
- Relato de Schmidl: está resumido y declarado como no textual.

**Datos y fechas**
- Censo indígena 2012 (DGEEC, hoy INE).
- Fechas arqueológicas regionales (unos 8.000 años; unos 2.000 años).
- Monte Verde, Clovis, Cueva Fell y White Sands.
- Fechas de mayas, mexicas e incas.
- Etimologías de palabras de origen tupí-guaraní y significado de topónimos.

**Mapas**
- Áreas guaraní, maya, mexica e inca: son polígonos aproximados de la editorial y así se declaran en las figuras.

## 7. Reconstrucción posterior (15/10/2026)

Al producir el Bloque II se corrigió la escala gráfica común (`scripts/figuras/comun.py`): cuando la barra es corta, se omite el rótulo intermedio, que se superponía con el final («150300»). El Bloque I se reconstruyó con ese cambio. Cambian cinco mapas (`eval_u1_mapa`, `eval_u1_mapa_clave`, `fig_1_3_mapa_orientacion`, `fig_2_2_regiones` y `fig_3_1_area_guarani`) y se revisaron de nuevo. Los controles siguen en 1626 correctos y 0 fallos, y la paginación no cambia.

### 7.1 Comparación visual con las versiones anteriores (pedida en la revisión del 15/10/2026)

Se compararon píxel a píxel los cinco mapas regenerados con sus versiones del commit `755d7ad`:

| Mapa | Tamaño (antes = después) | Zona con diferencias | Píxeles distintos |
|---|---|---|---:|
| `eval_u1_mapa` | 1062 × 1190 | 63 × 34 px, rótulo intermedio de la escala | 429 |
| `eval_u1_mapa_clave` | 1062 × 1190 | 63 × 34 px, ídem | 429 |
| `fig_1_3_mapa_orientacion` | 1417 × 1535 | 62 × 33 px, ídem | 452 |
| `fig_2_2_regiones` | 1299 × 1455 | 62 × 34 px, ídem | 433 |
| `fig_3_1_area_guarani` | 1358 × 1476 | 63 × 33 px, ídem | 464 |

Resultado:
- El único cambio es la supresión del rótulo intermedio de la escala («100» o «200»), que quedaba casi pegado al rótulo final.
- El tamaño de las imágenes no cambió y el resto de cada mapa es idéntico píxel a píxel.
- No hay desplazamientos, recortes ni rótulos superpuestos nuevos.
- Ampliación «antes / después» de cada escala en `datos/comparacion_escala_antes_despues.png`: arriba de la franja roja, antes; abajo, después.
