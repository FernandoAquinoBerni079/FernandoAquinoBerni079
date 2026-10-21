# -*- coding: utf-8 -*-
"""(Se llama armar_coleccion.py y no construir.py porque «construir» es el nombre del constructor de cada lote.)
Construye los tres documentos anuales de la colección desde las fuentes aprobadas de los seis lotes, en oficio O3
con márgenes espejados, en DOCX (entregable) y PDF (control):
  1. ADS_3BTI_LIBRO_ANUAL_ESTUDIANTE_OFICIO_O3: portada, índice general, preliminares del lote 1, las seis aperturas
     de unidad y los 18 capítulos, cada uno con la función de armado de su lote (construir_lN.capituloN), en un solo
     documento con paginación continua.
  2. ADS_3BTI_GUIA_DOCENTE_ANUAL_OFICIO_O3: portada, índice, parte general (texto nuevo) y seis partes, cada una armada
     por la guía aprobada de su lote (guia.construir / guia_uN.construir) dentro del mismo documento.
  3. ADS_3BTI_CUADERNO_ANUAL_PRACTICAS_OFICIO_O3: portada, índice y las prácticas de los Capítulos 1 a 15 y 17, con la
     función de práctica de los lotes (las Prácticas 1 a 3 estaban solo en el libro del lote 1).
Ciclo de los lotes: el índice se calcula sobre el PDF hasta que la paginación queda estable, y el control de filas de
la candidata O3 manda a hoja nueva el rótulo de toda tabla a la que le falte alguna fila.
Las figuras se generan con los scripts de cada lote en coleccion/build/figs/ (no dentro de los lotes).
Uso: python3 -B coleccion/build/armar_coleccion.py   →  coleccion/*.docx, *.pdf y resultado_construccion.json"""
import os, sys, json, contextlib
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
COL = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
import fuentes as FU
import piezas_coleccion as PC
import guia_general as GG

O, L, G, D = FU.cargar()
H, M, K = O.H, O.M, O.K
Z3 = sys.modules['piezas_u3']   # encadenado de tablas largas (lotes 3 a 6)
FIGS = os.path.join(AQUI, 'figs')
RUTA = {'libro': os.path.join(COL, 'ADS_3BTI_LIBRO_ANUAL_ESTUDIANTE_OFICIO_O3.docx'),
        'guia': os.path.join(COL, 'ADS_3BTI_GUIA_DOCENTE_ANUAL_OFICIO_O3.docx'),
        'cuaderno': os.path.join(COL, 'ADS_3BTI_CUADERNO_ANUAL_PRACTICAS_OFICIO_O3.docx')}
PDF = {k: v[:-5] + '.pdf' for k, v in RUTA.items()}


# ---------------------------------------------------------------- figuras
def figuras():
    """Las figuras de cada lote, generadas con su script en coleccion/build/figs/lote_N/ (mismo código y datos)."""
    out = {}
    D[1].AQUI = os.path.join(FIGS, 'lote_1')   # diagramas.py del lote 1 escribe en AQUI/figs
    os.makedirs(os.path.join(FIGS, 'lote_1', 'figs'), exist_ok=True)
    riesgos = [(r[0], r[2], r[3]) for r in FU.capitulo(3).TABLA_34[1]]
    out[1] = D[1].generar(riesgos)
    for n in range(2, 7):
        d = os.path.join(FIGS, 'lote_%d' % n)
        os.makedirs(d, exist_ok=True)
        out[n] = D[n].generar(d)
    return out


# ---------------------------------------------------------------- libro del estudiante
def entradas_libro():
    e = []
    for n in range(1, 7):
        e += L[n].entradas_indice()   # el del lote 1 empieza con los títulos de los preliminares
    return e


def libro(figs, paginas):
    doc = H.new_doc()
    PC.portada(doc, 'libro')
    K.indice_marcador(doc)
    L[1].preliminares(doc)
    H.CLAVES.clear()
    for n in range(1, 7):
        L[n].apertura_unidad(doc)
        for c in FU.CAPITULOS[n]:
            getattr(L[n], 'capitulo%d' % c)(doc, figs[n])
    M.pegar_renglones(doc)
    Z3.encadenar_inicio(doc)
    K.saltos_a_titulos(doc)
    hechos = PC.aplicar_reemplazos(doc)
    entradas, movidas = PC.ordenar_por_documento(doc, entradas_libro())
    PC.rellenar_indice(doc, entradas, paginas)
    H.finalizar(doc, RUTA['libro'])
    return {'claves': list(H.CLAVES), 'reemplazos': hechos, 'entradas': entradas, 'indice_reordenado': movidas}


# ---------------------------------------------------------------- guía docente
@contextlib.contextmanager
def en_documento(doc, n):
    """La guía del lote n arma su contenido dentro de `doc`: H.new_doc devuelve ese documento, la portada del lote no
    se imprime (la colección tiene una sola) y H.finalizar no guarda (se guarda una vez, al final)."""
    zs = [m for m in (getattr(G[n], 'Z', None), K) if m is not None]
    previos = [(H, 'new_doc', H.new_doc), (H, 'finalizar', H.finalizar)] + [(m, 'portada', m.portada) for m in zs]
    H.new_doc = lambda: doc
    H.finalizar = lambda d, ruta: ruta
    for m in zs:
        m.portada = lambda *a, **k: None
    try:
        yield
    finally:
        for m, nombre, f in previos:
            setattr(m, nombre, f)


def _insertar_despues(doc, ancla, armar):
    """Arma un bloque al final del documento y lo mueve detrás del elemento `ancla`."""
    body = doc.element.body
    antes = len(list(body.iterchildren()))
    armar()
    nuevos = list(body.iterchildren())[antes - 1:-1]   # el último hijo es sectPr
    for el in reversed(nuevos):
        ancla.addnext(el)


def _cerrar_parte(doc, n):
    from docx.oxml.ns import qn
    viejo = PC.ENCABEZADO_GUIA_LOTE % n
    hs = [p for p in doc.paragraphs if p.style.name == 'Heading 1' and p.text == viejo]
    assert len(hs) == 1, (viejo, len(hs))
    h = hs[0]
    assert len(h.runs) == 1
    h.runs[0].text = PC.titulo_parte(n)
    h.paragraph_format.page_break_before = True
    if n in PC.NOTAS_PARTE:
        _insertar_despues(doc, h._p, lambda: H.caja(doc, *PC.NOTAS_PARTE[n], tipo='neutra'))


def entradas_guia(doc):
    e = []
    for p in doc.paragraphs:
        if p.style.name == 'Heading 1' and p.text != 'Índice':
            e.append((1, p.text))
        elif p.style.name == 'Heading 2':
            e.append((2, p.text))
    return e


def guia(res_libro, pag_libro, figs, instrumentos, paginas):
    doc = H.new_doc()
    PC.portada(doc, 'guia')
    K.indice_marcador(doc)
    GG.construir(doc, instrumentos)
    pags = dict(zip([t for _, t in res_libro['entradas']], pag_libro))
    for n in range(1, 7):
        with en_documento(doc, n):
            if n == 1:
                G[1].construir(RUTA['guia'], res_libro['claves'], pags, PC.ESTADO['guia'])
            else:
                G[n].construir(RUTA['guia'], res_libro['claves'], pags, PC.ESTADO['guia'], figs[n])
        _cerrar_parte(doc, n)
    M.pegar_renglones(doc)
    Z3.encadenar_inicio(doc)
    K.saltos_a_titulos(doc)
    e = entradas_guia(doc)
    PC.rellenar_indice(doc, e, paginas)
    H.finalizar(doc, RUTA['guia'])
    return {'entradas': e, 'instrumentos': instrumentos_de(doc)}


PATRONES_INSTRUMENTO = ('Rúbrica del H', 'Planilla de registro del H', 'Clave de la evaluación', 'Lista de cotejo de la Práctica',
                        'Rúbrica de defensa', 'Planilla de defensa', 'Rúbrica de producto final', 'Planilla anual',
                        'Fichas de recuperación', 'Registro de recuperaciones', 'Planilla de tiempos: ejemplo',
                        'Claves del diagnóstico')


def instrumentos_de(doc):
    """[(rótulo, parte)] de las tablas de instrumentos, en orden, con la parte de la guía a la que pertenecen."""
    from docx.oxml.ns import qn
    from docx.text.paragraph import Paragraph
    out, parte = [], None
    for el in doc.element.body.iterchildren():
        if el.tag != qn('w:p'):
            continue
        p = Paragraph(el, doc)
        if p.style.name == 'Heading 1' and p.text.startswith('Parte ') and not p.text.startswith('Parte general'):
            parte = p.text.split(' — ')[0].replace('Parte ', '')
        sig = el.getnext()
        if parte and any(p.text.startswith(pat) for pat in PATRONES_INSTRUMENTO) and sig is not None and sig.tag == qn('w:tbl'):
            out.append((p.text, parte))
    return out


def paginas_de_instrumentos(ruta_pdf, instrumentos):
    import re, pymupdf
    pdf = pymupdf.open(ruta_pdf)
    norm = lambda s: re.sub(r'\s+', ' ', s).strip()
    textos = [norm(pg.get_text()) for pg in pdf]
    # se busca desde la Parte I: la tabla de instrumentos de la parte general repite los rótulos
    inicio = PC.fin_del_indice(pdf) + 1
    desde = next(i for i in range(inicio, len(pdf)) if any(l.startswith('Parte I — ') for l in PC._lineas(pdf[i])))
    out = []
    for rot, parte in instrumentos:
        for i in range(desde, len(pdf)):
            if norm(rot) in textos[i]:
                out.append((rot, parte, i + 1)); desde = i
                break
        else:
            raise AssertionError('instrumento no encontrado en el PDF de la guía: %s' % rot)
    return out


# ---------------------------------------------------------------- cuaderno de prácticas
def _cuerpos_lote1():
    """Los cuerpos de las Prácticas 1 a 3: las mismas llamadas que hace lote_1/build/construir.py dentro de capitulo1 a
    capitulo3 (allí son funciones internas). La equivalencia comprueba que el texto sea idéntico al del libro."""
    MB = L[1].MB

    def p1(doc):
        K.tabla_codigos(doc, MB.VISITA_TITULO, MB.VISITA, anchos=(1.6, 11.6, 3.4), extra_col=('Clasificación',))

    def p2(doc):
        K.tabla_codigos(doc, MB.NORMAS_TITULO, MB.NORMAS, anchos=(1.8, 14.8))

    def p3(doc):
        K.tabla_codigos(doc, MB.DATOS_TITULO, MB.DATOS, anchos=(1.8, 14.8))
        M.tabla(doc, (['Cód.', 'Necesidad', 'De dónde sale'], [list(x) for x in MB.NECESIDADES]), [1.6, 9.6, 5.4],
                rotulo=MB.NECESIDADES_TITULO)
    return ((FU.capitulo(1), p1), (FU.capitulo(2), p2), (FU.capitulo(3), p3))


def practicas():
    """[(lote, módulo del capítulo, cuerpo)] en el orden del año."""
    out = [(1, C, f) for C, f in _cuerpos_lote1()]
    for n in range(2, 7):
        out += [(n, C, f) for C, f in L[n].PRACTICAS]
    return out


def entradas_cuaderno():
    e, visto = [], set()
    for n, C, _ in practicas():
        if n not in visto:
            e.append((1, PC.TITULOS_UNIDAD[n])); visto.add(n)
        e.append((2, C.PRACTICA_TITULO))
    return e


def cuaderno(paginas):
    doc = H.new_doc()
    PC.portada(doc, 'cuaderno')
    K.indice_marcador(doc)
    for n, C, cuerpo in practicas():
        L[n].practica(doc, C, cuerpo) if n > 1 else L[2].practica(doc, C, cuerpo)
    M.pegar_renglones(doc)
    Z3.encadenar_inicio(doc)
    K.saltos_a_titulos(doc)
    entradas, movidas = PC.ordenar_por_documento(doc, entradas_cuaderno())
    assert not movidas, movidas
    PC.rellenar_indice(doc, entradas, paginas)
    H.finalizar(doc, RUTA['cuaderno'])
    return {'entradas': entradas, 'practicas': [C.PRACTICA_TITULO for _, C, _ in practicas()]}


def _completar_grupos(entradas, pags):
    """Los títulos de unidad del cuaderno no son líneas del documento: toman la página de su primera práctica."""
    out = list(pags)
    for i in range(len(out) - 1, -1, -1):
        if out[i] is None and entradas[i][0] == 1 and i + 1 < len(out):
            out[i] = out[i + 1]
    return out


# ---------------------------------------------------------------- ciclo
def con_indice(armar, clave, grupos=False, vueltas=7):
    pags = None
    for _ in range(vueltas):
        res = armar(pags)
        K.a_pdf(RUTA[clave], COL)
        nuevas, total = PC.paginas_en_orden(PDF[clave], res['entradas'])
        if grupos:
            nuevas = _completar_grupos(res['entradas'], nuevas)
        faltan = [t for (_, t), p in zip(res['entradas'], nuevas) if p is None]
        assert not faltan, '%s: títulos del índice no encontrados en el PDF: %s' % (clave, faltan[:5])
        if nuevas == pags:
            return res, pags, total
        pags = nuevas
    raise AssertionError('%s: la paginación del índice no se estabilizó' % clave)


def construir_guia(res_libro, pag_libro, figs):
    instrumentos, pags = [], None
    for _ in range(6):
        res, pags, total = con_indice(lambda p: guia(res_libro, pag_libro, figs, instrumentos, p if p else pags), 'guia')
        nuevos = paginas_de_instrumentos(PDF['guia'], res['instrumentos'])
        if nuevos == instrumentos:
            return res, pags, total
        instrumentos = nuevos
    raise AssertionError('la tabla de instrumentos de la guía no se estabilizó')


if __name__ == '__main__':
    import pymupdf
    figs = figuras()
    for vuelta in range(8):
        res_l, pag_l, tot_l = con_indice(lambda p: libro(figs, p), 'libro')
        res_g, pag_g, tot_g = construir_guia(res_l, pag_l, figs)
        res_c, pag_c, tot_c = con_indice(cuaderno, 'cuaderno', grupos=True)
        nuevas = set()
        for k in RUTA:
            inc = O.incompletas(RUTA[k], PDF[k])
            if inc:
                nuevas.add(inc[0])
        print('vuelta %d: libro %d págs., guía %d, cuaderno %d; tablas incompletas: %s' % (vuelta + 1, tot_l, tot_g, tot_c, sorted(nuevas)))
        if not nuevas - O.HOJA_NUEVA:
            assert not nuevas, 'tablas que siguen perdiendo filas: %s' % nuevas
            break
        O.HOJA_NUEVA.update(nuevas)
    else:
        raise AssertionError('no se pudo evitar la pérdida de filas: %s' % O.HOJA_NUEVA)
    print('Libro del estudiante: %d págs. · guía docente: %d págs. · cuaderno de prácticas: %d págs.' % (tot_l, tot_g, tot_c))
    print('tablas que empiezan en hoja nueva para no perder filas:', sorted(O.HOJA_NUEVA))
    print('columnas ensanchadas para no partir palabras:', len(dict.fromkeys(O.AJUSTES)))
    json.dump({'perfil': O.PERFIL, 'ancho_util': O.ANCHO, 'version': PC.VERSION,
               'tablas_en_hoja_nueva': sorted(O.HOJA_NUEVA),
               'columnas_ensanchadas': [{'tabla': a, 'columna': b, 'antes_cm': c, 'despues_cm': d} for a, b, c, d in dict.fromkeys(O.AJUSTES)],
               'paginas': {'libro': tot_l, 'guia': tot_g, 'cuaderno': tot_c},
               'indice_libro': [[t, p] for (_, t), p in zip(res_l['entradas'], pag_l)],
               'indice_guia': [[t, p] for (_, t), p in zip(res_g['entradas'], pag_g)],
               'indice_cuaderno': [[t, p] for (_, t), p in zip(res_c['entradas'], pag_c)],
               'instrumentos_guia': paginas_de_instrumentos(PDF['guia'], res_g['instrumentos']),
               'reemplazos': res_l['reemplazos'], 'indice_reordenado': res_l['indice_reordenado'], 'claves': res_l['claves'], 'practicas': res_c['practicas'],
               'figuras': {n: {k: os.path.relpath(v, COL) for k, v in f.items()} for n, f in figs.items()}},
              open(os.path.join(COL, 'resultado_construccion.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
