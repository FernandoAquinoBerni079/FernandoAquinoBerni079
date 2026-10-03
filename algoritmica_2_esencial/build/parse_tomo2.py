# -*- coding: utf-8 -*-
"""Extrae los bloques del tomo vigente de Algorítmica 2.º. El .docx (8,1 MB) excede el conector de Drive:
la estructura se toma de la exportación de texto del .docx (markdown) y el contenido de los recuadros, con
sus saltos de línea y la sangría del pseudocódigo, del PDF de la misma edición (26/08/2026)."""
import re, json
import pymupdf

SRC = '/home/claude/alg2/src/'
MD = SRC + 'Algoritmica_2do_Curso_TOMO_COMPLETO.txt'
PDF = SRC + 'Algoritmica_2do_Curso_TOMO_COMPLETO.pdf'
OUT = '/home/claude/alg2/build/tomo_blocks.json'
FIGDIR = '/home/claude/alg2/build/figs_src/'

# figuras con epígrafe, en orden de aparición → xref del PDF (las tres imágenes sin epígrafe se descartan: T14)
FIG_XREF = {'1.1': 823, '1.2': 1433, '1.3': 2333, '1.4': 2423, '1.5': 2755, '2.1': 3020, '2.2': 3628, '2.3': 3950,
            '2.4': 4033, '2.5': 4607, '2.6': 4894, '3.1': 5225, '3.2': 6171, '4.1': 6452, '4.2': 6572, '4.3': 6836, '4.4': 7339}

CODE_RE = re.compile(r'^(Algoritmo\b|FinAlgoritmo|Definir\b|Leer\b|Escribir\b|Si\b.*Entonces$|Si\b.*Entonces\s+\S|Sino$|SiNo$|FinSi|Para\b.*Hacer$|FinPara|Mientras\b.*Hacer$|FinMientras|Repetir$|Hasta Que\b|Segun\b.*Hacer$|FinSegun|De Otro Modo|\d+:\s|Funcion\b|FinFuncion|SubProceso\b|FinSubProceso|Dimension\b|//|Abrir\b|Cerrar\b|[\w\[\],+\- ]+ <- )')


def limpiar_md(t):
    for a, b in (('\\<', '<'), ('\\>', '>'), ('\\_', '_'), ('\\*', '*'), ('\\=', '='), ('\\!', '!'), ('\\-', '-'),
                 ('\\.', '.'), ('\\#', '#'), ('\\[', '['), ('\\]', ']'), ('\\+', '+'), ('\\|', '¦')):
        t = t.replace(a, b)
    t = t.replace('\\\\', '\\')
    return t


def despace(s):
    return re.sub(r'\s+', '', s)


def pdf_lineas():
    d = pymupdf.open(PDF)
    L = []
    for pn, p in enumerate(d):
        for b in p.get_text('dict')['blocks']:
            for l in b.get('lines', []):
                sp = l['spans']
                txt = ''.join(s['text'] for s in sp)
                if re.match(r'^Página \d+ de \d+$', txt.strip()) or not txt.strip():
                    continue
                bold = all(('Bold' in s['font']) for s in sp if s['text'].strip())
                L.append({'pag': pn + 1, 'x': l['bbox'][0], 'txt': txt.rstrip(), 'bold': bold})
    return L


def es_codigo(line):
    s = line.rstrip()
    if not s.strip():
        return False
    if s.startswith('  '):
        return True
    return bool(CODE_RE.match(s.strip())) and len(s) < 95


def caja_desde_pdf(celda, PL, desde):
    """Busca en las líneas del PDF el recuadro cuyo texto (sin espacios) es `celda`; devuelve (título, cuerpo, idx)."""
    meta = despace(celda)
    for i in range(desde, len(PL)):
        if not PL[i]['bold']:
            continue
        if not meta.startswith(despace(PL[i]['txt'])[:12]):
            continue
        acc = ''; j = i; lines = []
        while j < len(PL) and meta.startswith(acc + despace(PL[j]['txt'])) and len(acc) < len(meta):
            acc += despace(PL[j]['txt']); lines.append(PL[j]); j += 1
        if acc == meta:
            return lines, j
    return None, desde


def armar_caja(lines, celda):
    # título: líneas en negrita al comienzo
    k = 0; tit = []
    while k < len(lines) and lines[k]['bold']:
        tit.append(lines[k]['txt'].strip()); k += 1
    titulo = ' '.join(tit).strip()
    body = []; prosa = ''
    md = celda
    for ln in lines[k:]:
        t = ln['txt']
        if es_codigo(t):
            if prosa:
                body.append(prosa.strip()); prosa = ''
            body.append('§' + t.replace('\t', '    '))
        else:
            # ¿continúa el párrafo anterior? si en el md hay un espacio antes de esta línea, es un renglón partido
            if prosa:
                pos = md.find(t.strip()[:25])
                junta = pos > 0 and md[pos - 1] == ' '
                if junta:
                    prosa += ' ' + t.strip()
                else:
                    body.append(prosa.strip()); prosa = t.strip()
            else:
                prosa = t.strip()
    if prosa:
        body.append(prosa.strip())
    if titulo.endswith('—'):
        titulo = titulo.rstrip(' —')
    return titulo, body


def tabla_md(rows):
    cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
    cells = [c for c in cells if not all(re.match(r'^:?-+:?$', x) for x in c if x)]
    return cells


def main():
    md = limpiar_md(open(MD).read())
    md = md[md.find('# Prueba diagnóstica'):]
    PL = pdf_lineas()
    lines = md.split('\n')
    B = []; i = 0; pdf_pos = 0; perdidas = []
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1; continue
        m = re.match(r'^(#{1,3}) (.+)$', ln)
        if m:
            B.append({'t': 'h%d' % len(m.group(1)), 'text': m.group(2).strip()}); i += 1; continue
        if ln.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append(lines[i]); i += 1
            cells = tabla_md(rows)
            ncol = max(len(r) for r in cells)
            if ncol == 1 or all(len([x for x in r if x]) <= 1 for r in cells):
                for r in cells:
                    c = r[0].replace('¦', '|')
                    if not c:
                        continue
                    if c.startswith(('EVALUACIÓN', 'EVALUACION')):
                        B.append({'t': 'banda', 'text': c}); continue
                    lns, j = caja_desde_pdf(c, PL, pdf_pos)
                    if lns:
                        tit, body = armar_caja(lns, c); pdf_pos = j
                    else:
                        perdidas.append(c[:60])
                        if ' — ' in c:
                            tit, rest = c.split(' — ', 1); body = [rest]
                        else:
                            tit, body = c, []
                    if tit in ('Concepto clave', 'En Paraguay') or (body and tit.startswith(('Concepto clave —', 'En Paraguay —'))):
                        pass
                    B.append({'t': 'caja', 'title': tit, 'body': body})
                continue
            if cells and cells[0][0] == '' and len(cells) > 1 and cells[1][0] == 'Capacidad':
                cells = cells[1:]
            if cells and cells[0][0] == 'Capacidad':
                d = {r[0]: r[1] for r in cells}
                inds = [x.strip() for x in d['Indicadores de logro'].split('•') if x.strip()]
                B.append({'t': 'ficha', 'capacidad': d['Capacidad'], 'tema': d['Tema'], 'indicadores': inds}); continue
            hdr = [x.replace('¦', '|') for x in cells[0]]
            B.append({'t': 'tabla', 'hdr': hdr, 'rows': [[x.replace('¦', '|') for x in r] for r in cells[1:]]}); continue
        mf = re.match(r'^Figura (\d\.\d) — (.+)$', ln)
        if mf:
            B.append({'t': 'img', 'file': 'fig_%s.jpg' % mf.group(1).replace('.', '_'), 'epigrafe': ln.strip(), 'num_viejo': mf.group(1)}); i += 1; continue
        # párrafo (las líneas con dos espacios finales son un bloque de código del md)
        par = [ln]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(('|', '#')) and lines[i - 1].endswith('  '):
            par.append(lines[i].rstrip()); i += 1
        if len(par) > 1:
            B.append({'t': 'code_md', 'lines': [p.rstrip() for p in par]})
        else:
            B.append({'t': 'p', 'text': ln.strip()})
    # figuras
    d = pymupdf.open(PDF)
    import os
    os.makedirs(FIGDIR, exist_ok=True)
    for num, x in FIG_XREF.items():
        info = d.extract_image(x)
        open(FIGDIR + 'fig_%s.jpg' % num.replace('.', '_'), 'wb').write(info['image'])
    json.dump(B, open(OUT, 'w'), ensure_ascii=False, indent=1)
    print('bloques', len(B), 'cajas sin PDF:', len(perdidas))
    for p in perdidas:
        print('  ', p)


if __name__ == '__main__':
    main()
