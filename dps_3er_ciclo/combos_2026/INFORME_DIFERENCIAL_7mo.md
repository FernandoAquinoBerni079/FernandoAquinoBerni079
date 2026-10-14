# Informe diferencial — Combo DPS 7.º EEB (edición candidata para auditoría)

Estado: **candidata para auditoría de ChatGPT.** No está aprobada para la venta. La aprobación final corresponde a Fernando.

## 1. Base de trabajo

- La base es el combo candidato de 7.º que preparó ChatGPT. Se tomó del ZIP en partes de la carpeta de Drive `1CYSnbkZ4TGL0JXVHSrSHDToY47Bq8TzJ`.
  - SHA-256 del ZIP reensamblado: `6e87a63b28dfa8543e2211e6bc679d5ff42fff3967443c041c846a4007d09c06`.
  - Copia exacta en `base_candidata/7mo/`, con los hashes en `base_candidata/SHA256.txt`.
- La edición es diferencial. Los scripts de `edicion/` abren cada archivo candidato y aplican solo los cambios de la sección 2. No se reconstruyó el libro.
  - Las 21 clases, las evaluaciones y las ilustraciones conservan el texto y la maqueta de la candidata.
- No se tocaron los maestros de Drive ni se subió nada a Drive.

## 2. Cambios por archivo

### Tomo (`7mo/DPS_7mo_TOMO_INTEGRAL_PEC_OFICIO_2026.docx` y `.pdf`)

| N.º | Cambio | Motivo |
|---|---|---|
| T-1 | Portada profesional a página completa: imagen anclada, primera página sin pie. | La candidata abría con una portada de texto. |
| T-2 | Márgenes de 1,27 cm en todas las secciones. Las tablas se reescalaron al nuevo ancho útil. | La candidata tenía 2,2 / 2,0 cm. |
| T-3 | En la «Presentación», el párrafo sobre las «continuaciones prácticas» se reemplazó por la explicación de los dos componentes del área (Orientación y PEC). | Coherencia con la nueva distribución de 36 encuentros. |
| T-4 | Clase 8: se suprimió la afirmación «En 2026, el MINNA y el MITIC impulsan un proyecto de ley…». Ahora dice «En Paraguay hay servicios gratuitos de orientación…». | No está verificada; no se atribuye a organismos lo que no consta. |
| T-5 | «Continuación práctica N — » pasa a «Actividad complementaria N (opcional) — » (N = 1 a 6). | Quedan como material complementario, sin encuentro propio y sin duplicar los talleres. |
| T-6 | Las 21 fichas de clase llevan en la celda «Capacidad/Capacidades» la transcripción literal del programa MEC de 7.º. La Clase 15 tiene dos capacidades; la Clase 21 integra la 3 y la 10. | Trazabilidad. Las candidatas tenían paráfrasis. |
| T-7 | Módulo PEC reemplazado por completo (desde el título «PROYECTO EDUCATIVO COMUNITARIO» hasta el final). | Los talleres A–F de la candidata tenían unas 250 palabras cada uno y no eran trabajables en un encuentro de 3 HC. |
| T-8 | Índice regenerado con los números de página reales de esta edición: 54 entradas, verificadas contra el PDF. | El índice candidato era resumido, sin páginas. |
| T-9 | Regla N-02: se agregaron 35 bloques «Espacio para anotaciones y respuestas» con renglones donde una pieza terminaba con más del 55 % de la página libre. | Evitar páginas residuales. |

Detalle de T-7. El nuevo módulo, en el tomo, va de la pág. 62 a la 86.
- **Introducción.** Incluye el propósito del componente, citado literalmente del programa MEC, y la tabla «Cómo utilizar los talleres en el año»: taller, encuentro, mes, producto, ficha y vínculo con las clases.
- **Proyecto modelo** «Recreos que incluyen: un rincón de lectura y bienvenida».
  - Sigue los 13 apartados del esquema de proyecto, que se declara *sugerido* por el MEC y adaptable.
  - Se rotula «Caso didáctico».
  - Termina con la lista de actividades no permitidas.
- **Talleres A a F**, en los encuentros 4, 21, 23, 26, 29 y 32. Cada uno trae:
  - ficha PEC con el componente, el propósito MEC literal, la etapa y el encuentro, las capacidades del área vinculadas (literales) y los indicadores (elaboración editorial, declarada);
  - dos o tres apartados explicativos y una situación para conversar;
  - el avance del proyecto modelo, como ejemplo resuelto;
  - la secuencia de 120 min (20 + 35 + 40 + 25);
  - las actividades: consignas 1 a 3 «Pensá y respondé» y consigna 4 «En equipo»;
  - el recuadro «Para cuidarte», el registro del estudiante y el criterio de evaluación.
  - Prosa de 474 a 533 palabras por taller, sin contar tablas ni consignas.
- **Carpeta de trabajo — Fichas del PEC.** Las fichas 1 a 6 se conservan como material complementario y cada una está ligada a su taller. No suman encuentros.
- **Evaluación formativa.** Usa la escala del MEC para el PEC: L (Logrado), NL (No logrado), NM (Necesita mejorar).

Seguridad (talleres A, E y F y proyecto modelo):
- observaciones solo dentro del colegio, en horario escolar, con autorización;
- no se fotografía a personas, encuestas anónimas y voluntarias, y entrevistas a través del docente;
- sin dinero obligatorio, sin manipular instalaciones eléctricas, sin zonas de riesgo y sin traslados fuera del centro sin los procedimientos institucionales;
- ante un conflicto, avisar al docente y no intervenir.

### Plan Anual (`7mo/DPS_7mo_PLAN_ANUAL_PEC_OFICIO_2026.docx`; solo .docx)

| N.º | Cambio |
|---|---|
| PA-1 | Portada a página completa en una sección vertical propia. El cuerpo sigue en oficio horizontal. |
| PA-2 | Márgenes de 1,27 cm (antes 1,02 / 0,96 cm). Las tablas se reescalaron. |
| PA-3 | Línea de composición: 21 clases (Orientación) + 6 talleres PEC (encuentros 4, 21, 23, 26, 29 y 32) + 7 evaluaciones de unidad + 2 integradoras = 36 encuentros. Las continuaciones prácticas quedan como actividades complementarias opcionales. |
| PA-4 | Las bandas de unidad dicen «Capacidades (programa MEC): «…»» con las capacidades literales. La Unidad 5 aparece en las dos etapas. |
| PA-5 | En las seis filas PEC, «Vinculado a la unidad de Orientación correspondiente» se reemplazó por «Capacidades del área vinculadas (programa MEC): «…» Indicadores: elaboración editorial.» |

### Planes de Clase (`7mo/DPS_7mo_PLANES_DE_CLASE_PEC_OFICIO_2026.docx`; solo .docx)

| N.º | Cambio |
|---|---|
| PL-1 | Portada, y márgenes de 1,27 cm con las tablas reescaladas. |
| PL-2 | 36 fichas con rótulo según el tipo de encuentro y capacidades literales: «Capacidad/es» en las clases, «Capacidades del área vinculadas» en los talleres PEC y «Capacidades evaluadas» en las evaluaciones de unidad e integradoras. |
| PL-3 | En los talleres PEC, el objetivo pasa a decir «Objetivo del taller (elaboración editorial; el PEC no tiene capacidades propias en el programa): …». |
| PL-4 | Desarrollo 2 de cada taller remite a las consignas 1 a 3 y a la consigna 4 del tomo. Así coinciden tomo, plan y solucionario. |
| PL-5 | Se corrigieron la composición y la frase sobre los talleres que «reemplazan» las continuaciones. También se cambió «(articulado con la unidad correspondiente)» por «(componente Proyecto Educativo Comunitario)». |

### Solucionario (`7mo/DPS_7mo_SOLUCIONARIO_DOCENTE_PEC_OFICIO_2026.docx` y `.pdf`)

| N.º | Cambio |
|---|---|
| S-1 | Portada, y márgenes de 1,27 cm con las tablas reescaladas. |
| S-2 | «Continuación N» pasa a «Actividad complementaria N». El título de esa sección indica que las actividades son opcionales. |
| S-3 | El «ANEXO DOCENTE — PROYECTO EDUCATIVO COMUNITARIO» se reemplazó. Para cada taller incluye: el encuentro, la conducción, las respuestas esperadas a las consignas 1 a 4 del tomo (opción múltiple: c, a, d, b, a, c), las capacidades vinculadas y un instrumento de evaluación con la escala L / NL / NM. |
| S-4 | Las respuestas de las clases y evaluaciones de Orientación de la candidata no se tocaron. |

## 3. Lo que se preservó

- **Ilustraciones.** Las 21 imágenes del tomo candidato (Gemini) están presentes byte a byte, comprobado por SHA-256. No se regeneró, recortó ni recomprimió ninguna. La única imagen nueva es la portada.
- **Texto.** Todo el texto de las 21 clases, la prueba diagnóstica, las 7 evaluaciones de unidad y las 2 integradoras, salvo los reemplazos T-3 a T-6.
- **Fichas del PEC.** Las fichas 1 a 6 de la candidata, reubicadas en la «Carpeta de trabajo».

## 4. Controles del productor

El script es `edicion/verificar.py 7` y el resultado completo está en `verificacion/7mo/CONTROLES.md`. Dio **190 controles correctos y 0 fallos**. Se comprobó:
- exactamente seis archivos, sin PDF del Plan Anual ni de los Planes;
- oficio en todas las secciones de los cuatro .docx y en todas las páginas de los dos PDF, con márgenes de 1,27 cm;
- ningún símbolo de la lista ✓ ✗ ✅ ✔ ✘ ☑, ningún residuo de la candidata y ningún marcado sin procesar;
- cada celda de capacidad en tomo, Plan Anual y Planes es una transcripción literal del programa MEC;
- índice del tomo: 54 entradas, con la página comprobada en el PDF;
- PDF sin páginas en blanco (llenado mínimo del 12 %), y cada PDF generado del .docx entregado.

Páginas: tomo 86 (candidata: 72) y Solucionario 19 (candidata: 13). En el control interno, que no se entrega, el Plan Anual tiene 13 páginas y los Planes 39.

Hashes de entrega: `verificacion/7mo/SHA256_ENTREGA.md`.

~~Observación abierta: págs. 11, 42 y 51 casi vacías.~~ Resuelta en la versión 2 (ver sección 7).

## 5. Cómo reproducir

```
cd dps_3er_ciclo/combos_2026/edicion
python3 edit_tomo.py 7      # tomo .docx + .pdf e índice
python3 edit_docs.py 7      # Plan Anual, Planes (solo .docx) y Solucionario (.docx + .pdf)
python3 verificar.py 7      # controles
```

Fuentes del módulo PEC: `edicion/fuente_pec/pec7_tomo.md` y `pec7_sol.md`. Configuración del grado: `edicion/config_grados.py`.

## 6. Encargo para la auditoría de ChatGPT

> Auditá el combo DPS 7.º en la rama `claude/libros-5z31jx` del repositorio `FernandoAquinoBerni079/FernandoAquinoBerni079`, carpeta `dps_3er_ciclo/combos_2026/7mo/`, en el commit indicado por Claude. Compará contra tu candidata, en `dps_3er_ciclo/combos_2026/base_candidata/7mo/`, usando este informe (`INFORME_DIFERENCIAL_7mo.md`).
>
> Verificá:
> 1. Literalidad de las capacidades frente al programa MEC de 7.º, en las fichas del tomo, las bandas y filas PEC del Plan Anual y las 36 fichas de los Planes.
> 2. Que el PEC no aparezca con capacidades propias y que los indicadores estén declarados como editoriales.
> 3. Concordancia de los encuentros 4, 21, 23, 26, 29 y 32 entre tomo, Plan Anual, Planes y Solucionario. Las consignas 1 a 4 de cada taller deben tener respuesta esperada en el Solucionario.
> 4. Que las actividades complementarias no ocupen encuentro ni dupliquen talleres.
> 5. Seguridad de las actividades propuestas.
> 6. Formato oficio, márgenes, índice y paginación, y que no haya páginas residuales.
> 7. Concordancia entre Word y PDF.
> 8. Conservación de las 21 ilustraciones.
>
> Informá los hallazgos numerados con archivo, página o encuentro, y la corrección propuesta. Claude corregirá solo los hallazgos documentados.

## 7. Versión 2 (posterior al commit `e76e6e6`)

Al editar 8.º aparecieron cuatro mejoras de los scripts que también corresponden a 7.º. Se aplicaron antes de que la auditoría devolviera hallazgos. **ChatGPT debe auditar esta versión 2**, en el commit indicado por Claude.

| N.º | Cambio | Archivos |
|---|---|---|
| V2-1 | Los indicadores de las seis filas PEC del Plan Anual y de las seis fichas de taller de los Planes son ahora los mismos que los de la ficha del taller en el tomo. Antes conservaban los dos indicadores genéricos de la candidata. | Plan Anual, Planes |
| V2-2 | Las págs. 11, 42 y 51 del tomo (cierre de actividad complementaria antes de una evaluación) llevan ahora su espacio de anotaciones. En total hay 38 espacios y no queda ninguna página con menos del 30 % de llenado. | Tomo |
| V2-3 | Se quitó la portada de texto de la candidata, que quedaba repetida en la página 2 detrás de la portada de imagen. | Solucionario (19 → 18 págs.) |
| V2-4 | Se quitó el pedido de actualizar campos al abrir: la base traía dos. Los índices son estáticos y Word mostraba un aviso al abrir. | Tomo, Solucionario |

Controles de la versión 2: **232 correctos y 0 fallos**. Se agregaron controles para:
- la concordancia de indicadores PEC entre tomo, Plan Anual y Planes;
- los encuentros de los talleres en el Solucionario;
- la portada repetida;
- las páginas ocupadas solo por el espacio de anotaciones;
- los pedidos de actualizar campos.

Páginas: tomo 86 y Solucionario 18. En el control interno, el Plan Anual tiene 14 páginas.

**Nota sobre la extensión de las clases.** Las 21 clases de 7.º son más breves que las de 8.º: entre 400 y 750 palabras, frente a entre 930 y 1.590. Fernando autorizó completar y enriquecer las clases cortas. Para no cambiar el texto mientras ChatGPT audita, ese enriquecimiento se propone hacer junto con las correcciones de la auditoría, en una sola ronda.
