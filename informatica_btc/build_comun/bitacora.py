# -*- coding: utf-8 -*-
"""Genera la bitácora R1 → R2 en Markdown a partir del registro JSON que deja el constructor de cada curso.
Uso: python3 bitacora.py <registro.json> <salida.md> <título> [versión origen] [versión destino]"""
import json, sys
reg = json.load(open(sys.argv[1], encoding='utf8'))
V0, V1 = (sys.argv[4], sys.argv[5]) if len(sys.argv) > 5 else ('R1', 'R2')
def corto(t, n=260):
    t = ' '.join(str(t).split()).replace('|', '/')
    return t if len(t) <= n else t[:n - 1] + '…'
L = ['# ' + sys.argv[3], '',
     'Generada automáticamente desde `%s`. Cada fila es un cambio aplicado por el constructor sobre la copia %s '
     '(solo lectura); «Apariciones» es la cantidad verificada: si el texto de origen no aparecía exactamente esas veces, '
     'la construcción se detenía.' % (sys.argv[1].split('/')[-1], V0), '',
     '| N.º | Documento | Antes (%s) | Después (%s) | Apariciones | Motivo / hallazgo |' % (V0, V1), '|---|---|---|---|---|---|']
for i, c in enumerate(reg['cambios'], 1):
    L.append('| %d | %s | %s | %s | %s | %s |' % (i, c['documento'], corto(c['antes']), corto(c['despues']), c['apariciones'], corto(c['motivo'], 200)))
L += ['', '## Índices estáticos recalculados', '',
      'Números de página buscados en el PDF renderizado de R2 (segunda pasada; la primera ya había corregido los desplazamientos).', '']
for k, v in reg['indices'].items():
    L.append('- **%s**: %d entradas verificadas contra el render.' % (k, len(v)))
open(sys.argv[2], 'w', encoding='utf8').write('\n'.join(L) + '\n')
print(len(reg['cambios']), 'filas')
