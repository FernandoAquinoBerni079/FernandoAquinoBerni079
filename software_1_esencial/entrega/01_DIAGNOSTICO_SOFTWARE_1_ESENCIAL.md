# 01_DIAGNOSTICO — Gabinete de Informática – Software · 1.er Curso BTI · Edición Esencial Comercial 2026

Fecha de esta versión: 11/10/2026 · Paquete: `BTI_GABINETE_SOFTWARE_1` · Caso integrador: Servicio Técnico Panambi
Protocolo: PROTOCOLO_CLAUDE_CHATGPT_2026 v0.4, **en estado BORRADOR, pendiente de aprobación de Fer**.

Este archivo reúne tres cosas:

- **Parte A.** El estado del paquete al integrarlo al repositorio: qué versión se tomó, de dónde viene y cómo se verificó.
- **Parte B.** El diagnóstico original previo a la reconstrucción, *01_DIAGNOSTICO_BTI_GABINETE_SOFTWARE_1* (Drive, 01/10/2026).
- **Parte C.** El diagnóstico de unificación del tomo y el laboratorio, *01b_DIAGNOSTICO_UNIFICACION_LABORATORIO_BTI_GABINETE_SOFTWARE_1* (Drive, 01/10/2026, v2).

Las partes B y C se transcriben sin cambios, como registro histórico. **Sus cifras describen el material de agosto de 2026, no la versión actual.**

---

## Parte A — Estado al 11/10/2026 (verificación previa a la integración)

### A.1 Fuentes revisadas

| Fuente | Qué contiene | Resultado |
|---|---|---|
| Rama `claude/auditoria-software-1-3fp293`, commit `2fce279` (05/10/2026) | `Software_1er_Curso/`: combo completo (v1 corregida), 05_RESPUESTA, scripts de corrección | **Versión vigente.** Es la que se integra. |
| Rama `claude/vigilant-einstein-9wbdg0` | Contiene `2fce279` sin cambios en Software 1.º. Su último commit, `ac5454f`, toca solamente Planes de otras materias. | Archivos idénticos a la versión vigente, byte a byte. |
| Rama `claude/trusting-hawking-13gfsj` | Contiene `78e9aea` (02/10) pero no `2fce279` | Libro, Solucionario y 05_RESPUESTA idénticos. **Plan Anual, Planes y Muestra son la versión anterior, en A4**: no se usan. |
| Rama `claude/libros-5z31jx` (destino) | Algorítmica 1.º–3.º y Software 2.º | No había Software 1.º. No se modifica nada de lo existente. |
| Drive `01_BACHILLERATO_TECNICO_INFORMATICA/Software_1er_Curso` | Combo subido por Fer el 02/10, versiones anteriores en `SUPERSEDIDOS/`, `_TRABAJO/` | Sin cambios después del 03/10. Solucionario, Plan Anual, Planes y Muestra **coinciden** con la versión vigente. El **Libro de Drive es la revisión anterior** (.docx de 23.331.976 bytes): no tiene el párrafo ancla que hace empezar la diagnóstica y las 5 evaluaciones en hoja propia en Word. El texto y la paginación en LibreOffice son idénticos. |

No existe en Drive ni en el repositorio una auditoría v2 de ChatGPT para Software 1.º. La última es `04_AUDITORIA_CHATGPT_SOFTWARE_1_ESENCIAL_v1`, que se respondió con `05_RESPUESTA_CLAUDE_SOFTWARE_1_ESENCIAL_v1`.

### A.2 Versión integrada (procedencia por documento)

| Documento | Versión | Procedencia |
|---|---|---|
| LIBRO (.docx/.pdf) | v1 corregida + anclas de salto (02/10) | Original de Fer (`…LIBRO_ESENCIAL_COMERCIAL_2026_1.docx`, guardado en Word, A4, 137 págs.) → correcciones de la auditoría v1 → oficio, márgenes estrechos, tablas a la ventana → paginación e índice → anclas antes de las bandas de evaluación. PDF: LibreOffice 24.2. |
| SOLUCIONARIO (.docx/.pdf) | v1 corregida, en oficio (02/10) | Solucionario del 02/10 → correcciones v1 → oficio, decisión de Fer del 02/10. PDF: LibreOffice 24.2. |
| PLAN_ANUAL (.docx/.pdf) | v1 corregida, en oficio apaisado (02/10, 16:41) | Versión corregida por Claude (capacidad MEC por secuencia, Ley 7593) y pasada a oficio en otra sesión. Bajada de Drive y verificada. PDF: LibreOffice 25.2. |
| PLANES_DE_CLASE (.docx/.pdf) | v1 corregida, en oficio (02/10, 16:40) | Ídem. PDF: LibreOffice 25.2. |
| MUESTRA_COMERCIAL (.pdf) | 02/10, 16:41 | Libro pp. 1–4 y 6–10 (Clase 1 y Práctica 1), contraportada (p. 107), portada del Solucionario y Planes pp. 1, 3 y 4 (Plan 1). |

### A.3 Estado editorial

**Listo para la auditoría v2 de ChatGPT.** No está aprobado para la venta: falta la reauditoría (protocolo §3, paso 4) y la aprobación de Fer (paso 6). Los 14 hallazgos de la auditoría v1 se atendieron (ver `05_RESPUESTA…md`). No se hicieron cambios pedagógicos nuevos para esta integración.

### A.4 Documentos completos y faltantes

Completos: Libro, Solucionario, Plan Anual y Planes de Clase, cada uno en DOCX y PDF, y la Muestra en PDF. No falta ninguna pieza del combo (protocolo §4.4). Las prácticas van dentro del libro (§3quater).

### A.5 Diferencias entre versiones

- Libro de Drive y Libro integrado: misma letra y misma paginación; difieren solamente en los 6 párrafos ancla (1 pt) que hay antes de la Prueba diagnóstica y de las 5 evaluaciones.
- Rama `trusting-hawking` frente a la versión vigente: Plan Anual, Planes y Muestra en A4; mismo texto.
- La 05_RESPUESTA dice que «los Planes de clase y el Plan anual siguen en A4». Eso era cierto cuando se escribió; ahora están en oficio. La transcripción se deja sin cambios y la aclaración va en las notas del piloto.

---

## Parte B — 01_DIAGNOSTICO_BTI_GABINETE_SOFTWARE_1 (Drive, 01/10/2026; transcripción)

**Fecha:** 01/10/2026 · **Autor:** Claude · **Paquete:** Gabinete de Informática – Software, 1.er Curso BTI · **Caso integrador:** Servicio Técnico Panambi · **Protocolo:** PROTOCOLO_CLAUDE_CHATGPT_2026 v0.3

**Versión diagnosticada:** Software_1er_Curso_TOMO_Final (DOCX y PDF del 26/08/2026, 75 págs. A4) + Solucionario, Plan Anual, Planes de Clase y Cuaderno de Laboratorio de la misma fecha.

### 1. Veredicto

**NO APTO PARA VENTA todavía.** El combo está completo y las imágenes ya pasaron por Gemini; lo que falta es profundidad en las 20 clases, rehacer la portada y corregir el índice.

### 2. Combo

| Pieza | Estado | Observación |
|---|---|---|
| Tomo | Existe (DOCX + PDF) | 3 unidades, 20 clases núcleo, 3 evaluaciones de unidad, 2 de etapa. |
| Solucionario docente | Existe (DOCX + PDF) | Cubre las 20 clases (≈5 100 palabras). Habrá que ampliarlo junto con el tomo. |
| Plan Anual | Existe (DOCX + PDF) | 36 encuentros, 2 HC semanales. |
| Planes de Clase | Existe (DOCX + PDF) | **36 planes** = 36 encuentros. OK. (El catálogo dice «22 planes»: dato desactualizado, corregir.) |
| Cuaderno de Laboratorio | Existe (DOCX + PDF) | Misma numeración que el tomo. |
| Muestra comercial | Falta | Se arma al final. |

### 3. Imágenes

- 20 imágenes en el tomo; **las 20 pasaron por Gemini** (estilo, tamaño 1024/1536 px). Columna IMAGENES = **GEMINI_COMPLETO**. No se tocan.
- Epígrafes inconsistentes: 5 dicen «Ilustración didáctica generada con IA» y otras «Fuente: elaboración propia». Unificar el criterio (decisión de Fer, ver §7).
- Numeración de figuras fuera de orden en la Clase 1 (aparece la Figura 1.2 antes que la 1.1). Revisar en todo el tomo.

### 4. Portada e índice

- **Portada:** franja verde con texto centrado sobre página blanca, sin imagen, sin sello de colección ni de edición, con «Página 1 de 75» al pie. Rehacer con la plantilla nueva.
- **Índice:** está poblado (bien), pero **los números de página están corridos en una página desde la Clase 4 hasta la Clase 20** (ej.: Clase 4 dice p. 17 y empieza en p. 18; Clase 20 dice p. 68 y empieza en p. 69). Además lista los subtítulos de cada clase y ocupa 4 páginas; se incluye a sí mismo («Índice … 3») y repite el título («Índice / Índice de contenidos»). Rehacer con dos niveles (Unidad → Clase, más evaluaciones) y números verificados contra el PDF.

### 5. Profundidad por clase (desarrollo sin ficha ni actividades)

Mínimo Esencial para BT: **750 palabras**. Mediana actual: **471** (mín. 414, máx. 523). **Las 20 clases están por debajo del mínimo.** Todas tienen ejemplo, «Concepto clave», «En Paraguay» y 12 actividades: la estructura está bien, falta desarrollo.

| Clase | Tema | Palabras | Faltan para 750 | Actividades | Figuras |
|---|---|---|---|---|---|
| 1 | La informática: concepto, características y elementos | 488 | 262 | 12 | 2 |
| 2 | La computadora: definición, características, tipos y división | 417 | 333 | 12 | 0 |
| 3 | Unidades de medida de la información | 523 | 227 | 12 | 1 |
| 4 | Evolución histórica y generaciones de las computadoras | 445 | 305 | 12 | 1 |
| 5 | Elementos básicos del hardware | 466 | 284 | 12 | 2 |
| 6 | Elementos básicos del software | 419 | 331 | 12 | 1 |
| 7 | Unidades de almacenamiento secundario | 459 | 291 | 12 | 2 |
| 8 | Ética y seguridad en el ámbito informático | 522 | 228 | 12 | 2 |
| 9 | Software propietario, software libre y aplicaciones actuales | 507 | 243 | 12 | 0 |
| 10 | El sistema operativo: concepto, propósito, funciones y partes | 424 | 326 | 12 | 1 |
| 11 | Origen, generaciones y sistemas operativos actuales | 497 | 253 | 12 | 0 |
| 12 | Licencias de software y funcionamiento del sistema | 458 | 292 | 12 | 0 |
| 13 | Procesos: definición, tipos, estados y transiciones | 470 | 280 | 12 | 1 |
| 14 | Administración de procesos: planificación y algoritmos | 519 | 231 | 12 | 1 |
| 15 | Sistemas de archivos: archivos y directorios | 468 | 282 | 12 | 1 |
| 16 | La memoria y su administración | 472 | 278 | 12 | 1 |
| 17 | Sistemas de numeración y conversión de números enteros | 490 | 260 | 12 | 2 |
| 18 | Conversión entre bases: binario, octal y hexadecimal | 506 | 244 | 12 | 1 |
| 19 | Números fraccionarios: conversiones entre bases | 414 | 336 | 12 | 0 |
| 20 | Operaciones con números binarios | 503 | 247 | 12 | 1 |

Ampliación total estimada: unas 5 600 palabras (≈ +15 a 20 páginas). El tomo Esencial quedaría en unas 90–95 páginas.

### 6. Plan de trabajo (Edición Esencial)

1. Ampliar cada clase a ≥ 750 palabras: más explicación del «cómo funciona», un ejemplo resuelto completo con el caso Panambi y una tabla comentada donde falte. Sin cambiar las fichas (el Plan Anual y los Planes de Clase siguen valiendo).
2. Ampliar el Solucionario en lo que corresponda.
3. Portada nueva + contraportada; índice de dos niveles con números verificados.
4. Conservar las 20 imágenes de Gemini tal cual; ordenar la numeración de figuras y unificar epígrafes.
5. Nombres canónicos, metadatos, PDF regenerados; corregir el catálogo (36 planes, IMAGENES = GEMINI_COMPLETO).
6. Auditoría técnica → informe de ChatGPT → aprobación de Fer.

### 7. Bloqueos y decisiones

- **Bloqueo técnico:** el DOCX del tomo pesa 19 MB y la conexión de Drive de Claude no descarga archivos de más de 10 MB. Para rearmarlo conservando las imágenes de Gemini sin pérdida hace falta conectar a la sesión la carpeta de Drive del equipo de Fer (G:\Mi unidad). Mientras tanto se puede redactar la ampliación del contenido.
- **Decisión de Fer:** epígrafes «generada con IA»: ¿se mantienen en cada figura, se reemplazan por una nota única en créditos, o se quitan?
- **Decisión de Fer:** nombre de la colección para la portada; confirmar «Edición Esencial / Edición Completa».

---

## Parte C — 01b_DIAGNOSTICO_UNIFICACION_LABORATORIO_BTI_GABINETE_SOFTWARE_1 (Drive, 01/10/2026, v2; transcripción)

**Fecha:** 01/10/2026 (v2, corrige la v1) · **Autor:** Claude · **Decisión de Fer:** unificar en un solo libro, sin ejercicios duplicados (Protocolo v0.4, sección 3quater).

### 1. Material de partida

- Tomo: 75 págs., 20 clases.
- Cuaderno de Laboratorio: 49 págs., 20 prácticas (misma numeración que las clases) + 11 fichas complementarias A–K (una por cada continuación práctica del Plan Anual), 6 imágenes.
- Solucionario actual: ya incluye claves de prácticas y fichas.
- Libro unificado estimado (con la ampliación Esencial): unas 140 págs.

### 2. Ejercicios y datos duplicados (a corregir)

Comparación automática de datos numéricos y enunciados entre cada clase, su práctica y las fichas.

| Clase | Dato repetido en el tomo | Dónde se repite | Corrección |
|---|---|---|---|
| 3 | 16 GiB = 16 384 MiB; 2 048 KiB = 2 MiB; ítem V/F «1 GiB = 1 024 MiB» | Práctica 3 (2 048 KB = 2 MB; 16 GB = 16 384 MB) y Ficha A (tabla 1 GB = 1 000 MB / 1 GiB = 1 024 MiB) | Práctica 3 y Ficha A con capacidades distintas (otros discos y pendrives de Panambi) |
| 14 | Ejemplo FIFO/SJF: esperas 0/2/62 → 21,33 min; SJF 0/2/17 → 6,33 min | Práctica 14 (mismo cálculo en Excel, mismos resultados) | Práctica con otra cola de trabajos del taller |
| 17 | Código 156 = 10011100₂ = 234₈ (ejemplo resuelto) | Práctica 17, Actividad 1 (verifica el mismo 156) | Práctica con otros códigos de inventario |
| 18 | 37₈ → 11111₂; 2F₁₆ → 101111₂ | Práctica 18, Actividad 2 (mismas conversiones) | Práctica con otras cifras |
| 19 | 0,625; 0,8125; 0,4 → 0,0110… | Práctica 19 (mismos valores en la plantilla de Excel) | Práctica con otras fracciones |
| 20 | 1011 + 110 = 10001 (ejemplo y opción múltiple 2) | Práctica 20 (tabla de verificación con la misma suma) | Práctica con otras operaciones |

Coincidencias que **no** son duplicación y se mantienen: la tabla de generaciones (1946–1958…) como dato de referencia, la cita del MITIC del 23/07/2025 como fuente, y la Ley 1328/98 como norma. La Ficha J usa datos propios (A=6, B=2, C=4 ms), no repite la Clase 14.

### 3. Respuestas dentro del material del estudiante

Varias fichas dan el resultado en la misma consigna (ej.: Ficha J: «Calculá FIFO: esperas 0, 6, 8 y promedio 4,67 ms»). Así el estudiante no calcula nada. En el libro unificado, la consigna pide el cálculo y el resultado pasa al Solucionario; el punto de control dice qué verificar, no el número. Revisar todas las fichas A–K y los «Resultados esperados» de las prácticas con el mismo criterio.

### 4. Numeración de figuras

Hay figuras con el mismo número en los dos libros: 1.1, 4.1, 7.1, 10.1 y 15.1. En el libro unificado se renumeran de corrido por clase (las de la práctica siguen a las de la clase).

### 5. Orden del libro unificado

1. Portada · Presentación (fusionada) · Índice de dos niveles · Prueba diagnóstica
2. Por cada clase: Clase N → Práctica N (página propia)
3. Fichas A–K ubicadas después de la clase donde el Plan Anual pone su continuación práctica
4. Evaluaciones de unidad y de etapa en su lugar actual

### 6. Otros ajustes

- Plan Anual, Planes de Clase y presentación: reemplazar «Cuaderno de Laboratorio» por «Práctica N».
- Solucionario: actualizar las claves de las prácticas que cambien de datos.
- Las 6 imágenes del cuaderno se revisan con la regla de Gemini (sección 3ter).
- El mismo procedimiento se aplica luego a Laboratorio 1.º, 2.º y 3.º, Hardware 2.º y Software 2.º.
