# -*- coding: utf-8 -*-
"""Corre todas las pruebas del lote 5 y registra el entorno exacto en que corrieron.
Uso: python3 lote_5/build/reproducir.py   →  lote_5/resultados_pruebas/*.txt y resumen.json (sale con 1 si algo falla)

1. Genera desde las fuentes (caso/) los archivos que leen los programas PHP: proyecto/cargador_dp/dp.json,
   proyecto/matriz/casos.json y esperados_sc02.json.
2. Cargador DP: crea copias descartables desde la referencia v2 y desde la base del estudiante del lote 4, comprueba
   el estado esperado, que la huella de los datos sea la misma (reproducible) y que se niegue a sobrescribir.
3. Matriz del equipo modelo (C-01 a C-20) sobre copias con DP de tres sistemas: la referencia del lote 4 (v1, la que
   se prueba en los Capítulos 14 y 15), la v2 (corrección de IN-02) y la v2 con SC-02.
4. IN-02: prueba_in02.sh sobre una copia de la referencia del lote 4 (tiene que fallar: reproducción) y sobre la v2.
5. Regresión: las pruebas del lote 4 sobre la v2 y sobre la v2 con SC-02, más prueba_in02.sh.
6. Integración (Capítulo 15) sobre una copia con DP de la v2: permisos de la Tabla 11.3 con las tres cuentas,
   persistencia entre dos procesos y restauración de un respaldo (E-11, E-12).
Ninguna prueba toca lote_4/ ni las carpetas de las referencias: todo corre en copias temporales.
El entorno de construcción NO es una computadora escolar: el resumen lo dice expresamente."""
import os, re, sys, json, shutil, subprocess, tempfile, platform, datetime, glob
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
L5 = os.path.dirname(AQUI)
ADS = os.path.dirname(L5)
sys.path.insert(0, os.path.join(L5, 'caso'))
import datos_prueba_u5 as DP
import verificacion as V
import mbokaja_u5 as MB5

PROY = os.path.join(L5, 'proyecto')
V1 = os.path.join(ADS, 'lote_4', 'proyecto', 'referencia_docente')
BASE4 = os.path.join(ADS, 'lote_4', 'proyecto', 'base_estudiante')
V2 = os.path.join(PROY, 'referencia_docente_v2')
SC = os.path.join(PROY, 'referencia_docente_v2_sc02')
CARGADOR = os.path.join(PROY, 'cargador_dp', 'cargar_dp.php')
MATRIZ = os.path.join(PROY, 'matriz')
OUT = os.path.join(L5, 'resultados_pruebas')
PRUEBAS_L4 = ['prueba_contratos.php', 'prueba_mis_operaciones.php', 'prueba_carrera.php', 'prueba_garantias.php',
              'prueba_respaldo.php', 'prueba_mantenimiento.php', 'prueba_marca_huerfana.php', 'prueba_http.sh']


def sh(cmd, cwd=None, env=None):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=900, env=env)
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
        'tipo': 'Contenedor Linux de construcción del lote. NO es una computadora escolar ni Windows: '
                'las pruebas de campo E-1 a E-12 siguen pendientes.',
    }


def generar_entradas():
    DP.escribir(os.path.join(PROY, 'cargador_dp', 'dp.json'))
    json.dump(V.casos_json(), open(os.path.join(MATRIZ, 'casos.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    json.dump(V.ESPERADO_SC02, open(os.path.join(MATRIZ, 'esperados_sc02.json'), 'w', encoding='utf8'), indent=1)
    json.dump(MB5.p14_json(), open(os.path.join(PROY, 'cargador_dp', 'mbokaja_p14.json'), 'w', encoding='utf8'),
              ensure_ascii=False, indent=1)
    json.dump(MB5.casos_p14_json(), open(os.path.join(MATRIZ, 'casos_p14.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)


def copia_dp(sistema, tmp, nombre):
    destino = os.path.join(tmp, nombre)
    cod, sal = sh(['php', CARGADOR, '--sistema=' + sistema, '--destino=' + destino, '--clave=prueba-solo-local'])
    huella = re.search(r'Huella de los datos: ([0-9a-f]+)', sal)
    return destino, cod, sal, huella.group(1) if huella else None


def in02(sistema, tmp, nombre):
    """prueba_in02.sh sobre una copia del sistema (la del lote 4 no la trae: se le agrega para reproducir)."""
    c = os.path.join(tmp, nombre)
    shutil.copytree(sistema, c, ignore=shutil.ignore_patterns('biblioteca.sqlite*'))
    shutil.copy(os.path.join(V2, 'pruebas', 'prueba_in02.sh'), os.path.join(c, 'pruebas', 'prueba_in02.sh'))
    return sh(['bash', 'pruebas/prueba_in02.sh'], cwd=c)


def matriz(sistema, tmp, nombre, alternativos=None):
    c, cod, sal, huella = copia_dp(sistema, tmp, nombre)
    cmd = ['php', os.path.join(MATRIZ, 'ejecutar_matriz.php'), c, os.path.join(MATRIZ, 'casos.json')]
    if alternativos:
        cmd.append(os.path.join(MATRIZ, 'esperados_sc02.json'))
    cod2, sal2 = sh(cmd)
    res = json.loads(sal2[sal2.index('['):]) if cod2 == 0 else []
    http_cod, http_sal = in02(sistema, tmp, nombre + '_http')
    for r in res:
        if r['id'] == 'C-20':
            r.update({'ejecutado': True, 'correcto': http_cod == 0, 'esperado_codigo': None,
                      'obtenido': {'resultado': fin(http_sal)}})
    return res, cod == 0 and cod2 == 0, huella


def escribir(nombre, entorno_, texto):
    open(os.path.join(OUT, nombre), 'w', encoding='utf8').write(
        'Entorno: %s, PHP %s, SQLite %s (%s)\n\n%s' % (entorno_['sistema'], entorno_['php'], entorno_['sqlite'],
                                                       entorno_['fecha'], texto))


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    generar_entradas()
    E = entorno()
    res = {'entorno': E}
    fallos = 0
    tmp = tempfile.mkdtemp(prefix='ads_l5_')
    try:
        # 2. cargador DP
        c1, k1, s1, h1 = copia_dp(V2, tmp, 'dp_v2')
        c2, k2, s2, h2 = copia_dp(BASE4, tmp, 'dp_base')
        k3, s3 = sh(['php', CARGADOR, '--sistema=' + V2, '--destino=' + c1])
        intacta = not glob.glob(os.path.join(V2, 'datos', '*.sqlite')) and not glob.glob(os.path.join(V1, 'datos', '*.sqlite'))
        ok_dp = k1 == 0 and k2 == 0 and h1 == h2 and k3 != 0 and 'No se cambió nada' in s3 and intacta
        res['cargador_dp'] = {'estado_esperado_v2': 'Estado esperado: correcto' in s1,
                              'estado_esperado_base_estudiante': 'Estado esperado: correcto' in s2,
                              'misma_huella': h1 == h2, 'huella': h1, 'se_niega_a_sobrescribir': k3 != 0,
                              'origen_sin_base_creada': intacta, 'ok': ok_dp}
        escribir('cargador_dp.txt', E, s1 + '\n--- desde la base del estudiante (lote 4)\n' + s2
                 + '\n--- segunda carga sobre la misma carpeta (tiene que negarse)\n' + s3)
        fallos += not ok_dp
        print('Cargador DP:', 'correcto' if ok_dp else 'FALLA', '· huella', h1)

        # 2 bis. Práctica 14: carga de Mbokaja con --datos y casos de la guía sobre la referencia v2
        dest = os.path.join(tmp, 'p14')
        kp14, sp14 = sh(['php', CARGADOR, '--datos=' + os.path.join(PROY, 'cargador_dp', 'mbokaja_p14.json'),
                         '--sistema=' + V2, '--destino=' + dest, '--clave=prueba-solo-local'])
        kc, sc = sh(['php', os.path.join(MATRIZ, 'ejecutar_matriz.php'), dest, os.path.join(MATRIZ, 'casos_p14.json')])
        p14 = json.loads(sc[sc.index('['):]) if kc == 0 else []
        ok14 = kp14 == 0 and p14 and all(r['correcto'] for r in p14)
        res['practica_14'] = {'carga': 'Estado esperado: correcto' in sp14, 'casos': p14,
                              'correctos': sum(1 for r in p14 if r['correcto']), 'total': len(p14), 'ok': bool(ok14)}
        escribir('practica_14_mbokaja.txt', E, sp14 + '\n' + sc)
        fallos += not ok14
        print('Práctica 14 (Mbokaja, referencia v2): %d de %d' % (res['practica_14']['correctos'], len(p14)))

        # 3. matriz del equipo modelo
        res['matriz'] = {}
        for clave, sistema, alt in (('v1_lote4', V1, False), ('v2', V2, False), ('v2_sc02', SC, True)):
            filas, ok, huella = matriz(sistema, tmp, 'm_' + clave, alt)
            res['matriz'][clave] = {'casos': filas, 'correctos': sum(1 for f in filas if f['correcto']),
                                    'total': len(filas), 'huella_dp': huella}
            escribir('matriz_%s.txt' % clave, E, json.dumps(filas, ensure_ascii=False, indent=1))
            malos = [f['id'] for f in filas if not f['correcto']]
            print('Matriz %-9s %d de %d correctos%s' % (clave, len(filas) - len(malos), len(filas),
                                                         ('; no correctos: %s' % malos) if malos else ''))
            # en v1 se espera exactamente C-20 (IN-02); en v2 y v2_sc02, todos correctos
            fallos += not ok or malos != (['C-20'] if clave == 'v1_lote4' else [])

        # 4. IN-02: reproducción y corrección
        ca, sa = in02(V1, tmp, 'in02_v1')
        cb, sb = in02(V2, tmp, 'in02_v2')
        res['in02'] = {'lote4': fin(sa), 'lote4_falla': ca != 0, 'v2': fin(sb), 'v2_correcta': cb == 0}
        escribir('in02_reproduccion_lote4.txt', E, sa)
        escribir('in02_correccion_v2.txt', E, sb)
        fallos += not (ca != 0 and cb == 0)
        print('IN-02: lote 4', fin(sa), '(se reproduce) · v2', fin(sb))

        # 5. regresión
        res['regresion'] = {}
        for clave, sistema in (('v2', V2), ('v2_sc02', SC)):
            res['regresion'][clave] = {}
            for pr in PRUEBAS_L4 + ['prueba_in02.sh']:
                c = os.path.join(tmp, 'r_%s_%s' % (clave, pr.split('.')[0]))
                shutil.copytree(sistema, c, ignore=shutil.ignore_patterns('biblioteca.sqlite*'))
                cmd = ['bash', 'pruebas/' + pr] if pr.endswith('.sh') else ['php', 'pruebas/' + pr]
                cod, sal = sh(cmd, cwd=c)
                res['regresion'][clave][pr] = {'codigo_salida': cod, 'resultado': fin(sal)}
                escribir('regresion_%s__%s.txt' % (clave, pr.split('.')[0]), E, sal)
                fallos += cod != 0
                print('Regresión %-8s %-28s %s' % (clave, pr, fin(sal)))

        # 6. integración sobre copias con DP de la v1 (lo que prueba el Capítulo 15) y de la v2 (regresión)
        integ = os.path.join(MATRIZ, 'integracion.php')
        res['integracion'] = {}
        for clave, sistema in (('v1_lote4', V1), ('v2', V2)):
            c, _, _, _ = copia_dp(sistema, tmp, 'integ_' + clave)
            kp, sp = sh(['php', integ, c, 'permisos'])
            c2, _, _, _ = copia_dp(sistema, tmp, 'persist_' + clave)
            kw, sw = sh(['php', integ, c2, 'escribir'])
            kr, sr = sh(['php', integ, c2, 'leer'])
            c3, _, _, _ = copia_dp(sistema, tmp, 'restaurar_' + clave)
            kb, sb_ = sh(['php', 'respaldar.php'], cwd=c3)
            resp = sorted(glob.glob(os.path.join(c3, 'datos', 'respaldos', '*.sqlite')))
            kw2, sw2 = sh(['php', integ, c3, 'escribir'])
            kx, sx = sh(['php', 'restaurar.php', resp[-1] if resp else 'no-hay', '--si'], cwd=c3)
            ky, sy = sh(['php', integ, c3, 'leer'])     # tiene que FALLAR: el respaldo es anterior al préstamo
            previa = glob.glob(os.path.join(c3, 'datos', 'respaldos', 'antes_de_restaurar_*.sqlite'))
            ok_rest = kb == 0 and bool(resp) and kw2 == 0 and kx == 0 and ky != 0 and bool(previa)
            permisos = [l for l in sp.split('\n') if l.startswith(('CORRECTO', 'FALLA'))]
            res['integracion'][clave] = {'permisos': fin(sp), 'permisos_ok': kp == 0, 'permisos_detalle': permisos,
                                         'persistencia': kw == 0 and kr == 0, 'restauracion': ok_rest,
                                         'copia_previa_a_restaurar': bool(previa)}
            escribir('integracion_%s_permisos.txt' % clave, E, sp)
            escribir('integracion_%s_persistencia.txt' % clave, E, sw + '\n--- otro proceso\n' + sr)
            escribir('integracion_%s_restauracion.txt' % clave, E, sb_ + '\n--- cambio después del respaldo\n' + sw2
                     + '\n--- restauración\n' + sx + '\n--- el cambio ya no está (se espera FALLA en la lectura)\n' + sy)
            fallos += not (kp == 0 and kw == 0 and kr == 0 and ok_rest)
            print('Integración %-8s permisos %s · persistencia %s · restauración %s' % (
                clave, fin(sp), 'correcta' if kw == 0 and kr == 0 else 'FALLA', 'correcta' if ok_rest else 'FALLA'))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    res['fallos'] = fallos
    json.dump(res, open(os.path.join(OUT, 'resumen.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print('Entorno:', E['sistema'], '· PHP', E['php'], '· SQLite', E['sqlite'])
    print('Fallos:', fallos)
    sys.exit(1 if fallos else 0)
