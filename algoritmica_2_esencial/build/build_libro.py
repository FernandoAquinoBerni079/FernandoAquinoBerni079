# -*- coding: utf-8 -*-
"""Arma Algoritmica_2do_Curso_LIBRO_ESENCIAL_COMERCIAL_2026.docx (Clase N → Práctica N), en dos pasadas
para poblar el índice con números de página reales (verificados contra el PDF)."""
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)) + ('/..' if 'portadas' in __file__ else '')); import rutas as RT
import os, re, subprocess, sys, json
import maqueta as M
from estructura import cargar
import ediciones, actividades, practicas, evaluaciones, preliminares as PRE

B = RT.B
OUT = RT.OUT
os.makedirs(OUT, exist_ok=True)
NOMBRE = 'Algoritmica_2do_Curso_LIBRO_ESENCIAL_COMERCIAL_2026'
FIG_SRC = B + 'figs_src/'; FIG_NEW = B + 'figs_new/'
PFI_FIG = FIG_NEW + 'fig_pfi_caja.png'
PFI_FIG2 = FIG_SRC + 'fig_pfi_der.png'

pre, C, EV_OLD, U = cargar()
ediciones.aplicar(C)
FIGMAP = ediciones.fig_refs(C)
TIT_CLASE = {n: C[n]['titulo'] for n in C}
EVS = evaluaciones.EV


# v1.2 (hallazgo 02 de la auditoría): secciones que se componen en modo compacto porque su última hoja quedaba
# casi vacía. La lista la calcula el propio build (ver __main__) midiendo el PDF; se guarda en ajustes_paginacion.json.
# Nivel 1 («compacto»): interlineado sencillo y figuras al 90 % en esa sección. Nivel 2 («sin_salto»): si aun así queda
# residuo, la sección siguiente (sólo una Práctica o una Clase, nunca una evaluación ni el PFI) empieza en esa misma hoja.
AJ_PATH = B + 'ajustes_paginacion.json'
_aj = json.load(open(AJ_PATH)) if os.path.exists(AJ_PATH) else {}
AJUSTES = set(_aj.get('compacto', []))
COMPACTO2 = set(_aj.get('compacto2', []))
COMPACTO3 = set(_aj.get('compacto3', []))  # nivel 2 cuando la sección siguiente no puede subir (evaluación, fin del libro)
SIN_SALTO = set(_aj.get('sin_salto', []))


def nivel(clave):
    return 3 if clave in COMPACTO3 else 2 if clave in COMPACTO2 else (1 if clave in AJUSTES else 0)


def clave_seccion(titulo):
    if titulo.startswith(('Clase ', 'Práctica ')):
        return titulo.split(' — ')[0]
    if titulo.startswith('Proyecto Final Integrador'):
        return 'Proyecto Final Integrador'
    return titulo


def toc_entries():
    E = [(1, 'Prueba diagnóstica — ¿Qué sabés ya?')]
    for n in range(1, 22):
        u = C[n]['unidad']
        if n == min(k for k in C if C[k]['unidad'] == u):
            E.append((1, 'UNIDAD %d — %s' % (u, U[u])))
        E.append((2, 'Clase %d — %s' % (n, TIT_CLASE[n])))
        E.append((2, 'Práctica %d — %s' % (n, practicas.PR[n]['titulo'])))
        for e in EVS:
            if e['tras'] == n:
                E.append((2, e['titulo']))
    E.append((1, 'Proyecto Final Integrador — El sistema de gestión de un emprendimiento'))
    return E


def bloque_cuerpo(d, b):
    t = b['t']
    if t == 'h2':
        M.heading(d, b['text'], 3)
    elif t == 'p':
        txt = b['text']
        ind = 0.3 if re.match(r'^\d+\. ', txt) else None
        M.par(d, txt, indent=ind)
    elif t == 'caja':
        M.caja(d, b['title'], b['body'])
    elif t == 'tabla':
        M.tabla(d, b['hdr'], b['rows'])
    elif t == 'img':
        ruta = (FIG_NEW if b.get('nueva') else FIG_SRC) + b['file']
        M.imagen(d, ruta, b['epigrafe'], b.get('ancho_cm', 15.5), lead=b.get('lead'))
    else:
        raise ValueError(t)


def clase(d, n, salto=True):
    c = C[n]
    h = M.heading(d, 'Clase %d — %s' % (n, c['titulo']), 2, salto=salto and 'Clase %d' % n not in SIN_SALTO)
    if 'Clase %d' % n in SIN_SALTO:
        h.paragraph_format.space_before = M.Pt(20)
    f = c['ficha']
    M.ficha(d, f['capacidad'], f['tema'], f['indicadores'])
    for b in c['cuerpo']:
        bloque_cuerpo(d, b)
    M.heading(d, 'Actividades de aplicación', 4)
    for rot, hdr, rows in actividades.DATOS.get(n, []):
        M.tabla(d, hdr, rows, rotulo=rot)
    fam_prev = None
    for fam, k, enun, resp, nuevo in actividades.items(n):
        if fam != fam_prev:
            M.par(d, fam + ':', 10, True, color=M.MED, keep=True, antes=4, despues=2)
            fam_prev = fam
        M.par(d, '%d. %s' % (k, enun), 10, indent=0.4, despues=3)


def practica(d, n):
    p = practicas.PR[n]
    h = M.heading(d, 'Práctica %d — %s' % (n, p['titulo']), 2, salto='Práctica %d' % n not in SIN_SALTO)
    if 'Práctica %d' % n in SIN_SALTO:
        h.paragraph_format.space_before = M.Pt(20)
    M.linea_nombre(d)
    M.caja(d, 'Competencia de la práctica', [p['competencia'], 'Entorno de trabajo: %s.' % p['entorno']])
    M.par(d, 'Lo que necesitás saber', 10.5, True, color=M.MED, keep=True, antes=2, despues=2)
    for s in p['saber']:
        M.par(d, s, 10)
    M.par(d, p['antes'], 10, italic=True, color=M.MED, despues=6)
    for k, a in enumerate(p['acts'], 1):
        M.par(d, 'Actividad %d — %s' % (k, a['titulo']), 11, True, color=M.DARK, keep=True, antes=6, despues=2)
        pp = M.par(d, '', 10, keep=True)
        M.run(pp, 'Objetivo: ', True, size=10); M.run(pp, a['objetivo'], italic=True, size=10)
        if a.get('modelo'):
            tit, lineas = a['modelo']
            mono = tit.startswith('Esqueleto')
            M.caja(d, 'Modelo — ' + tit, lineas, mono=mono)
        M.par(d, 'Pasos:', 10, True, keep=True, despues=1)
        for i, s in enumerate(a['pasos'], 1):
            M.par(d, '%d. %s' % (i, s), 10, indent=0.4, despues=2)
        t = d.add_table(rows=1, cols=1)
        M.bordes(t, 'A5D6A7', '6'); M.margenes_celda(t, 70, 110)
        c = t.rows[0].cells[0]; M.shd(c, 'EEF7EE')
        q = c.paragraphs[0]; q.paragraph_format.space_after = M.Pt(0)
        M.run(q, 'Punto de control: ', True, size=10, color=M.DARK); M.run(q, a['control'], size=10)
        M.ancho_fijo(t, [M.ANCHO]); M.cant_split(t)
        M.separador(d, 4)
    if p.get('transfer'):
        tr = p['transfer']
        M.par(d, 'Transferencia y revisión entre pares (30 a 40 minutos)', 11, True, color=M.DARK, keep=True, antes=6, despues=2)
        pp = M.par(d, '', 10, keep=True)
        M.run(pp, 'Objetivo: ', True, size=10); M.run(pp, 'aplicar lo mismo a un segundo caso, con datos diferentes, y mejorar el trabajo con la revisión de otro equipo.', italic=True, size=10)
        M.caja(d, 'Modelo — Mini-caso: ' + tr['caso'][0], tr['caso'][1])
        M.par(d, 'Pasos:', 10, True, keep=True, despues=1)
        for i, s in enumerate(tr['pasos'], 1):
            M.par(d, '%d. %s' % (i, s), 10, indent=0.4, despues=2)
        t = d.add_table(rows=1, cols=1)
        M.bordes(t, 'A5D6A7', '6'); M.margenes_celda(t, 70, 110)
        c = t.rows[0].cells[0]; M.shd(c, 'EEF7EE')
        q = c.paragraphs[0]; q.paragraph_format.space_after = M.Pt(0)
        M.run(q, 'Punto de control: ', True, size=10, color=M.DARK); M.run(q, tr['control'], size=10)
        M.ancho_fijo(t, [M.ANCHO]); M.cant_split(t)
        M.separador(d, 4)
    M.par(d, 'Desafío final (para quienes terminan antes)', 10.5, True, color=M.MED, keep=True, antes=4, despues=2)
    M.par(d, p['desafio'], 10)
    if p.get('datos'):
        M.par(d, 'Datos para cargar', 11, True, color=M.DARK, keep=True, antes=8, despues=2)
        for rot, hdr, rows in p['datos']:
            M.tabla(d, hdr, rows, rotulo=rot)


LARGO = re.compile(r'algoritmo|procedimiento|Ordená|prueba de escritorio|Definí una función|referencias cruzadas|Formulá')
RENGLONES_LARGO = 6


def evaluacion(d, e):
    M.salto(d)
    dos_col = M.COMPACTO
    M.banda(d, e['titulo'], e['sub'], M.AZUL if e['etapa'] else M.AMB)
    if e.get('base'):
        M.caja(d, e['base'][0], e['base'][1], fill='F5F5F5', color_tit=M.DARK)
    M.par(d, 'Parte A — Diagnóstico rápido (marcá la opción correcta):', 10.5, True, color=M.DARK, keep=True, antes=2)
    k = 0
    for enun, ops, _ in e['mc']:
        k += 1
        M.par(d, '%d. %s' % (k, enun), 10, keep=True, despues=1)
        if dos_col:
            # v1.2: opciones en dos columnas (a y b en una línea, c y d en la siguiente), misma letra
            mitad = M.ANCHO / 2
            for j in range(0, len(ops), 2):
                pp = M.par(d, '', 10, indent=0.8, despues=1, keep=(j + 2 < len(ops)), align='l')
                pp.paragraph_format.tab_stops.add_tab_stop(M.Cm(mitad))
                M.run(pp, '%s) %s' % ('abcd'[j], ops[j]), size=10)
                if j + 1 < len(ops):
                    M.run(pp, '\t%s) %s' % ('abcd'[j + 1], ops[j + 1]), size=10)
        else:
            for j, o in enumerate(ops):
                M.par(d, '%s) %s' % ('abcd'[j], o), 10, indent=0.8, despues=1, keep=(j < len(ops) - 1))
        M.separador(d, 2)
    M.par(d, 'Parte B — Resolución y aplicación:', 10.5, True, color=M.DARK, keep=True, antes=4)
    for enun, _ in e['ab']:
        k += 1
        M.par(d, '%d. %s' % (k, enun), 10, keep=True, despues=2)
        # v1.2: espacio de respuesta proporcional a la tarea (escribir un algoritmo no entra en 3 renglones)
        M.renglones(d, RENGLONES_LARGO if LARGO.search(enun) else 3)


def pfi(d):
    M.heading(d, 'Proyecto Final Integrador — El sistema de gestión de un emprendimiento', 1, salto=True)
    for t in PRE.PFI_INTRO:
        M.par(d, t)
    M.heading(d, 'Competencia integradora', 3)
    M.par(d, PRE.PFI_COMPETENCIA)
    M.heading(d, 'Lo que aportás desde Algorítmica', 3)
    for t in PRE.PFI_APORTES:
        M.par(d, '• ' + t, indent=0.3, despues=2)
    M.imagen(d, PFI_FIG, PRE.PFI_FIG_EPI, 11.5, lead=PRE.PFI_FIG_LEAD)
    M.heading(d, 'Requisitos mínimos de la solución', 3)
    M.tabla(d, ['Componente', 'Qué debe tener'], [list(x) for x in PRE.PFI_REQUISITOS], anchos=[3.6, 13.0])
    pp = M.par(d, '', 10.5)
    ext, resto = PRE.PFI_EXTENSION.split(': ', 1)
    M.run(pp, ext + ': ', True, color=M.DARK); M.run(pp, resto)
    M.imagen(d, PFI_FIG2, PRE.PFI_FIG2_EPI, 14.0, lead=PRE.PFI_FIG2_LEAD)
    M.heading(d, 'Etapas del proyecto', 3)
    M.tabla(d, ['Taller', 'Qué hacés'], [list(x) for x in PRE.PFI_ETAPAS], anchos=[5.2, 11.4])
    M.heading(d, 'Trabajo interdisciplinario: qué aporta cada materia', 3)
    M.tabla(d, ['Materia', 'Aporte a la solución digital'], [list(x) for x in PRE.PFI_INTERDISCIPLINA], anchos=[4.6, 12.0])
    M.heading(d, 'Qué entrega el equipo', 3)
    for t in PRE.PFI_ENTREGABLES:
        M.par(d, '• ' + t, indent=0.3, despues=2)
    M.heading(d, 'Pautas para el equipo', 3)
    for t in PRE.PFI_PAUTAS:
        M.par(d, '• ' + t, indent=0.3, despues=2)


def construir(paginas=None):
    d = M.nuevo_doc('Algorítmica · 2.º Curso · Libro del estudiante con prácticas de laboratorio',
                    'Edición Esencial Comercial 2026', 'Algorítmica; BTI; 2.º Curso; algoritmos; PSeInt; archivos; Access')
    M.imagen_pagina_completa(d, B + 'portadas/portada_libro.jpg')
    cuerpo = M.portada_en_seccion(d)
    M.heading(d, 'Presentación', 1, estilo='Título preliminar')
    for t in PRE.PRESENTACION:
        M.par(d, t)
    M.par(d, 'Cómo está organizado este libro', 11, True, color=M.DARK, keep=True, antes=8)
    M.tabla(d, ['Pieza', 'Qué encontrás'], [list(x) for x in PRE.COMO_USAR], anchos=[3.8, 12.8])
    M.heading(d, 'Índice', 1, salto=True, estilo='Título preliminar')
    E = toc_entries()
    M.indice(d, E, paginas)
    # prueba diagnóstica
    M.heading(d, 'Prueba diagnóstica — ¿Qué sabés ya?', 1, salto=True)
    M.linea_nombre(d)
    M.par(d, PRE.DIAGNOSTICA_INTRO, 10, italic=True)
    for i, (q, _) in enumerate(PRE.DIAGNOSTICA, 1):
        M.par(d, '%d. %s' % (i, q), 10.5, keep=True, antes=4, despues=2)
        M.renglones(d, 2)
    for n in range(1, 22):
        u = C[n]['unidad']
        primera = n == min(k for k in C if C[k]['unidad'] == u)
        if primera:
            M.heading(d, 'UNIDAD %d — %s' % (u, U[u]), 1, salto=True)
            M.par(d, PRE.UNIDADES[u], 10.5, italic=True, despues=6)
        M.COMPACTO = nivel('Clase %d' % n)
        clase(d, n, salto=not primera)
        M.COMPACTO = nivel('Práctica %d' % n)
        practica(d, n)
        for e in EVS:
            if e['tras'] == n:
                M.COMPACTO = nivel(e['titulo'])
                evaluacion(d, e)
    M.COMPACTO = nivel('Proyecto Final Integrador')
    pfi(d)
    M.COMPACTO = False
    M.pie_paginas(d, cuerpo)
    M.seccion_sin_pie(d)
    M.imagen_pagina_completa(d, B + 'portadas/contraportada.jpg', 'Contraportada')
    M.no_actualizar_campos(d)
    M.purgar_relaciones(d)
    return d, E


def a_pdf(docx_path, outdir):
    env = dict(os.environ, HOME='/tmp/lohome')
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', outdir, docx_path], check=True, env=env,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=600)
    return os.path.join(outdir, os.path.basename(docx_path)[:-5] + '.pdf')


def componer(tmp):
    d, E = construir(None)
    p1 = tmp + NOMBRE + '.docx'; d.save(p1)
    pdf1 = a_pdf(p1, tmp)
    import pymupdf
    doc = pymupdf.open(pdf1)
    idx_last = max(i for i, pg in enumerate(doc) if re.search(r'\.{5,}\s*000', pg.get_text())) + 1
    pags, total = M.paginas_de(pdf1, [t for _, t in E], desde=idx_last + 1)
    print('pasada 1: páginas', total, 'índice termina en', idx_last)
    for it in range(3):
        d, E = construir(pags)
        out = OUT + NOMBRE + '.docx'; d.save(out)
        pdf = a_pdf(out, OUT)
        pags2, total = M.paginas_de(pdf, [t for _, t in E], desde=idx_last + 1)
        if pags2 == pags:
            break
        pags = pags2
    return d, E, pags, total, pdf, pags2 == pags


def residuales(pdf, E, pags, umbral=0.30):
    """Secciones cuya página (no la primera) queda ocupada por debajo del umbral."""
    import ocupacion
    occ = {x[0]: x for x in ocupacion.medir(pdf)}
    inicio = [(p, t) for p, (_, t) in zip(pags, E) if not t.startswith('UNIDAD')]
    res = []
    for p0, (pg, uso, pal, txt) in ((k, occ[k]) for k in sorted(occ)):
        if uso >= umbral or (pal == 0 and uso == 0) or pg <= inicio[0][0] or pg == len(occ):
            continue
        prev = [t for p, t in inicio if p <= pg]
        if not prev:
            continue
        res.append((pg, uso, clave_seccion(prev[-1])))
    return res


if __name__ == '__main__':
    tmp = B + 'tmp/'; os.makedirs(tmp, exist_ok=True)
    for ronda in range(6):
        d, E, pags, total, pdf, ok = componer(tmp)
        res = residuales(pdf, E, pags)
        print('ronda', ronda, 'páginas', total, 'residuales', [(p, round(u, 2), k) for p, u, k in res])
        claves = [clave_seccion(t) for _, t in E if not t.startswith('UNIDAD')]
        cambio = False
        for _, _, k in res:
            if k not in AJUSTES:
                AJUSTES.add(k); cambio = True
            else:
                sig = claves[claves.index(k) + 1] if claves.index(k) + 1 < len(claves) else ''
                if sig.startswith(('Práctica ', 'Clase ')) and sig not in SIN_SALTO:
                    SIN_SALTO.add(sig); cambio = True
                elif not sig.startswith(('Práctica ', 'Clase ')) and k not in COMPACTO2:
                    COMPACTO2.add(k); cambio = True
                elif k.startswith(('Práctica ', 'Clase ')) and k not in SIN_SALTO:
                    SIN_SALTO.add(k); cambio = True   # la sección sube a la última hoja de la anterior
                elif k not in COMPACTO3:
                    COMPACTO3.add(k); cambio = True
        if not cambio:
            break
        json.dump({'compacto': sorted(AJUSTES), 'compacto2': sorted(COMPACTO2), 'compacto3': sorted(COMPACTO3), 'sin_salto': sorted(SIN_SALTO)}, open(AJ_PATH, 'w'), ensure_ascii=False, indent=1)
    json.dump({'entradas': E, 'paginas': pags, 'total': total}, open(B + 'indice_libro.json', 'w'), ensure_ascii=False, indent=1)
    print('final: páginas', total, 'índice verificado =', ok, 'secciones compactas', len(AJUSTES), 'residuales', len(res))
