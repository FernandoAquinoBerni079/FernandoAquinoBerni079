# -*- coding: utf-8 -*-
"""Cubiertas de los cinco productos de la edición comercial v1.0, con una identidad común (verde BTI de la colección y un
color de acento por producto), dibujadas en vectores con PyMuPDF y la fuente Carlito (SIL Open Font License 1.1).

Para cada producto escribe en edicion_v1_0/salida/cubiertas/:
- <producto>_TAPA.pdf y <producto>_CONTRATAPA.pdf: una página oficio cada una (para la versión digital);
- <producto>_CUBIERTA_IMPRESION.pdf: tapa, lomo y contratapa en un pliego, con 3 mm de sangrado y lomo calculado para
  papel de 75 g/m² (0,1 mm por hoja; la imprenta lo ajusta a su papel);
- <producto>_TAPA.png: vista previa para la presentación comercial.
Los datos de titular e ISBN salen de datos_edicion.json; si faltan, la cubierta deja el recuadro del código de barras vacío
y el texto «[a completar por el titular]».
Uso: python3 -B analisis_diseno_3_bti/edicion_v1_0/build/cubiertas.py
"""
import json, os, sys
sys.dont_write_bytecode = True
import pymupdf

AQUI = os.path.dirname(os.path.abspath(__file__)); ED = os.path.dirname(AQUI)
SAL = os.path.join(ED, 'salida', 'cubiertas'); os.makedirs(SAL, exist_ok=True)
DATOS = json.load(open(os.path.join(ED, 'datos_edicion.json'), encoding='utf8'))
FALTA = DATOS['texto_si_falta']
FUENTES = {'r': '/usr/local/share/fonts/carlito/Carlito-Regular.ttf', 'b': '/usr/local/share/fonts/carlito/Carlito-Bold.ttf',
           'i': '/usr/local/share/fonts/carlito/Carlito-Italic.ttf'}
W, H = 21.59 / 2.54 * 72, 33.02 / 2.54 * 72          # oficio en puntos
MM = 72 / 25.4
SANGRADO = 3 * MM
hexrgb = lambda h: tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
VERDE, VERDE_M, VERDE_C, CLARO = hexrgb('1B5E20'), hexrgb('2E7D32'), hexrgb('A5D6A7'), hexrgb('E8F5E9')
BLANCO, GRIS, TEXTO = (1, 1, 1), hexrgb('607D8B'), hexrgb('263238')

UNIDADES = [('I', 'Comprender', 'el problema'), ('II', 'Especificar', 'requisitos'), ('III', 'Diseñar', 'la solución'),
            ('IV', 'Construir', 'el prototipo'), ('V', 'Verificar', 'y mejorar'), ('VI', 'Entregar', 'y comunicar')]

PRODUCTOS = {
    'libro': dict(
        nombre='Libro del estudiante', archivo='ADS_3BTI_LIBRO_DEL_ESTUDIANTE_v1_0', acento='2E7D32',
        cifras='18 capítulos · 6 unidades · 36 encuentros · 16 prácticas · 6 hitos',
        descripcion='Un año completo para aprender a analizar y diseñar sistemas de información trabajando en un proyecto real: '
                    'el sistema de préstamos de la biblioteca de un colegio. El curso pasa del problema y los requisitos a '
                    'los modelos, el prototipo web, las pruebas y la entrega documentada.',
        incluye=['Teoría breve y clara, con tablas, figuras y ejemplos resueltos paso a paso.',
                 'Actividades en cuatro bloques: Ejercitá, Resolvé, Pensá y decidí, y Desafío.',
                 '16 prácticas en tres niveles, con datos distintos de los ejemplos.',
                 'Revisiones de unidad con seis hitos integradores y evaluaciones de capítulo.',
                 'Recuadros «Para repasar» y «Si el calendario se acorta» en cada capítulo.'],
        beneficios=['Aprendizaje basado en proyectos, de punta a punta.',
                    'Requisitos verificables, modelos coherentes y decisiones justificadas.',
                    'Evidencia individual en cada hito: cada estudiante muestra lo que sabe hacer.']),
    'cuaderno': dict(
        nombre='Cuaderno de prácticas', archivo='ADS_3BTI_CUADERNO_DE_PRACTICAS_v1_0', acento='F9A825',
        cifras='16 prácticas · 3 niveles · renglones de 8 mm',
        descripcion='Las 16 prácticas del libro del estudiante, listas para resolver a mano. Cada práctica usa un caso propio, '
                    'la biblioteca de Mbokaja, para que el estudiante aplique lo aprendido sin copiar los ejemplos.',
        incluye=['Las consignas completas de los tres niveles de cada práctica.',
                 'Renglones de respuesta de 8 mm, tres por consigna.',
                 'Punto de control al final de cada práctica.',
                 'Índice por unidad para ubicar cada práctica.'],
        beneficios=['Se usa junto con el libro: allí están la teoría y los ejemplos.',
                    'Nivel 1 como piso común, Nivel 2 esperado y Nivel 3 de ampliación.',
                    'Facilita la corrección con las listas de cotejo de la guía docente.']),
    'guia': dict(
        nombre='Guía docente con solucionario', archivo='ADS_3BTI_GUIA_DOCENTE_SOLUCIONARIO_v1_0', acento='00695C',
        cifras='36 encuentros · claves de actividades, prácticas y evaluaciones · rúbricas H1 a H6',
        descripcion='La guía del docente para conducir el año sin improvisar: la secuencia de cada encuentro en horas cátedra, '
                    'las respuestas esperadas y los errores frecuentes de todas las actividades, las claves de las prácticas '
                    'y de las evaluaciones, y los instrumentos de los seis hitos.',
        incluye=['Secuencia de los 36 encuentros, tramo por tramo, en HC.',
                 'Claves y errores frecuentes de cada actividad, práctica y evaluación.',
                 'Rúbricas, planillas y evidencias 60/40 de los hitos H1 a H6.',
                 'Preparación del entorno técnico, prueba de campo y alternativas.',
                 'Calendario alternativo de 28 encuentros y procedencia de los recursos.'],
        beneficios=['Ahorra horas de preparación y corrección.',
                    'Evaluación por evidencias, con criterios explícitos y comparables.',
                    'Coordinación prevista con Algorítmica y Laboratorio de 3.º.']),
    'plan_anual': dict(
        nombre='Plan anual', archivo='ADS_3BTI_PLAN_ANUAL_v1_0', acento='37474F',
        cifras='5 HC semanales · 36 encuentros · 180 HC · editable',
        descripcion='Planificación anual completa para el Plan Optativo, alineada con el libro, la guía docente y el cuaderno, '
                    'con el encuadre del Diseño Curricular del MEC y la matriz de correspondencia de todo el año.',
        incluye=['Encuadre curricular: disposiciones del MEC citadas con su página.',
                 'Competencia, capacidades C1 a C10, contenidos e indicadores.',
                 'Desarrollo por unidad, capítulo y encuentro, con instrumentos.',
                 'Distribución de las 180 HC y matriz de correspondencia.',
                 'Campos editables para la institución.'],
        beneficios=['Listo para adoptar en el PCI de la institución.',
                    'Distingue lo oficial del MEC de la propuesta institucional.',
                    'DOCX editable y PDF.']),
    'planes': dict(
        nombre='Planes de clase', archivo='ADS_3BTI_PLANES_DE_CLASE_v1_0', acento='546E7A',
        cifras='36 planes · 5 HC por encuentro · editables',
        descripcion='Los 36 planes de clase del año, uno por encuentro, con inicio, desarrollo y cierre, explicaciones clave, '
                    'actividades, recursos, alternativas sin computadoras y evaluación con sus instrumentos.',
        incluye=['Capacidades e indicadores tomados de la ficha de cada capítulo.',
                 'Distribución de las 5 HC según la secuencia de la guía.',
                 'Páginas del libro, del cuaderno y de la guía en cada plan.',
                 'Errores frecuentes, preparación previa y alternativas.',
                 'Campos editables: institución, docente, sección y fecha.'],
        beneficios=['El docente adapta cada plan sin rehacerlo.',
                    'Coherencia total con el libro y la guía.',
                    'DOCX editable y PDF.']),
}
ORDEN = ['libro', 'cuaderno', 'guia', 'plan_anual', 'planes']


def fuentes(pg):
    for k, f in FUENTES.items():
        pg.insert_font(fontname='c' + k, fontfile=f)


def caja(pg, rect, texto, tam, estilo='r', color=TEXTO, alinea=0, rot=0):
    r = pymupdf.Rect(rect)
    for _ in range(8):   # la caja crece hacia abajo (o hacia la derecha si está girada) hasta que el texto entra
        sobra = pg.insert_textbox(r, texto, fontsize=tam, fontname='c' + estilo, color=color, align=alinea, rotate=rot)
        if sobra >= 0:
            return sobra
        if rot: r.x1 += tam * 0.5
        else: r.y1 += tam * 0.5
    raise AssertionError('texto que no entra: %r' % texto[:60])


def rect(pg, r, relleno, borde=None, ancho=0, radio=None):
    pg.draw_rect(pymupdf.Rect(r), color=borde, fill=relleno, width=ancho, radius=radio)


def esquema(pg, x0, y0, ancho, acento):
    """Las seis unidades como un recorrido: dos filas de tres tarjetas unidas por flechas."""
    cw, ch, gx, gy = (ancho - 2 * 22) / 3, 92, 22, 52
    pos = []
    for i, (rom, a, b) in enumerate(UNIDADES):
        fila, col = divmod(i, 3)
        if fila == 1: col = 2 - col          # recorrido en serpentina
        x = x0 + col * (cw + gx); y = y0 + fila * (ch + gy)
        pos.append((x, y))
        rect(pg, (x, y, x + cw, y + ch), CLARO if i % 2 else BLANCO, VERDE_M, 1.2, 0.18)
        rect(pg, (x, y, x + 30, y + ch), acento, None, 0, None)
        caja(pg, (x, y + 34, x + 30, y + 58), rom, 14, 'b', BLANCO, 1)
        caja(pg, (x + 38, y + 22, x + cw - 4, y + 44), a, 16, 'b', VERDE)
        caja(pg, (x + 38, y + 48, x + cw - 4, y + 68), b, 13, 'r', TEXTO)
    for i in range(5):
        (xa, ya), (xb, yb) = pos[i], pos[i + 1]
        if ya == yb:
            if xb > xa: p, q = (xa + cw + 3, ya + ch / 2), (xb - 3, yb + ch / 2)
            else: p, q = (xa - 3, ya + ch / 2), (xb + cw + 3, yb + ch / 2)
        else:
            p, q = (xa + cw / 2, ya + ch + 3), (xb + cw / 2, yb - 3)
        pg.draw_line(p, q, color=VERDE_M, width=2)
        dx, dy = q[0] - p[0], q[1] - p[1]; n = (dx * dx + dy * dy) ** 0.5; ux, uy = dx / n, dy / n
        a1 = (q[0] - 8 * ux + 4 * uy, q[1] - 8 * uy - 4 * ux); a2 = (q[0] - 8 * ux - 4 * uy, q[1] - 8 * uy + 4 * ux)
        pg.draw_polyline([a1, q, a2], color=VERDE_M, fill=VERDE_M, width=1, closePath=True)
    return y0 + 2 * ch + gy


def tapa(pg, ox, oy, clave):
    P = PRODUCTOS[clave]; ac = hexrgb(P['acento'])
    rect(pg, (ox, oy, ox + W, oy + 330), VERDE)
    pg.draw_polyline([(ox + W * 0.55, oy), (ox + W, oy), (ox + W, oy + 230)], color=None, fill=VERDE_M, closePath=True)
    pg.draw_polyline([(ox + W * 0.78, oy), (ox + W, oy), (ox + W, oy + 110)], color=None, fill=hexrgb('388E3C'), closePath=True)
    m = 46
    caja(pg, (ox + m, oy + 44, ox + W - m, oy + 64), 'COLECCIÓN ANUAL · 3.er CURSO · BACHILLERATO TÉCNICO EN INFORMÁTICA', 10.5, 'b', VERDE_C)
    caja(pg, (ox + m, oy + 78, ox + W - m, oy + 200), 'Análisis y Diseño\nde Sistemas', 42, 'b', BLANCO)
    caja(pg, (ox + m, oy + 210, ox + W - m, oy + 236), 'Del problema al prototipo web', 19, 'i', VERDE_C)
    rect(pg, (ox + m, oy + 262, ox + m + 300, oy + 300), ac, None, 0, 0.25)
    caja(pg, (ox + m + 14, oy + 271, ox + m + 296, oy + 296), P['nombre'].upper(), 15, 'b', BLANCO)
    caja(pg, (ox + m, oy + 352, ox + W - m, oy + 372), 'Seis unidades, un proyecto que crece todo el año', 13, 'b', GRIS, 1)
    fin = esquema(pg, ox + m, oy + 392, W - 2 * m, ac)
    caja(pg, (ox + m, fin + 34, ox + W - m, fin + 60), P['cifras'], 14.5, 'b', VERDE, 1)
    caja(pg, (ox + m, fin + 64, ox + W - m, fin + 84), 'Proyecto conductor: Sistema de Gestión de Biblioteca Escolar', 13, 'i', GRIS, 1)
    rect(pg, (ox + W / 2 - 60, fin + 100, ox + W / 2 + 60, fin + 103), ac)
    rect(pg, (ox, oy + H - 118, ox + W, oy + H), CLARO)
    rect(pg, (ox, oy + H - 118, ox + W, oy + H - 114), ac)
    caja(pg, (ox + m, oy + H - 100, ox + W - m, oy + H - 80), 'Plan Optativo · propuesta para el programa institucional', 12, 'b', VERDE)
    caja(pg, (ox + m, oy + H - 78, ox + W - m, oy + H - 60), 'Edición comercial v1.0 · %s · República del Paraguay' % DATOS['anio'], 11, 'r', TEXTO)
    caja(pg, (ox + m, oy + H - 56, ox + W - m, oy + H - 30),
         'No es un programa oficial ni está aprobado por el MEC. Las capacidades son propuestas para el programa '
         'institucional del Plan Optativo (Diseño Curricular del MEC, mayo de 2026, p. 29).', 8.5, 'r', GRIS)


def contratapa(pg, ox, oy, clave):
    P = PRODUCTOS[clave]; ac = hexrgb(P['acento']); m = 46
    rect(pg, (ox, oy, ox + W, oy + 18), VERDE); rect(pg, (ox, oy + 18, ox + W, oy + 22), ac)
    caja(pg, (ox + m, oy + 56, ox + W - m, oy + 82), 'Análisis y Diseño de Sistemas · %s' % P['nombre'], 19, 'b', VERDE)
    caja(pg, (ox + m, oy + 94, ox + W - m, oy + 200), P['descripcion'], 13.5, 'r', TEXTO)
    y = oy + 214
    for titulo, items in (('Qué incluye', P['incluye']), ('Para qué sirve', P['beneficios'])):
        caja(pg, (ox + m, y, ox + W - m, y + 22), titulo, 15, 'b', ac if clave != 'cuaderno' else VERDE)
        y += 26
        for it in items:
            rect(pg, (ox + m + 2, y + 6, ox + m + 9, y + 13), ac)
            caja(pg, (ox + m + 18, y, ox + W - m, y + 34), it, 12.5, 'r', TEXTO)
            y += 22 if len(it) < 80 else 38
        y += 14
    caja(pg, (ox + m, y + 4, ox + W - m, y + 26), 'La colección completa', 15, 'b', VERDE)
    y += 32
    for k in ORDEN:
        q = PRODUCTOS[k]; es = k == clave
        rect(pg, (ox + m, y, ox + W - m, y + 25), hexrgb(q['acento']) if es else CLARO, None, 0, 0.3)
        caja(pg, (ox + m + 10, y + 6, ox + W - m - 6, y + 24), '%s — %s' % (q['nombre'], q['cifras']), 10.5,
             'b' if es else 'r', BLANCO if es else TEXTO)
        y += 30
    assert y < oy + H - 160, 'la contratapa se superpone con el pie legal'
    # pie legal y espacio del código de barras
    titular = DATOS['titular'] or FALTA
    isbn = (DATOS['isbn'] or {}).get(clave) or None
    caja(pg, (ox + m, oy + H - 150, ox + W - 200, oy + H - 40),
         '© %s %s. Todos los derechos reservados. Prohibida su reproducción total o parcial sin autorización escrita del '
         'titular, salvo las excepciones de la Ley N.º 1328/98.\n'
         'Propuesta para el programa institucional del Plan Optativo; no constituye un programa oficial aprobado por el MEC. '
         'Los casos y nombres son ficticios.\nEdición comercial v1.0 · %s · República del Paraguay.' % (DATOS['anio'], titular, DATOS['anio']),
         8.5, 'r', GRIS)
    bx = (ox + W - 180, oy + H - 150, ox + W - m, oy + H - 62)
    rect(pg, bx, BLANCO, GRIS, 0.8)
    if isbn:
        caja(pg, (bx[0] + 6, bx[3] - 20, bx[2] - 6, bx[3] - 4), 'ISBN %s' % isbn, 9.5, 'b', TEXTO, 1)
    else:
        caja(pg, (bx[0] + 8, bx[1] + 22, bx[2] - 8, bx[3] - 6), 'Espacio para el ISBN y el código de barras (los asigna el '
             'editor ante la Agencia Paraguaya del ISBN)', 8.5, 'i', GRIS, 1)


def lomo(pg, x, oy, ancho, clave):
    P = PRODUCTOS[clave]
    rect(pg, (x, oy - SANGRADO, x + ancho, oy + H + SANGRADO), VERDE)
    if ancho >= 6 * MM:
        caja(pg, (x + 1, oy + 40, x + ancho - 1, oy + H - 40), 'Análisis y Diseño de Sistemas  ·  %s  ·  3.º BTI' % P['nombre'],
             min(12, ancho * 0.55), 'b', BLANCO, 1, rot=90)


def construir():
    salida = {}
    for clave in ORDEN:
        P = PRODUCTOS[clave]
        interior = pymupdf.open(os.path.join(ED, 'salida', P['archivo'] + '.pdf'))
        hojas = (len(interior) + 1) // 2
        ancho_lomo = hojas * 0.1 * MM
        for nombre, fn in (('TAPA', tapa), ('CONTRATAPA', contratapa)):
            d = pymupdf.open(); pg = d.new_page(width=W, height=H); fuentes(pg); fn(pg, 0, 0, clave)
            d.set_metadata({'title': 'Análisis y Diseño de Sistemas — %s — %s' % (P['nombre'], nombre.lower()),
                            'author': DATOS['titular'] or '', 'subject': 'Edición comercial v1.0'})
            d.save(os.path.join(SAL, '%s_%s.pdf' % (P['archivo'], nombre)), garbage=4, deflate=True)
            if nombre == 'TAPA':
                pg.get_pixmap(dpi=110).save(os.path.join(SAL, '%s_TAPA.png' % P['archivo']))
        # pliego de impresión: contratapa | lomo | tapa, con sangrado
        d = pymupdf.open()
        pg = d.new_page(width=2 * W + ancho_lomo + 2 * SANGRADO, height=H + 2 * SANGRADO); fuentes(pg)
        rect(pg, pg.rect, BLANCO)
        contratapa(pg, SANGRADO, SANGRADO, clave)
        lomo(pg, SANGRADO + W, SANGRADO, ancho_lomo, clave)
        tapa(pg, SANGRADO + W + ancho_lomo, SANGRADO, clave)
        for x in (SANGRADO + W, SANGRADO + W + ancho_lomo):       # marcas de plegado fuera del área útil
            pg.draw_line((x, 0), (x, SANGRADO * 0.8), color=(0, 0, 0), width=0.3)
            pg.draw_line((x, pg.rect.height - SANGRADO * 0.8), (x, pg.rect.height), color=(0, 0, 0), width=0.3)
        d.set_metadata({'title': 'Análisis y Diseño de Sistemas — %s — cubierta para imprenta' % P['nombre'],
                        'subject': 'Pliego con sangrado de 3 mm; lomo de %.1f mm para %d hojas de 75 g/m²' % (ancho_lomo / MM, hojas)})
        d.save(os.path.join(SAL, '%s_CUBIERTA_IMPRESION.pdf' % P['archivo']), garbage=4, deflate=True)
        salida[clave] = {'paginas_interior': len(interior), 'hojas': hojas, 'lomo_mm': round(ancho_lomo / MM, 1)}
    json.dump(salida, open(os.path.join(SAL, 'cubiertas.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    return salida


if __name__ == '__main__':
    print(construir())
