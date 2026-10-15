# Informe del lote editorial 1 — Preliminares y Unidad I (Capítulos 1 a 3)

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · Fase 3**

**Estado:** construido, verificado automáticamente e inspeccionado visualmente.
- Queda para auditoría independiente (ChatGPT y Work).
- **No está aprobado para la venta ni para uso en aula.** La aprobación final es de Fernando.

**Fuentes del lote:**
- `lote_1_plan/PLAN_LOTE_1_CAPITULOS_1_A_3.md`.
- Informe de Work v0.1, SHA-256 `3d4f5ab9daf3329f0dd34b13bc30b7001cb8e65780262c536346dbbea065069a`. No se sube al repositorio.
- Plan de integración del Capítulo 2 (Fase 2).
- Capítulo 4 v2 / v2.1.

## 1. Entregables

| Archivo | Contenido | Páginas |
|---|---|---:|
| `ADS_3BTI_LOTE1_ESTUDIANTE.docx` y `.pdf` | Portada, índice, 8 preliminares, apertura de la Unidad I y Capítulos 1 a 3 | 56 |
| `ADS_3BTI_LOTE1_GUIA_DOCENTE.docx` y `.pdf` | Guía docente del lote | 19 |
| `caso/dossier.py` | Fuente única del caso Arapoty | — |
| `caso/mbokaja.py` | Caso de práctica | — |
| `caso/verificar_caso.py` | Control del caso contra el Capítulo 4 v2 y el candidato del Capítulo 2 | — |
| `build/` | Scripts de construcción, figuras, verificador y prueba de fuentes, con sus resultados | — |
| `MANIFIESTO_LOTE_1.json` | SHA-256 y tamaño de los 60 archivos del lote y de la v2.3 del prototipo | — |

**Contenido del libro del estudiante:**
- **Por capítulo:** ficha; cuatro secciones de Work; ejemplos resueltos (Cap. 1: 4; Cap. 2: 5; Cap. 3: 4); figuras originales (2, 2 y 1); actividades del encuentro en cuatro bloques (Ejercitá, Resolvé, Pensá y decidí, Desafío); práctica en tres niveles; recuadros «Para repasar» y «Si el calendario se acorta»; evaluación opcional en página propia (15 puntos).
- **Capítulo 3:** además, la revisión de la Unidad I (H1), con su lista de verificación, sus criterios y los niveles de desempeño.

**Contenido de la guía docente:**
- secuencia de los seis encuentros en HC;
- claves de las 32 actividades, de las tres prácticas y de las tres evaluaciones, con criterios de corrección;
- listas de cotejo;
- claves del diagnóstico y mapa de apoyos;
- tarjetas de rol de la Práctica 2;
- destino de los 31 elementos del candidato del Capítulo 2;
- rúbrica completa del H1 con su planilla;
- calendario en 36 y en 28 encuentros;
- coordinación con Algorítmica y Laboratorio;
- procedencia de los recursos.

**Reconstrucción:**
```
python3 lote_1/build/construir.py
python3 lote_1/build/verificar.py
python3 lote_1/build/prueba_fuentes.py
python3 lote_1/caso/verificar_caso.py
```

## 2. Decisiones aprobadas y cómo se aplicaron

| N.º | Decisión | Aplicación |
|---:|---|---|
| 1 | Preliminares desde el lote 1 | Los ocho de Work §6, en orden (control A). El diagnóstico de entrada no lleva nota: 9 ítems de saberes de 1.º y 2.º, más una autoevaluación. |
| 2 | Caso Colegio Técnico Arapoty | Fuente única `caso/dossier.py` (§3). |
| 3 | Rúbrica de cuatro niveles y 60/40 como propuesta editorial | La rúbrica del H1 tiene 5 criterios × 4 niveles (descriptores de Work §4.3) y la evidencia del equipo (60 %) y la individual (40 %) de cada criterio. La ausencia de evidencia se registra aparte. Está rotulada «propuesta editorial» en el libro y en la guía. |
| 4 | 36 encuentros y 180 HC, con 28 como alternativa | Cada capítulo tiene su recuadro de calendario reducido. La guía trae la tabla 36/28: en 28, los Encuentros 5 y 6 se unen, con dos alternativas y un H1 breve (según la distribución v2.1 de la Fase 2). |
| 5 | Permisos mínimos en el núcleo; RN-01 a RN-06 como reglas didácticas | **Alcance mínimo:** la Tabla 3.5 incluye «Permisos mínimos», con sus fuentes E4-L8 y E5-L6. **Reglas:** el Capítulo 3 las presenta sin numerar, como «reglas iniciales para negociar en clase», con el texto idéntico al de RN-01 a RN-06 del Capítulo 4. |
| 6 | Mapa de interesados en el Capítulo 1; el Capítulo 2 con el material corregido | **Mapa:** sección 1.3, con los valores del candidato (control D). **Capítulo 2:** construido según el plan de integración (§4). |
| 7 | Capítulo 3: alternativas y factibilidad, sin la matriz ponderada | **Qué se compara:** tres tipos de solución, no tecnologías: registro manual mejorado, herramienta existente y prototipo propio. **Cómo:** factibilidad cualitativa (operativa, técnica, económica y de calendario) con razones y fuentes, sin números ni sumas. **Algorítmica:** un recuadro remite a la Práctica 4 de Algorítmica 3.º para quien quiera pesos (control E). |

## 3. Fuente única del caso y trazabilidad con el Capítulo 4

**`caso/dossier.py`** contiene:
- la institución y las personas;
- los registros D0, E1 a E5, O1, D1 y D2, numerados por línea;
- 13 necesidades N-01 a N-13 con sus fuentes y su estado;
- las necesidades no expresadas;
- los interesados, las reglas y el alcance mínimo.

**Origen de cada registro:**
- **E1, E2, E3 y O1:** del candidato del Capítulo 2, con el mismo texto.
- **E4 y E5:** las líneas que cita el Capítulo 4 v2 se copiaron sin cambios. Son nuevas las preguntas del analista y las líneas E4-L11, E4-L12, E5-L7 y E5-L8.
- **D0, D1 y D2:** nuevos.
  - D0 es la nota de la dirección que abre el proyecto.
  - El informe D2 tiene un error de suma intencional (112 frente a 115), que se usa en 2.2 y 2.3.

**`caso/verificar_caso.py`: 107 correctos, 0 fallos.** Comprueba:
- cada fragmento que cita el Capítulo 4 (v2 y v2.1): existe, lo dice el entrevistado y contiene la cita textual;
- las reglas, idénticas a las del Capítulo 4;
- N-02 = «Evitar entregar a dos lectores el mismo ejemplar.», fuente E4-L4, como en la Figura 4.2 y en Work §7.3;
- la conservación del texto del candidato;
- la ausencia de datos de Algorítmica 3.º.

**El Capítulo 4 no se tocó:**
- `contenido.py` de la v2 y de la v2.1 tienen el mismo SHA-256 (`62179ecb…`), y git no registra cambios en esas carpetas;
- la especificación de evidencia C3 queda aprobada para la próxima versión del capítulo y no se aplicó en este lote.

## 4. Integración del Capítulo 2

Los 31 elementos del candidato tienen destino:

| Acción | Elementos |
|---|---:|
| Adaptar | 15 |
| Conservar | 8 |
| Dividir | 1 |
| Retirar | 4 |
| Trasladar | 3 |

- **Conservar:** el control D verifica que el texto sea idéntico.
- **Retirar:** el capítulo no redacta requisitos, que quedan en el Capítulo 4.
- **Dossier:** incluye E4 y E5 y cierra con N-01 a N-13 (Tabla 2.7).

**Contenido nuevo pedido por el plan:**
- 2.2: análisis de documentos (Ejemplo resuelto 2.2 y Tabla 2.4);
- 2.3: necesidades no expresadas (Ejemplo resuelto 2.4) y una contradicción real del dossier (E2-L8 frente a D1-A3), en lugar de la situación hipotética del candidato;
- 2.4: autorización, anonimización y resguardo (Tabla 2.6);
- Práctica 2: simulación con roles.

**Diferencia con la renumeración del plan.** El plan preveía los Ejemplos resueltos 2.1 a 2.3. Al agregar el contenido nuevo quedaron cinco, numerados en orden de aparición:

| Ejemplo | Contenido | Origen |
|---|---|---|
| 2.1 | Guion | Candidato |
| 2.2 | Documentos | Nuevo |
| 2.3 | Contradicción | Adaptado del candidato |
| 2.4 | Necesidades no expresadas | Nuevo |
| 2.5 | Hallazgos | Adaptado del candidato |

## 5. Controles automáticos

### 5.1 `build/verificar.py`: 118 correctos, 0 fallos

| Bloque | Qué comprueba | Correctos |
|---|---|---:|
| A. Índice de Work | Títulos, encuentros, secciones textuales y en orden, prácticas, H1 y preliminares | 14 |
| B. Capacidades | Rótulo «propuesta para el programa institucional; no es (son) oficial(es) del MEC» en libro y guía; texto de C1, C2 y C7; ninguna presentada como oficial | 11 |
| C. Trazabilidad | Los 131 códigos de fuente del libro y los 58 de la guía existen; las 18 citas textuales con código coinciden con su línea; dossier completo en el libro; N-02; reglas sin numerar; sin RF, RNF ni RS; alcance con permisos; control del caso | 11 |
| D. Integración del Capítulo 2 | Ver §4 | 11 |
| E. Algorítmica 3.º | Sin sus personas ni títulos; sin «ponderad…» ni pesos 0,5/0,3/0,2; «pesos» solo en la remisión; sin comparación de tecnologías; Tabla 3.3 sin números | 5 |
| F. Voseo y residuos | Sin tuteo; sin identificadores de modelos; sin ✓ ✗; sin marcadores; no se declara apto | 10 |
| G. Maqueta en DOCX | `helpers.py` y `maqueta.py` idénticos a los del Capítulo 4 v2.1; todas las filas «no dividir»; tablas a 16,6 cm con tblGrid; encabezado repetido | 8 |
| H. Maqueta en PDF | Sin páginas en blanco ni renglones sueltos; evaluaciones y prácticas en página propia; índice de una página y estable; extensión | 15 |
| I. Evaluaciones e instrumentos | Ver la lista debajo | 18 |
| J. Numeración | Tablas, figuras y ejemplos correlativos; toda referencia existe | 15 |

**Detalle del bloque I:**
- claves repartidas;
- 15 puntos por evaluación;
- semillas nuevas;
- rúbrica del H1 completa;
- 60/40 rotulado;
- tres niveles por práctica;
- secuencia en HC;
- tarjetas de rol solo en la guía;
- calendario de 28 encuentros.

**Claves de opción múltiple:**

| Capítulo | Claves |
|---|---|
| 1 | b c d d |
| 2 | c b b a (semilla ADS3-L1-C2-i, elegida para repartirlas) |
| 3 | a b b d |

### 5.2 `build/prueba_fuentes.py`: 6 de 6 combinaciones correctas

| Fuente de sustitución | Libro | Guía | Evaluaciones en página propia | Páginas en blanco o renglones sueltos |
|---|---:|---:|---|---|
| Carlito | 56 | 19 | Sí | Ninguno |
| Liberation Sans | 57 | 19 | Sí | Ninguno |
| DejaVu Sans | 61 | 19 | Sí | Ninguno |

**Corrección que surgió de esta prueba:** con DejaVu Sans aparecía una hoja en blanco antes de una evaluación, por el salto que inserta `helpers.evaluacion()`.
- **Solución:** sin modificar `helpers.py`, un paso final (`comun.saltos_a_titulos`) convierte esos saltos en «salto de página antes» del título.
- **Libro y guía:** los títulos que empiezan página usan el mismo mecanismo.

## 6. Inspección visual

Se revisaron las 56 páginas del libro y las 19 de la guía en miniatura, además de las figuras.

**Hojas con menos de la mitad ocupada.** Son finales de sección antes de una página nueva:
- **Libro:**
  - pág. 6: fin de la autoevaluación del diagnóstico;
  - pág. 9: apertura de la Unidad I;
  - págs. 19, 23, 41 y 56: final de la práctica o de la evaluación;
  - págs. 38 y 52.
- **Guía:** págs. 3, 7, 16 y 19.

**Lo que no se pudo verificar:**
- No hay Calibri en el entorno: el PDF de control se generó con Carlito, que tiene las mismas métricas.
- El índice del libro es estático y se calcula sobre ese PDF. En Word, la paginación puede variar levemente.

## 7. Procedimiento para retirar la marca de mantenimiento

Pedido en la autorización de la Fase 3. **PHP + SQLite sigue provisional.**

| Archivo | Contenido |
|---|---|
| `fase2_pilotos/B_prueba_tecnica/PROCEDIMIENTO_RETIRO_MARCA_MANTENIMIENTO.md` | El procedimiento: pasos, comprobaciones, restauración y límites |
| `prototipo_v2_3/` | Copia de la v2.2 con `retirar_marca.php` (diagnóstico y retiro seguro), su prueba y el LEEME actualizado. La v2.2 no cambió. |
| `ADENDA_PRUEBA_TECNICA_v2_3.md` | Resumen de los cambios de la v2.3 |
| `PRUEBAS_PENDIENTES_CAMPO.md` | Punto 9 nuevo: el retiro en Windows |

**Prueba nueva:** `prueba_marca_huerfana.php`, **19 de 19**. Simula cortes con SIGKILL:
- durante la espera del reinicio;
- a mitad del reinicio, con diario caliente;
- en modo WAL.

También cubre:
- un proceso vivo;
- otra conexión con la base tomada;
- un respaldo cortado;
- una base dañada;
- un esquema incompleto.

**Regresión:**

| Prueba | Resultado |
|---|---|
| Mantenimiento | 30 de 30 |
| Respaldo | 18 de 18 |
| Garantías | 14 de 14 |
| Reglas | 37 de 37 |
| Carrera | 10 de 10 |
| HTTP | 32 de 32 |

**Límites:**
- solo Linux;
- el corte simulado mata el proceso, no apaga el disco.

## 8. Decisiones editoriales tomadas en el lote, para revisar en la auditoría

1. **Reparto de secciones por encuentro.**
   - **Qué se hizo:**
     - Encuentro 1: preliminares (reto, diagnóstico, acuerdo), 1.1 y 1.2;
     - Encuentro 2: 1.3, 1.4 y Práctica 1.
   - **Por qué:**
     - Work asigna el «mapa de apoyos» al Encuentro 1 y el índice ubica 1.4 al final.
     - El mapa de apoyos quedó como instrumento del docente (guía, §1), armado con el diagnóstico del Encuentro 1.
     - En 1.4, cada estudiante arma su plan de apoyo personal.
2. **Caso de práctica Mbokaja.**
   - Las tres prácticas usan otra escuela ficticia, con datos distintos de los ejemplos (Work §7.4).
   - En la Práctica 3, los datos llevan a recomendar el registro manual mejorado y no el prototipo. Muestra que el análisis no está forzado.
3. **Nota D0 de la dirección.** Es el reto inicial: el Capítulo 1 trabaja con ella y no cita registros que se relevan recién en el Capítulo 2.
4. **Pendiente que el caso deja a la vista.** Nadie entrevistó al encargado de informática. El Capítulo 3 lo marca «a verificar» en la factibilidad de la herramienta existente.
5. **Recomendación del caso.** Prototipo propio con alcance mínimo, con el registro manual mejorado como contingencia ante cortes. Decide la dirección.
6. **Hitos.** El calendario de H1 a H6 (Tabla 3.8) sale de Work §5.2.
7. **Evaluaciones de los capítulos.** Son opcionales; en la Unidad I, el instrumento principal es el H1.

## 9. Limitaciones y pendientes

- **Auditoría y aprobación:** auditoría independiente del lote y aprobación de Fernando. No se avanzó a los Capítulos 5 a 18 ni se subió nada a Drive.
- **Diseño curricular:**
  - La afirmación de que el diseño curricular (mayo de 2026, p. 29) permite el programa institucional del Plan Optativo se toma del informe de Work.
  - En este lote no se verificó por separado; así se declara en la guía.
- **Prueba en aula:** no se validaron los tiempos por encuentro. Las HC son aproximadas y la duración de la hora cátedra la fija la institución.
- **Maqueta:**
  - La identidad «verde BTI» sigue provisional, sin cotejo de color con el catálogo.
  - El índice es estático.
- **Constitución, art. 140:** recuadro «En Paraguay» conservado del candidato. El contenido coincide con el texto constitucional (país pluricultural y bilingüe; castellano y guaraní oficiales), pero no se cotejó en este lote contra una edición oficial.
- **Fuera de este lote:** la especificación C3 del Capítulo 4 se aplica en la próxima versión de ese capítulo.

## 10. Huellas SHA-256 de los entregables principales

| Archivo | SHA-256 |
|---|---|
| `ADS_3BTI_LOTE1_ESTUDIANTE.docx` | `333e9baad26b8c21860fc3ab0d97d53da02ce2525019c48c37b0438cd245f8e7` |
| `ADS_3BTI_LOTE1_ESTUDIANTE.pdf` | `4b41eeae22e92ce7d55fc4ba02d9d1378b0390b9e05bcadf48376ddb52864aa8` |
| `ADS_3BTI_LOTE1_GUIA_DOCENTE.docx` | `8c8741d0b5f50eeeb5d0d5a97ee2e22dbb3714c643adbd57622895bb1a6bff1e` |
| `ADS_3BTI_LOTE1_GUIA_DOCENTE.pdf` | `2aa150644168471675309f2aaf05a039b6ec6fdfb645d956c0c7bb27479f9ac0` |
| `caso/dossier.py` | `fa658775836e7649250271e76ea567e55feba9f1a6832be445e1db614a6b12e8` |
| `prototipo_v2_3/retirar_marca.php` | `6c4fd1d5ecaee246f8b8fd5caf44fff7769343c4174f59547fa0654a848b368d` |

La lista completa está en `MANIFIESTO_LOTE_1.json`.
