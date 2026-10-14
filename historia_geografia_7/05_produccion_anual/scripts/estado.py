"""Tabla de estado de los 36 encuentros y manifiesto de archivos.

Estados (acumulativos): desarrollado, verificado automáticamente,
inspeccionado visualmente, pendiente de auditoría, aprobado. «Aprobado» solo
lo registra Fernando; este script nunca lo marca solo.

Uso:
  python3 estado.py marcar CAMPO N [N ...]   (CAMPO: desarrollado | verificado | visual | auditoria)
  python3 estado.py tabla                    (regenera ESTADO_36_ENCUENTROS.md y MANIFIESTO.json)
"""
import hashlib
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
import curriculo as C  # noqa: E402

ARCHIVO = os.path.join(RAIZ, 'datos', 'estado.json')
CAMPOS = ('desarrollado', 'verificado', 'visual', 'auditoria', 'aprobado')
ROTULOS = {'desarrollado': 'Desarrollado', 'verificado': 'Verificado automáticamente', 'visual': 'Inspeccionado visualmente',
           'auditoria': 'Pendiente de auditoría', 'aprobado': 'Aprobado'}


def cargar():
    if os.path.exists(ARCHIVO):
        return json.load(open(ARCHIVO, encoding='utf-8'))
    return {str(n): {c: False for c in CAMPOS} for n in range(1, 37)}


def guardar(est):
    json.dump(est, open(ARCHIVO, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def marcar(campo, ns, valor=True):
    assert campo in CAMPOS[:-1], 'el estado «aprobado» solo lo registra Fernando'
    est = cargar()
    for n in ns:
        est[str(n)][campo] = valor
    guardar(est)


def bloque_de(n):
    return next(b for b, r in C.BLOQUES.items() if n in r)


def tabla():
    est = cargar()
    sys.path.insert(0, os.path.join(AQUI, 'contenido'))
    lineas = ['# Estado de los 36 encuentros', '',
              'Se genera con `scripts/estado.py tabla`. «Sí» indica que el encuentro superó esa etapa. «Aprobado» lo registra '
              'solo Fernando.', '',
              '| N.º | Bloque | Sección | Tipo | Capacidades | ' + ' | '.join(ROTULOS[c] for c in CAMPOS) + ' |',
              '|---:|:---:|---|---|---|' + '|'.join([':---:'] * len(CAMPOS)) + '|']
    for e in C.ENCUENTROS:
        n, tipo, sec, _, caps, _, _ = e
        titulo = sec
        try:
            m = __import__(f'e{n:02d}')
            titulo = m.TITULO
        except ImportError:
            pass
        fila = [str(n), str(bloque_de(n)), titulo, tipo, ', '.join(caps) or '— (editorial)']
        fila += ['Sí' if est[str(n)][c] else '—' for c in CAMPOS]
        lineas.append('| ' + ' | '.join(fila) + ' |')
    open(os.path.join(RAIZ, 'ESTADO_36_ENCUENTROS.md'), 'w', encoding='utf-8').write('\n'.join(lineas) + '\n')
    man = []
    for base, _, archivos in os.walk(RAIZ):
        if '__pycache__' in base:
            continue
        for a in sorted(archivos):
            if a == 'MANIFIESTO.json' or a.endswith('.pyc'):
                continue
            p = os.path.join(base, a)
            man.append({'archivo': os.path.relpath(p, RAIZ), 'bytes': os.path.getsize(p),
                        'sha256': hashlib.sha256(open(p, 'rb').read()).hexdigest()})
    man.sort(key=lambda x: x['archivo'])
    json.dump({'carpeta': 'historia_geografia_7/05_produccion_anual', 'modelo': '841f5bc9e4a4fec11af63cc821fc3062a6587de8',
               'archivos': man}, open(os.path.join(RAIZ, 'MANIFIESTO.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    if sys.argv[1] == 'marcar':
        marcar(sys.argv[2], [int(x) for x in sys.argv[3:]])
    elif sys.argv[1] == 'tabla':
        tabla()
