# -*- coding: utf-8 -*-
"""Figuras R2 de Informática 3.º BTC a partir de las 20 propuestas (PNG 1536 × 1024).

- Figuras 1-16 y 19: propuesta incorporada sin cambios (contenido cotejado con clase, pie, tabla y solucionario).
- Figura 17: propuesta con el logotipo de una red social comercial reemplazado por un ícono genérico de celular.
- Figura 18: propuesta con el logotipo de una aplicación de mensajería reemplazado por un globo genérico y el
  botón rotulado «Pedí por mensaje».
- Figura 20: reconstrucción vectorial (SVG + PNG a 300 ppi). La propuesta traía erratas de render («San Ḃlas»,
  «maestro ercapas») y logotipos comerciales; se recuperan los datos concretos del caso que tenía la figura R1.
Uso: python3 figuras_3btc.py <carpeta_propuestas> <carpeta_salida>
"""
import os, shutil, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
from PIL import Image, ImageDraw, ImageFont

AZUL, AZUL_CL, OCRE, OCRE_CL, TINTA, GRIS = '#0B4F7C', '#E3F0FA', '#B8730A', '#FDF1DC', '#0F2236', '#5B6B78'
NEGRITA = '/root/.fonts/Carlito-Bold.ttf'
for f in font_manager.findSystemFonts():
    if 'Carlito' in f:
        font_manager.fontManager.addfont(f)
plt.rcParams.update({'font.family': 'Carlito', 'svg.fonttype': 'none'})


def figura_17(origen, salida):
    im = Image.open(origen).convert('RGB'); d = ImageDraw.Draw(im)
    cx, cy = 100, 567                                   # círculo del ícono de la fila «Redes sociales»
    fondo = im.getpixel((cx, cy - 27)); tinta = (15, 34, 54)
    d.ellipse((cx - 29, cy - 29, cx + 29, cy + 29), fill=fondo)
    d.rounded_rectangle((cx - 13, cy - 22, cx + 13, cy + 22), radius=5, outline=tinta, width=4)   # celular genérico
    d.line((cx - 5, cy - 16, cx + 5, cy - 16), fill=tinta, width=3)
    d.ellipse((cx - 3, cy + 13, cx + 3, cy + 19), fill=tinta)
    im.save(salida)


def figura_18(origen, salida):
    im = Image.open(origen).convert('RGB'); d = ImageDraw.Draw(im)
    x0, y0, x1, y1 = 556, 684, 1012, 761               # interior del botón «Pedí por …»
    color = im.getpixel((x0 + 6, y0 + 8))
    d.rectangle((x0, y0, x1, y1), fill=color)
    blanco = (255, 255, 255)
    cx, cy = 610, 722                                  # globo de diálogo genérico
    d.rounded_rectangle((cx - 24, cy - 19, cx + 24, cy + 15), radius=10, outline=blanco, width=4)
    d.polygon([(cx - 12, cy + 13), (cx - 18, cy + 27), (cx - 2, cy + 14)], fill=blanco)
    for dx in (-11, 0, 11):
        d.ellipse((cx + dx - 3, cy - 5, cx + dx + 3, cy + 1), fill=blanco)
    f = ImageFont.truetype(NEGRITA, 36)
    d.text((662, cy), 'Pedí por mensaje', font=f, fill=blanco, anchor='lm')
    d.line((978, cy - 10, 988, cy, 978, cy + 10), fill=blanco, width=4, joint='curve')
    im.save(salida)


def figura_20(salida):
    fig = plt.figure(figsize=(15.5 / 2.54, 10.33 / 2.54))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 155); ax.set_ylim(0, 103.3); ax.axis('off')
    ax.text(77.5, 96, 'Ciclo de una promoción digital', ha='center', va='center', fontsize=19, fontweight='bold',
            color=TINTA)
    ax.text(77.5, 88.5, 'Caso San Blas · promoción «20 % en fiambres»', ha='center', va='center', fontsize=12.5,
            fontweight='bold', color=AZUL)
    pasos = [('Definir', 'Oferta, condiciones\ny vigencia:\n20 % en fiambres,\ndel 5 al 12'),
             ('Diseñar', 'Pieza desde\nel archivo\nmaestro en capas'),
             ('Publicar', 'Sección\nPromociones\ndel sitio\ny portada'),
             ('Difundir', 'Publicación\n1080 × 1080\nen redes y estado\nde mensajería'),
             ('Medir', 'Visitas, consultas\ny ventas del rubro\ncontra el mes\nanterior')]
    w, h, y, gap = 28.6, 46, 30, 2.4
    x0 = (155 - (5 * w + 4 * gap)) / 2
    for i, (t, s) in enumerate(pasos):
        x = x0 + i * (w + gap); col = AZUL if i % 2 == 0 else OCRE; rel = AZUL_CL if i % 2 == 0 else OCRE_CL
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=1.6', fc=rel, ec=col, lw=1.4))
        ax.add_patch(FancyBboxPatch((x, y + h - 11), w, 11, boxstyle='round,pad=0,rounding_size=1.6', fc=col,
                                    ec=col, lw=1.4))
        ax.add_patch(plt.Rectangle((x, y + h - 11), w, 2.5, fc=col, ec=col))
        ax.add_patch(Circle((x + 5.3, y + h - 5.5), 3.6, fc='white', ec='white'))
        ax.text(x + 5.3, y + h - 5.6, str(i + 1), ha='center', va='center', fontsize=12, fontweight='bold', color=col)
        ax.text(x + 17.6, y + h - 5.6, t, ha='center', va='center', fontsize=11, fontweight='bold', color='white')
        ax.text(x + w / 2, y + (h - 11) / 2, s, ha='center', va='center', fontsize=8.6, color=TINTA,
                linespacing=1.3)
        if i < 4:
            ax.add_patch(FancyArrowPatch((x + w + 0.3, y + h / 2), (x + w + gap - 0.3, y + h / 2),
                                         arrowstyle='-|>', mutation_scale=11, color=OCRE, lw=1.6))
    # retroalimentación: del paso 5 al paso 1
    xa, xb = x0 + w / 2, x0 + 4 * (w + gap) + w / 2
    ax.plot([xb, xb, xa, xa], [y, 21, 21, y - 0.2], color=OCRE, lw=1.8, ls=(0, (4, 2)))
    ax.add_patch(FancyArrowPatch((xa, 23), (xa, y - 0.2), arrowstyle='-|>', mutation_scale=12, color=OCRE, lw=1.8))
    ax.add_patch(FancyBboxPatch((50, 17.2), 55, 7.6, boxstyle='round,pad=0,rounding_size=1.6', fc=OCRE, ec=OCRE))
    ax.text(77.5, 21, 'Ajustar la próxima promoción', ha='center', va='center', fontsize=11, fontweight='bold',
            color='white')
    ax.add_patch(FancyBboxPatch((10, 4.5), 135, 8, boxstyle='round,pad=0,rounding_size=1.6', fc=AZUL_CL, ec=AZUL,
                                lw=1))
    ax.text(77.5, 8.5, 'Lo que se mide orienta la próxima promoción. Esquema didáctico: no representa una campaña real.',
            ha='center', va='center', fontsize=8.8, color=TINTA)
    fig.savefig(os.path.join(salida, 'R2_Figura_20.svg'))
    fig.savefig(os.path.join(salida, 'R2_Figura_20.png'), dpi=300)
    plt.close(fig)


if __name__ == '__main__':
    prop, sal = sys.argv[1], sys.argv[2]
    os.makedirs(sal, exist_ok=True)
    for n in list(range(1, 17)) + [19]:
        shutil.copyfile(os.path.join(prop, 'Figura_%02d.png' % n), os.path.join(sal, 'R2_Figura_%02d.png' % n))
    figura_17(os.path.join(prop, 'Figura_17.png'), os.path.join(sal, 'R2_Figura_17.png'))
    figura_18(os.path.join(prop, 'Figura_18.png'), os.path.join(sal, 'R2_Figura_18.png'))
    figura_20(sal)
    print('20 figuras R2 en', sal)
