# -*- coding: utf-8 -*-
"""Manifiesto SHA-256 de la colección → coleccion/MANIFIESTO_COLECCION.json: cada archivo de coleccion/ (salvo el propio
manifiesto) y la huella de los manifiestos de los seis lotes, para que una sola comprobación muestre que nada aprobado
cambió. El conjunto DR y el banco V6 no están en el repositorio ni en el manifiesto.
Uso: python3 -B coleccion/build/manifiesto_coleccion.py (al final, después de los controles)."""
import os, json, hashlib, datetime
AQUI = os.path.dirname(os.path.abspath(__file__))
COL = os.path.dirname(AQUI)
ADS = os.path.dirname(COL)
SALIDA = os.path.join(COL, 'MANIFIESTO_COLECCION.json')


def entrada(raiz, ruta):
    datos = open(os.path.join(raiz, ruta), 'rb').read()
    return {'ruta': ruta, 'bytes': len(datos), 'sha256': hashlib.sha256(datos).hexdigest()}


archivos = []
for d, carpetas, fs in os.walk(COL):
    carpetas[:] = sorted(c for c in carpetas if c != '__pycache__')
    for f in sorted(fs):
        ruta = os.path.relpath(os.path.join(d, f), COL)
        if os.path.join(COL, ruta) != SALIDA:
            archivos.append(entrada(COL, ruta))
lotes = [entrada(ADS, r) for r in ['lote_1/MANIFIESTO_LOTE_1.json', 'lote_1_oficio_candidata/MANIFIESTO_CANDIDATA_O3.json'] +
         ['lote_%d/MANIFIESTO_LOTE_%d.json' % (n, n) for n in range(2, 7)]]
j = lambda n: json.load(open(os.path.join(COL, n), encoding='utf8'))
json.dump({'coleccion': 'ADS 3.º BTI — documentos anuales v0.1 (integración editorial, para auditoría)',
           'fecha': datetime.date.today().isoformat(),
           'estado': 'Para auditoría independiente. No aprobado para la venta ni validado en laboratorios escolares. '
                     'Windows y los equipos escolares siguen pendientes; el borrador de licencia, pendiente de revisión jurídica.',
           'resultados': {'equivalencia_fallos': len(j('EQUIVALENCIA.json')['fallos']),
                          'impresion_fallos': len(j('CONTROLES_IMPRESION.json')['fallos']),
                          'coherencia_fallos': len(j('COHERENCIA.json')['fallos']),
                          'fuentes_con_fallos': sum(1 for x in j('PRUEBA_FUENTES.json') if x['resultado'] != 'correcto'),
                          'paginas': j('resultado_construccion.json')['paginas']},
           'reservados': 'No incluidos: el conjunto DR (lote 5) y el banco de variantes V6 (lote 6) son exclusivos del docente '
                         'y están fuera del repositorio.',
           'manifiestos_de_los_lotes': lotes, 'archivos': archivos},
          open(SALIDA, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('%d archivos de la colección y %d manifiestos de lotes' % (len(archivos), len(lotes)))
