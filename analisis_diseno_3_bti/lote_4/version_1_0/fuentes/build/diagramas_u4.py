# -*- coding: utf-8 -*-
"""Figuras del lote 4 (Capítulos 10 a 13), generadas por código con matplotlib; sin recursos de terceros.
Reutiliza sin modificarlo `lote_3/build/diagramas_u3.py`: la misma notación de capas del Capítulo 9 (Tabla 9.1),
sin símbolos nuevos, y el mismo registro que detiene la generación si una figura mezcla notaciones.
  - fig_10_1: estructura de carpetas del proyecto y su capa (esquema didáctico).
  - fig_10_2: recorrido del alta de un ejemplar (OA-01) por las tres capas (notación de capas).
  - fig_12_1: dos pedidos simultáneos del mismo ejemplar y las dos barreras de RI-01 (esquema didáctico).
  - fig_13_1: préstamos activos y vencidos según la fecha de referencia (esquema didáctico)."""
import os, sys, json
AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(ADS, 'lote_3', 'build'))
import diagramas_u3 as G3
plt, FancyBboxPatch, Rectangle, FancyArrowPatch = G3.plt, G3.FancyBboxPatch, G3.Rectangle, G3.FancyArrowPatch
DARK, MED, LIGHT, AMBAR, GRIS, NEGRO = G3.DARK, G3.MED, G3.LIGHT, G3.AMBAR, G3.GRIS, G3.NEGRO
Lienzo, REGISTRO, SIMBOLOS, NOTACIONES = G3.Lienzo, G3.REGISTRO, G3.SIMBOLOS, G3.NOTACIONES
FIGURAS = {'fig_10_2': 'capas', 'fig_10_1': 'esquema', 'fig_12_1': 'esquema', 'fig_13_1': 'esquema'}


def recorrido_capas(ruta):
    L = Lienzo('fig_10_2', 'capas')
    fig, ax = plt.subplots(figsize=(10.8, 5.0))
    ax.set_xlim(0, 16); ax.set_ylim(0, 7.4); ax.axis('off')
    bandas = [('Presentación', 5.6, 'public/lectores.php: formulario de PT-08 y mensaje (MA-01, MA-02, MA-03, MV-01, MV-02, ME-13)'),
              ('Reglas de negocio', 3.0, 'src/reglas.php: alta_ejemplar() comprueba el rol, valida y decide (contrato OA-01)'),
              ('Persistencia', 0.4, 'src/db.php y src/esquema.sql: la tabla ejemplares guarda el dato; el código es único')]
    for nombre, y, det in bandas:
        G3.capa_banda(L, ax, y, 1.6, nombre, det)
    pasos = [(3.3, '1 pedido POST'), (7.3, '2 valida'), (11.3, '3 resultado')]
    G3.capa_operacion(L, ax, 3.3, 5.55, 4.65, '1 pedido con código y edición')
    G3.capa_operacion(L, ax, 8.6, 2.95, 2.05, '2 INSERT parametrizado')
    ax.text(0.45, 5.1, 'la pantalla pide', ha='left', va='center', fontsize=8.2, color=GRIS, style='italic')
    ax.text(0.45, 2.5, 'las reglas guardan', ha='left', va='center', fontsize=8.2, color=GRIS, style='italic')
    ax.text(15.6, 5.1, '3 el mensaje vuelve a la pantalla', ha='right', va='center', fontsize=8.2, color=GRIS, style='italic')
    _ = pasos
    G3._guardar(fig, ruta)


def carpetas(ruta):
    Lienzo('fig_10_1', 'esquema')
    fig, ax = plt.subplots(figsize=(10.6, 3.6))
    ax.set_xlim(0, 16); ax.set_ylim(0, 5.4); ax.axis('off')
    cajas = [(0.3, 'public/', 'pantallas PT-01 a PT-09', 'Presentación'),
             (4.3, 'src/reglas.php', 'operaciones y contratos', 'Reglas de negocio'),
             (8.3, 'src/db.php y esquema.sql', 'conexión, tablas, restricciones', 'Persistencia'),
             (12.3, 'datos/', 'la base y sus respaldos', 'Datos (no se edita a mano)')]
    for x, t, s, capa in cajas:
        ax.add_patch(FancyBboxPatch((x, 1.6), 3.4, 1.8, boxstyle='round,pad=0.03,rounding_size=0.15', facecolor=LIGHT, edgecolor=MED, lw=1.5))
        ax.text(x + 1.7, 2.95, t, ha='center', va='center', fontsize=9.0 if len(t) < 18 else 7.8, weight='bold', color=DARK)
        ax.text(x + 1.7, 2.1, s, ha='center', va='center', fontsize=8.0, color='#333333')
        ax.text(x + 1.7, 3.9, capa, ha='center', va='center', fontsize=8.4, color=AMBAR, weight='bold')
    ax.text(0.3, 0.9, 'Además: pruebas/ (pruebas automáticas), instalar.php, respaldar.php y restaurar.php (herramientas), '
            'LEEME.txt.', ha='left', va='center', fontsize=8.4, color=GRIS, style='italic')
    ax.text(0.3, 0.35, 'La base del estudiante tiene la misma estructura: las operaciones de src/reglas.php se completan en los Capítulos 10 a 13.',
            ha='left', va='center', fontsize=8.4, color=GRIS, style='italic')
    G3._guardar(fig, ruta)


def carrera(ruta):
    Lienzo('fig_12_1', 'esquema')
    fig, ax = plt.subplots(figsize=(10.8, 3.9))
    ax.set_xlim(0, 16); ax.set_ylim(0, 5.8); ax.axis('off')
    for y, quien in ((3.9, 'Pedido A (proceso 1)'), (1.6, 'Pedido B (proceso 2)')):
        ax.text(0.2, y + 0.75, quien, ha='left', va='center', fontsize=9, weight='bold', color=DARK)
        ax.plot([0.2, 15.8], [y, y], color=GRIS, lw=1.2, zorder=1)
    def paso(x, y, w, t, c=MED):
        ax.add_patch(Rectangle((x, y - 0.35), w, 0.7, facecolor=LIGHT, edgecolor=c, lw=1.4, zorder=3))
        ax.text(x + w / 2, y, t, ha='center', va='center', fontsize=8.0, color=DARK, zorder=4)
    paso(1.0, 3.9, 3.0, 'BEGIN IMMEDIATE')
    paso(4.2, 3.9, 3.4, 'comprueba: EJ-0457 libre')
    paso(7.8, 3.9, 2.6, 'INSERT')
    paso(10.6, 3.9, 2.2, 'COMMIT · ME-04')
    paso(1.4, 1.6, 3.0, 'BEGIN IMMEDIATE', AMBAR)
    paso(4.6, 1.6, 7.9, 'espera: A tiene el permiso de escritura', AMBAR)
    paso(12.7, 1.6, 3.0, 've el préstamo · ME-03')
    ax.text(0.2, 0.45, 'Primera barrera: la operación atómica. Segunda barrera: aunque B saltee las reglas, el índice único de la base rechaza un segundo préstamo activo.',
            ha='left', va='center', fontsize=8.3, color=GRIS, style='italic')
    G3._guardar(fig, ruta)


def vencidos(ruta):
    Lienzo('fig_13_1', 'esquema')
    fig, ax = plt.subplots(figsize=(10.8, 3.4))
    ax.set_xlim(0, 16); ax.set_ylim(0, 5.0); ax.axis('off')
    dias = list(range(5, 22))
    x = lambda d: 0.8 + (d - 5) * 0.9
    ax.plot([x(5), x(21)], [0.9, 0.9], color=GRIS, lw=1.5)
    for d in dias:
        ax.plot([x(d), x(d)], [0.82, 0.98], color=GRIS, lw=1)
        if d % 2 == 1:
            ax.text(x(d), 0.5, '%02d/03' % d, ha='center', va='center', fontsize=7.4, color=GRIS)
    prestamos = [('EJ-0458', 5, 12, 3.6), ('EJ-0512', 10, 17, 2.6), ('EJ-0601', 14, 21, 1.6)]
    ref = 15
    for ej, s, v, y in prestamos:
        venc = v < ref
        c = AMBAR if venc else MED
        ax.add_patch(Rectangle((x(s), y - 0.3), x(v) - x(s), 0.6, facecolor=LIGHT, edgecolor=c, lw=1.5))
        ax.text((x(s) + x(v)) / 2, y, '%s · vence %02d/03 · %s' % (ej, v, 'vencido' if venc else 'en plazo'), ha='center', va='center',
                fontsize=8.0, color=DARK, zorder=4, bbox=dict(facecolor=LIGHT, edgecolor='none', pad=1.5))
    ax.plot([x(ref), x(ref)], [1.0, 4.4], color=NEGRO, lw=1.6, ls='--', zorder=2)
    ax.text(x(ref) + 0.15, 4.5, 'fecha de referencia: 15/03', ha='left', va='center', fontsize=8.6, color=NEGRO, weight='bold')
    ax.text(0.2, 4.5, 'Vencido = vence antes de la fecha de referencia.', ha='left', va='center', fontsize=8.6, color=GRIS, style='italic')
    G3._guardar(fig, ruta)


def generar(carpeta=None):
    d = carpeta or os.path.join(AQUI, 'figs')
    os.makedirs(d, exist_ok=True)
    REGISTRO.clear()
    r = {'fig_10_2': os.path.join(d, 'fig_10_2_recorrido_por_capas.png'), 'fig_10_1': os.path.join(d, 'fig_10_1_estructura_de_carpetas.png'),
         'fig_12_1': os.path.join(d, 'fig_12_1_dos_pedidos_simultaneos.png'), 'fig_13_1': os.path.join(d, 'fig_13_1_vencidos_y_fecha_de_referencia.png')}
    recorrido_capas(r['fig_10_2']); carpetas(r['fig_10_1']); carrera(r['fig_12_1']); vencidos(r['fig_13_1'])
    for s in SIMBOLOS:   # los de la notación de capas, para la leyenda de la guía (función de diagramas_u3)
        if SIMBOLOS[s][0] == 'capas':
            r['sim:' + s] = os.path.join(d, 'simbolo_%s.png' % s)
            G3.simbolo(s, r['sim:' + s])
    json.dump(REGISTRO, open(os.path.join(d, 'simbolos.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    return r


if __name__ == '__main__':
    print(generar('/tmp/claude-0/-home-user/26ffb67a-8ead-5080-85a6-8abfc1cb2d1d/scratchpad/l4figs'))
