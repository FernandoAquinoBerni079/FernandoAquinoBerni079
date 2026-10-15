"""Figuras del Bloque II (encuentros 10 a 18).

Las rutas de los viajes son trazados aproximados de la editorial sobre
síntesis históricas generales: indican el recorrido general, no la derrota
exacta. Las figuras 10.1 y 10.2 parten de las aprobadas en la muestra 3 y se
dibujan al tamaño de impresión (A17).
"""
import os

from matplotlib.lines import Line2D

from comun import (AGUA, AZUL, AZUL2, GRIS, OCRE, ROJO, VERDE, T_PAIS, area, caja, cargar, dibujar_paises, dibujar_rios,
                   escala, flecha, guardar, leyenda, lienzo, marco, norte, nota_fuente, rotulo, CIUDADES_PY)

ANCHOS = {}


def reg(nombre, ancho):
    ANCHOS[nombre] = ancho
    return nombre


def ruta(ax, pts, color, ls='-', lw=1.7, flecha_final=True):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, zorder=5, solid_capstyle='round')
    if flecha_final:
        ax.annotate('', xy=pts[-1], xytext=pts[-2], arrowprops=dict(arrowstyle='-|>', color=color, lw=lw), zorder=5)


def simbolo(color, texto, ls='-'):
    return Line2D([], [], color=color, lw=1.8, ls=ls, label=texto)


# ---------------------------------------------------------------- Clase 6
def mapa_viajes(geo, salida, ancho=16.0):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    fig, ax = lienzo(ancho, 10.5)
    marco(ax, -180, 180, -62, 62, ticks=False)
    dibujar_paises(ax, paises, borde=0.25)
    colon = [(-6.9, 37.2), (-15.4, 28.1), (-40, 26), (-74.5, 24.1)]
    dias = [(-9.1, 38.7), (-17, 15), (-12, -5), (8, -25), (18.5, -34.4)]
    gama = [(-9.1, 38.7), (-17, 15), (-20, -15), (18.5, -36), (40.5, -15), (40, -3), (60, 12), (75.8, 11.2)]
    magallanes = [(-6.4, 36.8), (-25, 5), (-38, -15), (-57.5, -35), (-68, -52.5), (-75, -51), (-110, -25), (-150, 5),
                  (145, 13.5), (124, 10), (127.5, 0.5), (100, -12), (60, -32), (18.5, -36), (0, -10), (-20, 15), (-6.4, 36.8)]
    ruta(ax, colon, ROJO)
    ruta(ax, dias, VERDE, ls=(0, (3, 1.5)))
    ruta(ax, gama, VERDE)
    xs, ys = zip(*magallanes)
    corte = 8   # el tramo del Pacífico cruza el borde del mapa en 180°
    ax.plot(xs[:corte], ys[:corte], color=AZUL, lw=1.6, zorder=5)
    ax.plot([-150, -180], [5, 8.5], color=AZUL, lw=1.6, zorder=5)
    ax.plot([180] + list(xs[corte:]), [8.5] + list(ys[corte:]), color=AZUL, lw=1.6, zorder=5)
    rotulo(ax, -45, 31, 'Colón, 1492', tam=8, color=ROJO, fontweight='bold')
    rotulo(ax, -5, -20, 'Dias,\n1487-1488', tam=8, color=VERDE, fontweight='bold', ha='center')
    rotulo(ax, 52, 2, 'Vasco da Gama,\n1497-1498', tam=8, color=VERDE, fontweight='bold', ha='center')
    rotulo(ax, -120, -36, 'Magallanes y Elcano,\n1519-1522', tam=8, color=AZUL, fontweight='bold', ha='center')
    for x, y, t in ((-9.1, 38.7, 'Lisboa'), (-6.0, 37.0, 'Sevilla'), (75.8, 11.2, 'Calicut (India)')):
        ax.plot(x, y, 'o', ms=4, color='#333333', zorder=6)
    rotulo(ax, 66, 17, 'Calicut', tam=7.5, ha='right')
    rotulo(ax, -150, 40, 'OCÉANO PACÍFICO', tam=8, color='#3A5F7D', ha='center')
    rotulo(ax, -38, 45, 'OCÉANO\nATLÁNTICO', tam=8, color='#3A5F7D', ha='center')
    rotulo(ax, 78, -32, 'OCÉANO ÍNDICO', tam=8, color='#3A5F7D', ha='center')
    leyenda(fig, [simbolo(ROJO, 'Colón (Castilla), 1492'), simbolo(VERDE, 'Dias (Portugal), 1487-1488', (0, (3, 1.5))),
                  simbolo(VERDE, 'Vasco da Gama (Portugal), 1497-1498'), simbolo(AZUL, 'Magallanes y Elcano (Castilla), 1519-1522')], ncol=2)
    nota_fuente(fig, 'Trazados aproximados de la editorial: muestran el recorrido general, no la derrota exacta. Países actuales: Natural Earth.')
    guardar(fig, salida, rect=(0, 0.1, 1, 1))


def esquema_navegacion(salida, ancho=15.0):
    fig, ax = lienzo(ancho, 6.0)
    ax.set_xlim(0, 15); ax.set_ylim(0, 6.0); ax.axis('off')
    caja(ax, 4.5, 4.8, 6.0, 0.9, 'NAVEGAR MAR ADENTRO\ny volver con seguridad', AZUL, tam=8.8)
    items = [('Carabela', 'barco liviano con velas\nlatinas y cuadradas'), ('Brújula', 'indica el norte aun\nsin ver la costa'),
             ('Astrolabio y\ncuadrante', 'miden la altura de las\nestrellas: latitud'), ('Cartas náuticas', 'mapas de costas,\npuertos y rumbos'),
             ('Imprenta', 'difunde mapas, relatos\ny conocimientos')]
    for k, (t, d) in enumerate(items):
        x = 0.1 + k * 3.0
        caja(ax, x, 2.6, 2.8, 1.0, t, AZUL2, tam=8.3)
        ax.text(x + 1.4, 2.4, d, ha='center', va='top', fontsize=7.8, color='#222222')
        flecha(ax, x + 1.4, 3.65, 7.5, 4.75)
    ax.text(7.5, 0.35, 'Muchos de estos inventos venían de otros pueblos (la brújula, de China; el astrolabio, perfeccionado\n'
            'por sabios árabes y judíos) y los navegantes europeos los combinaron y mejoraron.', ha='center', fontsize=7.8, color=AZUL)
    guardar(fig, salida, esquema=True)


# ---------------------------------------------------------------- Clase 7
def mapa_tordesillas(geo, salida, ancho=12.0):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    fig, ax = lienzo(ancho, 12.5)
    marco(ax, -110, 25, -58, 45, ticks=False)
    dibujar_paises(ax, paises, borde=0.25)
    lon = -46.6
    ax.axvspan(-110, lon, color=OCRE, alpha=0.12, zorder=0)
    ax.axvspan(lon, 25, color=VERDE, alpha=0.12, zorder=0)
    ax.plot([lon, lon], [-58, 45], color=ROJO, lw=2.0, zorder=6)
    ax.plot(-24.0, 15.5, 'o', ms=5, color='#333333', zorder=6)
    rotulo(ax, -22.5, 17.5, 'Islas de Cabo Verde', tam=8.0)
    ax.annotate('', xy=(lon, 9), xytext=(-24.0, 9), arrowprops=dict(arrowstyle='<->', color=ROJO, lw=1.2))
    rotulo(ax, -35.5, 10.5, '370 leguas', tam=8, color=ROJO, ha='center', fontweight='bold')
    rotulo(ax, -80, 36, 'PARA CASTILLA\n(al oeste de la línea)', tam=8.5, color='#6B4A12', ha='center', fontweight='bold')
    rotulo(ax, -12, 36, 'PARA PORTUGAL\n(al este)', tam=8.5, color='#2E5A1F', ha='center', fontweight='bold')
    rotulo(ax, lon + 1, -50, 'Línea de\nTordesillas (1494)', tam=8, color=ROJO)
    norte(ax, 18, 36, tam=4)
    leyenda(fig, [simbolo(ROJO, 'Meridiano de Tordesillas (aprox. 46° O)'), area(OCRE, 'Zona asignada a Castilla', alpha=0.25),
                  area(VERDE, 'Zona asignada a Portugal', alpha=0.25), 'limite'], ncol=2)
    nota_fuente(fig, 'Esquema aproximado: la ubicación exacta de la línea se discutió durante siglos. Países actuales: Natural Earth.')
    guardar(fig, salida, rect=(0, 0.1, 1, 1))


def esquema_gobierno(salida, ancho=15.0):
    fig, ax = lienzo(ancho, 8.6)
    ax.set_xlim(0, 15); ax.set_ylim(0, 8.6); ax.axis('off')
    ax.text(0.1, 8.3, 'EN ESPAÑA', fontsize=8, color=GRIS, fontweight='bold')
    ax.text(0.1, 5.4, 'EN AMÉRICA', fontsize=8, color=GRIS, fontweight='bold')
    ax.plot([0, 15], [5.7, 5.7], color='#BBBBBB', lw=0.8, ls='--')
    caja(ax, 5.35, 7.1, 4.3, 0.95, 'EL REY\n(monarquía absoluta)', AZUL, tam=8.4)
    caja(ax, 0.1, 6.2, 4.9, 0.95, 'Consejo de Indias (1524):\nleyes y nombramientos', AZUL2, tam=8.0)
    caja(ax, 10.0, 6.2, 4.9, 0.95, 'Casa de Contratación (1503):\ncomercio y navegación', AZUL2, tam=8.0)
    flecha(ax, 5.35, 7.4, 5.0, 6.9); flecha(ax, 9.65, 7.4, 10.0, 6.9)
    caja(ax, 0.1, 4.0, 4.9, 1.0, 'Virreyes: Nueva España\n(1535) y Perú (1542)', AZUL2, tam=8.0)
    caja(ax, 5.05, 4.0, 4.9, 1.0, 'Audiencias: tribunales\n(Charcas, 1559)', AZUL2, tam=8.0)
    caja(ax, 10.0, 4.0, 4.9, 1.0, 'Gobernadores y\ncapitanes generales', AZUL2, tam=8.0)
    flecha(ax, 7.5, 7.05, 2.55, 5.05); flecha(ax, 7.5, 7.05, 7.5, 5.05); flecha(ax, 7.5, 7.05, 12.45, 5.05)
    caja(ax, 2.3, 2.0, 5.0, 1.0, 'Cabildos de españoles\n(gobierno de cada ciudad)', '#E6EBF1', color=AZUL, tam=8.0)
    caja(ax, 7.7, 2.0, 5.0, 1.0, 'Caciques y cabildos de indios\n(pueblos indígenas)', '#E6EBF1', color=AZUL, tam=8.0)
    flecha(ax, 12.45, 3.95, 4.8, 3.05); flecha(ax, 12.45, 3.95, 10.2, 3.05)
    ax.text(7.5, 0.95, 'El Paraguay formó parte del Virreinato del Perú,\ncon capital en Lima, desde su creación en 1542.',
            ha='center', va='center', fontsize=8, color=AZUL, fontweight='bold')
    nota_fuente(fig, 'Esquema simplificado de la editorial: las fechas son las de creación de cada institución.')
    guardar(fig, salida, esquema=True, abajo=0.04)


# ---------------------------------------------------------------- Clase 8 y Continuación C
RUTAS_PLATA = {
    'solis': [(-50, -33), (-55.0, -34.8), (-57.6, -34.6)],
    'garcia': [(-48.6, -27.4), (-51.5, -26.0), (-54.5, -25.3), (-57.4, -24.8), (-60.0, -21.5), (-62.5, -20.0), (-64.8, -19.8)],
    'gaboto': [(-56.5, -34.9), (-58.4, -33.9), (-60.7, -32.6), (-60.5, -31.0), (-59.7, -28.5), (-58.6, -27.4), (-58.0, -26.0)],
    'mendoza_ayolas': [(-58.4, -34.6), (-60.7, -32.6), (-59.7, -28.5), (-58.6, -27.4), (-57.6, -25.3), (-57.6, -23.4), (-57.9, -21.0)],
}
LUGARES_PLATA = {'Buenos Aires (1536)': (-58.38, -34.6), 'Sancti Spiritus (1527)': (-60.75, -32.6),
                 'Asunción (1537)': (-57.63, -25.28), 'Isla de Santa Catalina': (-48.55, -27.6), 'Potosí (Charcas)': (-65.75, -19.6)}


def mapa_rutas_plata(geo, salida, ancho=12.0, mudo=False, numerado=None):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    rios = cargar(geo, 'ne_10m_rivers_lake_centerlines_scale_rank')
    # AN-01: con la leyenda de rutas (cuatro filas) se reserva más alto y una franja inferior libre para la escala;
    # el mapa mudo de la Ficha C conserva las medidas de 88a0970 (su leyenda es de una fila).
    fig, ax = lienzo(ancho, ancho * (1.08 if mudo else 1.28))
    marco(ax, -68.5, -46.0, -36.5 if mudo else -37.7, -16.5, ticks=False)
    dibujar_paises(ax, paises, borde=0.4)
    dibujar_rios(ax, rios, (-70, -45, -37, -15), nombres=('Paraná', 'Pilcomayo', 'Uruguay', 'Bermejo', 'Salado'))
    elems = []
    if not mudo:
        estilos = {'solis': (OCRE, '-', 'Solís, 1516'), 'garcia': (ROJO, (0, (3, 1.5)), 'Alejo García, hacia 1524'),
                   'gaboto': (VERDE, '-', 'Gaboto, 1526-1530'), 'mendoza_ayolas': (AZUL, '-', 'Mendoza y Ayolas, 1536-1537')}
        for k, pts in RUTAS_PLATA.items():
            c, ls, t = estilos[k]
            ruta(ax, pts, c, ls=ls)
            elems.append(simbolo(c, t, ls))
    lugares = numerado or ({} if mudo else {k: None for k in LUGARES_PLATA})
    for t, num in lugares.items():
        x, y = LUGARES_PLATA[t]
        if num is None:
            ax.plot(x, y, 'o', ms=4.5, color='#222222', zorder=7)
            ha = 'left' if t not in ('Buenos Aires (1536)', 'Sancti Spiritus (1527)', 'Isla de Santa Catalina') else 'right'
            rotulo(ax, x + (0.4 if ha == 'left' else -0.4), y + 0.25, t, tam=8, ha=ha)
        else:
            ax.plot(x, y, 'o', ms=12, color=AZUL, mec='white', zorder=7)
            ax.text(x, y, str(num), ha='center', va='center', fontsize=8.5, color='white', fontweight='bold', zorder=8)
    for x, y, t in ((-63.5, -26.0, 'ARGENTINA'), (-51.5, -20.0, 'BRASIL'), (-65.5, -17.5, 'BOLIVIA'), (-60.8, -22.5, 'PARAGUAY'),
                    (-56.0, -32.7, 'URUGUAY')):
        rotulo(ax, x, y, t, tam=8, color='#555555', fontweight='bold', ha='center')
    rotulo(ax, -49.5, -32.5, 'OCÉANO\nATLÁNTICO', tam=8, color='#3A5F7D', ha='center')
    escala(ax, -67.8, -35.6 if mudo else -36.75, -30, km=300, dy=0.3)
    norte(ax, -47.3, -18.5, tam=1.0)
    leyenda(fig, elems + ['rio', 'limite'] + (['ciudad'] if not mudo and not numerado else []), ncol=2)
    nota_fuente(fig, 'Recorridos aproximados de la editorial; países actuales solo como referencia. Datos: Natural Earth.')
    guardar(fig, salida, rect=(0, 0.12 if mudo else 0.2, 1, 1))


HITOS_PLATA = [(1516, 'Solís llega al Río de la Plata y muere en la costa'), (1524, 'Alejo García llega a la frontera inca (año aproximado)'),
               (1527, 'Gaboto levanta el fuerte de Sancti Spiritus'), (1536, 'Pedro de Mendoza funda Buenos Aires'),
               (1537, 'Salazar y Espinosa levanta una casa fuerte: Asunción'), (1539, 'Irala queda al frente de la provincia'),
               (1541, 'Se despuebla Buenos Aires; se crea el Cabildo de Asunción')]
HITOS_1534 = [(1534, 'Capitulación de Pedro de Mendoza'), (1536, 'Fundación de Buenos Aires'),
              (1537, 'Fundación de Asunción (15 de agosto)'), (1537, 'Real Provisión (12 de septiembre)'),
              (1539, 'Irala queda al frente de la provincia'), (1541, 'Cabildo de Asunción; se despuebla Buenos Aires'),
              (1542, 'Llega Cabeza de Vaca'), (1544, 'Cabeza de Vaca es depuesto'), (1547, 'Se crea el Obispado'),
              (1556, 'Reparto de encomiendas')]


def linea_vertical(salida, hitos, ancho=11.5):
    n = len(hitos)
    fig, ax = lienzo(ancho, 0.78 * n + 0.6)
    ax.set_xlim(0, 10); ax.set_ylim(-0.6, n - 0.4); ax.axis('off')
    ax.plot([1.55, 1.55], [-0.3, n - 0.7], color=AZUL, lw=2)
    for k, (anio, texto) in enumerate(hitos):
        y = n - 1 - k
        ax.text(1.25, y, str(anio), ha='right', va='center', fontsize=9, fontweight='bold', color=AZUL)
        ax.plot(1.55, y, 'o', ms=6, color=OCRE, zorder=5)
        ax.text(1.9, y, texto, ha='left', va='center', fontsize=8.8, color='#222222')
    guardar(fig, salida, esquema=True)


# ---------------------------------------------------------------- Clase 9
def esquema_sociedad(salida, ancho=15.0):
    fig, ax = lienzo(ancho, 7.8)
    ax.set_xlim(0, 15); ax.set_ylim(0, 7.8); ax.axis('off')
    niveles = [(6.1, 9.0, 'Españoles: gobernador, oficiales reales,\nencomenderos y vecinos', AZUL),
               (4.7, 11.0, 'Mestizos («mancebos de la tierra»): hijos de españoles y mujeres\nguaraníes; muchos fueron reconocidos como vecinos', AZUL2),
               (3.2, 13.0, 'Indígenas: yanaconas y mitayos en encomienda; pueblos que mantenían\nsu organización; grupos que resistían lejos de Asunción', '#5B7FA6'),
               (1.7, 13.0, 'Africanos y afrodescendientes esclavizados:\npocos en el siglo XVI, más numerosos después', '#7C8A99')]
    for y, w, t, c in niveles:
        caja(ax, 6.9 - w / 2, y, w, 1.2, t, c, tam=8.0)
    flecha(ax, 14.3, 7.1, 14.3, 1.8, color=GRIS)
    ax.text(14.55, 4.4, 'más poder', fontsize=7.5, color=GRIS, rotation=90, va='center')
    ax.text(7.0, 0.7, 'Esquema simplificado: en Asunción, el parentesco con los guaraníes y la lengua guaraní\nunían a todos los grupos.',
            ha='center', va='center', fontsize=8, color=AZUL, fontweight='bold')
    guardar(fig, salida, esquema=True)


# ---------------------------------------------------------------- Clase 10 (modelo aprobado, a tamaño de impresión)
def esquema_autoridades(salida, ancho=15.0):
    fig, ax = lienzo(ancho, 9.2)
    ax.set_xlim(0, 10); ax.set_ylim(0, 6.6); ax.axis('off')
    ax.text(0.05, 6.35, 'EN ESPAÑA', fontsize=8, color=GRIS, fontweight='bold')
    ax.text(0.05, 4.05, 'EN AMÉRICA', fontsize=8, color=GRIS, fontweight='bold')
    ax.plot([0, 10], [4.35, 4.35], color='#CCCCCC', lw=0.8, ls='--')
    caja(ax, 0.6, 5.4, 4.0, 0.8, 'El rey', AZUL, tam=9.5)
    caja(ax, 5.2, 5.4, 4.6, 0.8, 'Consejo de Indias\n(asesora al rey sobre América)', AZUL2, tam=8.2)
    flecha(ax, 4.6, 5.8, 5.2, 5.8)
    caja(ax, 0.6, 3.2, 4.0, 0.8, 'Virrey del Perú\n(desde 1542)', AZUL2, tam=8.2)
    caja(ax, 5.2, 3.2, 4.6, 0.8, 'Audiencia de Charcas\n(tribunal superior, desde 1559)', AZUL2, tam=8.2)
    flecha(ax, 2.6, 5.4, 2.6, 4.0); flecha(ax, 4.6, 3.6, 5.2, 3.6)
    caja(ax, 0.6, 1.9, 4.0, 0.9, 'Gobernador del Río de la Plata\ny del Paraguay (sede: Asunción)', '#5B7FA6', tam=8)
    flecha(ax, 2.6, 3.2, 2.6, 2.8)
    caja(ax, 0.05, 0.15, 3.15, 1.25, 'Cabildo de Asunción (1541):\nalcaldes y regidores,\ngobierno de la ciudad', '#E6EBF1', color=AZUL, tam=8.0)
    flecha(ax, 1.9, 1.9, 1.6, 1.4)
    caja(ax, 3.35, 0.15, 3.15, 1.25, 'Obispado del Río de la Plata\n(1547, sede en Asunción):\nvida religiosa', '#E6EBF1', color=AZUL, tam=8.0)
    caja(ax, 6.65, 0.15, 3.3, 1.25, 'Encomienda: NO gobernaba.\nAsignaba trabajo indígena\na un español', '#F3E2C7', color='#6B4A12', tam=8.0)
    ax.text(5.15, 2.35, 'El gobernador era nombrado por el rey.\nSi faltaba y no había sucesor, la Real\n'
                        'Provisión de 1537 permitía elegir uno\nprovisional «en nombre» del rey.', fontsize=8.0, color=AZUL, va='center')
    guardar(fig, salida, esquema=True)


def generar(geo, out):
    os.makedirs(out, exist_ok=True)
    p = lambda n: os.path.join(out, n)  # noqa: E731
    mapa_viajes(geo, p(reg('fig_6_1_viajes.png', 16.0)))
    esquema_navegacion(p(reg('fig_6_2_navegacion.png', 15.0)))
    mapa_tordesillas(geo, p(reg('fig_7_1_tordesillas.png', 12.0)))
    esquema_gobierno(p(reg('fig_7_2_gobierno.png', 15.0)))
    mapa_rutas_plata(geo, p(reg('fig_8_1_rutas_plata.png', 12.0)))
    linea_vertical(p(reg('fig_8_2_linea_1516_1541.png', 11.5)), HITOS_PLATA)
    mapa_rutas_plata(geo, p(reg('ficha_C_mapa_mudo.png', 15.0)), ancho=15.0, mudo=True)
    esquema_sociedad(p(reg('fig_9_1_sociedad.png', 15.0)))
    linea_vertical(p(reg('fig_10_1_linea_1534_1556.png', 11.5)), HITOS_1534)
    esquema_autoridades(p(reg('fig_10_2_autoridades.png', 15.0)))
    mapa_rutas_plata(geo, p(reg('eval_u3_mapa.png', 9.5)), ancho=9.5, mudo=True,
                     numerado={'Buenos Aires (1536)': 1, 'Asunción (1537)': 2, 'Sancti Spiritus (1527)': 3})
    mapa_rutas_plata(geo, p(reg('eval_u3_mapa_clave.png', 9.5)), ancho=9.5)
    return ANCHOS


if __name__ == '__main__':
    import sys
    generar(sys.argv[1], sys.argv[2])
