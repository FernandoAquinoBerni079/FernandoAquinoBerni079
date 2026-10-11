# build/ — scripts de la corrección v1 (02/10/2026)

Sirven para rastrear y repetir las correcciones. **No reconstruyen el libro desde cero**: trabajan sobre el .docx de Fer (`…LIBRO_ESENCIAL_COMERCIAL_2026_1.docx`, en Drive/SUPERSEDIDOS como `_SUPERSEDIDO_A`), que tiene las imágenes de Gemini.

| Script | Función |
|---|---|
| `ed.py` | Reemplazo de texto a nivel de párrafo, conservando el formato. |
| `caps.py` | Las 20 capacidades del programa MEC (págs. 59–63) y su asignación a clases y secuencias. |
| `fix_libro.py`, `fix_sol.py`, `fix_planes.py`, `fix_pa.py` | Correcciones de la auditoría v1 en cada documento. |
| `bincheck.py` | Control de operandos binarios repetidos (Unidad 3). |
| `oficio.py`, `saltos.py`, `paginar.py`, `ciclo.py` | Paso a oficio, saltos de página robustos y ajuste de páginas casi vacías. |
| `indice.py`, `tocchk.py` | Índice poblado con las páginas del PDF y su verificación. |
| `auditoria_v1.py` | Auditoría de contenido: 117 controles. Lee `out/` (hacer `ln -s ../salida out`). |
| `respuesta.py` | Genera el informe 05_RESPUESTA (.docx). |
| `auditoria_resultado.txt` | Salida de los controles del 11/10/2026 sobre `salida/`. |

Las versiones generalizadas de estos scripts están en la skill `cuadernillos-mec` (`skill/cuadernillos-mec.zip`): `paginacion.py`, `indice_pdf.py`, `formato_oficio.py`, `unicidad_datos.py`.
