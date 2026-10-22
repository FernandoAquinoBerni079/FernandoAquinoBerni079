# -*- coding: utf-8 -*-
"""Plantilla del conjunto RESERVADO (DR) de la Unidad V — exclusivo del docente. ESTE ARCHIVO NO TIENE DATOS.

Decisión 2 de Fernando (21-oct-2026): como el repositorio es público, no se publican los datos reservados, las semillas
privadas ni los resultados completos. Acá está solo la estructura y un generador: el docente lo corre con una semilla
que no anota en ningún archivo público, y la salida se escribe FUERA del repositorio (el generador se niega a escribir
adentro). Con el archivo generado, el docente crea la copia para la revisión cruzada (Práctica 15):
    php lote_5/proyecto/cargador_dp/cargar_dp.php --datos=<carpeta privada>/dr.json --sistema=<base> --destino=<copia>

Estructura (la misma de dp.json, para que el cargador la acepte):
  conjunto, parametros, obras, ediciones, ejemplares, lectores, prestamos, fecha_referencia, manual, esperado
  y, además, «casos»: los casos de la revisión cruzada con su resultado esperado, que el generador comprueba
  ejecutándolos sobre una copia descartable de la referencia docente v2 (la comprobación también queda afuera).
Códigos: rango 2000-8999, elegido al azar con la semilla (no se cruza con DP, que usa 1000-1999, ni con los lotes 1 a 4).
Uso: python3 lote_5/caso/dr_plantilla.py --semilla=<privada> --salida=<carpeta fuera del repositorio>"""
import os, sys, json, random, subprocess, tempfile, shutil

AQUI = os.path.dirname(os.path.abspath(__file__))
L5 = os.path.dirname(AQUI)
REPO = os.path.dirname(os.path.dirname(L5))     # raíz del repositorio (wt_libros)
sys.path.insert(0, AQUI)
import datos_prueba_u5 as DP

TITULOS = ['Cuentos de la siesta', 'El patio de las tejas', 'Plantas medicinales del monte', 'La escuela de barro',
           'Cartas al río', 'Números en el mercado', 'Mitos del cerro', 'El tren de la colonia', 'Canciones de cuna',
           'Atlas de las aves', 'La huerta de mi abuela', 'Historias del arroyo seco']
CURSOS = ['7.º grado', '8.º grado', '9.º grado', '1.º BTI', '2.º BTI', '3.º BTI']


def generar(semilla):
    rnd = random.Random(semilla)
    base = rnd.randrange(2, 9) * 1000 + rnd.randrange(0, 5) * 100
    cod = lambda p, i: '%s-%04d' % (p, base + i)
    tit = rnd.sample(TITULOS, 4)
    obras = [(cod('OB', i + 1), tit[i], 'Autor reservado (ficticio)') for i in range(4)]
    ediciones = [(cod('ED', i + 1), obras[i][0], 'Editorial reservada, %d' % rnd.randrange(2015, 2026)) for i in range(4)]
    ejemplares = []
    for i in range(10):
        ejemplares.append((cod('EJ', i + 1), ediciones[i % 4][0], 1))
    inactivo = rnd.randrange(0, 10)
    ejemplares[inactivo] = (ejemplares[inactivo][0], ejemplares[inactivo][1], 0)
    lectores = [(cod('LE', 1), 'Lector reservado 1 (ficticio)', 'estudiante', rnd.choice(CURSOS), 1),
                (cod('LE', 2), 'Lector reservado 2 (ficticio)', 'estudiante', rnd.choice(CURSOS), 1),
                (cod('LE', 3), 'Lector reservado 3 (ficticio)', 'docente', None, 1),
                (cod('LE', 4), 'Lector reservado 4 (ficticio)', 'estudiante', rnd.choice(CURSOS), 0)]
    mes = rnd.choice(['06', '07', '08', '09'])
    dia = rnd.randrange(3, 15)
    f = lambda d: '2026-%s-%02d' % (mes, d)
    libres = [e[0] for e in ejemplares if e[2] == 1]
    rnd.shuffle(libres)
    prestamos = [(libres[0], lectores[0][0], lectores[0][3], f(dia), f(dia + 7), None),
                 (libres[1], lectores[1][0], lectores[1][3], f(dia), f(dia + 7), None),
                 (libres[2], lectores[1][0], lectores[1][3], f(dia + 1), f(dia + 8), None),
                 (ejemplares[inactivo][0], lectores[3][0], lectores[3][3], f(1), f(8), f(2))]
    ref = f(dia + 7)
    casos = [  # (id, requisito, clase, operación, cuenta, entradas, código esperado)
        ('R-01', 'RF-05', 'Límite', 'OP-01', 'bibliotecaria', [lectores[1][0], libres[3], ref], 'ME-02'),
        ('R-02', 'RF-04', 'Rechazo', 'OP-01', 'bibliotecaria', [lectores[2][0], libres[0], ref], 'ME-03'),
        ('R-03', 'RF-06', 'Rechazo', 'OP-01', 'bibliotecaria', [lectores[3][0], libres[4], ref], 'ME-01'),
        ('R-04', 'RF-10', 'Rechazo', 'OP-01', 'bibliotecaria', [lectores[2][0], ejemplares[inactivo][0], ref], 'MV-06'),
        ('R-05', 'RF-01', 'Normal', 'OP-01', 'bibliotecaria', [lectores[0][0], libres[5], ref], 'ME-04'),
        ('R-06', 'RF-03', 'Normal', 'OP-02', 'bibliotecaria', [libres[1], f(dia + 9)], 'ME-07'),
        ('R-07', 'RF-03', 'Rechazo', 'OP-02', 'bibliotecaria', [libres[1], f(dia + 10)], 'ME-06'),
        ('R-08', 'RNF-02', 'Rechazo', 'OP-01', 'direccion', [lectores[0][0], libres[6], ref], 'ME-13'),
    ]
    d = {'conjunto': 'DR (reservado del docente, Unidad V; no publicar)', 'parametros': DP.PARAMETROS, 'obras': obras,
         'ediciones': ediciones, 'ejemplares': ejemplares, 'lectores': lectores, 'prestamos': prestamos,
         'fecha_referencia': ref, 'manual': []}
    # estado esperado con la misma regla que DP
    act = [p for p in prestamos if p[5] is None]
    disp = {}
    for o in obras:
        eds = [e[0] for e in ediciones if e[1] == o[0]]
        ejs = [x[0] for x in ejemplares if x[1] in eds and x[2] == 1]
        disp[o[0]] = [len(ejs), len([x for x in ejs if x not in [p[0] for p in act]])]
    d['esperado'] = {'obras': len(obras), 'ediciones': len(ediciones), 'ejemplares': len(ejemplares),
                     'lectores': len(lectores), 'prestamos': len(prestamos), 'prestamos_activos': len(act),
                     'activos_por_lector': {l[0]: len([p for p in act if p[1] == l[0]]) for l in lectores},
                     'ejemplares_y_disponibles_por_obra': disp}
    d['casos'] = [{'id': c[0], 'requisito': c[1], 'clase': c[2], 'descripcion': '', 'operacion': c[3], 'cuenta': c[4],
                   'entradas': c[5], 'esperado_codigo': c[6], 'control': None, 'esperado': c[6]} for c in casos]
    return d


def main():
    op = dict(a[2:].split('=', 1) for a in sys.argv[1:] if a.startswith('--') and '=' in a)
    if not op.get('semilla') or not op.get('salida'):
        sys.exit('Uso: python3 dr_plantilla.py --semilla=<privada> --salida=<carpeta fuera del repositorio>')
    salida = os.path.realpath(op['salida'])
    if (salida + os.sep).startswith(os.path.realpath(REPO) + os.sep):
        sys.exit('La salida tiene que estar FUERA del repositorio: el conjunto reservado no se publica.')
    if os.path.exists(os.path.join(salida, 'dr.json')):
        sys.exit('Ya hay un dr.json en %s: no se sobrescribe.' % salida)
    os.makedirs(salida, exist_ok=True)
    d = generar(op['semilla'])
    ruta = os.path.join(salida, 'dr.json')
    json.dump(d, open(ruta, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    # comprobación: cargar DR en una copia descartable de la referencia v2 y ejecutar los casos
    tmp = tempfile.mkdtemp(prefix='ads_dr_')
    try:
        copia = os.path.join(tmp, 'copia')
        p = subprocess.run(['php', os.path.join(L5, 'proyecto', 'cargador_dp', 'cargar_dp.php'), '--datos=' + ruta,
                            '--sistema=' + os.path.join(L5, 'proyecto', 'referencia_docente_v2'), '--destino=' + copia,
                            '--clave=docente-local'], capture_output=True, text=True)
        casos = os.path.join(tmp, 'casos.json')
        json.dump(d['casos'], open(casos, 'w', encoding='utf8'), ensure_ascii=False)
        q = subprocess.run(['php', os.path.join(L5, 'proyecto', 'matriz', 'ejecutar_matriz.php'), copia, casos],
                           capture_output=True, text=True)
        res = json.loads(q.stdout) if q.returncode == 0 else []
        bien = sum(1 for r in res if r.get('correcto'))
        informe = ('Conjunto reservado DR generado en %s\nCarga: %s\nCasos comprobados sobre la referencia v2: %d de %d\n'
                   % (ruta, 'correcta' if 'Estado esperado: correcto' in p.stdout else 'FALLA', bien, len(d['casos'])))
        open(os.path.join(salida, 'comprobacion_dr.txt'), 'w', encoding='utf8').write(informe + '\n' + q.stdout)
        print(informe)
        sys.exit(0 if bien == len(d['casos']) and 'Estado esperado: correcto' in p.stdout else 1)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    main()
