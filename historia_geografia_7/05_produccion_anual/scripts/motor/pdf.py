"""Render con LibreOffice, lectura de títulos en PDF y copia liviana para revisión.

Tomado de `04_muestra3/scripts/construir_muestra3.py` (muestra aprobada como modelo).
"""
import os
import re
import subprocess

import pymupdf


def render(docx_path):
    out = os.path.dirname(docx_path)
    env = dict(os.environ, HOME='/tmp/lohome')
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', out, docx_path], check=True, env=env,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=900)
    return docx_path[:-5] + '.pdf'


def titulos_pdf(pdf, patron, desde=0):
    """Página de cada título que cumple el patrón, después del índice."""
    d = pymupdf.open(pdf)
    res = {}
    for n in range(desde, d.page_count):
        for linea in d[n].get_text().split('\n'):
            l = linea.strip()
            if re.match(patron, l) and l not in res:
                res[l] = n + 1
    return res


def pagina_indice(pdf):
    d = pymupdf.open(pdf)
    return next(n for n in range(d.page_count) if 'Índice' in d[n].get_text().split('\n')[0:3])


def liviano(pdf, salida, lado_max=1100, calidad=72):
    """Copia del PDF para revisión visual: cada imagen se reemplaza en el mismo
    objeto por un JPEG de lado mayor 1100 píxeles; el texto no cambia."""
    import io
    from PIL import Image
    d = pymupdf.open(pdf)
    for x in range(1, d.xref_length()):
        if d.xref_get_key(x, 'Subtype')[1] != '/Image' or d.xref_get_key(x, 'ImageMask')[1] == 'true':
            continue
        if any(d.xref_get_key(y, 'SMask')[1] == f'{x} 0 R' for y in ()):
            continue
        try:
            pix = pymupdf.Pixmap(d, x)
        except Exception:
            continue
        if pix.n - pix.alpha < 3:      # máscaras y grises: se dejan
            continue
        if pix.alpha or pix.n > 3:
            pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
        img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
        img.thumbnail((lado_max, lado_max))
        buf = io.BytesIO(); img.save(buf, 'JPEG', quality=calidad, optimize=True)
        if buf.tell() >= len(d.xref_stream_raw(x) or b''):
            continue
        d.update_stream(x, buf.getvalue(), compress=False)
        for k, v in (('Filter', '/DCTDecode'), ('Width', str(img.width)), ('Height', str(img.height)),
                     ('ColorSpace', '/DeviceRGB'), ('BitsPerComponent', '8'), ('DecodeParms', 'null'), ('SMask', 'null'),
                     ('Length', str(buf.tell()))):
            d.xref_set_key(x, k, v)
    d.save(salida, garbage=4, deflate=True)
    return os.path.getsize(salida)
