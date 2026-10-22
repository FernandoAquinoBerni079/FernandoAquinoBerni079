# Validaciones realizadas — edición comercial v1.0

Fecha: 22 de octubre de 2026.

## Realizadas (en el entorno de construcción, Linux)

| Validación | Cómo | Resultado |
|---|---|---|
| Auditoría final de la entrega | `edicion_v1_0/build/auditoria_final.py` (79 controles) | 0 fallos |
| Auditoría de la planificación | `edicion_v1_0/build/plan/controles_plan.py` (83 controles) | 0 fallos |
| Fidelidad al contenido aprobado | Texto de cada página del libro y de la guía v1.0 comparado con v0.2 desde la página 2 | Idéntico |
| Renglones del cuaderno | Medición en el PDF de la distancia entre renglones | 8 mm (mediana) |
| Compatibilidad de fuentes | Calibri reemplazada por Carlito, Liberation Sans y DejaVu Sans; conversión a PDF | Ver PRUEBA_DE_FUENTES.json |
| Ortografía | Diccionario Hunspell de español con regla de voseo | 0 errores reales; formas no reconocidas listadas |
| Legibilidad de código y tablas | Render a 220 ppp de las páginas con código de 7,5 pt | Nítido |
| Datos reservados | Búsqueda en todo el texto de la entrega de los textos y códigos del conjunto DR y de las variantes V6 | Ninguno presente |
| ZIP de entrega | Prueba de integridad, contenido idéntico a la carpeta, búsqueda de archivos reservados | Ver INFORME_FINAL_DE_AUDITORIA |
| Manifiesto | SHA-256 de cada archivo de la entrega | MANIFIESTO_SHA256.json |

## No realizadas (requieren acceso o intervención que este entorno no tiene)

| Validación | Por qué no se hizo | Quién la hace |
|---|---|---|
| Apertura y edición de los DOCX en Microsoft Word sobre Windows | No hay acceso a Windows ni a Word | Titular, antes de la venta |
| Prueba de campo del entorno técnico (PHP, SQLite) en las computadoras de la institución (E-1 a E-12) | Solo se probó en Linux | Docente, en la institución |
| Prueba de impresión física (prueba de color, encuadernación, lomo) | No hay imprenta | Imprenta, con la prueba de color firmada |
| Revisión jurídica (titularidad, licencia del código, condiciones de uso) | Requiere un profesional | Abogado de propiedad intelectual |
| Consulta directa a los sitios oficiales (DINAPI, Agencia Paraguaya del ISBN, Biblioteca Nacional, DNIT) | Los sitios no respondieron desde el entorno; se usaron resúmenes de búsqueda | Titular o su asesor |
| ISBN y depósito legal | Los trámites los hace el editor | Editor |

Ninguna de las validaciones de la segunda tabla se declara cumplida en ningún documento de la entrega.
