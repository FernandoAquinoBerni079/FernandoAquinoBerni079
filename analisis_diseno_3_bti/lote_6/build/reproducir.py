# -*- coding: utf-8 -*-
"""Corre todas las pruebas del lote 6 y registra el entorno exacto en que corrieron → lote_6/resultados_pruebas/.
  1. Paquetes: se arman desde las fuentes (build/armar_paquetes.py) y se comprueba que el código del paquete modelo sea
     idéntico al de la referencia v2 con SC-02 del lote 5 (solo cambian LEEME.txt y ENTREGA/).
  2. Herramientas del docente (v1.1, fuera del paquete; build/herramientas_docente.py): la inspección estática y las
     pruebas en aislamiento dan 0 incoherencias en el paquete modelo; en el de Mbokaja, exactamente las de la clave
     (caso/mbokaja_u6.py), cada una con su herramienta; en una copia corregida con la clave, 0.
  3. La guía como prueba (build/prueba_guia.py, aislada) sobre el paquete modelo y sobre la copia corregida de Mbokaja.
  4. Pruebas negativas de las herramientas (build/pruebas_negativas.py).
  5. Regresión completa de la versión empaquetada (en una cuenta sin privilegios y sin red).
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
import herramientas_docente as H
import pruebas_negativas as PN
import mbokaja_u6 as MB
import entrega_u6 as E
OUT = os.path.join(L6, 'resultados_pruebas')
PRUEBAS = ['prueba_contratos.php', 'prueba_mis_operaciones.php', 'prueba_carrera.php', 'prueba_garantias.php',
           'prueba_respaldo.php', 'prueba_mantenimiento.php', 'prueba_marca_huerfana.php', 'prueba_http.sh', 'prueba_in02.sh']
DOCS_NUEVOS = {'LEEME.txt'}


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


def revisar(paquete):
    """Inspección estática y pruebas en aislamiento, con las herramientas del docente."""
    ci, si, ii = H.inspeccionar(paquete)
    ca, sa, ia, _ = H.probar_aislado(paquete)
    return {'inspeccion': {'codigo_salida': ci, 'incoherencias': ii, 'resultado': fin(si)},
            'aislamiento': {'codigo_salida': ca, 'incoherencias': ia, 'resultado': fin(sa)}}, si, sa


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

    # 2. herramientas del docente
    if not H.puede_aislar():
        print('AVISO: el entorno no permite aislar; las pruebas en aislamiento no se ejecutan')
    r1, si1, sa1 = revisar(A.MODELO)
    r2, si2, sa2 = revisar(A.MBOKAJA)
    tmp = tempfile.mkdtemp(prefix='ads_l6_')
    try:
        corr = os.path.join(tmp, 'mbokaja_corregido')
        shutil.copytree(A.MBOKAJA, corr)
        A.corregir(corr)
        r3, si3, sa3 = revisar(corr)
        exactas = {h: (r2[k]['incoherencias'] == MB.incoherencias_esperadas(h))
                   for k, h in (('inspeccion', MB.INSPECCION), ('aislamiento', MB.AISLAMIENTO))}
        r2['esperadas'] = {MB.INSPECCION: MB.incoherencias_esperadas(MB.INSPECCION),
                           MB.AISLAMIENTO: MB.incoherencias_esperadas(MB.AISLAMIENTO)}
        r2['exactas'] = all(exactas.values()) and len(MB.incoherencias_esperadas()) == 6
        res['herramientas'] = {'modelo': r1, 'mbokaja': r2, 'mbokaja_corregido': r3}
        for nombre, si, sa in (('paquete_modelo', si1, sa1), ('paquete_mbokaja', si2, sa2), ('mbokaja_corregido', si3, sa3)):
            escribir('inspeccion_%s.txt' % nombre, E_, si)
            escribir('aislamiento_%s.txt' % nombre, E_, sa)
        limpio = lambda r: all(r[k]['codigo_salida'] == 0 and not r[k]['incoherencias'] for k in ('inspeccion', 'aislamiento'))
        fallos += not (limpio(r1) and r2['exactas'] and r2['inspeccion']['codigo_salida'] == 1
                       and r2['aislamiento']['codigo_salida'] == 1 and limpio(r3))
        for nombre, r in (('modelo', r1), ('Mbokaja', r2), ('Mbokaja corregido', r3)):
            print('Herramientas %-18s inspección: %s · aislamiento: %s' % (nombre, r['inspeccion']['resultado'],
                                                                        r['aislamiento']['resultado']))
        print('Mbokaja: incoherencias %s con la clave' % ('exactas' if r2['exactas'] else 'que NO coinciden'))

        # 3. la guía como prueba
        res['guia'] = {}
        for clave, paquete in (('modelo', A.MODELO), ('mbokaja_corregido', corr), ('mbokaja_con_defectos', A.MBOKAJA)):
            r = PG.ejecutar(paquete)
            res['guia'][clave] = {'pasos': r, 'correctos': sum(x['correcto'] for x in r), 'total': len(r),
                                  'aislamiento': PG.ULTIMO.get('aislamiento')}
            escribir('guia_%s.txt' % clave, E_, texto_guia(r))
            print('Guía %-22s %d de %d pasos' % (clave, res['guia'][clave]['correctos'], len(r)))
        fallos += res['guia']['modelo']['correctos'] != res['guia']['modelo']['total']
        fallos += res['guia']['mbokaja_corregido']['correctos'] != res['guia']['mbokaja_corregido']['total']
        fallos += res['guia']['mbokaja_con_defectos']['correctos'] == res['guia']['mbokaja_con_defectos']['total']

        # 4. pruebas negativas de las herramientas
        res['pruebas_negativas'] = PN.correr()
        escribir('pruebas_negativas.txt', E_, '\n'.join('%s %s %s — %s' % ('CORRECTO' if x['correcto'] else 'FALLA   ',
                 x['caso'], x['titulo'], x['detalle']) for x in res['pruebas_negativas']) + '\nResultado: %d de %d pruebas '
                 'negativas correctas\n' % (sum(x['correcto'] for x in res['pruebas_negativas']), len(res['pruebas_negativas'])))
        fallos += not all(x['correcto'] for x in res['pruebas_negativas'])
        print('Pruebas negativas: %d de %d correctas' % (sum(x['correcto'] for x in res['pruebas_negativas']),
                                                         len(res['pruebas_negativas'])))

        # 5. regresión de la versión empaquetada: una copia de la cuenta sin privilegios, sin red
        res['regresion'] = {}
        for pr in PRUEBAS:
            base = tempfile.mkdtemp(prefix='ads_reg_', dir='/tmp')
            os.chmod(base, 0o755)
            c = os.path.join(base, 'paquete')
            shutil.copytree(A.MODELO, c, ignore=shutil.ignore_patterns('*.sqlite'))
            aislar = []
            if H.puede_aislar():
                for d, _, fs in os.walk(c):
                    for x in [d] + [os.path.join(d, f) for f in fs]:
                        os.lchown(x, H.NADIE, H.NADIE)
                aislar = ['unshare', '-n', sys.executable, '-I', os.path.join(AQUI, 'con_red_local.py')] + H.SIN_PRIVILEGIOS
            cod, sal = sh(aislar + (['bash', 'pruebas/' + pr] if pr.endswith('.sh') else ['php', 'pruebas/' + pr]), cwd=c)
            shutil.rmtree(base, ignore_errors=True)
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
