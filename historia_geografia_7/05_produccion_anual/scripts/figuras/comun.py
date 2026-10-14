"""Funciones comunes de las figuras de la producción anual.

Parte de `04_muestra3/scripts/figuras.py` (muestra aprobada) y aplica la
observación A17 del dictamen:
- cada figura se dibuja al tamaño en que se imprime (`lienzo(ancho_cm, alto_cm)`),
  de modo que los tamaños de letra son tamaños efectivos: rótulos que el
  estudiante debe leer en 8 a 9,5 pt; notas de fuente en 7 pt como mínimo;
- todo mapa lleva leyenda completa de los símbolos que usa, norte, escala
  aproximada y nota de fuente que declara su carácter aproximado;
- límites internacionales en trazo discontinuo (legibles en fotocopia
  monocroma) y halo blanco en los rótulos que cruzan líneas.

Mapas: geometrías de Natural Earth (dominio público), github.com/nvkelso/
natural-earth-vector, carpeta geojson. En ese conjunto el río Paraguay figura
rotulado «Paraná»: cada tramo se rotula por su ubicación (`es_rio_paraguay`).
Natural Earth no trae el río Apa ni los lagos Ypacaraí e Ypoá: cuando hacen
falta se marcan con un símbolo propio y figuran en la leyenda como
«posición aproximada».
"""
import json
import math
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import patheffects  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Patch  # noqa: E402

HALO = [patheffects.withStroke(linewidth=2.6, foreground='white')]
AZUL = '#21374D'
AZUL2 = '#3D5A80'
AGUA = '#2B7BB9'
MAR = '#EAF3FA'
TIERRA = '#F4EFE6'
TIERRA_PY = '#E9DDC4'
GRIS = '#5F656D'
OCRE = '#B8860B'
ROJO = '#B03A2E'
VERDE = '#4E7D3A'
plt.rcParams['font.family'] = 'DejaVu Sans'
DPI = 300

# tamaños efectivos (pt), porque el lienzo tiene el tamaño de impresión
T_ROTULO = 8.5
T_ROTULO_CH = 8.0
T_PAIS = 9.5
T_NOTA = 7.0

CIUDADES_PY = {
    'Asunción': (-57.63, -25.28), 'Concepción': (-57.43, -23.41), 'Encarnación': (-55.87, -27.33),
    'Ciudad del Este': (-54.61, -25.51), 'Pilar': (-58.30, -26.86), 'Bahía Negra': (-58.17, -20.23),
    'Filadelfia': (-60.03, -22.35), 'Pedro Juan Caballero': (-55.73, -22.55),
}
REPRESAS = {'Itaipú': (-54.59, -25.41), 'Yacyretá': (-56.73, -27.48)}
APA_DESEMBOCADURA = (-57.95, -22.08)   # aproximada


def lienzo(ancho_cm, alto_cm):
    fig, ax = plt.subplots(figsize=(ancho_cm / 2.54, alto_cm / 2.54))
    return fig, ax


def guardar(fig, salida, rect=None):
    if rect:
        fig.tight_layout(rect=rect, pad=0.3)
    else:
        fig.tight_layout(pad=0.3)
    fig.savefig(salida, dpi=DPI)
    plt.close(fig)


def cargar(geo, nombre):
    with open(os.path.join(geo, nombre + '.geojson'), encoding='utf-8') as f:
        return json.load(f)['features']


def lineas(g):
    if not g:
        return []
    if g['type'] == 'LineString':
        return [g['coordinates']]
    if g['type'] == 'MultiLineString':
        return g['coordinates']
    return []


def poligonos(g):
    if not g:
        return []
    if g['type'] == 'Polygon':
        return [g['coordinates'][0]]
    if g['type'] == 'MultiPolygon':
        return [p[0] for p in g['coordinates']]
    return []


def es_rio_paraguay(linea):
    xs = [p[0] for p in linea]
    ys = [p[1] for p in linea]
    return max(xs) < -56.95 and min(ys) > -27.36 and max(ys) < -15.0


def dibujar_paises(ax, paises, resaltar=None, borde=0.6, colores=None):
    for f in paises:
        nombre = f['properties'].get('NAME')
        es = resaltar and nombre == resaltar
        color = (colores or {}).get(nombre, TIERRA_PY if es else TIERRA)
        for p in poligonos(f['geometry']):
            xs, ys = zip(*p)
            ax.fill(xs, ys, color=color, zorder=1)
            ax.plot(xs, ys, color='#3A3A3A' if es else '#6E6E6E', lw=borde * (1.5 if es else 1), ls=(0, (4, 2)), zorder=2)


def dibujar_rios(ax, rios, caja, nombres=None, ancho=1.1, gruesos=('Paraná', 'Pilcomayo', 'Amazonas', 'Mississippi')):
    x0, x1, y0, y1 = caja
    for f in rios:
        nombre = f['properties'].get('name')
        if nombres is not None and nombre not in nombres:
            continue
        for l in lineas(f['geometry']):
            xs, ys = zip(*l)
            if max(xs) < x0 or min(xs) > x1 or max(ys) < y0 or min(ys) > y1:
                continue
            ax.plot(xs, ys, color=AGUA, lw=ancho * (1.8 if nombre in gruesos else 1), zorder=4, solid_capstyle='round')


def marco(ax, x0, x1, y0, y1, ticks=True):
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    ax.set_aspect('equal')
    ax.set_facecolor(MAR)
    if ticks:
        ax.tick_params(labelsize=6.5, colors=GRIS, length=2, pad=1)
    else:
        ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color(GRIS)


def norte(ax, x, y, tam=0.6):
    ax.annotate('N', xy=(x, y + tam), xytext=(x, y), ha='center', fontsize=9, fontweight='bold', color=AZUL,
                arrowprops=dict(arrowstyle='-|>', color=AZUL, lw=1.2), zorder=9)


def nota_fuente(fig, texto):
    fig.text(0.01, 0.004, texto, fontsize=T_NOTA, color=GRIS, ha='left', va='bottom', wrap=True)


def escala(ax, x, y, lat_ref, km=200, dy=0.18):
    grados = km / (111.32 * math.cos(math.radians(abs(lat_ref))))
    ax.plot([x, x + grados], [y, y], color='#222222', lw=2.4, zorder=9, solid_capstyle='butt')
    ax.plot([x, x + grados / 2], [y, y], color='white', lw=1.1, zorder=10, solid_capstyle='butt')
    for k, t in ((0, '0'), (0.5, str(km // 2)), (1, f'{km} km')):
        ax.text(x + grados * k, y + dy, t, ha='center', fontsize=7, color='#222222', zorder=10, path_effects=HALO)
    ax.text(x, y - 2 * dy, 'Escala aproximada', fontsize=7, color='#333333', zorder=10, path_effects=HALO)


def simbolos(elementos):
    """Elementos de leyenda por nombre."""
    tabla = {
        'rio': Line2D([], [], color=AGUA, lw=2.2, label='Río'),
        'limite': Line2D([], [], color='#3A3A3A', lw=1, ls=(0, (4, 2)), label='Límite internacional'),
        'ciudad': Line2D([], [], marker='o', ls='', color=AZUL, ms=5, label='Ciudad'),
        'capital': Line2D([], [], marker='*', ls='', color=AZUL, ms=9, label='Capital'),
        'represa': Line2D([], [], marker='s', ls='', color=OCRE, mec='white', ms=6, label='Represa'),
        'apa': Line2D([], [], marker='^', ls='', color=AGUA, mec='white', ms=7,
                      label='Desembocadura del río Apa (aprox.)'),
        'sitio': Line2D([], [], marker='D', ls='', color=ROJO, mec='white', ms=6, label='Sitio arqueológico'),
        'ruta': Line2D([], [], color=ROJO, lw=1.8, label='Ruta propuesta'),
        'ruta2': Line2D([], [], color=ROJO, lw=1.8, ls=(0, (3, 1.5)), label='Ruta discutida'),
    }
    return [tabla[e] if isinstance(e, str) else e for e in elementos]


def leyenda(fig, elementos, ncol=None, y=0.035, tam=7.5):
    h = simbolos(elementos)
    fig.legend(handles=h, loc='lower center', bbox_to_anchor=(0.5, y), ncol=ncol or min(len(h), 4), fontsize=tam,
               frameon=False, handlelength=1.6, columnspacing=1.2)


def area(color, rotulo, alpha=0.55, rayado=None):
    return Patch(facecolor=color, edgecolor='#444444', alpha=alpha, hatch=rayado, label=rotulo)


def caja(ax, x, y, w, h, texto, fc, color='white', tam=8.5, negrita=True, ec='none'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.02,rounding_size=0.08', fc=fc, ec=ec, lw=0.8))
    ax.text(x + w / 2, y + h / 2, texto, ha='center', va='center', fontsize=tam, color=color,
            fontweight='bold' if negrita else 'normal', wrap=True)


def flecha(ax, x0, y0, x1, y1, color=GRIS, lw=1.3):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle='-|>', color=color, lw=lw))


def rotulo(ax, x, y, texto, tam=T_ROTULO, color=AZUL, **kw):
    kw.setdefault('zorder', 8)
    return ax.text(x, y, texto, fontsize=tam, color=color, path_effects=HALO, **kw)
