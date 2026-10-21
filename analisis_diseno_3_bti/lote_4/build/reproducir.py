# -*- coding: utf-8 -*-
"""Corre todas las pruebas del proyecto del lote 4 y registra el entorno exacto en que corrieron.
Uso: python3 lote_4/build/reproducir.py   →  lote_4/resultados_pruebas/*.txt y resumen.json (sale con 1 si algo falla)

1. Referencia docente: las ocho pruebas (contratos, operaciones del estudiante, carrera, garantías, respaldo,
   mantenimiento, marca huérfana y HTTP).
2. Base del estudiante: E-6b (prueba_base.sh), las heredadas del Piloto B que no dependen de las operaciones y
   prueba_mis_operaciones.php, que tiene que dar todo PENDIENTE y ninguna falla.
3. Reproducción del ejemplo del libro: en una copia de la base se completa OA-01 con la función de la referencia
   (la que el Capítulo 10 muestra en fragmentos) y se comprueba que pasan sus cinco pruebas PA-01.
4. Práctica 11 (v1.1): se genera practica_11/secuencia.json desde caso/mbokaja_u4.py y se corre
   practica_11/comprobar_practica_11.php sobre una base temporal, con el código de la referencia sin modificar.
El entorno de construcción NO es una computadora escolar: el resumen lo dice expresamente."""
import os, re, sys, json, shutil, subprocess, tempfile, platform, datetime
L4 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROY = os.path.join(L4, 'proyecto')
REF, BASE = os.path.join(PROY, 'referencia_docente'), os.path.join(PROY, 'base_estudiante')
OUT = os.path.join(L4, 'resultados_pruebas')

PRUEBAS_REF = ['prueba_contratos.php', 'prueba_mis_operaciones.php', 'prueba_carrera.php', 'prueba_garantias.php',
               'prueba_respaldo.php', 'prueba_mantenimiento.php', 'prueba_marca_huerfana.php', 'prueba_http.sh']
PRUEBAS_BASE = ['prueba_base.sh', 'prueba_garantias.php', 'prueba_respaldo.php', 'prueba_mantenimiento.php',
                'prueba_marca_huerfana.php', 'prueba_mis_operaciones.php']


def correr(carpeta, prueba):
    cmd = ['bash', 'pruebas/' + prueba] if prueba.endswith('.sh') else ['php', 'pruebas/' + prueba]
    p = subprocess.run(cmd, cwd=carpeta, capture_output=True, text=True, timeout=900)
    salida = p.stdout + p.stderr
    fin = [l for l in salida.strip().split('\n') if l.startswith('Resultado')]
    return p.returncode, salida, fin[-1] if fin else '(sin línea de resultado)'


def entorno():
    v = lambda c: subprocess.run(c, capture_output=True, text=True).stdout.strip()
    return {
        'fecha': datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
        'sistema': '%s %s (%s)' % (platform.system(), platform.release(), platform.machine()),
        'php': v(['php', '-r', 'echo PHP_VERSION;']),
        'sqlite': v(['php', '-r', 'echo (new PDO("sqlite::memory:"))->query("SELECT sqlite_version()")->fetchColumn();']),
        'extensiones': v(['php', '-r', 'echo implode(", ", array_values(array_intersect(get_loaded_extensions(), array("PDO", "pdo_sqlite", "session", "posix"))));']),
        'curl': v(['curl', '--version']).split('\n')[0],
        'tipo': 'Contenedor Linux de construcción del lote. NO es una computadora escolar ni Windows: '
                'las pruebas de campo E-1 a E-12 siguen pendientes.',
    }


def reproducir_ejemplo():
    """Copia la base, pega en OA-01 la función de la referencia y corre prueba_mis_operaciones.php."""
    tmp = tempfile.mkdtemp(prefix='ads_l4_ejemplo_')
    copia = os.path.join(tmp, 'base')
    shutil.copytree(BASE, copia)
    ref = open(os.path.join(REF, 'src', 'reglas.php'), encoding='utf8').read()
    fun = re.search(r'function alta_ejemplar\(.*?\n}\n', ref, re.S).group(0)
    p = os.path.join(copia, 'src', 'reglas.php')
    base = open(p, encoding='utf8').read()
    base = re.sub(r'function alta_ejemplar\(.*?\n}\n', lambda m: fun, base, count=1, flags=re.S)
    open(p, 'w', encoding='utf8').write(base)
    cod, salida, fin = correr(copia, 'prueba_mis_operaciones.php')
    shutil.rmtree(tmp, ignore_errors=True)
    pa01 = [l for l in salida.split('\n') if 'PA-01' in l]
    return {'codigo': cod, 'resultado': fin, 'pa01': pa01,
            'ok': cod == 0 and len(pa01) == 5 and all(l.startswith('CORRECTO') for l in pa01)}, salida


def practica_11():
    """Genera la secuencia de la Práctica 11 desde la fuente de Mbokaja y la comprueba en una base temporal."""
    sys.path.insert(0, os.path.join(L4, 'caso'))
    sys.dont_write_bytecode = True
    import mbokaja_u4 as MB
    carpeta = os.path.join(L4, 'practica_11')
    json.dump({'pasos': [list(p) for p in MB.PASOS_P11], 'consultas': [list(c) for c in MB.CONSULTAS_P11]},
              open(os.path.join(carpeta, 'secuencia.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    p = subprocess.run(['php', 'comprobar_practica_11.php'], cwd=carpeta, capture_output=True, text=True, timeout=300)
    salida = p.stdout + p.stderr
    fin = [l for l in salida.strip().split('\n') if l.startswith('Resultado')]
    return {'codigo': p.returncode, 'resultado': fin[-1] if fin else '(sin línea de resultado)',
            'ok': p.returncode == 0}, salida


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    res = {'entorno': entorno(), 'referencia_docente': {}, 'base_estudiante': {}}
    fallos = 0
    for nombre, carpeta, lista in (('referencia_docente', REF, PRUEBAS_REF), ('base_estudiante', BASE, PRUEBAS_BASE)):
        for pr in lista:
            cod, salida, fin = correr(carpeta, pr)
            pend = len(re.findall(r'^PENDIENTE', salida, re.M))
            res[nombre][pr] = {'codigo_salida': cod, 'resultado': fin, 'pendientes': pend}
            open(os.path.join(OUT, '%s__%s.txt' % (nombre, pr.rsplit('.', 1)[0])), 'w', encoding='utf8').write(
                'Entorno: %s\n\n%s' % (json.dumps(res['entorno'], ensure_ascii=False), salida))
            fallos += cod != 0
            print('%-20s %-28s %s%s' % (nombre, pr, fin, ('  (%d pendientes)' % pend) if pend else ''))
    ej, salida = reproducir_ejemplo()
    res['reproduccion_ejemplo_capitulo_10'] = ej
    e = res['entorno']
    open(os.path.join(OUT, 'reproduccion_ejemplo_capitulo_10.txt'), 'w', encoding='utf8').write(
        'Entorno: %s, PHP %s, SQLite %s\n\n' % (e['sistema'], e['php'], e['sqlite']) + salida)
    fallos += not ej['ok']
    print('Reproducción del ejemplo del Capítulo 10 (OA-01 completada en una copia de la base):', 'correcta' if ej['ok'] else 'FALLA', ej['pa01'])
    p11, salida = practica_11()
    res['practica_11'] = p11
    open(os.path.join(OUT, 'practica_11_mbokaja.txt'), 'w', encoding='utf8').write(salida)
    fallos += not p11['ok']
    print('Práctica 11 (correspondencia fija, base temporal):', p11['resultado'])
    pend_base = res['base_estudiante']['prueba_mis_operaciones.php']['pendientes']
    res['base_estudiante_operaciones_pendientes'] = pend_base
    res['fallos'] = fallos
    json.dump(res, open(os.path.join(OUT, 'resumen.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print('Entorno:', res['entorno']['sistema'], '· PHP', res['entorno']['php'], '· SQLite', res['entorno']['sqlite'])
    print('Fallos:', fallos)
    sys.exit(1 if fallos else 0)
