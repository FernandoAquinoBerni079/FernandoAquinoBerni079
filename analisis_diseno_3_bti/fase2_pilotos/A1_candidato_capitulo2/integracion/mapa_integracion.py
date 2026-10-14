# -*- coding: utf-8 -*-
"""Plan de integración del candidato de elicitación (v1.1) al Capítulo 2 de Work, «Investigar antes de
diseñar» (encuentros 3 y 4, capacidad C2). NO genera el capítulo: solo declara el destino de cada elemento
del candidato, la renumeración y las condiciones, y comprueba que el plan sea completo y coherente con el
Capítulo 4 v2. Uso: python3 mapa_integracion.py  →  mapa_integracion.md (o código 1 si algo falla)."""
import os, sys, importlib.util

AQUI = os.path.dirname(os.path.abspath(__file__))
def cargar(nombre, ruta):
    sys.path.insert(0, os.path.dirname(ruta))
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    sys.path.pop(0)
    return m
CAND = cargar('cand', os.path.join(AQUI, '..', 'build', 'contenido.py'))
CAP4 = cargar('cap4', os.path.join(AQUI, '..', '..', 'A2_capitulo4_v2', 'build', 'contenido.py'))

# Datos del Capítulo 2 según el informe de Work (§4.2, §5.2 y §6). Capacidad e indicadores son propuestas de Work.
DESTINO = {
    'unidad': 'Unidad I — Comprender el problema y su contexto',
    'capitulo': 'Capítulo 2. Investigar antes de diseñar',
    'encuentros': (3, 4),
    'capacidad': 'C2. Obtiene y contrasta información sobre necesidades de usuarios.',
    'rotulo': 'Capacidad propuesta para el programa institucional (C2; no es una capacidad oficial del MEC)',
    'indicadores_work': 'Formula preguntas abiertas; registra evidencia; separa hechos, opiniones y supuestos; '
                        'contrasta dos fuentes o dos roles simulados. Evidencia: dossier de relevamiento.',
    'secciones': {
        '2.1': 'Entrevistar para comprender tareas y problemas.',
        '2.2': 'Observar un proceso y analizar documentos.',
        '2.3': 'Contrastar fuentes, contradicciones y necesidades no expresadas.',
        '2.4': 'Registrar evidencia con respeto por las personas y sus datos.',
    },
    'practica_work': 'Dossier de relevamiento con roles de bibliotecario, lector y dirección.',
    'encuentro_3': 'Preparar entrevista, observación y revisión de registros (evidencia: guion y criterios para resguardar información).',
    'encuentro_4': 'Realizar relevamiento real autorizado o simulación con roles (evidencia: notas, fuentes y registro de contradicciones).',
}

# Destino de cada elemento del candidato: (elemento, destino, acción, motivo)
MAPA = [
    ('S41', '2.1', 'Adaptar', 'La distinción necesidad/solución abre la entrevista; se quita la columna «Requisito candidato» de la Tabla 4.1, que pasa al Capítulo 4.'),
    ('TABLA_NRS', '2.1', 'Adaptar', 'Igual que S41: sin columna de requisitos.'),
    ('CONCEPTO_ELICITAR', '2.1', 'Adaptar', 'Definición; el producto pasa a ser el dossier con necesidades y fuentes, no requisitos.'),
    ('S42', 'Capítulo 1 (1.3)', 'Trasladar', 'Work ubica «actores e interesados» en 1.3. En el Capítulo 2 queda solo un recordatorio de una línea.'),
    ('EJ1', 'Capítulo 1 (1.3)', 'Trasladar', 'Mapa de interesados, con la Figura 4.1.'),
    ('TABLA_EJ1', 'Capítulo 1 (1.3)', 'Trasladar', 'Acompaña al EJ1.'),
    ('S43', '2.1 y 2.2', 'Dividir', 'Entrevista en 2.1; observación y análisis de documentos en 2.2.'),
    ('TABLA_TECNICAS', '2.2', 'Conservar', 'Panorama de técnicas.'),
    ('EN_PARAGUAY', '2.1', 'Conservar', 'Entrevistar en el idioma del interesado (Constitución Nacional, art. 140).'),
    ('S44', '2.1', 'Conservar', 'Preparar y conducir la entrevista: coincide con el encuentro 3 de Work.'),
    ('TABLA_PREGUNTAS', '2.1', 'Conservar', 'Preguntas a evitar.'),
    ('EJ2', '2.1', 'Conservar', 'Guion de la entrevista a la bibliotecaria.'),
    ('S45', '2.4', 'Adaptar', 'Registro numerado por línea. Las categorías se alinean con el indicador de Work: hechos, opiniones y supuestos, más problemas y propuestas.'),
    ('TRANSCRIPCION_E1', '2.4', 'Conservar', 'Registro E1. Las líneas que cita el Capítulo 4 deben seguir existiendo.'),
    ('EJ3', '2.4', 'Adaptar', 'Hallazgos con las categorías de Work.'),
    ('TABLA_HALLAZGOS', '2.4', 'Adaptar', 'Se agrega una columna «hecho, opinión o supuesto». H9 queda como ejemplo de dato contaminado por una pregunta inductora.'),
    ('S46', 'Capítulo 4', 'Retirar', 'Redactar requisitos es tema de 4.1 a 4.3 (ya cubierto por el Capítulo 4 v2).'),
    ('CONCEPTO_RC', 'Capítulo 4', 'Retirar', 'Igual que S46.'),
    ('EJ4', 'Capítulo 4', 'Retirar', 'Igual que S46. En su lugar, el Capítulo 2 cierra con una lista de necesidades N-01, N-02… con su fuente, que el Capítulo 4 usa (N-02 aparece en la Figura 4.2).'),
    ('TABLA_RC', 'Capítulo 4', 'Retirar', 'Igual que S46.'),
    ('S47', '2.3', 'Adaptar', 'Se conservan los conflictos y contradicciones entre fuentes. La reescritura de ambigüedades pasa a 4.4.'),
    ('EJ5', '2.3', 'Adaptar', 'Situación hipotética de conflicto; se reemplaza por una contradicción real entre dos registros del dossier (por ejemplo, E2-L8 frente a las reglas de circulación).'),
    ('S48', '2.4', 'Adaptar', 'Confirmar con el interesado; se agregan consentimiento, autorización y anonimización (Work §7.1).'),
    ('TRANSCRIPCION_E2', '2.3', 'Conservar', 'Registro de la docente; aporta la contradicción de 2.3.'),
    ('OBSERVACION_O1', '2.2', 'Conservar', 'Observación con líneas O1-1 a O1-4.'),
    ('ACT_E7', 'Actividades 2.1 y 2.2', 'Adaptar', 'Se quita la actividad del mapa de interesados (pasa a 1.3).'),
    ('ACT_E8', 'Actividades 2.3 y 2.4', 'Adaptar', 'Se quitan las consignas de redacción de requisitos (Capítulo 4).'),
    ('NIVELES', 'Práctica 2', 'Adaptar', 'Work pide un dossier con roles de bibliotecario, lector y dirección. Se reorganizan los tres niveles sobre esos roles; el Nivel 3 contrasta dos roles.'),
    ('EVAL_ITEMS', 'Evaluación del Capítulo 2', 'Adaptar', 'Se conservan los ítems de técnicas, preguntas y fuentes. Se reemplaza el ítem de reescritura de requisitos por uno de separar hechos, opiniones y supuestos.'),
    ('CALENDARIO_REDUCIDO', 'Capítulo 2', 'Adaptar', 'En el plan de 28 encuentros, los encuentros 3 y 4 se conservan sin fusión.'),
    ('REPASO', 'Capítulo 2', 'Adaptar', 'Ajustar al nuevo alcance.'),
]

# Renumeración de identificadores visibles
RENUMERACION = [
    ('Unidad 2 — Ingeniería de requisitos', DESTINO['unidad']),
    ('Capítulo 4', 'Capítulo 2'),
    ('Encuentros 7 y 8', 'Encuentros 3 y 4'),
    ('Secciones 4.1 a 4.8', 'Secciones 2.1 a 2.4 (según el MAPA)'),
    ('Ejemplos resueltos 4.2, 4.3 y 4.5', 'Ejemplos resueltos 2.1 a 2.3 (el 4.1 pasa al Capítulo 1 y el 4.4 se retira)'),
    ('Figura 4.2 (proceso de elicitación)', 'Figura 2.1 (la Figura 4.1 pasa al Capítulo 1)'),
    ('Tablas 4.1 a 4.6', 'Tablas 2.x, en el orden de aparición'),
    ('Práctica 4', 'Práctica 2'),
    ('Evaluación del Capítulo 4 (semilla ADS3-C4-1)', 'Evaluación del Capítulo 2 (semilla nueva, con claves repartidas)'),
    ('Capacidad institucional propia del candidato', DESTINO['capacidad']),
]

errores = []
def control(c, m):
    if not c:
        errores.append(m)

elementos = [k for k in dir(CAND) if k.isupper() and k.startswith(('S4', 'EJ', 'TABLA', 'TRANSCRIPCION', 'OBSERVACION', 'CONCEPTO', 'EN_PARAGUAY', 'ACT_', 'NIVELES', 'EVAL_ITEMS', 'CALENDARIO', 'REPASO'))]
mapeados = [m[0] for m in MAPA]
control(sorted(elementos) == sorted(mapeados), 'Elementos del candidato sin destino o inexistentes: %s' % sorted(set(elementos) ^ set(mapeados)))
control(len(mapeados) == len(set(mapeados)), 'Elementos mapeados dos veces')
destinos = {m[1].split()[0] for m in MAPA}
control(all(any(m[1].startswith(s) or (' ' + s) in m[1] for m in MAPA) for s in DESTINO['secciones']), 'Alguna sección 2.1 a 2.4 queda sin contenido')
control(all(m[2] in ('Conservar', 'Adaptar', 'Dividir', 'Trasladar', 'Retirar') for m in MAPA), 'Acción desconocida')

# Coherencia con el Capítulo 4 v2: sus fragmentos de E1 y E3 deben existir textualmente en el candidato.
cand_e1 = {l.split()[0]: l.split(':', 1)[1].strip() for l in CAND.TRANSCRIPCION_E1[1]}
cand_e3 = {l.split()[0]: l.split(':', 1)[1].strip() for l in CAND.EVAL_TEXTO_BASE[1]}
faltan = []
for cod, txt in CAP4.FUENTES.items():
    if cod.startswith('E1-'):
        if txt not in cand_e1.get(cod.split('-')[1], ''):
            faltan.append(cod)
    if cod.startswith('E3-'):
        if txt not in cand_e3.get(cod.split('-')[1], ''):
            faltan.append(cod)
control(not faltan, 'Fragmentos del Capítulo 4 que no están en el candidato: %s' % faltan)
nuevos = sorted({c.split('-')[0] for c in CAP4.FUENTES if c.startswith(('E4-', 'E5-'))})

if errores:
    print('CONTROLES FALLIDOS:'); [print(' -', e) for e in errores]; sys.exit(1)

L = ['<!-- Archivo generado por mapa_integracion.py. No editar a mano. -->', '',
     '### Destino de cada elemento del candidato (%d elementos)' % len(MAPA), '',
     '| Elemento (contenido.py) | Destino | Acción | Motivo |', '|---|---|---|---|']
L += ['| `%s` | %s | %s | %s |' % m for m in MAPA]
L += ['', '### Renumeración', '', '| En el candidato | En el Capítulo 2 |', '|---|---|']
L += ['| %s | %s |' % r for r in RENUMERACION]
acc = {}
for m in MAPA:
    acc[m[2]] = acc.get(m[2], 0) + 1
L += ['', '### Resumen', '', ', '.join('%s: %d' % (k, v) for k, v in sorted(acc.items())) + '.',
      '', 'Fragmentos de E1 y E3 citados por el Capítulo 4 v2: todos presentes, textualmente, en el candidato.',
      'Registros que cita el Capítulo 4 v2 y que el candidato todavía no tiene: %s. El dossier del Capítulo 2 '
      'debe incorporarlos con las mismas líneas.' % ', '.join(nuevos)]
open(os.path.join(AQUI, 'mapa_integracion.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('Controles correctos: %d elementos con destino; secciones 2.1 a 2.4 cubiertas; fragmentos E1 y E3 del Capítulo 4 presentes en el candidato.' % len(MAPA))
print('Resumen:', acc, '· registros a incorporar:', nuevos)
