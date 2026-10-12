# -*- coding: utf-8 -*-
"""Diagramas nuevos (estándar gráfico: matplotlib, 200 dpi, DejaVu Sans, VERDE BTI + acentos)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse, Polygon, Rectangle, FancyArrowPatch
import os
OUT = '/home/claude/alg3/build/figs_new/'
os.makedirs(OUT, exist_ok=True)
DARK, MED, LIGHT, SOFT = '#1B5E20', '#2E7D32', '#E8F5E9', '#A5D6A7'
AMB, AMBL, ROJO, AZUL, GRIS = '#B8860B', '#FFF4D6', '#C62828', '#1565C0', '#616161'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})


def caja(ax, x, y, w, h, txt, fc=LIGHT, ec=MED, tc=DARK, fs=10, bold=True, lw=1.6, r=0.04):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.01,rounding_size=%s' % r, fc=fc, ec=ec, lw=lw))
    ax.text(x + w / 2, y + h / 2, txt, ha='center', va='center', color=tc, fontsize=fs, fontweight='bold' if bold else 'normal', wrap=True)


def flecha(ax, x1, y1, x2, y2, c=GRIS, lw=1.5, ls='-', ms=14):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=ms, color=c, lw=lw, linestyle=ls))


def fin(fig, nombre):
    fig.savefig(OUT + nombre, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)


def niveles():
    fig, ax = plt.subplots(figsize=(11.4, 6.2)); ax.set_xlim(0, 11.6); ax.set_ylim(0, 6.4); ax.axis('off')
    # bandas
    bandas = [(4.45, 'NIVEL DE VISTAS (externo)', 'Lo que ve cada usuario'),
              (2.45, 'NIVEL LÓGICO (conceptual)', 'Qué datos hay y cómo se relacionan'),
              (0.35, 'NIVEL FÍSICO (interno)', 'Cómo se guardan en el disco')]
    for y, t, s in bandas:
        ax.add_patch(FancyBboxPatch((0.1, y), 9.8, 1.75, boxstyle='round,pad=0.02,rounding_size=0.08', fc='#F7FBF7', ec=SOFT, lw=1.2))
        ax.text(0.3, y + 1.48, t, color=DARK, fontsize=10.5, fontweight='bold', va='center')
        ax.text(0.3, y + 1.15, s, color=GRIS, fontsize=9, va='center', style='italic')
    caja(ax, 3.4, 4.6, 2.7, 0.95, 'Vista del cajero\nproductos y precios', fc='white', fs=9.5)
    caja(ax, 6.7, 4.6, 2.9, 0.95, 'Vista del dueño\nrecaudación por categoría', fc='white', fs=9.5)
    for i, t in enumerate(['Productos', 'Clientes', 'Ventas', 'DetalleVenta']):
        caja(ax, 0.6 + i * 2.35, 2.6, 2.05, 0.75, t, fc=MED, ec=DARK, tc='white', fs=10)
    caja(ax, 1.2, 0.5, 3.8, 0.85, 'Archivo Copetin.accdb\n(registros en el disco)', fc=AMBL, ec=AMB, tc='#5A4200', fs=9.5)
    caja(ax, 5.6, 0.5, 3.6, 0.85, 'Índices\n(clave principal, fecha)', fc=AMBL, ec=AMB, tc='#5A4200', fs=9.5)
    for x in (4.75, 8.15):
        flecha(ax, x, 4.6, x - 0.4 if x < 5 else x - 1.0, 3.38, c=MED)
    flecha(ax, 3.2, 2.6, 3.0, 1.38, c=MED); flecha(ax, 7.0, 2.6, 7.3, 1.38, c=MED)
    ax.annotate('', xy=(10.35, 2.35), xytext=(10.35, 4.45), arrowprops=dict(arrowstyle='<->', color=AZUL, lw=1.3))
    ax.annotate('', xy=(10.35, 0.35), xytext=(10.35, 2.25), arrowprops=dict(arrowstyle='<->', color=AZUL, lw=1.3))
    ax.text(10.5, 3.4, 'independencia\nlógica', ha='left', va='center', fontsize=8.5, color=AZUL, style='italic')
    ax.text(10.5, 1.3, 'independencia\nfísica', ha='left', va='center', fontsize=8.5, color=AZUL, style='italic')
    fin(fig, 'fig_10_1_niveles.png')


def atributos():
    fig, ax = plt.subplots(figsize=(10, 5.6)); ax.set_xlim(0, 10); ax.set_ylim(0, 5.6); ax.axis('off')
    ax.add_patch(Rectangle((4.0, 2.4), 2.0, 0.8, fc=MED, ec=DARK, lw=1.8))
    ax.text(5.0, 2.8, 'CLIENTE', ha='center', va='center', color='white', fontweight='bold', fontsize=12)

    def elipse(x, y, t, ls='-', doble=False, sub=False, fc='white'):
        ax.add_patch(Ellipse((x, y), 2.05, 0.72, fc=fc, ec=MED, lw=1.5, ls=ls))
        if doble:
            ax.add_patch(Ellipse((x, y), 2.3, 0.92, fc='none', ec=MED, lw=1.5))
        tt = ax.text(x, y, t, ha='center', va='center', fontsize=10, color=DARK)
        if sub:
            ax.plot([x - 0.38, x + 0.38], [y - 0.16, y - 0.16], color=DARK, lw=1.2)
        return x, y
    pos = {'código': (1.5, 4.6), 'nombre completo': (5.0, 4.75), 'teléfonos': (8.5, 4.6),
           'fecha_nac': (1.5, 1.2), 'edad': (8.5, 1.2)}
    elipse(*pos['código'], 'código', sub=True)
    elipse(*pos['nombre completo'], 'nombre completo')
    elipse(*pos['teléfonos'], 'teléfonos', doble=True)
    elipse(*pos['fecha_nac'], 'fecha_nac')
    elipse(*pos['edad'], 'edad', ls='--')
    for k, (x, y) in pos.items():
        ax.plot([x, 5.0 + (x - 5) * 0.35], [y + (0.36 if y < 2.8 else -0.36), 2.8 + (0.4 if y > 2.8 else -0.4)], color=GRIS, lw=1.2)
    for x, t in ((3.6, 'nombre'), (6.4, 'apellido')):
        ax.add_patch(Ellipse((x, 5.35), 1.5, 0.5, fc='white', ec=SOFT, lw=1.3))
        ax.text(x, 5.35, t, ha='center', va='center', fontsize=9, color=DARK)
        ax.plot([x + (0.55 if x < 5 else -0.55), 5.0 + (-0.6 if x < 5 else 0.6)], [5.3, 5.08], color=GRIS, lw=1.0)
    notas = [((0.25, 3.85), 'IDENTIFICADOR\nsubrayado', DARK), ((6.1, 4.05), 'COMPUESTO\nse divide en partes', DARK),
             ((9.85, 3.75), 'MULTIVALUADO\ndoble elipse', DARK), ((0.25, 0.45), 'SIMPLE y UNIVALORADO\nun solo valor', DARK),
             ((9.85, 0.4), 'DERIVADO\ncontorno punteado:\nse calcula desde fecha_nac', AMB)]
    for (x, y), t, col in notas:
        ax.text(x, y, t, ha='left' if x < 5 else ('right' if x > 9 else 'left'), va='center', fontsize=8.3, color=col, style='italic')
    fin(fig, 'fig_12_1_atributos.png')


def grado():
    fig, ax = plt.subplots(figsize=(11, 4.4)); ax.set_xlim(0, 11); ax.set_ylim(0, 4.6); ax.axis('off')

    def ent(x, y, t, w=1.7):
        ax.add_patch(Rectangle((x - w / 2, y - 0.3), w, 0.6, fc=MED, ec=DARK, lw=1.6))
        ax.text(x, y, t, ha='center', va='center', color='white', fontweight='bold', fontsize=9.5)

    def rombo(x, y, t, w=1.5, h=0.75):
        ax.add_patch(Polygon([(x - w / 2, y), (x, y + h / 2), (x + w / 2, y), (x, y - h / 2)], fc=AMBL, ec=AMB, lw=1.6))
        ax.text(x, y, t, ha='center', va='center', fontsize=9, color='#5A4200', fontweight='bold')
    # unaria
    ax.text(1.6, 4.3, 'UNARIA (grado 1)', ha='center', fontweight='bold', color=DARK)
    ent(1.6, 1.4, 'EMPLEADO'); rombo(1.6, 2.9, 'supervisa')
    ax.plot([1.0, 1.0, 0.85], [1.7, 2.9, 2.9], color=GRIS); ax.plot([0.85, 0.85], [2.9, 2.9])
    ax.plot([1.0, 0.85], [1.7, 1.7], color=GRIS)
    ax.plot([0.85, 0.85, 1.0], [1.7, 2.9, 2.9], color=GRIS)
    ax.plot([2.2, 2.35, 2.35], [1.7, 1.7, 2.9], color=GRIS); ax.plot([2.35, 2.35], [2.9, 2.9], color=GRIS)
    ax.plot([0.85, 0.85], [1.7, 2.9], color=GRIS); ax.plot([0.85, 0.87], [2.9, 2.9])
    ax.text(0.55, 2.3, 'supervisor', rotation=90, va='center', fontsize=8, color=GRIS, style='italic')
    ax.text(2.6, 2.3, 'supervisado', rotation=90, va='center', fontsize=8, color=GRIS, style='italic')
    ax.plot([2.35, 2.35], [2.9, 2.9]); ax.plot([2.35, 2.35], [2.9, 2.9])
    ax.plot([2.35, 2.35], [2.9, 2.9])
    ax.plot([2.35, 2.35], [2.9, 2.9])
    ax.plot([0.85, 0.85], [2.9, 2.9])
    ax.plot([0.85, 0.85], [2.9, 2.9])
    ax.plot([0.85, 0.85], [2.9, 2.9])
    ax.plot([0.85, 0.85], [2.9, 2.9])
    ax.plot([0.85, 0.85], [2.9, 2.9])
    ax.plot([0.85, 0.85], [2.9, 2.9])
    ax.plot([0.85, 0.85], [2.9, 2.9])
    ax.plot([0.85, 0.85], [2.9, 2.9])
    ax.plot([0.85, 0.85], [2.9, 2.9])
    ax.plot([0.85, 0.85], [2.9, 2.9])
    # binaria
    ax.text(5.0, 4.3, 'BINARIA (grado 2)', ha='center', fontweight='bold', color=DARK)
    ent(3.75, 2.4, 'CLIENTE', 1.5); rombo(5.0, 2.4, 'realiza', 1.3); ent(6.25, 2.4, 'VENTA', 1.5)
    ax.plot([4.5, 4.35], [2.4, 2.4], color=GRIS); ax.plot([5.65, 5.5], [2.4, 2.4], color=GRIS)
    ax.text(4.45, 2.55, '1', fontsize=9, color=DARK); ax.text(5.6, 2.55, 'N', fontsize=9, color=DARK)
    # ternaria
    ax.text(9.0, 4.3, 'TERNARIA (grado 3)', ha='center', fontweight='bold', color=DARK)
    rombo(9.0, 2.2, 'dicta', 1.3)
    ent(9.0, 3.55, 'DOCENTE'); ent(7.75, 0.75, 'MATERIA', 1.5); ent(10.25, 0.75, 'CURSO', 1.5)
    ax.plot([9.0, 9.0], [2.58, 3.25], color=GRIS); ax.plot([8.6, 7.9], [1.98, 1.05], color=GRIS); ax.plot([9.4, 10.1], [1.98, 1.05], color=GRIS)
    fin(fig, 'fig_13_3_grado.png')


def grado_limpio():
    """Versión prolija de la figura de grado (reemplaza a grado())."""
    fig, ax = plt.subplots(figsize=(11, 4.4)); ax.set_xlim(0, 11); ax.set_ylim(0, 4.6); ax.axis('off')

    def ent(x, y, t, w=1.7):
        ax.add_patch(Rectangle((x - w / 2, y - 0.3), w, 0.6, fc=MED, ec=DARK, lw=1.6, zorder=3))
        ax.text(x, y, t, ha='center', va='center', color='white', fontweight='bold', fontsize=9.5, zorder=4)

    def rombo(x, y, t, w=1.5, h=0.75):
        ax.add_patch(Polygon([(x - w / 2, y), (x, y + h / 2), (x + w / 2, y), (x, y - h / 2)], fc=AMBL, ec=AMB, lw=1.6, zorder=3))
        ax.text(x, y, t, ha='center', va='center', fontsize=9, color='#5A4200', fontweight='bold', zorder=4)
    for x0 in (3.3, 7.0):
        ax.plot([x0, x0], [0.3, 4.4], color='#DDDDDD', lw=1)
    # unaria
    ax.text(1.65, 4.25, 'UNARIA (grado 1)', ha='center', fontweight='bold', color=DARK)
    ent(1.65, 1.2, 'EMPLEADO'); rombo(1.65, 3.0, 'supervisa')
    ax.plot([1.1, 0.55, 0.55, 0.9], [1.2, 1.2, 3.0, 3.0], color=GRIS, lw=1.4)
    ax.plot([2.2, 2.75, 2.75, 2.4], [1.2, 1.2, 3.0, 3.0], color=GRIS, lw=1.4)
    ax.text(0.4, 2.1, 'supervisor', rotation=90, va='center', ha='center', fontsize=8, color=GRIS, style='italic')
    ax.text(2.9, 2.1, 'supervisado', rotation=90, va='center', ha='center', fontsize=8, color=GRIS, style='italic')
    ax.text(0.65, 1.32, '1', fontsize=9, color=DARK); ax.text(2.55, 1.32, 'N', fontsize=9, color=DARK)
    # binaria
    ax.text(5.15, 4.25, 'BINARIA (grado 2)', ha='center', fontweight='bold', color=DARK)
    ax.plot([4.0, 6.3], [2.3, 2.3], color=GRIS, lw=1.4, zorder=1)
    ent(3.95, 2.3, 'CLIENTE', 1.15); rombo(5.15, 2.3, 'realiza', 1.1, 0.7); ent(6.35, 2.3, 'VENTA', 1.05)
    ax.text(4.62, 2.45, '1', fontsize=9.5, color=DARK, fontweight='bold'); ax.text(5.6, 2.45, 'N', fontsize=9.5, color=DARK, fontweight='bold')
    # ternaria
    ax.text(9.0, 4.25, 'TERNARIA (grado 3)', ha='center', fontweight='bold', color=DARK)
    ax.plot([9.0, 9.0], [2.2, 3.35], color=GRIS, lw=1.4, zorder=1)
    ax.plot([9.0, 7.85], [2.2, 0.85], color=GRIS, lw=1.4, zorder=1)
    ax.plot([9.0, 10.15], [2.2, 0.85], color=GRIS, lw=1.4, zorder=1)
    rombo(9.0, 2.2, 'dicta', 1.3)
    ent(9.0, 3.55, 'DOCENTE'); ent(7.85, 0.75, 'MATERIA', 1.5); ent(10.15, 0.75, 'CURSO', 1.5)
    fin(fig, 'fig_13_3_grado.png')


def dependencias():
    fig, ax = plt.subplots(figsize=(11.6, 5.4)); ax.set_xlim(0, 11.6); ax.set_ylim(0, 5.4); ax.axis('off')
    cols = ['venta', 'producto', 'fecha', 'cliente', 'nombre_cliente', 'nombre_prod', 'categoría', 'precio', 'cantidad']
    xs = {}
    w = 1.2
    Y = 2.6
    ax.text(0.15, 5.15, 'Tabla única del Copetín · clave compuesta: venta + producto', fontsize=10, color=DARK, fontweight='bold')
    for i, cnom in enumerate(cols):
        x = 0.15 + i * 1.25
        clave = cnom in ('venta', 'producto')
        ax.add_patch(Rectangle((x, Y), w, 0.62, fc=MED if clave else 'white', ec=DARK, lw=1.4))
        ax.text(x + w / 2, Y + 0.31, cnom, ha='center', va='center', fontsize=8.6, color='white' if clave else DARK, fontweight='bold' if clave else 'normal')
        xs[cnom] = x + w / 2

    def arco(a, b, col, rad, abajo=False, lw=1.6):
        y0 = Y if abajo else Y + 0.62
        ax.add_patch(FancyArrowPatch((xs[a], y0), (xs[b], y0), connectionstyle='arc3,rad=%s' % rad, arrowstyle='-|>', mutation_scale=12, color=col, lw=lw))
    arco('venta', 'fecha', AMB, -0.45); arco('venta', 'cliente', AMB, -0.38)
    arco('cliente', 'nombre_cliente', ROJO, -0.7)
    for t in ('nombre_prod', 'categoría', 'precio'):
        arco('producto', t, AMB, 0.22, abajo=True)
    # clave completa: corchete bajo venta+producto y flecha a cantidad
    yb = 0.75
    ax.plot([xs['venta'], xs['venta'], xs['producto'], xs['producto']], [Y, yb, yb, Y], color=MED, lw=2.2)
    ax.add_patch(FancyArrowPatch(((xs['venta'] + xs['producto']) / 2, yb), (xs['cantidad'], Y), connectionstyle='angle,angleA=0,angleB=90,rad=0', arrowstyle='-|>', mutation_scale=13, color=MED, lw=2.2))
    ley = [(MED, 'completa: necesita venta + producto juntos (queda en DetalleVenta)'),
           (AMB, 'parcial: alcanza con una parte de la clave (la elimina la 2FN)'),
           (ROJO, 'transitiva: pasa por cliente, que no es clave (la elimina la 3FN)')]
    for i, (col, t) in enumerate(ley):
        y = 4.75 - i * 0.36
        ax.plot([6.6, 7.2], [y, y], color=col, lw=2.4)
        ax.text(7.3, y, t, va='center', fontsize=8.4, color=GRIS)
    fin(fig, 'fig_16_1_dependencias.png')


if __name__ == '__main__':
    niveles(); atributos(); grado_limpio(); dependencias()
    from PIL import Image
    for f in sorted(os.listdir(OUT)):
        im = Image.open(OUT + f).convert('L'); px = im.getdata()
        tinta = sum(1 for v in px if v < 100) / len(px)
        print(f, im.size, 'tinta %.2f%%' % (tinta * 100))
        assert tinta > 0.002
