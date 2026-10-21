# -*- coding: utf-8 -*-
"""Registra las diferencias entre la referencia docente del lote 4 y las copias v2 del lote 5 (decisión 3 de Fernando):
lote_5/proyecto/DIFERENCIAS_v2.md, con el diff unificado de cada archivo que cambia. La referencia del lote 4 no se toca.
Uso: python3 lote_5/build/diferencias.py"""
import os, difflib
AQUI = os.path.dirname(os.path.abspath(__file__))
L5 = os.path.dirname(AQUI)
ADS = os.path.dirname(L5)
V1 = os.path.join(ADS, 'lote_4', 'proyecto', 'referencia_docente')
PARES = [('referencia_docente_v2', V1, 'Corrección de IN-02 (Capítulo 16, ejemplo central)'),
         ('referencia_docente_v2_sc02', os.path.join(L5, 'proyecto', 'referencia_docente_v2'),
          'Cambio aprobado SC-02 sobre la v2 (Capítulo 16, ejemplo complementario)')]


def archivos(raiz):
    out = set()
    for d, _, fs in os.walk(raiz):
        for f in fs:
            r = os.path.relpath(os.path.join(d, f), raiz)
            if not r.startswith('datos'):
                out.add(r)
    return out


def diferencias(antes, despues):
    filas = []
    for r in sorted(archivos(antes) | archivos(despues)):
        a = os.path.join(antes, r); b = os.path.join(despues, r)
        la = open(a, encoding='utf8').read().split('\n') if os.path.exists(a) else []
        lb = open(b, encoding='utf8').read().split('\n') if os.path.exists(b) else []
        if la != lb:
            d = list(difflib.unified_diff(la, lb, 'antes/' + r, 'despues/' + r, lineterm='', n=2))
            filas.append((r, 'nuevo' if not la else 'modificado', d))
    return filas


if __name__ == '__main__':
    out = ['# Diferencias de la referencia docente v2 (lote 5)', '',
           'Generado por `lote_5/build/diferencias.py`. La referencia del lote 4 (`lote_4/proyecto/referencia_docente/`) '
           'no se modificó: las versiones nuevas son copias en `lote_5/proyecto/`. Las pruebas de regresión están en '
           '`lote_5/resultados_pruebas/`.', '']
    for nueva, antes, titulo in PARES:
        fs = diferencias(antes, os.path.join(L5, 'proyecto', nueva))
        out += ['## %s — %s' % (nueva, titulo), '', '| Archivo | Cambio | Líneas agregadas | Líneas quitadas |', '|---|---|---|---|']
        for r, tipo, d in fs:
            out.append('| `%s` | %s | %d | %d |' % (r, tipo, sum(1 for l in d if l.startswith('+') and not l.startswith('+++')),
                                                  sum(1 for l in d if l.startswith('-') and not l.startswith('---'))))
        out.append('')
        for r, tipo, d in fs:
            out += ['### `%s`' % r, '', '```diff'] + d + ['```', '']
    open(os.path.join(L5, 'proyecto', 'DIFERENCIAS_v2.md'), 'w', encoding='utf8').write('\n'.join(out))
    print('\n'.join(l for l in out if l.startswith('|')))
