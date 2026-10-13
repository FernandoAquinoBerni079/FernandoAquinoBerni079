# -*- coding: utf-8 -*-
"""Figuras de elaboración editorial (matplotlib, 200 ppp, PNG sin pérdida), con la paleta violeta de la serie.
1) Redibujos de figuras de la edición anterior con texto desbordado o cortado (los originales de figs/originales no se tocan).
2) Figuras nuevas de los talleres del Proyecto Educativo Comunitario.
Cada texto se ajusta a su caja: si no entra, se reduce el cuerpo hasta que entre (control al final)."""
import os, textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Wedge

OUT = os.path.dirname(os.path.abspath(__file__)) + '/../figs/nuevas/'
os.makedirs(OUT, exist_ok=True)
DARK, MED, SOFT, PALE, AMB, GRIS = '#6A3E7A', '#8E5BA6', '#B79BCF', '#F3ECF7', '#B8860B', '#5F5F5F'
plt.rcParams['font.family'] = 'DejaVu Sans'
DESBORDES = []


def lienzo(w, h):
    fig = plt.figure(figsize=(w, h), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, w * 100); ax.set_ylim(0, h * 100); ax.axis('off')
    return fig, ax


def titulo(ax, fig, txt, y=None, size=17):
    w = ax.get_xlim()[1]
    ax.text(w / 2, y or ax.get_ylim()[1] - 30, txt, ha='center', va='center', fontsize=size, color=DARK, fontweight='bold')


def ajustar(fig, ax, t, x0, y0, x1, y1, pad=8):
    """Reduce la fuente hasta que el texto quede dentro del rectángulo (en unidades de datos)."""
    r = fig.canvas.get_renderer()
    for _ in range(40):
        bb = t.get_window_extent(r).transformed(ax.transData.inverted())
        if bb.x0 >= x0 + pad and bb.x1 <= x1 - pad and bb.y0 >= y0 + pad and bb.y1 <= y1 - pad:
            return
        t.set_fontsize(t.get_fontsize() - 0.5)
    DESBORDES.append(t.get_text())


def caja(fig, ax, x, y, w, h, txt, fill=MED, color='white', size=13, bold=True, ancho=None, r=10):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=%d' % r, fc=fill, ec=DARK, lw=2, zorder=2))
    if ancho:
        txt = '\n'.join(textwrap.fill(p, ancho, break_long_words=False) for p in txt.split('\n'))
    t = ax.text(x + w / 2, y + h / 2, txt, ha='center', va='center', fontsize=size, color=color,
                fontweight='bold' if bold else 'normal', linespacing=1.25, zorder=3)
    ajustar(fig, ax, t, x, y, x + w, y + h)
    return t


def texto(fig, ax, x, y, w, h, txt, size=11, color='#222222', ancho=None, bold=False):
    if ancho:
        txt = '\n'.join(textwrap.fill(p, ancho, break_long_words=False) for p in txt.split('\n'))
    t = ax.text(x + w / 2, y + h / 2, txt, ha='center', va='center', fontsize=size, color=color, linespacing=1.3,
                fontweight='bold' if bold else 'normal')
    ajustar(fig, ax, t, x, y, x + w, y + h, pad=2)


def flecha(ax, x0, y0, x1, y1, color=GRIS, lw=3, z=1):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle='-|>', mutation_scale=22, color=color, lw=lw, zorder=z))


def guardar(fig, nombre):
    fig.savefig(OUT + nombre, dpi=200, facecolor='white')
    plt.close(fig)


# ---------------- redibujos de la edición anterior ----------------

def fig_norma():  # image3
    fig, ax = lienzo(12, 4.6); titulo(ax, fig, 'Una buena norma de convivencia se construye entre todos', 420)
    pasos = [('Dialogamos y nos escuchamos', SOFT, 'black'), ('Buscamos el acuerdo', MED, 'white'),
             ('Escribimos la norma', DARK, 'white'), ('La cumplimos entre todos', AMB, 'white')]
    for i, (t, f, c) in enumerate(pasos):
        x = 40 + i * 292
        caja(fig, ax, x, 110, 240, 210, t, f, c, 17, ancho=12)
        if i < 3:
            flecha(ax, x + 245, 215, x + 287, 215)
    guardar(fig, 'fig_norma.png')


def fig_escalera():  # image5
    fig, ax = lienzo(10.5, 8.2); titulo(ax, fig, 'La escalera de la autoestima', 790)
    ax.text(60, 715, 'Cada peldaño\nsostiene al siguiente', fontsize=12, color=GRIS, style='italic', va='top')
    pel = [('Me conozco', SOFT, 'black'), ('Me acepto', SOFT, 'black'), ('Me valoro', MED, 'white'),
           ('Me cuido', MED, 'white'), ('Me respeto y respeto a los demás', DARK, 'white')]
    for i, (t, f, c) in enumerate(pel):
        x, y = 30 + i * 170, 40 + i * 125
        caja(fig, ax, x, y, 230 if i < 4 else 330, 85, t, f, c, 15, ancho=20 if i == 4 else 14)
    flecha(ax, 30, 20, 1010, 690, AMB, 2.5, z=0)
    guardar(fig, 'fig_escalera.png')


def fig_derechos():  # image10
    fig, ax = lienzo(11, 6.4); titulo(ax, fig, 'Cada derecho viene con una responsabilidad', 610)
    caja(fig, ax, 60, 470, 400, 80, 'TENGO DERECHO A…', MED, 'white', 16)
    caja(fig, ax, 640, 470, 400, 80, 'Y TENGO LA RESPONSABILIDAD DE…', AMB, 'white', 16, ancho=24)
    pares = [('estudiar y aprender', 'esforzarme y asistir'), ('ser respetado', 'respetar a los demás'),
             ('expresar mi opinión', 'escuchar la del otro'), ('jugar y descansar', 'cumplir mis tareas')]
    for i, (a, b) in enumerate(pares):
        y = 360 - i * 105
        caja(fig, ax, 60, y, 400, 80, a, PALE, 'black', 15, bold=False)
        caja(fig, ax, 640, y, 400, 80, b, '#FDF3DD', 'black', 15, bold=False)
        flecha(ax, 470, y + 40, 630, y + 40, DARK)
    guardar(fig, 'fig_derechos.png')


def fig_participacion():  # image14
    fig, ax = lienzo(12, 5.2); titulo(ax, fig, 'Participación estudiantil: un ejemplo posible', 485)
    ax.text(600, 435, 'La organización concreta depende del reglamento o mecanismo vigente en cada institución.',
            ha='center', fontsize=11.5, color=DARK, fontweight='bold')
    pasos = [('El grado elige o designa representantes según sus normas', SOFT, 'black'),
             ('Los representantes se reúnen en el mecanismo vigente', MED, 'white'),
             ('Presentan propuestas y deliberan', DARK, 'white'),
             ('Comunican los acuerdos y cumplen responsabilidades', AMB, 'white')]
    for i, (t, f, c) in enumerate(pasos):
        x = 30 + i * 295
        caja(fig, ax, x, 150, 250, 220, t, f, c, 14.5, ancho=16)
        if i < 3:
            flecha(ax, x + 254, 260, x + 290, 260)
    ax.text(600, 80, 'Puede llamarse Parlamento Escolar, centro de estudiantes, consejo de delegados u otro mecanismo equivalente.',
            ha='center', fontsize=11.5, color='#222222')
    guardar(fig, 'fig_participacion.png')


def fig_semana():  # image17, según el pedido del redactor de la Clase 17 (sin «Colegio» el fin de semana)
    fig, ax = lienzo(12, 6.6); titulo(ax, fig, 'Una semana organizada tiene lugar para todo', 630)
    dias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
    for j, dname in enumerate(dias):
        x = 70 + j * 152
        ax.text(x + 66, 570, dname, ha='center', va='center', fontsize=15, color=DARK, fontweight='bold')
        if j < 5:
            caja(fig, ax, x, 390, 132, 150, 'Colegio', MED, 'white', 13, r=6)
            caja(fig, ax, x, 290, 132, 85, 'Estudio', DARK, 'white', 13, r=6)
        else:
            caja(fig, ax, x, 390, 132, 150, 'Familia / tiempo libre', PALE, 'black', 12.5, ancho=10, r=6)
            ax.add_patch(FancyBboxPatch((x, 290), 132, 85, boxstyle='round,pad=0,rounding_size=6', fc='white', ec=DARK, lw=2, ls='--', zorder=2))
            texto(fig, ax, x, 290, 132, 85, 'Repaso corto (si hay prueba)', 11, ancho=12)
        caja(fig, ax, x, 140, 132, 135, 'Descanso / deporte', SOFT, 'black', 12.5, ancho=10, r=6)
    ax.text(600, 85, 'El bloque de estudio es corto y diario: así se forma el hábito.', ha='center', fontsize=12, color=GRIS, style='italic')
    guardar(fig, 'nueva_semana_organizada.png')


def fig_metas():  # image18
    fig, ax = lienzo(11, 7.6); titulo(ax, fig, 'De las metas pequeñas al gran sueño', 730)
    m = [('Corto plazo, esta semana:\ntermino mis tareas', SOFT, 'black'), ('Mediano plazo, este año:\napruebo con esfuerzo', MED, 'white'),
         ('Largo plazo, mi sueño:\nquién quiero ser', DARK, 'white')]
    for i, (t, f, c) in enumerate(m):
        caja(fig, ax, 60 + i * 340, 70 + i * 200, 330, 150, t, f, c, 15, ancho=22)
    flecha(ax, 30, 40, 1080, 660, AMB, 2.5, z=0)
    guardar(fig, 'fig_metas.png')


def fig_red_proyecto():  # image21
    fig, ax = lienzo(9, 8.4); titulo(ax, fig, 'Cierro el año con mi red y mi proyecto de vida', 810, 16)
    import math
    cx, cy = 450, 390
    nodos = [('Familia', MED), ('Adultos de confianza', MED), ('Colegio', MED), ('Comunidad', SOFT), ('Amistades', SOFT), ('Fono Ayuda 147 y CODENI', DARK)]
    for k, (t, f) in enumerate(nodos):
        a = math.pi / 2 - 2 * math.pi * k / len(nodos)
        x, y = cx + 290 * math.cos(a), cy + 280 * math.sin(a)
        ax.plot([cx, x], [cy, y], color=SOFT, lw=3, zorder=1)
        ax.add_patch(Circle((x, y), 92, fc=f, ec=DARK, lw=2, zorder=2))
        t_ = ax.text(x, y, textwrap.fill(t, 11), ha='center', va='center', fontsize=13, color='white' if f != SOFT else 'black', fontweight='bold', zorder=3)
        ajustar(fig, ax, t_, x - 80, y - 66, x + 80, y + 66, pad=0)
    ax.add_patch(Circle((cx, cy), 120, fc=AMB, ec=DARK, lw=2, zorder=2))
    t_ = ax.text(cx, cy, 'YO\ny mi proyecto\nde vida', ha='center', va='center', fontsize=15, color='white', fontweight='bold', zorder=3)
    ajustar(fig, ax, t_, cx - 95, cy - 85, cx + 95, cy + 85, pad=0)
    guardar(fig, 'fig_red_proyecto.png')


def fig_sentir_pensar_actuar():  # Clase 6 (pedido del redactor)
    import math
    fig, ax = lienzo(10, 8.4); titulo(ax, fig, 'Sentir, pensar y actuar: un ciclo con una pausa para decidir', 810, 15.5)
    cx, cy, R = 500, 390, 235
    nodos = [('SENTIR', '¿Qué estoy sintiendo?', 90, SOFT, 'black'),
             ('PENSAR', '¿Qué estoy pensando? ¿Es un hecho o una opinión?', -30, MED, 'white'),
             ('ACTUAR', '¿Qué quiero hacer y qué va a pasar si lo hago?', 210, DARK, 'white')]
    from matplotlib.patches import Arc
    ax.add_patch(Arc((cx, cy), 2 * R, 2 * R, theta1=0, theta2=360, color=GRIS, lw=3, zorder=0))
    for ang in (30, -90, 150):  # puntas de flecha en sentido horario
        a = math.radians(ang); x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        tx, ty = math.sin(a), -math.cos(a)
        flecha(ax, x - tx * 14, y - ty * 14, x + tx * 14, y + ty * 14, GRIS, 3)
    pos = {}
    for t, q, ang, f, c in nodos:
        a = math.radians(ang); x, y = cx + R * math.cos(a), cy + R * math.sin(a); pos[t] = (x, y)
        ax.add_patch(Circle((x, y), 92, fc=f, ec=DARK, lw=2, zorder=2))
        t_ = ax.text(x, y, t, ha='center', va='center', fontsize=17, color=c, fontweight='bold', zorder=3)
        ajustar(fig, ax, t_, x - 85, y - 40, x + 85, y + 40, pad=0)
        yy = y - 155 if ang != 90 else y + 115
        texto(fig, ax, x - 170, yy - 40, 340, 80, q, 12.5, ancho=26)
    # recuadro PAUSA sobre el tramo SENTIR → PENSAR → ACTUAR (lado derecho, junto a PENSAR)
    a = math.radians(30); x, y = cx + R * math.cos(a), cy + R * math.sin(a)
    caja(fig, ax, x + 25, y + 20, 150, 62, 'PAUSA', AMB, 'white', 17)
    guardar(fig, 'nueva_sentir_pensar_actuar.png')


# ---------------- figuras de los talleres del Proyecto Educativo Comunitario ----------------

def pec_ciclo():
    fig, ax = lienzo(11, 10.4); titulo(ax, fig, 'El ciclo del Proyecto Educativo Comunitario', 1005)
    import math
    et = [('1. Comprender e identificar necesidades', 'Junio'), ('2. Diagnosticar y priorizar', 'Agosto'),
          ('3. Elegir, fundamentar y fijar objetivos', 'Agosto'), ('4. Planificar y organizarse', 'Septiembre'),
          ('5. Ejecutar y hacer el seguimiento', 'Octubre'), ('6. Evaluar los resultados', 'Noviembre'),
          ('7. Socializar lo aprendido', 'Noviembre')]
    cx, cy, R = 550, 480, 365
    cols = [SOFT, SOFT, MED, MED, DARK, DARK, AMB]
    from matplotlib.patches import Arc
    ax.add_patch(Arc((cx, cy), 2 * R, 2 * R, theta1=90 - 360 * 6 / 7, theta2=90, color=GRIS, lw=3, zorder=1))
    for k in range(6):  # puntas de flecha en el sentido de avance, a mitad de camino entre etapas
        a = math.pi / 2 - 2 * math.pi * (k + 0.5) / 7
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        tx, ty = math.sin(a), -math.cos(a)
        flecha(ax, x - tx * 12, y - ty * 12, x + tx * 12, y + ty * 12, GRIS, 3)
    for k, ((t, mes), f) in enumerate(zip(et, cols)):
        a = math.pi / 2 - 2 * math.pi * k / 7
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        c = 'black' if f == SOFT else 'white'
        caja(fig, ax, x - 135, y - 72, 270, 144, t + '\n(' + mes + ')', f, c, 14, ancho=17)
    ax.add_patch(Circle((cx, cy), 120, fc=PALE, ec=DARK, lw=2))
    t_ = ax.text(cx, cy, 'Nuestra\nescuela como\ncomunidad', ha='center', va='center', fontsize=15, color=DARK, fontweight='bold')
    ajustar(fig, ax, t_, cx - 95, cy - 85, cx + 95, cy + 85, pad=0)
    guardar(fig, 'nueva_pec_ciclo.png')


if __name__ == '__main__':
    import sys
    for f in [fig_sentir_pensar_actuar, fig_norma, fig_escalera, fig_derechos, fig_participacion, fig_semana, fig_metas, fig_red_proyecto, pec_ciclo]:
        f()
    import pec_figuras
    pec_figuras.todas(sys.modules[__name__])
    print('desbordes', DESBORDES)
    assert not DESBORDES
