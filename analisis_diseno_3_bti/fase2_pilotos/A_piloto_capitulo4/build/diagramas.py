# -*- coding: utf-8 -*-
"""Figuras originales del Capítulo 4 (generadas por código; sin recursos de terceros)."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans'})
DARK, MED, SOFT, LIGHT = '#1B5E20', '#2E7D32', '#43A047', '#E8F5E9'
AMBAR, GRIS = '#B8860B', '#616161'
AQUI = os.path.dirname(os.path.abspath(__file__))

# Posiciones del mapa de interesados (interés, influencia), en escala 0 a 10.
# Las mismas cifras se usan en la tabla del Ejemplo resuelto 1.
INTERESADOS = [
    ('Bibliotecaria', 9, 8),
    ('Directora', 4, 9),
    ('Encargado de\ninformática', 2.5, 6.5),
    ('Docentes', 6.5, 3.6),
    ('Estudiantes', 8.5, 2.2),
    ('Familias', 2.5, 1.5),
]


def mapa_interesados(ruta):
    fig, ax = plt.subplots(figsize=(7.2, 6.0))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    cuad = [((0, 5), 'Mantener satisfecho'), ((5, 5), 'Gestionar de cerca'),
            ((0, 0), 'Observar'), ((5, 0), 'Mantener informado')]
    for (x, y), t in cuad:
        fill = LIGHT if t == 'Gestionar de cerca' else '#F7F7F7'
        ax.add_patch(plt.Rectangle((x, y), 5, 5, facecolor=fill, edgecolor='#BDBDBD', lw=1))
        ax.text(x + 2.5, y + 4.6, t, ha='center', va='top', fontsize=10.5, color=GRIS, style='italic')
    for nombre, interes, influencia in INTERESADOS:
        ax.plot(interes, influencia, 'o', ms=11, color=MED, mec='white', mew=1.5, zorder=3)
        ax.text(interes, influencia - 0.45, nombre, ha='center', va='top', fontsize=9.5, color=DARK, zorder=4)
    ax.set_xlabel('Interés en el sistema  →', fontsize=11)
    ax.set_ylabel('Influencia sobre las decisiones  →', fontsize=11)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color('#9E9E9E')
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)


PASOS = [
    ('1. Preparar', 'objetivo, interesados\ny guion'),
    ('2. Obtener', 'entrevista, observación,\ncuestionario…'),
    ('3. Registrar', 'notas con número\nde línea y fecha'),
    ('4. Analizar', 'hallazgos y requisitos\ncandidatos con su fuente'),
    ('5. Confirmar', 'devolución al\ninteresado'),
]


def flujo_elicitacion(ruta):
    fig, ax = plt.subplots(figsize=(11.5, 3.4))
    ax.set_xlim(0, 11.5); ax.set_ylim(0, 3.4); ax.axis('off')
    w, h, y = 2.0, 1.45, 1.45
    xs = [0.15 + i * 2.3 for i in range(len(PASOS))]
    for x, (tit, sub) in zip(xs, PASOS):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03,rounding_size=0.12',
                                    facecolor=LIGHT, edgecolor=MED, lw=1.6))
        ax.text(x + w / 2, y + h - 0.3, tit, ha='center', va='center', fontsize=11, weight='bold', color=DARK)
        ax.text(x + w / 2, y + 0.5, sub, ha='center', va='center', fontsize=8.4, color='#333333')
    for a, b in zip(xs[:-1], xs[1:]):
        ax.add_patch(FancyArrowPatch((a + w + 0.02, y + h / 2), (b - 0.02, y + h / 2),
                                     arrowstyle='-|>', mutation_scale=14, color=MED, lw=1.6))
    # Retorno: si la confirmación encuentra errores, se vuelve a obtener información.
    ax.add_patch(FancyArrowPatch((xs[4] + w / 2, y - 0.03), (xs[1] + w / 2, y - 0.03),
                                 connectionstyle='arc3,rad=-0.18', arrowstyle='-|>',
                                 mutation_scale=14, color=AMBAR, lw=1.4, ls='--'))
    ax.text((xs[1] + xs[4] + w) / 2, 0.5, 'si el interesado corrige o agrega algo, se vuelve a obtener información',
            ha='center', va='center', fontsize=8.8, color=AMBAR, style='italic')
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)


def generar():
    d = os.path.join(AQUI, 'figs')
    os.makedirs(d, exist_ok=True)
    r1 = os.path.join(d, 'fig_4_1_mapa_interesados.png')
    r2 = os.path.join(d, 'fig_4_2_flujo_elicitacion.png')
    mapa_interesados(r1)
    flujo_elicitacion(r2)
    return r1, r2


if __name__ == '__main__':
    print(generar())
