# -*- coding: utf-8 -*-
"""Divide los bloques del tomo de 2.º en clases, con su ficha, cuerpo y unidad (mismo formato que el piloto de 3.º)."""
import json, re

B_PATH = '/home/claude/alg2/build/tomo_blocks.json'


def cargar():
    B = json.load(open(B_PATH))
    pre = []; clases = {}; unidades = {}
    cur = None; modo = 'pre'; u = None
    for b in B:
        if b['t'] == 'h1':
            m = re.match(r'Clase (\d+) — (.*)', b['text'])
            mu = re.match(r'Unidad (\d+) — (.*)', b['text'])
            if m:
                n = int(m.group(1)); cur = {'n': n, 'titulo': m.group(2).strip(), 'unidad': u, 'cuerpo': []}
                clases[n] = cur; modo = 'cuerpo'; continue
            if mu:
                u = int(mu.group(1)); unidades[u] = mu.group(2).strip(); modo = 'skip'; continue
            modo = 'skip'; continue
        if b['t'] == 'banda':
            modo = 'eval'; continue
        if modo == 'cuerpo':
            if b['t'] == 'ficha':
                cur['ficha'] = b; continue
            if b['t'] == 'h3' and 'Actividades' in b['text']:
                modo = 'acts'; continue
            cur['cuerpo'].append(b)
        elif modo == 'pre':
            pre.append(b)
    return pre, clases, [], unidades


if __name__ == '__main__':
    import sys
    pre, C, E, U = cargar()
    print(U)
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    print(C[n]['titulo'], C[n]['ficha']['capacidad'])
    for i, b in enumerate(C[n]['cuerpo']):
        s = b.get('text') or b.get('title') or b.get('file') or str(b.get('hdr') or b.get('lines'))
        print(i, b['t'], s[:120])
