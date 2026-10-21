# -*- coding: utf-8 -*-
"""Corre todas las pruebas del lote 6 y registra el entorno exacto en que corrieron → lote_6/resultados_pruebas/.
  1. Paquetes: se arman desde las fuentes (build/armar_paquetes.py) y se comprueba que el código del paquete modelo sea
     idéntico al de la referencia v2 con SC-02 del lote 5 (solo cambian LEEME.txt, ENTREGA/ y el comprobador).
  2. Comprobador de entrega: 0 incoherencias en el paquete modelo; en el de Mbokaja, exactamente las de la clave
     (caso/mbokaja_u6.py); en una copia corregida con la clave, 0.
  3. La guía como prueba (build/prueba_guia.py) sobre el paquete modelo y sobre la copia corregida de Mbokaja.
  4. Regresión completa de la versión empaquetada.
Todo corre sobre copias temporales. El entorno de construcción NO es una computadora escolar ni Windows, y una
ejecución automática NO es la instalación por otro equipo: el resumen lo dice expresamente.
Uso: python3 lote_6/build/reproducir.py"""
import os, sys, json, shutil, tempfile, subprocess, filecmp, datetime, platform
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
L6 = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
sys.path.insert(1, os.path.join(L6, 'caso'))
import armar_paquetes as A
import prueba_guia as PG
import mbokaja_u6 as MB
import entrega_u6 as E
OUT = os.path.join(L6, 'resultados_pruebas')
PRUEBAS = ['prueba_contratos.php', 'prueba_mis_operaciones.php', 'prueba_carrera.php', 'prueba_garantias.php',
           'prueba_respaldo.php', 'prueba_mantenimiento.php', 'prueba_marca_huerfana.php', 'prueba_http.sh', 'prueba_in02.sh']
DOCS_NUEVOS = {'LEEME.txt', 'comprobar_entrega.php'}


def sh(cmd, cwd=None):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=900)
    return p.returncode, p.stdout + p.stderr


def fin(salida):
    f = [l for l in salida.strip().split('\n') if l.startswith('Resultado')]
    return f[-1] if f else '(sin línea de resultado)'


def entorno():
    v = lambda c: subprocess.run(c, capture_output=True, text=True).stdout.strip()
    return {
        'fecha': datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
        'sistema': '%s %s (%s)' % (platform.system(), platform.release(), platform.machine()),
        'php': v(['php', '-r', 'echo PHP_VERSION;']),
        'sqlite': v(['php', '-r', 'echo (new PDO("sqlite::memory:"))->query("SELECT sqlite_version()")->fetchColumn();']),
        'curl': v(['curl', '--version']).split('\n')[0].split(' (')[0],
        'bash': v(['bash', '--version']).split('\n')[0],
        'tipo': 'Contenedor Linux de construcción del lote. NO es una computadora escolar ni Windows: las pruebas de campo '
                'E-1 a E-12 siguen pendientes. Una ejecución automática de la guía es una comprobación técnica: NO '
                'reemplaza la instalación por otro equipo, sin ayuda, que evalúa una persona ajena al desarrollo.',
    }


def escribir(nombre, E_, texto):
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, nombre), 'w', encoding='utf8').write(
        'Entorno: %s, PHP %s, SQLite %s (%s)\nCondición: comprobación técnica automática en el entorno de construcción\n\n%s'
        % (E_['sistema'], E_['php'], E_['sqlite'], E_['fecha'], texto))


def archivos(raiz):
    out = set()
    for d, _, fs in os.walk(raiz):
        for f in fs:
            r = os.path.relpath(os.path.join(d, f), raiz)
            if not f.endswith('.sqlite'):
                out.add(r)
    return out


def comprobar(paquete):
    cod, sal = sh(['php', 'comprobar_entrega.php'], cwd=paquete)
    inc = sorted(l.replace('INCOHERENCIA ', '') for l in sal.split('\n') if l.startswith('INCOHERENCIA'))
    return cod, sal, inc


def texto_guia(r):
    return '\n'.join('%s Paso %d. %s — %s%s' % ('CORRECTO' if x['correcto'] else 'FALLA   ', x['paso'], x['titulo'],
                                               x['comando'], ' (%s)' % x['nota'] if x['nota'] else '') for x in r) + \
        '\nResultado: %d de %d pasos correctos\n' % (sum(x['correcto'] for x in r), len(r))


if __name__ == '__main__':
    E_ = entorno(); res = {'entorno': E_}; fallos = 0
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    A.modelo(); A.mbokaja()

    # 1. el código del paquete modelo es el de la referencia v2 con SC-02
    origen, paq = archivos(E.ORIGEN), archivos(A.MODELO)
    distintos = sorted(r for r in origen & paq if not filecmp.cmp(os.path.join(E.ORIGEN, r), os.path.join(A.MODELO, r), shallow=False))
    nuevos = sorted(paq - origen)
    res['paquete_modelo'] = {'archivos': len(paq), 'distintos_del_origen': distintos, 'nuevos': nuevos,
                             'faltan_del_origen': sorted(origen - paq),
                             'codigo_identico': set(distintos) <= {'LEEME.txt'} and not (origen - paq)
                             and all(n.startswith('ENTREGA/') or n in DOCS_NUEVOS for n in nuevos)}
    fallos += not res['paquete_modelo']['codigo_identico']
    print('Paquete modelo: %d archivos; distintos del origen: %s; nuevos: %d' % (len(paq), distintos, len(nuevos)))

    # 2. comprobador de entrega
    c1, s1, i1 = comprobar(A.MODELO)
    c2, s2, i2 = comprobar(A.MBOKAJA)
    esperadas = MB.incoherencias_esperadas()
    tmp = tempfile.mkdtemp(prefix='ads_l6_')
    try:
        corr = os.path.join(tmp, 'mbokaja_corregido')
        shutil.copytree(A.MBOKAJA, corr)
        A.corregir(corr)
        c3, s3, i3 = comprobar(corr)
        coinciden = [x for x in i2 if any(x.startswith(e) for e in esperadas)]
        res['comprobador'] = {
            'modelo': {'codigo_salida': c1, 'incoherencias': i1, 'resultado': fin(s1)},
            'mbokaja': {'codigo_salida': c2, 'incoherencias': i2, 'resultado': fin(s2), 'esperadas': esperadas,
                        'exactas': len(i2) == len(esperadas) and len(coinciden) == len(esperadas)},
            'mbokaja_corregido': {'codigo_salida': c3, 'incoherencias': i3, 'resultado': fin(s3)}}
        escribir('comprobador_paquete_modelo.txt', E_, s1)
        escribir('comprobador_paquete_mbokaja.txt', E_, s2)
        escribir('comprobador_mbokaja_corregido.txt', E_, s3)
        fallos += not (c1 == 0 and not i1 and c2 == 1 and res['comprobador']['mbokaja']['exactas'] and c3 == 0 and not i3)
        print('Comprobador: modelo %s · Mbokaja %s (%s) · Mbokaja corregido %s' % (
            fin(s1), fin(s2), 'exactas' if res['comprobador']['mbokaja']['exactas'] else 'NO coinciden con la clave', fin(s3)))

        # 3. la guía como prueba
        res['guia'] = {}
        for clave, paquete in (('modelo', A.MODELO), ('mbokaja_corregido', corr), ('mbokaja_con_defectos', A.MBOKAJA)):
            r = PG.ejecutar(paquete)
            res['guia'][clave] = {'pasos': r, 'correctos': sum(x['correcto'] for x in r), 'total': len(r)}
            escribir('guia_%s.txt' % clave, E_, texto_guia(r))
            print('Guía %-22s %d de %d pasos' % (clave, res['guia'][clave]['correctos'], len(r)))
        fallos += res['guia']['modelo']['correctos'] != res['guia']['modelo']['total']
        fallos += res['guia']['mbokaja_corregido']['correctos'] != res['guia']['mbokaja_corregido']['total']
        fallos += res['guia']['mbokaja_con_defectos']['correctos'] == res['guia']['mbokaja_con_defectos']['total']

        # 4. regresión de la versión empaquetada
        res['regresion'] = {}
        for pr in PRUEBAS:
            c = os.path.join(tmp, 'r_' + pr.split('.')[0])
            shutil.copytree(A.MODELO, c)
            cod, sal = sh(['bash', 'pruebas/' + pr] if pr.endswith('.sh') else ['php', 'pruebas/' + pr], cwd=c)
            res['regresion'][pr] = {'codigo_salida': cod, 'resultado': fin(sal)}
            escribir('regresion_paquete_modelo__%s.txt' % pr.split('.')[0], E_, sal)
            fallos += cod != 0
            print('Regresión %-28s %s' % (pr, fin(sal)))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    for d in (A.MODELO, A.MBOKAJA):
        restos = [r for r in os.listdir(os.path.join(d, 'datos')) if r.endswith('.sqlite')]
        assert not restos, 'quedó una base en el paquete: %s' % restos
    res['fallos'] = fallos
    json.dump(res, open(os.path.join(OUT, 'resumen.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print('Entorno:', E_['sistema'], '· PHP', E_['php'], '· SQLite', E_['sqlite'])
    print('Fallos:', fallos)
    sys.exit(1 if fallos else 0)
