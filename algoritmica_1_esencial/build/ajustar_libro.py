# -*- coding: utf-8 -*-
"""Ajusta la paginación del libro (H03) SIN quitar ningún salto obligatorio: cada clase, práctica y evaluación
abre página. Mientras haya una hoja interior con menos del 25 % de ocupación:
 · si es la última hoja de una clase o una práctica, se lleva a esa hoja un párrafo de la hoja anterior de la
   MISMA sección (corte = salto de página antes de ese párrafo), elegido para que las dos hojas queden ocupadas;
 · si es la última hoja de una evaluación, se compactan sus renglones o la Parte B pasa a hoja propia.
Los ajustes quedan en ajustes_libro.json."""
import json, subprocess, re
import pymupdf, docx
import ocupacion as OC
B = '/home/claude/alg1/build/'
DOCX = '/home/claude/alg1/salida_v1_3_1/Algoritmica_1er_Curso_LIBRO_ESENCIAL_COMERCIAL_2026.docx'
PDF = DOCX[:-5] + '.pdf'
UMBRAL = 0.27            # 25 % exigido + margen de seguridad
PREV_MIN, TAIL_OBJ, TAIL_MAX = 0.40, 0.32, 0.92
EVID = {'Evaluación de la Unidad 1': 'U1', 'Evaluación de la Unidad 2': 'U2', 'Evaluación integradora de la 1.ª etapa': 'E1',
        'Evaluación de la Unidad 3': 'U3', 'Evaluación integradora de la 2.ª etapa': 'E2'}
M_CM = 1.27 / 2.54 * 72


def clave(s):
    return re.sub(r'[^0-9A-Za-zÀ-ÿ]', '', s).lower()[:40]


def seccion(ent, pags, p):
    cand = [(pg, t) for (lvl, t), pg in zip(ent, pags) if pg <= p]
    return cand[-1] if cand else (0, '?')


def proponer_corte(sec, p, occ_p):
    """Párrafo de la hoja p-1 (misma sección) que conviene pasar a la hoja p."""
    import build_libro as BL
    d = docx.Document(DOCX)
    parrafos = [(clave(t), t) for s_, t, el in BL.secciones_cuerpo(d) if s_ == sec and len(clave(t)) >= 12]
    usados = {(s_, a) for s_, a in BL.AJ['cortes']}
    pg = pymupdf.open(PDF)[p - 2]
    top, bot = M_CM, pg.rect.height - M_CM
    alto = bot - top
    fondo = max(OC.ocupacion(PDF)[p - 2][1] * alto + top, 0)
    cands = []
    for blk in pg.get_text('blocks'):
        k = clave(blk[4])
        if len(k) < 12:
            continue
        for kk, t in parrafos:
            if kk.startswith(k[:min(len(k), 30)]) or k.startswith(kk[:30]):
                y0 = blk[1]
                prev = (y0 - top) / alto
                mov = (fondo - y0) / alto
                if prev >= PREV_MIN and occ_p + mov >= TAIL_OBJ and occ_p + mov <= TAIL_MAX and (sec, t[:60]) not in usados:
                    borde = bool(re.match(r'(Actividad \d+ —|Desafío|Actividades de aplicación|Ejercitá|Resolvé|Pensá|Transferencia|Lo que necesitás|Datos para cargar)', t))
                    cands.append((not borde, mov, y0, t[:60]))
                break
    if not cands:
        return None
    return min(cands)[3]   # primero los bordes de bloque; entre ellos, el menor movimiento que alcanza el objetivo


def main(max_iter=40):
    for it in range(max_iter):
        subprocess.run(['python3', B + 'build_libro.py'], check=True, cwd=B, stdout=subprocess.DEVNULL)
        ji = json.load(open(B + 'indice_libro.json'))
        occ = OC.ocupacion(PDF)
        bajas = [x for x in occ if x[1] < UMBRAL and not x[3] and x[0] > 3]
        print('iter', it, 'páginas', len(occ), 'bajas', [(x[0], int(x[1] * 100)) for x in bajas], flush=True)
        if not bajas:
            return True
        AJ = json.load(open(B + 'ajustes_libro.json'))
        cambio = False
        for x in bajas:
            p = x[0]
            ini, tit = seccion(ji['entradas'], ji['paginas'], p)
            m = re.match(r'(Clase|Práctica) (\d+) ', tit)
            if m and ini < p:
                sec = '%s %s' % (m.group(1), m.group(2))
                ancla = proponer_corte(sec, p, x[1])
                if ancla:
                    AJ['cortes'].append([sec, ancla]); cambio = True
                    print('  p.%d (%s): corte antes de «%s»' % (p, sec, ancla[:50])); break
            if tit in EVID and EVID[tit] not in AJ['ev']:
                AJ['ev'].append(EVID[tit]); cambio = True; print('  p.%d: compacta renglones de %s' % (p, EVID[tit])); break
            if tit in EVID and EVID[tit] not in AJ['evsplit']:
                AJ['evsplit'].append(EVID[tit]); cambio = True; print('  p.%d: %s con la Parte B en hoja propia' % (p, EVID[tit])); break
            print('  p.%d (%s): sin ajuste automático' % (p, tit[:50]))
        json.dump(AJ, open(B + 'ajustes_libro.json', 'w'), ensure_ascii=False, indent=1)
        if not cambio:
            return False
    return False


if __name__ == '__main__':
    print('OK' if main() else 'QUEDAN páginas bajas')
