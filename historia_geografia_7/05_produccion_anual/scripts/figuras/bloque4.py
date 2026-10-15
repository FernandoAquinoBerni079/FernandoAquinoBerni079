"""Figuras del Bloque IV (encuentros 28 a 36).

Los mapas de la Clase 18, la Continuación F y la Evaluación U5 parten de los
aprobados en la muestra 3 y se redibujan al tamaño de impresión (A17), con el
río Apa marcado con símbolo propio en la leyenda. Los mapas de climas y de
regiones naturales son esquemas de ubicación general, no mapas temáticos
medidos; los valores de lluvia del Paraguay son aproximados y se declaran así.
"""
import os

from matplotlib.lines import Line2D
from matplotlib.patches import Ellipse

from comun import (AGUA, AZUL, AZUL2, GRIS, OCRE, ROJO, VERDE, area, caja, cargar, dibujar_paises, escala, flecha, guardar,
                   leyenda, lienzo, lineas, marco, norte, nota_fuente, poligonos, rotulo, es_rio_paraguay, APA_DESEMBOCADURA,
                   CIUDADES_PY, REPRESAS)

ANCHOS = {}
RIO_T = '#1B5E8C'


def reg(nombre, ancho):
    ANCHOS[nombre] = ancho
    return nombre


def punto(color, texto, marker='o', ms=6):
    return Line2D([], [], marker=marker, ls='', color=color, mec='white', ms=ms, label=texto)


def rios_caja(ax, rios, caja_, grueso=('Paraná', 'Pilcomayo'), lw=1.0):
    x0, x1, y0, y1 = caja_
    for f in rios:
        nombre = f['properties'].get('name')
        for l in lineas(f['geometry']):
            xs, ys = zip(*l)
            if max(xs) < x0 or min(xs) > x1 or max(ys) < y0 or min(ys) > y1:
                continue
            ax.plot(xs, ys, color=AGUA, lw=lw * (2.0 if nombre in grueso else 1), zorder=4, solid_capstyle='round')


# ---------------------------------------------------------------- Clase 18
def mapa_rios_paraguay(geo, salida, ancho=13.5, mudo=False):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    rios = cargar(geo, 'ne_10m_rivers_lake_centerlines_scale_rank')
    fig, ax = lienzo(ancho, ancho * 1.12)
    marco(ax, -63.2, -53.6, -28.4, -18.6, ticks=False)
    dibujar_paises(ax, paises, resaltar='Paraguay')
    rios_caja(ax, rios, (-64, -53, -29, -18))
    elems = ['rio', 'limite']
    if not mudo:
        for n in ('Asunción', 'Concepción', 'Encarnación', 'Ciudad del Este', 'Pilar'):
            x, y = CIUDADES_PY[n]
            ax.plot(x, y, 'o', ms=4.5, color=AZUL, zorder=6)
            dx, dy, ha = {'Ciudad del Este': (-0.2, -0.45, 'right'), 'Encarnación': (0.0, 0.3, 'center'),
                          'Pilar': (-0.2, 0.2, 'right')}.get(n, (0.2, 0.15, 'left'))
            rotulo(ax, x + dx, y + dy, n, tam=8, ha=ha)
        for n, (x, y) in REPRESAS.items():
            ax.plot(x, y, 's', ms=7, color=OCRE, mec='white', zorder=6)
            dx, dy, ha = {'Itaipú': (-0.2, 0.7, 'right'), 'Yacyretá': (-0.3, -0.45, 'right')}[n]
            rotulo(ax, x + dx, y + dy, 'Represa ' + n, tam=8, color='#7A5A08', ha=ha)
        rot = dict(tam=8, color=RIO_T, fontstyle='italic', fontweight='bold')
        rotulo(ax, -58.0, -20.9, 'Río\nParaguay', **rot)
        rotulo(ax, -54.4, -22.9, 'Río\nParaná', **rot)
        rotulo(ax, -56.2, -27.9, 'Río Paraná', **rot)
        rotulo(ax, -60.9, -24.0, 'Río Pilcomayo', rotation=-30, **rot)
        ax.plot(*APA_DESEMBOCADURA, '^', ms=7, color=AGUA, mec='white', zorder=7)
        rotulo(ax, -57.75, -22.05, 'Río Apa', tam=8, color=RIO_T, fontweight='bold', va='center')
        for x, y, t in ((-62.4, -19.5, 'BOLIVIA'), (-55.6, -20.0, 'BRASIL'), (-62.2, -26.8, 'ARGENTINA')):
            rotulo(ax, x, y, t, tam=9.5, color='#555555', fontweight='bold')
        rotulo(ax, -60.8, -21.8, 'PARAGUAY', tam=10.5, color='#7A5A2B', fontweight='bold')
        rotulo(ax, -61.1, -22.35, 'Región Occidental (Chaco)', tam=8, color='#7A5A2B')
        rotulo(ax, -56.6, -24.3, 'Región Oriental', tam=8, color='#7A5A2B')
        elems += ['ciudad', 'represa', 'apa']
    norte(ax, -54.2, -19.9)
    escala(ax, -62.9, -28.0, -24.0)
    leyenda(fig, elems, ncol=3, y=0.06)
    nota_fuente(fig, 'Mapa aproximado. Elaboración propia con datos de Natural Earth (dominio público). Ciudades y represas en posición '
                     'aproximada; Natural Earth no trae el río Apa: se marca su desembocadura.' if not mudo else
                     'Mapa mudo. Elaboración propia con datos de Natural Earth (dominio público).')
    guardar(fig, salida, rect=(0, 0.13 if not mudo else 0.09, 1, 1))


RIOS_AMERICA = ['Amazonas', 'Orinoco', 'Paraná', 'Uruguay', 'Mississippi', 'Missouri', 'St. Lawrence', 'Magdalena',
                'São  Francisco', 'Mackenzie', 'Colorado', 'Rio Grande', 'Madeira', 'Pilcomayo', 'Yukon']
RIOS_NUMERADOS = {'Amazonas': (1, (-60.0, -3.2)), 'Mississippi': (2, (-90.6, 35.0)), 'Paraná': (3, (-59.9, -31.6))}


def mapa_rios_america(geo, salida, ancho=13.0, numerado=None):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    rios = cargar(geo, 'ne_50m_rivers_lake_centerlines')
    lagos = cargar(geo, 'ne_50m_lakes')
    fig, ax = lienzo(ancho, ancho * 1.08)
    marco(ax, -170, -30, -57, 72, ticks=False)
    ame = [f for f in paises if f['properties'].get('CONTINENT') in ('North America', 'South America')]
    dibujar_paises(ax, ame, borde=0.25)
    for f in lagos:
        for p in poligonos(f['geometry']):
            xs, ys = zip(*p)
            if max(xs) < -30 and min(xs) > -170:
                ax.fill(xs, ys, color=AGUA, zorder=3)
    for f in rios:
        nombre = f['properties'].get('name')
        for l in lineas(f['geometry']):
            xs, ys = zip(*l)
            if max(xs) > -30:
                continue
            principal = nombre in RIOS_AMERICA
            ax.plot(xs, ys, color=AGUA, lw=1.4 if principal else 0.5, zorder=4, alpha=1 if principal else 0.6)
    if numerado:
        for nombre, (num, obj) in numerado.items():
            cand = [p for f in rios if f['properties'].get('name') == nombre for l in lineas(f['geometry']) for p in l]
            x, y = min(cand, key=lambda p: (p[0] - obj[0]) ** 2 + (p[1] - obj[1]) ** 2)
            ax.plot(x, y, 'o', ms=13, color=AZUL, mec='white', zorder=8)
            ax.text(x, y, str(num), ha='center', va='center', fontsize=9, color='white', fontweight='bold', zorder=9)
        nota = 'Mapa para la evaluación. Elaboración propia con datos de Natural Earth (dominio público).'
    else:
        pos = {'Amazonas': (-63, -1.4, 'Amazonas'), 'Orinoco': (-69, 9.0, 'Orinoco'), 'Paraná': (-56.5, -29.5, 'Paraná'),
               'Mississippi': (-88.0, 36, 'Mississippi'), 'Missouri': (-112, 46.5, 'Missouri'), 'San Lorenzo': (-73, 50, 'San Lorenzo'),
               'Mackenzie': (-133, 63.5, 'Mackenzie'), 'São Francisco': (-45.5, -12.5, 'São Francisco'), 'Colorado': (-123, 34.5, 'Colorado'),
               'Bravo': (-113, 27.5, 'Bravo (Grande)'), 'Uruguay': (-55.0, -33.6, 'Uruguay')}
        for _, (x, y, t) in pos.items():
            rotulo(ax, x, y, t, tam=8, color=RIO_T, fontstyle='italic', fontweight='bold')
        rotulo(ax, -86, 41.5, 'Grandes Lagos', tam=7.8, color=RIO_T)
        rotulo(ax, -71.0, -17.5, 'Lago Titicaca', tam=7.8, color=RIO_T, ha='right')
        rotulo(ax, -150, -20, 'OCÉANO\nPACÍFICO', tam=8.5, color='#3A5F7D', ha='center')
        rotulo(ax, -42, 18, 'OCÉANO\nATLÁNTICO', tam=8.5, color='#3A5F7D', ha='center')
        rotulo(ax, -110, 69, 'OCÉANO GLACIAL ÁRTICO', tam=8, color='#3A5F7D', ha='center')
        nota = 'Elaboración propia con datos de Natural Earth (dominio público; detalle 1:50 millones). Proyección simple.'
    norte(ax, -38, 58, tam=5)
    leyenda(fig, ['rio', 'limite', area(AGUA, 'Lago', alpha=1)], ncol=3, y=0.045)
    nota_fuente(fig, nota)
    guardar(fig, salida, rect=(0, 0.08, 1, 1))


def mapa_hidrovia(geo, salida, ancho=10.5):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    rios = cargar(geo, 'ne_10m_rivers_lake_centerlines_scale_rank')
    fig, ax = lienzo(ancho, ancho * 1.5)
    marco(ax, -66, -50, -36, -14, ticks=False)
    sa = [f for f in paises if f['properties'].get('CONTINENT') == 'South America']
    dibujar_paises(ax, sa, resaltar='Paraguay', borde=0.4)
    for f in rios:
        nombre = f['properties'].get('name')
        for l in lineas(f['geometry']):
            xs, ys = zip(*l)
            if max(xs) < -66 or min(xs) > -50 or max(ys) < -36 or min(ys) > -14:
                continue
            via = False
            if nombre == 'Paraná':
                if es_rio_paraguay(l):
                    pts = [p for p in l if p[1] <= -19.0]
                    if len(pts) > 1:
                        px, py = zip(*pts)
                        ax.plot(px, py, color=ROJO, lw=2.6, zorder=5)
                    via = True
                elif max(ys) <= -27.15 and min(ys) > -34.2:
                    ax.plot(xs, ys, color=ROJO, lw=2.6, zorder=5)
                    via = True
            if not via:
                ax.plot(xs, ys, color=AGUA, lw=0.9, zorder=4)
    ax.annotate('', xy=(-57.68, -16.25), xytext=(-57.66, -18.9), arrowprops=dict(arrowstyle='-|>', color=ROJO, lw=1.6, ls='--'), zorder=6)
    for n, (x, y), ha in [('Cáceres (Brasil)', (-57.68, -16.07), 'left'), ('Corumbá', (-57.65, -19.01), 'left'),
                          ('Asunción', (-57.63, -25.28), 'left'), ('Rosario', (-60.65, -32.95), 'right'),
                          ('Nueva Palmira (Uruguay)', (-58.42, -33.88), 'left')]:
        ax.plot(x, y, 'o', ms=5, color=AZUL, zorder=7)
        rotulo(ax, x + (0.4 if ha == 'left' else -0.4), y, n, tam=8, ha=ha, va='center')
    for x, y, t in ((-64.8, -17.5, 'BOLIVIA'), (-53.5, -18.5, 'BRASIL'), (-64.5, -30.5, 'ARGENTINA'), (-56.0, -32.5, 'URUGUAY')):
        rotulo(ax, x, y, t, tam=8.5, color='#555555', fontweight='bold')
    rotulo(ax, -61.4, -22.3, 'PARAGUAY', tam=9, color='#7A5A2B', fontweight='bold')
    norte(ax, -51.2, -16.0, tam=1)
    escala(ax, -65.5, -35.2, -30, km=300, dy=0.35)
    leyenda(fig, [Line2D([], [], color=ROJO, lw=2.6, label='Hidrovía (recorrido aproximado)'),
                  Line2D([], [], color=ROJO, lw=1.6, ls='--', label='Continúa hasta Cáceres'), 'rio', 'limite', 'ciudad'], ncol=2, y=0.075)
    nota_fuente(fig, 'Elaboración propia con datos de Natural Earth (dominio público). Puertos en posición aproximada.')
    guardar(fig, salida, rect=(0, 0.17, 1, 1))


# ---------------------------------------------------------------- Clase 19
def esquema_clima(salida, ancho=15.0):
    fig, ax = lienzo(ancho, 7.0)
    ax.set_xlim(0, 15); ax.set_ylim(0, 7.0); ax.axis('off')
    caja(ax, 0.1, 6.0, 6.9, 0.8, 'ELEMENTOS DEL CLIMA\n(lo que se mide)', AZUL, tam=8.2)
    caja(ax, 8.0, 6.0, 6.9, 0.8, 'FACTORES DEL CLIMA\n(lo que lo modifica)', AZUL2, tam=8.2)
    elem = ['Temperatura (termómetro, °C)', 'Precipitaciones (pluviómetro, mm)', 'Humedad del aire (higrómetro, %)',
            'Presión atmosférica (barómetro)', 'Vientos (veleta y anemómetro)']
    fact = ['Latitud: cerca del Ecuador hace más calor', 'Altitud: cuanto más alto, más frío',
            'Cercanía al mar: modera la temperatura', 'Relieve: las montañas frenan vientos y lluvias',
            'Corrientes marinas frías o cálidas']
    for k, (e, f) in enumerate(zip(elem, fact)):
        y = 5.2 - k * 1.0
        caja(ax, 0.1, y, 6.9, 0.8, e, '#E6EBF1', color=AZUL, tam=8.2, negrita=False)
        caja(ax, 8.0, y, 6.9, 0.8, f, '#E2EDD9', color='#2E5A1F', tam=8.2, negrita=False)
    flecha(ax, 7.95, 3.6, 7.05, 3.6, color=GRIS, lw=1.6)
    ax.text(7.5, 3.9, 'modifican', ha='center', fontsize=8, color=GRIS, rotation=0)
    guardar(fig, salida, esquema=True)



def esquema_numerado(geo, salida, ancho, zonas, titulo_nota, alto=1.25):
    """Zonas como elipses de color con un número; la descripción va en la leyenda (más legible a tamaño de impresión)."""
    from matplotlib.patches import Patch
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    fig, ax = lienzo(ancho, ancho * alto)
    marco(ax, -170, -25, -58, 84, ticks=False)
    ame = {f['properties'].get('NAME') for f in paises if f['properties'].get('CONTINENT') in ('North America', 'South America')}
    dibujar_paises(ax, paises, borde=0.2, colores={n: '#F1ECE1' for n in ame})
    elems = []
    for k, (cx, cy, w, h, c, t) in enumerate(zonas, 1):
        ax.add_patch(Ellipse((cx, cy), w, h, fc=c, ec='none', alpha=0.6, zorder=3))
        ax.plot(cx, cy, 'o', ms=11, color='white', mec='#333333', mew=0.6, zorder=5)
        ax.text(cx, cy, str(k), ha='center', va='center', fontsize=7.8, fontweight='bold', color='#222222', zorder=6)
        elems.append(Patch(facecolor=c, alpha=0.6, edgecolor='none', label=f'{k}. {t}'))
    ax.axhline(0, color=ROJO, lw=0.9, zorder=2)
    rotulo(ax, -167, 1.5, 'Ecuador', tam=7.6, color=ROJO)
    for lat in (23.44, -23.44):
        ax.axhline(lat, color=OCRE, lw=0.9, ls=(0, (4, 2)), zorder=2)
    ax.plot(-58.4, -23.4, '*', ms=10, color=ROJO, mec='white', zorder=7)
    rotulo(ax, -54, -23.0, 'Paraguay', tam=7.8, color=ROJO, fontweight='bold')
    elems.append(Line2D([], [], color=OCRE, lw=0.9, ls=(0, (4, 2)), label='Trópicos'))
    fig.legend(handles=elems, loc='lower center', bbox_to_anchor=(0.5, 0.05), ncol=2, fontsize=7.2, frameon=False,
               handlelength=1.4, columnspacing=1.0)
    nota_fuente(fig, titulo_nota)
    filas = (len(elems) + 1) // 2
    guardar(fig, salida, rect=(0, 0.07 + 0.033 * filas, 1, 1))


CLIMAS = [(-60, -4, 26, 13, '#3E8E41', 'Ecuatorial: cálido y muy lluvioso'),
          (-46, -15, 14, 10, '#A3C14A', 'Tropical: con estación seca'),
          (-57, -29, 11, 7, '#E8C547', 'Subtropical: inviernos suaves'),
          (-70.5, -24, 4, 14, '#D99A4E', 'Desértico (Atacama) y árido'),
          (-110, 32, 14, 9, '#D99A4E', 'Árido (norte de México)'),
          (-85, 39, 16, 11, '#7FB3D5', 'Templado'),
          (-68, -45, 7, 11, '#9EC5E0', 'Templado frío (Patagonia)'),
          (-105, 58, 40, 10, '#5D6D7E', 'Frío'),
          (-120, 70, 40, 6, '#B0C4DE', 'Polar'),
          (-77, -9, 4, 14, '#8E7CC3', 'De montaña (Andes)')]


def mapa_climas(geo, salida, ancho=11.0):
    esquema_numerado(geo, salida, ancho, CLIMAS, 'Esquema simplificado de la editorial: ubica en forma general los grandes tipos de clima; '
                     'los límites reales son graduales. Países actuales: Natural Earth.', alto=1.45)


def mapa_lluvias_py(geo, salida, ancho=11.0):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    rios = cargar(geo, 'ne_10m_rivers_lake_centerlines_scale_rank')
    fig, ax = lienzo(ancho, ancho * 1.12)
    marco(ax, -63.2, -53.6, -28.4, -18.6, ticks=False)
    dibujar_paises(ax, paises, resaltar='Paraguay')
    rios_caja(ax, rios, (-64, -53, -29, -18), lw=0.9)
    ax.annotate('', xy=(-55.0, -26.0), xytext=(-61.2, -20.6),
                arrowprops=dict(arrowstyle='-|>', color=AZUL2, lw=3.0, alpha=0.8), zorder=6)
    rotulo(ax, -60.2, -20.1, 'menos lluvias:\nunos 400 mm al año', tam=8, color=ROJO, fontweight='bold', ha='center')
    rotulo(ax, -55.6, -27.2, 'más lluvias:\nunos 1.800 mm al año', tam=8, color=AZUL, fontweight='bold', ha='center')
    rotulo(ax, -62.6, -24.9, 'Chaco: más seco y\nmás caluroso en verano', tam=7.8, color='#7A5A2B')
    rotulo(ax, -56.3, -24.3, 'Región Oriental:\nmás húmeda', tam=7.8, color='#7A5A2B')
    ax.axhline(-23.44, color=OCRE, lw=1.0, ls=(0, (4, 2)), zorder=3)
    rotulo(ax, -54.0, -23.25, 'Trópico de Capricornio', tam=7.6, color='#8A6A10', ha='right')
    x, y = CIUDADES_PY['Asunción']
    ax.plot(x, y, '*', ms=9, color=AZUL, mec='white', zorder=7)
    rotulo(ax, x + 0.2, y + 0.2, 'Asunción', tam=8)
    norte(ax, -54.2, -19.9)
    escala(ax, -62.9, -28.0, -24.0)
    leyenda(fig, [Line2D([], [], color=AZUL2, lw=3, label='Las lluvias aumentan hacia el este'), 'rio', 'limite', 'capital'], ncol=2, y=0.075)
    nota_fuente(fig, 'Esquema aproximado: los valores de lluvia anual son redondeados y varían de un año a otro (cotejar con la Dirección '
                     'de Meteorología e Hidrología). Datos geográficos: Natural Earth.')
    guardar(fig, salida, rect=(0, 0.17, 1, 1))


# ---------------------------------------------------------------- Clase 20
REGIONES_AM = [(-62, -5, 24, 12, '#2E7D32', 'Selva tropical (Amazonía)'),
               (-46, -15, 13, 9, '#A3C14A', 'Sabana (Cerrado)'),
               (-61.5, -22.5, 7, 8, '#C8B560', 'Gran Chaco'),
               (-60, -34, 8, 5, '#D7E3A1', 'Pampa (pradera)'),
               (-68, -46, 7, 10, '#C2B280', 'Estepa patagónica'),
               (-70.5, -24, 4, 12, '#D99A4E', 'Desierto de Atacama'),
               (-100, 42, 13, 11, '#D7E3A1', 'Praderas (América del Norte)'),
               (-112, 32, 10, 7, '#D99A4E', 'Desiertos (América del Norte)'),
               (-80, 39, 11, 10, '#6B8E23', 'Bosque templado'),
               (-100, 56, 44, 9, '#355E3B', 'Bosque de coníferas (taiga)'),
               (-115, 68, 44, 5, '#B0C4DE', 'Tundra'),
               (-77, -9, 4, 14, '#8E7CC3', 'Alta montaña (Andes)')]


def mapa_regiones_america(geo, salida, ancho=11.0):
    esquema_numerado(geo, salida, ancho, REGIONES_AM, 'Esquema simplificado de la editorial: ubica en forma general las grandes '
                     'regiones naturales; en la realidad pasan gradualmente de una a otra. Países actuales: Natural Earth.', alto=1.5)


ECO_PY = [('Chaco Seco', (-61.2, -21.4), '#C8B560'), ('Chaco Húmedo', (-59.0, -24.3), '#8FBF7F'),
          ('Pantanal', (-58.6, -20.0), '#7FB3D5'), ('Cerrado', (-56.4, -22.6), '#A3C14A'),
          ('Bosque Atlántico\ndel Alto Paraná', (-55.0, -25.4), '#2E7D32'), ('Humedales\ndel Ñeembucú', (-58.0, -27.0), '#5DADE2')]


def mapa_ecorregiones_py(geo, salida, ancho=12.0, numerado=None):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    rios = cargar(geo, 'ne_10m_rivers_lake_centerlines_scale_rank')
    fig, ax = lienzo(ancho, ancho * 1.12)
    marco(ax, -63.2, -53.6, -28.4, -18.6, ticks=False)
    dibujar_paises(ax, paises, resaltar='Paraguay')
    rios_caja(ax, rios, (-64, -53, -29, -18), lw=0.9)
    elems = ['rio', 'limite']
    for t, (x, y), c in ECO_PY:
        clave = t.split('\n')[0]
        if numerado is not None:
            if clave in numerado:
                ax.plot(x, y, 'o', ms=13, color=AZUL, mec='white', zorder=8)
                ax.text(x, y, str(numerado[clave]), ha='center', va='center', fontsize=9, color='white', fontweight='bold', zorder=9)
            continue
        ax.add_patch(Ellipse((x, y), 1.9, 1.2, fc=c, ec='none', alpha=0.6, zorder=3))
        rotulo(ax, x, y, t, tam=7.8, color='#222222', ha='center', va='center', fontweight='bold')
    for x, y, t in ((-62.4, -19.5, 'BOLIVIA'), (-55.2, -20.0, 'BRASIL'), (-62.2, -27.2, 'ARGENTINA')):
        rotulo(ax, x, y, t, tam=9, color='#555555', fontweight='bold')
    norte(ax, -54.2, -19.9)
    escala(ax, -62.9, -28.0, -24.0)
    leyenda(fig, elems, ncol=2, y=0.05 if numerado is None else 0.1)
    nota_fuente(fig, 'Esquema de ubicación aproximada de grandes ecosistemas: no reproduce los límites oficiales de las ecorregiones '
                     '(consultar el mapa del MADES). Datos geográficos: Natural Earth.')
    guardar(fig, salida, rect=(0, 0.1 if numerado is None else 0.17, 1, 1))


# ---------------------------------------------------------------- Clase 21
def esquema_gestion(salida, ancho=15.0):
    fig, ax = lienzo(ancho, 8.2)
    ax.set_xlim(0, 15); ax.set_ylim(0, 8.2); ax.axis('off')
    caja(ax, 3.5, 7.0, 8.0, 0.95, 'Constitución Nacional (1992), arts. 7 y 8:\nderecho a un ambiente saludable', AZUL, tam=8.4)
    caja(ax, 0.1, 5.0, 4.6, 1.3, 'MADES\nMinisterio del Ambiente y\nDesarrollo Sostenible', AZUL2, tam=8.1)
    caja(ax, 5.2, 5.0, 4.6, 1.3, 'INFONA\nInstituto Forestal\nNacional (bosques)', AZUL2, tam=8.1)
    caja(ax, 10.3, 5.0, 4.6, 1.3, 'Ministerio Público\n(fiscalías ambientales)\ny Poder Judicial', AZUL2, tam=8.1)
    for x in (2.4, 7.5, 12.6):
        flecha(ax, 7.5, 6.95, x, 6.35)
    leyes = ['Ley 294/1993:\nevaluación de\nimpacto ambiental', 'Ley 352/1994:\náreas silvestres\nprotegidas',
             'Ley 716/1996:\ndelitos contra el\nmedio ambiente', 'Ley 2524/2004:\nprohíbe deforestar\nen la R. Oriental']
    for k, t in enumerate(leyes):
        caja(ax, 0.1 + k * 3.72, 2.6, 3.55, 1.5, t, '#E6EBF1', color=AZUL, tam=7.9, negrita=False)
    ax.text(7.5, 4.4, 'Algunas leyes que aplican', ha='center', fontsize=8.2, color=AZUL, fontweight='bold')
    caja(ax, 1.5, 0.4, 12.0, 1.4, 'También participan los gobiernos departamentales y municipales, las organizaciones de la\n'
                                  'sociedad civil, las comunidades indígenas y cada ciudadano.', '#E2EDD9', color='#2E5A1F', tam=8.1,
         negrita=False)
    nota_fuente(fig, 'Esquema simplificado de la editorial; nómina no exhaustiva de leyes vigentes (cotejar en la BACN).')
    guardar(fig, salida, esquema=True, abajo=0.04)


def generar(geo, out):
    os.makedirs(out, exist_ok=True)
    p = lambda n: os.path.join(out, n)  # noqa: E731
    mapa_rios_paraguay(geo, p(reg('fig_18_1_rios_paraguay.png', 13.5)))
    mapa_hidrovia(geo, p(reg('fig_18_2_hidrovia.png', 10.5)))
    mapa_rios_america(geo, p(reg('fig_18_3_rios_america.png', 13.0)))
    mapa_rios_paraguay(geo, p(reg('ficha_18A_mapa_mudo.png', 15.0)), ancho=15.0, mudo=True)
    mapa_rios_paraguay(geo, p(reg('eval_u5_mapa_mudo.png', 12.0)), ancho=12.0, mudo=True)
    mapa_rios_paraguay(geo, p(reg('eval_u5_mapa_clave.png', 12.0)), ancho=12.0)
    mapa_rios_america(geo, p(reg('eval_u5_rios_numerados.png', 9.5)), ancho=9.5, numerado=RIOS_NUMERADOS)
    esquema_clima(p(reg('fig_19_1_clima.png', 15.0)))
    mapa_climas(geo, p(reg('fig_19_2_climas_america.png', 11.0)))
    mapa_lluvias_py(geo, p(reg('fig_19_3_lluvias_py.png', 11.0)))
    mapa_regiones_america(geo, p(reg('fig_20_1_regiones_america.png', 11.0)))
    mapa_ecorregiones_py(geo, p(reg('fig_20_2_ecosistemas_py.png', 12.0)))
    esquema_gestion(p(reg('fig_21_1_gestion.png', 15.0)))
    mapa_rios_paraguay(geo, p(reg('ficha_G_mapa_mudo.png', 15.0)), ancho=15.0, mudo=True)
    mapa_ecorregiones_py(geo, p(reg('eval_u6_mapa.png', 10.0)), ancho=10.0,
                         numerado={'Chaco Seco': 1, 'Bosque Atlántico': 2, 'Humedales': 3})
    mapa_ecorregiones_py(geo, p(reg('eval_u6_mapa_clave.png', 12.0)))
    return ANCHOS


if __name__ == '__main__':
    import sys
    generar(sys.argv[1], sys.argv[2])
