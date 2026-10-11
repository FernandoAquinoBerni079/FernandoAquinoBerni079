# -*- coding: utf-8 -*-
"""Convierte el TOMO y el LABORATORIO originales (.docx) en archivos de texto editables (src_md/),
uno por bloque (clase, práctica, ficha, evaluación…), y extrae las imágenes sin tocarlas (figs_src/).

Marcado (una línea por elemento):
  ## Título de sección          (Heading 3 dentro de la clase)
  [[FICHA]] / Capacidad: … / Tema: … / - indicador / [[/FICHA]]
  [[CAJA Título]] líneas del cuerpo [[/CAJA]]
  [[TABLA]] fila | fila … (la primera es el encabezado) [[/TABLA]]
  [[IMG archivo|ancho_cm]] seguida de la línea del epígrafe
  cualquier otra línea: párrafo
"""
import os, re, sys, hashlib, docx
from docx.oxml.ns import qn

ORIG = '/home/claude/sw2/orig/'
OUT = '/home/claude/sw2/src_md/'
FIG = '/home/claude/sw2/build/figs_src/'
os.makedirs(OUT, exist_ok=True); os.makedirs(FIG, exist_ok=True)
EMU = 360000


def txt(el):
    out = []
    for x in el.iter(qn('w:t'), qn('w:br'), qn('w:tab')):
        if x.tag == qn('w:t'):
            out.append(x.text or '')
        elif x.tag == qn('w:tab'):
            out.append('\t')
        else:
            out.append(' / ')
    return ''.join(out)


def estilo(p):
    if p.pPr is not None and p.pPr.pStyle is not None:
        return p.pPr.pStyle.val
    return 'Normal'


def celdas(tr):
    res = []
    for tc in tr.findall(qn('w:tc')):
        ps = tc.findall(qn('w:p'))
        res.append([txt(p) for p in ps])
    return res


def volcar(path, pref, hashes):
    d = docx.Document(path)
    rels = d.part.rels
    lineas = []
    for el in d.element.body:
        if el.tag == qn('w:p'):
            blips = list(el.iter(qn('a:blip')))
            if blips:
                for b in blips:
                    part = rels[b.get(qn('r:embed'))].target_part
                    h = hashlib.sha256(part.blob).hexdigest()
                    if h in hashes:
                        nombre = hashes[h]
                    else:
                        nombre = pref + os.path.basename(part.partname)
                        open(FIG + nombre, 'wb').write(part.blob)
                        hashes[h] = nombre
                    ext = next(el.iter(qn('wp:extent')))
                    ancho = round(int(ext.get('cx')) / EMU, 1)
                    lineas.append('[[IMG %s|%s]]' % (nombre, ancho))
                if txt(el).strip():
                    lineas.append(txt(el).strip())
                continue
            st = estilo(el); t = txt(el).rstrip()
            if st.startswith('TDC'):
                continue
            if st == 'Ttulo1':
                lineas.append('@@H1 ' + t)
            elif st == 'Ttulo2':
                lineas.append('@@H2 ' + t)
            elif st == 'Ttulo3':
                lineas.append('## ' + t)
            elif t.strip():
                lineas.append(t)
        elif el.tag == qn('w:tbl'):
            rows = el.findall(qn('w:tr'))
            cs = [celdas(r) for r in rows]
            if len(rows) == 1 and len(cs[0]) == 1:
                ps = [x for x in cs[0][0] if x.strip()]
                if not ps:
                    continue
                # caja: primer párrafo = título (puede venir pegado al cuerpo en la misma línea)
                lineas.append('[[CAJA %s]]' % ps[0])
                lineas.extend(ps[1:])
                lineas.append('[[/CAJA]]')
            elif len(rows) == 3 and len(cs[0]) == 2 and ''.join(cs[0][0]).strip().startswith('Capacidad'):
                lineas.append('[[FICHA]]')
                lineas.append('Capacidad: ' + ' '.join(x for x in cs[0][1] if x.strip()))
                lineas.append('Tema: ' + ' '.join(x for x in cs[1][1] if x.strip()))
                for x in cs[2][1]:
                    for i in re.split(r'•', x):
                        if i.strip():
                            lineas.append('- ' + i.strip())
                lineas.append('[[/FICHA]]')
            else:
                lineas.append('[[TABLA]]')
                for r in cs:
                    lineas.append(' | '.join(' / '.join(x.strip() for x in c if x.strip()) for c in r))
                lineas.append('[[/TABLA]]')
    return lineas


def partir(lineas, reglas, prefijo):
    """Corta la secuencia en archivos según las líneas que empiezan un bloque."""
    actual = prefijo + '00_preliminares'; buf = {actual: []}; orden = [actual]
    for l in lineas:
        nuevo = reglas(l)
        if nuevo:
            actual = nuevo
            if actual not in buf:
                buf[actual] = []; orden.append(actual)
        buf[actual].append(l)
    for k in orden:
        open(OUT + k + '.md', 'w').write('\n'.join(buf[k]).strip() + '\n')
    return orden


def reglas_tomo(l):
    m = re.match(r'@@H2 Clase (\d+) —', l)
    if m:
        return 'tomo_clase%02d' % int(m.group(1))
    if l.startswith('@@H1 UNIDAD'):
        return 'tomo_unidad%s' % ('1' if 'UNIDAD 1' in l else '2')
    if l.startswith('[[CAJA EVALUACIÓN DE LA UNIDAD 1'):
        return 'tomo_eval_u1'
    if l.startswith('[[CAJA EVALUACIÓN INTEGRADORA · 1.ª'):
        return 'tomo_integ1'
    if l.startswith('[[CAJA EVALUACIÓN DE LA UNIDAD 2'):
        return 'tomo_eval_u2'
    if l.startswith('[[CAJA EVALUACIÓN INTEGRADORA · 2.ª'):
        return 'tomo_integ2'
    if l.startswith('## Caso integrador — El presupuesto'):
        return 'tomo_caso1'
    if l.startswith('## Caso integrador — La red'):
        return 'tomo_caso2'
    if l.startswith('## Prueba diagnóstica'):
        return 'tomo_diagnostica'
    return None


def reglas_lab(l):
    m = re.match(r'@@H1 Práctica (\d+) —', l)
    if m:
        return 'lab_practica%02d' % int(m.group(1))
    m = re.match(r'@@H1 Ficha ([A-L]) —', l)
    if m:
        return 'lab_ficha_%s' % m.group(1)
    if l.startswith('@@H1 Proyecto Final'):
        return 'lab_pfi'
    return None


if __name__ == '__main__':
    hashes = {}
    T = volcar(ORIG + 'GabineteSoftware_2do_Curso_TOMO_V2.3_ENRIQUECIDO_GRAFICO.docx', 'T_', hashes)
    L = volcar(ORIG + 'GabineteSoftware_2do_Curso_LABORATORIO_V2.3_ENRIQUECIDO_GRAFICO.docx', 'L_', hashes)
    print(partir(T, reglas_tomo, 'tomo_'))
    print(partir(L, reglas_lab, 'lab_'))
    print('imágenes únicas', len(hashes))
