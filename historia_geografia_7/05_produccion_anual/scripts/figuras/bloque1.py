"""Figuras del Bloque I (encuentros 1 a 9).

Los mapas usan geometrías de Natural Earth (dominio público). Las áreas
culturales (guaraníes, mayas, mexicas, incas) son polígonos trazados a mano
por la editorial sobre síntesis históricas generales: son esquemas
aproximados, no límites. Así se declara en cada figura.
"""
import os

from comun import (AGUA, AZUL, AZUL2, GRIS, HALO, OCRE, ROJO, T_NOTA, T_PAIS, T_ROTULO, TIERRA, VERDE, area, caja,
                   cargar, dibujar_paises, dibujar_rios, es_rio_paraguay, escala, flecha, guardar, leyenda, lienzo, lineas,
                   marco, norte, nota_fuente, plt, rotulo, CIUDADES_PY, APA_DESEMBOCADURA)

ANCHOS = {}   # archivo -> ancho de impresión en cm (lo usa el contenido)


def reg(nombre, ancho):
    ANCHOS[nombre] = ancho
    return nombre


# ---------------------------------------------------------------- esquemas y líneas de tiempo
def tipos_fuentes(salida, ancho=15.0):
    fig, ax = lienzo(ancho, 6.2)
    ax.set_xlim(0, 15); ax.set_ylim(0, 6.2); ax.axis('off')
    caja(ax, 5.0, 4.9, 5.0, 1.0, 'FUENTES HISTÓRICAS\nhuellas del pasado', AZUL, tam=9.5)
    tipos = [('Escritas', 'cartas, leyes,\ncrónicas, censos'), ('Materiales', 'herramientas,\nvasijas, edificios'),
             ('Orales', 'relatos, entrevistas,\ncanciones'), ('Iconográficas', 'pinturas, grabados,\nfotografías'),
             ('Cartográficas', 'mapas, planos,\ncroquis')]
    for k, (t, ej) in enumerate(tipos):
        x = 0.1 + k * 3.0
        caja(ax, x, 2.6, 2.8, 0.9, t, AZUL2, tam=8.5)
        ax.text(x + 1.4, 2.4, ej, ha='center', va='top', fontsize=7.8, color='#222222')
        flecha(ax, 7.5, 4.85, x + 1.4, 3.55)
    ax.text(7.5, 0.55, 'Fuentes primarias: producidas en la época que se estudia.\n'
            'Fuentes secundarias: elaboradas después, a partir de otras fuentes.', ha='center', va='center', fontsize=8.2,
            color=AZUL, fontweight='bold')
    guardar(fig, salida, esquema=True)


def eje_tiempo(ax, x0, x1, y=0.0):
    ax.annotate('', xy=(x1, y), xytext=(x0, y), arrowprops=dict(arrowstyle='-|>', color=AZUL, lw=1.6))


def linea_tiempo_era(salida, ancho=16.0):
    """Era cristiana: la escala es proporcional (1 cm del eje = 400 años aprox.)."""
    fig, ax = lienzo(ancho, 5.6)
    x0, x1 = -3200, 2300
    ax.set_xlim(x0, x1); ax.set_ylim(-2.2, 2.6); ax.axis('off')
    eje_tiempo(ax, x0, x1)
    for a in range(-3000, 2001, 500):
        ax.plot([a, a], [-0.12, 0.12], color=AZUL, lw=1 if a % 1000 == 0 else 0.6)
        if a % 1000 == 0 and a != 0:
            ax.text(a, -0.45, f'{-a} a. C.' if a < 0 else f'{a} d. C.', ha='center', fontsize=7.5, color='#222222')
    ax.plot([1, 1], [-0.25, 0.25], color=ROJO, lw=2)
    ax.text(1, -0.95, 'Año 1 d. C.\n(no existe el año 0)', ha='center', fontsize=8, color=ROJO, fontweight='bold')
    ax.text(-1600, 1.75, 'ANTES DE CRISTO (a. C.)\nlos años se cuentan hacia atrás', ha='center', fontsize=8.5, color=AZUL2, fontweight='bold')
    ax.text(1000, 1.75, 'DESPUÉS DE CRISTO (d. C.)\nlos años se cuentan hacia adelante', ha='center', fontsize=8.5, color=AZUL2, fontweight='bold')
    hechos = [(-3000, 'Hacia 3000 a. C.: primeras\nescrituras (Mesopotamia, Egipto)', 0.5, 'left'),
              (1537, '1537: fundación\nde Asunción', 0.5, 'right'), (2026, '2026:\nhoy', 0.5, 'left'),
              (1811, '1811: independencia\ndel Paraguay', -1.5, 'center')]
    for a, t, yy, ha in hechos:
        ax.plot([a, a], [0, yy * 0.8], color=GRIS, lw=0.8)
        ax.text(a + (-25 if ha == 'right' else 25 if ha == 'left' else 0), yy, t, ha=ha,
                va='bottom' if yy > 0 else 'top', fontsize=7.8, color='#222222')
    nota_fuente(fig, 'Esquema propio. Los hechos son ejemplos; la escala del eje es aproximada.')
    guardar(fig, salida, esquema=True, abajo=0.07)


def linea_prehistoria(salida, ancho=16.0):
    fig, ax = lienzo(ancho, 5.0)
    ax.set_xlim(-11, 1.2); ax.set_ylim(-2.3, 2.4); ax.axis('off')
    eje_tiempo(ax, -11, 1.0)
    for k in range(-10, 1, 2):
        ax.plot([k, k], [-0.12, 0.12], color=AZUL, lw=1)
        ax.text(k, -0.48, f'hace {-k}.000 años' if k else 'hoy', ha='center', fontsize=7.5)
    ax.axvspan(-10.5, -2.0, ymin=0.47, ymax=0.53, color=OCRE, alpha=0.5)
    hechos = [(-8.0, 'Hace unos 8.000 años o más:\ncazadores-recolectores en la cuenca\ndel Paraná (sitios fechados sobre todo\nen Misiones y el sur del Brasil)', 0.5),
              (-2.0, 'Hace unos 2.000 años:\nagricultores ceramistas de lengua\ntupí-guaraní en la cuenca\ndel Paraná y del Paraguay', -1.0),
              (-0.5, 'Siglo XVI (hace\nunos 500 años):\nllegan los europeos', 0.5)]
    for x, t, yy in hechos:
        ax.plot([x, x], [0, yy * 0.8], color=GRIS, lw=0.8)
        ax.text(x, yy, t, ha='center', va='bottom' if yy > 0 else 'top', fontsize=7.6, color='#222222')
    nota_fuente(fig, 'Esquema propio con fechas aproximadas de síntesis arqueológicas regionales. Los sitios del Paraguay están poco fechados.')
    guardar(fig, salida, esquema=True, abajo=0.08)


def cronologia_civilizaciones(salida, ancho=16.0):
    fig, ax = lienzo(ancho, 5.6)
    barras = [('Mayas: período clásico', 250, 900, VERDE), ('Mayas: período posclásico', 900, 1540, '#8DB07A'),
              ('Mexicas: de Tenochtitlan a la conquista', 1325, 1521, OCRE), ('Incas: imperio', 1438, 1533, ROJO)]
    for k, (t, a, b, col) in enumerate(barras):
        y = len(barras) - k
        ax.barh(y, b - a, left=a, height=0.55, color=col, edgecolor='#333333', lw=0.6)
        ax.text(b + 15, y, f'{a}-{b}', va='center', fontsize=8, color='#222222')
    ax.set_yticks([len(barras) - k for k in range(len(barras))])
    ax.set_yticklabels([b[0] for b in barras], fontsize=8)
    ax.set_xlim(0, 1850); ax.set_ylim(0.4, len(barras) + 0.9)
    ax.set_xticks(range(0, 1701, 200)); ax.tick_params(axis='x', labelsize=7.5)
    ax.set_xlabel('Años después de Cristo (d. C.)', fontsize=8)
    for sp in ('top', 'right'):
        ax.spines[sp].set_visible(False)
    ax.axvline(1492, color=AZUL, lw=1, ls='--')
    ax.text(1492, len(barras) + 0.55, '1492: llegada de Colón', ha='center', fontsize=7.8, color=AZUL)
    nota_fuente(fig, 'Esquema propio. Fechas aproximadas de uso habitual en la bibliografía; los mayas vivían en la región mucho antes del 250 d. C.')
    guardar(fig, salida, rect=(0, 0.06, 1, 1))


def linea_vacia(salida, ancho=16.0):
    """Eje en blanco de 0 a 1600 d. C. (1 cm = 100 años aprox.) para la Ficha B-2."""
    fig, ax = lienzo(ancho, 6.0)
    ax.set_xlim(-60, 1680); ax.set_ylim(-1.2, 4.2); ax.axis('off')
    eje_tiempo(ax, -40, 1660)
    for a in range(0, 1601, 100):
        ax.plot([a, a], [-0.15, 0.15], color=AZUL, lw=1 if a % 500 == 0 else 0.7)
        ax.text(a, -0.6, str(a), ha='center', fontsize=7.5, color='#222222')
    for y in (1.0, 2.0, 3.0):
        ax.plot([0, 1600], [y, y], color='#BBBBBB', lw=0.6, ls=(0, (2, 3)))
    ax.text(800, 3.8, 'Años después de Cristo (d. C.) · 1 división = 100 años', ha='center', fontsize=8, color=AZUL)
    guardar(fig, salida, esquema=True)


def esquema_aldea(salida, ancho=15.0):
    fig, ax = lienzo(ancho, 6.6)
    ax.set_xlim(0, 15); ax.set_ylim(0.2, 6.75); ax.axis('off')
    caja(ax, 4.3, 5.7, 6.4, 1.0, 'TEKOHA: territorio donde se vive\nsegún el modo de ser guaraní (teko)', AZUL, tam=8.2)
    caja(ax, 4.3, 4.1, 6.4, 1.0, 'Aldea: varias casas comunales\nalrededor de un espacio abierto', AZUL2, tam=8.2)
    caja(ax, 4.3, 2.5, 6.4, 1.0, 'Casa comunal: una familia extensa\n(abuelos, hijos, yernos, nietos)', AZUL2, tam=8.2)
    flecha(ax, 7.5, 5.65, 7.5, 5.15); flecha(ax, 7.5, 4.05, 7.5, 3.55)
    caja(ax, 0.05, 4.1, 4.0, 1.0, 'Mburuvicha: líder por\nprestigio y generosidad', '#E6EBF1', color=AZUL, tam=8.0)
    caja(ax, 10.95, 4.1, 4.0, 1.0, 'Paje: guía religioso\n(cantos, sueños, curación)', '#E6EBF1', color=AZUL, tam=8.0)
    caja(ax, 0.05, 0.35, 14.9, 1.3, 'Jopói (reciprocidad): se da con la mano abierta y se recibe del mismo modo.\n'
         'Quien cosecha o caza mucho comparte; compartir da prestigio y crea obligaciones entre parientes.', '#FFF8E1',
         color='#222222', tam=8.0, negrita=False)
    nota_fuente(fig, 'Esquema propio a partir de síntesis etnohistóricas (por ejemplo, B. Melià). Simplificado: hubo variaciones entre grupos.')
    guardar(fig, salida, esquema=True, abajo=0.03)


# ---------------------------------------------------------------- mapas
def mapa_orientacion_py(geo, salida, ancho=12.0):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    rios = cargar(geo, 'ne_10m_rivers_lake_centerlines_scale_rank')
    fig, ax = lienzo(ancho, 13.0)
    marco(ax, -63.0, -53.8, -28.3, -18.8)
    dibujar_paises(ax, paises, resaltar='Paraguay')
    dibujar_rios(ax, rios, (-64, -53, -29, -18), nombres=('Paraná', 'Pilcomayo', 'Paraguay', 'Verde', 'Tebicuary', 'Jejuí Guazú'))
    for n in ('Asunción', 'Concepción', 'Encarnación', 'Ciudad del Este', 'Filadelfia'):
        x, y = CIUDADES_PY[n]
        ax.plot(x, y, 'o', ms=4.5, color=AZUL, zorder=6)
        dx, ha = (-0.18, 'right') if n in ('Ciudad del Este',) else (0.18, 'left')
        rotulo(ax, x + dx, y + 0.12, n, ha=ha)
    rotulo(ax, -61.9, -19.6, 'BOLIVIA', tam=T_PAIS, color='#555555', fontweight='bold')
    rotulo(ax, -55.3, -20.2, 'BRASIL', tam=T_PAIS, color='#555555', fontweight='bold')
    rotulo(ax, -62.4, -26.9, 'ARGENTINA', tam=T_PAIS, color='#555555', fontweight='bold')
    rotulo(ax, -60.9, -21.7, 'PARAGUAY', tam=10, color='#7A5A2B', fontweight='bold')
    # rosa de los vientos
    cx, cy, r = -55.2, -27.0, 0.55
    for dx, dy, t in ((0, 1, 'N'), (0, -1, 'S'), (1, 0, 'E'), (-1, 0, 'O')):
        ax.annotate('', xy=(cx + dx * r, cy + dy * r), xytext=(cx, cy), arrowprops=dict(arrowstyle='-|>', color=AZUL, lw=1.1))
        ax.text(cx + dx * (r + 0.25), cy + dy * (r + 0.25), t, ha='center', va='center', fontsize=8.5, color=AZUL, fontweight='bold')
    escala(ax, -62.7, -27.9, -24.0)
    leyenda(fig, ['rio', 'limite', 'ciudad'])
    nota_fuente(fig, 'Mapa aproximado. Elaboración propia con datos de Natural Earth (dominio público). Ciudades en posición aproximada.')
    guardar(fig, salida, rect=(0, 0.07, 1, 1))


def mapa_regiones_py(geo, salida, ancho=11.0, rotulado=True):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    rios = cargar(geo, 'ne_10m_rivers_lake_centerlines_scale_rank')
    fig, ax = lienzo(ancho, ancho * 1.12)
    marco(ax, -63.0, -53.8, -28.3, -18.8)
    dibujar_paises(ax, paises, resaltar='Paraguay')
    dibujar_rios(ax, rios, (-64, -53, -29, -18), nombres=('Paraná', 'Pilcomayo', 'Paraguay'), ancho=1.3)
    if rotulado:
        rotulo(ax, -61.4, -22.2, 'REGIÓN\nOCCIDENTAL\n(Chaco)', tam=9, color='#7A5A2B', fontweight='bold', ha='center')
        rotulo(ax, -56.3, -24.6, 'REGIÓN\nORIENTAL', tam=9, color='#7A5A2B', fontweight='bold', ha='center')
        rotulo(ax, -57.9, -21.6, 'Río Paraguay', tam=8, rotation=-80, ha='center', fontstyle='italic')
        rotulo(ax, -60.6, -24.55, 'Río Pilcomayo', tam=8, rotation=-30, ha='center', fontstyle='italic')
    escala(ax, -62.7, -27.9, -24.0)
    norte(ax, -54.4, -20.0)
    leyenda(fig, ['rio', 'limite'])
    nota_fuente(fig, 'Mapa aproximado. Elaboración propia con datos de Natural Earth (dominio público).')
    guardar(fig, salida, rect=(0, 0.07, 1, 1))


def mapa_guarani(geo, salida, ancho=11.5):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    rios = cargar(geo, 'ne_10m_rivers_lake_centerlines_scale_rank')
    fig, ax = lienzo(ancho, 12.5)
    marco(ax, -66.0, -46.5, -35.5, -16.0)
    dibujar_paises(ax, paises)
    dibujar_rios(ax, rios, (-67, -46, -36, -15), nombres=('Paraná', 'Paraguay', 'Uruguay', 'Pilcomayo', 'Iguaçu', 'Paranapanema'))
    guarani = [(-57.9, -20.8), (-55.0, -21.4), (-52.0, -22.4), (-48.5, -25.0), (-48.6, -28.5), (-50.5, -31.5), (-53.0, -33.3),
               (-56.0, -32.4), (-58.3, -34.0), (-59.1, -32.5), (-59.5, -30.0), (-58.7, -27.4), (-57.8, -25.4), (-57.6, -23.0)]
    chiriguano = [(-64.2, -18.4), (-62.9, -18.4), (-62.7, -22.2), (-64.2, -22.2)]
    for pol in (guarani, chiriguano):
        xs, ys = zip(*pol)
        ax.fill(xs, ys, color='#4E7D3A', alpha=0.35, zorder=3)
        ax.plot(list(xs) + [xs[0]], list(ys) + [ys[0]], color='#2E5A1F', lw=1.0, zorder=3)
    for x, y, t in ((-57.63, -25.28, 'carios\n(Asunción)'), (-56.6, -21.2, 'itatines'), (-52.6, -24.2, 'guaireños\n(Guairá)'),
                    (-63.5, -20.3, 'chiriguanos'), (-55.4, -28.8, 'tapes')):
        rotulo(ax, x, y, t, tam=8, ha='center', color='#1E3D14', fontweight='bold')
    for x, y, t in ((-63.5, -26.5, 'ARGENTINA'), (-51.0, -19.0, 'BRASIL'), (-64.5, -17.0, 'BOLIVIA'), (-56.2, -33.8, 'URUGUAY'),
                    (-60.8, -23.6, 'PARAGUAY')):
        rotulo(ax, x, y, t, tam=8.5, color='#555555', fontweight='bold', ha='center')
    escala(ax, -65.5, -34.8, -28.0, km=400, dy=0.35)
    norte(ax, -47.6, -17.6, tam=1.0)
    leyenda(fig, [area('#4E7D3A', 'Área aproximada de pueblos guaraníes hacia 1500', alpha=0.35), 'rio', 'limite'], ncol=2)
    nota_fuente(fig, 'Esquema aproximado sobre síntesis etnohistóricas; no marca límites. Países actuales como referencia. Datos: Natural Earth.')
    guardar(fig, salida, rect=(0, 0.11, 1, 1))


def mapa_poblamiento(geo, salida, ancho=12.0):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    fig, ax = lienzo(ancho, 15.0)
    marco(ax, -180, -25, -58, 72, ticks=False)
    dibujar_paises(ax, paises, borde=0.3)
    # Beringia (puente de tierra) y rutas
    ax.fill([-180, -158, -158, -180], [62, 62, 68, 68], color=OCRE, alpha=0.45, zorder=3)
    rotulo(ax, -166, 69.5, 'Beringia', tam=8.5, ha='center', fontweight='bold')
    costa = [(-165, 62), (-150, 58), (-135, 55), (-125, 45), (-118, 32), (-108, 22), (-95, 14), (-82, 6), (-80, -3), (-79, -12),
             (-73, -25), (-74, -40)]
    interior = [(-160, 64), (-140, 63), (-120, 58), (-113, 50), (-105, 40), (-100, 30)]
    for pts, ls in ((costa, '-'), (interior, (0, (3, 1.5)))):
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color=ROJO, lw=1.8, ls=ls, zorder=5)
        ax.annotate('', xy=pts[-1], xytext=pts[-2], arrowprops=dict(arrowstyle='-|>', color=ROJO, lw=1.6), zorder=5)
    sitios = [('Monte Verde (Chile)', -73.2, -41.5, 'left', 0), ('Clovis (EE. UU.)', -103.3, 34.3, 'left', 3),
              ('White Sands (EE. UU.)', -106.3, 32.8, 'right', -3), ('Cueva Fell (Chile)', -70.0, -52.0, 'left', 0)]
    for t, x, y, ha, dy in sitios:
        ax.plot(x, y, 'D', ms=5.5, color=ROJO, mec='white', zorder=7)
        rotulo(ax, x + (2.5 if ha == 'left' else -2.5), y + dy, t, tam=8, ha=ha, va='center')
    rotulo(ax, -160, 20, 'OCÉANO\nPACÍFICO', tam=8.5, color='#3A5F7D', ha='center')
    rotulo(ax, -40, 25, 'OCÉANO\nATLÁNTICO', tam=8.5, color='#3A5F7D', ha='center')
    leyenda(fig, ['sitio', simbolo_ruta('Ruta costera (Pacífico)'), simbolo_ruta('Ruta por el interior', discontinua=True),
                  area(OCRE, 'Beringia (tierra emergida)', alpha=0.45)], ncol=2)
    nota_fuente(fig, 'Esquema aproximado de rutas propuestas; no son caminos documentados. Países actuales: Natural Earth.')
    guardar(fig, salida, rect=(0, 0.09, 1, 1))


def simbolo_ruta(texto, discontinua=False):
    from matplotlib.lines import Line2D
    return Line2D([], [], color=ROJO, lw=1.8, ls=(0, (3, 1.5)) if discontinua else '-', label=texto)


AREAS = {
    'maya': [(-92.5, 21.5), (-86.8, 21.6), (-87.5, 15.8), (-88.5, 13.6), (-90.5, 13.8), (-92.3, 14.5), (-94.0, 16.0), (-93.5, 18.5)],
    'mexica': [(-101.5, 21.0), (-97.2, 21.6), (-95.8, 18.6), (-94.6, 17.2), (-92.3, 14.7), (-93.6, 15.8), (-98.5, 16.4),
               (-101.6, 17.8), (-102.0, 19.6)],
    'inca': [(-78.0, 1.4), (-80.4, -2.5), (-81.2, -6.0), (-79.0, -8.5), (-76.4, -14.0), (-70.4, -18.5), (-70.2, -24.0),
             (-71.4, -30.0), (-72.2, -35.3), (-70.4, -35.3), (-69.4, -31.0), (-67.0, -28.0), (-65.0, -24.0), (-64.2, -21.0),
             (-65.4, -17.5), (-68.4, -14.5), (-71.4, -11.0), (-74.0, -7.0), (-76.4, -3.0), (-77.0, 0.5)],
}
COLORES_AREA = {'maya': VERDE, 'mexica': OCRE, 'inca': ROJO}
CAPITALES = {'Tenochtitlan': (-99.13, 19.43), 'Cuzco': (-71.97, -13.53), 'Tikal': (-89.62, 17.22),
             'Chichén Itzá': (-88.57, 20.68)}


def mapa_civilizaciones(geo, salida, ancho=12.0, numerado=None, mudo=False):
    """numerado: {lugar: número} para la evaluación; mudo: sin áreas ni rótulos."""
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    fig, ax = lienzo(ancho, ancho * 1.2)
    marco(ax, -118, -32, -40, 34, ticks=False)
    dibujar_paises(ax, paises, borde=0.3)
    if not mudo:
        for k, pol in AREAS.items():
            xs, ys = zip(*pol)
            ax.fill(xs, ys, color=COLORES_AREA[k], alpha=0.45, zorder=3)
            ax.plot(list(xs) + [xs[0]], list(ys) + [ys[0]], color='#333333', lw=0.7, zorder=3)
    lugares = numerado or ({} if mudo else {k: None for k in CAPITALES})
    for t, num in lugares.items():
        x, y = CAPITALES[t]
        if num is None:
            ax.plot(x, y, '*' if t in ('Tenochtitlan', 'Cuzco') else 'o', ms=9 if t in ('Tenochtitlan', 'Cuzco') else 4.5,
                    color=AZUL, zorder=7)
            dx = {'Tenochtitlan': (-1.0, 'right'), 'Cuzco': (1.2, 'left'), 'Tikal': (1.0, 'left'), 'Chichén Itzá': (1.0, 'left')}[t]
            rotulo(ax, x + dx[0], y, t, tam=8.2, ha=dx[1], va='center')
        else:
            ax.plot(x, y, 'o', ms=12, color=AZUL, mec='white', zorder=7)
            ax.text(x, y, str(num), ha='center', va='center', fontsize=8.5, color='white', fontweight='bold', zorder=8)
    rotulo(ax, -110, -10, 'OCÉANO\nPACÍFICO', tam=8.5, color='#3A5F7D', ha='center')
    rotulo(ax, -45, 15, 'OCÉANO\nATLÁNTICO', tam=8.5, color='#3A5F7D', ha='center')
    norte(ax, -36, 27, tam=3.0)
    elems = []
    if not mudo:
        elems = [area(VERDE, 'Mayas', alpha=0.45), area(OCRE, 'Mexicas (hacia 1519)', alpha=0.45),
                 area(ROJO, 'Incas (hacia 1530)', alpha=0.45)]
        if not numerado:
            elems += ['capital', 'ciudad']
    elems += ['limite']
    leyenda(fig, elems, ncol=3)
    nota_fuente(fig, 'Áreas aproximadas trazadas por la editorial; no son límites. Países actuales como referencia: Natural Earth.')
    guardar(fig, salida, rect=(0, 0.09, 1, 1))


def generar(geo, out):
    os.makedirs(out, exist_ok=True)
    p = lambda n: os.path.join(out, n)  # noqa: E731
    tipos_fuentes(p(reg('fig_1_1_tipos_fuentes.png', 15.0)))
    linea_tiempo_era(p(reg('fig_1_2_linea_tiempo_era.png', 16.0)))
    mapa_orientacion_py(geo, p(reg('fig_1_3_mapa_orientacion.png', 12.0)))
    linea_prehistoria(p(reg('fig_2_1_linea_prehistoria.png', 16.0)))
    mapa_regiones_py(geo, p(reg('fig_2_2_regiones.png', 11.0)))
    mapa_guarani(geo, p(reg('fig_3_1_area_guarani.png', 11.5)))
    esquema_aldea(p(reg('fig_3_2_aldea.png', 15.0)))
    mapa_poblamiento(geo, p(reg('fig_4_1_poblamiento.png', 12.0)))
    mapa_civilizaciones(geo, p(reg('fig_5_1_civilizaciones.png', 12.0)))
    cronologia_civilizaciones(p(reg('fig_5_2_cronologia.png', 16.0)))
    # Continuación B y evaluaciones
    mapa_civilizaciones(geo, p(reg('ficha_B_mapa_mudo_america.png', 15.0)), ancho=15.0, mudo=True)
    linea_vacia(p(reg('ficha_B_linea_vacia.png', 16.0)))
    mapa_regiones_py(geo, p(reg('eval_u1_mapa.png', 9.0)), ancho=9.0, rotulado=False)
    mapa_regiones_py(geo, p(reg('eval_u1_mapa_clave.png', 9.0)), ancho=9.0, rotulado=True)
    mapa_civilizaciones(geo, p(reg('eval_u2_mapa.png', 10.0)), ancho=10.0, numerado={'Tenochtitlan': 1, 'Tikal': 2, 'Cuzco': 3}, mudo=True)
    mapa_civilizaciones(geo, p(reg('eval_u2_mapa_clave.png', 10.0)), ancho=10.0)
    return ANCHOS


if __name__ == '__main__':
    import sys
    generar(sys.argv[1], sys.argv[2])
