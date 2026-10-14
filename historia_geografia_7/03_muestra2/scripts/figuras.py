"""Figuras nuevas de la segunda muestra.

Mapas: geometrías de Natural Earth (dominio público), descargadas de
github.com/nvkelso/natural-earth-vector (carpeta geojson). En ese conjunto el
río Paraguay figura rotulado como «Paraná»; acá cada tramo se rotula según
su ubicación (ver `es_rio_paraguay`). Solo se dibujan ríos y lagos que están
en los datos; las ciudades y represas se marcan con coordenadas aproximadas.

Esquemas: dibujos propios (no son mapas).

Uso: python3 figuras.py CARPETA_GEOJSON CARPETA_SALIDA
"""
import json
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

AZUL = '#21374D'
AZUL2 = '#3D5A80'
AGUA = '#2B7BB9'
TIERRA = '#F4EFE6'
TIERRA_PY = '#E9DDC4'
GRIS = '#8A8F96'
FUENTE = 'DejaVu Sans'
plt.rcParams['font.family'] = FUENTE

# Coordenadas aproximadas (longitud, latitud)
CIUDADES_PY = {
    'Asunción': (-57.63, -25.28), 'Concepción': (-57.43, -23.41), 'Encarnación': (-55.87, -27.33),
    'Ciudad del Este': (-54.61, -25.51), 'Pilar': (-58.30, -26.86), 'Bahía Negra': (-58.17, -20.23),
}
REPRESAS = {'Itaipú': (-54.59, -25.41), 'Yacyretá': (-56.73, -27.48)}


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
    """Tramos rotulados «Paraná» en Natural Earth que en realidad son el río
    Paraguay: los que corren al oeste de 57° O y al norte de la confluencia
    (27,3° S), entre 15,5° S y 27,35° S."""
    xs = [p[0] for p in linea]
    ys = [p[1] for p in linea]
    return max(xs) < -56.95 and min(ys) > -27.36 and max(ys) < -15.0


def pais(features, nombre):
    for f in features:
        p = f['properties']
        if nombre in (p.get('NAME'), p.get('ADMIN'), p.get('NAME_ES')):
            return f
    raise KeyError(nombre)


def dibujar_paises(ax, paises, resaltar=None, borde=0.6):
    for f in paises:
        es = resaltar and f['properties'].get('NAME') == resaltar
        for p in poligonos(f['geometry']):
            xs, ys = zip(*p)
            ax.fill(xs, ys, color=TIERRA_PY if es else TIERRA, zorder=1)
            ax.plot(xs, ys, color='#6B6B6B' if es else '#A8A8A8', lw=borde * (1.6 if es else 1), zorder=2)


def marco(ax, x0, x1, y0, y1):
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    ax.set_aspect('equal')
    ax.set_facecolor('#EAF3FA')
    ax.tick_params(labelsize=7, colors=GRIS)
    for s in ax.spines.values():
        s.set_color(GRIS)


def norte(ax, x, y, tam=0.6):
    ax.annotate('N', xy=(x, y + tam), xytext=(x, y), ha='center', fontsize=9, fontweight='bold', color=AZUL,
                arrowprops=dict(arrowstyle='-|>', color=AZUL, lw=1.2), zorder=9)


def nota_fuente(fig, texto):
    fig.text(0.01, 0.005, texto, fontsize=6.5, color=GRIS, ha='left', va='bottom')


def mapa_rios_paraguay(geo, salida, mudo=False):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    rios = cargar(geo, 'ne_10m_rivers_lake_centerlines_scale_rank')
    lagos = cargar(geo, 'ne_10m_lakes')
    fig, ax = plt.subplots(figsize=(6.4, 6.6))
    marco(ax, -63.2, -53.6, -28.4, -18.6)
    dibujar_paises(ax, paises, resaltar='Paraguay')
    for f in lagos:
        for p in poligonos(f['geometry']):
            xs, ys = zip(*p)
            if min(xs) > -64 and max(xs) < -53 and min(ys) > -29 and max(ys) < -18:
                ax.fill(xs, ys, color=AGUA, zorder=3)
    for f in rios:
        nombre = f['properties'].get('name')
        for l in lineas(f['geometry']):
            xs, ys = zip(*l)
            if max(xs) < -64 or min(xs) > -53 or max(ys) < -29 or min(ys) > -18:
                continue
            ancho = 2.2 if nombre in ('Paraná', 'Pilcomayo') else 1.1
            ax.plot(xs, ys, color=AGUA, lw=ancho, zorder=4, solid_capstyle='round')
    if not mudo:
        for n, (x, y) in CIUDADES_PY.items():
            ax.plot(x, y, 'o', ms=4, color=AZUL, zorder=6)
            dx, dy, ha = {'Ciudad del Este': (-0.15, -0.28, 'right'), 'Encarnación': (0.0, 0.2, 'center')}.get(n, (0.15, 0.12, 'left'))
            ax.text(x + dx, y + dy, n, fontsize=7.5, color=AZUL, ha=ha, zorder=7)
        for n, (x, y) in REPRESAS.items():
            ax.plot(x, y, 's', ms=6, color='#B8860B', mec='white', zorder=6)
            dx, dy, ha = {'Itaipú': (-0.15, 0.18, 'right'), 'Yacyretá': (-0.1, -0.32, 'right')}[n]
            ax.text(x + dx, y + dy, 'Represa ' + n, fontsize=7, color='#7A5A08', ha=ha, zorder=7)
        rot = dict(fontsize=8, color='#1B5E8C', fontstyle='italic', zorder=8)
        ax.text(-58.05, -21.3, 'Río\nParaguay', rotation=0, **rot)
        ax.text(-54.35, -23.2, 'Río\nParaná', **rot)
        ax.text(-55.6, -27.75, 'Río Paraná', **rot)
        ax.text(-61.2, -23.05, 'Río Pilcomayo', rotation=-28, **rot)
        ax.text(-60.6, -22.95, '', **rot)
        ax.text(-59.6, -23.05, 'Río Verde', rotation=-8, fontsize=7, color='#1B5E8C', fontstyle='italic', zorder=8)
        ax.text(-56.75, -24.15, 'Río Jejuí Guazú', fontsize=7, color='#1B5E8C', fontstyle='italic', zorder=8)
        lab = dict(fontsize=9.5, color='#555555', fontweight='bold', zorder=8)
        ax.text(-62.6, -19.4, 'BOLIVIA', **lab)
        ax.text(-55.6, -20.0, 'BRASIL', **lab)
        ax.text(-62.2, -26.6, 'ARGENTINA', **lab)
        ax.text(-60.6, -21.9, 'PARAGUAY', fontsize=11, color='#7A5A2B', fontweight='bold', zorder=8)
        ax.text(-60.9, -22.35, 'Región Occidental (Chaco)', fontsize=7.5, color='#7A5A2B', zorder=8)
        ax.text(-57.0, -25.95, 'Región\nOriental', fontsize=7.5, color='#7A5A2B', zorder=8)
    norte(ax, -54.2, -19.9)
    nota_fuente(fig, 'Elaboración propia con datos de Natural Earth (dominio público). Ciudades y represas en posición aproximada.'
                if not mudo else 'Mapa mudo. Elaboración propia con datos de Natural Earth (dominio público).')
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    fig.savefig(salida, dpi=220)
    plt.close(fig)


RIOS_AMERICA = ['Amazonas', 'Orinoco', 'Paraná', 'Uruguay', 'Mississippi', 'Missouri', 'St. Lawrence',
                'Magdalena', 'São  Francisco', 'Mackenzie', 'Colorado', 'Rio Grande', 'Madeira', 'Pilcomayo', 'Yukon']
ROTULO_ES = {'St. Lawrence': 'San Lorenzo', 'São  Francisco': 'São Francisco', 'Rio Grande': 'Bravo (Grande)'}


def mapa_america(geo, salida, numerado=None):
    """numerado: dict {nombre_ne: número} para la evaluación (sin nombres)."""
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    rios = cargar(geo, 'ne_50m_rivers_lake_centerlines')
    lagos = cargar(geo, 'ne_50m_lakes')
    fig, ax = plt.subplots(figsize=(6.2, 6.4))
    marco(ax, -170, -30, -57, 72)
    ame = [f for f in paises if f['properties'].get('CONTINENT') in ('North America', 'South America')]
    dibujar_paises(ax, ame, borde=0.35)
    for f in lagos:
        nombre = f['properties'].get('name') or ''
        for p in poligonos(f['geometry']):
            xs, ys = zip(*p)
            if max(xs) < -30 and min(xs) > -170:
                ax.fill(xs, ys, color=AGUA, zorder=3)
    puntos = {}
    for f in rios:
        nombre = f['properties'].get('name')
        for l in lineas(f['geometry']):
            xs, ys = zip(*l)
            if max(xs) > -30:
                continue
            principal = nombre in RIOS_AMERICA
            ax.plot(xs, ys, color=AGUA, lw=1.3 if principal else 0.5, zorder=4, alpha=1 if principal else 0.6)
            if principal:
                puntos.setdefault(nombre, []).append(l[len(l) // 2])
    if numerado:
        for nombre, num in numerado.items():
            x, y = puntos[nombre][0]
            ax.text(x, y, str(num), fontsize=10, fontweight='bold', color='white', ha='center', va='center', zorder=9,
                    bbox=dict(boxstyle='circle,pad=0.25', fc=AZUL, ec='white'))
    else:
        pos = {'Amazonas': (-63, -2.2), 'Orinoco': (-69, 8.6), 'Paraná': (-56.5, -30.5), 'Mississippi': (-88.5, 36),
               'Missouri': (-110, 46), 'St. Lawrence': (-75, 49.5), 'Mackenzie': (-131, 63.5), 'Magdalena': (-80.5, 10.2),
               'São  Francisco': (-46, -13), 'Colorado': (-121, 35.5), 'Rio Grande': (-112, 28.5), 'Uruguay': (-55.5, -33.5)}
        for nombre, (x, y) in pos.items():
            ax.text(x, y, ROTULO_ES.get(nombre, nombre), fontsize=7.5, color='#1B5E8C', fontstyle='italic', zorder=8)
        ax.text(-93, 48.5, 'Grandes Lagos', fontsize=7, color='#1B5E8C', zorder=8)
        ax.text(-73.5, -17.5, 'Lago Titicaca', fontsize=7, color='#1B5E8C', zorder=8, ha='right')
        ax.text(-152, -20, 'OCÉANO\nPACÍFICO', fontsize=8.5, color='#5A7C95', ha='center')
        ax.text(-40, 18, 'OCÉANO\nATLÁNTICO', fontsize=8.5, color='#5A7C95', ha='center')
        ax.text(-125, 75, '', fontsize=8)
    norte(ax, -38, 58, tam=6)
    nota_fuente(fig, 'Elaboración propia con datos de Natural Earth (dominio público). Escala de 1:50 millones.')
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    fig.savefig(salida, dpi=220)
    plt.close(fig)


def mapa_hidrovia(geo, salida):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    rios = cargar(geo, 'ne_10m_rivers_lake_centerlines_scale_rank')
    fig, ax = plt.subplots(figsize=(5.6, 7.8))
    marco(ax, -66, -50, -36, -14)
    sa = [f for f in paises if f['properties'].get('CONTINENT') == 'South America']
    dibujar_paises(ax, sa, resaltar='Paraguay', borde=0.45)
    for f in rios:
        nombre = f['properties'].get('name')
        for l in lineas(f['geometry']):
            xs, ys = zip(*l)
            if max(xs) < -66 or min(xs) > -50 or max(ys) < -36 or min(ys) > -14:
                continue
            via = False
            if nombre == 'Paraná':
                if es_rio_paraguay(l):
                    pts = [p for p in l if p[1] <= -19.0]   # desde Corumbá hacia el sur
                    if len(pts) > 1:
                        px, py = zip(*pts)
                        ax.plot(px, py, color='#C0392B', lw=2.4, zorder=4)
                    via = True
                elif max(ys) <= -27.15 and min(ys) > -34.2:   # Paraná inferior, desde la confluencia
                    ax.plot(xs, ys, color='#C0392B', lw=2.4, zorder=4)
                    via = True
            if not via:
                ax.plot(xs, ys, color=AGUA, lw=0.8, zorder=3)
    ax.annotate('', xy=(-57.68, -16.25), xytext=(-57.66, -18.9),
                arrowprops=dict(arrowstyle='-|>', color='#C0392B', lw=1.6, ls='--'), zorder=5)
    for n, (x, y), ha in [('Cáceres (Brasil)', (-57.68, -16.07), 'left'), ('Corumbá', (-57.65, -19.01), 'left'),
                          ('Asunción', (-57.63, -25.28), 'left'), ('Rosario', (-60.65, -32.95), 'right'),
                          ('Nueva Palmira (Uruguay)', (-58.42, -33.88), 'left')]:
        ax.plot(x, y, 'o', ms=4.5, color=AZUL, zorder=6)
        ax.text(x + (0.35 if ha == 'left' else -0.35), y, n, fontsize=7.5, color=AZUL, ha=ha, va='center', zorder=7)
    lab = dict(fontsize=8.5, color='#555555', fontweight='bold')
    ax.text(-64.8, -17.5, 'BOLIVIA', **lab)
    ax.text(-53.5, -18.5, 'BRASIL', **lab)
    ax.text(-64.5, -30.5, 'ARGENTINA', **lab)
    ax.text(-56.2, -32.6, 'URUGUAY', **lab)
    ax.text(-60.4, -22.3, 'PARAGUAY', fontsize=9, color='#7A5A2B', fontweight='bold')
    ax.plot([], [], color='#C0392B', lw=2.4, label='Hidrovía Paraguay-Paraná (recorrido aproximado)')
    ax.plot([], [], color='#C0392B', lw=1.6, ls='--', label='Continúa hacia el norte hasta Cáceres')
    ax.legend(loc='lower right', fontsize=6.8, frameon=True)
    norte(ax, -51.2, -16.0, tam=1)
    nota_fuente(fig, 'Elaboración propia con datos de Natural Earth (dominio público). Puertos en posición aproximada.')
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    fig.savefig(salida, dpi=220)
    plt.close(fig)


def caja(ax, x, y, w, h, texto, fc, color='white', tam=8.5, negrita=True):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.02,rounding_size=0.08', fc=fc, ec='none'))
    ax.text(x + w / 2, y + h / 2, texto, ha='center', va='center', fontsize=tam, color=color,
            fontweight='bold' if negrita else 'normal', wrap=True)


def flecha(ax, x0, y0, x1, y1):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle='-|>', color=GRIS, lw=1.3))


def esquema_autoridades(salida):
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6.6); ax.axis('off')
    ax.text(0.05, 6.35, 'EN ESPAÑA', fontsize=7.5, color=GRIS, fontweight='bold')
    ax.text(0.05, 4.05, 'EN AMÉRICA', fontsize=7.5, color=GRIS, fontweight='bold')
    ax.plot([0, 10], [4.35, 4.35], color='#CCCCCC', lw=0.8, ls='--')
    caja(ax, 1.0, 5.45, 3.6, 0.75, 'El rey', AZUL, tam=9.5)
    caja(ax, 5.4, 5.45, 3.6, 0.75, 'Consejo de Indias\n(asesora al rey sobre América)', AZUL2, tam=7.8)
    flecha(ax, 4.6, 5.82, 5.4, 5.82)
    caja(ax, 1.0, 3.25, 3.6, 0.75, 'Virrey del Perú\n(desde 1542)', AZUL2, tam=8)
    caja(ax, 5.4, 3.25, 3.6, 0.75, 'Audiencia de Charcas\n(tribunal superior, creada en 1559)', AZUL2, tam=7.3)
    flecha(ax, 2.8, 5.45, 2.8, 4.0)
    flecha(ax, 4.6, 3.62, 5.4, 3.62)
    caja(ax, 1.0, 1.95, 3.6, 0.85, 'Gobernador del Río de la Plata\ny del Paraguay (sede: Asunción)', '#5B7FA6', tam=7.6)
    flecha(ax, 2.8, 3.25, 2.8, 2.8)
    caja(ax, 0.2, 0.25, 2.9, 1.15, 'Cabildo de Asunción (1541)\nalcaldes y regidores:\ngobierno de la ciudad', '#E6EBF1', color=AZUL, tam=7.3)
    flecha(ax, 2.0, 1.95, 1.65, 1.4)
    caja(ax, 3.4, 0.25, 2.9, 1.15, 'Obispado del Río de la Plata\n(1547, sede en Asunción):\nvida religiosa', '#E6EBF1', color=AZUL, tam=7.3)
    caja(ax, 6.6, 0.25, 3.2, 1.15, 'Encomienda: NO gobernaba.\nInstitución que asignaba\ntrabajo indígena a un español', '#F3E2C7', color='#6B4A12', tam=7.3)
    ax.text(6.0, 2.35, 'El gobernador era nombrado por el rey.\nSi faltaba y no había sucesor, la\nReal Provisión de 1537 permitía elegir\nuno provisional «en nombre» del rey.',
            fontsize=7.2, color=AZUL, va='center')
    fig.tight_layout()
    fig.savefig(salida, dpi=220)
    plt.close(fig)


HITOS_1534 = [
    (1534, 'Capitulación de\nPedro de Mendoza', 1), (1536, 'Fundación de\nBuenos Aires', -1),
    (1537.6, 'Fundación de Asunción\n(15 de agosto)', 1), (1537.7, 'Real Provisión\n(12 de septiembre)', -1),
    (1539, 'Irala, gobernador\ninterino', 1), (1541, 'Cabildo de Asunción;\nse despuebla Buenos Aires', -1),
    (1542, 'Llega Cabeza\nde Vaca', 1), (1544, 'Cabeza de Vaca\nes depuesto', -1),
    (1547, 'Se crea el\nObispado', 1), (1556, 'Reparto de\nencomiendas', -1),
]


def linea_tiempo(salida):
    """Línea de tiempo vertical: un renglón por hecho, sin superposiciones."""
    n = len(HITOS_1534)
    fig, ax = plt.subplots(figsize=(6.6, 0.42 * n + 0.5))
    ax.set_xlim(0, 10); ax.set_ylim(-0.6, n - 0.4); ax.axis('off')
    ax.plot([1.55, 1.55], [-0.3, n - 0.7], color=AZUL, lw=2)
    for k, (anio, texto, _) in enumerate(HITOS_1534):
        y = n - 1 - k
        etiqueta = '1537' if anio != int(anio) else str(int(anio))
        ax.text(1.25, y, etiqueta, ha='right', va='center', fontsize=9, fontweight='bold', color=AZUL)
        ax.plot(1.55, y, 'o', ms=6, color='#B8860B', zorder=5)
        ax.text(1.9, y, texto.replace('\n', ' '), ha='left', va='center', fontsize=8.8, color='#222222')
    fig.tight_layout()
    fig.savefig(salida, dpi=220)
    plt.close(fig)


def main():
    geo, out = sys.argv[1:3]
    os.makedirs(out, exist_ok=True)
    esquema_autoridades(os.path.join(out, 'fig_10_2_autoridades.png'))
    linea_tiempo(os.path.join(out, 'fig_10_3_linea_tiempo.png'))
    mapa_rios_paraguay(geo, os.path.join(out, 'fig_18_2_rios_paraguay.png'))
    mapa_rios_paraguay(geo, os.path.join(out, 'ficha_18A_mapa_mudo.png'), mudo=True)
    mapa_america(geo, os.path.join(out, 'fig_18_3_rios_america.png'))
    mapa_america(geo, os.path.join(out, 'eval_u5_rios_numerados.png'),
                 numerado={'Amazonas': 1, 'Mississippi': 2, 'Paraná': 3, 'St. Lawrence': 4})
    mapa_hidrovia(geo, os.path.join(out, 'fig_F1_hidrovia.png'))


if __name__ == '__main__':
    main()
