# -*- coding: utf-8 -*-
"""Distribución del tiempo de los 36 encuentros de Work y de la adaptación a 28 encuentros.
Uso: python3 distribucion.py  →  verifica las sumas y escribe distribucion_36.csv, distribucion_28.csv
y tablas_generadas.md. Si algún control falla, termina con código 1 y no escribe nada.

Categorías (HC dentro de cada encuentro de 5 HC):
  A   Análisis: relevamiento, requisitos, procesos y casos de uso, priorización y cambios.
  D   Diseño: modelo de datos, interacción, arquitectura; y, en la Unidad IV, la revisión del diseño
      y del requisito de cada operación antes de programarla.
  P   Programación: preparar el entorno de ejecución, implementar y corregir código.
  V   Verificación y validación: pruebas, revisión entre pares, sesiones de uso, aceptación.
  Doc Documentación de entrega: guía de instalación y uso, respaldo, paquete.
  G   Gestión del proyecto: equipo, tareas, incrementos, versiones, retrospectiva.
  E   Evaluación: diagnóstico, revisiones de unidad (hitos H1 a H6), defensa y recuperación.
Criterio general: estructura de taller de Work (§5.1), con 1 HC de problema y explicación, 3 HC de práctica y
1 HC de revisión, redistribuida según el foco de cada encuentro que Work declara en §5.2. La asignación es
editorial y se puede discutir fila por fila; el foco, las capacidades y los hitos se copian de Work sin cambios."""
import csv, os, sys

CAT = ['A', 'D', 'P', 'V', 'Doc', 'G', 'E']
NOMBRE = {'A': 'Análisis', 'D': 'Diseño', 'P': 'Programación', 'V': 'Verificación y validación',
          'Doc': 'Documentación de entrega', 'G': 'Gestión del proyecto', 'E': 'Evaluación'}
UNIDADES = {'I': (range(1, 7), 30), 'II': (range(7, 13), 30), 'III': (range(13, 19), 30),
            'IV': (range(19, 27), 40), 'V': (range(27, 33), 30), 'VI': (range(33, 37), 20)}

# n, foco (Work §5.2), capacidades (Work), hito, {categoría: HC}, criterio de la asignación
S36 = [
    (1, 'Presentación del reto y diagnóstico de programación, formularios, datos y comunicación.', 'C1, C7', '', {'A': 3, 'E': 2}, 'Diagnóstico de entrada como evaluación; presentación del problema como análisis.'),
    (2, 'Sistema de biblioteca, actores, límites y situación problemática.', 'C1', '', {'A': 5}, 'Todo el encuentro delimita el problema.'),
    (3, 'Preparar entrevista, observación y revisión de registros.', 'C2', '', {'A': 5}, 'Preparación del relevamiento.'),
    (4, 'Realizar relevamiento real autorizado o simulación con roles.', 'C2', '', {'A': 5}, 'Relevamiento.'),
    (5, 'Comparar alternativas: registro manual mejorado, herramienta existente y prototipo.', 'C1, C2', '', {'A': 5}, 'Factibilidad: análisis, no diseño de la solución.'),
    (6, 'Delimitar alcance, exclusiones y equipo; revisión de unidad I.', 'C1, C2, C7', 'H1', {'A': 2, 'G': 1, 'E': 2}, 'Alcance (A), equipo (G), revisión H1 (E).'),
    (7, 'Formular requisitos funcionales y reglas de préstamo.', 'C3', '', {'A': 5}, 'Capítulo 4, encuentro 1.'),
    (8, 'Definir calidad, restricciones y criterios de aceptación.', 'C3, C9', '', {'A': 4, 'V': 1}, 'Capítulo 4, encuentro 2: 1 HC de revisión entre pares (V).'),
    (9, 'Representar proceso actual y proceso propuesto.', 'C4', '', {'A': 3, 'D': 2}, 'El proceso propuesto ya es una decisión de diseño.'),
    (10, 'Desarrollar casos de uso y excepciones.', 'C3, C4', '', {'A': 5}, 'Modelado de requisitos.'),
    (11, 'Priorizar, planificar incrementos y establecer trazabilidad.', 'C3, C7', '', {'A': 2, 'G': 3}, 'Priorización y trazabilidad (A); incrementos, tareas y responsables (G).'),
    (12, 'Resolver una solicitud de cambio; revisión de unidad II.', 'C3, C4, C7', 'H2', {'A': 3, 'E': 2}, 'Cambio de requisitos (A), revisión H2 (E).'),
    (13, 'Revisar antecedentes de Algorítmica y modelar el dominio.', 'C5', '', {'D': 5}, 'Modelo de datos.'),
    (14, 'Validar integridad, historial y diccionario de datos.', 'C5', '', {'D': 4, 'V': 1}, 'Revisión del modelo con ejemplos y contraejemplos (V).'),
    (15, 'Diseñar recorridos y bocetos de pantallas.', 'C6', '', {'D': 5}, 'Diseño de interacción.'),
    (16, 'Revisar accesibilidad, mensajes y estados con usuarios simulados.', 'C6, C9', '', {'D': 3, 'V': 2}, 'Sesión con usuarios simulados (V).'),
    (17, 'Diseñar responsabilidades, conexiones y entorno de ejecución.', 'C5, C6', '', {'D': 5}, 'Arquitectura.'),
    (18, 'Evaluación intermedia: defender análisis y diseño; corregir.', 'C1-C7', 'H3', {'E': 4, 'D': 1}, 'Defensa (E) y corrección del dossier (D).'),
    (19, 'Preparar entorno, estructura de trabajo, versiones y datos ficticios.', 'C7, C8', '', {'P': 3, 'G': 2}, 'Entorno y estructura (P); versiones y bitácora (G).'),
    (20, 'Construir una operación mínima de extremo a extremo.', 'C6, C8, C9', '', {'P': 3, 'D': 1, 'V': 1}, '1 HC repasa requisito y diseño de la operación (D); 1 HC prueba de persistencia (V).'),
    (21, 'Implementar catálogo y control de ejemplares.', 'C5, C8', '', {'P': 3, 'D': 1, 'V': 1}, 'Igual criterio que el 20.'),
    (22, 'Implementar lectores y permisos mínimos.', 'C6, C8', '', {'P': 3, 'D': 1, 'V': 1}, 'Igual criterio; la prueba incluye el rechazo de acceso indebido.'),
    (23, 'Implementar préstamo y prevención de duplicados.', 'C5, C8, C9', '', {'P': 3, 'D': 1, 'V': 1}, 'Igual criterio; la prueba incluye el reenvío.'),
    (24, 'Implementar devolución e historial.', 'C5, C8, C9', '', {'P': 3, 'D': 1, 'V': 1}, 'Igual criterio.'),
    (25, 'Construir consultas de disponibilidad y vencimientos.', 'C3, C8', '', {'P': 3, 'D': 1, 'V': 1}, 'Igual criterio; fecha de referencia definida.'),
    (26, 'Integrar y demostrar el incremento; revisar unidad IV.', 'C7-C9', 'H4', {'P': 2, 'V': 1, 'E': 2}, 'Integración (P), demostración (V), revisión H4 (E).'),
    (27, 'Diseñar cobertura y datos independientes de prueba.', 'C9', '', {'V': 5}, 'Pruebas.'),
    (28, 'Ejecutar pruebas funcionales, límites y entradas inválidas.', 'C8, C9', '', {'V': 5}, 'Pruebas.'),
    (29, 'Probar integración, permisos, persistencia y restauración.', 'C8-C10', '', {'V': 5}, 'Pruebas.'),
    (30, 'Realizar sesiones de uso y prueba de aceptación.', 'C3, C6, C9', '', {'V': 4, 'A': 1}, 'Aceptación (V); repriorizar con lo observado (A).'),
    (31, 'Corregir problemas y repetir pruebas afectadas.', 'C7-C9', '', {'P': 2, 'V': 3}, 'Corrección (P) y regresión (V).'),
    (32, 'Recuperación técnica y revisión de unidad V.', 'C8, C9', 'H5', {'P': 2, 'V': 1, 'E': 2}, 'Recuperación técnica (P, V), revisión H5 (E).'),
    (33, 'Redactar guía de uso, instalación, respaldo y límites.', 'C10', '', {'Doc': 5}, 'Documentación.'),
    (34, 'Entregar a otro equipo para instalación y revisión.', 'C7, C10', 'H6', {'Doc': 2, 'V': 2, 'E': 1}, 'Ajustes de la guía (Doc), instalación por otro equipo (V), hito H6 (E).'),
    (35, 'Demostración y defensa individual del proyecto.', 'C1-C10', '', {'E': 5}, 'Defensa.'),
    (36, 'Recuperación individual, retrospectiva y cierre.', 'C7, C9, C10', '', {'E': 3, 'G': 2}, 'Recuperación (E), retrospectiva (G).'),
]

# Adaptación a 28: n, encuentros de Work que reúne, foco, {categoría: HC}, ajuste de alcance declarado
S28 = [
    (1, [1], 'Reto y diagnóstico de entrada.', {'A': 3, 'E': 2}, 'Sin cambios.'),
    (2, [2], 'Sistema, actores y límites.', {'A': 5}, 'Sin cambios.'),
    (3, [3], 'Preparar el relevamiento.', {'A': 5}, 'Sin cambios.'),
    (4, [4], 'Relevamiento.', {'A': 5}, 'Sin cambios.'),
    (5, [5, 6], 'Alternativas, alcance y equipo; H1.', {'A': 3, 'G': 1, 'E': 1}, 'Factibilidad con dos alternativas en lugar de tres; H1 como defensa breve por equipo.'),
    (6, [7], 'Requisitos funcionales y reglas (Capítulo 4).', {'A': 5}, 'Sin cambios.'),
    (7, [8], 'Calidad, restricciones y aceptación (Capítulo 4).', {'A': 4, 'V': 1}, 'Sin cambios.'),
    (8, [9, 10], 'Proceso propuesto y casos de uso.', {'A': 4, 'D': 1}, 'El proceso actual se toma del dossier sin diagramarlo; se mantienen los tres casos de uso con un flujo alternativo cada uno.'),
    (9, [11, 12], 'Prioridad, trazabilidad y cambio; H2.', {'A': 2, 'G': 1, 'E': 2}, 'Plan de incrementos como lista breve; la solicitud de cambio se resuelve dentro de la revisión.'),
    (10, [13], 'Modelo del dominio.', {'D': 5}, 'Sin cambios.'),
    (11, [14], 'Integridad, historial y diccionario.', {'D': 4, 'V': 1}, 'Sin cambios.'),
    (12, [15, 16], 'Recorridos, bocetos y revisión con usuarios.', {'D': 4, 'V': 1}, 'Tres recorridos en baja fidelidad; una sola sesión de revisión entre equipos.'),
    (13, [17], 'Arquitectura y entorno.', {'D': 5}, 'Sin cambios.'),
    (14, [18], 'Evaluación intermedia; H3.', {'E': 4, 'D': 1}, 'Sin cambios.'),
    (15, [19, 20], 'Base de proyecto y primera operación.', {'P': 3, 'D': 1, 'V': 1}, 'El docente entrega el entorno, la conexión y el inicio de sesión listos (base explicada, Work §7.5); el equipo hace la primera operación.'),
    (16, [21, 22], 'Catálogo, ejemplares, lectores y permisos.', {'P': 3, 'D': 1, 'V': 1}, 'Lectores por carga inicial; los permisos mínimos vienen en la base y el equipo los prueba.'),
    (17, [23], 'Préstamo y prevención de duplicados.', {'P': 3, 'D': 1, 'V': 1}, 'Sin cambios.'),
    (18, [24], 'Devolución e historial.', {'P': 3, 'D': 1, 'V': 1}, 'Sin cambios.'),
    (19, [25, 26], 'Consultas mínimas, integración; H4.', {'P': 2, 'V': 1, 'E': 2}, 'Solo disponibles, activos y vencidos con fecha de referencia.'),
    (20, [27], 'Cobertura y datos de prueba.', {'V': 5}, 'Sin cambios.'),
    (21, [28], 'Pruebas funcionales y de límite.', {'V': 5}, 'Sin cambios.'),
    (22, [29], 'Integración, permisos, persistencia y restauración.', {'V': 5}, 'Sin cambios.'),
    (23, [30], 'Uso y aceptación.', {'V': 4, 'A': 1}, 'Sin cambios.'),
    (24, [31, 32], 'Corrección, regresión; H5.', {'P': 2, 'V': 1, 'E': 2}, 'Sin encuentro de reserva para recuperación técnica.'),
    (25, [33], 'Guía de uso, instalación y respaldo.', {'Doc': 5}, 'Sin cambios.'),
    (26, [34], 'Entrega a otro equipo; H6.', {'Doc': 2, 'V': 2, 'E': 1}, 'Sin cambios.'),
    (27, [35], 'Demostración y defensa individual.', {'E': 5}, 'Sin cambios.'),
    (28, [36], 'Recuperación individual y cierre.', {'E': 3, 'G': 2}, 'Sin cambios.'),
]

errores = []
def control(cond, msg):
    if not cond:
        errores.append(msg)

# Controles 36
control([r[0] for r in S36] == list(range(1, 37)), '36: numeración 1 a 36')
for n, _, _, _, hc, _ in S36:
    control(sum(hc.values()) == 5, '36: el encuentro %d suma %d HC' % (n, sum(hc.values())))
    control(set(hc) <= set(CAT), '36: categoría desconocida en %d' % n)
for u, (rng, esperado) in UNIDADES.items():
    s = sum(sum(r[4].values()) for r in S36 if r[0] in rng)
    control(s == esperado, '36: la unidad %s suma %d HC y Work indica %d' % (u, s, esperado))
hitos36 = {r[3]: r[0] for r in S36 if r[3]}
control(hitos36 == {'H1': 6, 'H2': 12, 'H3': 18, 'H4': 26, 'H5': 32, 'H6': 34}, '36: hitos en los encuentros de Work')

# Controles 28
control([r[0] for r in S28] == list(range(1, 29)), '28: numeración 1 a 28')
cubiertos = sorted(o for r in S28 for o in r[1])
control(cubiertos == list(range(1, 37)), '28: cada encuentro de Work aparece exactamente una vez')
for n, orig, _, hc, _ in S28:
    control(sum(hc.values()) == 5, '28: el encuentro %d suma %d HC' % (n, sum(hc.values())))

def caps(texto):
    out = set()
    for parte in texto.split(','):
        parte = parte.strip()
        if '-' in parte:
            a, b = parte.split('-')
            out |= {'C%d' % i for i in range(int(a[1:]), int(b[1:]) + 1)}
        elif parte:
            out.add(parte)
    return out

cap36 = {r[0]: caps(r[2]) for r in S36}
cap28 = set().union(*[cap36[o] for r in S28 for o in r[1]])
control(cap28 == {'C%d' % i for i in range(1, 11)}, '28: se conservan C1 a C10')
hitos28 = sorted(hitos36[h] for h in hitos36 if any(hitos36[h] in r[1] for r in S28))
control(len(hitos28) == 6, '28: se conservan los seis hitos')

if errores:
    print('CONTROLES FALLIDOS:'); [print(' -', e) for e in errores]; sys.exit(1)

def totales(filas, idx):
    t = {c: 0 for c in CAT}
    for f in filas:
        for c, v in f[idx].items():
            t[c] += v
    return t

t36, t28 = totales(S36, 4), totales(S28, 3)
assert sum(t36.values()) == 180 and sum(t28.values()) == 140

AQUI = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(AQUI, 'distribucion_36.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['encuentro', 'unidad', 'foco_work', 'capacidades_work', 'hito'] + CAT + ['criterio'])
    for n, foco, cp, h, hc, crit in S36:
        u = [k for k, (rng, _) in UNIDADES.items() if n in rng][0]
        w.writerow([n, u, foco, cp, h] + [hc.get(c, 0) for c in CAT] + [crit])
with open(os.path.join(AQUI, 'distribucion_28.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['encuentro', 'reune_encuentros_work', 'foco'] + CAT + ['ajuste_de_alcance'])
    for n, orig, foco, hc, aj in S28:
        w.writerow([n, '+'.join(map(str, orig)), foco] + [hc.get(c, 0) for c in CAT] + [aj])

def pct(v, tot):
    return ('%.1f' % (100 * v / tot)).replace('.', ',')

L = ['<!-- Archivo generado por distribucion.py. No editar a mano. -->', '']
L += ['### Totales: secuencia de Work (36 encuentros, 180 HC) y adaptación (28 encuentros, 140 HC)', '',
      '| Categoría | HC en 36 | % en 36 | HC en 28 | % en 28 |', '|---|---|---|---|---|']
for c in CAT:
    L.append('| %s | %d | %s %% | %d | %s %% |' % (NOMBRE[c], t36[c], pct(t36[c], 180), t28[c], pct(t28[c], 140)))
L.append('| **Total** | **180** | **100 %** | **140** | **100 %** |')
L += ['', '### Por unidad (36 encuentros)', '', '| Unidad | Encuentros | HC | ' + ' | '.join(CAT) + ' |', '|---' * (3 + len(CAT)) + '|']
for u, (rng, hc) in UNIDADES.items():
    tu = totales([r for r in S36 if r[0] in rng], 4)
    L.append('| %s | %d–%d | %d | %s |' % (u, rng[0], rng[-1], hc, ' | '.join(str(tu[c]) for c in CAT)))
L += ['', '### Encuentro por encuentro (36)', '', '| N.º | Foco (Work) | Cap. | Hito | ' + ' | '.join(CAT) + ' | Criterio |', '|---' * (5 + len(CAT)) + '|']
for n, foco, cp, h, hc, crit in S36:
    L.append('| %02d | %s | %s | %s | %s | %s |' % (n, foco, cp, h or '—', ' | '.join(str(hc.get(c, 0)) or '0' for c in CAT), crit))
L += ['', '### Adaptación a 28 encuentros', '', '| N.º | Reúne (Work) | Foco | ' + ' | '.join(CAT) + ' | Ajuste de alcance |', '|---' * (4 + len(CAT)) + '|']
for n, orig, foco, hc, aj in S28:
    L.append('| %d | %s | %s | %s | %s |' % (n, ' + '.join('%02d' % o for o in orig), foco, ' | '.join(str(hc.get(c, 0)) for c in CAT), aj))
open(os.path.join(AQUI, 'tablas_generadas.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')

print('Controles correctos: 36 encuentros de 5 HC; unidades 30/30/30/40/30/20; hitos H1 a H6; 28 encuentros que reúnen los 36 una sola vez; C1 a C10 conservadas.')
for c in CAT:
    print('%-28s 36: %3d HC (%5s %%)   28: %3d HC (%5s %%)' % (NOMBRE[c], t36[c], pct(t36[c], 180), t28[c], pct(t28[c], 140)))
