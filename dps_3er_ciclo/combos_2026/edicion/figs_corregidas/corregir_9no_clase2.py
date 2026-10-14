# -*- coding: utf-8 -*-
"""Corrige SOLO las dos erratas de la ilustración de estilos de comunicación de 9.º (Clase 2), sin regenerarla:
1. «AGRƸIVO» → «AGRESIVO»: la palabra se recompone con las letras A, G, R, I, V, O de la propia cabecera y con la E y
   la S de «ASERTIVO» (mismo dibujo tipográfico de la ilustración), al 95 % para conservar el aire con los íconos.
2. «¡Es asíy punto!» → «¡Es así y punto!»: se abre el espacio entre «así» y «y» desplazando los dos tramos 7 px.
El resto de los píxeles queda idéntico. Uso: python3 corregir_9no_clase2.py → 9no_clase2_estilos_CORREGIDA.png"""
import numpy as np
from PIL import Image
from scipy import ndimage as nd

SRC, DST = '9no_clase2_estilos_ORIGINAL.png', '9no_clase2_estilos_CORREGIDA.png'
im = np.array(Image.open(SRC).convert('RGB')).astype(float)
out = im.copy()

# ---------- 1. cabecera «AGRESIVO» ----------
Y0, Y1 = 302, 357                       # franja del texto (mayúsculas 309-349 más antialias)
ROJO = np.array([200., 69., 77.]); BLANCO = np.array([255., 250., 250.])

def alfa(x0, x1, canal, fondo):
    a = (im[Y0:Y1, x0:x1, canal] - fondo) / (255. - fondo)
    return np.clip(a, 0, 1)

letras = [alfa(1577, 1620, 1, 69), alfa(1621, 1658, 1, 69), alfa(1665, 1699, 1, 69),     # A G R (rojo: canal G)
          alfa(993, 1023, 0, 56), alfa(956, 988, 0, 56),                                   # E y S de ASERTIVO (A-S-E-R…; verde: canal R)
          alfa(1756, 1766, 1, 69), alfa(1769, 1811, 1, 69), alfa(1812, 1854, 1, 69)]       # I V O
huecos = [2, 8, 6, 5, 6, 5, 1]          # separación entre cajas, como en la tipografía original
ancho = sum(l.shape[1] for l in letras) + sum(huecos)
palabra = np.zeros((Y1 - Y0, ancho)); x = 0
for k, l in enumerate(letras):
    palabra[:, x:x + l.shape[1]] = np.maximum(palabra[:, x:x + l.shape[1]], l)
    x += l.shape[1] + (huecos[k] if k < len(huecos) else 0)
ESC = 0.95
pw, ph = round(ancho * ESC), round((Y1 - Y0) * ESC)
palabra = np.asarray(Image.fromarray((palabra * 255).astype(np.uint8)).resize((pw, ph), Image.LANCZOS)) / 255.
# borrar la palabra original entre los íconos (1556-1867) con el fondo interpolado entre filas limpias
XA, XB = 1556, 1868
arriba, abajo = im[Y0 - 3, XA:XB], im[Y1 + 2, XA:XB]
for i, y in enumerate(range(Y0, Y1)):
    t = (i + 1) / (Y1 - Y0 + 1)
    out[y, XA:XB] = arriba * (1 - t) + abajo * t
cx = (1577 + 1854) / 2                   # mismo centro que la palabra original
px0 = round(cx - pw / 2); py0 = round((Y0 + Y1) / 2 - ph / 2)
reg = out[py0:py0 + ph, px0:px0 + pw]
out[py0:py0 + ph, px0:px0 + pw] = reg * (1 - palabra[..., None]) + BLANCO * palabra[..., None]
assert px0 > 1556 and px0 + pw < 1868, (px0, pw)

# ---------- 2. globo «¡Es así y punto!» ----------
GY0, GY1, GX0, GX1 = 678, 736, 1520, 1890
reg = im[GY0:GY1, GX0:GX1]
TEXTO = np.array([160., 9., 10.]); ROSA_G = 210.
a = np.clip((ROSA_G - reg[:, :, 1]) / (ROSA_G - 9.), 0, 1)
# núcleos de cada glifo (umbral alto, para que la «í» y la «y» no queden unidas por el antialias)
lab, n = nd.label(a > 0.45)
lado = np.zeros(n + 1, bool)            # True = tramo derecho («y punto!»»)
for i in range(1, n + 1):
    ys, xs = np.where(lab == i)
    lado[i] = GX0 + xs.min() >= 1688
# cada píxel de borde se asigna al núcleo más cercano
_, (iy, ix) = nd.distance_transform_edt(lab == 0, return_indices=True)
cerca = lab[iy, ix]
der = np.where(lado[cerca], a, 0.); izq = np.where(~lado[cerca], a, 0.)
D = 7
nuevo = np.zeros_like(a)
nuevo[:, :-D] = np.maximum(nuevo[:, :-D], izq[:, D:])      # «¡Es así» 7 px a la izquierda
nuevo[:, D:] = np.maximum(nuevo[:, D:], der[:, :-D])       # «y punto!»» 7 px a la derecha
# fondo rosado sin texto: se interpola entre la fila de arriba y la de abajo del tramo
arriba, abajo = im[GY0 - 1, GX0:GX1], im[GY1, GX0:GX1]
for i, y in enumerate(range(GY0, GY1)):
    t = (i + 1) / (GY1 - GY0 + 1)
    out[y, GX0:GX1] = arriba * (1 - t) + abajo * t
out[GY0:GY1, GX0:GX1] = out[GY0:GY1, GX0:GX1] * (1 - nuevo[..., None]) + TEXTO * nuevo[..., None]

Image.fromarray(np.clip(out.round(), 0, 255).astype(np.uint8)).save(DST, optimize=True)
print('ok', DST)
