# -*- coding: utf-8 -*-
"""Diagramas nuevos de Algorítmica 2.º (estándar gráfico: matplotlib, 200 dpi, DejaVu Sans, VERDE BTI + acentos).
Los siete corresponden a clases que no tenían figura (2, 4, 5, 9, 12, 16, 17)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle, FancyArrowPatch, Ellipse
import os
OUT = '/home/claude/alg2/build/figs_new/'
os.makedirs(OUT, exist_ok=True)
DARK, MED, LIGHT, SOFT = '#1B5E20', '#2E7D32', '#E8F5E9', '#A5D6A7'
AMB, AMBL, ROJO, AZUL, GRIS = '#B8860B', '#FFF4D6', '#C62828', '#1565C0', '#616161'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})


def caja(ax, x, y, w, h, txt, fc=LIGHT, ec=MED, tc=DARK, fs=10, bold=True, lw=1.6, r=0.04):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.01,rounding_size=%s' % r, fc=fc, ec=ec, lw=lw))
    ax.text(x + w / 2, y + h / 2, txt, ha='center', va='center', color=tc, fontsize=fs, fontweight='bold' if bold else 'normal')


def ovalo(ax, cx, cy, w, h, txt):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h, boxstyle='round,pad=0.01,rounding_size=%s' % (h / 2), fc=MED, ec=DARK, lw=1.6))
    ax.text(cx, cy, txt, ha='center', va='center', color='white', fontweight='bold', fontsize=10)


def rombo(ax, cx, cy, w, h, txt, fs=9.5):
    ax.add_patch(Polygon([(cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2), (cx - w / 2, cy)], closed=True, fc=AMBL, ec=AMB, lw=1.6))
    ax.text(cx, cy, txt, ha='center', va='center', color='#5A4200', fontsize=fs, fontweight='bold')


def romboide(ax, cx, cy, w, h, txt, fs=9.5):
    d = 0.25
    ax.add_patch(Polygon([(cx - w / 2 + d, cy + h / 2), (cx + w / 2 + d, cy + h / 2), (cx + w / 2 - d, cy - h / 2), (cx - w / 2 - d, cy - h / 2)],
                         closed=True, fc='white', ec=MED, lw=1.6))
    ax.text(cx, cy, txt, ha='center', va='center', color=DARK, fontsize=fs, fontweight='bold')


def flecha(ax, x1, y1, x2, y2, c=GRIS, lw=1.5, ms=14):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=ms, color=c, lw=lw))


def linea(ax, xs, ys, c=GRIS, lw=1.5):
    ax.plot(xs, ys, color=c, lw=lw, solid_capstyle='round')


def fin(fig, nombre):
    fig.savefig(OUT + nombre, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)


def si_simple():
    fig, ax = plt.subplots(figsize=(7.2, 8.2)); ax.set_xlim(0, 8); ax.set_ylim(0, 9.4); ax.axis('off')
    ovalo(ax, 3.5, 8.9, 2.0, 0.6, 'Inicio')
    romboide(ax, 3.5, 7.75, 3.2, 0.75, 'Leer monto')
    rombo(ax, 3.5, 6.0, 3.6, 1.6, 'monto >= 50000')
    caja(ax, 1.9, 3.75, 3.2, 0.9, 'monto ← monto\n− monto * 0.10', fc='white', fs=9.5)
    romboide(ax, 3.5, 2.0, 3.6, 0.75, 'Escribir "Total: ", monto', fs=9)
    ovalo(ax, 3.5, 0.75, 2.0, 0.6, 'Fin')
    flecha(ax, 3.5, 8.6, 3.5, 8.13); flecha(ax, 3.5, 7.37, 3.5, 6.8)
    flecha(ax, 3.5, 5.2, 3.5, 4.65); ax.text(3.65, 4.95, 'Sí (V)', color=MED, fontweight='bold', fontsize=9.5)
    linea(ax, [5.3, 6.6, 6.6], [6.0, 6.0, 3.0]); flecha(ax, 6.6, 3.0, 3.6, 3.0)
    ax.text(5.5, 6.15, 'No (F)', color=ROJO, fontweight='bold', fontsize=9.5)
    linea(ax, [3.5, 3.5], [3.75, 3.0]); flecha(ax, 3.5, 3.0, 3.5, 2.38)
    ax.plot([3.5], [3.0], 'o', color=GRIS, ms=5)
    flecha(ax, 3.5, 1.62, 3.5, 1.05)
    ax.text(6.75, 4.5, 'el bloque\nse saltea', color=ROJO, fontsize=8.5, style='italic')
    ax.text(0.1, 3.05, 'los dos caminos\nse juntan acá', color=GRIS, fontsize=8.5, style='italic', va='center')
    fin(fig, 'fig_n_si_simple.png')


def condicion():
    fig, ax = plt.subplots(figsize=(10.5, 4.6)); ax.set_xlim(0, 10.5); ax.set_ylim(0, 4.6); ax.axis('off')
    ax.text(5.25, 4.3, '(monto >= 50000)   Y   (enBarrio = Verdadero)', ha='center', fontsize=12, fontweight='bold', color=DARK, family='DejaVu Sans Mono')
    ax.text(5.25, 3.85, 'con monto = 60.000 y enBarrio = Falso', ha='center', fontsize=9.5, color=GRIS, style='italic')
    caja(ax, 0.5, 2.25, 3.6, 0.95, '60000 >= 50000', fc='white', fs=10)
    caja(ax, 6.4, 2.25, 3.6, 0.95, 'Falso = Verdadero', fc='white', fs=10)
    caja(ax, 1.4, 1.0, 1.8, 0.65, 'V', fc=LIGHT, ec=MED, tc=MED, fs=13)
    caja(ax, 7.3, 1.0, 1.8, 0.65, 'F', fc='#FDECEA', ec=ROJO, tc=ROJO, fs=13)
    flecha(ax, 2.3, 2.25, 2.3, 1.68); flecha(ax, 8.2, 2.25, 8.2, 1.68)
    rombo(ax, 5.25, 1.33, 1.7, 1.0, 'Y', fs=12)
    flecha(ax, 3.2, 1.33, 4.42, 1.33); flecha(ax, 7.3, 1.33, 6.08, 1.33)
    flecha(ax, 5.25, 0.83, 5.25, 0.32)
    ax.text(5.25, 0.12, 'V Y F = F  →  "Envío con costo"', ha='center', fontsize=10.5, fontweight='bold', color=ROJO)
    ax.text(0.5, 3.35, '1.ª comparación', fontsize=9, color=GRIS); ax.text(6.4, 3.35, '2.ª comparación', fontsize=9, color=GRIS)
    fin(fig, 'fig_n_condicion.png')


def segun():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.4, 6.6), gridspec_kw={'width_ratios': [1.05, 1]})
    for a in (a1, a2):
        a.set_xlim(0, 7); a.set_ylim(0, 7.4); a.axis('off')
    a1.set_title('Con Si anidados: una pregunta por valor', fontsize=10.5, color=DARK, fontweight='bold')
    a2.set_title('Con Segun: un reparto en un solo paso', fontsize=10.5, color=DARK, fontweight='bold')
    salidas = ['Chipa', 'Empanada', 'Mixto', 'Sopa']
    for i, s in enumerate(salidas):
        y = 6.4 - i * 1.45
        rombo(a1, 1.6, y, 2.4, 0.95, 'opcion = %d' % (i + 1), fs=9)
        caja(a1, 3.6, y - 0.3, 2.0, 0.6, s, fc='white', fs=9)
        flecha(a1, 2.8, y, 3.58, y); a1.text(2.95, y + 0.1, 'Sí', fontsize=8.5, color=MED, fontweight='bold')
        if i < 3:
            flecha(a1, 1.6, y - 0.48, 1.6, y - 0.97); a1.text(1.7, y - 0.78, 'No', fontsize=8.5, color=ROJO, fontweight='bold')
    flecha(a1, 1.6, 6.4 - 3 * 1.45 - 0.48, 1.6, 0.55); a1.text(1.7, 1.0, 'No', fontsize=8.5, color=ROJO, fontweight='bold')
    caja(a1, 0.5, 0.0, 2.2, 0.55, 'Opción inválida', fc='#FDECEA', ec=ROJO, tc=ROJO, fs=9)
    a1.text(6.9, 0.3, '4 preguntas\nen el peor caso', ha='right', fontsize=8.5, color=GRIS, style='italic')
    rombo(a2, 3.5, 6.2, 2.6, 1.1, 'Segun\nopcion', fs=10)
    xs = [0.75, 2.15, 3.55, 4.95, 6.3]
    labs = ['1', '2', '3', '4', 'De Otro\nModo']
    outs = ['Chipa', 'Empanada', 'Mixto', 'Sopa', 'Opción\ninválida']
    for x, l, o in zip(xs, labs, outs):
        linea(a2, [3.5, x], [5.65, 4.4]); flecha(a2, x, 4.4, x, 3.25)
        a2.text(x, 3.85, l, ha='center', fontsize=9, color=AMB, fontweight='bold', bbox=dict(fc='white', ec='none', pad=1))
        rojo = 'Opción' in o
        caja(a2, x - 0.62, 2.35, 1.24, 0.85, o, fc='#FDECEA' if rojo else 'white', ec=ROJO if rojo else MED, tc=ROJO if rojo else DARK, fs=8.5)
    a2.text(3.5, 1.4, 'una sola evaluación de opcion', ha='center', fontsize=8.5, color=GRIS, style='italic')
    plt.tight_layout()
    fin(fig, 'fig_n_segun.png')


def maximo():
    v = [420000, 500000, 450000, 580000, 850000, 1100000, 300000]
    dias = ['lun', 'mar', 'mié', 'jue', 'vie', 'sáb', 'dom']
    fig, ax = plt.subplots(figsize=(11, 5.0))
    may = []; m = 0; pos = 0; cambios = []
    for i, x in enumerate(v):
        if i == 0 or x > m:
            m = x; pos = i + 1
            if i > 0:
                cambios.append(i)
        may.append(m)
    cols = [MED if i in cambios else (AZUL if i == 0 else SOFT) for i in range(7)]
    ax.bar(range(7), [x / 1000 for x in v], color=cols, ec=DARK, lw=0.8, width=0.62)
    ax.step(range(7), [x / 1000 for x in may], where='mid', color=AMB, lw=2.2, label='valor de mayor después de cada paso')
    for i, x in enumerate(v):
        ax.text(i, x / 1000 - 40, '{:,}'.format(x).replace(',', '.'), ha='center', va='top', fontsize=8.5, color=DARK if cols[i] == SOFT else 'white', fontweight='bold')
    ax.set_xticks(range(7)); ax.set_xticklabels(['%d\n%s' % (i + 1, d) for i, d in enumerate(dias)])
    ax.set_ylabel('venta (miles de G.)'); ax.set_ylim(0, 1500)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(fc=AZUL, ec=DARK, label='día 1: valor inicial de mayor'),
                       Patch(fc=MED, ec=DARK, label='mayor cambia (días 2, 4, 5 y 6)'),
                       Patch(fc=SOFT, ec=DARK, label='mayor no cambia'),
                       plt.Line2D([0], [0], color=AMB, lw=2.2, label='mayor después de cada paso')],
              loc='upper left', fontsize=8.5, frameon=False)
    ax.text(6.4, 1470, 'resultado:\nmayor = 1.100.000\nposMayor = 6', ha='right', va='top', fontsize=9, color=DARK, fontweight='bold')
    fin(fig, 'fig_n_maximo.png')


def azar():
    fig, ax = plt.subplots(figsize=(11, 3.9)); ax.set_xlim(-0.6, 9.6); ax.set_ylim(0, 3.9); ax.axis('off')
    ax.text(0, 3.55, 'Azar(7)', fontsize=11, fontweight='bold', color=DARK, family='DejaVu Sans Mono')
    ax.text(1.7, 3.55, 'devuelve un entero entre 0 y 6: siete valores posibles', fontsize=9.5, color=GRIS, va='baseline')
    for i in range(7):
        caja(ax, 1.6 + i * 1.0, 2.55, 0.8, 0.65, str(i), fc='white', fs=11)
    ax.text(0, 1.95, '+ 1', fontsize=11, fontweight='bold', color=AMB, family='DejaVu Sans Mono')
    ax.text(0, 1.6, 'corre el rango:\nmín pasa a 1', fontsize=8.5, color=GRIS, va='top')
    for i in range(7):
        flecha(ax, 2.0 + i * 1.0, 2.53, 2.0 + i * 1.0, 1.62, c=AMB, ms=11)
        caja(ax, 1.6 + i * 1.0, 0.9, 0.8, 0.65, str(i + 1), fc=MED, ec=DARK, tc='white', fs=11)
    ax.text(0, 0.35, 'Azar(7) + 1  →  un número entre 1 y 7, cada uno con chance 1 entre 7', fontsize=10, fontweight='bold', color=DARK)
    ax.text(9.5, 3.55, '7 = máx − mín + 1', ha='right', fontsize=9, color=AZUL, style='italic')
    fin(fig, 'fig_n_azar.png')


def modos():
    fig, ax = plt.subplots(figsize=(11.5, 6.0)); ax.set_xlim(0, 11.5); ax.set_ylim(0, 6.0); ax.axis('off')
    for i, (t, s) in enumerate([('ABRIR', 'nombre + modo'), ('TRABAJAR', 'leer o escribir líneas'), ('CERRAR', 'vacía el buffer y libera')]):
        caja(ax, 0.4 + i * 3.8, 4.55, 3.0, 1.05, t + '\n' + s, fc=MED, ec=DARK, tc='white', fs=10)
        if i < 2:
            flecha(ax, 3.45 + i * 3.8, 5.07, 4.15 + i * 3.8, 5.07, c=DARK)
    filas = [('Lectura', 'Leer Archivo', 'se lee tal como está', 'no cambia', LIGHT),
             ('Escritura', 'Escribir Archivo', 'se empieza en blanco', 'se pierde', '#FDECEA'),
             ('Agregar', 'Escribir Archivo', 'se escribe al final', 'se conserva', AMBL)]
    ax.text(0.4, 3.85, 'Modo', fontweight='bold', color=DARK); ax.text(2.4, 3.85, 'Instrucción', fontweight='bold', color=DARK)
    ax.text(5.1, 3.85, 'Qué hace', fontweight='bold', color=DARK); ax.text(8.6, 3.85, 'Contenido anterior', fontweight='bold', color=DARK)
    for k, (m, ins, q, c, fc) in enumerate(filas):
        y = 2.85 - k * 1.05
        ax.add_patch(Rectangle((0.3, y), 10.9, 0.85, fc=fc, ec=SOFT, lw=1))
        ax.text(0.45, y + 0.42, m, va='center', fontweight='bold', color=DARK, fontsize=10.5)
        ax.text(2.4, y + 0.42, ins, va='center', color=DARK, family='DejaVu Sans Mono', fontsize=9.5)
        ax.text(5.1, y + 0.42, q, va='center', color=DARK, fontsize=10)
        ax.text(8.6, y + 0.42, c, va='center', color=ROJO if c == 'se pierde' else DARK, fontsize=10, fontweight='bold')
    fin(fig, 'fig_n_modos.png')


def buffer():
    fig, ax = plt.subplots(figsize=(11.5, 4.8)); ax.set_xlim(0, 11.5); ax.set_ylim(0, 4.8); ax.axis('off')
    caja(ax, 0.3, 1.4, 2.3, 2.0, 'DISCO\nventas_semana.txt\n7 líneas', fc=AMBL, ec=AMB, tc='#5A4200', fs=9.5)
    caja(ax, 4.2, 0.6, 3.0, 3.6, '', fc='#F7FBF7', ec=SOFT)
    ax.text(5.7, 3.95, 'BUFFER (RAM)  · 4 líneas', ha='center', fontsize=9.5, fontweight='bold', color=DARK)
    for k, (ini, fin_, y) in enumerate([(1, 4, 2.65), (5, 7, 1.0)]):
        for j in range(ini, fin_ + 1):
            caja(ax, 4.4 + (j - ini) * 0.7, y, 0.6, 0.55, str(j), fc='white', fs=9)
        ax.text(5.8, y + 0.8, 'tanda %d' % (k + 1), ha='center', fontsize=8.5, color=GRIS, style='italic')
        flecha(ax, 2.65, 2.4 if k == 0 else 1.9, 4.35, y + 0.27, c=AMB, lw=2.2)
        ax.text(3.45, (2.4 if k == 0 else 1.9) + (0.42 if k == 0 else -0.95), 'acceso %d\nal disco' % (k + 1), ha='center', fontsize=8.5, color=AMB, fontweight='bold')
    caja(ax, 8.8, 1.4, 2.4, 2.0, 'PROGRAMA\nLeer Archivo linea\n(7 veces)', fc=MED, ec=DARK, tc='white', fs=9.5)
    flecha(ax, 7.25, 2.9, 8.75, 2.6, c=MED, lw=2); flecha(ax, 7.25, 1.3, 8.75, 2.0, c=MED, lw=2)
    ax.text(8.0, 3.35, 'de a una línea', ha='center', fontsize=8.5, color=MED)
    ax.text(5.75, 0.15, '7 lecturas del programa  ·  2 accesos reales al disco', ha='center', fontsize=10, fontweight='bold', color=DARK)
    fin(fig, 'fig_n_buffer.png')


def pfi_caja():
    fig, ax = plt.subplots(figsize=(8.6, 10.2)); ax.set_xlim(0, 10); ax.set_ylim(0, 12.2); ax.axis('off')
    cx = 4.2
    ovalo(ax, cx, 11.7, 2.2, 0.62, 'Inicio')
    caja(ax, cx - 1.4, 10.45, 2.8, 0.62, 'total <- 0', fc='white', fs=10)
    romboide(ax, cx, 9.35, 4.6, 0.7, 'Leer producto, precio, cantidad', fs=9.5)
    # módulo (rectángulo con barras laterales)
    ax.add_patch(Rectangle((cx - 2.6, 7.95), 5.2, 0.7, fc='white', ec=MED, lw=1.6))
    for x in (cx - 2.4, cx + 2.4):
        ax.plot([x, x], [7.95, 8.65], color=MED, lw=1.4)
    ax.text(cx, 8.3, 'sub <- CalcularTotal(precio, cantidad)', ha='center', va='center', fontsize=9.5, color=DARK, fontweight='bold')
    ax.text(cx + 2.75, 8.3, 'módulo\n(función)', ha='left', va='center', fontsize=8.5, color=MED, style='italic')
    caja(ax, cx - 1.6, 6.75, 3.2, 0.62, 'total <- total + sub', fc='white', fs=10)
    rombo(ax, cx, 5.55, 3.0, 1.1, '¿otro\nproducto?', fs=9.5)
    rombo(ax, cx, 3.75, 3.0, 1.1, '¿total >=\n50000?', fs=9.5)
    caja(ax, cx + 2.2, 2.55, 2.9, 0.62, 'total <- total\n- total * 0.10', fc='white', fs=9)
    romboide(ax, cx, 1.5, 4.4, 0.7, 'Escribir el ticket con el total', fs=9.5)
    ovalo(ax, cx, 0.45, 2.2, 0.62, 'Fin')
    flecha(ax, cx, 11.39, cx, 11.09); flecha(ax, cx, 10.45, cx, 9.72); flecha(ax, cx, 8.98, cx, 8.67)
    flecha(ax, cx, 7.95, cx, 7.39); flecha(ax, cx, 6.75, cx, 6.12)
    # Sí: vuelve a leer
    linea(ax, [cx - 1.5, cx - 3.6, cx - 3.6], [5.55, 5.55, 9.35]); flecha(ax, cx - 3.6, 9.35, cx - 2.45, 9.35)
    ax.text(cx - 2.9, 5.7, 'Sí', color=MED, fontweight='bold', fontsize=10)
    flecha(ax, cx, 5.0, cx, 4.32); ax.text(cx + 0.15, 4.55, 'No', color=ROJO, fontweight='bold', fontsize=10)
    # decisión del descuento
    linea(ax, [cx + 1.5, cx + 3.65], [3.75, 3.75]); flecha(ax, cx + 3.65, 3.75, cx + 3.65, 3.19)
    ax.text(cx + 1.7, 3.9, 'Sí', color=MED, fontweight='bold', fontsize=10)
    linea(ax, [cx + 3.65, cx + 3.65, cx], [2.55, 2.1, 2.1])
    flecha(ax, cx, 3.2, cx, 1.87); ax.text(cx + 0.15, 2.75, 'No', color=ROJO, fontweight='bold', fontsize=10)
    ax.plot([cx], [2.1], 'o', color=GRIS, ms=5)
    flecha(ax, cx, 1.13, cx, 0.78)
    ax.text(9.9, 6.9, 'secuencia, decisión,\nciclo y módulo:\ntodo lo del año\nen un programa', ha='right', va='center', fontsize=9, color=GRIS, style='italic')
    fin(fig, 'fig_pfi_caja.png')


if __name__ == '__main__':
    for f in (si_simple, condicion, segun, maximo, azar, modos, buffer, pfi_caja):
        f()
    print(sorted(os.listdir(OUT)))
