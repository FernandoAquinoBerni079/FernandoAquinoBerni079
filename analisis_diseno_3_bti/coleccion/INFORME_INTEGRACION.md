# Informe de integración editorial — Colección ADS 3.º BTI

> **Registro de la v0.1** (commit `43de4bc`). La versión vigente es la v0.2: ver `INFORME_CIERRE_EDITORIAL.md`.

**Análisis y Diseño de Sistemas, 3.er curso BTI · Biblioteca Comercial 2026 · 21 de octubre de 2026**

**Estado:** primer paso del cierre de la colección, para la auditoría independiente.
- No está aprobado para la venta ni para uso en aula. No se declara apto para comercialización.
- No se generaron el plan anual definitivo ni los 36 planes de clase.
- No se subió nada a Drive.
- No se modificó ningún archivo de los seis lotes ni de otras asignaturas.

## 1. Qué se entrega

| Documento (oficio O3, márgenes espejados) | DOCX (editable) y PDF (control) | Páginas |
|---|---|---|
| Libro anual del estudiante: portada, índice general, preliminares, 6 aperturas de unidad y 18 capítulos | `ADS_3BTI_LIBRO_ANUAL_ESTUDIANTE_OFICIO_O3` | 211 |
| Guía docente anual con solucionario: parte general y 6 partes (una por unidad) | `ADS_3BTI_GUIA_DOCENTE_ANUAL_OFICIO_O3` | 109 |
| Cuaderno anual de prácticas: las 16 prácticas (1 a 15 y 17), incluidas las Prácticas 1 a 3 | `ADS_3BTI_CUADERNO_ANUAL_PRACTICAS_OFICIO_O3` | 33 |

**Junto con los documentos:**
- `DIFERENCIAS.md`: la lista cerrada de diferencias con los seis lotes (17 entradas).
- `INVENTARIO.md`: inventario provisional de fuentes, versiones, commits, referencias de código y pendientes.
- `EVALUACION_ENCUADERNACION.md`: grosor y encuadernación, tomo anual o dos volúmenes.
- Resultados de los verificadores: `EQUIVALENCIA.json`, `CONTROLES_IMPRESION.json`, `COHERENCIA.json`, `PRUEBA_FUENTES.json` y `resultado_construccion.json`.
- `revision_visual/`: 22 láminas de revisión.
- `MANIFIESTO_COLECCION.json`: manifiesto SHA-256.
- `build/`: el armado y los controles, que se pueden volver a correr.

## 2. Cómo se armó

**Sin copiar ni reescribir capítulos.** `build/fuentes.py` carga los constructores aprobados de los seis lotes, cada uno con su propio espacio de nombres:
- los seis se llaman `construir`;
- los lotes 1 y 2 comparten además los nombres `guia` y `diagramas`.

Con esos constructores se arman los tres documentos:
- **Libro.** Cada capítulo se arma con la función `capituloN` de su lote, y cada unidad con su `apertura_unidad`. Los preliminares salen del lote 1.
- **Guía.** Cada parte se arma con la función `construir` de la guía de su lote, dentro del mismo documento. Se omite la portada de cada lote.
- **Cuaderno.** Cada práctica se arma con la función `practica` de los lotes.

**Versiones que se usan:**
- lote 1: candidata O3 (las funciones del lote 1 con el perfil O3);
- lote 2: v1.0;
- lote 3: v1.1;
- lote 4: v1.1;
- lote 5: v1.0;
- lote 6: v1.1.

**Figuras, código y datos:**
- Las figuras se generan con los scripts de cada lote en `coleccion/build/figs/`, nunca dentro de los lotes. Las 58 coinciden byte a byte con las de los lotes.
- Los bloques de código se leen de los archivos del proyecto.
- Los resultados de las pruebas se leen de `resultados_pruebas/` de cada lote.

**El ciclo de armado es el de los lotes:**
1. índice recalculado sobre el PDF hasta que la paginación queda estable;
2. control de filas: toda tabla que pierde una fila pasa a hoja nueva.

En el armado anual ninguna tabla perdió filas.

## 3. Equivalencia con los seis lotes

Cada capítulo, cada parte de la guía y cada práctica se comparó con su versión aprobada, párrafo por párrafo y tabla por tabla. Se compararon:
- el texto, el estilo y el formato de cada tramo;
- cada celda, los anchos de columna y el sombreado;
- los píxeles y el tamaño de cada imagen.

| Comparación | Segmentos | Resultado |
|---|---|---|
| Libro: preliminares, 6 aperturas y 18 capítulos, con el documento aprobado de su lote | 25 | 25 iguales; solo aparecen los reemplazos de la lista cerrada |
| Guía: cada parte con la guía aprobada de su lote | 6 | 6 iguales; solo cambian el título de la parte, las notas de las Partes V y VI y la página del diagnóstico |
| Cuaderno: cada práctica con la del libro anual y con su versión aprobada | 16 | 16 iguales en las dos comparaciones |

**Diferencias autorizadas** (detalle en `DIFERENCIAS.md`):
- **Portada, índice y paginación.**
  - Una sola portada por documento y un índice general.
  - Paginación continua.
  - El encadenado de tablas largas de los lotes 3 a 6 se aplica también a las Unidades I y II.
- **Remisiones y referencias editoriales del libro.** Siete reemplazos exactos, con su cantidad controlada:
  - la frase de alcance de la presentación («Esta edición de control contiene… la Unidad I» pasa a «Este tomo anual contiene… las seis unidades»);
  - seis menciones a «lote» que pasan a nombrar la unidad, por ejemplo «prototipo del lote 4» → «prototipo de la Unidad IV».
- **Guía.**
  - La parte general (texto nuevo).
  - El título de cada parte.
  - Dos notas de integración:
    - Parte V: preparación del Encuentro 30 y conjunto reservado, las observaciones de la auditoría del lote 5;
    - Parte VI: código recibido de otros.
  - La página del diagnóstico de entrada en la Parte I, que ahora es la del libro anual.
- **Índice.** Sigue el orden real de los títulos. En el índice del lote 1, la sección 3.3 figuraba bajo el Encuentro 6, aunque está en el Encuentro 5.

No cambió ninguna teoría, ejemplo, práctica, consigna, evaluación, puntaje, indicador ni solución.

## 4. Control de calidad del tomo (todas las páginas)

| Control (sobre las 353 páginas de los tres documentos) | Resultado |
|---|---|
| Filas de tablas impresas | Libro 212 tablas y 1388 filas · guía 263 y 1696 · cuaderno 37 y 208: todas impresas |
| Tablas repartidas entre páginas | 9 en el libro y 17 en la guía, con todas sus filas y el encabezado repetido; ninguna deja menos de dos filas en una página |
| Párrafos impresos y palabras de celda enteras | Sin faltantes ni palabras partidas |
| Figuras y epígrafes | 29 figuras, cada una impresa una vez, con su imagen encima de su epígrafe en la misma página |
| Código fuente | 20 bloques del libro (181 líneas) y 9 de la guía (152 líneas): enteros, en la página de su rótulo y su ficha, dentro de los márgenes |
| Índice y referencias | 180, 58 y 22 entradas, cada una en su página y en orden; los 51 instrumentos de la guía, en la página que indica la tabla |
| Paginación continua | «Página X de Y» correcta en las 353 páginas |
| Márgenes espejados | Medidos en todas las páginas con texto: impares con el interior a la izquierda y pares a la derecha |
| Hojas en blanco accidentales | Ninguna |
| Legibilidad | Ningún texto por debajo de 7,5 pt; ningún renglón de respuesta suelto; las 17 evaluaciones, cada una en página propia |
| Tres fuentes de sustitución (Carlito, Liberation Sans, DejaVu Sans) | 9 de 9 combinaciones sin hojas en blanco ni renglones sueltos |

**Coherencia de la colección** (42 controles, 0 fallos):
- **Lotes intactos.** Los seis lotes, sus planes, el plan anual y los planes de clase no cambiaron, ni ninguna otra asignatura. Coinciden todos los archivos de los manifiestos:
  - lote 1: 60;
  - candidata O3: 27;
  - lote 2: 62;
  - lote 3: 134;
  - lote 4: 187;
  - lote 5: 171;
  - lote 6: 214.
- **Referencias cruzadas.** Todas existen en el libro con su número: 229 citas del libro, 211 de la guía y 9 del cuaderno a tablas, figuras, códigos y ejemplos resueltos.
- **Evaluaciones.**
  - Hay 17, con semillas únicas y 15 puntos cada una.
  - La guía trae la clave de cada uno de los 153 ítems, con la misma letra que el libro.
  - El Capítulo 18 no tiene evaluación escrita, y los Capítulos 16 y 18 no tienen práctica.
- **Prototipo.**
  - Existen las 33 rutas de archivos citadas.
  - Los 29 bloques de código se leen de archivos que existen.
  - Las herramientas de inspección estática y de ejecución controlada del lote 6 v1.1 se conservan sin cambios.
- **Rótulos.**
  - Ninguna capacidad se presenta como oficial del MEC.
  - Nada se declara validado en aulas.
  - Windows y los equipos escolares figuran como pendientes en los tres documentos.
  - La licencia figura como pendiente de revisión jurídica.
- **Reservados.** Con las rutas privadas, se comprobó que ninguno de los 22 códigos de DR ni de las 12 variantes V6 aparece en los documentos ni en `coleccion/`.

## 5. Seguridad y archivos reservados

**Herramientas de prueba.**
- Las herramientas del lote 6 v1.1 se conservan como estaban, en `lote_6/proyecto/herramientas/`.
- La guía anual dice dos veces (parte general, sección 3, y nota de la Parte VI) que:
  - las pruebas funcionales de código recibido requieren una máquina virtual o un equipo verdaderamente aislado, sin datos institucionales ni de personas, sin red y con una cuenta sin permisos de administrador;
  - la lista cerrada de nombres de pruebas no vuelve confiable su código.

**Datos reservados.** DR y V6 siguen fuera de GitHub, del libro, del cuaderno, de la guía y de los paquetes públicos.

**Siguen pendientes:**
- Windows y los equipos escolares;
- la revisión jurídica del borrador de licencia.

## 6. Grosor y encuadernación (detalle en `EVALUACION_ENCUADERNACION.md`)

**El libro.** Tiene 211 páginas (106 hojas):
- su lomo es de unos 11 a 13 mm, según el papel;
- pesa unos 640 g con papel de 80 g.

**Recomendación técnica: mantener el tomo anual,** en rústica fresada con cola PUR o en anillado. El grosor no obliga a dividirlo.

**Dos volúmenes por etapa (corte en el H3).** Quedarían de unas 123 y 92 páginas. Implicarían:
- otra portada, otro índice y otra tapa;
- rehacer las remisiones de página de la guía.

No se dividió nada.

**El cuaderno** conviene anillado, para que abra plano.

## 7. Observaciones para decidir (no se cambiaron)

Están en textos aprobados. Por la regla de integración no se tocaron: las informo para que decidas.

1. **Presentación (lote 1).**
   - Dice: «organizados en seis unidades de tres capítulos».
   - La Unidad IV tiene cuatro capítulos y la VI, dos.
   - Propuesta: «seis unidades de dos a cuatro capítulos (18 en total)».
2. **«Cómo usar el libro» (lote 1).**
   - Dice que cada capítulo tiene una práctica y, al final, una evaluación opcional.
   - Los Capítulos 16 y 18 no tienen práctica, y el 18 no tiene evaluación (decisiones D-3 y D-4).
   - Propuesta: agregar «salvo los Capítulos 16 y 18, que cierran con sus hitos».
3. **Fichas de los bloques de código.**
   - Las del lote 4 nombran el archivo desde la carpeta del proyecto (`referencia_docente/public/lectores.php`).
   - Las de los lotes 5 y 6 lo nombran desde la raíz (`lote_5/proyecto/…`).
   - Las dos formas son correctas; se podría unificar la notación.
4. **Inicio de las unidades.** Empiezan en la página siguiente a la anterior, como en los lotes. Si la imprenta prefiere que empiecen en página impar, se agregarían hasta 6 páginas en blanco intencionales.
5. **Guía anual.**
   - Cada parte conserva su recuadro «Sobre las capacidades» y su tabla de 28 encuentros.
   - No hay una tabla única del calendario de 28 encuentros para todo el año. La propuse en la estrategia de cierre, pero sería texto nuevo.
   - Puede ir con el plan anual definitivo, si la aprobás.

## 8. Cómo reproducir

Desde `analisis_diseno_3_bti/`:

```
python3 -B coleccion/build/armar_coleccion.py        # los tres documentos (unos 3 minutos)
python3 -B coleccion/build/equivalencia.py           # comparación con los seis lotes
python3 -B coleccion/build/controles.py              # auditoría de impresión de todas las páginas
ADS_V6=<ruta privada>/variantes_v6.json ADS_DR=<ruta privada>/dr.json python3 -B coleccion/build/coherencia.py
python3 -B coleccion/build/prueba_fuentes_coleccion.py
python3 -B coleccion/build/laminas.py
python3 -B coleccion/build/encuadernacion.py
python3 -B coleccion/build/informes.py
python3 -B coleccion/build/manifiesto_coleccion.py
```

Entorno de construcción:
- Linux, Python 3, python-docx, LibreOffice y PyMuPDF.
- Las pruebas del prototipo que se citan son las de los lotes, con su entorno registrado.

## 9. Próximo paso

El trabajo se detiene acá, para la auditoría independiente. Si se aprueba esta integración y las observaciones del punto 7, siguen:
1. el plan anual definitivo;
2. los 36 planes de clase.
