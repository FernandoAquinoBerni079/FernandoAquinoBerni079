# -*- coding: utf-8 -*-
"""Figuras nuevas de Algorítmica 1.º (matplotlib, 200 dpi, DejaVu Sans, VERDE BTI + acentos)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle, FancyArrowPatch, Ellipse
import os
OUT = '/home/claude/alg1/build/figs_new/'
os.makedirs(OUT, exist_ok=True)
DARK, MED, LIGHT, SOFT = '#1B5E20', '#2E7D32', '#E8F5E9', '#A5D6A7'
AMB, AMBL, ROJO, ROJOL, AZUL, GRIS = '#B8860B', '#FFF4D6', '#C62828', '#FDECEA', '#1565C0', '#616161'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})


def caja(ax, x, y, w, h, txt, fc=LIGHT, ec=MED, tc=DARK, fs=10, bold=True, lw=1.6):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.01,rounding_size=0.06', fc=fc, ec=ec, lw=lw))
    ax.text(x + w / 2, y + h / 2, txt, ha='center', va='center', color=tc, fontsize=fs, fontweight='bold' if bold else 'normal')


def rombo(ax, cx, cy, w, h, txt, fs=9.5):
    ax.add_patch(Polygon([(cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2), (cx - w / 2, cy)], closed=True, fc=AMBL, ec=AMB, lw=1.6))
    ax.text(cx, cy, txt, ha='center', va='center', color='#5A4200', fontsize=fs, fontweight='bold')


def ovalo(ax, cx, cy, w, h, txt):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h, boxstyle='round,pad=0.01,rounding_size=%s' % (h / 2), fc=MED, ec=DARK, lw=1.6))
    ax.text(cx, cy, txt, ha='center', va='center', color='white', fontweight='bold', fontsize=10)


def romboide(ax, cx, cy, w, h, txt, fs=9.5):
    d = 0.22
    ax.add_patch(Polygon([(cx - w / 2 + d, cy + h / 2), (cx + w / 2 + d, cy + h / 2), (cx + w / 2 - d, cy - h / 2), (cx - w / 2 - d, cy - h / 2)], closed=True, fc='white', ec=MED, lw=1.6))
    ax.text(cx, cy, txt, ha='center', va='center', color=DARK, fontsize=fs, fontweight='bold')


def flecha(ax, x1, y1, x2, y2, c=GRIS, lw=1.5):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=13, color=c, lw=lw))


def linea(ax, xs, ys, c=GRIS):
    ax.plot(xs, ys, color=c, lw=1.5)


def fin(fig, n):
    fig.savefig(OUT + n, dpi=200, bbox_inches='tight', facecolor='white'); plt.close(fig)


def lienzo(w, h, W, H):
    fig, ax = plt.subplots(figsize=(w, h)); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off'); return fig, ax


def pertenencia():
    fig, ax = lienzo(9, 4.6, 9, 4.6)
    ax.add_patch(Ellipse((3.6, 2.3), 6.0, 3.6, fc=LIGHT, ec=MED, lw=2))
    ax.text(1.0, 3.95, 'M = menú del día', color=DARK, fontsize=11, fontweight='bold')
    for (x, y, t) in ((2.2, 2.9, 'chipa'), (3.9, 3.1, 'mixta'), (5.2, 2.4, 'empanada'), (2.6, 1.6, 'coquito'), (4.3, 1.4, 'gaseosa')):
        ax.plot([x], [y], 'o', color=MED, ms=7); ax.text(x + 0.12, y + 0.12, t, color=DARK, fontsize=10.5)
    ax.plot([7.8], [2.3], 'o', color=ROJO, ms=7); ax.text(7.95, 2.42, 'pizza', color=ROJO, fontsize=10.5)
    ax.text(3.6, 0.15, 'chipa ∈ M   ·   gaseosa ∈ M', ha='center', color=MED, fontsize=11, fontweight='bold')
    ax.text(7.9, 1.6, 'pizza ∉ M', ha='center', color=ROJO, fontsize=11, fontweight='bold')
    ax.text(3.6, 4.3, 'n(M) = 5', ha='center', color=AMB, fontsize=11, fontweight='bold')
    fin(fig, 'fig_n_pertenencia.png')


def inclusion():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.4))
    for a in (a1, a2):
        a.set_xlim(0, 6); a.set_ylim(0, 4.4); a.axis('off')
        a.add_patch(Ellipse((3, 2.1), 5.4, 3.4, fc=LIGHT, ec=MED, lw=2)); a.text(0.6, 3.6, 'M', color=DARK, fontsize=13, fontweight='bold')
    a1.set_title('Pertenencia: un elemento en un conjunto', fontsize=10.5, color=DARK, fontweight='bold')
    for (x, y, t) in ((1.6, 2.6, 'chipa'), (2.8, 3.0, 'mixta'), (4.1, 2.5, 'gaseosa'), (2.4, 1.3, 'coquito')):
        a1.plot([x], [y], 'o', color=GRIS, ms=6); a1.text(x + 0.1, y + 0.1, t, fontsize=9.5, color=GRIS)
    a1.plot([3.7], [1.4], 'o', color=AMB, ms=9); a1.text(3.85, 1.5, 'empanada', fontsize=10.5, color=AMB, fontweight='bold')
    a1.text(3, 0.05, 'empanada ∈ M', ha='center', fontsize=12, color=AMB, fontweight='bold')
    a2.set_title('Inclusión: un conjunto dentro de otro', fontsize=10.5, color=DARK, fontweight='bold')
    a2.add_patch(Ellipse((3.6, 1.8), 2.4, 1.5, fc=AMBL, ec=AMB, lw=2)); a2.text(2.6, 2.45, 'F', color=AMB, fontsize=12, fontweight='bold')
    for (x, y, t) in ((3.1, 1.9, 'empanada'), (3.6, 1.4, 'coquito')):
        a2.plot([x], [y], 'o', color=AMB, ms=6); a2.text(x + 0.1, y + 0.1, t, fontsize=9.5, color='#5A4200')
    for (x, y, t) in ((1.3, 2.7, 'chipa'), (2.4, 3.2, 'mixta'), (1.3, 1.5, 'gaseosa')):
        a2.plot([x], [y], 'o', color=GRIS, ms=6); a2.text(x + 0.1, y + 0.1, t, fontsize=9.5, color=GRIS)
    a2.text(3, 0.05, 'F ⊆ M   (y también F ⊂ M)', ha='center', fontsize=12, color=AMB, fontweight='bold')
    plt.tight_layout(); fin(fig, 'fig_n_inclusion.png')


def union_inter():
    fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.2))
    for a, tit, modo in ((axs[0], 'A ∪ B: todo lo que cubren los dos óvalos', 'u'), (axs[1], 'A ∩ B: solo la zona común', 'i')):
        a.set_xlim(0, 7); a.set_ylim(0, 4.2); a.axis('off'); a.set_title(tit, fontsize=10.5, color=DARK, fontweight='bold')
        a.add_patch(Rectangle((0.1, 0.1), 6.8, 3.7, fc='white', ec=GRIS, lw=1.2))
        if modo == 'u':
            a.add_patch(Ellipse((2.6, 1.95), 3.4, 2.7, fc=SOFT, ec='none')); a.add_patch(Ellipse((4.4, 1.95), 3.4, 2.7, fc=SOFT, ec='none'))
        else:
            from matplotlib.patches import Ellipse as E
            e1 = E((2.6, 1.95), 3.4, 2.7, fc=SOFT, ec='none'); a.add_patch(e1)
            e2 = E((4.4, 1.95), 3.4, 2.7, fc='none', ec='none'); a.add_patch(e2); e1.set_clip_path(e2)
        a.add_patch(Ellipse((2.6, 1.95), 3.4, 2.7, fc='none', ec=MED, lw=2)); a.add_patch(Ellipse((4.4, 1.95), 3.4, 2.7, fc='none', ec=AZUL, lw=2))
        a.text(1.2, 3.35, 'A (mañana)', color=MED, fontweight='bold'); a.text(4.6, 3.35, 'B (siesta)', color=AZUL, fontweight='bold')
        for (x, y, t) in ((1.6, 2.3, 'chipa'), (1.7, 1.5, 'coquito'), (3.5, 1.95, 'mixta'), (4.8, 2.4, 'empanada'), (4.9, 1.5, 'gaseosa'), (6.2, 0.5, 'jugo')):
            a.text(x, y, t, ha='center', fontsize=9.5, color=DARK if t != 'jugo' else GRIS)
    fin(fig, 'fig_n_union_inter.png')


def clasif_prop():
    fig, ax = lienzo(11, 6.2, 11, 6.2)
    caja(ax, 0.3, 5.3, 2.2, 0.6, 'Expresión', fc=MED, ec=DARK, tc='white')
    preg = [(3.6, 5.6, '¿Es una oración\ndeclarativa?'), (3.6, 4.1, '¿Tiene una variable\nsin valor?'), (3.6, 2.6, '¿Tiene un único\nvalor V o F?'), (3.6, 1.1, '¿Tiene\nconectivos?')]
    flecha(ax, 2.5, 5.6, 2.55, 5.6)
    for k, (x, y, t) in enumerate(preg):
        rombo(ax, x, y, 2.3, 1.15, t, fs=8.5)
        if k < 3:
            flecha(ax, x, y - 0.58, x, preg[k + 1][1] + 0.58)
    res = [(5.6, 'No es proposición\n(pregunta, orden, deseo)', 'No', ROJOL, ROJO), (4.1, 'Proposición abierta\n(«x + 3 = 10»)', 'Sí', AMBL, AMB),
           (2.6, 'No es proposición\n(opinión, paradoja)', 'No', ROJOL, ROJO), (1.1, 'Molecular\n(«hay chipa y cocido»)', 'Sí', LIGHT, MED)]
    for y, t, et, fc, ec in res:
        flecha(ax, 4.75, y, 6.6, y); ax.text(5.6, y + 0.12, et, color=ec, fontweight='bold', fontsize=9)
        caja(ax, 6.6, y - 0.42, 3.6, 0.84, t, fc=fc, ec=ec, tc=DARK, fs=9)
    for y, t in ((4.85, 'Sí'), (3.35, 'No'), (1.85, 'Sí')):
        ax.text(3.75, y, t, color=MED if t == 'Sí' else ROJO, fontweight='bold', fontsize=9)
    flecha(ax, 3.6, 0.52, 3.6, 0.1); ax.text(3.75, 0.3, 'No', color=ROJO, fontweight='bold', fontsize=9)
    caja(ax, 2.0, -0.6, 3.2, 0.62, 'Atómica («hay chipa»)', fc=LIGHT, ec=MED, fs=9)
    ax.set_ylim(-0.75, 6.2)
    fin(fig, 'fig_n_clasif_prop.png')


def condicional():
    fig, ax = lienzo(10.5, 5.2, 10.5, 5.2)
    ax.text(5.25, 4.9, 'p = «comprás dos chipas»     q = «te regalo un cocido»     p → q', ha='center', fontsize=11, color=DARK, fontweight='bold')
    esc = [('p V, q V', 'compraste y te regaló', 'promesa cumplida', 'V', LIGHT, MED), ('p V, q F', 'compraste y no te regaló', 'promesa rota', 'F', ROJOL, ROJO),
           ('p F, q V', 'no compraste y te regaló igual', 'no prometió nada para ese caso', 'V', LIGHT, MED), ('p F, q F', 'no compraste y no te regaló', 'no prometió nada para ese caso', 'V', LIGHT, MED)]
    for k, (a, b, c_, v, fc, ec) in enumerate(esc):
        x = 0.3 + (k % 2) * 5.1; y = 2.45 - (k // 2) * 2.2
        ax.add_patch(FancyBboxPatch((x, y), 4.8, 1.9, boxstyle='round,pad=0.02,rounding_size=0.08', fc=fc, ec=ec, lw=1.8))
        ax.text(x + 0.25, y + 1.5, a, fontsize=10.5, fontweight='bold', color=DARK)
        ax.text(x + 0.25, y + 1.0, b, fontsize=10, color=DARK); ax.text(x + 0.25, y + 0.5, c_, fontsize=9.5, color=GRIS, style='italic')
        ax.text(x + 4.4, y + 0.95, v, fontsize=22, fontweight='bold', color=ec, ha='center', va='center')
    fin(fig, 'fig_n_condicional.png')


def arbol8():
    fig, ax = lienzo(11, 5.4, 11, 5.4)
    def nodo(x, y, t, c):
        ax.add_patch(Ellipse((x, y), 0.6, 0.42, fc=LIGHT if t == 'V' else ROJOL, ec=c, lw=1.4)); ax.text(x, y, t, ha='center', va='center', fontweight='bold', color=c)
    ys = {1: 4.4, 2: 3.0, 3: 1.6}
    ax.text(0.2, 4.4, 'p', fontsize=12, fontweight='bold', color=DARK); ax.text(0.2, 3.0, 'q', fontsize=12, fontweight='bold', color=DARK); ax.text(0.2, 1.6, 'r', fontsize=12, fontweight='bold', color=DARK)
    fila = 0
    for i, pv in enumerate('VF'):
        xp = 2.9 + i * 5.2
        linea(ax, [5.5, xp], [5.25, ys[1] + 0.21]); nodo(xp, ys[1], pv, MED if pv == 'V' else ROJO)
        for j, qv in enumerate('VF'):
            xq = xp - 1.3 + j * 2.6
            linea(ax, [xp, xq], [ys[1] - 0.21, ys[2] + 0.21]); nodo(xq, ys[2], qv, MED if qv == 'V' else ROJO)
            for k, rv in enumerate('VF'):
                xr = xq - 0.65 + k * 1.3
                linea(ax, [xq, xr], [ys[2] - 0.21, ys[3] + 0.21]); nodo(xr, ys[3], rv, MED if rv == 'V' else ROJO)
                fila += 1
                ax.text(xr, 0.85, 'fila %d' % fila, ha='center', fontsize=8.5, color=GRIS)
                ax.text(xr, 0.45, pv + qv + rv, ha='center', fontsize=9.5, color=DARK, fontweight='bold')
    ax.text(5.5, 5.3, 'inicio', ha='center', fontsize=9, color=GRIS)
    fin(fig, 'fig_n_arbol8.png')


def demorgan():
    fig, ax = lienzo(10.5, 3.9, 10.5, 3.9)
    hdr = ['p', 'q', 'p ∧ q', '¬(p ∧ q)', '¬p', '¬q', '¬p ∨ ¬q']
    rows = [['V', 'V', 'V', 'F', 'F', 'F', 'F'], ['V', 'F', 'F', 'V', 'F', 'V', 'V'], ['F', 'V', 'F', 'V', 'V', 'F', 'V'], ['F', 'F', 'F', 'V', 'V', 'V', 'V']]
    w = 1.45; x0 = 0.1
    for j, h in enumerate(hdr):
        dest = j in (3, 6)
        ax.add_patch(Rectangle((x0 + j * w, 3.0), w, 0.6, fc=AMB if dest else DARK, ec='white'))
        ax.text(x0 + j * w + w / 2, 3.3, h, ha='center', va='center', color='white', fontweight='bold', fontsize=10.5)
        for i, r in enumerate(rows):
            v = r[j]; y = 2.4 - i * 0.6
            ax.add_patch(Rectangle((x0 + j * w, y), w, 0.6, fc=(AMBL if dest else (LIGHT if v == 'V' else ROJOL)), ec='white'))
            ax.text(x0 + j * w + w / 2, y + 0.3, v, ha='center', va='center', fontweight='bold', color=MED if v == 'V' else ROJO, fontsize=11)
    ax.text(5.25, 0.0, 'Las columnas resaltadas coinciden fila por fila: F, V, V, V  →  ¬(p ∧ q) ≡ ¬p ∨ ¬q', ha='center', fontsize=10.5, color=DARK, fontweight='bold')
    fin(fig, 'fig_n_demorgan.png')


def cuantif():
    fig, ax = plt.subplots(figsize=(11, 3.9))
    datos = [('coquito', 500), ('chipa', 4000), ('empanada', 6000), ('gaseosa', 8000), ('mixta', 10000)]
    for k, (t, v) in enumerate(datos):
        c = ROJO if v >= 8000 else MED
        ax.plot([v], [0], 'o', ms=12, color=c, zorder=3); ax.text(v, 0.35 if k % 2 == 0 else -0.5, '%s\n%s' % (t, format(v, ',').replace(',', '.')), ha='center', fontsize=9.5, color=DARK)
    ax.axvline(8000, color=ROJO, ls='--', lw=1.5); ax.text(8050, 1.0, '8.000', color=ROJO, fontsize=9.5, fontweight='bold')
    ax.axvline(9000, color=AZUL, ls=':', lw=1.5); ax.text(9050, 1.0, '9.000', color=AZUL, fontsize=9.5, fontweight='bold')
    ax.text(200, 1.25, '∀x: «x cuesta menos de 8.000»  →  F (contraejemplos en rojo: gaseosa y mixta)', fontsize=10, color=ROJO, fontweight='bold')
    ax.text(200, -1.25, '∃x: «x cuesta más de 9.000»  →  V (alcanza con la mixta)', fontsize=10, color=AZUL, fontweight='bold')
    ax.set_ylim(-1.5, 1.5); ax.set_xlim(-300, 11300); ax.set_yticks([]); ax.set_xlabel('precio en guaraníes')
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    fin(fig, 'fig_n_cuantif.png')


def reglas():
    fig, ax = lienzo(12, 4.2, 12, 4.2)
    R = [('MPP', 'p → q\np', 'q'), ('MTT', 'p → q\n¬q', '¬p'), ('MTP', 'p ∨ q\n¬p', 'q'), ('Silogismo\nhipotético', 'p → q\nq → r', 'p → r'), ('Dilema\nconstructivo', 'p ∨ q\np → r\nq → s', 'r ∨ s')]
    for k, (n, pr, co) in enumerate(R):
        x = 0.2 + k * 2.38
        caja(ax, x, 3.3, 2.1, 0.75, n, fc=MED, ec=DARK, tc='white', fs=9.5)
        caja(ax, x, 1.6, 2.1, 1.45, pr, fc='white', ec=MED, tc=DARK, fs=10.5, bold=False)
        ax.plot([x + 0.2, x + 1.9], [1.45, 1.45], color=DARK, lw=2)
        caja(ax, x, 0.55, 2.1, 0.75, co, fc=AMBL, ec=AMB, tc='#5A4200', fs=11)
    ax.text(6.0, 0.1, 'premisas arriba · conclusión debajo de la raya', ha='center', fontsize=9.5, color=GRIS, style='italic')
    fin(fig, 'fig_n_reglas.png')


def expresion():
    fig, ax = lienzo(11.5, 5.4, 11.5, 5.4)
    def n(x, y, t, v, fc=LIGHT, ec=MED):
        x += 0.5
        caja(ax, x - 0.85, y - 0.3, 1.7, 0.6, t, fc=fc, ec=ec, fs=10, tc='white' if fc == MED else DARK)
        if v:
            ax.text(x, y - 0.55, v, ha='center', va='top', fontsize=9, color=AMB, fontweight='bold')
    n(5.5, 4.9, 'Y', 'V', fc=MED, ec=DARK)
    n(3.0, 3.7, '>', 'V'); n(8.0, 3.7, '<', 'V')
    n(1.8, 2.5, '+', '14000'); n(4.4, 2.5, '10000', None, fc='white'); n(7.1, 2.5, 'cantidad', '3', fc=AMBL, ec=AMB); n(9.0, 2.5, '5', None, fc='white')
    n(1.0, 1.3, '*', '12000'); n(2.9, 1.3, 'envio', '2000', fc=AMBL, ec=AMB)
    n(0.6, 0.1, 'precio', '4000', fc=AMBL, ec=AMB); n(2.3, 0.1, 'cantidad', '3', fc=AMBL, ec=AMB)
    for (x1, y1, x2, y2) in ((5.5, 4.6, 3.0, 4.0), (5.5, 4.6, 8.0, 4.0), (3.0, 3.4, 1.8, 2.8), (3.0, 3.4, 4.4, 2.8), (8.0, 3.4, 7.1, 2.8), (8.0, 3.4, 9.0, 2.8),
                             (1.8, 2.2, 1.0, 1.6), (1.8, 2.2, 2.9, 1.6), (1.0, 1.0, 0.6, 0.4), (1.0, 1.0, 2.3, 0.4)):
        linea(ax, [x1 + 0.5, x2 + 0.5], [y1, y2])
    ax.text(10.9, 4.9, 'se evalúa de abajo\nhacia arriba:\nhojas = datos,\nraíz = resultado', ha='right', va='top', fontsize=9.5, color=GRIS, style='italic')
    ax.set_ylim(-0.6, 5.4)
    fin(fig, 'fig_n_expresion.png')


def anidada():
    fig, ax = lienzo(10, 7.4, 10, 7.4)
    ovalo(ax, 3.2, 7.0, 1.8, 0.55, 'Inicio')
    romboide(ax, 3.2, 6.1, 2.6, 0.6, 'Leer total')
    rombo(ax, 3.2, 4.85, 3.0, 1.2, 'total >= 80000', fs=9)
    caja(ax, 5.6, 4.55, 3.2, 0.6, 'Escribir "mayorista"', fc='white', fs=9)
    rombo(ax, 3.2, 3.1, 3.0, 1.2, 'total >= 40000', fs=9)
    caja(ax, 5.6, 2.8, 3.2, 0.6, 'Escribir "frecuente"', fc='white', fs=9)
    caja(ax, 1.6, 1.55, 3.2, 0.6, 'Escribir "ocasional"', fc='white', fs=9)
    ovalo(ax, 3.2, 0.35, 1.8, 0.55, 'Fin')
    flecha(ax, 3.2, 6.72, 3.2, 6.42); flecha(ax, 3.2, 5.8, 3.2, 5.47)
    flecha(ax, 4.7, 4.85, 5.58, 4.85); ax.text(4.85, 5.0, 'V', color=MED, fontweight='bold')
    flecha(ax, 3.2, 4.25, 3.2, 3.72); ax.text(3.35, 3.9, 'F', color=ROJO, fontweight='bold')
    flecha(ax, 4.7, 3.1, 5.58, 3.1); ax.text(4.85, 3.25, 'V', color=MED, fontweight='bold')
    flecha(ax, 3.2, 2.5, 3.2, 2.17); ax.text(3.35, 2.3, 'F', color=ROJO, fontweight='bold')
    linea(ax, [3.2, 3.2], [1.55, 1.0]); linea(ax, [8.8, 9.3, 9.3], [4.85, 4.85, 1.0]); linea(ax, [8.8, 9.3], [3.1, 3.1]); linea(ax, [9.3, 3.2], [1.0, 1.0])
    flecha(ax, 3.2, 1.0, 3.2, 0.64)
    ax.text(0.1, 3.1, 'el segundo rombo\nsolo recibe compras\nmenores que 80000', fontsize=9, color=GRIS, style='italic', va='center')
    fin(fig, 'fig_n_anidada.png')


def pfi_caja():
    fig, ax = lienzo(9, 9.4, 9, 9.4)
    X = 3.0
    ovalo(ax, X, 9.0, 1.8, 0.55, 'Inicio')
    romboide(ax, X, 8.05, 2.8, 0.6, 'Leer precio')
    romboide(ax, X, 7.05, 2.8, 0.6, 'Leer cantidad')
    caja(ax, X - 1.75, 5.75, 3.5, 0.65, 'total ← precio * cantidad', fc='white', fs=9.5)
    rombo(ax, X, 4.45, 3.2, 1.25, 'total >= 50000', fs=9.5)
    caja(ax, 5.15, 4.13, 3.6, 0.65, 'cobrar ← total − total * 10 / 100', fc='white', fs=8.6)
    caja(ax, X - 1.75, 2.75, 3.5, 0.65, 'cobrar ← total', fc='white', fs=9.5)
    romboide(ax, X, 1.55, 2.8, 0.6, 'Escribir cobrar')
    ovalo(ax, X, 0.4, 1.8, 0.55, 'Fin')
    flecha(ax, X, 8.72, X, 8.36); flecha(ax, X, 7.74, X, 7.36); flecha(ax, X, 6.74, X, 6.42); flecha(ax, X, 5.74, X, 5.09)
    flecha(ax, X + 1.6, 4.45, 5.13, 4.45); ax.text(4.75, 4.6, 'V', color=MED, fontweight='bold')
    flecha(ax, X, 3.82, X, 3.42); ax.text(X + 0.15, 3.55, 'F', color=ROJO, fontweight='bold')
    linea(ax, [6.95, 6.95], [4.12, 2.2]); linea(ax, [6.95, X], [2.2, 2.2]); linea(ax, [X, X], [2.74, 2.2])
    flecha(ax, X, 2.2, X, 1.86); flecha(ax, X, 1.24, X, 0.69)
    ax.text(5.15, 5.25, 'frontera: 50000 >= 50000 es V,\nla venta de exactamente 50000 recibe descuento', fontsize=8.6, color=GRIS, style='italic', va='center')
    fin(fig, 'fig_pfi_caja1.png')


if __name__ == '__main__':
    for f in (pertenencia, inclusion, union_inter, clasif_prop, condicional, arbol8, demorgan, cuantif, reglas, expresion, anidada, pfi_caja):
        f()
    print(sorted(os.listdir(OUT)))
