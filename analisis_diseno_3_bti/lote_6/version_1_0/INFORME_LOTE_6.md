# Lote 6 — Unidad VI (Capítulos 17 y 18), versión 1.0

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · 21 de octubre de 2026**

**Estado:** lote para la última auditoría individual, antes del armado de la colección. No está aprobado para la venta ni para uso en aula, y no está validado en laboratorios escolares. El borrador de licencia no cierra el aspecto jurídico.

**Límites respetados:**
- No se modificaron los lotes 1 a 5 ni los planes de los lotes 5 y 6. El verificador lo comprueba con git y con los manifiestos SHA-256 de los lotes 3, 4 y 5.
- No se armó el tomo anual ni se generaron los 36 planes de clase.
- No se subió nada a Drive.
- Los datos reservados DR y las variantes reservadas V6 no están en el repositorio.

**Próximo paso:** el lote se detiene acá para la auditoría independiente. La estrategia de cierre está aprobada, pero no autorizada para ejecutarse.

## 1. Qué se entrega

| Documento | Páginas (oficio O3) | Estimación del plan |
|---|---|---|
| Libro del estudiante (`ADS_3BTI_LOTE6_ESTUDIANTE_OFICIO_O3`) | 20 | 26 a 34 |
| Guía docente con solucionario (`ADS_3BTI_LOTE6_GUIA_DOCENTE_OFICIO_O3`) | 15 | 18 a 24 |
| Cuaderno de prácticas (`ADS_3BTI_LOTE6_CUADERNO_PRACTICAS_OFICIO_O3`) | 3 | 3 a 6 |

Cada documento está en DOCX (el entregable) y en PDF (para control).

El libro y la guía quedaron por debajo de la estimación, y no se rellenaron para alcanzarla:
- son dos capítulos;
- el 18 no tiene práctica ni prueba escrita (decisiones D-3 y D-4);
- buena parte del material del 17 son tablas que salen de los documentos del paquete.

**Proyecto (`lote_6/proyecto/`):**
- **`paquete_entrega_modelo/`:** copia nueva de la referencia v2 con SC-02 del lote 5 (D-1).
  - El código es idéntico, archivo por archivo.
  - Se agregan `LEEME.txt`, `ENTREGA/` y el comprobador. `ENTREGA/` tiene la guía de instalación, el manual por tareas, los límites, la ficha de procedencia, el borrador de licencia, el acta y la lista de entrega.
- **`paquete_mbokaja/`:** el paquete del voluntario de la Práctica 17, con cinco defectos introducidos a propósito y comprobables.
- **`comprobar_entrega.php`:** comprobador de entrega (90 líneas de código, seis bloques A a F). Los estudiantes lo usan con su propio paquete.

**Instrumentos:**
- rúbrica del H6 (seis criterios, cuatro niveles);
- guion de demostración;
- rúbrica de defensa individual;
- rúbrica de producto final con la ponderación de Work §4.3;
- preguntas de transferencia;
- fichas de recuperación FR-1 a FR-4;
- planilla anual H1 a H6;
- registro de retrospectiva;
- planilla de tiempos del Encuentro 35, en `lote_6/instrumentos/planilla_tiempos_encuentro_35.xlsx`, con fórmulas.

**Otros archivos:**
- resultados de las pruebas con su entorno (`resultados_pruebas/`, 15 archivos y `resumen.json`);
- láminas de revisión (`revision_visual/`, 15);
- controles (`verificacion_resultado.json`, `CONTROLES_FINALES.json`, `prueba_fuentes_resultado.json`);
- este informe y `MANIFIESTO_LOTE_6.json`.

**Plan anual preliminar:**
- Se regeneró con los indicadores de las fichas de los Capítulos 17 y 18.
- Los 36 encuentros tienen ahora sus indicadores leídos de las fichas, y ninguno queda pendiente.
- `lote_6/build/tomo.py` lista los 18 capítulos con su fuente.

## 2. Cómo se aplicaron las decisiones

**D-1. Versión del equipo modelo.**
- El paquete es una copia nueva de `lote_5/proyecto/referencia_docente_v2_sc02/`, y los originales, sus diferencias y su regresión no se tocaron.
- La regresión completa de la versión empaquetada da 9 de 9 pruebas sin fallos (contratos 93/93, HTTP 32/32, IN-02 7/7, etc.).

**D-2. Licencias.**
- **Borrador de uso educativo institucional:**
  - derechos reservados a los titulares;
  - autorización para instalar, ejecutar, estudiar y modificar dentro de la institución adquirente;
  - sin redistribución comercial.
- Se declara borrador en el paquete, en el libro y en la guía. El aspecto jurídico no se declara cerrado.
- **Ficha de procedencia:** separa el código propio, los datos ficticios, la documentación y los componentes de terceros.
- **Licencias de terceros:** se verificaron con su fuente primaria y para la versión exacta del entorno de las pruebas, con fecha de consulta 21/10/2026:
  - PHP 8.3.6: «The PHP License, version 3.01», archivo LICENSE de php-src, etiqueta php-8.3.6;
  - SQLite 3.45.1: dedicado al dominio público, LICENSE.md de la etiqueta version-3.45.1 y sqlite.org/copyright.html;
  - curl 8.5.0: su «COPYRIGHT AND PERMISSION NOTICE», archivo COPYING de la etiqueta curl-8_5_0;
  - bash 5.2.21: «License GPLv3+», según el propio programa.
- Ninguno de ellos se redistribuye en el paquete.
- La ficha no atribuye a la editorial código ajeno ni código de los estudiantes. Lo dice expresamente, y el verificador lo comprueba.
- El sitio sqlite.org no respondió desde el contenedor. La página de copyright se confirmó por un buscador web y el texto del LICENSE.md, en el repositorio oficial de la etiqueta. Si querés una copia archivada de cada fuente, la puedo agregar en el cierre.

**D-3. Evaluaciones.**
- El Capítulo 17 tiene su evaluación opcional de 15 puntos, con un texto base nuevo (ludoteca escolar, LU-1 a LU-4) y claves repartidas entre a, b y c.
- El Capítulo 18 no tiene prueba escrita. Sus instrumentos son:
  - la demostración (guion);
  - la defensa individual (rúbrica y planilla);
  - la evaluación integradora: H6, rúbrica de producto final y defensa.

**D-4. Práctica 18.**
- No hay práctica independiente.
- La Práctica 17 y el H6 se hicieron según el plan.

**D-5. Encuentro 35.**
- La planilla calcula con un solo evaluador. Datos de entrada:
  - equipos y estudiantes;
  - minutos de la HC, que no se suponen;
  - minutos por demostración, por cambio y por defensa;
  - recuperaciones previstas.
- **Qué dice:**
  - alternativa A: todo entra en el Encuentro 35;
  - alternativa B: cuántas defensas pasan al 36, antes que las recuperaciones;
  - alternativa B+: cuántos minutos necesitan tiempo institucional autorizado.
- No se elimina ninguna evidencia obligatoria y no se suponen horas extraordinarias.
- **Comprobación:** no hay LibreOffice Calc en el contenedor, así que las fórmulas del XLSX se recalcularon con un evaluador independiente (pycel, instalado solo para esta comprobación). Coinciden con el cálculo de la guía en tres casos, que ejercitan A, B y B+.
- La guía trae además la lista de preparación anticipada del Encuentro 35 (variantes impresas, planillas, paquetes instalados y orden), como pidió la auditoría para el Encuentro 30.

**D-6. Anexos.**
- Se construyeron solo la ficha de procedencia y la lista de entrega, que son documentos del paquete.
- Los demás anexos quedan para el cierre.

## 3. Precauciones adicionales

**Instalación por otro equipo.**
- Como evidencia de C10 se exige la instalación por un equipo distinto, sin ayuda:
  - el equipo autor se retira;
  - el docente observa y no ayuda;
  - el acta registra las condiciones reales.
- La guía del paquete modelo, seguida por un proceso nuevo en una carpeta limpia (8 de 8 pasos), se rotula como «comprobación técnica». Se dice en todos los documentos que no reemplaza a una persona ajena al desarrollo.
- En la tabla del libro, la instalación por otro equipo figura como «Pendiente hasta el acta».

**Pruebas que siguen pendientes:** Windows, laboratorios escolares, instalación por otro equipo y concurrencia real. Figuran en el libro, en la guía y en `ENTREGA/LIMITES.md` del paquete.

**Datos y condiciones de cada prueba.**
- Los datos son ficticios.
- Cada archivo de resultados tiene su línea de entorno y su condición.

**Variantes V6.**
- El repositorio tiene solo la plantilla, un validador y tres ejemplos públicos (V6-E1 a V6-E3), rotulados «no se usan en la defensa».
- El validador se niega a leer un banco que esté dentro del repositorio y revisa que ninguna variante repita un ejemplo público ni un texto del repositorio.
- El banco definitivo, de 12 variantes, está fuera del repositorio, en `/home/user/ADS_LOTE6_RESERVADO_DOCENTE/`, y se entrega por separado.
- Con `ADS_V6` y `ADS_DR`, el verificador comprueba que ningún texto reservado esté en el repositorio ni en los documentos.

**Tiempo.** Se mantienen las 20 HC y la recuperación no supone horas extraordinarias.

## 4. Cómo se comprobó la reproducibilidad

| Prueba (en el entorno de construcción) | Resultado |
|---|---|
| Código del paquete modelo frente a la referencia v2 con SC-02 | Idéntico (solo cambian `LEEME.txt`, `ENTREGA/` y el comprobador) |
| Comprobador sobre el paquete modelo | 0 incoherencias |
| Comprobador sobre el paquete de Mbokaja | Exactamente las 6 incoherencias de la clave (5 defectos: DM-1 a DM-5) |
| Comprobador sobre Mbokaja con la clave aplicada | 0 incoherencias |
| Guía como prueba: paquete modelo | 8 de 8 pasos |
| Guía como prueba: Mbokaja corregido | 8 de 8 pasos |
| Guía como prueba: Mbokaja con defectos | 4 de 8 (no se puede instalar, como corresponde) |
| Regresión de la versión empaquetada | 9 de 9 pruebas sin fallos |

**Entorno:** Linux 6.18.44-fc-v140 (x86_64), PHP 8.3.6, SQLite 3.45.1, curl 8.5.0, GNU bash 5.2.21, en un contenedor de construcción. No es una computadora escolar ni Windows.

**Dos fallas encontradas y corregidas durante la construcción:**
1. La función que aplica la clave de Mbokaja vaciaba los archivos, porque los abría para escribir antes de leerlos.
2. El comprobador aceptaba como buena una prueba vacía. Ahora exige la línea «Resultado:».

Las dos se detectaron porque la ejecución real no coincidió con lo esperado.

## 5. Controles

| Control | Resultado |
|---|---|
| `build/verificar.py` (con `ADS_V6` y `ADS_DR`) | 158 correctos, 0 fallos |
| `build/controles_finales.py` | 21 controles, 0 fallos |
| `build/prueba_fuentes.py` | 9 combinaciones, 0 fallos |
| `build/planilla_tiempos.py` | 3 casos, 11 de 11 resultados coinciden en cada uno |
| `build/tomo.py` | 18 de 18 capítulos con su fuente |
| `plan_anual/plan_anual_preliminar.py` | Controles correctos; 36 encuentros, 180 HC |

**Cómo reproducir**, desde `analisis_diseno_3_bti/`:

```
python3 -B lote_6/build/reproducir.py          # arma los paquetes y corre las pruebas sobre copias (unos 2 minutos)
python3 -B lote_6/build/construir.py
ADS_V6=<ruta privada>/variantes_v6.json ADS_DR=<ruta privada>/dr.json python3 -B lote_6/build/verificar.py
python3 -B lote_6/build/controles_finales.py
python3 -B lote_6/build/prueba_fuentes.py
python3 -B lote_6/build/planilla_tiempos.py    # requiere pycel para recalcular la planilla
```

## 6. Para la auditoría

Te sugiero revisar estos puntos:
1. **El borrador de licencia:** redacción, alcance y la exclusión del código de los estudiantes. No es un texto jurídico.
2. **Los cinco defectos del paquete de Mbokaja:** si son adecuados para el nivel del curso. Uno de ellos (DM-3) solo aparece al ejecutar el comprobador.
3. **La planilla de tiempos:** si el orden de prioridad de la alternativa B (defensas antes que recuperaciones) es el que querés.
4. **La extensión del libro (20 págs.) y de la guía (15 págs.):** si alcanza o si conviene ampliar alguna sección. No se amplió para llegar a la estimación.
5. **El banco V6 reservado:** si querés reemplazar o agregar variantes antes de usarlo.
