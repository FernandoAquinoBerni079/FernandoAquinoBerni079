"""Controles de coherencia de la segunda muestra.

1. Capacidades: cada capacidad usada figura literalmente en el texto del
   programa MEC 2014 (PDF provisto por Fernando).
2. Tomo ↔ solucionario: cada ítem numerado del tomo tiene respuesta con el
   mismo número, y no hay respuestas para ítems inexistentes.
3. Tomo ↔ planes: cada actividad que cita un plan existe en el tomo, y todas
   las actividades del tomo quedan asignadas en el plan (clase o tarea).
4. Claves: distribución de letras correctas en las opciones múltiples.
5. Figuras y fichas citadas en los planes existen en el tomo.

No reemplaza la revisión visual ni la auditoría de contenido.

Uso: python3 verificar_muestra2.py PROGRAMA.txt
"""
import collections
import re
import sys
import unicodedata

from contenido_planes import PLANES
from contenido_solucionario import SECCIONES as SOL
from contenido_tomo import SECCIONES as TOMO

MAPA = {15: ('clase10', 'Clase 10'), 28: ('clase18', 'Clase 18'), 29: ('contF', 'Continuación F'),
        30: ('evalU5', 'EVALUACIÓN DE LA UNIDAD 5')}


def norm(s):
    s = unicodedata.normalize('NFC', s)
    s = re.sub(r'[•]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def items_tomo(bloques):
    nums = set()
    for b in bloques:
        if b[0] == 'item':
            m = re.match(r'(\d+)\.', b[1])
            if m:
                nums.add(int(m.group(1)))
    return nums


def textos(bloques):
    """Todo el texto de una lista de bloques, recorriendo listas anidadas."""
    out = []

    def rec(x):
        if isinstance(x, str):
            out.append(x)
        elif isinstance(x, (list, tuple)):
            for y in x:
                rec(y)
    rec(bloques)
    return ' '.join(out)


def main():
    programa = norm(open(sys.argv[1], encoding='utf-8').read())
    fallos, ok = [], 0

    # 1. capacidades literales
    caps = {b[1] for k in TOMO for b in TOMO[k] if b[0] == 'ficha'}
    for pl in PLANES:
        caps |= {c.strip() + ('' if c.strip().endswith('.') else '.') for c in re.split(r'(?<=\.)\s+', pl['capacidad']) if c.strip()}
    for c in sorted(caps):
        if norm(c) in programa:
            ok += 1
        else:
            fallos.append(f'Capacidad no literal: «{c}»')

    # 2. tomo ↔ solucionario
    for enc, (clave, nombre) in MAPA.items():
        nt = items_tomo(TOMO[clave])
        sec = next(s for s in SOL if s['encuentro'] == enc)
        ns = {int(n) for _, its in sec['bloques'] for n, _, _ in its if n.isdigit()}
        if clave == 'clase10' or clave == 'clase18':
            # en las clases, los números 1-3 de la fuente se repiten; se comparan los ítems de actividades
            pass
        faltan = sorted(nt - ns)
        sobran = sorted(ns - nt - ({1, 2, 3} if clave in ('clase10', 'clase18') else set()))
        if faltan:
            fallos.append(f'{nombre}: ítems sin respuesta en el solucionario: {faltan}')
        if sobran:
            fallos.append(f'{nombre}: respuestas sin ítem en el tomo: {sobran}')
        if not faltan and not sobran:
            ok += 1

    # 3. tomo ↔ planes
    for pl in PLANES:
        clave, nombre = MAPA[pl['n']]
        nt = items_tomo(TOMO[clave])
        texto_plan = ' '.join(x for _, pasos in pl['secuencia'] for paso in pasos for x in paso) + ' ' + pl['tarea']
        citados = set()
        for m in re.finditer(r'actividad(?:es)? ([\d ,y a]+)', texto_plan, re.I):
            frag = m.group(1)
            for a, b in re.findall(r'(\d+) a (\d+)', frag):
                citados |= set(range(int(a), int(b) + 1))
            frag = re.sub(r'\d+ a \d+', '', frag)
            citados |= {int(x) for x in re.findall(r'\d+', frag)}
        for m in re.finditer(r'consignas? (\d+) a (\d+)', texto_plan):
            citados |= set(range(int(m.group(1)), int(m.group(2)) + 1))
        for m in re.finditer(r'\(consigna (\d+)\)', texto_plan):
            citados.add(int(m.group(1)))
        if clave == 'evalU5':
            citados |= nt   # la prueba se resuelve completa («Partes A a F»)
        inexistentes = sorted(citados - nt)
        sin_asignar = sorted(nt - citados)
        if inexistentes:
            fallos.append(f'Plan {pl["n"]}: cita actividades que no existen en el tomo: {inexistentes}')
        if sin_asignar:
            fallos.append(f'Plan {pl["n"]}: actividades del tomo no asignadas: {sin_asignar}')
        if not inexistentes and not sin_asignar:
            ok += 1
        # 5. figuras y fichas citadas
        t_tomo = textos(TOMO[clave]) + ' ' + ' '.join(textos(TOMO[k]) for k in ('ficha18A', 'fichasF'))
        for ref in set(re.findall(r'(Figura \d+\.\d+|Figura F\.\d|Ficha (?:reproducible )?\d+-[A-Z]|Ficha F-[A-C])', texto_plan + pl['material'])):
            base = ref.replace('Ficha reproducible', 'Ficha')
            if base in t_tomo.replace('Ficha reproducible', 'Ficha') or ref in t_tomo:
                ok += 1
            else:
                fallos.append(f'Plan {pl["n"]}: cita «{ref}», que no está en el tomo')

    # 4. distribución de claves
    letras = collections.Counter()
    for sec in SOL:
        for nombre, its in sec['bloques']:
            for n, resp, _ in its:
                m = re.match(r'([a-d])\)', resp)
                if m:
                    letras[m.group(1)] += 1
    print('Distribución de claves de opción múltiple:', dict(sorted(letras.items())))
    if letras and max(letras.values()) - min(letras.get(x, 0) for x in 'abcd') > 3:
        fallos.append(f'Claves desbalanceadas: {dict(letras)}')
    else:
        ok += 1

    print(f'Controles correctos: {ok}. Fallos: {len(fallos)}.')
    for f in fallos:
        print(' -', f)
    sys.exit(1 if fallos else 0)


if __name__ == '__main__':
    main()
