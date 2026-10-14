# Historia y Geografía 7.º — Producción anual (36 encuentros)

**Estado: producción en curso. No es versión comercial ni definitiva.** Claude construye y controla técnicamente; ChatGPT audita pedagógica y curricularmente; Work puede verificar visualmente; Fernando aprueba.

- **Modelo aprobado:** muestra 3, commit `841f5bc9e4a4fec11af63cc821fc3062a6587de8`, carpeta `../04_muestra3/` (congelada, sin cambios).
- **Dictamen:** `../auditorias/AUDITORIA_MUESTRA3_841f5bc9/DICTAMEN_INDEPENDIENTE_MUESTRA3.md` (APTO CON OBSERVACIONES como modelo).
- **Condiciones obligatorias:** `CONDICIONES_PRODUCCION.md` (A05, A10, A14, A17, A19 y N01-N05).
- **Estado de los 36 encuentros:** `ESTADO_36_ENCUENTROS.md` (lo genera `scripts/estado.py`).
- **Manifiesto:** `MANIFIESTO.json` (archivos, tamaños y SHA-256).

## Organización

| Carpeta | Contenido |
|---|---|
| `scripts/curriculo.py` | Capacidades y temas literales del programa MEC 2014 y arquitectura de los 36 encuentros. |
| `scripts/contenido/eNN.py` | Contenido de cada encuentro: tomo, fichas, plan y solucionario. |
| `scripts/figuras/` | Figuras propias por bloque, más las funciones comunes. |
| `scripts/motor/` | Constructores del tomo, planes y solucionario, y render a PDF. Generalizan los scripts de la muestra 3. |
| `scripts/construir_bloque.py` | Construye un bloque: figuras, tomo, planes, solucionario, PDF y copias livianas. |
| `scripts/verificar.py` | Controles automáticos (extiende el verificador de la muestra 3). |
| `bloque_N/` | Entregables de cada bloque y su informe técnico de control. |
| `anual/` | Documentos anuales consolidados, al terminar los cuatro bloques. |
| `datos/` | Texto del programa MEC y datos de trazabilidad. |

## Bloques

| Bloque | Encuentros |
|---|---|
| I | 1-9 |
| II | 10-18 |
| III | 19-27 |
| IV | 28-36 |

Cada bloque debe superar los controles automáticos y la inspección visual de todas sus páginas antes de pasar al siguiente.

## Reconstrucción

```
python3 scripts/construir_bloque.py N MAESTRO.docx GEOJSON
python3 scripts/verificar.py N
```

Insumos:
- **`MAESTRO.docx`:** tomo del 03/10/2026, SHA-256 `8dbc4f44…179413`. Solo se usan su portada, presentación, estilos e índice.
- **`GEOJSON`:** carpeta con los datos de Natural Earth (dominio público).
