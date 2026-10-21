# -*- coding: utf-8 -*-
"""Plantilla del banco RESERVADO de variantes V6 para la defensa individual (Capítulo 18, Encuentro 35) — exclusivo del
docente. ESTE ARCHIVO NO TIENE LAS VARIANTES DEFINITIVAS.

Decisión de Fernando (21-oct-2026): los ejemplos de variantes pueden aparecer en la guía; las variantes definitivas se
reservan fuera del repositorio público, con un procedimiento similar al del conjunto DR del lote 5. Acá están solo los
campos de cada variante, tres ejemplos públicos (que no se usan en la defensa) y un validador que:
  - se niega a leer o escribir un banco que esté dentro del repositorio;
  - comprueba que cada variante tenga todos sus campos y un identificador único;
  - comprueba que ninguna variante repita un ejemplo público ni un texto que esté en el repositorio (libro, guía,
    bancos H3 a H5, evaluaciones);
  - avisa si hay menos variantes que estudiantes;
  - deja su informe junto al banco (fuera del repositorio).
Uso:
  python3 lote_6/caso/v6_plantilla.py --plantilla                      (imprime una variante vacía, en JSON)
  python3 lote_6/caso/v6_plantilla.py --banco=<ruta privada> [--estudiantes=N]"""
import os, sys, json, subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(AQUI)))
ADS = os.path.dirname(os.path.dirname(AQUI))
CAMPOS = [
    ('id', 'V6- y dos cifras'),
    ('situacion', 'El pedido o la regla nueva, como lo diría la biblioteca (una o dos oraciones)'),
    ('que_cambia', 'Requisito o regla que cambia, o requisito nuevo'),
    ('capas', 'Capas que toca: presentación, reglas de negocio, persistencia'),
    ('modelo_y_contratos', 'Qué cambia en el modelo de datos y en los contratos'),
    ('pruebas', 'Pruebas que habría que agregar o cambiar, y la regresión'),
    ('criterio_solido', 'Qué tiene que decir una respuesta de nivel Sólido'),
    ('criterio_logrado', 'Qué tiene que decir una respuesta de nivel Logrado'),
]
EJEMPLOS = [  # públicos: sirven para practicar en clase; NO se usan en la defensa individual
    {'id': 'V6-E1', 'situacion': 'Las revistas del colegio se van a prestar con un plazo de tres días; los libros siguen con siete.',
     'que_cambia': 'RF-02: el plazo depende del tipo de material, no solo del lector.',
     'capas': 'Reglas de negocio y persistencia (y la pantalla de alta de la obra).',
     'modelo_y_contratos': 'Tipo de material en la obra o la edición; plazo por tipo en Parámetro; contrato de OP-01 (cálculo del vencimiento).',
     'pruebas': 'Vencimiento de una revista y de un libro el mismo día; regresión de P-02, P-04 y C-12.',
     'criterio_solido': 'Ubica el dato en el modelo, no en el código; cambia el contrato y nombra la regresión de vencimientos.',
     'criterio_logrado': 'Dice qué regla cambia y una prueba nueva.'},
    {'id': 'V6-E2', 'situacion': 'La dirección quiere que el informe mensual separe los préstamos de los docentes por área.',
     'que_cambia': 'RF-09: un agrupamiento nuevo del informe.',
     'capas': 'Persistencia (dato nuevo del lector) y reglas de negocio (consulta de OP-05); presentación de PT-09.',
     'modelo_y_contratos': 'Área del docente en Lector; contrato de OP-05 con el agrupamiento nuevo.',
     'pruebas': 'Informe con docentes de dos áreas y un docente sin área; regresión de P-09 y C-16.',
     'criterio_solido': 'Prevé el docente sin área y conserva el total contado de nuevo.',
     'criterio_logrado': 'Agrega el dato y cambia el informe.'},
    {'id': 'V6-E3', 'situacion': 'Un ejemplar puede quedar «en reparación»: no se presta, pero tampoco está dado de baja.',
     'que_cambia': 'RF-10: un estado nuevo del ejemplar.',
     'capas': 'Persistencia y reglas de negocio; presentación de PT-08 y de la consulta pública.',
     'modelo_y_contratos': 'Estado del ejemplar (activo, en reparación, inactivo); precondición de OP-01; disponibles en OP-03.',
     'pruebas': 'Préstamo de un ejemplar en reparación (rechazo con su mensaje) y disponibles; regresión de P-10 y C-08.',
     'criterio_solido': 'Distingue el estado nuevo de la baja y cuida el historial y los disponibles.',
     'criterio_logrado': 'Agrega el estado y rechaza el préstamo.'},
]


def _dentro_del_repo(ruta):
    return (os.path.realpath(ruta) + os.sep).startswith(os.path.realpath(REPO) + os.sep)


def _texto_del_repo():
    fs = subprocess.run(['git', 'ls-files'], cwd=ADS, capture_output=True, text=True).stdout.split('\n')
    fs += subprocess.run(['git', 'ls-files', '--others', '--exclude-standard'], cwd=ADS, capture_output=True, text=True).stdout.split('\n')
    out = []
    for f in fs:
        p = os.path.join(ADS, f)
        if f and os.path.isfile(p) and f.endswith(('.py', '.md', '.json', '.txt', '.php', '.csv')):
            out.append(open(p, encoding='utf8', errors='ignore').read())
    return '\n'.join(out)


def validar(banco, estudiantes=0):
    fallas, avisos = [], []
    ids = [v.get('id') for v in banco]
    if len(set(ids)) != len(ids):
        fallas.append('hay identificadores repetidos')
    repo = _texto_del_repo()
    publicos = {e['situacion'] for e in EJEMPLOS}
    for v in banco:
        falta = [c for c, _ in CAMPOS if not str(v.get(c, '')).strip()]
        if falta:
            fallas.append('%s: faltan %s' % (v.get('id'), ', '.join(falta)))
        if not str(v.get('id', '')).startswith('V6-') or v.get('id', '').startswith('V6-E'):
            fallas.append('%s: el identificador tiene que ser V6- y dos cifras' % v.get('id'))
        s = str(v.get('situacion', ''))
        if s in publicos or (len(s) > 30 and s[:40] in repo):
            fallas.append('%s: su situación ya está en un ejemplo público o en el repositorio' % v.get('id'))
    if estudiantes and len(banco) < estudiantes:
        avisos.append('hay %d variantes para %d estudiantes: se repetirían' % (len(banco), estudiantes))
    return fallas, avisos


def main():
    op = dict(a[2:].split('=', 1) if '=' in a else (a[2:], '') for a in sys.argv[1:] if a.startswith('--'))
    if 'plantilla' in op:
        print(json.dumps([{c: '' for c, _ in CAMPOS}], ensure_ascii=False, indent=1)); return 0
    if not op.get('banco'):
        sys.exit(__doc__)
    if _dentro_del_repo(op['banco']):
        sys.exit('El banco de variantes tiene que estar FUERA del repositorio: las variantes definitivas no se publican.')
    banco = json.load(open(op['banco'], encoding='utf8'))
    fallas, avisos = validar(banco, int(op.get('estudiantes') or 0))
    informe = 'Banco V6: %d variantes. Fallas: %d. Avisos: %d.\n%s\n' % (len(banco), len(fallas), len(avisos),
                                                                       '\n'.join(['FALLA ' + f for f in fallas] + ['AVISO ' + a for a in avisos]))
    open(os.path.join(os.path.dirname(os.path.realpath(op['banco'])), 'comprobacion_v6.txt'), 'w', encoding='utf8').write(informe)
    print(informe)
    return 1 if fallas else 0


if __name__ == '__main__':
    sys.exit(main())
