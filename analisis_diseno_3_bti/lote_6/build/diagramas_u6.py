# -*- coding: utf-8 -*-
"""Figuras del lote 6 (Capítulos 17 y 18), generadas por código con matplotlib; sin recursos de terceros.
Reutiliza sin modificarlo el lienzo de `lote_3/build/diagramas_u3.py` y las cajas de `lote_5/build/diagramas_u5.py`.
Las dos son esquemas didácticos: no usan ninguna notación de diagramas ni símbolos nuevos.
  - fig_17_1: de la guía escrita al acta de entrega (Encuentros 33 y 34).
  - fig_18_1: una demostración organizada por requisitos y evidencias."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(ADS, 'lote_5', 'build'))
import diagramas_u5 as G5
G3 = G5.G3
plt, caja, flecha = G5.plt, G5.caja, G5.flecha
MED, AMBAR, GRIS = G5.MED, G5.AMBAR, G5.GRIS
Lienzo, REGISTRO = G5.Lienzo, G5.REGISTRO
FIGURAS = {'fig_17_1': 'esquema', 'fig_18_1': 'esquema'}


def entrega(ruta):
    Lienzo('fig_17_1', 'esquema')
    fig, ax = plt.subplots(figsize=(10.8, 3.3))
    ax.set_xlim(0, 16); ax.set_ylim(0, 4.6); ax.axis('off')
    pasos = [('Guía y manual', 'el equipo los escribe'), ('Prueba propia', 'carpeta limpia,\nal pie de la letra'),
             ('Otro equipo', 'instala y restaura\nsin ayuda'), ('Acta', 'pasos, mensajes\ny observaciones'),
             ('Ajustes', 'se corrige y se\nvuelve a probar'), ('H6', 'paquete\nreproducible')]
    for i, (t, s) in enumerate(pasos):
        x = 0.2 + i * 2.65
        caja(ax, x, 1.9, 2.25, 1.5, t, s, borde=AMBAR if t == 'Otro equipo' else MED)
        if i:
            flecha(ax, x - 0.4, 2.65, x, 2.65)
    ax.text(0.2, 1.0, 'La instalación por otro equipo la evalúa una persona ajena al desarrollo: una ejecución automática de la '
            'guía', ha='left', va='center', fontsize=8.2, color=GRIS, style='italic')
    ax.text(0.2, 0.55, 'es solo una comprobación técnica.', ha='left', va='center', fontsize=8.2, color=GRIS, style='italic')
    G3._guardar(fig, ruta)


def demostracion(ruta):
    Lienzo('fig_18_1', 'esquema')
    fig, ax = plt.subplots(figsize=(10.8, 3.4))
    ax.set_xlim(0, 16); ax.set_ylim(0, 4.8); ax.axis('off')
    caja(ax, 0.1, 2.4, 3.2, 1.4, 'Requisito', 'imprescindible,\ndel catálogo')
    caja(ax, 3.9, 2.4, 3.2, 1.4, 'Evidencia', 'caso, prueba\no acta')
    caja(ax, 7.7, 3.3, 3.6, 1.1, 'En vivo', 'se muestra el caso')
    caja(ax, 7.7, 1.7, 3.6, 1.1, 'Si falla en vivo', 'se muestra lo registrado', borde=AMBAR)
    caja(ax, 12.0, 2.4, 3.8, 1.4, 'Pregunta', 'del docente: decisión\no prueba')
    flecha(ax, 3.3, 3.1, 3.9, 3.1); flecha(ax, 7.1, 3.3, 7.7, 3.8); flecha(ax, 7.1, 2.9, 7.7, 2.25)
    flecha(ax, 11.3, 3.8, 12.0, 3.25); flecha(ax, 11.3, 2.25, 12.0, 2.85)
    ax.text(0.2, 0.7, 'Cada paso del guion tiene un tiempo fijo. Si algo falla en vivo, se dice y se muestra la evidencia '
            'registrada: no se oculta.', ha='left', va='center', fontsize=8.2, color=GRIS, style='italic')
    G3._guardar(fig, ruta)


def generar(carpeta=None):
    d = carpeta or os.path.join(AQUI, 'figs')
    os.makedirs(d, exist_ok=True)
    REGISTRO.clear()
    r = {'fig_17_1': os.path.join(d, 'fig_17_1_de_la_guia_al_acta.png'),
         'fig_18_1': os.path.join(d, 'fig_18_1_demostracion_por_requisitos.png')}
    entrega(r['fig_17_1']); demostracion(r['fig_18_1'])
    json.dump(REGISTRO, open(os.path.join(d, 'simbolos.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    return r


if __name__ == '__main__':
    print(generar())
