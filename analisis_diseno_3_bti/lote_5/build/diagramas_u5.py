# -*- coding: utf-8 -*-
"""Figuras del lote 5 (Capítulos 14 a 16), generadas por código con matplotlib; sin recursos de terceros.
Reutiliza sin modificarlo `lote_3/build/diagramas_u3.py` (lienzo, colores, registro de símbolos). Las tres son esquemas
didácticos: no usan ninguna notación de diagramas ni símbolos nuevos.
  - fig_14_1: clases de casos alrededor del límite de préstamos de un estudiante (máximo 2).
  - fig_14_2: de un caso de prueba a un reporte de defecto, con su condición.
  - fig_16_1: el ciclo de una corrección: reproducir, diagnosticar, corregir, revisar entre pares, regresión."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(ADS, 'lote_3', 'build'))
import diagramas_u3 as G3
plt, FancyBboxPatch, Rectangle, FancyArrowPatch = G3.plt, G3.FancyBboxPatch, G3.Rectangle, G3.FancyArrowPatch
DARK, MED, LIGHT, AMBAR, GRIS, NEGRO = G3.DARK, G3.MED, G3.LIGHT, G3.AMBAR, G3.GRIS, G3.NEGRO
Lienzo, REGISTRO = G3.Lienzo, G3.REGISTRO
FIGURAS = {'fig_14_1': 'esquema', 'fig_14_2': 'esquema', 'fig_16_1': 'esquema'}


def caja(ax, x, y, w, h, t, sub=None, borde=MED, fs=8.6):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03,rounding_size=0.12', facecolor=LIGHT,
                                edgecolor=borde, lw=1.4, zorder=2))
    ax.text(x + w / 2, y + h / 2 + (0.18 if sub else 0), t, ha='center', va='center', fontsize=fs, weight='bold',
            color=DARK, zorder=3)
    if sub:
        ax.text(x + w / 2, y + h / 2 - 0.25, sub, ha='center', va='center', fontsize=7.4, color='#333333', zorder=3)


def flecha(ax, x0, y0, x1, y1):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle='-|>', mutation_scale=12, color=GRIS, lw=1.3, zorder=1))


def limites(ruta):
    Lienzo('fig_14_1', 'esquema')
    fig, ax = plt.subplots(figsize=(10.6, 3.3))
    ax.set_xlim(0, 16); ax.set_ylim(0, 4.6); ax.axis('off')
    ax.text(0.2, 4.2, 'Préstamos activos de un estudiante antes de pedir otro (máximo 2, en Parámetro)', ha='left', va='center',
            fontsize=9, weight='bold', color=DARK)
    pos = [(0, 'Normal', 'tiene 0: se presta', MED), (1, 'Límite (se acepta)', 'tiene 1: se presta y llega a 2', MED),
           (2, 'Límite (se rechaza)', 'tiene 2: ME-02, sin préstamo nuevo', AMBAR)]
    x = lambda k: 2.2 + k * 5.4
    ax.plot([x(0) - 1.2, x(2) + 1.2], [2.0, 2.0], color=GRIS, lw=1.5, zorder=1)
    for k, clase, que, c in pos:
        ax.add_patch(plt.Circle((x(k), 2.0), 0.32, facecolor=LIGHT, edgecolor=c, lw=1.8, zorder=2))
        ax.text(x(k), 2.0, str(k), ha='center', va='center', fontsize=10, weight='bold', color=DARK, zorder=3)
        ax.text(x(k), 3.0, clase, ha='center', va='center', fontsize=8.6, weight='bold', color=c)
        ax.text(x(k), 1.25, que, ha='center', va='center', fontsize=8.0, color='#333333')
    ax.plot([x(1.5), x(1.5)], [1.55, 3.4], color=NEGRO, lw=1.4, ls='--')
    ax.text(x(1.5) + 0.12, 3.55, 'el borde de la regla', ha='left', va='center', fontsize=8, color=NEGRO)
    ax.text(0.2, 0.4, 'Los casos de límite se eligen a los dos lados del borde: uno que todavía se acepta y el primero que se rechaza.',
            ha='left', va='center', fontsize=8.2, color=GRIS, style='italic')
    G3._guardar(fig, ruta)


def reporte(ruta):
    Lienzo('fig_14_2', 'esquema')
    fig, ax = plt.subplots(figsize=(10.8, 3.4))
    ax.set_xlim(0, 16); ax.set_ylim(0, 4.8); ax.axis('off')
    caja(ax, 0.1, 2.3, 3.4, 1.4, 'Caso de prueba', 'requisito · entradas\n· esperado')
    caja(ax, 4.0, 2.3, 3.2, 1.4, 'Ejecución', 'obtenido · entorno\n· evidencia')
    caja(ax, 8.0, 3.2, 3.3, 1.1, '¿Coincide?', 'sí: se registra «correcto»')
    caja(ax, 8.0, 1.6, 3.3, 1.1, 'No coincide', 'se reproduce otra vez', borde=AMBAR)
    caja(ax, 12.1, 1.3, 3.7, 1.7, 'Reporte de defecto', 'pasos · esperado · obtenido ·\ngravedad · entorno · condición', borde=AMBAR)
    flecha(ax, 3.5, 3.0, 4.0, 3.0); flecha(ax, 7.2, 3.2, 8.0, 3.7); flecha(ax, 7.2, 2.8, 8.0, 2.1); flecha(ax, 11.3, 2.15, 12.1, 2.15)
    ax.text(0.2, 0.55, 'Condición del resultado: comprobado, reproducido, simulado o pendiente. Lo que no se pudo probar no es «correcto».',
            ha='left', va='center', fontsize=8.2, color=GRIS, style='italic')
    G3._guardar(fig, ruta)


def ciclo(ruta):
    Lienzo('fig_16_1', 'esquema')
    fig, ax = plt.subplots(figsize=(10.8, 3.2))
    ax.set_xlim(0, 16); ax.set_ylim(0, 4.4); ax.axis('off')
    pasos = [('Reproducir', 'pasos que se repiten'), ('Diagnosticar', 'causa, capa e impacto'),
             ('Corregir', 'el cambio mínimo'), ('Revisar', 'otro integrante'),
             ('Regresión', 'pruebas afectadas\ny núcleo'), ('Versión', 'bitácora y\ntrazabilidad')]
    for i, (t, s) in enumerate(pasos):
        x = 0.2 + i * 2.65
        caja(ax, x, 1.8, 2.25, 1.5, t, s, borde=AMBAR if t == 'Regresión' else MED)
        if i:
            flecha(ax, x - 0.4, 2.55, x, 2.55)
    ax.text(0.2, 0.95, 'Si la regresión falla, la corrección no se integra: se vuelve a diagnosticar.', ha='left', va='center',
            fontsize=8.2, color=GRIS, style='italic')
    ax.text(0.2, 0.45, 'Un cambio de requisito (como SC-02) pasa antes por la solicitud de cambio, con su versión.', ha='left',
            va='center', fontsize=8.2, color=GRIS, style='italic')
    G3._guardar(fig, ruta)


def generar(carpeta=None):
    d = carpeta or os.path.join(AQUI, 'figs')
    os.makedirs(d, exist_ok=True)
    REGISTRO.clear()
    r = {'fig_14_1': os.path.join(d, 'fig_14_1_casos_alrededor_del_limite.png'),
         'fig_14_2': os.path.join(d, 'fig_14_2_del_caso_al_reporte.png'),
         'fig_16_1': os.path.join(d, 'fig_16_1_ciclo_de_una_correccion.png')}
    limites(r['fig_14_1']); reporte(r['fig_14_2']); ciclo(r['fig_16_1'])
    json.dump(REGISTRO, open(os.path.join(d, 'simbolos.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    return r


if __name__ == '__main__':
    print(generar())
