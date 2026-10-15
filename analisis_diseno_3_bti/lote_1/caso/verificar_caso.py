# -*- coding: utf-8 -*-
"""Controles de la fuente única del caso (caso/dossier.py).
  A. Coherencia interna: códigos únicos y correlativos, fuentes de las necesidades existentes, cifras de D2.
  B. Capítulo 4 v2 (y v2.1): cada fragmento que cita existe acá, en boca del entrevistado, y su texto coincide.
     Las reglas RN-01 a RN-06 y la necesidad N-02 de la Figura 4.2 coinciden.
  C. Candidato del Capítulo 2: E1, E2, E3 y O1 se conservan sin cambios en el texto.
  D. Ninguna persona ni título del caso de Algorítmica 3.º.
Uso: python3 caso/verificar_caso.py   (sale con código 1 si hay fallos)"""
import os, re, sys, importlib.util, hashlib

AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
import dossier as D

ok = fallos = 0
def chk(desc, cond):
    global ok, fallos
    if cond: ok += 1
    else: fallos += 1
    print(('CORRECTO ' if cond else 'FALLA    ') + desc)

def cargar(ruta, nombre):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

# ---------------------------------------------------------------- A. coherencia interna
codigos = [c for r in D.REGISTROS for c, _, _ in r['lineas']]
chk('A. %d líneas de registro con código único' % len(codigos), len(codigos) == len(set(codigos)))
for r in D.REGISTROS:
    pref = r['cod'] + ('-L' if r['tipo'] == 'entrevista' else '-A' if r['cod'] == 'D1' else '-')
    nums = [int(c[len(pref):]) for c, _, _ in r['lineas']]
    chk('A. %s: códigos %s1 a %s%d correlativos' % (r['cod'], pref, pref, len(nums)), nums == list(range(1, len(nums) + 1)))
    chk('A. %s: contexto con fecha, lugar y autorización o procedencia' % r['cod'], len(r['contexto']) > 40)
    if r['persona']:
        chk('A. %s: la persona %s existe' % (r['cod'], r['persona']), r['persona'] in D.NOMBRE)
for r in D.REGISTROS:
    if r['tipo'] == 'entrevista' and r['cod'] != 'E3':
        pila = D.NOMBRE[r['persona']].split()[-2]
        habs = [h for _, h, _ in r['lineas']]
        chk('A. %s: solo hablan «Analista» y %s' % (r['cod'], pila), set(habs) <= {'Analista', pila})
nec = [c for c, *_ in D.NECESIDADES]
chk('A. Necesidades N-01 a N-%02d correlativas' % len(nec), nec == ['N-%02d' % i for i in range(1, len(nec) + 1)])
for c, t, fs, est in D.NECESIDADES:
    chk('A. %s: tiene fuentes y todas existen (%s)' % (c, ', '.join(fs)), fs and all(f in D.TEXTO for f in fs))
for f, _ in D.NO_EXPRESADAS:
    chk('A. Necesidad no expresada apoyada en %s, que existe' % f, f in D.TEXTO)
nums = [int(re.search(r': (\d+) préstamos', D.TEXTO['D2-%d' % i]).group(1)) for i in range(1, 9)]
total = int(re.search(r'(\d+)', D.TEXTO['D2-9']).group(1))
chk('A. D2: los renglones suman %d y el total escrito es %d, como dicen E4-L11 y el módulo' % (sum(nums), total),
    sum(nums) == D.D2_SUMA_RENGLONES and total == D.D2_TOTAL_ESCRITO and
    str(D.D2_SUMA_RENGLONES) in D.TEXTO['E4-L11'] and str(D.D2_TOTAL_ESCRITO) in D.TEXTO['E4-L11'])
o = [int(re.match(r'(\d+)', D.TEXTO['O1-%d' % i].split('había ')[-1]).group(1)) if i == 1 else
     int(re.search(r'(\d+)', D.TEXTO['O1-%d' % i]).group(1)) for i in (1, 2, 3)]
chk('A. O1: en fila (%d) = préstamos (%d) + se fueron sin libro (%d)' % tuple(o), o[0] == o[1] + o[2])
chk('A. Las reglas son seis, RN-01 a RN-06', [c for c, _ in D.REGLAS] == ['RN-%02d' % i for i in range(1, 7)])
chk('A. Interesados: seis, con interés e influencia entre 0 y 10',
    len(D.INTERESADOS) == 6 and all(0 <= a <= 10 and 0 <= b <= 10 for _, a, b, _, _ in D.INTERESADOS))
chk('A. Alcance mínimo: siete funciones (Work §7.2), con «Permisos mínimos»',
    len(D.ALCANCE_NUCLEO) == 7 and any(f == 'Permisos mínimos' for f, _ in D.ALCANCE_NUCLEO))
chk('A. Fuera del núcleo: las ocho exclusiones de Work §7.2', len(D.FUERA_DEL_NUCLEO) == 8)

# ---------------------------------------------------------------- B. Capítulo 4 v2 y v2.1
for carpeta in ('A2_capitulo4_v2', 'A2_capitulo4_v2_1'):
    ruta = os.path.join(ADS, 'fase2_pilotos', carpeta, 'build', 'contenido.py')
    C4 = cargar(ruta, 'c4_' + carpeta)
    for reg, titulo, frs in C4.DOSSIER:
        r = D.REGISTRO.get(reg)
        chk('B. %s: el registro %s existe y se titula igual («%s»)' % (carpeta, reg, titulo), r is not None and r['titulo'] == titulo)
        for cod, txt in frs:
            hab, linea = D.LINEA.get(cod, (None, ''))
            chk('B. %s: %s existe, lo dice el entrevistado y contiene la cita textual' % (carpeta, cod),
                hab not in (None, 'Analista') and txt in linea)
    chk('B. %s: las reglas RN-01 a RN-06 coinciden palabra por palabra' % carpeta, C4.REGLAS == D.REGLAS)
    # Fuentes que cita cualquier texto del capítulo con formato E#-L#.
    texto = repr([getattr(C4, n) for n in dir(C4) if n.isupper()])
    citados = sorted(set(re.findall(r'\bE\d-L\d+\b', texto)))
    chk('B. %s: las %d fuentes E#-L# citadas en el capítulo existen en el caso' % (carpeta, len(citados)),
        all(c in D.TEXTO for c in citados))
dg = open(os.path.join(ADS, 'fase2_pilotos', 'A2_capitulo4_v2', 'build', 'diagramas.py'), encoding='utf8').read()
m = re.search(r"\('Necesidad\\nN-02', '([^']+)'\)", dg)
fig = m.group(1).replace('\\n', ' ') if m else ''
chk('B. Figura 4.2: N-02 «%s» coincide con el caso y su fuente E4-L4 es fuente de N-02' % fig,
    fig.startswith(D.NECESIDAD['N-02'].rstrip('.')[:30]) and 'E4-L4' in fig and 'E4-L4' in dict((c, f) for c, _, f, _ in D.NECESIDADES)['N-02'])
chk('B. N-02 dice lo mismo que el ejemplo de Work §7.3', D.NECESIDAD['N-02'] == 'Evitar entregar a dos lectores el mismo ejemplar.')
h = {c: hashlib.sha256(open(os.path.join(ADS, 'fase2_pilotos', c, 'build', 'contenido.py'), 'rb').read()).hexdigest()
     for c in ('A2_capitulo4_v2', 'A2_capitulo4_v2_1')}
chk('B. El Capítulo 4 no se modificó en este lote (contenido v2 = v2.1, SHA-256 %s…)' % h['A2_capitulo4_v2'][:12],
    len(set(h.values())) == 1)

# ---------------------------------------------------------------- C. candidato del Capítulo 2
CC = cargar(os.path.join(ADS, 'fase2_pilotos', 'A1_candidato_capitulo2', 'build', 'contenido.py'), 'cand2')
def lineas_candidato(bloque, pref):
    out = {}
    for s in bloque:
        m = re.match(r'^(L\d+|O1-\d+)\s+(?:(\w+): )?(.*)$', s)
        cod = m.group(1) if m.group(1).startswith('O1') else pref + '-' + m.group(1)
        out[cod] = (m.group(2), m.group(3))
    return out
for nombre, pref, bloque in (('E1', 'E1', CC.TRANSCRIPCION_E1[1]), ('E2', 'E2', CC.TRANSCRIPCION_E2[1]),
                             ('E3', 'E3', CC.EVAL_TEXTO_BASE[1]), ('O1', 'O1', CC.OBSERVACION_O1[1])):
    cand = lineas_candidato(bloque, pref)
    nuestras = {c: (h, t) for c, h, t in D.REGISTRO[nombre]['lineas']}
    chk('C. %s: las %d líneas del candidato se conservan con el mismo texto y hablante' % (nombre, len(cand)),
        set(cand) == set(nuestras) and all(cand[c][1] == nuestras[c][1] and (cand[c][0] or None) == nuestras[c][0] for c in cand))
chk('C. Presentación del caso: conserva la del candidato', D.CASO_PRESENTACION[0] == CC.CASO[0])
cand_int = [(f[0], float(f[1].replace(',', '.')), float(f[2].replace(',', '.')), f[3], f[4]) for f in CC.TABLA_EJ1[1]]
chk('C. Mapa de interesados: mismos interesados, valores, razones y estrategias que el candidato',
    cand_int == [(a, float(b), float(c), d, e) for a, b, c, d, e in D.INTERESADOS])

# ---------------------------------------------------------------- D. Algorítmica 3.º
todo = repr([getattr(D, n) for n in dir(D) if n.isupper() and n != 'PROHIBIDOS_ALGORITMICA'])
chk('D. Sin personas, títulos ni opciones tecnológicas del caso de Algorítmica 3.º',
    not any(p in todo for p in D.PROHIBIDOS_ALGORITMICA))
chk('D. Sin matriz ponderada en el caso', not re.search(r'(?i)ponderad|pesos?\b', todo))

print('\nResultado: %d correctos, %d fallos' % (ok, fallos))
sys.exit(1 if fallos else 0)
