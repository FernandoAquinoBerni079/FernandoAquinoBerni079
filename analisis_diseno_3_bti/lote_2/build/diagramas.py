# -*- coding: utf-8 -*-
"""Figuras del lote 2 (Capítulos 4 a 6), generadas por código con matplotlib; sin recursos de terceros.

Capítulo 4: Figuras 4.1 y 4.2, con el mismo código del Capítulo 4 v2 (`fase2_pilotos/A2_capitulo4_v2/build/diagramas.py`);
la cadena de la Figura 4.2 toma N-02 de la fuente única del caso.

Capítulo 5: dibujo POR NOTACIÓN (`lote_2_plan/NOTACIONES_CAPITULO_5.md`, §4). Cada figura declara su notación y solo
puede usar las funciones de esa notación: actividad_* (nodo inicial, acción, decisión, flujo, nodo final, carril),
contexto_* (sistema, entidad, flujo) y cu_* (actor, caso, límite, asociación). Cada función registra el símbolo que
dibuja; si una figura llama a una función de otra notación, la generación se detiene. El registro se guarda en
figs/simbolos.json y lo controla build/verificar.py. Las figuras se dibujan desde los datos de caso/modelos.py.
Las leyendas de símbolos (libro y guía) se dibujan con las mismas funciones.

Capítulo 6: esquemas didácticos (cadena de trazabilidad e impacto de un cambio), que no usan ninguna notación UML."""
import os, sys, json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon, Ellipse, Rectangle

AQUI = os.path.dirname(os.path.abspath(__file__))
L2 = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(L2, 'caso'))
import requisitos as R
import modelos as MO
D = R.D

plt.rcParams.update({'font.family': 'DejaVu Sans'})
DARK, MED, SOFT, LIGHT = '#1B5E20', '#2E7D32', '#43A047', '#E8F5E9'
AMBAR, GRIS, NEGRO = '#B8860B', '#616161', '#212121'


# ================================================================ Capítulo 4 (código del piloto v2)
CADENA = [
    ('Necesidad\nN-02', 'Evitar entregar a dos\nlectores el mismo\nejemplar (E4-L4)'),
    ('Regla\nRN-01', 'Un ejemplar solo puede\ntener un préstamo\nactivo'),
    ('Requisito\nRF-04', 'Rechazar el préstamo\nde un ejemplar que ya\nestá prestado'),
    ('Aceptación\nCA-04', 'Dado… cuando…\nentonces se rechaza y\nqueda un solo préstamo'),
    ('Prueba\nP-07', 'Segunda solicitud sobre\nel mismo ejemplar:\nrechazo comprobado'),
]


def _caja4(ax, x, y, w, h, titulo, texto, borde=MED, fondo=LIGHT):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03,rounding_size=0.12',
                                facecolor=fondo, edgecolor=borde, lw=1.6))
    ax.text(x + w / 2, y + h - (0.38 if texto else h / 2), titulo, ha='center', va='center', fontsize=10, weight='bold', color=DARK)
    ax.text(x + w / 2, y + 0.62, texto, ha='center', va='center', fontsize=8.2, color='#333333')


def cadena_trazabilidad(ruta):
    fig, ax = plt.subplots(figsize=(11.5, 3.2))
    ax.set_xlim(0, 11.5); ax.set_ylim(0, 2.5); ax.axis('off')
    w, h, y = 2.0, 1.75, 0.6
    xs = [0.15 + i * 2.3 for i in range(len(CADENA))]
    for x, (t, s) in zip(xs, CADENA):
        _caja4(ax, x, y, w, h, t, s)
    for a, b in zip(xs[:-1], xs[1:]):
        ax.add_patch(FancyArrowPatch((a + w + 0.02, y + h / 2), (b - 0.02, y + h / 2),
                                     arrowstyle='-|>', mutation_scale=14, color=MED, lw=1.6))
    ax.text(5.75, 0.18, 'Capítulo 4: N, RN, RF y criterio de aceptación  ·  Capítulos 14 a 16: la prueba',
            ha='center', va='center', fontsize=8.6, color=GRIS, style='italic')
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)


TIPOS = [
    ('Funcionales', 'Qué hace el sistema', 'RF-04: rechazar el préstamo\nde un ejemplar ya prestado'),
    ('De calidad', 'Qué tan bien lo hace', 'RNF-01: la bibliotecaria lo usa\nsin ayuda tras una práctica'),
    ('Restricciones', 'Qué condiciones limitan\nla solución', 'RS-01: funciona sin internet\nen la computadora de la biblioteca'),
]


def tipos_requisito(ruta):
    fig, ax = plt.subplots(figsize=(10.5, 4.6))
    ax.set_xlim(0, 10.5); ax.set_ylim(0, 4.6); ax.axis('off')
    _caja4(ax, 3.55, 3.35, 3.4, 0.75, 'Requisitos', '', borde=DARK)
    xs = [0.15, 3.6, 7.05]
    for x, (t, q, e) in zip(xs, TIPOS):
        ax.add_patch(FancyArrowPatch((5.25, 3.33), (x + 1.65, 2.62), arrowstyle='-|>', mutation_scale=13, color=MED, lw=1.4))
        ax.add_patch(FancyBboxPatch((x, 0.75), 3.3, 1.85, boxstyle='round,pad=0.03,rounding_size=0.12',
                                    facecolor=LIGHT, edgecolor=MED, lw=1.5))
        ax.text(x + 1.65, 2.3, t, ha='center', va='center', fontsize=11, weight='bold', color=DARK)
        ax.text(x + 1.65, 1.82, q, ha='center', va='center', fontsize=8.8, color=GRIS, style='italic')
        ax.text(x + 1.65, 1.15, e, ha='center', va='center', fontsize=8.4, color='#333333')
    ax.text(5.25, 0.25, 'Las reglas de negocio (RN) son de la organización: existen aunque no haya sistema; '
            'los requisitos dicen cómo el sistema las hace cumplir.', ha='center', va='center', fontsize=8.6, color=AMBAR, style='italic')
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)


# ================================================================ Capítulo 5: registro de símbolos por notación
NOTACIONES = {'actividad': 'Diagrama de actividades UML con particiones',
              'contexto': 'Diagrama de contexto',
              'casos_de_uso': 'Diagrama de casos de uso UML'}
# símbolo → (notación, nombre, significado, regla de uso): tabla del §2 de NOTACIONES_CAPITULO_5.md
SIMBOLOS = {
    'actividad_inicial': ('actividad', 'Nodo inicial', 'Donde empieza el proceso', 'Uno por diagrama'),
    'actividad_accion': ('actividad', 'Acción', 'Una tarea que hace un participante', 'Verbo en infinitivo y objeto: «Registrar el préstamo»'),
    'actividad_decision': ('actividad', 'Decisión (y fusión)', 'El camino se divide según una condición, o se vuelve a unir', 'Cada salida lleva su guarda entre corchetes: «[ya prestado]»'),
    'actividad_flujo': ('actividad', 'Flujo', 'El orden en que se suceden las acciones', 'Sin rótulo, salvo las guardas que salen de una decisión'),
    'actividad_final': ('actividad', 'Nodo final', 'Donde termina el proceso', 'Puede haber más de uno'),
    'actividad_carril': ('actividad', 'Partición (carril)', 'El responsable de las acciones de esa columna', 'Una por participante; en el proceso propuesto se agrega «Sistema»'),
    'contexto_sistema': ('contexto', 'Sistema', 'El sistema de préstamos, visto como un todo', 'Uno por diagrama, con su nombre'),
    'contexto_entidad': ('contexto', 'Entidad externa', 'Persona, rol o sistema que da o recibe información y queda fuera del límite', 'Solo si intercambia información con el sistema'),
    'contexto_flujo': ('contexto', 'Flujo de información', 'Un dato o documento que va en un sentido', 'Rótulo con sustantivo: «informe mensual por curso»; nunca un verbo'),
    'cu_actor': ('casos_de_uso', 'Actor', 'Un rol que usa el sistema, no una persona concreta', '«Bibliotecaria», «Lector»; nunca un nombre propio'),
    'cu_caso': ('casos_de_uso', 'Caso de uso', 'Un objetivo del actor que el sistema cumple', 'Verbo y objeto: «Registrar préstamo»'),
    'cu_limite': ('casos_de_uso', 'Límite del sistema', 'Lo que queda adentro es responsabilidad del sistema', 'Los actores quedan afuera'),
    'cu_asociacion': ('casos_de_uso', 'Asociación', 'El actor participa en el caso de uso', 'Línea sin flecha ni rótulo'),
}
REGISTRO = {}   # figura → {'notacion': ..., 'simbolos': {símbolo: veces}, 'datos': {...}}


class Lienzo:
    def __init__(self, figura, notacion):
        assert notacion in NOTACIONES or notacion == 'esquema', notacion
        self.figura, self.notacion = figura, notacion
        self.simbolos = {}
        REGISTRO[figura] = {'notacion': notacion, 'simbolos': self.simbolos}

    def usar(self, simbolo):
        assert SIMBOLOS[simbolo][0] == self.notacion, 'la figura %s (%s) no puede usar %s' % (self.figura, self.notacion, simbolo)
        self.simbolos[simbolo] = self.simbolos.get(simbolo, 0) + 1


# ---------------------------------------------------------------- diagrama de actividades
AW, AH, DS = 4.1, 1.45, 0.45     # ancho y alto de una acción; semilado del rombo
RI = 0.24                        # radio del nodo inicial


def actividad_carril(L, ax, x0, w, y0, h, nombre):
    L.usar('actividad_carril')
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor='none', edgecolor=GRIS, lw=1.1))
    ax.add_patch(Rectangle((x0, y0 + h - 0.75), w, 0.75, facecolor='#F2F2F2', edgecolor=GRIS, lw=1.1))
    ax.text(x0 + w / 2, y0 + h - 0.375, nombre, ha='center', va='center', fontsize=11, weight='bold', color=NEGRO)


def actividad_inicial(L, ax, x, y):
    L.usar('actividad_inicial')
    ax.add_patch(Circle((x, y), RI, facecolor=NEGRO, edgecolor=NEGRO))


def actividad_final(L, ax, x, y):
    L.usar('actividad_final')
    ax.add_patch(Circle((x, y), RI + 0.04, facecolor='white', edgecolor=NEGRO, lw=1.5))
    ax.add_patch(Circle((x, y), RI - 0.09, facecolor=NEGRO, edgecolor=NEGRO))


def actividad_accion(L, ax, x, y, texto, w=AW, h=AH, fs=8.2):
    L.usar('actividad_accion')
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0.02,rounding_size=0.35',
                                facecolor=LIGHT, edgecolor=MED, lw=1.5))
    if texto:
        ax.text(x, y, texto, ha='center', va='center', fontsize=fs, color=NEGRO, linespacing=1.15)


def actividad_decision(L, ax, x, y, s=DS):
    L.usar('actividad_decision')
    ax.add_patch(Polygon([(x, y + s), (x + s, y), (x, y - s), (x - s, y)], closed=True,
                         facecolor='white', edgecolor=NEGRO, lw=1.4))


def actividad_flujo(L, ax, puntos, guarda=None, pos_guarda=None):
    L.usar('actividad_flujo')
    for a, b in zip(puntos[:-2], puntos[1:-1]):
        ax.plot([a[0], b[0]], [a[1], b[1]], color=NEGRO, lw=1.25, solid_capstyle='butt')
    ax.add_patch(FancyArrowPatch(puntos[-2], puntos[-1], arrowstyle='-|>', mutation_scale=12, color=NEGRO, lw=1.25,
                                 shrinkA=0, shrinkB=0))
    if guarda:
        x, y, ha = pos_guarda
        ax.text(x, y, guarda, ha=ha, va='bottom', fontsize=8.8, color=NEGRO, style='italic')


def _bordes(tipo, x, y):
    """Puntos de salida y de llegada de un nodo: (arriba, abajo, izquierda, derecha)."""
    if tipo == 'accion':
        return (x, y + AH / 2), (x, y - AH / 2), (x - AW / 2, y), (x + AW / 2, y)
    if tipo == 'decision':
        return (x, y + DS), (x, y - DS), (x - DS, y), (x + DS, y)
    r = RI + 0.04
    return (x, y + r), (x, y - r), (x - r, y), (x + r, y)


def proceso(modelo, ruta, clave, anchos=None, ejes=None, paso=1.85):
    L = Lienzo(clave, modelo['notacion'])
    car = modelo['carriles']
    anchos = anchos or [4.6] * len(car)
    filas = max(n[3] for n in modelo['nodos'])
    alto = 1.3 + (filas + 0.55) * paso
    W = sum(anchos)
    fig, ax = plt.subplots(figsize=(W * 0.43, alto * 0.43))
    ax.set_xlim(-0.05, W + 0.05); ax.set_ylim(-0.05, alto + 0.05); ax.axis('off'); ax.set_aspect('equal')
    x0 = 0; centro = {}; ejes = ejes or {}
    for nombre, w in zip(car, anchos):
        actividad_carril(L, ax, x0, w, 0, alto, nombre)
        centro[nombre] = x0 + w * ejes.get(nombre, 0.5); x0 += w
    top = alto - 0.75 - 0.55
    pos = {}
    for nid, tipo, carril, fila, dx, texto in modelo['nodos']:
        assert carril in centro, (nid, carril)
        x = centro[carril] + dx * AW; y = top - fila * paso
        pos[nid] = (tipo, x, y)
        {'inicial': lambda: actividad_inicial(L, ax, x, y), 'final': lambda: actividad_final(L, ax, x, y),
         'decision': lambda: actividad_decision(L, ax, x, y),
         'accion': lambda: actividad_accion(L, ax, x, y, texto)}[tipo]()
    for a, b, guarda in modelo['flujos']:
        ta, xa, ya = pos[a]; tb, xb, yb = pos[b]
        arr_b = _bordes(tb, xb, yb)[0]
        ab_a, iz_a, de_a = _bordes(ta, xa, ya)[1:]
        if ta == 'decision' and abs(xb - xa) > 0.01:
            inicio = de_a if xb > xa else iz_a
            pts = [inicio, (xb, inicio[1]), arr_b]
            pg = ((inicio[0] + 0.12, inicio[1] + 0.06, 'left') if xb > xa else (inicio[0] - 0.12, inicio[1] + 0.06, 'right'))
        elif abs(xb - xa) < 0.01:
            pts = [ab_a, arr_b]
            pg = (xa + 0.14, (ab_a[1] + arr_b[1]) / 2 - 0.12, 'left')
        else:
            ym = arr_b[1] + 0.32 if tb != 'accion' or ab_a[1] - arr_b[1] < 1.2 else (ab_a[1] + arr_b[1]) / 2
            pts = [ab_a, (xa, ym), (xb, ym), arr_b]
            pg = (xa + 0.14, ab_a[1] - 0.3, 'left')
        actividad_flujo(L, ax, pts, guarda, pg)
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white'); plt.close(fig)
    REGISTRO[clave]['datos'] = modelo['titulo']


# ---------------------------------------------------------------- diagrama de contexto
def contexto_sistema(L, ax, x, y, r, texto):
    L.usar('contexto_sistema')
    ax.add_patch(Circle((x, y), r, facecolor=LIGHT, edgecolor=MED, lw=2.0))
    ax.text(x, y, texto, ha='center', va='center', fontsize=10.5, weight='bold', color=DARK, linespacing=1.2)


def contexto_entidad(L, ax, x, y, w, h, texto):
    L.usar('contexto_entidad')
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, facecolor='white', edgecolor=NEGRO, lw=1.5))
    ax.text(x, y, texto, ha='center', va='center', fontsize=11, weight='bold', color=NEGRO)


def contexto_flujo(L, ax, a, b, rotulo, rad=0.0, pos=0.5, desp=(0, 0)):
    L.usar('contexto_flujo')
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=13, color=NEGRO, lw=1.3,
                                 connectionstyle='arc3,rad=%s' % rad, shrinkA=0, shrinkB=0))
    if rotulo:
        x = a[0] + (b[0] - a[0]) * pos + desp[0]; y = a[1] + (b[1] - a[1]) * pos + desp[1]
        ax.text(x, y, rotulo, ha='center', va='center', fontsize=9, color=NEGRO, style='italic')


def contexto(modelo, ruta, clave):
    """Sistema al centro; cada entidad en un lado (izquierda, derecha o abajo) y sus flujos en paralelo, ortogonales."""
    import math
    L = Lienzo(clave, modelo['notacion'])
    fig, ax = plt.subplots(figsize=(11.0, 5.5))
    ax.set_xlim(0, 19); ax.set_ylim(0, 9.4); ax.axis('off'); ax.set_aspect('equal')
    cx, cy, r = 9.5, 6.7, 2.3
    contexto_sistema(L, ax, cx, cy, r, modelo['sistema'])
    lado = {'Bibliotecaria': 'izquierda', 'Lector': 'derecha', 'Dirección': 'abajo'}
    por = {}
    for o, d, rot, _ in modelo['flujos']:
        e = d if o == 'Sistema' else o
        por.setdefault(e, []).append((o, rot))
    for e in modelo['entidades']:
        fl = por[e]; n = len(fl); lugar = lado[e]
        if lugar in ('izquierda', 'derecha'):
            sep = 0.95
            h = max(1.3, sep * n + 0.4); w = 3.0
            x0 = 0.2 if lugar == 'izquierda' else 19 - 0.2 - w
            contexto_entidad(L, ax, x0 + w / 2, cy, w, h, e)
            borde = x0 + w if lugar == 'izquierda' else x0
            for k, (o, rot) in enumerate(fl):
                y = cy + ((n - 1) / 2 - k) * sep
                xc = cx - math.sqrt(r * r - (y - cy) ** 2) if lugar == 'izquierda' else cx + math.sqrt(r * r - (y - cy) ** 2)
                a, b = ((xc, y), (borde, y)) if o == 'Sistema' else ((borde, y), (xc, y))
                contexto_flujo(L, ax, a, b, rot, pos=0.5, desp=(0, 0.26))
        else:
            sep = 1.3; w = 3.0; h = 1.2
            contexto_entidad(L, ax, cx, 0.95, w, h, e)
            for k, (o, rot) in enumerate(fl):
                x = cx + (k - (n - 1) / 2) * sep
                yc = cy - math.sqrt(r * r - (x - cx) ** 2)
                a, b = ((x, yc), (x, 0.95 + h / 2)) if o == 'Sistema' else ((x, 0.95 + h / 2), (x, yc))
                L.usar('contexto_flujo')
                ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=13, color=NEGRO, lw=1.3, shrinkA=0, shrinkB=0))
                izq = k < (n - 1) / 2 + 0.01 and k == 0
                ax.text(x + (-0.2 if izq else 0.2), (a[1] + b[1]) / 2, rot, ha='right' if izq else 'left', va='center',
                        fontsize=9, color=NEGRO, style='italic')
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white'); plt.close(fig)
    REGISTRO[clave]['datos'] = modelo['titulo']


# ---------------------------------------------------------------- diagrama de casos de uso
def cu_actor(L, ax, x, y, nombre, s=1.0):
    L.usar('cu_actor')
    ax.add_patch(Circle((x, y + 0.95 * s), 0.27 * s, facecolor='white', edgecolor=NEGRO, lw=1.5))
    ax.plot([x, x], [y + 0.68 * s, y - 0.1 * s], color=NEGRO, lw=1.5)
    ax.plot([x - 0.45 * s, x + 0.45 * s], [y + 0.45 * s, y + 0.45 * s], color=NEGRO, lw=1.5)
    ax.plot([x, x - 0.38 * s], [y - 0.1 * s, y - 0.75 * s], color=NEGRO, lw=1.5)
    ax.plot([x, x + 0.38 * s], [y - 0.1 * s, y - 0.75 * s], color=NEGRO, lw=1.5)
    if nombre:
        ax.text(x, y - 1.0 * s, nombre, ha='center', va='top', fontsize=10.5, weight='bold', color=NEGRO)


def cu_caso(L, ax, x, y, texto, w=4.1, h=1.25):
    L.usar('cu_caso')
    ax.add_patch(Ellipse((x, y), w, h, facecolor=LIGHT, edgecolor=MED, lw=1.5))
    if texto:
        ax.text(x, y, texto, ha='center', va='center', fontsize=9.6, color=NEGRO, linespacing=1.1)


def cu_limite(L, ax, x0, y0, w, h, nombre):
    L.usar('cu_limite')
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor='none', edgecolor=NEGRO, lw=1.6))
    if nombre:
        ax.text(x0 + w / 2, y0 + h - 0.35, nombre, ha='center', va='center', fontsize=10.5, weight='bold', color=NEGRO)


def cu_asociacion(L, ax, a, b):
    L.usar('cu_asociacion')
    ax.plot([a[0], b[0]], [a[1], b[1]], color=NEGRO, lw=1.3)


def casos_de_uso(modelo, ruta, clave):
    L = Lienzo(clave, modelo['notacion'])
    fig, ax = plt.subplots(figsize=(10.0, 7.6))
    ax.set_xlim(0, 15); ax.set_ylim(0, 11.4); ax.axis('off'); ax.set_aspect('equal')
    lx0, ly0, lw, lh = 4.0, 0.4, 7.0, 10.6
    cu_limite(L, ax, lx0, ly0, lw, lh, modelo['limite'])
    ys = [9.0, 7.2, 5.4, 3.6, 1.8]
    pcaso = {}
    for (cid, nom), y in zip(modelo['casos'], ys):
        cu_caso(L, ax, lx0 + lw / 2, y, nom)
        pcaso[cid] = (lx0 + lw / 2, y)
    pact = {'Bibliotecaria': (1.7, 5.6), 'Lector': (13.3, 6.6), 'Dirección': (13.3, 2.6)}
    for a in modelo['actores']:
        cu_actor(L, ax, *pact[a], a)
    for a, c in modelo['asociaciones']:
        ax_, ay = pact[a]; cx, cy = pcaso[c]
        ini = (ax_ + 0.55, ay + 0.35) if ax_ < cx else (ax_ - 0.55, ay + 0.35)
        fin = (cx - 2.05, cy) if ax_ < cx else (cx + 2.05, cy)
        cu_asociacion(L, ax, ini, fin)
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white'); plt.close(fig)
    REGISTRO[clave]['datos'] = modelo['titulo']


# ---------------------------------------------------------------- leyendas (un símbolo por imagen)
def simbolo(nombre, ruta):
    notac = SIMBOLOS[nombre][0]
    L = Lienzo('leyenda:' + nombre, notac)
    fig, ax = plt.subplots(figsize=(1.6, 0.9))
    ax.set_xlim(0, 4); ax.set_ylim(0, 2.25); ax.axis('off'); ax.set_aspect('equal')
    if nombre == 'actividad_inicial':
        actividad_inicial(L, ax, 2, 1.12)
    elif nombre == 'actividad_final':
        actividad_final(L, ax, 2, 1.12)
    elif nombre == 'actividad_accion':
        actividad_accion(L, ax, 2, 1.12, '', w=3.0, h=1.2)
    elif nombre == 'actividad_decision':
        actividad_decision(L, ax, 2, 1.12, s=0.7)
    elif nombre == 'actividad_flujo':
        actividad_flujo(L, ax, [(0.4, 1.12), (3.6, 1.12)])
    elif nombre == 'actividad_carril':
        ax.add_patch(Rectangle((1.1, 0.1), 1.8, 2.05, facecolor='none', edgecolor=GRIS, lw=1.1)); L.usar('actividad_carril')
        ax.add_patch(Rectangle((1.1, 1.6), 1.8, 0.55, facecolor='#F2F2F2', edgecolor=GRIS, lw=1.1))
    elif nombre == 'contexto_sistema':
        contexto_sistema(L, ax, 2, 1.12, 0.95, '')
    elif nombre == 'contexto_entidad':
        contexto_entidad(L, ax, 2, 1.12, 2.8, 1.1, '')
    elif nombre == 'contexto_flujo':
        contexto_flujo(L, ax, (0.3, 1.12), (3.7, 1.12), '')
    elif nombre == 'cu_actor':
        cu_actor(L, ax, 2, 0.95, '', s=0.95)
    elif nombre == 'cu_caso':
        cu_caso(L, ax, 2, 1.12, '', w=3.2, h=1.3)
    elif nombre == 'cu_limite':
        cu_limite(L, ax, 0.5, 0.15, 3.0, 1.95, '')
    elif nombre == 'cu_asociacion':
        cu_asociacion(L, ax, (0.4, 1.12), (3.6, 1.12))
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white', pad_inches=0.02); plt.close(fig)


# ================================================================ Capítulo 6: esquemas
def _caja6(ax, x, y, w, h, titulo, texto, borde=MED, fondo=LIGHT, ft=10, fx=8.2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03,rounding_size=0.12',
                                facecolor=fondo, edgecolor=borde, lw=1.6))
    ax.text(x + w / 2, y + h - 0.36, titulo, ha='center', va='center', fontsize=ft, weight='bold', color=DARK)
    ax.text(x + w / 2, y + (h - 0.5) / 2, texto, ha='center', va='center', fontsize=fx, color='#333333', linespacing=1.15)


CADENA_6 = [
    ('Necesidad N-02', 'Evitar entregar a\ndos lectores el\nmismo ejemplar'),
    ('Regla RN-01', 'Un ejemplar solo\npuede tener un\npréstamo activo'),
    ('Requisito RF-04', 'Rechazar el préstamo\nde un ejemplar\nya prestado'),
    ('Caso de uso CU-01', 'Flujo alternativo 5a:\nel ejemplar ya tiene\nun préstamo activo'),
    ('Criterio CA-04', 'Se rechaza y queda\nun solo préstamo\nactivo, el original'),
    ('Prueba P-07', 'Segunda solicitud\nsobre el mismo\nejemplar'),
]


def cadena_extendida(ruta):
    L = Lienzo('fig_6_1', 'esquema')
    fig, ax = plt.subplots(figsize=(12.6, 2.9))
    ax.set_xlim(0, 12.6); ax.set_ylim(0, 2.4); ax.axis('off')
    w, h, y = 1.72, 1.55, 0.72
    xs = [0.1 + i * 2.12 for i in range(len(CADENA_6))]
    for i, (x, (t, s)) in enumerate(zip(xs, CADENA_6)):
        _caja6(ax, x, y, w, h, t, s, borde=AMBAR if i == 3 else MED, fx=8.0, ft=9.2)
    for a, b in zip(xs[:-1], xs[1:]):
        ax.add_patch(FancyArrowPatch((a + w + 0.02, y + h / 2), (b - 0.02, y + h / 2), arrowstyle='<|-|>',
                                     mutation_scale=12, color=MED, lw=1.4))
    ax.text(6.3, 0.28, 'Hacia adelante: qué hay que construir y probar  ·  Hacia atrás: por qué existe cada cosa. '
            'En ámbar, el eslabón que agrega el Capítulo 5.', ha='center', va='center', fontsize=8.6, color=GRIS, style='italic')
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white'); plt.close(fig)
    REGISTRO['fig_6_1']['datos'] = 'cadena N-02 → P-07'


def impacto_cambio(ruta):
    L = Lienzo('fig_6_2', 'esquema')
    fig, ax = plt.subplots(figsize=(11.6, 5.4))
    ax.set_xlim(0, 11.6); ax.set_ylim(0, 5.4); ax.axis('off')
    _caja6(ax, 0.1, 2.0, 2.0, 1.5, 'SC-01', 'Nota D3 de\nla dirección', borde=DARK, fondo='white')
    fila1 = [('RN-02', 'modificada:\ndocentes, hasta 5'), ('RF-05', 'sin cambio de\ntexto: «máximo\nvigente»'),
             ('CU-01', 'paso 4 y\nflujo 4b'), ('Criterio y P-06', 'P-06a estudiante\nP-06b docente')]
    fila2 = [('RF-11', 'nuevo: tipo\nde lector'), ('Incremento 2', 'un dato más\ndel lector'), ('Capítulo 7', 'el modelo de datos\nincluye el tipo')]
    est1 = [AMBAR, GRIS, AMBAR, AMBAR]; est2 = [DARK, AMBAR, GRIS]
    for k, ((t, s), c) in enumerate(zip(fila1, est1)):
        x = 2.75 + k * 2.2
        _caja6(ax, x, 3.25, 1.9, 1.55, t, s, borde=c, fondo='white' if c == GRIS else LIGHT, fx=8.0, ft=9.4)
        a = (2.12, 3.1) if k == 0 else (x - 0.3 + 0.0, 4.02)
        ax.add_patch(FancyArrowPatch(a if k else (2.12, 3.0), (x - 0.02, 4.02), arrowstyle='-|>', mutation_scale=12, color=MED, lw=1.4))
    for k, ((t, s), c) in enumerate(zip(fila2, est2)):
        x = 2.75 + k * 2.2
        _caja6(ax, x, 0.95, 1.9, 1.55, t, s, borde=c, fondo='white' if c == GRIS else LIGHT, fx=8.0, ft=9.4)
        a = (2.12, 2.4) if k == 0 else (x - 0.3, 1.72)
        ax.add_patch(FancyArrowPatch(a, (x - 0.02, 1.72), arrowstyle='-|>', mutation_scale=12, color=MED, lw=1.4))
    for (x1, y1), (x2, y2) in (((2.75 + 1.9, 4.02), (2.75 + 2.2, 4.02)), ((2.75 + 3.2 * 1.375 - 0.02, 4.02), (2.75 + 4.4 - 0.02, 4.02))):
        pass
    for x, y, c, t in ((0.3, 0.32, AMBAR, 'cambia'), (2.6, 0.32, DARK, 'nuevo'), (4.9, 0.32, GRIS, 'se revisa, no cambia')):
        ax.add_patch(Rectangle((x, y - 0.13), 0.4, 0.26, facecolor='white', edgecolor=c, lw=2))
        ax.text(x + 0.55, y, t, ha='left', va='center', fontsize=8.8, color='#333333')
    fig.savefig(ruta, dpi=200, bbox_inches='tight', facecolor='white'); plt.close(fig)
    REGISTRO['fig_6_2']['datos'] = 'impacto de SC-01'


# ================================================================ generación
def generar(carpeta=None):
    d = carpeta or os.path.join(AQUI, 'figs')
    os.makedirs(d, exist_ok=True)
    REGISTRO.clear()
    r = {
        'fig_4_1': os.path.join(d, 'fig_4_1_tipos_de_requisito.png'),
        'fig_4_2': os.path.join(d, 'fig_4_2_cadena_de_trazabilidad.png'),
        'fig_5_1': os.path.join(d, 'fig_5_1_proceso_actual.png'),
        'fig_5_2': os.path.join(d, 'fig_5_2_proceso_propuesto.png'),
        'fig_5_3': os.path.join(d, 'fig_5_3_contexto.png'),
        'fig_5_4': os.path.join(d, 'fig_5_4_casos_de_uso.png'),
        'fig_6_1': os.path.join(d, 'fig_6_1_cadena_extendida.png'),
        'fig_6_2': os.path.join(d, 'fig_6_2_impacto_del_cambio.png'),
    }
    tipos_requisito(r['fig_4_1'])
    cadena_trazabilidad(r['fig_4_2'])
    proceso(MO.PROCESO_ACTUAL, r['fig_5_1'], 'fig_5_1', anchos=[5.0, 9.0], ejes={'Bibliotecaria': 0.27})
    proceso(MO.PROCESO_PROPUESTO, r['fig_5_2'], 'fig_5_2', anchos=[4.8, 5.0, 9.0], ejes={'Sistema': 0.27})
    contexto(MO.CONTEXTO, r['fig_5_3'], 'fig_5_3')
    casos_de_uso(MO.CASOS_USO, r['fig_5_4'], 'fig_5_4')
    cadena_extendida(r['fig_6_1'])
    impacto_cambio(r['fig_6_2'])
    for s in SIMBOLOS:
        r['sim:' + s] = os.path.join(d, 'simbolo_%s.png' % s)
        simbolo(s, r['sim:' + s])
    json.dump(REGISTRO, open(os.path.join(d, 'simbolos.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    return r


if __name__ == '__main__':
    print(generar())
