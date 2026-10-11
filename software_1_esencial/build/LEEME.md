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
| `fix_v2_maqueta.py` | Corrección v2 (V2-01, V2-02): márgenes de 1,27 cm, tablas al ancho útil y espaciado, para que cada plan entre en una hoja y el Plan Anual no deje la firma sola. No cambia texto. Uso: `python3 fix_v2_maqueta.py ENTRADA.docx SALIDA.docx [0 18]` (Planes con `0 18`; Plan Anual sin argumentos). |
| `control_v2.py` | Controles de la v2 sobre `salida/` (94): páginas, una hoja por plan, firmas, márgenes, identidad textual con la v1 y muestra. |
| `auditoria_resultado.txt` | Salida de los controles del 11/10/2026 sobre `salida/`. |

Las versiones generalizadas de estos scripts están en la skill `cuadernillos-mec` (`skill/cuadernillos-mec.zip`): `paginacion.py`, `indice_pdf.py`, `formato_oficio.py`, `unicidad_datos.py`.

PDF: se exportan con LibreOffice y la fuente **Carlito** (equivalente métrico de Calibri). Sin Carlito, LibreOffice usa DejaVu y la paginación cambia.
