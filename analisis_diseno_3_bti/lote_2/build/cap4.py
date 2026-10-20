# -*- coding: utf-8 -*-
"""Capítulo 4 — «Requisitos que se pueden comprobar» (Work §6: secciones 4.1 a 4.4 y práctica; encuentros 7 y 8).

Integración del piloto, SIN reescribir el contenido: este módulo carga el Capítulo 4 v2.1
(`fase2_pilotos/A2_capitulo4_v2_1/build/contenido.py`, idéntico a la v2) y conserva todos sus textos, salvo los cambios
declarados en CAMBIOS, que build/verificar.py comprueba uno por uno (todo lo demás tiene que quedar idéntico):
  - especificación de evidencia C3 aprobada (consigna común RNF-04, Nivel 2 desde RNF-05 y solo B-08, Actividad 1 (d)
    del Encuentro 8 a tarea);
  - conexión con la fuente única del caso: el extracto del dossier, las reglas, el catálogo, los postergados y el buzón
    se leen de `lote_1/caso/dossier.py` y `lote_2/caso/requisitos.py`;
  - integración en el tomo: rótulo de capacidades con el formato del lote 1 (C3 y C9, según Work §5.2 para el
    Encuentro 8), un indicador de C9, título de 4.2 textual de Work §6, recuadro del calendario sin nombres internos
    y remisión al extracto del dossier."""
import os, sys, importlib.util
AQUI = os.path.dirname(os.path.abspath(__file__))
L2 = os.path.dirname(AQUI)
ADS = os.path.dirname(L2)
sys.path.insert(0, os.path.join(L2, 'caso'))
import requisitos as R
D = R.D
MB = None

RUTA_PILOTO = os.path.join(ADS, 'fase2_pilotos', 'A2_capitulo4_v2_1', 'build', 'contenido.py')
_spec = importlib.util.spec_from_file_location('cap4_piloto', RUTA_PILOTO)
PILOTO = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(PILOTO)
for _n in dir(PILOTO):
    if _n.isupper():
        globals()[_n] = getattr(PILOTO, _n)

NUM = 4
SECCIONES = ['4.1 Necesidad, requisito, regla de negocio y solución técnica',
             '4.2 Requisitos funcionales, calidad y restricciones',
             '4.3 Identificación, fuente, prioridad y criterios de aceptación',
             '4.4 Ambigüedades frecuentes y cómo corregirlas']
PRACTICA_WORK = 'convertir pedidos de usuarios en requisitos verificables'

# ------------------------------------------------------------------ cambios declarados respecto del piloto
CAMBIOS = []


def cambio(nombre, valor, motivo):
    CAMBIOS.append((nombre, motivo))
    globals()[nombre] = valor


cambio('ROTULO_CAPACIDAD', 'Capacidades propuestas para el programa institucional (C3 y C9; no son capacidades oficiales del MEC)',
       'Formato del lote 1; Work §5.2 asigna C3 y C9 al Encuentro 8 (revisión entre pares).')
cambio('CAPACIDAD', 'C3. Especifica y prioriza requisitos verificables.\nC9. Verifica y mejora la solución a partir de evidencia.',
       'Formato del lote 1 con el código de cada capacidad; texto de Work §4.2.')
cambio('INDICADORES', PILOTO.INDICADORES + ['Revisa los requisitos de otro equipo con una lista de verificación y propone correcciones concretas.'],
       'Indicador de C9 para la revisión entre pares, que ya tenía el capítulo (Encuentro 8, Actividad 3).')
cambio('ARTICULACION', ['Con el Capítulo 2: los fragmentos del dossier de relevamiento que se usan acá están reproducidos '
                        'al comienzo del capítulo. Cada requisito cita el fragmento exacto que lo respalda.'] + PILOTO.ARTICULACION[1:],
       'El extracto ya no va en «la página siguiente»: va al comienzo del capítulo, dentro del tomo.')
cambio('S42', ('4.2 Requisitos funcionales, calidad y restricciones', PILOTO.S42[1]),
       'Título textual de Work §6 (el piloto decía «de calidad»); los párrafos no cambian.')

# extracto del dossier: los mismos registros y códigos del piloto, con el texto de la fuente única
cambio('DOSSIER', [(reg, D.REGISTRO[reg]['titulo'], [(c, D.TEXTO[c]) for c, _ in frs]) for reg, _, frs in PILOTO.DOSSIER],
       'Fuente única: las líneas se leen de lote_1/caso/dossier.py (texto completo de cada línea); se elimina la copia.')
cambio('REGLAS', list(D.REGLAS), 'Fuente única: reglas RN-01 a RN-06 de lote_1/caso/dossier.py (texto idéntico).')
cambio('CATALOGO', list(R.CATALOGO), 'Fuente única: lote_2/caso/requisitos.py (texto idéntico).')
cambio('POSTERGADOS', list(R.POSTERGADOS), 'Fuente única: lote_2/caso/requisitos.py (texto idéntico).')
cambio('BUZON', list(R.BUZON), 'Fuente única: lote_2/caso/requisitos.py (texto idéntico).')
cambio('FUENTES', dict(R.TEXTO, **dict(D.REGLAS)), 'Fuentes citables: dossier, reglas y buzón de la fuente única.')

# especificación de evidencia C3 (§2): Actividad 1 (d) del Encuentro 8 a tarea
_e8 = [list(g) for g in PILOTO.ACT_E8]
_e8[0] = ('Ejercitá', [PILOTO.ACT_E8[0][1][0].replace('(d) «El sistema nunca debe prestar mal un libro.»',
                                                         '(d) Para resolver en casa: «El sistema nunca debe prestar mal un libro.»')])
cambio('ACT_E8', [tuple(g) for g in _e8], 'Especificación C3, §2: la Actividad 1 (d) pasa a tarea para compensar la consigna común.')

CONSIGNA_COMUN_TITULO = 'Consigna común — para todos, antes de empezar tu nivel'
CONSIGNA_COMUN = [
    'El pedido B-03 dice: «El sistema tiene que avisar rápido si el libro está.»\n'
    '(a) Redactalo como requisito de calidad RNF-04, con una cifra comprobable marcada «a confirmar».\n'
    '(b) Escribí su criterio de aceptación «Dado… cuando… entonces…», de modo que otra persona pueda comprobarlo.\n'
    '(c) Anotá la fuente (B-03) y una prioridad con su razón.',
]
_n2 = PILOTO.NIVELES[1][1]
cambio('NIVELES', [
    PILOTO.NIVELES[0],
    ('Nivel 2 — Intermedio', [
        _n2[0].replace('a partir de RF-11, RNF-04 y RS-03', 'a partir de RF-11, RNF-05 y RS-03'),
        'Corregí la ambigüedad de B-08. Escribí la pregunta que le harías a quien la pidió y una versión comprobable '
        'marcada «a confirmar».',
    ]),
    PILOTO.NIVELES[2],
], 'Especificación C3, §2: el Nivel 2 numera desde RNF-05 y corrige solo B-08 (B-03 lo resuelve la consigna común).')
cambio('PRACTICA_INTRO', [PILOTO.PRACTICA_INTRO[0] + ' Antes de tu nivel, todos resuelven la consigna común.'],
       'Remisión a la consigna común de la especificación C3.')
cambio('CALENDARIO', ('Si el calendario se acorta', [
    'En la adaptación de 28 encuentros, este capítulo conserva sus dos encuentros: los requisitos son una evidencia '
    'esencial del proyecto.'] + PILOTO.CALENDARIO[1][1:]),
       'Sin el nombre interno «Piloto C».')

EVAL_PUNTAJE = ('Puntaje total: 15 puntos (ítems 1 a 7: 1 punto cada uno; ítem 8: 3 puntos; ítem 9: 5 puntos). '
                'Es opcional: puede reemplazarse por la evidencia de la Práctica 4.')
EVAL_FUENTES = {'R-07': EVAL_TEXTO_BASE[1][0]}
