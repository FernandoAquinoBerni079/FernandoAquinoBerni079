# -*- coding: utf-8 -*-
"""Ajusta los saltos del libro (H03): mientras haya páginas interiores con menos de 25 % de ocupación, une la
sección con la siguiente (sin salto de página) o compacta los renglones de la evaluación. Deja el resultado en
uniones_libro.json y repite el build del libro."""
import json, subprocess, re, sys, os
import ocupacion as OC
B = '/home/claude/alg1/build/'
PDF = '/home/claude/alg1/salida_v1_3/Algoritmica_1er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026.pdf'
UMBRAL = 0.25 + 0.02   # margen de seguridad sobre el 25 % exigido
EVID = {'Evaluación de la Unidad 1': 'U1', 'Evaluación de la Unidad 2': 'U2', 'Evaluación integradora de la 1.ª etapa': 'E1',
        'Evaluación de la Unidad 3': 'U3', 'Evaluación integradora de la 2.ª etapa': 'E2'}

def seccion(ent, pags, p):
    cand = [(pg, t) for (lvl, t), pg in zip(ent, pags) if pg <= p]
    return cand[-1] if cand else (0, '?')

def main(max_iter=14):
    UN_PATH = B + 'uniones_libro.json'
    for it in range(max_iter):
        subprocess.run(['python3', B + 'build_libro.py'], check=True, cwd=B, stdout=subprocess.DEVNULL)
        ji = json.load(open(B + 'indice_libro.json'))
        occ = OC.ocupacion(PDF)
        bajas = [x for x in occ if x[1] < UMBRAL and not x[3] and x[0] > 3]
        print('iter', it, 'páginas', len(occ), 'bajas', [(x[0], int(x[1] * 100)) for x in bajas])
        if not bajas:
            return True
        UN = json.load(open(UN_PATH))
        cambio = False
        for x in bajas:
            p = x[0]
            ini, tit = seccion(ji['entradas'], ji['paginas'], p)
            m = re.match(r'(Clase|Práctica) (\d+) ', tit)
            if m and m.group(1) == 'Clase' and int(m.group(2)) not in UN['cp']:
                UN['cp'].append(int(m.group(2))); cambio = True; print('  p.%d: une Práctica %s a la Clase' % (p, m.group(2))); break
            if m and m.group(1) == 'Práctica' and int(m.group(2)) not in UN['pc']:
                n = int(m.group(2))
                tras_eval = n in (5, 12, 21)
                if not tras_eval and n < 21:
                    UN['pc'].append(n); cambio = True; print('  p.%d: une Clase %d a la Práctica %d' % (p, n + 1, n)); break
            if tit in EVID and EVID[tit] not in UN['ev']:
                UN['ev'].append(EVID[tit]); cambio = True; print('  p.%d: compacta renglones de %s' % (p, EVID[tit])); break
            if tit in EVID and EVID[tit] not in UN['evsplit']:
                UN['evsplit'].append(EVID[tit]); cambio = True; print('  p.%d: %s con la Parte B en hoja propia' % (p, EVID[tit])); break
            if m and m.group(1) == 'Práctica':
                n = int(m.group(2)); k = len(__import__('practicas').PR[n]['acts']) - 1
                if k >= 2 and [n, k] not in UN['pb']:
                    UN['pb'].append([n, k]); cambio = True; print('  p.%d: salto de página antes de la Actividad %d de la Práctica %d' % (p, k, n)); break
            print('  p.%d (%s): sin ajuste automático' % (p, tit))
        json.dump(UN, open(UN_PATH, 'w'))
        if not cambio:
            return False
    return False

if __name__ == '__main__':
    print('OK' if main() else 'QUEDAN páginas bajas')
