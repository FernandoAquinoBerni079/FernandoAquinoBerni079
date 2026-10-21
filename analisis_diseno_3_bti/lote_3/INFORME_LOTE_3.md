# Lote editorial 3 — Unidad III (Capítulos 7, 8 y 9) en oficio O3

**Análisis y Diseño de Sistemas, 3.º BTI · Biblioteca Comercial 2026 · 21 de octubre de 2026**

> **Versión vigente: 1.1.** Este informe describe la versión 1.0 (commit `f1c8bbf`), conservada en `version_1_0/`. Las dos correcciones del cierre de auditoría (acceso a PT-09, y ME-12 frente a ME-13) y sus resultados están en `INFORME_CORRECCIONES_v1_1.md`.

**Estado:** lote para auditoría independiente.
- No está aprobado para la venta ni para uso en aula.
- La aprobación comercial la hace Fernando sobre el conjunto completo.
- Las pruebas reales de instalación en equipos escolares siguen pendientes.

**Base:**
- plan del lote 3 aprobado por Fernando (`lote_3_plan/PLAN_LOTE_3_UNIDAD_III.md`, commit `f5151f5`);
- sus decisiones del 20-oct-2026, sin cambios.

**Lo que no se hizo, por los límites de la autorización:**
- la Unidad IV y los Capítulos 10 a 18;
- los planes de clase;
- la subida de maestros a Drive.

**Lotes 1 y 2:** no se modificó ningún archivo. El control Q del verificador lo comprueba con `git status`.

## 1. Entregables

| Archivo | Págs. | Contenido |
|---|---:|---|
| `ADS_3BTI_LOTE3_ESTUDIANTE_OFICIO_O3.docx` y `.pdf` | 35 | Apertura de la Unidad III; Capítulos 7, 8 y 9; Prácticas 7 a 9; H3; tres evaluaciones opcionales |
| `ADS_3BTI_LOTE3_GUIA_DOCENTE_OFICIO_O3.docx` y `.pdf` | 16 | Material docente completo (detalle debajo) |
| `ADS_3BTI_LOTE3_CUADERNO_PRACTICAS_OFICIO_O3.docx` y `.pdf` | 7 | Prácticas 7, 8 y 9, desde la misma fuente |

**Contenido de la guía docente:**
- acuerdo con Algorítmica 3.º antes del Encuentro 13 (rutas A y B de Work §3);
- secuencia en HC de cada encuentro, con las categorías de Work §5.2;
- claves de todas las actividades, prácticas y evaluaciones, con criterios de los ítems abiertos;
- listas de cotejo, leyendas de notación y errores frecuentes;
- tarjetas de rol del Encuentro 16;
- contratos de referencia OP-04 y OP-05;
- rúbrica del H3, evidencias, planilla y banco de variantes;
- calendario de 28 encuentros y procedencia de los recursos.

**Extensión:** el libro quedó en 35 páginas, por debajo de las 38 a 46 estimadas en el plan. No se agregó relleno; el verificador lo informa.

**Otros archivos:**
- resultados: `verificacion_resultado.*`, `CONTROLES_FINALES.*`, `prueba_fuentes_resultado.json`, `resultado_construccion.json`;
- láminas: `revision_visual/*.png`;
- manifiesto: `MANIFIESTO_LOTE_3.json`, con el SHA-256 de cada archivo.

## 2. Fuente editable común

Nada se transcribe entre documentos: el libro, la guía y el cuaderno se generan con `python3 lote_3/build/construir.py` desde estos módulos.

**Datos del caso (`lote_3/caso/`):**
- `diseno.py`: catálogo v1.1; entidades, relaciones y restricciones RI-01 a RI-08; datos derivados, parámetros y diccionario; pantallas, zonas, transiciones, recorridos y mensajes ME-01 a ME-12; accesibilidad; capas, contratos OP-01 a OP-06, DT-01 y matriz de coherencia; banco del H3.
  - Lee sin modificarlos `lote_1/caso/dossier.py` y `lote_2/caso/requisitos.py` y `modelos.py`.
- `mbokaja_u3.py`: datos nuevos M-F8 y M-F9, situaciones MS-3 a MS-5 y observaciones OBS-1 a OBS-6.

**Contenido y armado (`lote_3/build/`):**
- contenido: `cap7.py`, `cap8.py` y `cap9.py`, con los mismos atributos que los capítulos 1 a 6 (lo comprueba `tomo.py`);
- figuras: `diagramas_u3.py`, una función por símbolo y por notación, con registro en `figs/simbolos.json`;
- armado: `piezas_u3.py`, `construir.py` y `guia_u3.py`.

**Lo que se reutiliza sin copiarlo:**
- la maqueta del lote 1 y el perfil O3 de `lote_2/build/oficio.py`;
- la portada y las piezas de `lote_2/build/piezas.py`;
- el control de filas de la candidata O3.

**Índice del tomo anual:** `lote_3/build/tomo.py` amplía el del lote 2 sin tocarlo; quedan pendientes los Capítulos 10 a 18.

## 3. Cómo se aplicaron las decisiones de Fernando

### Capítulo 7 — Datos que representan las reglas (Encuentros 13 y 14)

**Notación y alcance:**
- notación entidad-relación clásica de Algorítmica 3.º, rotulada como representación simplificada;
- los atributos van en el diccionario: Tabla 7.5, con 25 campos, cada uno con significado, obligatoriedad, ejemplo y origen;
- 7.1 es una ficha de recuperación con remisión a las clases de Algorítmica: no se enseñan claves, formas normales ni bases de datos;
- 7.4 revisa anomalías con el cuaderno del caso (D1-A4, D2-8), sin teoría de formas normales.

**Obra, edición y ejemplar:**
- Obra → Edición → Ejemplar → Préstamo: el préstamo es siempre de un ejemplar;
- la disponibilidad se calcula, no se guarda.

**Integridad e historial:**
- la devolución completa la fecha y no borra (RI-04, RN-05);
- lo que tiene historia se inactiva (RI-05, RN-06);
- la «eliminación en cascada» de Algorítmica aparece solo como contraste.

**Catálogo v1.1:**
- RF-11 (tipo de lector) y RN-02 v1.1 (máximos de 2 y 5 en Parámetro), con trazabilidad a SC-01 (Ejemplos resueltos 7.2 y 9.3).

**Curso y reportes:**
- el curso es obligatorio solo para estudiantes (RI-06);
- el préstamo guarda el curso del día (RI-08);
- el informe por curso cuenta a los docentes en una fila propia, sin cursos ficticios y con el total recontado (Tabla 7.8).

**Capacidades:** C5 en los dos encuentros. C9 aparece solo como articulación de la revisión con contraejemplos, en la guía, sin atribuirla a Work.

### Capítulo 8 — Diseñar para las tareas de las personas (Encuentros 15 y 16)

**Mapa de navegación (Figura 8.1):**
- pantallas rectangulares con su código, flechas rotuladas con la acción (verbo), un punto de inicio y zonas Pública, Bibliotecaria y Dirección;
- la Tabla 8.2 lo distingue expresamente de los diagramas de actividades, contexto y casos de uso.

**Bocetos, estados y mensajes:**
- bocetos de baja fidelidad de las tres tareas (Figura 8.2);
- los cuatro estados de PT-05 (Figura 8.3);
- doce mensajes que salen de los flujos alternativos de CU-01 a CU-03 (Tabla 8.6).

**Accesibilidad y revisión:**
- lista de accesibilidad A-01 a A-08, con teclado y foco visible;
- sesión con usuarios simulados y tarjetas de rol en la guía.

**Práctica 8 (Mbokaja):**
- el voluntario de 9.º es menor y trabaja supervisado;
- se analizan permisos mínimos y privacidad (Nivel 3), sin suponer que accede a datos personales ni a funciones administrativas.

### Capítulo 9 — Arquitectura y revisión del diseño (Encuentros 17 y 18)

**Arquitectura:**
- tres capas (Figura 9.1) y la regla de dónde vive cada restricción (Tabla 9.2);
- las reglas se comprueban en el servidor, y RI-01 se protege también en la persistencia.

**Contratos:**
- Tablas 9.3 y 9.4: entradas, precondiciones, resultado, errores y requisitos de las operaciones prioritarias;
- cada error tiene su mensaje del Capítulo 8.

**Decisión técnica DT-01 (Tabla 9.5):**
- condiciones excluyentes RS-01 y RS-02, sin puntajes;
- HTML/CSS, PHP y SQLite solo como ejemplo provisional: no obligatorio, no aprobado para todos los colegios y sin probar en equipos escolares;
- funcionamiento local y sin servicios pagos;
- no se repite la matriz de selección de Algorítmica.

**Matriz de coherencia (Tabla 9.6):** los 16 requisitos v1.1, con datos, interfaz, operación y prueba.

**Práctica 9:**
- complemento editorial al índice de Work, rotulado así;
- va en el Encuentro 17 o como actividad complementaria, fuera de sus 5 HC, antes del Encuentro 18;
- decisiones nuevas: contrato de devolución con libro dañado, reposición y mantenimiento del entorno (M-F9).

**H3 (Encuentro 18, página nueva):**
- rúbrica de seis criterios que cubren C1 a C7, con cuatro niveles;
- 60 % de evidencia del equipo y 40 % individual, rotulado como propuesta editorial;
- variante individual del banco VH-1 a VH-5, que no está en el dossier, el buzón, D3 ni las prácticas;
- ausencia de evidencia registrada aparte (AE);
- 4 HC de defensa y 1 HC de corrección del dossier.

## 4. Plan anual

- `plan_anual/plan_anual_preliminar.py` lee ahora también `lote_3/build/cap7.py` a `cap9.py`.
- Los indicadores de los Capítulos 7 a 9 salen de esas fichas, sin transcribirlos.
- El control de rótulos entiende rangos como «C1 a C7».
- Se regeneraron el CSV y el MD; sigue siendo preliminar.

## 5. Controles

| Programa | Resultado |
|---|---|
| `build/verificar.py` | 200 correctos, 0 fallos (bloques A, B, C, D, E, F, G, H, I, J, L, M, N, P, Q) |
| `build/controles_finales.py` | 18 controles, 0 fallos |
| `build/prueba_fuentes.py` | 9 combinaciones (Carlito, Liberation Sans y DejaVu Sans), 0 fallos |
| `build/tomo.py` | Capítulos 1 a 9 con todos los atributos de armado |
| `plan_anual/plan_anual_preliminar.py` | Controles correctos: 36 encuentros, 18 capítulos, 180 HC |
| `lote_1/caso/verificar_caso.py` | Sin fallos |

**Controles nuevos del verificador:**
- obra y ejemplar;
- ninguna operación borra;
- orígenes del diccionario;
- cada requisito v1.1 en la matriz de coherencia;
- cada flujo alternativo con su mensaje y su error de contrato;
- notaciones sin mezcla y mapa con verbos;
- DT-01 con RS-01 y RS-02 y sin puntajes;
- sin Socios, Access ni formas normales;
- rúbrica del H3 con C1 a C7;
- banco del H3 ausente de las fuentes;
- lotes 1 y 2 intactos.

**Impresión:**
- todas las filas de todas las tablas están en el PDF;
- las tablas de hasta seis filas no se parten;
- las largas se cortan con al menos tres filas de cada lado y con el encabezado repetido: Tablas 7.5, 8.3, 9.3 y 9.6, y la clave de la evaluación 9 en la guía;
- cada figura sale con su epígrafe en la misma página.

## 6. Revisión visual

`revision_visual/` tiene quince láminas:
- índice;
- modelo y diccionario;
- leyendas;
- mapa, bocetos y estados;
- mensajes y accesibilidad;
- capas, contratos y DT-01;
- matriz de coherencia;
- prácticas y evaluaciones;
- H3;
- rúbrica y tarjetas de la guía;
- márgenes;
- tablas repartidas;
- cuaderno.

Se revisaron todas las páginas de los tres PDF.

**Corregido en la revisión:**
- Figura 9.1: rótulo encimado y bandas vacías;
- cortes de tabla con el encabezado y una sola fila;
- páginas medio vacías al comienzo de los capítulos;
- dos transiciones del mapa sin verbo.

## 7. Decisiones editoriales para revisar en la auditoría

1. **Tabla 7.8:** muestra abril, el primer mes con el sistema, con cifras ficticias propias. No reconstruye marzo (D2), cuyos seis préstamos sin curso no se pueden recuperar.
2. **Contratos:** los de OP-01 a OP-03 van en la Tabla 9.4 y no en recuadros, para mantener la numeración correlativa. Los de OP-04 y OP-05 van en la guía; OP-06 es una actividad.
3. **Pérdida y reposición en Mbokaja:** el ejemplar perdido queda inactivo y el que lo repone es un ejemplar nuevo. Se acepta otra solución si no borra el historial.
4. **Transiciones del mapa:** «Buscar otro» y «Gestionar lectores» reemplazan rótulos sin verbo.

## 8. Limitaciones y pendientes

- Las pruebas reales de instalación del entorno de referencia en equipos escolares siguen pendientes.
- El libro tiene menos páginas que las estimadas en el plan.
- Unidad IV en adelante: no se construyó. Se espera la auditoría de este lote y la autorización de Fernando.
