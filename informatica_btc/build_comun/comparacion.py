# -*- coding: utf-8 -*-
"""Arma un PDF de aprobación: cada página muestra «antes» y «después» lado a lado, el cambio y su motivo, y casillas
para que el responsable marque Aprobado / Con cambios / Rechazado y escriba observaciones.
Uso desde Python: armar(paginas, salida, titulo), con paginas = [dict(codigo, titulo, antes, despues, rot_antes,
rot_despues, cambio, motivo)]; antes y despues son rutas PNG o (ruta_pdf, n.º de página)."""
import textwrap
import pymupdf
from PIL import Image, ImageDraw, ImageFont

W, H = 3508, 2480                                  # A4 apaisado a 300 ppi
F = '/usr/local/share/fonts/carlito/Carlito-Regular.ttf'; FB = '/root/.fonts/Carlito-Bold.ttf'
TINTA, AZUL, OCRE, GRIS = (15, 34, 54), (11, 79, 124), (184, 115, 10), (110, 120, 130)


def imagen(src):
    if isinstance(src, tuple):                 # (pdf, página[, recorte]) — recorte: rectángulo en puntos, o
        doc = pymupdf.open(src[0]); pg = doc[src[1] - 1]   # (texto inicial, texto final) para recortar entre ambos
        clip = None
        if len(src) > 2:
            if isinstance(src[2][0], str):
                a = pg.search_for(src[2][0])[0]; b = pg.search_for(src[2][1])[-1]
                clip = pymupdf.Rect(pg.rect.x0 + 20, a.y0 - 8, pg.rect.x1 - 20, b.y1 + 8)
            else:
                clip = pymupdf.Rect(*src[2])
        pix = pg.get_pixmap(dpi=300, clip=clip)
        return Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    return Image.open(src).convert('RGB')


def encajar(im, w, h):
    r = min(w / im.width, h / im.height)
    return im.resize((int(im.width * r), int(im.height * r)), Image.LANCZOS)


def texto(d, xy, t, tam, bold=False, color=TINTA, ancho=None):
    f = ImageFont.truetype(FB if bold else F, tam)
    lineas = textwrap.wrap(t, ancho) if ancho else [t]
    x, y = xy
    for l in lineas:
        d.text((x, y), l, font=f, fill=color); y += int(tam * 1.25)
    return y


def pagina(p, n, total, titulo_doc):
    im = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(im)
    texto(d, (120, 70), titulo_doc, 44, color=GRIS)
    texto(d, (W - 520, 70), 'Página %d de %d' % (n, total), 44, color=GRIS)
    texto(d, (120, 140), '%s · %s' % (p['codigo'], p['titulo']), 78, bold=True)
    top = 290
    if p.get('apilar'):                          # piezas anchas (filas del plan anual): una arriba de la otra
        cajas = [(120, top, W - 240, 660), (120, top + 760, W - 240, 660)]
    else:
        cajas = [(120, top, 1580, 1460), (120 + 1580 + 108, top, 1580, 1460)]
    for (x0, y0, cw, ch), (src, rot, col) in zip(cajas, ((p['antes'], p['rot_antes'], GRIS), (p['despues'], p['rot_despues'], AZUL))):
        d.rectangle((x0, y0, x0 + cw, y0 + 70), fill=col)
        texto(d, (x0 + 24, y0 + 10), rot, 48, bold=True, color='white')
        d.rectangle((x0, y0 + 70, x0 + cw, y0 + 70 + ch), outline=col, width=4)
        if src is None:
            texto(d, (x0 + 60, y0 + ch // 2), '(sin versión anterior)', 56, color=GRIS)
        else:
            sub = encajar(imagen(src), cw - 40, ch - 40)
            im.paste(sub, (x0 + (cw - sub.width) // 2, y0 + 70 + (ch - sub.height) // 2))
    caja_h = cajas[-1][1] + cajas[-1][3] - top
    y = top + 70 + caja_h + 40
    y = texto(d, (120, y), 'Cambio: ' + p['cambio'], 46, ancho=150)
    y = texto(d, (120, y + 8), 'Motivo: ' + p['motivo'], 46, color=(60, 70, 80), ancho=150)
    y = max(y + 30, H - 250)
    for k, op in enumerate(('Aprobado', 'Aprobado con cambios', 'Rechazado')):
        x = 120 + k * 700
        d.rectangle((x, y, x + 56, y + 56), outline=TINTA, width=4)
        texto(d, (x + 80, y + 2), op, 48)
    texto(d, (2250, y + 2), 'Firma: ____________________', 48)
    texto(d, (120, y + 100), 'Observaciones: ' + '_' * 150, 48)
    return im


def armar(paginas, salida, titulo_doc):
    ims = [pagina(p, i + 1, len(paginas), titulo_doc) for i, p in enumerate(paginas)]
    ims[0].save(salida, save_all=True, append_images=ims[1:], resolution=300)
    return len(ims)
