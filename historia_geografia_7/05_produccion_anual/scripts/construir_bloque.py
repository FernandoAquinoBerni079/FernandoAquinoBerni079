"""Construye un bloque de la producción anual: figuras, tomo, planes,
solucionario, PDF y copias livianas para revisión.

Uso: python3 construir_bloque.py BLOQUE MAESTRO.docx CARPETA_GEOJSON

Salida en `bloque_N/`:
- tomo/TOMO_BLOQUE_N_oficio.docx y .pdf
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
PATRON_TITULOS = r'^(UNIDAD \d —|Clase \d+ —|Continuación [A-G] —|Ficha reproducible|EVALUACIÓN)'


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
    return pags, rangos


def construir_tomo(maestro, figuras, ns, dx):
    import docx
    import tomo as T
    import tomo_piloto as TP
    T.construir(maestro, figuras, secciones_tomo(ns), dx)
    pdf = PDF.render(dx)
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
        T.construir(maestro, figuras, secciones_tomo(ns), dx, claves)
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
    tpdf, rangos = construir_tomo(maestro, fig, ns, os.path.join(carpeta, 'tomo', f'TOMO_{nombre}_oficio.docx'))
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
        bl = list(m.TOMO) + list(getattr(m, 'FICHAS', []))
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
