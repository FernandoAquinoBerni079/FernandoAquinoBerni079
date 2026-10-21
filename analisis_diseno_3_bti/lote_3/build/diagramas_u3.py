# -*- coding: utf-8 -*-
"""Figuras del lote 3 (Capítulos 7 a 9), generadas por código con matplotlib; sin recursos de terceros.

Una notación por figura, con el mismo mecanismo del Capítulo 5 (lote_2/build/diagramas.py): cada figura declara su
notación y solo puede usar las funciones de esa notación; cada función registra el símbolo que dibuja y la generación
se detiene si una figura mezcla. El registro queda en figs/simbolos.json.
  - der_*: entidad-relación clásica de Algorítmica 3.º (entidad, relación, cardinalidad y línea). Representación
    simplificada: los atributos están en el diccionario de datos (decisión de Fernando del 20-oct-2026).
  - nav_*: mapa de navegación aprobado (pantalla, transición rotulada con la acción, inicio y zona por rol).
  - boc_*: boceto de baja fidelidad (marco de pantalla, campo con etiqueta, botón y zona de mensaje).
  - capa_*: esquema de capas (banda de capa y operación entre capas).
  - esquema: figuras didácticas sin notación (obra y ejemplares, historial).
Los datos de cada figura se leen de caso/diseno.py."""
import os, sys, json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon, Rectangle

AQUI = os.path.dirname(os.path.abspath(__file__))
L3 = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(L3, 'caso'))
import diseno as X

plt.rcParams.update({'font.family': 'DejaVu Sans'})
DARK, MED, SOFT, LIGHT = '#1B5E20', '#2E7D32', '#43A047', '#E8F5E9'
AMBAR, GRIS, NEGRO, GRIS_C = '#B8860B', '#616161', '#212121', '#BDBDBD'

NOTACIONES = {'der': 'Entidad-relación (notación clásica de Algorítmica 3.º)',
              'navegacion': 'Mapa de navegación', 'boceto': 'Boceto de baja fidelidad', 'capas': 'Esquema de capas'}
SIMBOLOS = {
    'der_entidad': ('der', 'Entidad', 'Una cosa de la que el sistema guarda datos', 'Sustantivo en singular: «Ejemplar»'),
    'der_relacion': ('der', 'Relación', 'Cómo se vinculan dos entidades', 'Verbo: «se presta en»'),
    'der_cardinalidad': ('der', 'Cardinalidad', 'Cuántos de un lado se vinculan con uno del otro', '1 o N junto a cada entidad'),
    'der_linea': ('der', 'Línea', 'Une cada entidad con la relación', 'Sin flecha'),
    'nav_pantalla': ('navegacion', 'Pantalla', 'Una pantalla del sistema, con su código', 'Código y nombre: «PT-05 Registrar préstamo»'),
    'nav_transicion': ('navegacion', 'Transición', 'Cómo se pasa de una pantalla a otra', 'Flecha rotulada con la acción: «Prestar»'),
    'nav_inicio': ('navegacion', 'Inicio', 'La pantalla con la que empieza el uso', 'Uno por mapa'),
    'nav_zona': ('navegacion', 'Zona por rol', 'Las pantallas que solo ve un rol', 'Marco punteado con el nombre del rol'),
    'boc_marco': ('boceto', 'Pantalla del boceto', 'El borde de una pantalla, con su título', 'Sin colores ni logotipos'),
    'boc_campo': ('boceto', 'Campo con etiqueta', 'Dónde se escribe un dato', 'La etiqueta siempre visible'),
    'boc_boton': ('boceto', 'Botón', 'Una acción', 'Un verbo: «Prestar»'),
    'boc_mensaje': ('boceto', 'Zona de mensaje', 'Dónde aparecen los mensajes', 'Junto a la acción que los provoca'),
    'capa_banda': ('capas', 'Capa', 'Una responsabilidad del sistema', 'Presentación, reglas o persistencia'),
    'capa_operacion': ('capas', 'Operación', 'Un pedido que una capa le hace a otra', 'Flecha con el código de la operación'),
}
REGISTRO = {}


class Lienzo:
    def __init__(self, figura, notacion):
        assert notacion in NOTACIONES or notacion == 'esquema', notacion
        self.figura, self.notacion, self.simbolos = figura, notacion, {}
        REGISTRO[figura] = {'notacion': notacion, 'simbolos': self.simbolos}

    def usar(self, s):
        assert SIMBOLOS[s][0] == self.notacion, 'la figura %s (%s) no puede usar %s' % (self.figura, self.notacion, s)
        self.simbolos[s] = self.simbolos.get(s, 0) + 1


def _guardar(fig, ruta):
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white', pad_inches=0.05); plt.close(fig)


# ---------------------------------------------------------------- entidad-relación
def der_entidad(L, ax, x, y, nombre, w=2.6, h=0.9):
    L.usar('der_entidad')
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, facecolor=LIGHT, edgecolor=MED, lw=1.8))
    if nombre:
        ax.text(x, y, nombre.upper(), ha='center', va='center', fontsize=11, weight='bold', color=DARK)


def der_relacion(L, ax, x, y, nombre, w=2.5, h=1.0):
    L.usar('der_relacion')
    ax.add_patch(Polygon([(x - w / 2, y), (x, y + h / 2), (x + w / 2, y), (x, y - h / 2)], closed=True,
                         facecolor='white', edgecolor=NEGRO, lw=1.5))
    if nombre:
        ax.text(x, y, nombre, ha='center', va='center', fontsize=9.5, color=NEGRO, style='italic')


def der_linea(L, ax, a, b):
    L.usar('der_linea')
    ax.plot([a[0], b[0]], [a[1], b[1]], color=NEGRO, lw=1.4)


def der_cardinalidad(L, ax, x, y, c):
    L.usar('der_cardinalidad')
    ax.text(x, y, c, ha='center', va='center', fontsize=11, weight='bold', color=AMBAR)


def modelo_datos(ruta):
    L = Lienzo('fig_7_1', 'der')
    fig, ax = plt.subplots(figsize=(11.0, 6.0))
    ax.set_xlim(0, 19); ax.set_ylim(0, 10.4); ax.axis('off'); ax.set_aspect('equal')
    pos = {'Obra': (2.0, 8.6), 'Edición': (2.0, 4.6), 'Ejemplar': (2.0, 0.8), 'Préstamo': (10.2, 0.8), 'Lector': (17.0, 0.8)}
    for e, (x, y) in pos.items():
        der_entidad(L, ax, x, y, e)
    for e1, rel, e2, c1, c2, _ in X.RELACIONES:
        (x1, y1), (x2, y2) = pos[e1], pos[e2]
        rx, ry = (x1 + x2) / 2, (y1 + y2) / 2
        der_relacion(L, ax, rx, ry, rel)
        if x1 == x2:   # vertical
            der_linea(L, ax, (x1, y1 - 0.45), (rx, ry + 0.5)); der_linea(L, ax, (rx, ry - 0.5), (x2, y2 + 0.45))
            der_cardinalidad(L, ax, x1 + 0.35, y1 - 0.75, c1); der_cardinalidad(L, ax, x2 + 0.35, y2 + 0.75, c2)
        else:          # horizontal
            s = 1 if x2 > x1 else -1
            der_linea(L, ax, (x1 + s * 1.3, y1), (rx - s * 1.25, ry)); der_linea(L, ax, (rx + s * 1.25, ry), (x2 - s * 1.3, y2))
            der_cardinalidad(L, ax, x1 + s * 1.6, y1 + 0.32, c1); der_cardinalidad(L, ax, x2 - s * 1.6, y2 + 0.32, c2)
    for k, e in enumerate(X.SIN_RELACION):
        der_entidad(L, ax, 12.0 + k * 3.6, 8.6, e)
    ax.text(13.8, 7.5, 'Sin relaciones en el núcleo: guardan reglas y permisos', ha='center', va='center', fontsize=8.8,
            color=GRIS, style='italic')
    _guardar(fig, ruta)


# ---------------------------------------------------------------- mapa de navegación
def nav_pantalla(L, ax, x, y, cod, nombre, w=3.3, h=1.15):
    L.usar('nav_pantalla')
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, facecolor='white', edgecolor=MED, lw=1.6))
    if cod:
        import textwrap
        ax.text(x, y + h / 2 - 0.28, cod, ha='center', va='center', fontsize=9, weight='bold', color=DARK)
        ax.text(x, y - 0.14, '\n'.join(textwrap.wrap(nombre, 18)), ha='center', va='center', fontsize=8.0, color=NEGRO, linespacing=1.05)


def nav_transicion(L, ax, puntos, accion, pos=None):
    """Flecha de un punto a otro, recta o en tramos; el rótulo es la acción que lleva de una pantalla a la otra."""
    L.usar('nav_transicion')
    for a, b in zip(puntos[:-2], puntos[1:-1]):
        ax.plot([a[0], b[0]], [a[1], b[1]], color=NEGRO, lw=1.2)
    ax.add_patch(FancyArrowPatch(puntos[-2], puntos[-1], arrowstyle='-|>', mutation_scale=12, color=NEGRO, lw=1.2, shrinkA=0, shrinkB=0))
    if accion:
        x, y = pos or ((puntos[0][0] + puntos[-1][0]) / 2, (puntos[0][1] + puntos[-1][1]) / 2)
        ax.text(x, y, accion, ha='center', va='center', fontsize=8, color=NEGRO, style='italic',
                bbox=dict(boxstyle='round,pad=0.12', facecolor='white', edgecolor='none'))


def nav_inicio(L, ax, x, y):
    L.usar('nav_inicio')
    ax.add_patch(Circle((x, y), 0.22, facecolor=NEGRO))


def nav_zona(L, ax, x0, y0, w, h, rol):
    L.usar('nav_zona')
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor='none', edgecolor=AMBAR, lw=1.6, ls='--'))
    if rol:
        ax.text(x0 + 0.15, y0 + h - 0.3, rol, ha='left', va='center', fontsize=9.5, weight='bold', color=AMBAR)


def mapa_navegacion(ruta):
    L = Lienzo('fig_8_1', 'navegacion')
    fig, ax = plt.subplots(figsize=(11.4, 6.6))
    ax.set_xlim(0, 22.6); ax.set_ylim(2.6, 13.0); ax.axis('off'); ax.set_aspect('equal')
    pos = {'PT-01': (2.1, 10.6), 'PT-02': (2.1, 6.8), 'PT-03': (6.0, 10.6), 'PT-04': (12.6, 10.6), 'PT-08': (16.9, 10.6),
           'PT-05': (10.0, 6.6), 'PT-06': (13.4, 6.6), 'PT-07': (16.8, 6.6), 'PT-09': (20.6, 6.6)}
    W, Hh = 3.1, 0.7
    nav_zona(L, ax, 0.3, 4.0, 7.6, 8.6, 'Pública')
    nav_zona(L, ax, 8.3, 5.1, 10.4, 7.5, 'Bibliotecaria')
    nav_zona(L, ax, 18.9, 5.4, 3.5, 2.5, 'Dirección')
    nav_inicio(L, ax, 2.1, 12.2)
    nav_transicion(L, ax, [(2.1, 11.95), (2.1, 11.3)], '')
    for cod, (x, y) in pos.items():
        nav_pantalla(L, ax, x, y, cod, X.PANTALLA[cod][1], w=W, h=1.4)
    n = lambda c, dx=0: (pos[c][0] + dx, pos[c][1] + Hh); s_ = lambda c, dx=0: (pos[c][0] + dx, pos[c][1] - Hh)
    e = lambda c, dy=0: (pos[c][0] + W / 2, pos[c][1] + dy); o = lambda c, dy=0: (pos[c][0] - W / 2, pos[c][1] + dy)
    rutas = {
        ('PT-01', 'PT-02'): ([s_('PT-01', -0.6), n('PT-02', -0.6)], (1.0, 8.7)),
        ('PT-02', 'PT-01'): ([n('PT-02', 0.6), s_('PT-01', 0.6)], (3.4, 8.7)),
        ('PT-01', 'PT-03'): ([e('PT-01'), o('PT-03')], (4.05, 11.6)),
        ('PT-03', 'PT-04'): ([e('PT-03'), o('PT-04')], (9.3, 11.6)),
        ('PT-03', 'PT-09'): ([s_('PT-03'), (6.0, 4.5), (20.6, 4.5), s_('PT-09')], (13.0, 4.5)),
        ('PT-04', 'PT-05'): ([s_('PT-04', -1.0), n('PT-05')], (10.4, 8.7)),
        ('PT-04', 'PT-06'): ([s_('PT-04', 0.2), n('PT-06')], (13.4, 8.7)),
        ('PT-04', 'PT-07'): ([s_('PT-04', 1.0), n('PT-07')], (15.6, 8.9)),
        ('PT-04', 'PT-08'): ([e('PT-04'), o('PT-08')], (14.75, 11.6)),
        ('PT-04', 'PT-09'): ([s_('PT-04', 1.4), n('PT-09')], (19.2, 8.6)),
    }
    for a, b, acc in X.TRANSICIONES:
        pts, p = rutas[(a, b)]
        nav_transicion(L, ax, pts, acc, pos=p)
    _guardar(fig, ruta)


# ---------------------------------------------------------------- bocetos
def boc_marco(L, ax, x0, y0, w, h, titulo):
    L.usar('boc_marco')
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor='white', edgecolor=NEGRO, lw=1.4))
    ax.add_patch(Rectangle((x0, y0 + h - 0.6), w, 0.6, facecolor='#EEEEEE', edgecolor=NEGRO, lw=1.4))
    if titulo:
        ax.text(x0 + 0.2, y0 + h - 0.3, titulo, ha='left', va='center', fontsize=8.8, weight='bold', color=NEGRO)


def boc_campo(L, ax, x0, y, w, etiqueta, valor=''):
    L.usar('boc_campo')
    if etiqueta:
        ax.text(x0, y + 0.42, etiqueta, ha='left', va='center', fontsize=7.8, color=NEGRO)
    ax.add_patch(Rectangle((x0, y - 0.22), w, 0.44, facecolor='white', edgecolor=GRIS, lw=1.1))
    if valor:
        ax.text(x0 + 0.12, y, valor, ha='left', va='center', fontsize=7.6, color=GRIS)


def boc_boton(L, ax, x0, y, w, texto, gris=False):
    L.usar('boc_boton')
    ax.add_patch(FancyBboxPatch((x0, y - 0.24), w, 0.48, boxstyle='round,pad=0.02,rounding_size=0.1',
                                facecolor='#E0E0E0' if not gris else '#F5F5F5', edgecolor=GRIS if gris else NEGRO, lw=1.1))
    if texto:
        ax.text(x0 + w / 2, y, texto, ha='center', va='center', fontsize=7.8, color=GRIS if gris else NEGRO, weight='bold')


def boc_mensaje(L, ax, x0, y, w, texto, h=0.75):
    L.usar('boc_mensaje')
    ax.add_patch(Rectangle((x0, y - h / 2), w, h, facecolor='#FAFAFA', edgecolor=NEGRO, lw=1.1, ls=':'))
    if texto:
        ax.text(x0 + 0.12, y, texto, ha='left', va='center', fontsize=7.2, color=NEGRO, wrap=True, linespacing=1.15)


def _pt05(L, ax, x0, y0, estado):
    w, h = 6.2, 5.0
    boc_marco(L, ax, x0, y0, w, h, 'PT-05 Registrar préstamo')
    boc_campo(L, ax, x0 + 0.3, y0 + 3.6, 2.7, 'Código del lector', 'LE-0123' if estado != 'vacío' else '')
    ax.text(x0 + 3.3, y0 + 3.6, ('Lector del caso · estudiante\n1 préstamo activo' if estado != 'vacío' else ''),
            ha='left', va='center', fontsize=7.0, color=GRIS)
    boc_campo(L, ax, x0 + 0.3, y0 + 2.5, 2.7, 'Código del ejemplar', 'EJ-0457' if estado != 'vacío' else '')
    boc_boton(L, ax, x0 + 0.3, y0 + 1.6, 1.7, 'Guardando…' if estado == 'carga' else 'Prestar', gris=(estado == 'carga'))
    boc_boton(L, ax, x0 + 3.5, y0 + 1.6, 2.4, 'Volver al inicio')
    txt = {'vacío': 'Escribí el código del lector para empezar.',
           'carga': X.MENSAJE['ME-11'][4].split(' (')[0].split(' / ')[1],
           'error': 'No se puede prestar: el ejemplar EJ-0457\nya está prestado y vence el 12/03.\nElegí otro ejemplar disponible.',
           'confirmación': X.MENSAJE['ME-04'][4]}[estado]
    boc_mensaje(L, ax, x0 + 0.3, y0 + 0.7, w - 0.6, txt, h=0.95)
    ax.text(x0 + w / 2, y0 - 0.35, 'Estado: ' + estado, ha='center', va='center', fontsize=8.6, weight='bold', color=AMBAR)


def bocetos_tareas(ruta):
    L = Lienzo('fig_8_2', 'boceto')
    fig, ax = plt.subplots(figsize=(11.4, 4.2))
    ax.set_xlim(0, 21); ax.set_ylim(-0.8, 6.2); ax.axis('off'); ax.set_aspect('equal')
    # consulta
    boc_marco(L, ax, 0.2, 0.2, 6.4, 5.6, 'PT-01 y PT-02 Consulta pública')
    boc_campo(L, ax, 0.5, 4.3, 3.9, 'Título o parte del título', 'arroyo')
    boc_boton(L, ax, 4.6, 4.3, 1.7, 'Buscar')
    for k, (t, n) in enumerate((('Cuentos del arroyo Arapoty', '2 disponibles'), ('El arroyo y la escuela', '0 disponibles por ahora'))):
        ax.text(0.5, 3.4 - k * 1.0, t, ha='left', va='center', fontsize=7.8, color=NEGRO)
        ax.text(0.7, 3.0 - k * 1.0, n, ha='left', va='center', fontsize=7.6, color=NEGRO, weight='bold')
    boc_mensaje(L, ax, 0.5, 1.0, 5.8, 'Sin datos de lectores (RNF-03).')
    # préstamo
    boc_marco(L, ax, 7.3, 0.2, 6.4, 5.6, 'PT-05 Registrar préstamo')
    boc_campo(L, ax, 7.6, 4.3, 2.8, 'Código del lector', 'LE-0123')
    ax.text(10.6, 4.3, 'estudiante · 1 activo', ha='left', va='center', fontsize=7.2, color=GRIS)
    boc_campo(L, ax, 7.6, 3.1, 2.8, 'Código del ejemplar', 'EJ-0457')
    boc_boton(L, ax, 7.6, 2.1, 1.7, 'Prestar'); boc_boton(L, ax, 11.0, 2.1, 2.4, 'Volver al inicio')
    boc_mensaje(L, ax, 7.6, 1.0, 5.8, 'Mensaje de la operación')
    # devolución
    boc_marco(L, ax, 14.4, 0.2, 6.4, 5.6, 'PT-06 Registrar devolución')
    boc_campo(L, ax, 14.7, 4.3, 2.8, 'Código del ejemplar', 'EJ-0457')
    ax.text(14.7, 3.3, 'Préstamo 1042 · Lector del caso\nsalió el 02/03 · vence el 09/03', ha='left', va='center', fontsize=7.2, color=GRIS)
    boc_boton(L, ax, 14.6, 2.1, 3.4, 'Confirmar devolución'); boc_boton(L, ax, 18.3, 2.1, 2.3, 'Volver al inicio')
    boc_mensaje(L, ax, 14.7, 1.0, 5.8, 'Mensaje de la operación')
    _guardar(fig, ruta)


def estados_prestamo(ruta):
    L = Lienzo('fig_8_3', 'boceto')
    fig, ax = plt.subplots(figsize=(11.4, 7.6))
    ax.set_xlim(0, 13.4); ax.set_ylim(-0.6, 11.6); ax.axis('off'); ax.set_aspect('equal')
    for k, est in enumerate(('vacío', 'carga', 'error', 'confirmación')):
        _pt05(L, ax, 0.2 + (k % 2) * 6.8, 6.3 - (k // 2) * 6.2, est)
    _guardar(fig, ruta)


# ---------------------------------------------------------------- capas
def capa_banda(L, ax, y, h, nombre, detalle):
    L.usar('capa_banda')
    ax.add_patch(FancyBboxPatch((0.3, y), 15.4, h, boxstyle='round,pad=0.02,rounding_size=0.2', facecolor=LIGHT, edgecolor=MED, lw=1.6))
    ax.text(0.6, y + h - 0.35, nombre, ha='left', va='center', fontsize=11, weight='bold', color=DARK)
    ax.text(0.6, y + 0.4, detalle, ha='left', va='center', fontsize=8.6, color='#333333')


def capa_operacion(L, ax, x, y1, y2, rotulo):
    L.usar('capa_operacion')
    ax.add_patch(FancyArrowPatch((x, y1), (x, y2), arrowstyle='-|>', mutation_scale=12, color=NEGRO, lw=1.3))
    ax.text(x + 0.15, (y1 + y2) / 2, rotulo, ha='left', va='center', fontsize=8.2, color=NEGRO, weight='bold')


def esquema_capas(ruta):
    L = Lienzo('fig_9_1', 'capas')
    fig, ax = plt.subplots(figsize=(10.8, 5.0))
    ax.set_xlim(0, 16); ax.set_ylim(0, 7.4); ax.axis('off')
    ys = {'Presentación': 5.6, 'Reglas de negocio': 3.0, 'Persistencia': 0.4}
    for nombre, que, det in X.CAPAS:
        capa_banda(L, ax, ys[nombre], 1.6, nombre, que + '  (' + det + ')')
    for k, op in enumerate(X.OPERACIONES):
        x = 3.3 + k * 2.1
        capa_operacion(L, ax, x, 5.55, 4.65, op[0])
        capa_operacion(L, ax, x + 0.5, 2.95, 2.05, '')
    ax.text(0.45, 5.1, 'la pantalla pide', ha='left', va='center', fontsize=8.2, color=GRIS, style='italic')
    ax.text(0.45, 2.5, 'las reglas leen\ny guardan', ha='left', va='center', fontsize=8.2, color=GRIS, style='italic')
    _guardar(fig, ruta)


# ---------------------------------------------------------------- esquemas didácticos
def obra_ejemplares(ruta):
    Lienzo('fig_7_2', 'esquema')
    fig, ax = plt.subplots(figsize=(10.6, 3.9))
    ax.set_xlim(0, 16); ax.set_ylim(0, 6); ax.axis('off')
    def caja(x, y, w, h, t, s, borde=MED):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03,rounding_size=0.15', facecolor=LIGHT, edgecolor=borde, lw=1.5))
        ax.text(x + w / 2, y + h - 0.35, t, ha='center', va='center', fontsize=9.6, weight='bold', color=DARK)
        ax.text(x + w / 2, y + 0.42, s, ha='center', va='center', fontsize=8.0, color='#333333')
    caja(5.6, 4.4, 4.8, 1.3, 'Obra OB-0031', '«Cuentos del arroyo Arapoty»')
    for k, (e, s) in enumerate((('Edición ED-0045', 'editorial del caso, 2019'), ('Edición ED-0052', 'otra editorial, 2023'))):
        caja(1.6 + k * 8.0, 2.4, 4.8, 1.3, e, s)
        ax.plot([8.0, 4.0 + k * 8.0], [4.4, 3.7], color=MED, lw=1.3)
    ejs = [('EJ-0457', 'prestado'), ('EJ-0458', 'disponible'), ('EJ-0459', 'inactivo'), ('EJ-0512', 'disponible')]
    for k, (e, s) in enumerate(ejs):
        x = 0.3 + k * 4.0
        caja(x, 0.2, 3.2, 1.3, e, s, borde=AMBAR if s == 'prestado' else MED)
        ax.plot([x + 1.6, 4.0 if k < 3 else 12.0], [1.5, 2.4], color=MED, lw=1.1)
    ax.text(15.9, 5.4, 'La consulta pública suma\nlos disponibles de la obra:\n2 disponibles', ha='right', va='center', fontsize=8.6, color=GRIS, style='italic')
    _guardar(fig, ruta)


def historial(ruta):
    Lienzo('fig_7_3', 'esquema')
    fig, ax = plt.subplots(figsize=(10.6, 2.9))
    ax.set_xlim(0, 16); ax.set_ylim(0, 4.2); ax.axis('off')
    ax.plot([0.5, 15.5], [1.62, 1.62], color=GRIS, lw=2)
    tramos = [(1.0, 4.2, '1042', '02/03 → 07/03', 'devuelto'), (5.2, 8.6, '1077', '10/03 → 16/03', 'devuelto'),
              (9.6, 14.8, '1103', '18/03 → (sin devolución)', 'activo')]
    for a, b, n, f, est in tramos:
        c = AMBAR if est == 'activo' else MED
        ax.add_patch(Rectangle((a, 1.7), b - a, 0.6, facecolor=LIGHT, edgecolor=c, lw=1.6))
        ax.text((a + b) / 2, 2.0, 'Préstamo ' + n, ha='center', va='center', fontsize=8.6, weight='bold', color=DARK)
        ax.text((a + b) / 2, 1.2, f, ha='center', va='center', fontsize=8.0, color='#333333')
        ax.text((a + b) / 2, 0.75, est, ha='center', va='center', fontsize=8.0, color=c, style='italic')
    ax.text(0.5, 3.4, 'Historial del ejemplar EJ-0457: cada devolución cierra su préstamo; ninguno se borra. Solo uno puede estar activo (RI-01).',
            ha='left', va='center', fontsize=8.8, color=GRIS, style='italic')
    _guardar(fig, ruta)


# ---------------------------------------------------------------- símbolos para las leyendas
def simbolo(nombre, ruta):
    L = Lienzo('leyenda:' + nombre, SIMBOLOS[nombre][0])
    fig, ax = plt.subplots(figsize=(1.6, 0.9))
    ax.set_xlim(0, 4); ax.set_ylim(0, 2.25); ax.axis('off'); ax.set_aspect('equal')
    f = {'der_entidad': lambda: der_entidad(L, ax, 2, 1.12, '', w=3.0, h=1.1),
         'der_relacion': lambda: der_relacion(L, ax, 2, 1.12, '', w=3.0, h=1.4),
         'der_cardinalidad': lambda: der_cardinalidad(L, ax, 2, 1.12, '1   N'),
         'der_linea': lambda: der_linea(L, ax, (0.4, 1.12), (3.6, 1.12)),
         'nav_pantalla': lambda: nav_pantalla(L, ax, 2, 1.12, '', '', w=3.0, h=1.2),
         'nav_transicion': lambda: nav_transicion(L, ax, [(0.3, 1.12), (3.7, 1.12)], ''),
         'nav_inicio': lambda: nav_inicio(L, ax, 2, 1.12),
         'nav_zona': lambda: nav_zona(L, ax, 0.4, 0.2, 3.2, 1.85, ''),
         'boc_marco': lambda: boc_marco(L, ax, 0.4, 0.2, 3.2, 1.85, ''),
         'boc_campo': lambda: boc_campo(L, ax, 0.4, 0.9, 3.2, 'Etiqueta'),
         'boc_boton': lambda: boc_boton(L, ax, 1.0, 1.12, 2.0, 'Acción'),
         'boc_mensaje': lambda: boc_mensaje(L, ax, 0.4, 1.12, 3.2, ''),
         'capa_banda': lambda: (L.usar('capa_banda'), ax.add_patch(FancyBboxPatch((0.4, 0.5), 3.2, 1.2, boxstyle='round,pad=0.02,rounding_size=0.2', facecolor=LIGHT, edgecolor=MED, lw=1.6))),
         'capa_operacion': lambda: capa_operacion(L, ax, 2.0, 2.0, 0.3, '')}[nombre]
    f()
    _guardar(fig, ruta)


def generar(carpeta=None):
    d = carpeta or os.path.join(AQUI, 'figs')
    os.makedirs(d, exist_ok=True)
    REGISTRO.clear()
    r = {'fig_7_1': os.path.join(d, 'fig_7_1_modelo_de_datos.png'), 'fig_7_2': os.path.join(d, 'fig_7_2_obra_ediciones_ejemplares.png'),
         'fig_7_3': os.path.join(d, 'fig_7_3_historial_del_ejemplar.png'), 'fig_8_1': os.path.join(d, 'fig_8_1_mapa_de_navegacion.png'),
         'fig_8_2': os.path.join(d, 'fig_8_2_bocetos_de_tres_tareas.png'), 'fig_8_3': os.path.join(d, 'fig_8_3_estados_de_una_pantalla.png'),
         'fig_9_1': os.path.join(d, 'fig_9_1_esquema_de_capas.png')}
    modelo_datos(r['fig_7_1']); obra_ejemplares(r['fig_7_2']); historial(r['fig_7_3'])
    mapa_navegacion(r['fig_8_1']); bocetos_tareas(r['fig_8_2']); estados_prestamo(r['fig_8_3']); esquema_capas(r['fig_9_1'])
    for s in SIMBOLOS:
        r['sim:' + s] = os.path.join(d, 'simbolo_%s.png' % s)
        simbolo(s, r['sim:' + s])
    json.dump(REGISTRO, open(os.path.join(d, 'simbolos.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    return r


if __name__ == '__main__':
    print(generar())
