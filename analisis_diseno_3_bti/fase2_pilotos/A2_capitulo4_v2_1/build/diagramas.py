# -*- coding: utf-8 -*-
"""Figuras originales del Capítulo 4 v2 (generadas por código; sin recursos de terceros)."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({'font.family': 'DejaVu Sans'})
DARK, MED, SOFT, LIGHT = '#1B5E20', '#2E7D32', '#43A047', '#E8F5E9'
AMBAR, GRIS = '#B8860B', '#616161'
AQUI = os.path.dirname(os.path.abspath(__file__))

# Cadena de trazabilidad del ejemplo del informe de Work (§7.3), con las fuentes del capítulo.
CADENA = [
    ('Necesidad\nN-02', 'Evitar entregar a dos\nlectores el mismo\nejemplar (E4-L4)'),
    ('Regla\nRN-01', 'Un ejemplar solo puede\ntener un préstamo\nactivo'),
    ('Requisito\nRF-04', 'Rechazar el préstamo\nde un ejemplar que ya\nestá prestado'),
    ('Aceptación\nCA-04', 'Dado… cuando…\nentonces se rechaza y\nqueda un solo préstamo'),
    ('Prueba\nP-07', 'Segunda solicitud sobre\nel mismo ejemplar:\nrechazo comprobado'),
]


def _caja(ax, x, y, w, h, titulo, texto, borde=MED, fondo=LIGHT):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03,rounding_size=0.12',
                                facecolor=fondo, edgecolor=borde, lw=1.6))
    ax.text(x + w / 2, y + h - (0.38 if texto else h / 2), titulo, ha='center', va='center', fontsize=10, weight='bold', color=DARK)
    ax.text(x + w / 2, y + 0.62, texto, ha='center', va='center', fontsize=8.2, color='#333333')


def cadena_trazabilidad(ruta):
    fig, ax = plt.subplots(figsize=(11.5, 3.2))
    ax.set_xlim(0, 11.5); ax.set_ylim(0, 2.5); ax.axis('off')
    w, h, y = 2.0, 1.75, 0.6
    xs = [0.15 + i * 2.3 for i in range(len(CADENA))]
    for x, (t, s) in zip(xs, CADENA):
        _caja(ax, x, y, w, h, t, s)
    for a, b in zip(xs[:-1], xs[1:]):
        ax.add_patch(FancyArrowPatch((a + w + 0.02, y + h / 2), (b - 0.02, y + h / 2),
                                     arrowstyle='-|>', mutation_scale=14, color=MED, lw=1.6))
    ax.text(5.75, 0.18, 'Capítulo 4: N, RN, RF y criterio de aceptación  ·  Capítulos 14 a 16: la prueba',
            ha='center', va='center', fontsize=8.6, color=GRIS, style='italic')
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)


TIPOS = [
    ('Funcionales', 'Qué hace el sistema', 'RF-04: rechazar el préstamo\nde un ejemplar ya prestado'),
    ('De calidad', 'Qué tan bien lo hace', 'RNF-01: la bibliotecaria lo usa\nsin ayuda tras una práctica'),
    ('Restricciones', 'Qué condiciones limitan\nla solución', 'RS-01: funciona sin internet\nen la computadora de la biblioteca'),
]


def tipos_requisito(ruta):
    fig, ax = plt.subplots(figsize=(10.5, 4.6))
    ax.set_xlim(0, 10.5); ax.set_ylim(0, 4.6); ax.axis('off')
    _caja(ax, 3.55, 3.35, 3.4, 0.75, 'Requisitos', '', borde=DARK)
    xs = [0.15, 3.6, 7.05]
    for x, (t, q, e) in zip(xs, TIPOS):
        ax.add_patch(FancyArrowPatch((5.25, 3.33), (x + 1.65, 2.62), arrowstyle='-|>', mutation_scale=13, color=MED, lw=1.4))
        ax.add_patch(FancyBboxPatch((x, 0.75), 3.3, 1.85, boxstyle='round,pad=0.03,rounding_size=0.12',
                                    facecolor=LIGHT, edgecolor=MED, lw=1.5))
        ax.text(x + 1.65, 2.3, t, ha='center', va='center', fontsize=11, weight='bold', color=DARK)
        ax.text(x + 1.65, 1.82, q, ha='center', va='center', fontsize=8.8, color=GRIS, style='italic')
        ax.text(x + 1.65, 1.15, e, ha='center', va='center', fontsize=8.4, color='#333333')
    ax.text(5.25, 0.25, 'Las reglas de negocio (RN) son de la organización: existen aunque no haya sistema; '
            'los requisitos dicen cómo el sistema las hace cumplir.', ha='center', va='center', fontsize=8.6, color=AMBAR, style='italic')
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)


def generar():
    d = os.path.join(AQUI, 'figs')
    os.makedirs(d, exist_ok=True)
    r1 = os.path.join(d, 'fig_4_1_tipos_de_requisito.png')
    r2 = os.path.join(d, 'fig_4_2_cadena_de_trazabilidad.png')
    tipos_requisito(r1)
    cadena_trazabilidad(r2)
    return r1, r2


if __name__ == '__main__':
    print(generar())
