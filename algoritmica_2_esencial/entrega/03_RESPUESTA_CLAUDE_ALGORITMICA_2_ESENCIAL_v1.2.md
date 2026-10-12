# 03_RESPUESTA_CLAUDE_ALGORITMICA_2_ESENCIAL_v1.2

**Respuesta del constructor al Informe 02 del compendio** (`auditorias/COMPENDIO_AUDITORIAS_ALGORITMICA_1_2_3_ESENCIAL_2026.md`, auditoría de la v1.1 del 11/10/2026) · Protocolo v0.4, §3, paso 5

Algorítmica · 2.º Curso BTI · Edición Esencial Comercial 2026 · versión corregida **v1.2** (12/10/2026)

**Estado: corregido. Vuelve a ChatGPT para la reauditoría (paso 4).** No se declara listo para la venta: la aprobación comercial es exclusiva de Fer.

## Resumen

La v1.2 atiende los ocho hallazgos del informe: seis MAYORES y dos MENORES. No hubo hallazgos críticos.

- La entrega está en una carpeta nueva, `algoritmica_2_esencial/salida_v1_2/`.
- La v1.1 queda intacta en `algoritmica_2_esencial/salida/` como base de comparación. No se modificó, renombró ni borró ningún archivo maestro.
- Se regeneró todo con `build/`.
- No cambió el contenido curricular: capacidades MEC, indicadores, 21 clases, 21 prácticas, 36 encuentros, ubicación de las evaluaciones, pesos de la rúbrica y figuras.

**Páginas por documento (v1.1 → v1.2):**

| Documento | v1.1 | v1.2 |
|---|---|---|
| Libro | 127 | 113 |
| Solucionario | 19 | 18 |
| Plan Anual | 8 | 7 |
| Planes de Clase | 65 | 38 |
| Muestra | 17 | 15 |
| **Total** | **236** | **191** |

**Ubicación y control de versión**

- La rama de trabajo de esta sesión es `claude/zen-meitner-kes7dg`. Se unió con `claude/libros-5z31jx` en el commit `5ce7e24` y contiene todo su historial.
- Las correcciones están en el commit `e760ea8`.
- El reporte de QA se generó sobre el commit `673a5b7`, con el árbol limpio.

## 1. Hallazgos y qué se hizo

| N.º | Gravedad | Hallazgo | Qué se hizo en la v1.2 | Dónde |
|---|---|---|---|---|
| 01 | MAYOR | Planes: 27 continuaciones casi vacías | Cada uno de los 36 planes entra en una sola hoja oficio, con momentos, recursos, evaluación, observaciones y firmas. La letra se mantiene en 9,5 pt, el mínimo de la norma de Planes de Clase. No se quitó contenido. Para ganar espacio:<br>• Las celdas pasan a interlineado sencillo (antes 1,15).<br>• Los márgenes internos de celda bajan de 2 a 1,5 pt.<br>• Los separadores entre tablas miden 2 pt.<br>• Observaciones y firmas quedan en un único bloque sin bordes al pie del plan.<br>Ninguna hoja queda solo con firmas. Ocupación por hoja: entre 73 % y 94 %. | Planes de Clase: pp. 3–38. Índice regenerado y verificado contra el PDF. |
| 02 | MAYOR | Libro: 17 páginas interiores casi vacías | Ajuste por sección, medido en el PDF y en tres niveles. El tamaño de letra no cambia en ninguno:<br>1. **Compacto:** interlineado sencillo y figuras al 90 %. Se aplicó a 15 secciones.<br>2. **Compacto 2:** espaciados de 2 pt como máximo. Se usa solo si la sección siguiente no puede subir. Se aplicó a la Práctica 18, la Práctica 21 y el PFI.<br>3. **Compacto 3:** figuras al 80 %. Se aplicó solo al PFI, que no puede subir porque lo precede la Integradora.<br>Cuando con el nivel 1 no alcanzaba, la Clase o la Práctica siguiente empieza en la misma hoja, con su título y contenido (Clases 10, 14, 18 y 21; Prácticas 9, 11, 19 y 21). Las evaluaciones siguen empezando en hoja propia, igual que el PFI. La lista de ajustes la calcula el propio build y queda en `build/ajustes_paginacion.json`.<br>En las evaluaciones, los ítems que piden escribir un algoritmo, un procedimiento, un ordenamiento, una consulta o una prueba de escritorio tienen 6 renglones en lugar de 3. Así la segunda hoja de cada evaluación tiene espacio real de respuesta, no un remanente. | Libro (113 págs.). Ocupación mínima de una hoja interior: 33 %. |
| 03 | MAYOR | Plan Anual: p. 8 solo con firmas | Los criterios generales y las estrategias de inclusión pasan a dos columnas. Las firmas («Firma del docente: ____» y «Dirección — Visto bueno: ____») van en la misma tabla de cierre, al pie de la última hoja de la tabla anual. La p. 8 se eliminó. Los 36 encuentros están completos. | Plan Anual, p. 7 de 7 |
| 04 | MAYOR | Muestra con hoja residual y díptico incompleto | La Muestra se rearmó con documentos íntegros:<br>• Portada, presentación, índice y prueba diagnóstica.<br>• Unidad 1: Clase 1 y Práctica 1 completas. La Práctica 1, con su desafío final, ahora entra en una hoja.<br>• Contraportada y portada del solucionario, sin claves.<br>• Portada y primera hoja de la tabla del Plan Anual.<br>• Portada y Plan de Clase N.º 1 íntegro, en una hoja y con firmas.<br>El build controla que no haya hojas casi vacías ni las palabras «Clave», «Resultado esperado» u «Opción correcta». | Muestra (15 págs.) |
| 05 | MAYOR | U4 e Integradora 2 con la misma tabla Insumos | Se aplicó la sustitución propuesta solo en la Integradora 2. Registros nuevos:<br>• HEL-11 Yogur 11.000 lácteo 28<br>• HEL-12 Queso 16.000 lácteo 8<br>• HEL-13 Harina 6.000 seco 35<br>• HEL-14 Galleta 14.000 seco 11<br>• HEL-15 Mango 12.000 fruta 16<br>• HEL-16 Naranja 5.000 fruta 22<br>El ítem 6 pasa de Azúcar a Harina y el ítem 9, de Cacao a Queso. La Evaluación U4 no cambia. Claves nuevas, recalculadas por script:<br>• Stock total: 120.<br>• Menos de 15: Queso y Galleta.<br>• Por categoría: lácteo 36, seco 46, fruta 38 (suma 120).<br>• Selección descendente de precios: [16.000, 14.000, 12.000, 11.000, 6.000, 5.000]; queda primero el Queso.<br>• ValorStock: Harina 210.000 y Queso 128.000.<br>Ningún resultado aparece en el libro. | Libro, pp. 109–110 · Solucionario, p. 17 (clave E2) |
| 06 | MAYOR | Access 2016 sin advertencia de fin de soporte | Se agregó la advertencia en tres lugares:<br>• Libro, Clase 19 (texto general).<br>• Libro, Prácticas 19, 20 y 21 (versión breve que conserva la alternativa en papel).<br>• Solucionario, p. 2.<br>Dice que Access 2016 en castellano es la referencia de las rutas, que su soporte finalizó en octubre de 2025, y que para 2026 se recomienda Access para Microsoft 365 o Access 2024 con licencia y soporte vigentes, comprobando las rutas y el separador de expresiones según la configuración regional. **Diferencia con el texto propuesto:** no se escribió «se verificaron históricamente con Access 2016», porque los procedimientos de Access no se ejecutaron en el programa (las notas v1.1 lo declaran). Afirmarlo sería falso. | Libro, pp. 95, 97, 102 y 106 · Solucionario, p. 2 |
| 07 | MENOR | Nombres de la planificación | Ahora se llaman `Algoritmica_2do_Curso_PLAN_ANUAL_COMERCIAL_2026` y `Algoritmica_2do_Curso_PLANES_DE_CLASE_COMERCIAL_2026` (.docx y .pdf). Los maestros de `salida/` no se renombraron. La identidad editorial con una edición Completa sigue sin acreditarse: queda como decisión de Fer (ver §3). | `salida_v1_2/` |
| 08 | MENOR | Reporte de QA sin versión inequívoca y sin alertas de maquetación | `build/auditoria_resultado.txt` ahora incluye:<br>• **Identificación:** versión v1.2, commit `673a5b7`, rama, aviso si el árbol tiene cambios sin commit, y huella SHA-256 de los 9 archivos.<br>• **Dos partes separadas:** 1) comprobación automática y 2) revisión visual, con la advertencia de que 0 fallos automáticos no equivale a APTO editorial.<br>• **Bloques nuevos:**<br>– K: hojas casi vacías en los cinco PDF, hojas solo de firmas, un plan por hoja y cierre del Plan Anual.<br>– L: independencia de los datos entre evaluaciones y recálculo de la Integradora 2.<br>– M: Access 2016.<br>– N: nombres.<br>Resultado: 894 controles, 0 fallos. Antes de usarlos, los controles nuevos se probaron contra la v1.1: detectan las 27 hojas de Planes, la p. 8 del Plan Anual, las pp. 10 y 17 de la Muestra, la tabla repetida y las hojas del Libro (ver §2). | `build/auditoria_resultado.txt` |

## 2. Más allá del informe

- **Solucionario, p. 4.** La diagnóstica ocupaba un quinto de hoja y la Primera parte arrancaba en hoja nueva, así que ahora sigue en la misma hoja (19 → 18 págs.). El informe no lo señalaba; lo detectó el control K.
- **Medición del Libro.** Con el control K, la v1.1 tiene 20 hojas interiores bajo el 30 %: las 17 del informe más las pp. 49, 59 y 107. Las 20 quedaron resueltas.
- **Build portable.** El build ya no depende de `/home/claude/` y se reconstruye desde el repositorio:
  - `build/rutas.py` define las rutas y la carpeta de salida (variable `SALIDA`).
  - `build/plantilla_base.docx` reemplaza la plantilla de 3.º, que no estaba en el repositorio.
  - `pseint/run.sh` acepta `PSEINT_DIR`.
  - `build/ocupacion.py` mide las hojas.
  - Se comprobó que el build reproduce la v1.1 página por página (127/19/8/65/17) antes de tocar nada.
- **PSeInt.** En esta sesión se re-ejecutaron los programas de las prácticas con PSeInt 20250314 para Linux, perfil Flexible: 69 controles del bloque C, 0 fallos. Ningún `.psc` cambió.

## 3. Lo que queda abierto

- **Paginación en Word.** La ocupación se mide sobre el PDF de LibreOffice. En Word, el plan más cargado ocupa 94 % de su hoja, así que hay margen, pero conviene abrir los DOCX en Word y confirmar que ningún plan pasa a dos hojas.
- **Access y Windows.** No se probaron en un equipo con Access ni con Windows. Siguen pendientes de comprobación manual las mismas tareas que en la v1.1:
  - rótulos de la fila Total y del asistente de referencias cruzadas;
  - aceptación de `SiInm(…;…;…)` con punto y coma según la configuración regional;
  - comportamiento del Explorador de archivos y del Bloc de notas.
- **Decisión de Fer (hallazgo 07):** confirmar si el Plan Anual y los Planes de Clase se comparten con una edición Completa de Algorítmica 2.º. Si no existe esa edición, el nombre sin «ESENCIAL» igual sigue la regla §3bis, pero conviene registrarlo.

**Estado final: corregido y listo para reauditoría independiente. No aprobado para la venta.**
