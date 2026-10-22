# -*- coding: utf-8 -*-
"""Figuras R2 de Informática 2.º BTC.

- Figuras 1-3, 6, 7, 10-13: se usan las propuestas gráficas tal como llegaron (copia con nombre R2).
- Figura 4: propuesta con la errata del subtítulo corregida («absoliutas» → «absolutas»).
- Figuras 5, 8 y 9: reconstrucción vectorial (SVG + PNG a 300 ppi) con la línea gráfica de las propuestas:
  5 usa los datos reales del caso; 8 dibuja una Bézier cúbica con manijas tangentes exactas;
  9 conserva tamaño y posición relativa de los objetos entre «Antes» y «Después».
Uso: python3 figuras_2btc.py <carpeta_propuestas> <carpeta_salida>
"""
import os, shutil, sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Ellipse, PathPatch
from matplotlib.path import Path
from PIL import Image, ImageDraw, ImageFont
from shapely.geometry import Point
from shapely.ops import unary_union

AZUL, AZUL_CL, OCRE, OCRE_CL, TINTA, GRIS = '#0B4F7C', '#E3F0FA', '#B8730A', '#FDF1DC', '#0F2236', '#5B6B78'
ANCHO_CM, ALTO_CM = 15.5, 10.33          # 3:2, igual que las propuestas
FUENTE = 'Carlito'
for f in font_manager.findSystemFonts():
    if 'Carlito' in f:
        font_manager.fontManager.addfont(f)
plt.rcParams.update({'font.family': FUENTE, 'svg.fonttype': 'none'})


def lienzo():
    fig = plt.figure(figsize=(ANCHO_CM / 2.54, ALTO_CM / 2.54))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 155); ax.set_ylim(0, 103.3); ax.axis('off')
    return fig, ax


def caja(ax, x, y, w, h, color, relleno, titulo=None, alto_titulo=7):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=1.6', fc=relleno, ec=color, lw=1.4))
    if titulo:
        ax.add_patch(FancyBboxPatch((x, y + h - alto_titulo), w, alto_titulo, boxstyle='round,pad=0,rounding_size=1.6',
                                    fc=color, ec=color, lw=1.4))
        ax.add_patch(Rectangle((x, y + h - alto_titulo), w, 2, fc=color, ec=color))
        ax.text(x + w / 2, y + h - alto_titulo / 2, titulo, ha='center', va='center', color='white', fontsize=12.5,
                fontweight='bold')


def titulo(ax, t, sub=None):
    ax.text(77.5, 98.3, t, ha='center', va='center', fontsize=19, fontweight='bold', color=TINTA)
    if sub:
        ax.text(77.5, 91.3, sub, ha='center', va='center', fontsize=12.5, fontweight='bold', color=AZUL)


def guardar(fig, salida, nombre):
    fig.savefig(os.path.join(salida, nombre + '.svg'))
    fig.savefig(os.path.join(salida, nombre + '.png'), dpi=300)
    plt.close(fig)


# ------------------------------------------------------------------ Figura 5: cuatro tipos con datos del caso
def figura_5(salida):
    fig, ax = lienzo()
    titulo(ax, 'Elegí el gráfico según la pregunta', 'Datos del Estudio Contable Arandu · importes mensuales en millones de guaraníes')
    paneles = [(3, 47, AZUL, AZUL_CL, 'COLUMNAS · comparar'), (80, 47, OCRE, OCRE_CL, 'LÍNEAS · evolución'),
               (3, 6, OCRE, OCRE_CL, 'CIRCULAR · partes de un total'), (80, 6, AZUL, AZUL_CL, 'BARRAS · ranking')]
    for x, y, c, r, t in paneles:
        caja(ax, x, y, 72, 38, c, r, t)
    # columnas: honorarios por régimen
    sub = fig.add_axes([0.07, 0.505, 0.36, 0.25]); reg = ['RESIMPLE', 'SIMPLE', 'GENERAL']; val = [4.05, 4.50, 3.60]
    b = sub.bar(reg, val, color=['#7FB3D9', AZUL, '#A9CBE6'], width=0.6)
    for rect, v in zip(b, val):
        sub.text(rect.get_x() + rect.get_width() / 2, v + 0.12, ('%.2f' % v).replace('.', ','), ha='center', fontsize=9.5, color=TINTA)
    sub.set_ylim(0, 5.3); sub.set_yticks([0, 1, 2, 3, 4, 5]); sub.tick_params(labelsize=8.5)
    for s in ('top', 'right'): sub.spines[s].set_visible(False)
    sub.set_facecolor(AZUL_CL); sub.patch.set_alpha(0)
    # líneas: doce meses supuestos iguales
    sub = fig.add_axes([0.565, 0.505, 0.39, 0.25]); m = np.arange(1, 13)
    sub.plot(m, [12.15] * 12, color=OCRE, marker='o', ms=4, lw=2)
    sub.set_ylim(0, 14); sub.set_xticks(m); sub.set_xticklabels(['E', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'], fontsize=8.5)
    sub.tick_params(labelsize=8.5); sub.text(6.5, 5.2, '12,15 cada mes: proyección de doce\nmeses iguales, no datos reales', ha='center', fontsize=9, color=TINTA)
    for s in ('top', 'right'): sub.spines[s].set_visible(False)
    sub.patch.set_alpha(0)
    # circular
    sub = fig.add_axes([0.035, 0.075, 0.25, 0.29])
    sub.pie([4.05, 4.50, 3.60], colors=['#E0A64B', '#7A5A1E', '#F3D39A'], startangle=90, counterclock=False,
            wedgeprops=dict(edgecolor='white', linewidth=1.5))
    sub.set_aspect('equal')
    ax.text(45, 26.5, 'RESIMPLE 33,3 %\nSIMPLE 37,0 %\nGENERAL 29,6 %', fontsize=10, color=TINTA, va='center', linespacing=1.5)
    ax.text(45, 12.5, 'Suman 99,9 % por\nredondeo a un\ndecimal', fontsize=8.5, color=GRIS, va='center')
    # barras: egresos del mes ordenados
    sub = fig.add_axes([0.64, 0.115, 0.31, 0.245])
    eg = [('Insumos', 0.380), ('Publicidad', 0.560), ('IPS patronal', 0.561), ('Servicios', 0.649), ('Alquiler', 2.100), ('Sueldo', 3.400)]
    sub.barh([e[0] for e in eg], [e[1] for e in eg], color=AZUL, height=0.6)
    for i, (_, v) in enumerate(eg):
        sub.text(v + 0.05, i, ('%.2f' % v).replace('.', ','), va='center', fontsize=8.5, color=TINTA)
    sub.set_xlim(0, 4.1); sub.tick_params(labelsize=8.5)
    for s in ('top', 'right'): sub.spines[s].set_visible(False)
    sub.patch.set_alpha(0)
    guardar(fig, salida, 'R2_Figura_05')


# ------------------------------------------------------------------ Figura 8: nodos y manijas (Bézier exacta)
def bezier(p0, p1, p2, p3, n=200):
    t = np.linspace(0, 1, n)[:, None]
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3


def figura_8(salida):
    fig, ax = lienzo()
    titulo(ax, 'Nodos y manijas: cómo se edita una curva', 'El trazado vectorial es una curva Bézier definida por cuatro puntos')
    p0, p1, p2, p3 = map(np.array, ([35, 46], [50, 80], [105, 80], [120, 46]))
    q2 = np.array([130, 74])                       # manija derecha desplazada (variante)
    c2 = bezier(p0, p1, q2, p3); ax.plot(c2[:, 0], c2[:, 1], color=OCRE, lw=1.6, ls=(0, (4, 3)), alpha=0.9)
    ax.plot([p3[0], q2[0]], [p3[1], q2[1]], color=OCRE, lw=1, ls=':', alpha=0.9)
    ax.add_patch(Circle(q2, 1.3, fc='white', ec=OCRE, lw=1.2))
    c = bezier(p0, p1, p2, p3); ax.plot(c[:, 0], c[:, 1], color=AZUL, lw=3)
    for a, b in ((p0, p1), (p3, p2)):
        ax.plot([a[0], b[0]], [a[1], b[1]], color=GRIS, lw=1.2, ls=(0, (3, 2)))
    for h in (p1, p2):
        ax.add_patch(Circle(h, 1.6, fc=OCRE, ec=OCRE))
    for n in (p0, p3):
        ax.add_patch(Rectangle(n - 1.8, 3.6, 3.6, fc=AZUL, ec=AZUL))
    est = dict(fontsize=11, fontweight='bold', va='center')
    ax.text(p0[0] - 3, p0[1] - 5, 'Nodo\n(punto de anclaje)', ha='center', color=AZUL, fontsize=10.5, fontweight='bold', va='top')
    ax.text(p3[0] + 3, p3[1] - 5, 'Nodo', ha='center', color=AZUL, va='top', fontsize=10.5, fontweight='bold')
    ax.text(p1[0] - 3, p1[1] + 3.5, 'Manija de control', ha='center', color=OCRE, **est)
    ax.text(p2[0] - 10, p2[1] + 3.5, 'Manija de control', ha='center', color=OCRE, **est)
    ax.text(77.5, 61, 'Trazado', ha='center', color=AZUL, **est)
    ax.text(77.5, 54, 'La manija marca la dirección\nde la curva al salir del nodo', ha='center', fontsize=9.5, color=GRIS, va='center')
    caja(ax, 4, 3, 72, 22, AZUL, AZUL_CL, 'Nodo')
    ax.add_patch(Rectangle((9, 7.5), 5, 5, fc=AZUL))
    ax.text(18, 10, 'Moverlo cambia el punto por donde\npasa el trazado (el anclaje).', fontsize=10.5, color=TINTA, va='center')
    caja(ax, 79, 3, 72, 22, OCRE, OCRE_CL, 'Manija de control')
    ax.add_patch(Circle((86.5, 10), 2.6, fc=OCRE))
    ax.text(92, 10, 'Moverla cambia dirección y curvatura;\nel nodo no se mueve. En punteado:\nla curva con la manija desplazada.', fontsize=9.8, color=TINTA, va='center')
    guardar(fig, salida, 'R2_Figura_08')


# ------------------------------------------------------------------ Figura 9: alinear, agrupar, soldar
def figura_9(salida):
    fig, ax = lienzo()
    titulo(ax, 'Alinear, agrupar y soldar', 'Tres operaciones distintas sobre los mismos objetos')
    cols = [(3, AZUL, AZUL_CL, 'ALINEAR'), (54, OCRE, OCRE_CL, 'AGRUPAR'), (105, AZUL, AZUL_CL, 'SOLDAR')]
    for x, c, r, t in cols:
        caja(ax, x, 14, 47, 72, c, r, t)
        ax.text(x + 23.5, 76, 'Antes', ha='center', fontsize=10.5, fontweight='bold', color=TINTA)
        ax.text(x + 23.5, 45, 'Después', ha='center', fontsize=10.5, fontweight='bold', color=TINTA)
        ax.annotate('', xy=(x + 23.5, 47.5), xytext=(x + 23.5, 52.5), arrowprops=dict(arrowstyle='-|>', color=OCRE, lw=2))
    # alinear: mismos rectángulos, mismo ancho y alto; cambia solo la posición vertical
    rects = [(9, 8, 6), (21, 8, 10), (33, 8, 14)]
    for (x, w, h), y0 in zip(rects, (60, 56, 54)):
        ax.add_patch(Rectangle((x, y0), w, h, fc='white', ec=TINTA, lw=1.2))
    for x, w, h in rects:
        ax.add_patch(Rectangle((x, 24), w, h, fc='white', ec=TINTA, lw=1.2))
    ax.plot([7, 44], [24, 24], color=OCRE, lw=2)
    ax.text(26.5, 18.5, 'Mismo borde inferior; tamaños\ny formas no cambian', ha='center', fontsize=9.5, color=TINTA, va='center')
    # agrupar: mismas posiciones; aparece el marco del grupo
    for dy in (56, 25):
        ax.add_patch(Circle((67, dy + 8), 4.5, fc='#E0A64B', ec=TINTA, lw=1.2))
        ax.add_patch(Rectangle((75, dy + 1), 14, 7, fc='#9CC7EA', ec=TINTA, lw=1.2))
    ax.add_patch(Rectangle((60.5, 23), 31, 17, fill=False, ec=OCRE, lw=1.6, ls=(0, (4, 2))))
    ax.text(77.5, 18.5, 'Se mueven juntos; se pueden\ndesagrupar (reversible)', ha='center', fontsize=9.5, color=TINTA, va='center')
    # soldar: misma silueta, una sola geometría
    a, b = Point(122, 64).buffer(6.5, 64), Point(132, 64).buffer(6.5, 64)
    ax.add_patch(Circle((122, 64), 6.5, fc='#E0A64B', ec=TINTA, lw=1.2, alpha=0.85))
    ax.add_patch(Circle((132, 64), 6.5, fc='#9CC7EA', ec=TINTA, lw=1.2, alpha=0.85))
    u = unary_union([a, b]); xs, ys = u.exterior.xy
    ax.fill(np.array(xs), np.array(ys) - 33, fc=AZUL, ec=TINTA, lw=1.2)
    ax.text(128.5, 18.5, 'Una sola forma: los originales\nya no son objetos separados', ha='center', fontsize=9.5, color=TINTA, va='center')
    ax.add_patch(FancyBboxPatch((3, 3), 149, 8, boxstyle='round,pad=0,rounding_size=1.6', fc=OCRE_CL, ec=OCRE, lw=1.2))
    ax.text(77.5, 7, 'Antes de soldar, duplicá los objetos si querés conservar una versión editable.', ha='center',
            va='center', fontsize=11, fontweight='bold', color='#7A4A05')
    guardar(fig, salida, 'R2_Figura_09')


# ------------------------------------------------------------------ Figura 4: errata del subtítulo
def figura_4(origen, salida):
    im = Image.open(origen).convert('RGB'); dr = ImageDraw.Draw(im)
    # franja del subtítulo «Referencias relativas y absoliutas» (y ≈ 100-150 px en la imagen de 1536 × 1024)
    # Se mide la franja real del subtítulo (tinta oscura entre el título y las cajas) y se reescribe en el mismo lugar.
    a = np.asarray(im.convert('L')).astype(int)
    filas = [y for y in range(95, 170) if (a[y, 250:1300] < 90).sum() > 5]
    cols = [x for x in range(250, 1300) if (a[filas[0]:filas[-1] + 1, x] < 90).sum() > 0]
    y0, y1, x0, x1 = filas[0], filas[-1], cols[0], cols[-1]
    fondo = im.getpixel((x0 - 30, (y0 + y1) // 2))
    dr.rectangle((x0 - 6, y0 - 4, x1 + 6, y1 + 4), fill=fondo)
    fuente = [f for f in font_manager.findSystemFonts() if 'Carlito-Bold.' in f][0]
    t = 'Referencias relativas y absolutas'
    tam = 60
    while True:
        f = ImageFont.truetype(fuente, tam)
        bb = dr.textbbox((0, 0), t, font=f)
        if bb[2] - bb[0] <= (x1 - x0) * 0.97 and bb[3] - bb[1] <= (y1 - y0) + 2:
            break
        tam -= 1
    w = bb[2] - bb[0]
    dr.text(((x0 + x1) / 2 - w / 2 - bb[0], y0 - bb[1]), t, font=f, fill=(15, 34, 54))
    print('Figura 4: subtítulo reescrito en', (x0, y0, x1, y1), 'cuerpo', tam)
    im.save(os.path.join(salida, 'R2_Figura_04.png'))


if __name__ == '__main__':
    prop, sal = sys.argv[1], sys.argv[2]
    os.makedirs(sal, exist_ok=True)
    for n in (1, 2, 3, 6, 7, 10, 11, 12, 13):
        shutil.copyfile(os.path.join(prop, 'Figura_%02d.png' % n), os.path.join(sal, 'R2_Figura_%02d.png' % n))
    figura_4(os.path.join(prop, 'Figura_04.png'), sal)
    figura_5(sal); figura_8(sal); figura_9(sal)
    print('figuras listas en', sal)
