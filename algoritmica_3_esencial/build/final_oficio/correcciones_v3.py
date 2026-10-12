"""Correcciones de la reauditoría FINAL OFICIO v2 (04_REAUDITORIA_CHATGPT…_v2, 12/10/2026).

Uso: python3 -I correcciones_v3.py LIBRO_V2.docx LIBRO_V3.docx
Fuente: el Libro FINAL OFICIO v2. Solo toca el Libro:
  10 (MAYOR)  Clase 21: la igualdad de sumas de la tabla cruzada controla la coherencia de los
              subtotales, no la exactitud de cada celda (paso 5, concepto clave y su anticipo).
  11 (MENOR)  Proyecto Final: un solo encabezado para la capacidad transversal.
"""
import sys, os, copy, docx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx.oxml.ns import qn
from correcciones_v2 import texto, reemplazar, unico, parrafo_tras, CAP as _CAP
CAP = _CAP[1:-1]   # frase oficial sin comillas

LIBRO = [
    # 10 — anticipo en la introducción del paso a paso
    ('La figura muestra el resultado completo — y su doble control: cada fila suma el total del cliente y cada columna, el total de la categoría.',
     'La figura muestra el resultado completo — y su control de sumas: cada fila suma el total del cliente y cada columna, el total de la categoría.'),
    # 10 — paso 5 (texto del auditor)
    ('5. Doble control: filas y columnas convergen en la misma esquina — G. 134.000. Si un solo cruce estuviera mal, las dos sumas '
     'no coincidirían: la cruzada trae su propio auditor incorporado.',
     '5. Control de sumas: la suma de los totales por filas debe coincidir con la suma de los totales por columnas, porque ambas '
     'reúnen las mismas celdas (en el Copetín, G. 134.000). Esta igualdad permite detectar errores de suma o presentación, pero NO '
     'demuestra que cada celda sea correcta. Para comprobar los importes, contrastá una muestra de cruces con los registros originales '
     'de DetalleVenta o calculá los totales mediante una consulta independiente.'),
    # 10 — concepto clave (título y texto del auditor)
    ('Concepto clave — la esquina que audita', 'Concepto clave — coherencia no es exactitud'),
    ('Que el total por clientes y el total por categorías coincidan al guaraní no es casualidad: son dos particiones de las MISMAS '
     'once filas de DetalleVenta. Toda cifra de gestión seria se verifica así, por caminos independientes que deben encontrarse.',
     'Una tabla cruzada facilita comprobar la coherencia de sus subtotales. La exactitud de cada importe exige además validarlo '
     'contra los datos de origen.'),
]


def libro(ent, sal):
    d = docx.Document(ent)
    for v, n in LIBRO:
        reemplazar(d, v, n)
    # 11 — PFI: un solo encabezado; la capacidad en párrafo propio y la evidencia en otro
    hs = [e for e in d.element.body if e.tag == qn('w:p') and texto(e) == 'Capacidad transversal del programa']
    assert len(hs) == 1, len(hs)
    h = hs[0]
    ts = list(h.iter(qn('w:t'))); ts[0].text = 'Capacidad transversal del programa MEC'
    for t in ts[1:]:
        t.text = ''
    p = h.getnext()
    assert texto(p).startswith('Capacidad transversal MEC: ' + CAP), texto(p)[:60]
    evid = texto(p).split(CAP, 1)[1].strip()
    cap = parrafo_tras(h, p, [(CAP, False)])
    parrafo_tras(cap, p, [(evid, False)])
    p.getparent().remove(p)
    d.save(sal)


if __name__ == '__main__':
    libro(sys.argv[1], sys.argv[2])
    print('correcciones v3 aplicadas:', len(LIBRO), 'reemplazos + encabezado único del PFI')
