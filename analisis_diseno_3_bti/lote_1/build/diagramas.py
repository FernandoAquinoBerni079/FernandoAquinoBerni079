# -*- coding: utf-8 -*-
"""Figuras originales del lote 1 (generadas por código con matplotlib; sin recursos de terceros).
Los datos de cada figura se leen de los módulos del caso o del capítulo, para que figura y texto coincidan.
Figura 1.2 y Figura 2.1: adaptadas del candidato del Capítulo 2 (Figuras 4.1 y 4.2 de ese candidato)."""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'caso'))
import dossier as D

plt.rcParams.update({'font.family': 'DejaVu Sans'})
DARK, MED, SOFT, LIGHT = '#1B5E20', '#2E7D32', '#43A047', '#E8F5E9'
AMBAR, GRIS = '#B8860B', '#616161'


def _caja(ax, x, y, w, h, titulo, texto='', borde=MED, fondo=LIGHT, ft=10, fx=8.4):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03,rounding_size=0.12',
                                facecolor=fondo, edgecolor=borde, lw=1.5))
    if texto:
        ax.text(x + w / 2, y + h - 0.3, titulo, ha='center', va='center', fontsize=ft, weight='bold', color=DARK)
        ax.text(x + w / 2, y + (h - 0.45) / 2, texto, ha='center', va='center', fontsize=fx, color='#333333')
    else:
        ax.text(x + w / 2, y + h / 2, titulo, ha='center', va='center', fontsize=ft, weight='bold', color=DARK)


def _flecha(ax, a, b, color=MED, ls='-', rad=0.0):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=13, color=color, lw=1.4, ls=ls,
                                 connectionstyle='arc3,rad=%s' % rad))


# ---------------------------------------------------------------- Figura 1.1
def sistema_prestamos(ruta):
    fig, ax = plt.subplots(figsize=(10.5, 6.4))
    ax.set_xlim(0, 10.5); ax.set_ylim(0, 6.4); ax.axis('off')
    # límite del sistema
    ax.add_patch(FancyBboxPatch((1.9, 0.75), 6.7, 4.95, boxstyle='round,pad=0.02,rounding_size=0.3',
                                facecolor='none', edgecolor=GRIS, lw=1.4, ls='--'))
    ax.text(8.5, 5.55, 'Límite del sistema', ha='right', va='center', fontsize=8.6, color=GRIS, style='italic')
    _caja(ax, 3.7, 2.45, 3.1, 1.6, 'Procesos', 'prestar · devolver\nbuscar un libro\npreparar el informe')
    _caja(ax, 2.2, 4.3, 2.6, 1.15, 'Personas', 'bibliotecaria · lectores\ndirección')
    _caja(ax, 5.7, 4.3, 2.6, 1.15, 'Datos', 'quién llevó qué y cuándo\nqué hay disponible')
    _caja(ax, 2.2, 1.0, 2.6, 1.15, 'Recursos', 'cuaderno · estantes\ntiempo de atención')
    _caja(ax, 5.7, 1.0, 2.6, 1.15, 'Salidas', 'informe mensual\npor curso')
    for a, b in (((3.5, 4.3), (4.3, 4.05)), ((7.0, 4.3), (6.2, 4.05)), ((3.5, 2.15), (4.3, 2.45)), ((6.2, 2.45), (7.0, 2.15))):
        _flecha(ax, a, b)
    # entorno
    _caja(ax, 0.05, 2.6, 1.6, 1.3, 'Entorno', 'inscripción de\nestudiantes', borde=GRIS, fondo='#F5F5F5', ft=9, fx=8)
    _caja(ax, 8.85, 2.6, 1.6, 1.3, 'Entorno', 'compra de\nlibros', borde=GRIS, fondo='#F5F5F5', ft=9, fx=8)
    ax.text(2.65, 3.45, 'entra: quiénes\nson lectores', ha='center', va='bottom', fontsize=7.6, color=GRIS)
    ax.text(9.3, 1.85, 'sale: títulos\nmás pedidos', ha='center', va='center', fontsize=7.6, color=GRIS)
    _flecha(ax, (1.65, 3.25), (3.68, 3.25), color=GRIS, ls='--')
    _flecha(ax, (8.3, 1.55), (9.6, 2.58), color=GRIS, ls='--')
    ax.text(5.25, 0.3, 'En esta etapa, «datos» es la información que usa o produce cada persona; las tablas se diseñan en la Unidad III.',
            ha='center', va='center', fontsize=8.4, color=AMBAR, style='italic')
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white'); plt.close(fig)


# ---------------------------------------------------------------- Figura 1.2 (del candidato, datos del caso)
def mapa_interesados(ruta):
    fig, ax = plt.subplots(figsize=(7.2, 6.0))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    cuad = [((0, 5), 'Mantener satisfecho'), ((5, 5), 'Gestionar de cerca'),
            ((0, 0), 'Observar'), ((5, 0), 'Mantener informado')]
    for (x, y), t in cuad:
        fill = LIGHT if t == 'Gestionar de cerca' else '#F7F7F7'
        ax.add_patch(Rectangle((x, y), 5, 5, facecolor=fill, edgecolor='#BDBDBD', lw=1))
        ax.text(x + 2.5, y + 4.6, t, ha='center', va='top', fontsize=10.5, color=GRIS, style='italic')
    for nombre, interes, influencia, _, _ in D.INTERESADOS:
        ax.plot(interes, influencia, 'o', ms=11, color=MED, mec='white', mew=1.5, zorder=3)
        ax.text(interes, influencia - 0.45, nombre.replace('Encargado de informática', 'Encargado de\ninformática'),
                ha='center', va='top', fontsize=9.5, color=DARK, zorder=4)
    ax.set_xlabel('Interés en el sistema  →', fontsize=11)
    ax.set_ylabel('Influencia sobre las decisiones  →', fontsize=11)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color('#9E9E9E')
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white'); plt.close(fig)


# ---------------------------------------------------------------- Figura 2.1 (del candidato, sin requisitos)
PASOS = [
    ('1. Preparar', 'objetivo, interesados,\nguion y autorización'),
    ('2. Obtener', 'entrevista, observación,\ndocumentos…'),
    ('3. Registrar', 'notas con número\nde línea y contexto'),
    ('4. Analizar', 'hallazgos y necesidades\ncon su fuente'),
    ('5. Confirmar', 'devolución al\ninteresado'),
]


def flujo_relevamiento(ruta):
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
        _flecha(ax, (a + w + 0.02, y + h / 2), (b - 0.02, y + h / 2))
    ax.add_patch(FancyArrowPatch((xs[4] + w / 2, y - 0.03), (xs[1] + w / 2, y - 0.03),
                                 connectionstyle='arc3,rad=-0.18', arrowstyle='-|>',
                                 mutation_scale=14, color=AMBAR, lw=1.4, ls='--'))
    ax.text((xs[1] + xs[4] + w) / 2, 0.5, 'si el interesado corrige o agrega algo, se vuelve a obtener información',
            ha='center', va='center', fontsize=8.8, color=AMBAR, style='italic')
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white'); plt.close(fig)


# ---------------------------------------------------------------- Figura 2.2 (contraste de fuentes)
CONTRASTE = [
    ('Lo que se dice', 'E1-L2', '«anoto apurada y después\nno entiendo mi letra»'),
    ('Lo que se ve', 'O1-1, O1-2', '14 en fila; 9 préstamos\nen un recreo'),
    ('Lo que se cuenta después', 'E4-L4', 'anotó el mismo libro\na dos chicos distintos'),
]


def contraste_fuentes(ruta):
    fig, ax = plt.subplots(figsize=(10.5, 4.4))
    ax.set_xlim(0, 10.5); ax.set_ylim(0, 4.4); ax.axis('off')
    xs = [0.2, 3.65, 7.1]
    for x, (tipo, cod, txt) in zip(xs, CONTRASTE):
        _caja(ax, x, 2.55, 3.2, 1.65, '%s  (%s)' % (tipo, cod), txt, ft=9.4, fx=8.6)
        _flecha(ax, (x + 1.6, 2.53), (5.25, 1.42))
    _caja(ax, 2.5, 0.35, 5.5, 1.05, 'Hallazgo: en hora pico el registro falla',
          'necesidades N-04 (registrar sin errores) y N-02 (no prestar dos veces)', borde=DARK, ft=9.8, fx=8.6)
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white'); plt.close(fig)


# ---------------------------------------------------------------- Figura 3.1 (mapa de riesgos, cualitativo)
def mapa_riesgos(ruta, riesgos):
    """riesgos: [(cod, prob, impacto)] con valores 'Baja/Media/Alta' y 'Bajo/Medio/Alto'."""
    niv_p = {'Baja': 0, 'Media': 1, 'Alta': 2}
    niv_i = {'Bajo': 0, 'Medio': 1, 'Alto': 2}
    fig, ax = plt.subplots(figsize=(7.4, 5.6))
    ax.set_xlim(0, 3); ax.set_ylim(0, 3)
    for i in range(3):
        for j in range(3):
            tono = ['#F7F7F7', '#FFF8E1', '#FDECEA'][min(2, (i + j + 1) // 2)]
            ax.add_patch(Rectangle((i, j), 1, 1, facecolor=tono, edgecolor='#BDBDBD', lw=1))
    celdas = {}
    for cod, p, imp in riesgos:
        celdas.setdefault((niv_p[p], niv_i[imp]), []).append(cod)
    for (i, j), cods in celdas.items():
        for k, c in enumerate(cods):
            fila, col = divmod(k, 2)
            x = i + 0.3 + col * 0.42
            yy = j + 0.68 - fila * 0.3
            ax.text(x, yy, c, ha='center', va='center', fontsize=10, weight='bold', color=DARK,
                    bbox=dict(boxstyle='round,pad=0.25', facecolor='white', edgecolor=MED, lw=1.2))
    ax.set_xticks([0.5, 1.5, 2.5]); ax.set_xticklabels(['Baja', 'Media', 'Alta'], fontsize=10)
    ax.set_yticks([0.5, 1.5, 2.5]); ax.set_yticklabels(['Bajo', 'Medio', 'Alto'], fontsize=10)
    ax.set_xlabel('Probabilidad  →', fontsize=11); ax.set_ylabel('Impacto  →', fontsize=11)
    ax.tick_params(length=0)
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white'); plt.close(fig)


def generar(riesgos):
    d = os.path.join(AQUI, 'figs')
    os.makedirs(d, exist_ok=True)
    rutas = {
        'fig_1_1': os.path.join(d, 'fig_1_1_sistema_prestamos.png'),
        'fig_1_2': os.path.join(d, 'fig_1_2_mapa_interesados.png'),
        'fig_2_1': os.path.join(d, 'fig_2_1_proceso_relevamiento.png'),
        'fig_2_2': os.path.join(d, 'fig_2_2_contraste_fuentes.png'),
        'fig_3_1': os.path.join(d, 'fig_3_1_mapa_riesgos.png'),
    }
    sistema_prestamos(rutas['fig_1_1'])
    mapa_interesados(rutas['fig_1_2'])
    flujo_relevamiento(rutas['fig_2_1'])
    contraste_fuentes(rutas['fig_2_2'])
    mapa_riesgos(rutas['fig_3_1'], riesgos)
    return rutas
