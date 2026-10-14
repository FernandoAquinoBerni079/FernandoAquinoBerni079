"""Construye las tres variantes del piloto del tomo en dos pasadas (la segunda
escribe el índice con los números de página medidos en la primera) y mide cada
página del PDF resultante.

Uso: python3 construir_tomo.py BASE.docx CARPETA_SALIDA
"""
import json
import os
import subprocess
import sys

import pymupdf

AQUI = os.path.dirname(os.path.abspath(__file__))
VARIANTES = ['oficio_actual', 'oficio_mejorado', 'a4_mejorado']


def render(docx_path, outdir):
    env = dict(os.environ, HOME='/tmp/lohome')
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', outdir, docx_path],
                   check=True, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=600)
    return os.path.join(outdir, os.path.basename(docx_path)[:-5] + '.pdf')


def paginas_de(pdf_path, secciones):
    """Página donde aparece cada título, buscando en orden a partir de la página 3
    (después de la página del índice)."""
    d = pymupdf.open(pdf_path)
    indice = next(n for n in range(d.page_count) if d[n].get_text().lstrip().startswith('Índice')
                  or '\nÍndice\n' in d[n].get_text())
    res, desde = {}, indice + 1
    for t in secciones:
        clave = t[:45]
        for n in range(desde, d.page_count):
            if clave in d[n].get_text().replace('\n', ' '):
                res[t] = n + 1
                desde = n
                break
    return res


def medir(pdf_path):
    """Para cada página: dónde empieza cada sección (fracción de altura) y qué
    fracción inferior queda en blanco."""
    d = pymupdf.open(pdf_path)
    filas = []
    for n, p in enumerate(d):
        H = p.rect.height
        pie = H - 45
        ys = [b[3] for b in p.get_text('blocks') if b[4].strip() and b[1] < pie]
        for im in p.get_images():
            ys += [r.y1 for r in p.get_image_rects(im[0])]
        ys += [dr['rect'].y1 for dr in p.get_drawings() if dr['rect'].y1 < pie]
        fondo = max(ys) if ys else 0
        tamaños = {}
        for b in p.get_text('dict')['blocks']:
            for l in b.get('lines', []):
                for s in l['spans']:
                    if s['text'].strip():
                        k = round(s['size'], 1)
                        tamaños[k] = tamaños.get(k, 0) + len(s['text'])
        filas.append({'pag': n + 1, 'blanco_inferior': round(max(0, 1 - fondo / pie), 2),
                      'letra_min': min(tamaños) if tamaños else None,
                      'letra_mayoritaria': max(tamaños, key=tamaños.get) if tamaños else None})
    return {'paginas': d.page_count, 'ancho_pt': round(d[0].rect.width), 'alto_pt': round(d[0].rect.height),
            'detalle': filas}


def main():
    base, out = sys.argv[1:3]
    os.makedirs(out, exist_ok=True)
    informe = {}
    for v in VARIANTES:
        dx = os.path.join(out, f'TOMO_PILOTO_{v}.docx')
        subprocess.run([sys.executable, os.path.join(AQUI, 'tomo_piloto.py'), base, v, dx], check=True)
        secciones = json.load(open(dx + '.secciones.json'))
        pdf = render(dx, out)
        pags = paginas_de(pdf, secciones)
        jp = dx + '.paginas.json'
        json.dump(pags, open(jp, 'w'), ensure_ascii=False, indent=1)
        subprocess.run([sys.executable, os.path.join(AQUI, 'tomo_piloto.py'), base, v, dx, jp], check=True)
        pdf = render(dx, out)
        pags2 = paginas_de(pdf, secciones)
        m = medir(pdf)
        m['indice_estable'] = pags == pags2
        m['secciones'] = pags2
        informe[v] = m
        os.remove(dx + '.secciones.json'); os.remove(jp)
    json.dump(informe, open(os.path.join(out, 'medicion_tomo.json'), 'w'), ensure_ascii=False, indent=1)
    for v, m in informe.items():
        print(v, m['paginas'], 'págs.', m['ancho_pt'], 'x', m['alto_pt'], 'índice estable:', m['indice_estable'])
        print('   ', m['secciones'])


if __name__ == '__main__':
    main()
