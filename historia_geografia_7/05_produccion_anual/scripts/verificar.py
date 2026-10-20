"""Controles automáticos de la producción anual (extiende `04_muestra3/scripts/verificar_muestra3.py`).

 1. Capacidades y temas: literales del programa MEC 2014; la ficha de cada
    clase y continuación reproduce la capacidad y los temas del encuentro; las
    evaluaciones no imprimen ficha.
 2. Tomo ↔ solucionario: cada ítem numerado, cada pregunta de fuente (F1…),
    el Ubicate (U) y la prueba diagnóstica (D1…) tienen respuesta; no sobran.
 3. Tomo ↔ planes: toda actividad citada existe y toda actividad está asignada.
 4. Funciones: tres categorías (esenciales, consolidación, complementarias o
    domiciliarias) y cada actividad en una sola.
 5. Secuencias: tramos contiguos de 0 a 120 con Inicio, Desarrollo y Cierre.
 6. Rúbricas: el criterio anunciado en el tomo se repite en el solucionario;
    no hay rúbricas no anunciadas; en las evaluaciones los puntajes impresos
    suman el total y la matriz ítem-capacidad-puntaje cubre todos los ítems con
    capacidades del encuentro y el mismo total.
 7. Claves: la respuesta coincide con la opción impresa; cuatro opciones
    distintas; sin «todas/ninguna de las anteriores»; en cada sección ninguna
    letra repetida tres veces seguidas ni más de la mitad de las claves.
 8. Figuras: numeración consecutiva por sección; citas existentes; archivo
    presente; ancho de impresión igual al del lienzo (los tamaños de letra de
    la figura son efectivos, A17).
 9. Trazabilidad: capacidad y vínculo del plan coherentes con la arquitectura.
10. Evaluación equitativa: en los planes de evaluación no se revelan claves
    mientras alguien sigue rindiendo y se define el tiempo adicional.
11. Integridad visual (A14): área realmente ocupada de cada hoja, hojas finales
    no residuales, títulos y bandas que no quedan solos al pie.
12. Voseo: sin formas de tuteo en el texto del estudiante.
13. Numeración de las actividades consecutiva en cada sección.

No reemplaza la revisión visual ni la de exactitud histórica y geográfica.

Uso: python3 verificar.py BLOQUE      (o «anual»)
"""
import collections
import importlib
import json
import os
import re
import sys
import unicodedata

import pymupdf

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
for sub in ('', 'motor', 'contenido', 'figuras'):
    sys.path.insert(0, os.path.join(AQUI, sub))
import curriculo as C  # noqa: E402
import construir_bloque as CB  # noqa: E402

fallos, ok = [], [0]
informe = collections.OrderedDict()
TUTEO = re.compile(r'\b(tú|tienes|puedes|crees|piensas|sabes|quieres|debes|eres|tuyo|tuya|contigo|escríbelo|explícalo|'
                   r'respóndelo|obsérvalo|anótalo)\b|(?:^|[.:;!?¿¡]\s*|^\d+\.\s+)(Escribe|Responde|Completa|Marca|Observa|Explica|'
                   r'Elige|Lee|Busca|Ubica|Compara|Dibuja|Piensa|Imagina|Recuerda|Señala|Subraya|Nombra|Ordena)\b', re.M)


def control(nombre, condicion, detalle):
    informe.setdefault(nombre, [0, []])
    if condicion:
        ok[0] += 1; informe[nombre][0] += 1
    else:
        fallos.append(f'[{nombre}] {detalle}'); informe[nombre][1].append(detalle)


def norm(s):
    s = unicodedata.normalize('NFC', s)
    s = re.sub(r'[•]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return re.sub(r'(\w)- (\w)', r'\1-\2', s)


def textos(x, out=None):
    out = [] if out is None else out
    if isinstance(x, str):
        out.append(x)
    elif isinstance(x, dict):
        for v in x.values():
            textos(v, out)
    elif isinstance(x, (list, tuple)):
        for y in x:
            textos(y, out)
    return out


def items(bloques):
    return [int(m.group(1)) for b in bloques if b[0] == 'item' for m in [re.match(r'(\d+)\.', b[1])] if m]


def numeros(frag):
    s = set()
    for a, b in re.findall(r'(\d+) a (\d+)', frag):
        s |= set(range(int(a), int(b) + 1))
    return s | {int(x) for x in re.findall(r'\d+', re.sub(r'\d+ a \d+', '', frag))}


def citados(texto):
    c = set()
    for m in re.finditer(r'actividad(?:es)? ([\d ,y a]+)', texto, re.I):
        c |= numeros(m.group(1))
    for m in re.finditer(r'consignas? (\d+ a \d+|\d+(?:, \d+)*(?: y \d+)?)', texto, re.I):
        c |= numeros(m.group(1))
    for m in re.finditer(r'ítems? (\d+ a \d+|\d+(?:, \d+)*(?: y \d+)?)', texto, re.I):
        c |= numeros(m.group(1))
    return c


def todos_bloques(m):
    return list(getattr(m, 'DIAGNOSTICA', [])) + list(m.TOMO) + list(getattr(m, 'FICHAS', []))


def aplanar(bloques):
    """Bloques de las fichas reproducibles incluidos."""
    out = []
    for b in bloques:
        out.append(b)
        if b[0] == 'ficha_repro':
            out.extend(aplanar(b[2]))
    return out


def verificar_encuentro(n, programa, figdir):
    e, m = C.encuentro(n), CB.modulo(n)
    bl = aplanar(todos_bloques(m))
    pl, sol = CB.plan_completo(n), CB.sol_completo(n)
    nom = f'E{n:02d}'
    es_eval = e['tipo'] in ('evaluacion', 'integradora')

    # 1. capacidades y fichas
    fichas = [b for b in bl if b[0] == 'ficha']
    if es_eval:
        control('1. Capacidades', not fichas, f'{nom}: una evaluación no imprime ficha de capacidad')
    else:
        control('1. Capacidades', len(fichas) == 1, f'{nom}: debe tener exactamente una ficha')
        if fichas and e['caps']:
            control('1. Capacidades', fichas[0][1] == C.texto_capacidades(e['caps']), f'{nom}: capacidad de la ficha no literal')
            esperado = ' '.join(C.TEMAS[t] for t in e['temas'])
            control('1. Capacidades', fichas[0][2] == esperado, f'{nom}: el tema de la ficha no reproduce los temas del programa')
        for c in ([fichas[0][1]] if fichas and e['caps'] else []) + [pl['capacidad']] * bool(e['caps']):
            for frase in re.split(r'(?<=\.)\s+', c):
                control('1. Capacidades', norm(frase) in programa, f'{nom}: «{frase}» no está en el programa')
        if fichas:
            control('1. Capacidades', fichas[0][3] == pl['indicadores'], f'{nom}: los indicadores del plan y de la ficha difieren')

    # 13. numeración consecutiva
    nums = items(bl)
    control('13. Numeración', nums == list(range(1, len(nums) + 1)), f'{nom}: numeración {nums}')

    # 2. tomo ↔ solucionario
    claves_sol = [num for _, its in sol['bloques'] for num, _, _ in its]
    esperadas = [str(k) for k in nums]
    for b in bl:
        if b[0] == 'fuente':
            esperadas += [f'F{k}' for k in range(1, len(b[4]) + 1)]
        if b[0] == 'ubicate':
            esperadas.append('U')
        if b[0] == 'recuadro' and b[1].startswith('Prueba diagnóstica'):
            esperadas += [f'D{k}' for k in range(1, len(b[2]) + 1)]
    faltan = sorted(set(esperadas) - set(claves_sol))
    sobran = sorted(set(claves_sol) - set(esperadas) - {'—'})
    dobles = sorted(k for k, v in collections.Counter(claves_sol).items() if v > 1 and k != '—')
    control('2. Tomo ↔ solucionario', not faltan and not sobran and not dobles,
            f'{nom}: faltan {faltan}; sobran {sobran}; repetidas {dobles}')

    # 3 y 4. planes
    texto_plan = ' '.join(x for _, pasos in pl['secuencia'] for paso in pasos for x in paso) + ' ' + pl['tarea']
    cit = citados(texto_plan) | (set(nums) if es_eval else set())
    control('3. Tomo ↔ planes', cit == set(nums), f'{nom}: inexistentes {sorted(cit - set(nums))}; sin asignar {sorted(set(nums) - cit)}')
    if not es_eval:
        por_cat = {k: citados(v) for k, v in pl['funciones'].items()}
        cuenta = collections.Counter(x for v in por_cat.values() for x in v)
        dobles = sorted(x for x, k in cuenta.items() if k > 1)
        control('4. Funciones', set(cuenta) == set(nums) and not dobles,
                f'{nom}: sin función {sorted(set(nums) - set(cuenta))}; en dos {dobles}; inexistentes {sorted(set(cuenta) - set(nums))}')
        control('4. Funciones', [k.split()[0] for k in pl['funciones']] == ['Esenciales', 'Consolidación', 'Complementarias'],
                f'{nom}: categorías {list(pl["funciones"])}')

    # 5. secuencia
    tramos = [tuple(int(x) for x in p[0].split('–')) for _, pasos in pl['secuencia'] for p in pasos]
    contigua = all(tramos[i][1] == tramos[i + 1][0] for i in range(len(tramos) - 1))
    momentos = [mo for mo, _ in pl['secuencia']]
    control('5. Secuencias', tramos[0][0] == 0 and tramos[-1][1] == 120 and contigua and all(a < b for a, b in tramos)
            and momentos == ['Inicio', 'Desarrollo', 'Cierre'], f'{nom}: tramos {tramos}; momentos {momentos}')

    # 6. rúbricas
    crit = {num: norm(c) for _, its in sol['bloques'] for num, _, c in its}
    for b in bl:
        if b[0] != 'item':
            continue
        k = re.match(r'(\d+)\.', b[1]).group(1)
        mm = re.search(r'se tendrá en cuenta(?: \([^)]*\))?:? (.*?)\)?\.?$', b[1], re.I)
        if mm:
            anunciado = norm(mm.group(1)).rstrip('.)')
            control('6. Rúbricas', anunciado in crit.get(k, '') and crit[k].startswith('Criterio anunciado'),
                    f'{nom}, ítem {k}: el solucionario no repite el criterio impreso «{anunciado[:60]}»')
    for k, c in crit.items():
        control('6. Rúbricas', 'Rúbrica' not in c, f'{nom}, {k}: rúbrica no anunciada en el tomo')
    if es_eval:
        txt = ' '.join(textos(bl))
        total = int(re.search(r'Puntaje total: (\d+)', txt).group(1))
        partes = []
        for b in bl:
            if b[0] == 'consigna':
                mm = re.match(r'Parte ([A-H]) — .*?\((\d+(?:,\d+)?) puntos?( cada una)?', b[1])
                if mm:
                    partes.append((mm.group(1), float(mm.group(2).replace(',', '.')), bool(mm.group(3))))
        suma = 0
        for i, (letra, pts, cada) in enumerate(partes):
            ini = next(j for j, b in enumerate(bl) if b[0] == 'consigna' and b[1].startswith(f'Parte {letra}'))
            fin = next((j for j, b in enumerate(bl) if j > ini and b[0] == 'consigna' and b[1].startswith('Parte ')), len(bl))
            k_items = sum(1 for b in bl[ini:fin] if b[0] == 'item')
            suma += pts * (k_items if cada else 1)
        control('6. Rúbricas', abs(suma - total) < 0.01 and sol.get('puntaje') == total,
                f'{nom}: las partes suman {suma}, el total impreso es {total} y el solucionario dice {sol.get("puntaje")}')
        mz = sol.get('matriz', [])
        en_matriz = set()
        for item, cap, _, pts in mz:
            en_matriz |= numeros(item)
            control('6. Rúbricas', all(c.strip() in e['caps'] for c in cap.split(',')),
                    f'{nom}: la matriz asigna {cap}, que no es capacidad del encuentro')
        control('6. Rúbricas', en_matriz == set(nums) and abs(sum(x[3] for x in mz) - total) < 0.01,
                f'{nom}: matriz ítem-capacidad-puntaje incompleta o con otro total')
        cubre = {c.strip() for _, cap, _, _ in mz for c in cap.split(',')}
        control('6. Rúbricas', cubre == set(e['caps']), f'{nom}: la evaluación no cubre {sorted(set(e["caps"]) - cubre)}')

    # 7. claves
    opciones = {}
    for i, b in enumerate(bl):
        if b[0] == 'item' and i + 1 < len(bl) and bl[i + 1][0] == 'opc':
            ops = bl[i + 1][1]
            k = re.match(r'(\d+)\.', b[1]).group(1)
            opciones[k] = ops
            control('7. Claves', len(ops) == 4 and len(set(ops)) == 4 and not any(re.search(r'anteriores', o, re.I) for o in ops),
                    f'{nom}, ítem {k}: opciones mal formadas')
    letras = []
    for _, its in sol['bloques']:
        for k, resp, _ in its:
            mm = re.match(r'([a-d])\) (.*)', resp)
            if mm and k in opciones:
                letras.append(mm.group(1))
                control('7. Claves', opciones[k]['abcd'.index(mm.group(1))] == mm.group(2),
                        f'{nom}, ítem {k}: la clave no coincide con la opción impresa')
    control('7. Claves', set(opciones) <= {k for _, its in sol['bloques'] for k, r, _ in its if re.match(r'[a-d]\) ', r)},
            f'{nom}: opción múltiple sin clave')
    if len(letras) >= 3:
        racha = any(letras[i] == letras[i + 1] == letras[i + 2] for i in range(len(letras) - 2))
        mayor = max(collections.Counter(letras).values())
        control('7. Claves', not racha and mayor <= len(letras) / 2, f'{nom}: claves {"".join(letras)}')

    # 8. figuras
    caps_fig = [re.match(r'Figura (\S+) —', b[2]).group(1) for b in bl if b[0] == 'fig' and b[2].startswith('Figura')]
    if caps_fig:
        pref = caps_fig[0].split('.')[0]
        control('8. Figuras', caps_fig == [f'{pref}.{i}' for i in range(1, len(caps_fig) + 1)], f'{nom}: numeración {caps_fig}')
    txt = ' '.join(textos(bl))
    refs = set(re.findall(r'Figuras? (\d+\.\d+|[A-G]\.\d)', txt)) | set(re.findall(r'Figuras \S+ y (\d+\.\d+|[A-G]\.\d)', txt))
    previas = set()   # se pueden citar figuras de encuentros anteriores (por ejemplo, en una continuación)
    for k in range(1, n + 1):
        try:
            mk = CB.modulo(k)
        except ImportError:
            continue
        previas |= {re.match(r'Figura (\S+) —', x[2]).group(1) for x in aplanar(todos_bloques(mk))
                    if x[0] == 'fig' and x[2].startswith('Figura')}
    control('8. Figuras', refs <= previas, f'{nom}: cita figuras inexistentes {sorted(refs - previas)}')
    from PIL import Image
    for b in bl:
        if b[0] == 'fig':
            ruta = os.path.join(figdir, b[1])
            control('8. Figuras', os.path.exists(ruta), f'{nom}: falta {b[1]}')
            if os.path.exists(ruta):
                im = Image.open(ruta)
                dpi = im.info.get('dpi', (300, 300))[0]
                ancho_lienzo = im.size[0] / dpi * 2.54
                control('8. Figuras', abs(b[3] - ancho_lienzo) / ancho_lienzo < 0.04,
                        f'{nom}: {b[1]} se imprime a {b[3]} cm y se dibujó a {ancho_lienzo:.1f} cm (letra no efectiva)')
    for archivo, ancho, _ in sol.get('mapas', []):
        control('8. Figuras', os.path.exists(os.path.join(figdir, archivo)), f'{nom}: falta la clave gráfica {archivo}')

    # 9. trazabilidad
    control('9. Trazabilidad', pl['capacidad'] == (C.texto_capacidades(e['caps']) if e['caps'] else pl['capacidad']),
            f'{nom}: capacidad del plan')
    control('9. Trazabilidad', pl['vinculo'].startswith(e['vinculo'].split()[0]), f'{nom}: vínculo «{pl["vinculo"][:40]}»')

    # 10. equidad
    if es_eval:
        sec = ' '.join(x for _, pasos in pl['secuencia'] for paso in pasos for x in paso)
        control('10. Equidad', not re.search(r'autocorrec|corrigen con|con (?:la|las) claves?|claves? en voz|entrega (?:la|las) claves?', sec, re.I)
                and 'sin claves' in sec and re.search(r'tiempo adicional', ' '.join(textos(pl)), re.I),
                f'{nom}: posible revelación de claves o tiempo adicional sin definir')

    # 12. voseo
    for t in textos([b for b in bl if b[0] not in ('fig', 'nota', 'ficha')]):   # los indicadores van en tercera persona
        mm = TUTEO.search(t)
        control('12. Voseo', not mm, f'{nom}: forma de tuteo «{mm.group(0) if mm else ""}» en «{t[:60]}»')
    return {'items': len(nums), 'claves': letras}


def cobertura(pg):
    """Fracción de la altura útil cubierta por contenido (intervalos unidos si
    distan menos de 1 cm), sin contar el pie de página."""
    alto = pg.rect.height
    # límite: el borde superior del pie de página («Página N de M»); sin pie, el 94 % del alto (márgenes del oficio)
    pies = [b[1] for b in pg.get_text('blocks') if re.match(r'\s*(Página \d+ de \d+|.*· Página \d+)\s*$', b[4]) and b[1] > alto * 0.85]
    lim = min(pies) - 1 if pies else alto * 0.94
    iv = [(b[1], b[3]) for b in pg.get_text('blocks') if b[3] < lim]
    iv += [(r.y0, r.y1) for img in pg.get_images() for r in pg.get_image_rects(img[0]) if r.y1 < lim]
    iv += [(d['rect'].y0, d['rect'].y1) for d in pg.get_drawings() if d['rect'].y1 < lim]
    if not iv:
        return 0, 0
    iv.sort()
    gap = 28.35   # 1 cm en puntos
    tot, (a, b) = 0, iv[0]
    for x, y in iv[1:]:
        if x <= b + gap:
            b = max(b, y)
        else:
            tot += b - a; a, b = x, y
    tot += b - a
    util = lim - min(i[0] for i in iv)
    return tot / (lim - 0.04 * alto), max(i[1] for i in iv) / (lim / 0.94)


def verificar_pdf(ruta, finales, titulos, nombre, desde=1):
    d = pymupdf.open(ruta)
    for k in range(desde, d.page_count + 1):
        pg = d[k - 1]
        cub, ultimo = cobertura(pg)
        if k in finales:
            control('11. Integridad visual', ultimo > 0.25, f'{nombre}, pág. {k}: hoja final residual ({ultimo:.0%})')
        else:
            control('11. Integridad visual', cub > 0.5 and ultimo > 0.6,
                    f'{nombre}, pág. {k}: hoja con poco contenido (cubierta {cub:.0%}, último elemento {ultimo:.0%})')
        lineas = [l.strip() for l in pg.get_text().split('\n') if l.strip() and not l.strip().startswith('Página ')
                  and 'Planes de clase · Página' not in l and 'Solucionario docente · Página' not in l]
        if lineas:
            control('11. Integridad visual', lineas[-1] not in titulos, f'{nombre}, pág. {k}: «{lineas[-1][:50]}» queda solo al pie')


def main():
    arg = sys.argv[1]
    if arg == 'anual':
        ns, carpeta, nombre = list(range(1, 37)), os.path.join(RAIZ, 'anual'), 'ANUAL'
    else:
        b = int(arg)
        ns, carpeta, nombre = list(C.BLOQUES[b]), os.path.join(RAIZ, f'bloque_{b}'), f'BLOQUE_{CB.ROMANOS[b]}'
        if len(sys.argv) > 2:
            ns = [int(x) for x in sys.argv[2].split(',')]
    programa = norm(open(os.path.join(RAIZ, 'datos', 'programa_MEC_2014_HyG7_texto_extraido.txt'), encoding='utf-8').read())
    for c in list(C.CAPACIDADES.values()) + list(C.TEMAS.values()):
        control('1. Capacidades', norm(c) in programa, f'currículo: «{c[:50]}» no es literal')
    figdir = os.path.join(carpeta, 'figuras')
    todas = []
    for n in ns:
        r = verificar_encuentro(n, programa, figdir)
        todas += r['claves']
    if todas:
        cnt = collections.Counter(todas)
        control('7. Claves', max(cnt.values()) - min(cnt.get(x, 0) for x in 'abcd') <= max(3, len(todas) // 8),
                f'claves del bloque desbalanceadas {dict(cnt)}')
    # títulos que no pueden quedar solos al pie
    titulos = set()
    for n in ns:
        for b in aplanar(todos_bloques(CB.modulo(n))):
            if b[0] in ('h2', 'h3', 'consigna'):
                titulos.add(b[1])
    titulos |= {f'{mo} ({k} min)' for mo in ('Inicio', 'Desarrollo', 'Cierre') for k in range(1, 121)}
    titulos |= {'Capacidad, tema e indicadores', 'Actividades del tomo según su función', 'Secuencia didáctica (120 minutos)',
                'Atención a la diversidad', 'Evaluación', 'Precisiones para el docente', 'Tarea'}
    rangos = json.load(open(os.path.join(carpeta, 'datos', 'paginas_tomo.json')))
    tomo_pdf = os.path.join(carpeta, 'tomo', f'TOMO_{nombre}_legal.pdf')
    verificar_pdf(tomo_pdf, {b for a, b in rangos.values()}, titulos, os.path.basename(tomo_pdf),
                  desde=min(a for a, b in rangos.values()))
    planes_pdf = os.path.join(carpeta, 'planes', f'PLANES_{nombre}_A4.pdf')
    d = pymupdf.open(planes_pdf)
    inicios = [k for k in range(3, d.page_count + 1) if re.search(r'^Plan de Clase N\.º \d+$', d[k - 1].get_text(), re.M)]
    verificar_pdf(planes_pdf, {i - 1 for i in inicios[1:]} | {d.page_count}, titulos, os.path.basename(planes_pdf), desde=3)
    sol_pdf = os.path.join(carpeta, 'solucionario', f'SOLUCIONARIO_{nombre}_A4.pdf')
    verificar_pdf(sol_pdf, {pymupdf.open(sol_pdf).page_count}, titulos, os.path.basename(sol_pdf))

    print(f'Controles correctos: {ok[0]}. Fallos: {len(fallos)}.')
    for k, (c, fs) in informe.items():
        print(f'  {k}: {c} correctos, {len(fs)} fallos')
    for f in fallos:
        print(' -', f)
    print('Claves de opción múltiple:', dict(sorted(collections.Counter(todas).items())))
    json.dump({'correctos': ok[0], 'fallos': fallos,
               'por_control': {k: {'correctos': c, 'fallos': fs} for k, (c, fs) in informe.items()},
               'claves': dict(sorted(collections.Counter(todas).items()))},
              open(os.path.join(carpeta, 'datos', 'controles.json'), 'w'), ensure_ascii=False, indent=1)
    sys.exit(1 if fallos else 0)


if __name__ == '__main__':
    main()
