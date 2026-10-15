"""Figuras del Bloque III (encuentros 19 a 27).

Ubicaciones históricas (Villa Rica y Ciudad Real del Guairá, Santiago de
Jerez, Concepción del Bermejo, Mbororé, Palmares) en posición aproximada;
recorridos y áreas son trazados de la editorial sobre síntesis históricas
generales. Los esquemas del relieve no son mapas topográficos. Todo se declara
en la nota de cada figura (A17).
"""
import os

import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Ellipse, Polygon, Rectangle

from comun import (AGUA, AZUL, AZUL2, GRIS, OCRE, ROJO, VERDE, T_PAIS, area, caja, cargar, dibujar_paises, dibujar_rios,
                   escala, flecha, guardar, leyenda, lienzo, marco, norte, nota_fuente, rotulo, APA_DESEMBOCADURA, CIUDADES_PY)
from bloque2 import linea_vertical, ruta, simbolo

ANCHOS = {}
MORADO = '#6A4C93'


def reg(nombre, ancho):
    ANCHOS[nombre] = ancho
    return nombre


def punto(color, texto, marker='o', ms=6):
    return Line2D([], [], marker=marker, ls='', color=color, mec='white', ms=ms, label=texto)


def paises_rotulos(ax, lista, tam=8):
    for x, y, t in lista:
        rotulo(ax, x, y, t, tam=tam, color='#555555', fontweight='bold', ha='center')


# ---------------------------------------------------------------- Clase 11
CIUDADES_1617 = {
    'paraguay': {'Asunción': (-57.63, -25.28), 'Villa Rica del Espíritu Santo': (-51.97, -23.90),
                 'Ciudad Real del Guairá': (-54.00, -24.10), 'Santiago de Jerez': (-55.80, -20.50)},
    'plata': {'Buenos Aires': (-58.38, -34.60), 'Santa Fe': (-60.16, -31.20), 'Corrientes': (-58.83, -27.47),
              'Concepción del Bermejo': (-60.60, -26.70)},
}


def mapa_division_1617(geo, salida, ancho=12.0):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    rios = cargar(geo, 'ne_10m_rivers_lake_centerlines_scale_rank')
    fig, ax = lienzo(ancho, ancho * 1.12)
    marco(ax, -64.5, -46.0, -36.0, -18.5, ticks=False)
    dibujar_paises(ax, paises, borde=0.35)
    dibujar_rios(ax, rios, (-66, -44, -37, -17), nombres=('Paraná', 'Uruguay', 'Pilcomayo', 'Bermejo', 'Paranapanema', 'Ivaí', 'Salado'))
    via = [(-57.63, -25.28), (-58.2, -26.9), (-58.75, -27.35), (-59.6, -28.6), (-60.1, -30.6), (-60.16, -31.2),
           (-60.6, -32.3), (-59.6, -33.4), (-58.6, -34.3)]
    ruta(ax, via, OCRE, ls=(0, (4, 2)), lw=1.8)
    for (gob, color, mk) in (('paraguay', ROJO, 's'), ('plata', AZUL, 'o')):
        for t, (x, y) in CIUDADES_1617[gob].items():
            ax.plot(x, y, mk, ms=6.5, color=color, mec='white', zorder=7)
            if t == 'Concepción del Bermejo':
                rotulo(ax, x, y + 0.45, t, tam=8, ha='center')
                continue
            izq = t in ('Santa Fe', 'Buenos Aires', 'Corrientes')
            dy = -0.55 if t == 'Ciudad Real del Guairá' else 0.25
            rotulo(ax, x + (-0.35 if izq else 0.35), y + dy, t, tam=8, ha='right' if izq else 'left')
    rotulo(ax, -50.2, -31.5, 'OCÉANO\nATLÁNTICO', tam=8, color='#3A5F7D', ha='center')
    paises_rotulos(ax, ((-63.0, -22.5, 'BOLIVIA'), (-49.0, -21.0, 'BRASIL'), (-63.0, -33.0, 'ARGENTINA'), (-55.6, -32.6, 'URUGUAY')))
    rotulo(ax, -59.3, -22.0, 'PARAGUAY\n(actual)', tam=7.5, color='#7A5A2B', ha='center')
    escala(ax, -63.8, -35.2, -30, km=300, dy=0.3)
    norte(ax, -47.3, -20.3, tam=0.9)
    leyenda(fig, [punto(ROJO, 'Ciudad de la gobernación del Paraguay (Guairá)', 's'),
                  punto(AZUL, 'Ciudad de la gobernación del Río de la Plata'),
                  simbolo(OCRE, 'Salida fluvial de Asunción al mar', (0, (4, 2))), 'rio', 'limite'], ncol=2, y=0.095)
    nota_fuente(fig, 'División de 1617. Ciudades en posición aproximada (algunas cambiaron de lugar o desaparecieron). Los límites entre las '
                     'dos gobernaciones eran imprecisos y no se dibujan. Países actuales como referencia. Datos: Natural Earth.')
    guardar(fig, salida, rect=(0, 0.2, 1, 1))


# ---------------------------------------------------------------- Clase 12
def esquema_yerba(salida, ancho=15.0):
    fig, ax = lienzo(ancho, 7.0)
    ax.set_xlim(0, 15); ax.set_ylim(0, 7.0); ax.axis('off')
    caja(ax, 0.1, 4.4, 3.4, 1.5, 'Yerbales naturales\n(Mbaracayú\ny Guairá)', VERDE, tam=8.3)
    ax.text(0.15, 4.25, 'trabajo de mitayos, con alta mortalidad', ha='left', va='top', fontsize=8, color='#222222')
    caja(ax, 4.2, 4.4, 2.9, 1.5, 'Asunción\n(acopio y envío)', AZUL, tam=8.5)
    caja(ax, 7.8, 4.4, 3.2, 1.5, 'Santa Fe y\nBuenos Aires\n(pago de derechos)', AZUL2, tam=8.2)
    caja(ax, 11.7, 4.4, 3.2, 1.5, 'Mercados: Potosí y\nAlto Perú, Chile,\nBuenos Aires', OCRE, tam=8.2)
    flecha(ax, 3.55, 5.15, 4.15, 5.15); flecha(ax, 7.15, 5.15, 7.75, 5.15); flecha(ax, 11.05, 5.15, 11.65, 5.15)
    ax.text(7.45, 6.2, 'por el río Paraguay y el Paraná', ha='center', fontsize=8, color=AGUA, fontweight='bold')
    caja(ax, 0.1, 0.2, 6.9, 2.6, 'Economía de subsistencia\nmaíz, mandioca, porotos, ganado,\nalgodón: se produce para comer\ny vestirse en la chacra y la estancia',
         '#E6EBF1', color=AZUL, tam=8.2)
    caja(ax, 7.6, 0.2, 7.3, 2.6, 'Moneda de la tierra\nfaltaban monedas de metal: se pagaba\ncon yerba, tabaco, lienzo de algodón\no ganado, con valores fijados', '#F3E2C7',
         color='#6B4A12', tam=8.2)
    ax.text(7.5, 3.25, 'Convivían dos economías: una para vivir y otra para vender afuera, sobre todo yerba.', ha='center',
            fontsize=8.2, color=AZUL, fontweight='bold')
    guardar(fig, salida, esquema=True)


# ---------------------------------------------------------------- Clase 13
def plano_reduccion(salida, ancho=15.0):
    fig, ax = lienzo(ancho, 9.0)
    ax.set_xlim(0, 15); ax.set_ylim(0, 9.0); ax.axis('off')
    ax.add_patch(Rectangle((4.6, 2.7), 5.8, 3.4, fc='#F4EFE6', ec='#999999', lw=0.8))
    ax.text(7.5, 4.4, 'PLAZA', ha='center', va='center', fontsize=9, color=GRIS, fontweight='bold')
    ax.plot(7.5, 3.6, marker='+', ms=12, mew=2, color=GRIS)
    caja(ax, 5.7, 6.3, 3.6, 1.1, 'Iglesia', AZUL, tam=8.5)
    caja(ax, 9.45, 6.3, 2.2, 1.1, 'Colegio y\ntalleres', AZUL2, tam=8)
    caja(ax, 3.35, 6.3, 2.2, 1.1, 'Cementerio', '#7C8A99', tam=8)
    caja(ax, 11.8, 6.3, 1.9, 1.1, 'Huerta', VERDE, tam=8)
    for fila in range(3):
        for lado, x0 in (('izq', 0.4), ('der', 10.75)):
            ax.add_patch(Rectangle((x0, 1.0 + fila * 1.55), 3.85, 0.9, fc='#D9C7A3', ec='#8A7650', lw=0.6))
    ax.text(2.3, 0.55, 'Casas de las familias\nguaraníes (por cacicazgo)', ha='center', va='center', fontsize=8, color='#5A4A2A')
    ax.text(12.65, 0.55, 'Casas de las familias\nguaraníes (por cacicazgo)', ha='center', va='center', fontsize=8, color='#5A4A2A')
    caja(ax, 5.1, 1.35, 4.8, 1.0, 'Cabildo indígena\n(corregidor, alcaldes, regidores)', '#E6EBF1', color=AZUL, tam=8)
    caja(ax, 0.2, 7.7, 6.8, 1.15, 'Tupambaé («de Dios»): tierras y ganado comunes,\npara viudas, enfermos, el culto y el tributo', '#E2EDD9',
         color='#2E5A1F', tam=8, negrita=False)
    caja(ax, 7.4, 7.7, 7.4, 1.15, 'Abambaé («del hombre»): parcelas que cada familia\ncultivaba para su propio sustento', '#F3E2C7',
         color='#6B4A12', tam=8, negrita=False)
    nota_fuente(fig, 'Plano esquemático de la editorial: cada reducción tenía su propio trazado, pero casi todas seguían este modelo.')
    guardar(fig, salida, esquema=True, abajo=0.03)


# ---------------------------------------------------------------- Continuación E
LUGARES_E = {'São Paulo': (-46.63, -23.55), 'Asunción': (-57.63, -25.28), 'Ciudad Real': (-54.00, -24.10),
             'Villa Rica': (-51.97, -23.90), 'Salto del Guairá': (-54.28, -24.06), 'Mbororé': (-54.90, -27.70)}
GUAIRA = [(-54.3, -22.6), (-51.8, -22.4), (-50.3, -23.0), (-50.2, -25.6), (-52.5, -26.0), (-54.4, -25.6)]
PUEBLOS = [(-57.6, -26.6), (-55.2, -25.9), (-53.6, -27.2), (-53.4, -29.4), (-56.2, -29.8), (-57.8, -28.2)]
MALOCAS = [[(-46.8, -23.6), (-48.6, -23.4), (-50.6, -23.3), (-52.2, -23.4)],
           [(-46.9, -23.3), (-49.5, -21.6), (-53.0, -20.6), (-55.6, -21.0)]]
EXODO = [(-52.0, -22.8), (-53.2, -22.7), (-53.7, -23.6), (-54.25, -24.3), (-54.6, -25.5), (-55.3, -26.6), (-55.5, -27.2)]


def mapa_guaira(geo, salida, ancho=13.0, mudo=False, numerado=None):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    rios = cargar(geo, 'ne_10m_rivers_lake_centerlines_scale_rank')
    fig, ax = lienzo(ancho, ancho * 0.92)
    marco(ax, -61.0, -44.5, -31.0, -18.5, ticks=False)
    dibujar_paises(ax, paises, borde=0.35)
    dibujar_rios(ax, rios, (-62, -43, -32, -17), nombres=('Paraná', 'Uruguay', 'Pilcomayo', 'Paranapanema', 'Ivaí', 'Tietê', 'Ivinheima'))
    elems = []
    if not mudo:
        ax.add_patch(Polygon(GUAIRA, closed=True, fc=OCRE, alpha=0.28, ec=OCRE, lw=1.0, zorder=3))
        ax.add_patch(Polygon(PUEBLOS, closed=True, fc=VERDE, alpha=0.18, ec=VERDE, lw=1.0, ls='--', zorder=3))
        for k, m in enumerate(MALOCAS):
            ruta(ax, m, ROJO, ls='-' if k == 0 else (0, (3, 1.5)), lw=1.8)
        ruta(ax, EXODO, VERDE, lw=2.0)
        rotulo(ax, -52.2, -24.9, 'GUAIRÁ', tam=8.5, color='#6B4A12', fontweight='bold', ha='center')
        rotulo(ax, -55.6, -21.6, 'Itatín', tam=8, color='#6B4A12', ha='center')
        rotulo(ax, -55.7, -28.9, 'Reducciones del\nParaná y del Uruguay', tam=7.8, color='#2E5A1F', ha='center')
        rotulo(ax, -48.3, -24.6, 'malocas, 1628-1631', tam=7.8, color=ROJO, ha='center')
        rotulo(ax, -56.4, -24.2, 'éxodo, 1631', tam=7.8, color='#2E5A1F', ha='right', fontweight='bold')
        elems = [area(OCRE, 'Reducciones del Guairá, destruidas 1628-1631', alpha=0.4),
                 area(VERDE, 'Reducciones del Paraná y del Uruguay (después de 1631)', alpha=0.3),
                 simbolo(ROJO, 'Malocas bandeirantes al Guairá'), simbolo(ROJO, 'Malocas al Itatín (desde 1632)', (0, (3, 1.5))),
                 simbolo(VERDE, 'Éxodo encabezado por Ruiz de Montoya')]
    lugares = numerado or ({} if mudo else {k: None for k in LUGARES_E})
    for t, num in lugares.items():
        x, y = LUGARES_E[t]
        if num is not None:
            ax.plot(x, y, 'o', ms=12, color=AZUL, mec='white', zorder=8)
            ax.text(x, y, str(num), ha='center', va='center', fontsize=8.5, color='white', fontweight='bold', zorder=9)
        elif t == 'Mbororé':
            ax.plot(x, y, '*', ms=13, color=ROJO, mec='white', zorder=8)
            rotulo(ax, x + 0.5, y - 0.15, 'Mbororé, 1641', tam=8.2, fontweight='bold', color=ROJO, va='center')
        elif t == 'Salto del Guairá':
            ax.plot(x, y, '^', ms=7, color=AGUA, mec='white', zorder=8)
            rotulo(ax, x - 0.35, y - 0.55, 'Saltos del Guairá', tam=7.8, ha='right')
        else:
            ax.plot(x, y, 'o', ms=5, color='#222222', zorder=8)
            dx, ha = (-0.35, 'right') if t == 'Asunción' else (0.35, 'left')
            rotulo(ax, x + dx, y + 0.3, t, tam=8, ha=ha)
    paises_rotulos(ax, ((-59.3, -21.0, 'PARAGUAY'), (-48.0, -20.0, 'BRASIL'), (-59.0, -28.3, 'ARGENTINA'), (-54.6, -30.4, 'URUGUAY')))
    rotulo(ax, -46.7, -28.5, 'OCÉANO\nATLÁNTICO', tam=8, color='#3A5F7D', ha='center')
    escala(ax, -60.5, -30.3, -26, km=200, dy=0.25)
    norte(ax, -45.5, -20.0, tam=0.8)
    if mudo or numerado:
        leyenda(fig, ['rio', 'limite'], ncol=2, y=0.1)
    else:
        leyenda(fig, elems + [punto('#222222', 'Ciudad o villa'), punto(ROJO, 'Batalla de Mbororé', '*', 9),
                              punto(AGUA, 'Saltos del Guairá', '^'), 'rio'], ncol=2, tam=7.3)
    nota_fuente(fig, 'Áreas, recorridos y lugares históricos en posición aproximada (trazado de la editorial sobre síntesis históricas). '
                     'Países actuales como referencia. Datos: Natural Earth.')
    guardar(fig, salida, rect=(0, 0.17 if (mudo or numerado) else 0.25, 1, 1))


HITOS_E = [(1609, 'Primera reducción jesuítica: San Ignacio Guazú'), (1610, 'Loreto y San Ignacio en el Guairá'),
           (1628, 'Comienzan las grandes malocas al Guairá'), (1631, 'Éxodo por el Paraná, con Ruiz de Montoya'),
           (1632, 'Se abandonan Villa Rica y Ciudad Real'), (1639, 'Montoya publica la Conquista espiritual'),
           (1641, 'Batalla de Mbororé')]


# ---------------------------------------------------------------- Clase 14
PUERTOS = {'Sevilla': (-6.0, 37.4), 'Veracruz': (-96.1, 19.2), 'La Habana': (-82.4, 23.1), 'Portobelo': (-79.65, 9.55),
           'Cartagena': (-75.5, 10.4), 'Callao (Lima)': (-77.1, -12.05), 'Buenos Aires': (-58.4, -34.6)}
MINAS = {'Potosí': (-65.75, -19.6), 'Zacatecas': (-102.6, 22.8), 'Huancavelica (azogue)': (-75.0, -12.8)}


def mapa_plata(geo, salida, ancho=16.0):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    fig, ax = lienzo(ancho, 12.6)
    marco(ax, -118, 2, -40, 45, ticks=False)
    dibujar_paises(ax, paises, borde=0.25)
    ruta(ax, [(-8, 36.6), (-40, 30), (-70, 23), (-95.5, 19.6)], AZUL)
    ruta(ax, [(-8, 36.2), (-40, 18), (-65, 12.5), (-75.2, 10.8)], AZUL2)
    ruta(ax, [(-75.6, 10.0), (-79.3, 9.7)], AZUL2, flecha_final=True)
    ruta(ax, [(-82.0, 23.6), (-60, 31), (-30, 38), (-7, 37.0)], GRIS, ls=(0, (3, 1.5)))
    ruta(ax, [(-77.4, -12.2), (-81.5, -5), (-80.0, 8.6)], AZUL2)
    ruta(ax, [(-65.9, -19.4), (-70.5, -18.5), (-76.6, -12.4)], OCRE)
    ruta(ax, [(-65.5, -20.0), (-63.5, -27.0), (-60.0, -32.5), (-58.7, -34.3)], ROJO, ls=(0, (3, 1.5)))
    ruta(ax, [(-57.63, -25.28), (-61.5, -22.5), (-65.3, -19.9)], VERDE, ls=(0, (2, 1.2)))
    for t, (x, y) in PUERTOS.items():
        ax.plot(x, y, 'o', ms=4.8, color='#222222', zorder=8)
        dx, ha = {'Sevilla': (-1.5, 'right'), 'Veracruz': (-1.5, 'right'), 'La Habana': (1.2, 'left'), 'Portobelo': (-1.5, 'right'),
                  'Cartagena': (1.2, 'left'), 'Callao (Lima)': (-1.5, 'right'), 'Buenos Aires': (1.2, 'left')}[t]
        if t == 'Callao (Lima)':
            rotulo(ax, x - 1.5, y + 0.4, t, tam=8, ha='right', va='bottom')
            continue
        rotulo(ax, x + dx, y - 0.4, t, tam=8, ha=ha, va='top' if t != 'La Habana' else 'bottom')
    for t, (x, y) in MINAS.items():
        ax.plot(x, y, 'D', ms=6.5, color=OCRE, mec='#222222', zorder=8)
        dx, ha = (1.3, 'left') if t == 'Potosí' else (-1.5, 'right')
        if t.startswith('Huanca'):
            rotulo(ax, x + 1.6, y + 0.2, t, tam=8, ha='left', fontweight='bold')
            continue
        rotulo(ax, x + dx, y + 0.5, t, tam=8, ha=ha, fontweight='bold')
    ax.plot(-57.63, -25.28, 's', ms=5.5, color=VERDE, mec='white', zorder=8)
    rotulo(ax, -56.2, -25.6, 'Asunción', tam=8, ha='left', va='top')
    rotulo(ax, -40, 5, 'OCÉANO\nATLÁNTICO', tam=8.5, color='#3A5F7D', ha='center')
    rotulo(ax, -105, -10, 'OCÉANO\nPACÍFICO', tam=8.5, color='#3A5F7D', ha='center')
    rotulo(ax, -10, 41.5, 'ESPAÑA', tam=8, color='#555555', fontweight='bold', ha='center')
    leyenda(fig, [punto(OCRE, 'Mina', 'D'), punto('#222222', 'Puerto autorizado o ciudad'), simbolo(AZUL, 'Flota de Nueva España'),
                  simbolo(AZUL2, 'Galeones de Tierra Firme y del Pacífico'), simbolo(GRIS, 'Regreso conjunto a Sevilla', (0, (3, 1.5))),
                  simbolo(OCRE, 'Plata de Potosí hacia Lima'), simbolo(ROJO, 'Contrabando por Buenos Aires', (0, (3, 1.5))),
                  simbolo(VERDE, 'Yerba del Paraguay hacia Potosí', (0, (2, 1.2)))], ncol=3, tam=7.3, y=0.055)
    nota_fuente(fig, 'Esquema aproximado de la editorial: muestra el sistema general del siglo XVII, no derrotas exactas. Países actuales: Natural Earth.')
    guardar(fig, salida, rect=(0, 0.16, 1, 1))


# ---------------------------------------------------------------- Clase 15
COLONIAS = [('Quebec, 1608', (-71.2, 46.8), 'fr', (1.2, 0.3, 'left')), ('Jamestown, 1607', (-76.8, 37.2), 'in', (1.2, -0.6, 'left')),
            ('Plymouth, 1620', (-70.7, 41.95), 'in', (1.2, -0.4, 'left')), ('Nueva Ámsterdam, 1625', (-74.0, 40.7), 'ho', (-1.2, 0.6, 'right')),
            ('Barbados, 1627', (-59.6, 13.1), 'in', (1.2, -0.6, 'left')), ('Martinica, 1635', (-61.0, 14.6), 'fr', (1.2, 0.6, 'left')),
            ('Curazao, 1634', (-68.9, 12.1), 'ho', (-1.2, -0.9, 'right')), ('Jamaica, 1655', (-77.3, 18.1), 'in', (-1.2, -0.6, 'right')),
            ('Salvador de Bahía, 1549', (-38.5, -12.97), 'po', (-1.2, -1.3, 'right')), ('Recife (holandés 1630-1654)', (-34.9, -8.05), 'ho', (1.0, 2.2, 'right')),
            ('São Paulo', (-46.6, -23.5), 'po', (1.2, -0.6, 'left'))]
COLOR_POT = {'in': ROJO, 'fr': AZUL, 'ho': OCRE, 'po': VERDE}


def mapa_colonias(geo, salida, ancho=12.0):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    fig, ax = lienzo(ancho, 14.6)
    marco(ax, -100, -28, -36, 56, ticks=False)
    dibujar_paises(ax, paises, borde=0.25)
    for t, (x, y), p, (dx, dy, ha) in COLONIAS:
        ax.plot(x, y, 'o', ms=6.5, color=COLOR_POT[p], mec='white', zorder=8)
        rotulo(ax, x + dx, y + dy, t, tam=7.8, ha=ha, va='center')
    ax.plot(-36.0, -9.2, '^', ms=8, color='#222222', mec='white', zorder=8)
    rotulo(ax, -37.0, -9.4, 'Palmares (quilombo)', tam=7.8, ha='right', va='center', fontweight='bold')
    ax.plot(-57.63, -25.28, 's', ms=5, color='#555555', zorder=8)
    rotulo(ax, -58.3, -25.6, 'Asunción', tam=7.8, ha='right', va='top')
    rotulo(ax, -88, 52, 'NUEVA FRANCIA', tam=7.8, color=AZUL, fontweight='bold', ha='center')
    rotulo(ax, -47, -3, 'BRASIL\n(Portugal)', tam=8, color='#2E5A1F', fontweight='bold', ha='center')
    rotulo(ax, -45, 30, 'OCÉANO\nATLÁNTICO', tam=8, color='#3A5F7D', ha='center')
    leyenda(fig, [punto(ROJO, 'Inglaterra'), punto(AZUL, 'Francia'), punto(OCRE, 'Holanda'), punto(VERDE, 'Portugal'),
                  punto('#222222', 'Comunidad de africanos libres', '^', 7)], ncol=3)
    nota_fuente(fig, 'Fechas de fundación o de ocupación; posiciones aproximadas. Las colonias de España no se marcan (ver Unidad 3). '
                     'Países actuales: Natural Earth.')
    guardar(fig, salida, rect=(0, 0.09, 1, 1))


# ---------------------------------------------------------------- Clase 16
def mapa_america_posicion(geo, salida, ancho=11.0, relieve=False):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    fig, ax = lienzo(ancho, ancho * 1.25)
    marco(ax, -170, -25, -58, 84, ticks=not relieve)
    ameri = {f['properties'].get('NAME') for f in paises if f['properties'].get('CONTINENT') in ('North America', 'South America')}
    colores = {n: '#EFE6D2' for n in ameri}
    if not relieve:
        colores['Paraguay'] = '#C9A86A'
    dibujar_paises(ax, paises, borde=0.2, colores=colores)
    if not relieve:
        for lat, t, c in ((0, 'Ecuador (0°)', ROJO), (23.44, 'Trópico de Cáncer', OCRE), (-23.44, 'Trópico de Capricornio', OCRE),
                          (66.56, 'Círculo Polar Ártico', AZUL2)):
            ax.axhline(lat, color=c, lw=1.1, ls='-' if lat == 0 else (0, (4, 2)), zorder=3)
            rotulo(ax, -168, lat + 1.3, t, tam=7.8, color=c, fontweight='bold')
        for x, y, t in ((-100, 50, 'AMÉRICA\nDEL NORTE'), (-92, 12, 'AMÉRICA\nCENTRAL'), (-62, -8, 'AMÉRICA\nDEL SUR')):
            rotulo(ax, x, y, t, tam=8.2, color=AZUL, fontweight='bold', ha='center')
        ax.annotate('Paraguay', xy=(-58.4, -23.4), xytext=(-40, -38), fontsize=8.5, color='#7A5A2B', fontweight='bold',
                    arrowprops=dict(arrowstyle='-|>', color='#7A5A2B', lw=1.0), path_effects=None)
        rotulo(ax, -140, 10, 'OCÉANO\nPACÍFICO', tam=8, color='#3A5F7D', ha='center')
        rotulo(ax, -40, 25, 'OCÉANO\nATLÁNTICO', tam=8, color='#3A5F7D', ha='center')
        rotulo(ax, -110, 79, 'OCÉANO GLACIAL ÁRTICO', tam=7.8, color='#3A5F7D', ha='center')
        ax.set_xticks([-160, -120, -80, -40]); ax.set_xticklabels(['160° O', '120° O', '80° O', '40° O'])
        ax.set_yticks([-40, -20, 0, 20, 40, 60, 80]); ax.set_yticklabels(['40° S', '20° S', '0°', '20° N', '40° N', '60° N', '80° N'])
        leyenda(fig, [area('#C9A86A', 'Paraguay', alpha=1), area('#EFE6D2', 'Otros países de América', alpha=1),
                      Line2D([], [], color=OCRE, lw=1.1, ls=(0, (4, 2)), label='Trópicos'), 'limite'], ncol=2)
        nota_fuente(fig, 'Mapa aproximado en proyección simple (latitud y longitud como ejes). Datos: Natural Earth.')
        guardar(fig, salida, rect=(0, 0.08, 1, 1))
        return
    # relieve esquemático de América
    cadenas = [('Montañas Rocosas', [(-150, 62), (-135, 58), (-123, 50), (-113, 43), (-107, 37), (-106, 32)], (-128, 44)),
               ('Sierra Madre', [(-108, 29), (-104, 24), (-99, 19), (-96, 17)], (-116, 22)),
               ('Apalaches', [(-68, 46), (-74, 42), (-79, 38), (-84, 34)], (-73, 34)),
               ('Cordillera de los Andes', [(-73, 10), (-77, 3), (-79, -3), (-76, -12), (-70, -17), (-69, -23), (-70, -32),
                                            (-71.5, -40), (-73, -48), (-73, -53)], (-102, -18))]
    for t, pts, (lx, ly) in cadenas:
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color='#7A4E2D', lw=4.2, solid_capstyle='round', zorder=5, alpha=0.9)
        rotulo(ax, lx, ly, t, tam=8, color='#5A3A1F', fontweight='bold', ha='center')
    for (cx, cy, w, h, t, lx, ly) in ((-44, -12, 22, 18, 'Macizo de\nBrasilia', -37, -27), (-60, 5, 14, 7, 'Macizo de\nGuayana', -50, 12),
                                     (-70, -46, 8, 12, 'Meseta\npatagónica', -55, -47)):
        ax.add_patch(Ellipse((cx, cy), w, h, fc='#C9A86A', ec='#8A6A30', alpha=0.55, hatch='..', zorder=4))
        rotulo(ax, lx, ly, t, tam=7.8, color='#5A3A1F', ha='center')
    for (cx, cy, w, h, t, lx, ly) in ((-97, 42, 18, 16, 'Llanuras\ncentrales', -97, 42), (-62, -29, 10, 14, 'Llanura\nchaco-pampeana', -62, -29),
                                     (-62, -3, 18, 9, 'Llanura\namazónica', -62, -3)):
        ax.add_patch(Ellipse((cx, cy), w, h, fc='#A8C99A', ec='#4E7D3A', alpha=0.55, zorder=4))
        rotulo(ax, lx, ly, t, tam=7.8, color='#2E5A1F', ha='center', va='center')
    ax.plot(-70.0, -32.65, '^', ms=8, color=ROJO, mec='white', zorder=7)
    rotulo(ax, -82, -33.5, 'Aconcagua', tam=7.8, color=ROJO, ha='right', fontweight='bold')
    leyenda(fig, [Line2D([], [], color='#7A4E2D', lw=4, label='Gran cordillera'), area('#C9A86A', 'Macizo o meseta', rayado='..'),
                  area('#A8C99A', 'Gran llanura'), punto(ROJO, 'Aconcagua, punto más alto', '^', 7)], ncol=2)
    nota_fuente(fig, 'Esquema simplificado de la editorial: muestra la ubicación general de las grandes formas de relieve; no es un mapa '
                     'topográfico. Países actuales: Natural Earth.')
    guardar(fig, salida, rect=(0, 0.08, 1, 1))


EXTREMOS_PY = {'Norte': (-58.17, -19.29), 'Sur': (-58.62, -27.60), 'Este': (-54.32, -24.06), 'Oeste': (-62.64, -22.25)}


def mapa_py_posicion(geo, salida, ancho=12.0):
    paises = cargar(geo, 'ne_50m_admin_0_countries')
    rios = cargar(geo, 'ne_10m_rivers_lake_centerlines_scale_rank')
    fig, ax = lienzo(ancho, 13.2)
    marco(ax, -63.4, -53.6, -28.4, -18.6)
    dibujar_paises(ax, paises, resaltar='Paraguay')
    dibujar_rios(ax, rios, (-64, -53, -29, -18), nombres=('Paraná', 'Pilcomayo', 'Paraguay', 'Verde'))
    ax.axhline(-23.44, color=OCRE, lw=1.2, ls=(0, (4, 2)), zorder=3)
    rotulo(ax, -57.4, -23.3, 'Trópico de\nCapricornio (23° 26\' S)', tam=7.8, color='#8A6A10', fontweight='bold', va='bottom')
    for lado, (x, y) in EXTREMOS_PY.items():
        ax.plot(x, y, 'X', ms=7, color=ROJO, mec='white', zorder=8)
    rotulo(ax, -58.0, -19.05, 'Extremo norte 19° 18\' S', tam=7.8, color=ROJO, ha='left')
    rotulo(ax, -58.5, -28.05, 'Extremo sur 27° 36\' S', tam=7.8, color=ROJO, ha='left')
    rotulo(ax, -54.45, -24.3, 'Extremo este\n54° 19\' O', tam=7.8, color=ROJO, ha='right', va='top')
    rotulo(ax, -62.5, -21.75, 'Extremo oeste\n62° 38\' O', tam=7.8, color=ROJO, ha='left')
    ax.plot(*APA_DESEMBOCADURA, '^', ms=7, color=AGUA, mec='white', zorder=8)
    rotulo(ax, -57.75, -21.85, 'río Apa', tam=7.8, color=AGUA, ha='left', fontweight='bold')
    x, y = CIUDADES_PY['Asunción']
    ax.plot(x, y, '*', ms=10, color=AZUL, mec='white', zorder=8)
    rotulo(ax, x + 0.2, y - 0.45, 'Asunción', tam=8)
    for xx, yy, t, rot in ((-58.55, -21.2, 'río Paraguay', 80), (-55.55, -26.4, 'río Paraná', 40), (-60.7, -24.0, 'río Pilcomayo', -33)):
        rotulo(ax, xx, yy, t, tam=7.8, color=AGUA, rotation=rot, fontweight='bold')
    paises_rotulos(ax, ((-61.8, -19.4, 'BOLIVIA'), (-55.2, -20.0, 'BRASIL'), (-62.0, -27.4, 'ARGENTINA')), tam=9)
    rotulo(ax, -60.3, -22.6, 'PARAGUAY', tam=10, color='#7A5A2B', fontweight='bold', ha='center')
    ax.set_xticks([-62, -60, -58, -56, -54]); ax.set_xticklabels(['62° O', '60° O', '58° O', '56° O', '54° O'])
    ax.set_yticks([-28, -26, -24, -22, -20]); ax.set_yticklabels(['28° S', '26° S', '24° S', '22° S', '20° S'])
    ax.grid(color='#BBBBBB', lw=0.4, ls=':', zorder=0)
    escala(ax, -63.1, -27.9, -24.0)
    norte(ax, -54.3, -27.6, tam=0.5)
    leyenda(fig, [punto(ROJO, 'Punto extremo', 'X', 7), 'capital', 'apa', 'rio', 'limite',
                  Line2D([], [], color=OCRE, lw=1.2, ls=(0, (4, 2)), label='Trópico de Capricornio')], ncol=2, y=0.085)
    nota_fuente(fig, 'Mapa aproximado. Coordenadas extremas según la bibliografía geográfica escolar (a cotejar con el IGM o el INE). '
                     'Natural Earth no trae el río Apa: se marca su desembocadura en posición aproximada. Datos: Natural Earth.')
    guardar(fig, salida, rect=(0, 0.22, 1, 1))


# ---------------------------------------------------------------- Clase 17
def perfil_py(salida, ancho=15.0):
    fig, ax = lienzo(ancho, 6.6)
    x = np.array([0, 60, 140, 230, 330, 420, 470, 500, 540, 590, 640, 700, 760, 820, 880])
    z = np.array([330, 300, 250, 190, 140, 105, 80, 64, 200, 260, 160, 330, 420, 260, 110])
    ax.fill_between(x, 0, z, color='#D9C7A3', zorder=2)
    ax.plot(x, z, color='#7A5A2B', lw=1.4, zorder=3)
    ax.set_xlim(0, 880); ax.set_ylim(0, 620)
    ax.set_ylabel('Altura aproximada (m)', fontsize=7.5, color=GRIS)
    ax.set_xticks([]); ax.tick_params(labelsize=7, colors=GRIS)
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    marcas = [(40, 'CHACO (Región Occidental)\nllanura con suave pendiente\nhacia el este', 470, 'center'),
              (500, 'río Paraguay', 120, 'center'), (565, 'cordillera\nde los Altos', 330, 'center'),
              (700, 'serranías del\ncentro y del este', 500, 'center'), (880, 'río Paraná', 170, 'right')]
    for xx, t, yy, ha in marcas:
        ax.text(xx if ha != 'center' or xx > 100 else 230, yy, t, fontsize=8, color=AZUL, ha=ha if xx > 100 else 'center', va='bottom',
                fontweight='bold')
    ax.annotate('', xy=(500, 66), xytext=(500, 118), arrowprops=dict(arrowstyle='-|>', color=AGUA, lw=1.1))
    ax.annotate('', xy=(878, 112), xytext=(860, 166), arrowprops=dict(arrowstyle='-|>', color=AGUA, lw=1.1))
    ax.text(5, 585, 'OESTE', fontsize=8, color=GRIS, fontweight='bold')
    ax.text(875, 585, 'ESTE', fontsize=8, color=GRIS, fontweight='bold', ha='right')
    nota_fuente(fig, 'Perfil esquemático de la editorial, de oeste a este y pasando cerca de Asunción. Alturas aproximadas; escala '
                     'vertical muy exagerada.')
    fig.subplots_adjust(left=0.08, right=0.99, top=0.97, bottom=0.15)
    from comun import DPI
    fig.savefig(salida, dpi=DPI)
    import matplotlib.pyplot as plt
    plt.close(fig)


def generar(geo, out):
    os.makedirs(out, exist_ok=True)
    p = lambda n: os.path.join(out, n)  # noqa: E731
    mapa_division_1617(geo, p(reg('fig_11_1_division_1617.png', 12.0)))
    esquema_yerba(p(reg('fig_12_1_yerba.png', 15.0)))
    plano_reduccion(p(reg('fig_13_1_reduccion.png', 15.0)))
    mapa_guaira(geo, p(reg('fig_E_1_guaira_mborore.png', 13.0)))
    linea_vertical(p(reg('fig_E_2_linea_1609_1641.png', 11.5)), HITOS_E)
    mapa_guaira(geo, p(reg('ficha_E_mapa_mudo.png', 15.0)), ancho=15.0, mudo=True)
    mapa_plata(geo, p(reg('fig_14_1_plata.png', 16.0)))
    mapa_colonias(geo, p(reg('fig_15_1_colonias.png', 12.0)))
    mapa_guaira(geo, p(reg('eval_u4_mapa.png', 10.0)), ancho=10.0, mudo=True,
                numerado={'São Paulo': 1, 'Ciudad Real': 2, 'Mbororé': 3})
    mapa_guaira(geo, p(reg('eval_u4_mapa_clave.png', 13.0)))
    mapa_america_posicion(geo, p(reg('fig_16_1_america.png', 11.0)))
    mapa_py_posicion(geo, p(reg('fig_16_2_paraguay_posicion.png', 12.0)))
    mapa_america_posicion(geo, p(reg('fig_17_1_relieve_america.png', 11.0)), relieve=True)
    perfil_py(p(reg('fig_17_2_perfil.png', 15.0)))
    return ANCHOS


if __name__ == '__main__':
    import sys
    generar(sys.argv[1], sys.argv[2])
