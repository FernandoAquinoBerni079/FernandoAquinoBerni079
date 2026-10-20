"""Construye un bloque de la producción anual: figuras, tomo, planes,
solucionario, PDF y copias livianas para revisión.

Uso: python3 construir_bloque.py BLOQUE MAESTRO.docx CARPETA_GEOJSON

Salida en `bloque_N/`:
- tomo/TOMO_BLOQUE_N_legal.docx y .pdf
- planes/PLANES_BLOQUE_N_A4.docx y .pdf
- solucionario/SOLUCIONARIO_BLOQUE_N_A4.docx y .pdf
- figuras/
- datos/paginas_tomo.json
- revision_liviana/

Con BLOQUE = «anual» construye los documentos consolidados de los 36
encuentros en `anual/` (solo con los cuatro bloques desarrollados).
"""
import importlib
import json
import os
import re
import sys

import pymupdf

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
for sub in ('', 'motor', 'contenido', 'figuras'):
    sys.path.insert(0, os.path.join(AQUI, sub))
import curriculo as C  # noqa: E402
import pdf as PDF  # noqa: E402

ROMANOS = {1: 'I', 2: 'II', 3: 'III', 4: 'IV'}
PRIMERO_DE_UNIDAD = {1: 1, 6: 2, 10: 3, 19: 4, 26: 5, 31: 6}
PATRON_TITULOS = r'^(UNIDAD \d —|Clase \d+ —|Continuación [A-G] —|Ficha reproducible|EVALUACIÓN|Prueba diagnóstica$)'


def modulo(n):
    return importlib.import_module(f'e{n:02d}')


def vinculo_texto(e, plan):
    if plan.get('vinculo'):
        return plan['vinculo']
    caps = e['caps']
    if e['vinculo'] == C.LITERAL:
        pags = sorted({C.PAGINA_CAPACIDAD[c] for c in caps})
        return (f"Capacidad literal del programa MEC 2014 (pág. {', '.join(map(str, pags))}); el tema reproduce temas "
                f"del programa para esa capacidad.")
    if e['vinculo'] == C.ASOCIACION:
        return (f"Asociación curricular: la evaluación integra {', '.join(caps)}, capacidades literales del programa "
                f"MEC 2014; no tiene capacidad propia.")
    raise ValueError(f"El encuentro {e['n']} necesita un vínculo explícito en el plan")


def plan_completo(n):
    e, m = C.encuentro(n), modulo(n)
    pl = dict(m.PLAN)
    pl['n'] = pl['encuentro'] = n
    pl['titulo'] = m.TITULO
    pl['unidad'] = C.UNIDADES[e['unidad']] if e['unidad'] else 'Integración de la etapa'
    if e['caps']:
        pl['capacidad'] = C.texto_capacidades(e['caps'])
    else:
        assert pl.get('capacidad'), 'la Clase 1 declara su formulación editorial'
    pl['vinculo'] = vinculo_texto(e, pl)
    return pl


def sol_completo(n):
    m = modulo(n)
    s = dict(m.SOL)
    s['encuentro'] = n
    s.setdefault('titulo', m.TITULO)
    s.setdefault('clave', m.CLAVE)
    if s.get('puntaje'):
        s.setdefault('total', f"Total: {s['puntaje']} puntos")
    return s


def secciones_tomo(ns):
    secs = []
    for n in ns:
        m = modulo(n)
        bloques = list(m.TOMO)
        if n in PRIMERO_DE_UNIDAD:
            u = PRIMERO_DE_UNIDAD[n]
            bloques = [('unidad', C.UNIDADES[u].replace('Unidad', 'UNIDAD', 1))] + bloques
        if getattr(m, 'DIAGNOSTICA', None):   # hoja propia antes de la Unidad 1 y de la Clase 1
            secs.append(list(m.DIAGNOSTICA))
        secs.append(bloques + list(getattr(m, 'FICHAS', [])))
    return secs


def rangos_pdf(pdf_path):
    ind = PDF.pagina_indice(pdf_path)
    pags = PDF.titulos_pdf(pdf_path, PATRON_TITULOS, ind + 1)
    total = pymupdf.open(pdf_path).page_count
    orden = sorted(pags.items(), key=lambda x: x[1])
    rangos = {}
    for k, (t, p) in enumerate(orden):
        fin = (orden[k + 1][1] - 1) if k + 1 < len(orden) else total
        if t.startswith('UNIDAD'):
            continue
        rangos[t] = (p, max(fin, p))
    # la prueba diagnóstica se aplica en el encuentro 1: las páginas de la Clase 1 la incluyen
    diag = rangos.get('Prueba diagnóstica')
    c1 = next((t for t in rangos if t.startswith('Clase 1 —')), None)
    if diag and c1:
        rangos[c1] = (diag[0], rangos[c1][1])
    return pags, rangos


def diferimientos(pdf_path, secciones, diferir, umbral=0.08):
    """Hojas con hueco al pie (más del 8 % del alto útil) dentro de una sección
    cuya hoja siguiente empieza con una figura: se calcula cuántos bloques de
    texto que siguen a la figura hacen falta para llenar el hueco (midiendo su
    alto en el PDF) y la figura se corre detrás de ellos. Un subtítulo nunca
    queda separado de su primer párrafo. Devuelve {archivo: bloques}."""
    import tomo as T

    def norm(x):
        return re.sub(r'\s+', ' ', x).strip()

    figs = {}   # epígrafe → (archivo, bloques movibles que siguen a la figura)
    for sec in secciones:
        for k, b in enumerate(sec):
            if b[0] != 'fig':
                continue
            sig = []
            for j, x in enumerate(sec[k + 1:], k + 1):
                if x[0] == 'renglones' and sec[j - 1][0] in ('fuente', 'ubicate'):
                    continue   # van dentro del recuadro: un solo bloque
                if x[0] not in T.MOVIBLES:
                    break
                sig.append(x)
            figs[norm(b[2])[:40]] = (b[1], sig)
    d = pymupdf.open(pdf_path)

    def contenido(pg):
        bl = []
        for b in pg.get_text('dict')['blocks']:
            t = norm(' '.join(''.join(s['text'] for s in l['spans']) for l in b.get('lines', []))) if b['type'] == 0 else None
            if t is not None and (not t or re.match(r'^Página \d+ de \d+$', t)):
                continue
            bl.append((b['bbox'][1], b['bbox'][3], t))
        return sorted(bl)

    paginas = [contenido(pg) for pg in d]
    fondo = max(b[1] for p in paginas for b in p)
    tope = min(p[0][0] for p in paginas if p)
    nuevo = dict(diferir)
    for i in range(PDF.pagina_indice(pdf_path) + 1, len(paginas) - 1):
        act, sig = paginas[i], paginas[i + 1]
        if not act or not sig or sig[0][2] is not None:
            continue   # la hoja siguiente no empieza con una imagen
        hueco = fondo - act[-1][1]
        if hueco < umbral * (fondo - tope):
            continue
        k_epi = next((k for k, b in enumerate(sig) if b[2] and b[2][:40] in figs), None)
        if k_epi is None:
            continue
        archivo, siguientes = figs[sig[k_epi][2][:40]]
        ya = diferir.get(archivo, 0)
        candidatos = siguientes[ya:]
        resto = sig[k_epi + 1:]
        tops = []
        for x in candidatos:   # ubicación de cada bloque en la hoja siguiente
            pt = norm(T.primer_texto(x))[:25]
            # un subtítulo y su primer párrafo pueden salir como un solo bloque de texto del PDF
            y = next((b[0] for b in resto if b[2] and pt in b[2] and (not tops or b[0] >= tops[-1])), None)
            if y is None:
                break
            tops.append(y)
        if not tops:
            continue
        fin_contenido = max(b[1] for b in sig)
        altos = [(tops[k + 1] if k + 1 < len(tops) else fin_contenido) - tops[k] for k in range(len(tops))]
        # los párrafos y las listas se pueden partir entre hojas; subtítulos, recuadros y tablas solo suben si entran enteros
        acum, k = 0, 0
        while k < len(altos) and acum < hueco - 6:
            if candidatos[k][0] not in ('p', 'lista', 'nota', 'tabla', 'fuente') and acum + altos[k] > hueco:
                break
            acum += altos[k]; k += 1
        while k and candidatos[k - 1][0] in ('h2', 'h3'):
            k -= 1   # un subtítulo no queda separado de su texto
        if k:
            nuevo[archivo] = ya + k
    return nuevo


def finales_residuales(pdf_path, secciones, minimo=0.30):
    """Índices de las secciones cuya última hoja (o la de una ficha propia) queda
    ocupada menos del 30 % de su alto."""
    _, rangos = rangos_pdf(pdf_path)
    d = pymupdf.open(pdf_path)
    alto = d[0].rect.height
    titulos = []
    for i, s in enumerate(secciones):
        for b in s:
            if b[0] in ('h1', 'ficha_repro') or (b[0] == 'banda'):
                titulos.append((b[1], i))
    out = set()
    for t, (a, z) in rangos.items():
        if t == 'Prueba diagnóstica' or a == z:
            continue
        pg = d[z - 1]
        ys = [b[3] for b in pg.get_text('blocks') if b[3] < alto * 0.94] + [r.y1 for r in (x['rect'] for x in pg.get_drawings()) if r.y1 < alto * 0.94]
        if ys and max(ys) / alto < minimo:
            i = next((i for tt, i in titulos if t.startswith(tt[:40]) or tt.startswith(t[:40])), None)
            if i is not None:
                out.add(i)
    return out


def huecos_internos(pdf_path, secciones, umbral=0.15):
    """Índices de las secciones con alguna hoja que no es la última y queda vacía
    en más del 15 % de su alto útil."""
    _, rangos = rangos_pdf(pdf_path)
    d = pymupdf.open(pdf_path)
    alto = d[0].rect.height
    pie = min((b[1] for b in d[-1].get_text('blocks') if re.match(r'\s*Página \d+ de \d+\s*$', b[4])), default=alto * 0.94)
    titulos = [(b[1], i) for i, s in enumerate(secciones) for b in s if b[0] in ('h1', 'ficha_repro', 'banda')]
    out = set()
    for t, (a, z) in rangos.items():
        i = next((i for tt, i in titulos if t.startswith(tt[:40]) or tt.startswith(t[:40])), None)
        if i is None:
            continue
        for n in range(a, z):
            pg = d[n - 1]
            ys = [b[3] for b in pg.get_text('blocks') if b[3] < pie - 1] + [x['rect'].y1 for x in pg.get_drawings() if x['rect'].y1 < pie - 1]
            if ys and (pie - max(ys)) / pie > umbral:
                out.add(i)
    return out


def construir_tomo(maestro, figuras, ns, dx):
    import docx
    import tomo as T
    import tomo_piloto as TP
    secs = secciones_tomo(ns)
    diferir, ajustes = {}, {}
    for _ in range(5):   # secciones cuya última hoja quedaría casi vacía: ajuste fino y se vuelve a calcular
        for _ in range(7):   # corre figuras hasta que no quedan huecos evitables
            T.construir(maestro, figuras, secs, dx, None, diferir, ajustes)
            pdf = PDF.render(dx)
            nuevo = diferimientos(pdf, secs, diferir)
            if nuevo == diferir:
                break
            diferir = nuevo
        residuales = finales_residuales(pdf, secs)
        cambia = False
        for i in huecos_internos(pdf, secs):   # airear no puede abrir un hueco dentro de la sección
            if ajustes.get(i) == 'airear':
                ajustes[i] = 'airear final'; cambia = True   # solo la segunda mitad de la sección
            elif ajustes.get(i) == 'airear final':
                ajustes[i] = 'sin ajuste'; cambia = True
        for i in residuales:   # primero se aprieta; si no alcanza, se airea
            if ajustes.get(i) is None:
                ajustes[i] = 'apretar'; cambia = True
            elif ajustes[i] == 'apretar':
                ajustes[i] = 'airear'; cambia = True
        if not cambia:
            break
    print('figuras corridas detrás del texto:', diferir)
    print('secciones con ajuste fino:', ajustes)
    ind = PDF.pagina_indice(pdf)
    pags = PDF.titulos_pdf(pdf, PATRON_TITULOS, ind + 1)
    # El índice estático puede ocupar más de una hoja (tomo anual) y correr la paginación: se itera hasta que
    # los números impresos en el índice coinciden con la paginación real.
    for _ in range(4):
        d = docx.Document(dx)
        claves = {}
        for e in d.element.body:
            t = TP.texto(e) if TP.es_p(e) else (TP.texto(e.find('.//' + TP.W + 'p')) if e.tag == TP.W + 'tbl' else '')
            for k, v in pags.items():
                if t and t.startswith(k[:40]):
                    claves[t] = v
        T.construir(maestro, figuras, secs, dx, claves, diferir, ajustes)
        pdf = PDF.render(dx)
        pags2, rangos = rangos_pdf(pdf)
        if pags2 == pags:
            return pdf, rangos
        pags = pags2
    raise AssertionError('el índice no estabiliza la paginación')


def construir_planes(ns, dx, subtitulo):
    import planes as P
    planes = [plan_completo(n) for n in ns]
    P.construir(planes, dx, {}, subtitulo)
    pdf = PDF.render(dx)
    d = pymupdf.open(pdf)
    pags = {}
    for k in range(2, d.page_count):
        for mm in re.finditer(r'Plan de Clase N\.º (\d+)\n', d[k].get_text()):
            pags.setdefault(f'Plan de Clase N.º {mm.group(1)}', k + 1)
    P.construir(planes, dx, pags, subtitulo)
    return PDF.render(dx)


def construir_solucionario(ns, rangos, figuras, dx, titulo):
    import solucionario as S
    import referencias_docente as RD
    S.construir([sol_completo(n) for n in ns], rangos, figuras, dx, titulo, referencias=(RD.INTRO, RD.REFERENCIAS) if len(ns) == 36 else None)   # COM-02: solo en el volumen anual
    return PDF.render(dx)


def main():
    arg, maestro, geo = sys.argv[1:4]
    if arg == 'anual':
        ns, nombre, carpeta = list(range(1, 37)), 'ANUAL', os.path.join(RAIZ, 'anual')
        sub = 'Colección anual · 36 encuentros'
        bloques_fig = [1, 2, 3, 4]
    else:
        b = int(arg)
        ns, nombre, carpeta = list(C.BLOQUES[b]), f'BLOQUE_{ROMANOS[b]}', os.path.join(RAIZ, f'bloque_{b}')
        if len(sys.argv) > 4:   # prueba parcial: solo algunos encuentros
            ns = [int(x) for x in sys.argv[4].split(',')]
        sub = f'Bloque {ROMANOS[b]} · encuentros {ns[0]} a {ns[-1]}'
        bloques_fig = [b]
    for s in ('tomo', 'planes', 'solucionario', 'figuras', 'datos', 'revision_liviana'):
        os.makedirs(os.path.join(carpeta, s), exist_ok=True)
    fig = os.path.join(carpeta, 'figuras')
    for bf in bloques_fig:
        importlib.import_module(f'bloque{bf}').generar(geo, fig)
    tpdf, rangos = construir_tomo(maestro, fig, ns, os.path.join(carpeta, 'tomo', f'TOMO_{nombre}_legal.docx'))
    json.dump(rangos, open(os.path.join(carpeta, 'datos', 'paginas_tomo.json'), 'w'), ensure_ascii=False, indent=1)
    ppdf = construir_planes(ns, os.path.join(carpeta, 'planes', f'PLANES_{nombre}_A4.docx'), sub)
    spdf = construir_solucionario(ns, rangos, fig, os.path.join(carpeta, 'solucionario', f'SOLUCIONARIO_{nombre}_A4.docx'),
                                  f'Solucionario docente — {sub}')
    for p in (tpdf, ppdf, spdf):
        dst = os.path.join(carpeta, 'revision_liviana', os.path.basename(p)[:-4] + '_REVISION.pdf')
        print(os.path.basename(p), pymupdf.open(p).page_count, 'págs.;', os.path.getsize(p), 'bytes; liviano', PDF.liviano(p, dst))
    traz = []
    for n in ns:
        e, m = C.encuentro(n), modulo(n)
        bl = list(getattr(m, 'DIAGNOSTICA', [])) + list(m.TOMO) + list(getattr(m, 'FICHAS', []))
        traz.append({'encuentro': n, 'seccion': m.TITULO, 'tipo': e['tipo'], 'tipo_vinculo': e['vinculo'],
                     'capacidades_mec': e['caps'], 'temas_mec': e['temas'],
                     'ficha_impresa': any(x[0] == 'ficha' for x in bl),
                     'paginas_tomo': next((v for t, v in rangos.items() if t.startswith(m.CLAVE)), None),
                     'pendientes_de_verificacion': [list(v) for v in getattr(m, 'VERIFICACION', [])]})
    json.dump({'programa': 'MEC (2014), Programa de Estudio: Historia y Geografía, 7.º grado, EEB (reproducción, SHA-256 389190d3…c8d27e)',
               'encuentros': traz}, open(os.path.join(carpeta, 'datos', 'trazabilidad.json'), 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(rangos, ensure_ascii=False))


if __name__ == '__main__':
    main()
