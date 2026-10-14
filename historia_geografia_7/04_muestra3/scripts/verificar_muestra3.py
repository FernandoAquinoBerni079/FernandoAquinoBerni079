"""Controles automáticos de la tercera muestra.

Repite los controles de la segunda muestra y agrega los que pidió la
autorización condicionada:

 1. Capacidades: cada capacidad de las fichas, de los planes y de las bandas
    del plan anual figura literalmente en el texto del programa MEC 2014.
 2. Tomo ↔ solucionario: cada ítem numerado tiene respuesta, y no sobran.
 3. Tomo ↔ planes: cada actividad citada existe y todas quedan asignadas.
 4. Funciones: cada actividad del tomo está en una sola categoría (esenciales,
    consolidación, complementarias o domiciliarias).
 5. Duración: la secuencia de cada plan es contigua, empieza en 0 y termina
    en 120 minutos.
 6. Transparencia de rúbricas: todo criterio anunciado en el tomo se repite
    igual en el solucionario, y el solucionario no agrega rúbricas no anunciadas.
    Los puntajes de la evaluación suman el total impreso.
 7. Exactitud de respuestas: claves de opción múltiple dentro de las opciones
    impresas; distribución de letras balanceada; los ríos de la Parte D son
    los numerados en el mapa.
 8. Figuras: numeración consecutiva en orden de lectura; toda figura citada
    existe; la Figura 10.1 del maestro no se usa.
 9. Trazabilidad: JSON, matriz y plan anual coinciden (Continuación E como
    ampliación editorial, cobertura de las integradoras, conteo de fichas,
    sin «priorización MEC» ni «requerimiento curricular»).
10. Evaluación equitativa: ninguna clave se entrega antes del encuentro 31.
11. Integridad visual: páginas con poco contenido en los PDF de la muestra
    (huecos residuales), salvo la última hoja de cada plan o sección.

No reemplaza la revisión visual ni la auditoría de contenido.

Uso: python3 verificar_muestra3.py PROGRAMA.txt CARPETA_SALIDA
"""
import collections
import json
import os
import re
import sys
import unicodedata

import docx
import pymupdf

from contenido_matriz import CAPACIDADES
from contenido_planes import PLANES
from contenido_solucionario import SECCIONES as SOL
from contenido_tomo import SECCIONES as TOMO

MAPA = {15: ('clase10', 'Clase 10'), 28: ('clase18', 'Clase 18'), 29: ('contF', 'Continuación F'),
        30: ('evalU5', 'EVALUACIÓN DE LA UNIDAD 5')}
fallos, ok = [], [0]
informe = collections.OrderedDict()


def control(nombre, condicion, detalle):
    informe.setdefault(nombre, [0, []])
    if condicion:
        ok[0] += 1; informe[nombre][0] += 1
    else:
        fallos.append(f'[{nombre}] {detalle}'); informe[nombre][1].append(detalle)


def norm(s):
    s = unicodedata.normalize('NFC', s)
    s = re.sub(r'[•]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def items_tomo(bloques):
    return {int(m.group(1)) for b in bloques if b[0] == 'item' for m in [re.match(r'(\d+)\.', b[1])] if m}


def textos(x, out=None):
    out = [] if out is None else out
    if isinstance(x, str):
        out.append(x)
    elif isinstance(x, (list, tuple)):
        for y in x:
            textos(y, out)
    return out


def numeros(frag):
    s = set()
    for a, b in re.findall(r'(\d+) a (\d+)', frag):
        s |= set(range(int(a), int(b) + 1))
    return s | {int(x) for x in re.findall(r'\d+', re.sub(r'\d+ a \d+', '', frag))}


def citados(texto):
    c = set()
    for m in re.finditer(r'actividad(?:es)? ([\d ,y a]+)', texto, re.I):
        c |= numeros(m.group(1))
    for m in re.finditer(r'consignas? (\d+ a \d+)', texto, re.I):
        c |= numeros(m.group(1))
    for m in re.finditer(r'\(consigna (\d+)\)', texto, re.I):
        c.add(int(m.group(1)))
    return c


def sol_seccion(enc):
    return next(s for s in SOL if s['encuentro'] == enc)


def main():
    programa = norm(open(sys.argv[1], encoding='utf-8').read())
    out = sys.argv[2]

    # 1. capacidades literales
    caps = {b[1] for k in TOMO for b in TOMO[k] if b[0] == 'ficha'}
    for pl in PLANES:
        caps |= {c.strip() + ('' if c.strip().endswith('.') else '.') for c in re.split(r'(?<=\.)\s+', pl['capacidad']) if c.strip()}
    caps |= set(CAPACIDADES.values())
    pa = docx.Document(os.path.join(out, 'plan_anual', 'PLAN_ANUAL_OFICIO_M3.docx'))
    filas_pa = pa.tables[0].rows
    for f in filas_pa:
        for linea in f.cells[0].text.split('\n'):
            m = re.match(r'Capacidad [HG]\d \(MEC 2014, literal\): (.*)', linea)
            if m:
                caps.add(m.group(1))
    for c in sorted(caps):
        control('1. Capacidades literales', norm(c) in programa, f'Capacidad no literal: «{c}»')

    # 2. tomo ↔ solucionario
    for enc, (clave, nombre) in MAPA.items():
        nt = items_tomo(TOMO[clave])
        ns = {int(n) for _, its in sol_seccion(enc)['bloques'] for n, _, _ in its if n.isdigit()}
        extra = {1, 2, 3} if clave in ('clase10', 'clase18') else set()   # preguntas de la fuente
        control('2. Tomo ↔ solucionario', nt <= ns and not (ns - nt - extra),
                f'{nombre}: sin respuesta {sorted(nt - ns)}; sobran {sorted(ns - nt - extra)}')

    # 3, 4 y 5. planes
    for pl in PLANES:
        clave, nombre = MAPA[pl['n']]
        nt = items_tomo(TOMO[clave])
        texto_plan = ' '.join(x for _, pasos in pl['secuencia'] for paso in pasos for x in paso) + ' ' + pl['tarea']
        c = citados(texto_plan) | (nt if clave == 'evalU5' else set())
        control('3. Tomo ↔ planes', c == nt, f'Plan {pl["n"]}: inexistentes {sorted(c - nt)}; sin asignar {sorted(nt - c)}')
        if clave != 'evalU5':
            por_cat = {k: citados(v) for k, v in pl['funciones'].items()}
            todas = collections.Counter(x for v in por_cat.values() for x in v)
            dobles = sorted(x for x, n in todas.items() if n > 1)
            control('4. Funciones de las actividades', set(todas) == nt and not dobles,
                    f'Plan {pl["n"]}: sin función {sorted(nt - set(todas))}; en dos funciones {dobles}; inexistentes {sorted(set(todas) - nt)}')
            control('4. Funciones de las actividades', len(pl['funciones']) == 3 and
                    [k.split()[0] for k in pl['funciones']] == ['Esenciales', 'Consolidación', 'Complementarias'],
                    f'Plan {pl["n"]}: las categorías no son las tres pedidas')
        tramos = [tuple(int(x) for x in p[0].split('–')) for _, pasos in pl['secuencia'] for p in pasos]
        contigua = all(tramos[i][1] == tramos[i + 1][0] for i in range(len(tramos) - 1))
        control('5. Duración de las secuencias', tramos[0][0] == 0 and tramos[-1][1] == 120 and contigua and
                all(a < b for a, b in tramos), f'Plan {pl["n"]}: tramos {tramos}')
        for m in re.finditer(r'figura (\d+\.\d+|F\.\d)', texto_plan + pl['material'], re.I):
            t_tomo = ' '.join(textos(list(TOMO.values())))
            control('8. Figuras', f'Figura {m.group(1)} —' in t_tomo, f'Plan {pl["n"]} cita la Figura {m.group(1)}, que no existe')

    # 6. transparencia de rúbricas
    for enc, (clave, nombre) in MAPA.items():
        crit = {n: norm(c) for _, its in sol_seccion(enc)['bloques'] for n, _, c in its}
        for b in TOMO[clave]:
            if b[0] != 'item':
                continue
            n = re.match(r'(\d+)\.', b[1]).group(1)
            m = re.search(r'se tendrá en cuenta(?: \([^)]*\))?:? (.*?)\)?\.?$', b[1], re.I)
            if m:
                anunciado = norm(m.group(1)).rstrip('.)')
                control('6. Transparencia de rúbricas', anunciado in crit.get(n, '') and
                        crit[n].startswith('Criterio anunciado'),
                        f'{nombre}, ítem {n}: el solucionario no repite el criterio impreso «{anunciado}»')
        for n, c in crit.items():
            control('6. Transparencia de rúbricas', 'Rúbrica' not in c,
                    f'{nombre}, ítem {n}: el solucionario trae una rúbrica no anunciada en el tomo')
    ev = TOMO['evalU5']
    partes = {}
    for b in ev:
        if b[0] == 'consigna':
            m = re.match(r'Parte ([A-F]) — .*?\((\d+) puntos?(?: cada una)?(?:: (.*))?\)\.?$', b[1])
            if m:
                partes[m.group(1)] = (m.group(2), m.group(3))
    items_parte = {'A': 6, 'B': 4, 'C': 1, 'D': 1, 'E': 1, 'F': 1}
    total = sum(int(p[0]) * (items_parte[k] if 'cada una' in next(b[1] for b in ev if b[0] == 'consigna' and b[1].startswith(f'Parte {k}')) else 1)
                for k, p in partes.items())
    impreso = int(re.search(r'Puntaje total: (\d+)', ' '.join(textos(ev))).group(1))
    control('6. Transparencia de rúbricas', len(partes) == 6 and total == impreso,
            f'Evaluación: las partes suman {total} y el total impreso es {impreso}')
    bloques_sol = {nombre.split(' — ')[0]: its for nombre, its in sol_seccion(30)['bloques']}
    for k, (pts, det) in partes.items():
        if det:
            d = norm(det).split(': ')[-1] if k == 'B' else norm(det)
            c = ' '.join(norm(x[2]) for x in bloques_sol[f'Parte {k}'])
            control('6. Transparencia de rúbricas', d in c, f'Parte {k}: criterio impreso «{d}» ausente del solucionario')

    # 7. exactitud de las claves
    letras = collections.Counter()
    for enc, (clave, nombre) in MAPA.items():
        bl = TOMO[clave]
        opciones = {}
        for i, b in enumerate(bl):
            if b[0] == 'item' and i + 1 < len(bl) and bl[i + 1][0] == 'opc':
                opciones[re.match(r'(\d+)\.', b[1]).group(1)] = bl[i + 1][1]
        for _, its in sol_seccion(enc)['bloques']:
            for n, resp, _ in its:
                m = re.match(r'([a-d])\) (.*)', resp)
                if m and n in opciones:
                    letras[m.group(1)] += 1
                    control('7. Exactitud de respuestas', opciones[n]['abcd'.index(m.group(1))] == m.group(2),
                            f'{nombre}, ítem {n}: la clave «{resp}» no coincide con la opción impresa')
    control('7. Exactitud de respuestas', max(letras.values()) - min(letras.get(x, 0) for x in 'abcd') <= 3,
            f'Claves desbalanceadas: {dict(letras)}')
    import figuras
    numerados = sorted(figuras.RIOS_NUMERADOS.items(), key=lambda x: x[1][0]) if hasattr(figuras, 'RIOS_NUMERADOS') else []
    resp_d = next(r for _, its in sol_seccion(30)['bloques'] for n, r, _ in its if n == '12')
    if numerados:
        esperado = [f'{num}: {rio}' for rio, (num, _) in numerados]
        control('7. Exactitud de respuestas', all(e in resp_d for e in esperado) and '4:' not in resp_d,
                f'Parte D: el solucionario no coincide con el mapa numerado {esperado}')

    # 8. figuras: numeración consecutiva, citas existentes y ninguna figura heredada del maestro
    todas = set()
    for clave in ('clase10', 'clase18', 'contF'):
        caps_fig = [re.match(r'Figura (\S+) —', b[2]).group(1) for b in TOMO[clave] if b[0] in ('fig', 'fig_original') and 'Figura' in b[2]]
        todas |= set(caps_fig)
        if caps_fig:
            pref = caps_fig[0].split('.')[0]
            esperado = [f'{pref}.{i}' for i in range(1, len(caps_fig) + 1)]
            control('8. Figuras', caps_fig == esperado, f'{clave}: numeración {caps_fig}, se esperaba {esperado}')
    for clave in ('clase10', 'clase18', 'contF', 'evalU5', 'ficha18A', 'fichasF'):
        t = ' '.join(textos(TOMO[clave]))
        refs = set(re.findall(r'Figuras? (\d+\.\d+|F\.\d)', t)) | set(re.findall(r'Figuras \S+ y (\d+\.\d+)', t))
        control('8. Figuras', refs <= todas, f'{clave}: cita figuras inexistentes {sorted(refs - todas)}')
    control('8. Figuras', not any(b[0] == 'fig_original' for k in TOMO for b in TOMO[k]),
            'El tomo todavía usa figuras heredadas del maestro (10.1 errónea; Hidrovía ilegible)')

    # 9. trazabilidad: JSON, matriz y plan anual
    tz = json.load(open(os.path.join(out, 'datos', 'trazabilidad_curricular.json')))
    enc = {e['encuentro']: e for e in tz['encuentros']}
    control('9. Trazabilidad curricular', len(enc) == 36, f'El JSON tiene {len(enc)} encuentros')
    control('9. Trazabilidad curricular', enc[22]['tipo_vinculo'] == 'Ampliación editorial' and not enc[22]['capacidades_mec'],
            'Continuación E no figura como ampliación editorial en el JSON')
    control('9. Trazabilidad curricular', enc[18]['capacidades_mec'] == ['H1', 'H2', 'H3', 'H4'],
            f'Integradora 1.ª etapa: {enc[18]["capacidades_mec"]}')
    control('9. Trazabilidad curricular', enc[36]['capacidades_mec'] == ['H5', 'H6', 'G1', 'G2', 'G3', 'G4'],
            f'Integradora 2.ª etapa: {enc[36]["capacidades_mec"]}')
    evals = [e for e in enc.values() if e['seccion'].startswith(('Evaluación', 'Integradora'))]
    control('9. Trazabilidad curricular', len(evals) == 8 and all(e['ficha_maestro_estado'] == 'sin_ficha' and
                                                               e['tipo_vinculo'] == 'Asociación curricular' for e in evals),
            'Las evaluaciones no figuran como «sin ficha» y «asociación curricular»')
    cnt = tz['conteo_fichas_maestro']
    control('9. Trazabilidad curricular', cnt.get('literal') == 16 and cnt.get('truncada') == 5 and cnt.get('abreviada') == 1 and
            cnt.get('editorial', 0) + cnt.get('variante', 0) == 6 and cnt.get('sin_ficha') == 8, f'Conteo de fichas: {cnt}')
    texto_pa = '\n'.join(p.text for p in pa.paragraphs) + '\n'.join(c.text for r in filas_pa for c in r.cells)
    for prohibido in ('priorización MEC', 'requerimiento curricular', 'sin contenido extracurricular'):
        control('9. Trazabilidad curricular', prohibido not in texto_pa, f'El plan anual todavía dice «{prohibido}»')
    fila = lambda n: next(r for r in filas_pa if r.cells[0].text.strip() == str(n))  # noqa: E731
    control('9. Trazabilidad curricular', 'H5, H6, G1, G2, G3 y G4' in fila(36).cells[6].text, 'Plan anual: cobertura de la fila 36')
    control('9. Trazabilidad curricular', 'H1, H2, H3 y H4' in fila(18).cells[6].text, 'Plan anual: cobertura de la fila 18')
    control('9. Trazabilidad curricular', fila(22).cells[6].text.startswith('Ampliación editorial'), 'Plan anual: fila 22')
    for n, clave in ((15, 'clase10'), (28, 'clase18'), (29, 'contF')):
        ficha = next(b for b in TOMO[clave] if b[0] == 'ficha')
        control('9. Trazabilidad curricular', ficha[2] in fila(n).cells[1].text and all(i in fila(n).cells[2].text for i in ficha[3]),
                f'Plan anual: la fila {n} no repite tema e indicadores de la ficha del tomo')
    mz = docx.Document(os.path.join(out, 'matriz', 'MATRIZ_CURRICULAR_36_ENCUENTROS_M3.docx'))
    filas_mz = {r.cells[0].text: [c.text for c in r.cells] for r in mz.tables[1].rows}
    control('9. Trazabilidad curricular', filas_mz['22'][3] == 'Ampliación editorial', 'Matriz: tipo de vínculo de la fila 22')
    control('9. Trazabilidad curricular', filas_mz['36'][2] == 'H5, H6, G1, G2, G3, G4', 'Matriz: cobertura de la fila 36')
    for pl in PLANES:
        control('9. Trazabilidad curricular', pl['vinculo'].split(':')[0].split(' del')[0] in
                ('Capacidad literal', 'Asociación curricular') and enc[pl['n']]['tipo_vinculo'].startswith(pl['vinculo'][:10]),
                f'Plan {pl["n"]}: el vínculo «{pl["vinculo"][:40]}» no coincide con el JSON')

    # 10. evaluación equitativa
    p30 = next(p for p in PLANES if p['n'] == 30)
    sec30 = ' '.join(x for _, pasos in p30['secuencia'] for paso in pasos for x in paso)
    control('10. Evaluación equitativa', not re.search(r'autocorrec|corrigen con|con (?:la|las) claves?|claves? en voz|entrega (?:la|las) claves?', sec30, re.I) and
            'sin claves' in sec30 and 'encuentro 31' in ' '.join(p30['funciones'].values()),
            'Plan 30: se entregan o comentan claves antes de que terminen todos')
    control('10. Evaluación equitativa', 'Todo lo que necesitás está en esta prueba' in ' '.join(textos(ev)) and
            sum(1 for b in ev if b[0] == 'fig') == 2, 'La evaluación no trae sus dos mapas')

    # 11. integridad visual: huecos residuales
    pdfs = {'tomo': ('tomo', 'TOMO_MUESTRA3_oficio.pdf'), 'planes': ('planes', 'PLANES_MUESTRA3_A4.pdf'),
            'solucionario': ('solucionario', 'SOLUCIONARIO_MUESTRA3_A4.pdf')}
    rangos = json.load(open(os.path.join(out, 'datos', 'paginas_tomo.json')))
    for k, (carp, nom) in pdfs.items():
        d = pymupdf.open(os.path.join(out, carp, nom))
        if k == 'tomo':
            revisar = sorted({p for a, b in rangos.values() for p in range(a, b + 1)})
            finales = {b for a, b in rangos.values()}
        elif k == 'planes':
            inicios = [n for n in range(d.page_count) if re.search(r'^Plan de Clase N\.º \d+$', d[n].get_text(), re.M) and n > 1]
            revisar = list(range(3, d.page_count + 1))
            finales = {i for i in inicios} | {d.page_count}   # la hoja anterior a un plan nuevo (n.º de página = índice) es final de plan
        else:
            revisar, finales = list(range(1, d.page_count + 1)), {d.page_count}
        for n in revisar:
            pg = d[n - 1]
            alto = pg.rect.height
            ys = [b[3] for b in pg.get_text('blocks') if b[3] < alto * 0.93] + [r.y1 for img in pg.get_images() for r in pg.get_image_rects(img[0])] + [dr['rect'].y1 for dr in pg.get_drawings() if dr['rect'].y1 < alto * 0.93]
            uso = (max(ys) / alto) if ys else 0
            minimo = 0.25 if n in finales else 0.55   # la última hoja de una sección puede ser corta, pero no residual
            control('11. Integridad visual', uso > minimo, f'{nom}, pág. {n}: solo {uso:.0%} de la hoja con contenido')

    print(f'Controles correctos: {ok[0]}. Fallos: {len(fallos)}.')
    for k, (n, fs) in informe.items():
        print(f'  {k}: {n} correctos, {len(fs)} fallos')
    for f in fallos:
        print(' -', f)
    print('Distribución de claves de opción múltiple:', dict(sorted(letras.items())))
    json.dump({'correctos': ok[0], 'fallos': fallos, 'por_control': {k: {'correctos': n, 'fallos': fs} for k, (n, fs) in informe.items()},
               'claves': dict(sorted(letras.items()))},
              open(os.path.join(out, 'datos', 'controles_muestra3.json'), 'w'), ensure_ascii=False, indent=1)
    sys.exit(1 if fallos else 0)


if __name__ == '__main__':
    main()
