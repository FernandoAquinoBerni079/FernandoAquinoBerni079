# -*- coding: utf-8 -*-
"""Bloques del tomo vigente de Algorítmica 1.º (docx). Mismo formato que 2.º: h1 unidad/clase, h2 sección,
caja (título + cuerpo; líneas de código en monoespaciado marcadas con '§'), ficha, tabla, img (con epígrafe), banda."""
import docx, json, os, re
from docx.oxml.ns import qn
SRC = '/home/claude/alg1/src/Algoritmica_1er_Curso_TOMO_COMPLETO.docx'
FIG = '/home/claude/alg1/build/figs_src/'
MONO = ('Courier New', 'Consolas', 'Courier', 'Lucida Console', 'Cascadia Mono', 'DejaVu Sans Mono')
d = docx.Document(SRC)
rels = d.part.rels


def es_mono(p):
    rs = [r for r in p.runs if r.text.strip()]
    return bool(rs) and all((r.font.name or (r.style.font.name if r.style else None) or '') in MONO for r in rs)


CODE_RE = re.compile(r'^(Inicio$|Fin$|Algoritmo\b|FinAlgoritmo|Definir\b|Leer\b|Escribir\b|Si\b.*Entonces|Sino$|SiNo$|FinSi|Para\b.*Hacer|FinPara|Mientras\b.*Hacer|FinMientras|Repetir$|Hasta Que\b|Segun\b|FinSegun|De Otro Modo|//|[\w\[\]]+ (←|<-) )')


def es_codigo(line):
    if not line.strip():
        return False
    if line.startswith('  ') and len(line) < 90:
        return True
    return bool(CODE_RE.match(line.strip())) and len(line) < 90 and not line.strip().endswith(':')


def lineas_celda(cell):
    out = []
    for p in cell.paragraphs:
        for tx in p.text.replace('\t', '    ').split('\n'):
            if not tx.strip():
                continue
            out.append(('§' + tx.rstrip()) if (es_mono(p) or es_codigo(tx)) else tx.strip())
    return out


B = []; nfig = 0
for el in d.element.body.iterchildren():
    tag = el.tag.split('}')[1]
    if tag == 'p':
        p = docx.text.paragraph.Paragraph(el, d)
        blips = el.findall('.//' + qn('a:blip'))
        if blips:
            part = rels[blips[0].get(qn('r:embed'))].target_part
            nfig += 1
            name = 'src_%02d%s' % (nfig, os.path.splitext(part.partname)[1])
            open(FIG + name, 'wb').write(part.blob)
            ext = el.find('.//' + qn('wp:extent'))
            B.append({'t': 'img', 'file': name, 'ancho_cm': round(int(ext.get('cx')) / 360000, 2) if ext is not None else 15})
            continue
        st = p.style.name; tx = p.text.strip()
        if not tx or st.startswith('toc'):
            continue
        if st == 'Heading 1':
            m = re.match(r'UNIDAD (\d+) — (.+)', tx)
            B.append({'t': 'h1', 'text': ('Unidad %s — %s' % (m.group(1), m.group(2).capitalize())) if m else tx, 'raw': tx})
        elif st == 'Heading 2':
            B.append({'t': 'h1', 'text': tx})
        elif st == 'Heading 3':
            B.append({'t': 'h2' if not tx.startswith('Actividades') else 'h3', 'text': tx})
        elif re.match(r'^Figura \d+\.\d+ — ', tx) and B and B[-1]['t'] == 'img':
            B[-1]['epigrafe'] = tx; B[-1]['num_viejo'] = re.match(r'Figura (\d+\.\d+)', tx).group(1)
        elif es_mono(p):
            B.append({'t': 'code', 'text': p.text.rstrip()})
        else:
            B.append({'t': 'p', 'text': tx})
    elif tag == 'tbl':
        t = docx.table.Table(el, d)
        nr, nc = len(t.rows), len(t.columns)
        if nr == 3 and nc == 2 and t.rows[0].cells[0].text.strip() == 'Capacidad':
            inds = [x.lstrip('• ').strip() for x in t.rows[2].cells[1].text.split('\n') if x.strip()]
            B.append({'t': 'ficha', 'capacidad': t.rows[0].cells[1].text.strip(), 'tema': t.rows[1].cells[1].text.strip(), 'indicadores': inds})
        elif nr == 1 and nc == 1:
            ls = lineas_celda(t.rows[0].cells[0])
            if ls and ls[0].upper().startswith('EVALUACIÓN'):
                B.append({'t': 'banda', 'text': ' / '.join(ls[:2]), 'lines': ls})
            elif ls and ls[0].startswith('PRUEBA DIAGNÓSTICA'):
                B.append({'t': 'diag', 'lines': ls})
            else:
                B.append({'t': 'caja', 'title': ls[0].lstrip('§') if ls else '', 'body': ls[1:]})
        else:
            rows = []
            for r in t.rows:
                cells = []; prev = None
                for c in r.cells:
                    if c._tc is prev:
                        continue
                    prev = c._tc; cells.append(c.text.strip())
                rows.append(cells)
            B.append({'t': 'tabla', 'hdr': rows[0], 'rows': rows[1:]})
json.dump(B, open('/home/claude/alg1/build/tomo_blocks.json', 'w'), ensure_ascii=False, indent=1)
from collections import Counter
print(Counter(b['t'] for b in B), 'figs', nfig, 'sin epígrafe', [b['file'] for b in B if b['t'] == 'img' and 'epigrafe' not in b])
