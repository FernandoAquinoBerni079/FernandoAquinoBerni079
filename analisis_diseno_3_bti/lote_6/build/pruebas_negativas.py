# -*- coding: utf-8 -*-
"""Pruebas negativas de las herramientas del docente (v1.1, auditoría del lote 6). Cada caso arma una copia del paquete
modelo con un contenido hostil y comprueba que las herramientas NO ejecuten lo que el paquete propone: la inspección
estática no ejecuta nada, las pruebas en aislamiento solo corren la lista cerrada, en una copia descartable, sin red, con
una cuenta sin privilegios y con tiempo límite, y la guía como prueba no ejecuta formas de comando desconocidas.
Un «centinela» es un archivo de /tmp que el contenido hostil intentaría crear: si aparece, la herramienta ejecutó algo.
Uso: python3 lote_6/build/pruebas_negativas.py   (sale con 1 si algún caso falla)"""
import os, sys, glob, time, shutil, hashlib, tempfile, secrets
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import armar_paquetes as A
import herramientas_docente as H
import prueba_guia as PG


def _centinela():
    return '/tmp/ads_centinela_' + secrets.token_hex(6)


def _hash(raiz):
    h = hashlib.sha256()
    for d, ds, fs in sorted(os.walk(raiz)):
        ds.sort()
        for f in sorted(fs):
            p = os.path.join(d, f)
            h.update(os.path.relpath(p, raiz).encode())
            h.update(os.readlink(p).encode() if os.path.islink(p) else open(p, 'rb').read())
    return h.hexdigest()


def _agregar(paquete, ruta, texto):
    open(os.path.join(paquete, ruta), 'a', encoding='utf8').write(texto)


def _cambiar(paquete, ruta, texto):
    open(os.path.join(paquete, ruta), 'w', encoding='utf8').write(texto)


def n1(p, c):
    _agregar(p, 'ENTREGA/LISTA_ENTREGA.md', '- prueba: `php pruebas/prueba_contratos.php; touch %s`\n- prueba: `touch %s`\n' % (c, c))
    ci, si, ii = H.inspeccionar(p)
    ca, sa, ia, _ = H.probar_aislado(p)
    bien = (sum('no está en la lista cerrada: no se ejecuta' in x for x in ii) == 2 and ca == 0 and not ia
            and not os.path.exists(c))
    return bien, 'inspección: %d en [C]; pruebas aisladas: %s; centinela: %s' % (
        len(ii), H.incoherencias(sa) or 'solo la lista cerrada, bien', 'creado' if os.path.exists(c) else 'no creado')


def n2(p, c):
    _agregar(p, 'ENTREGA/INSTALAR.md', '\n### Paso 8. Paso agregado\n\n```\ntouch %s\n```\n\n### Paso 9. Otro paso\n\n'
             '```\nphp instalar.php; touch %s\n```\n\n### Paso 10. Otro más\n\n```\nphp $(touch %s).php\n```\n' % (c, c, c))
    ci, si, ii = H.inspeccionar(p)
    r = PG.ejecutar(p)
    rechazados = [x for x in r if x['paso'] >= 8 and not x['correcto'] and 'no permitida' in x['salida']]
    bien = sum('forma desconocida' in x for x in ii) == 3 and len(rechazados) == 3 and not os.path.exists(c)
    return bien, 'inspección: %d comandos de forma desconocida; guía como prueba: %d pasos rechazados sin ejecutar (%s)' % (
        sum('forma desconocida' in x for x in ii), len(rechazados), PG.ULTIMO.get('aislamiento'))


def n3(p, c):
    m = os.path.join(p, 'src', 'mensajes.php')
    t = open(m, encoding='utf8').read()
    _cambiar(p, 'src/mensajes.php', t.replace('<?php', "<?php\nfile_put_contents('%s', 'ejecutado');" % c, 1))
    ci, si, ii = H.inspeccionar(p)
    bien = ci == 0 and not os.path.exists(c)
    return bien, 'inspección: %s; centinela: %s' % (H.incoherencias(si) or '0 incoherencias (los mensajes se leyeron como texto)',
                                                    'creado' if os.path.exists(c) else 'no creado')


def n4(p, c):
    _agregar(p, 'ENTREGA/LISTA_ENTREGA.md', '- archivo: `../../../etc/passwd` — fuera\n- archivo: `/etc/passwd` — absoluta\n')
    g = open(os.path.join(p, 'ENTREGA', 'INSTALAR.md'), encoding='utf8').read()
    _cambiar(p, 'ENTREGA/INSTALAR.md', g.replace('```\nphp respaldar.php\n```', '```\nphp ../../herramientas/x.php\n```', 1))
    ci, si, ii = H.inspeccionar(p)
    bien = sum('fuera del paquete' in x for x in ii) == 2 and any(x.startswith('[A]') and '../../' in x for x in ii)
    return bien, 'inspección: %s' % ' · '.join(ii)


def n5(p, c):
    os.symlink('/etc/passwd', os.path.join(p, 'pruebas', 'prueba_respaldo.php.enlace'))
    ci, si, ii = H.inspeccionar(p)
    ca, sa, ia, _ = H.probar_aislado(p)
    bien = any('enlace simbólico' in x for x in ii) and ca == 2 and 'No se ejecutó ninguna prueba' in sa
    return bien, 'inspección: %s; pruebas aisladas: código %s, «%s»' % (
        ' · '.join(ii), ca, sa.strip().split('\n')[-1])


def n6(p, c):
    _cambiar(p, 'pruebas/prueba_contratos.php', "<?php\nfile_put_contents('%s', 'ejecutado');\necho \"Resultado: 1 de 1\\n\";\n" % c)
    ca, sa, ia, _ = H.probar_aislado(p, como_administrador=True)
    bien = ca == 2 and 'administrador' in sa and not os.path.exists(c)
    return bien, 'con cuenta de administrador: código %s, «%s»; centinela: %s' % (
        ca, sa.strip().split('\n')[0], 'creado' if os.path.exists(c) else 'no creado')


def n7(p, c):
    _cambiar(p, 'pruebas/prueba_respaldo.php', '<?php\nsleep(600);\necho "Resultado: nunca\\n";\n')
    t0 = time.time()
    ca, sa, ia, _ = H.probar_aislado(p, limite=2)
    seg = time.time() - t0
    bien = ca == 1 and ia == ['[C] la prueba pruebas/prueba_respaldo.php no terminó bien'] and 'tiempo límite' in sa and seg < 60
    return bien, 'prueba colgada: cortada por tiempo límite (2 s); la herramienta terminó en %.0f s; %s' % (seg, ' · '.join(ia))


def n8(p, c):
    antes = _hash(p)
    copias_antes = set(glob.glob('/tmp/ads_aislado_*'))
    ca, sa, ia, base = H.probar_aislado(p)
    quedan = set(glob.glob('/tmp/ads_aislado_*')) - copias_antes
    bien = ca == 0 and _hash(p) == antes and not quedan and base and not os.path.exists(base)
    return bien, 'paquete recibido sin cambios (SHA-256 igual: %s); copias descartables que quedaron: %d' % (
        _hash(p) == antes, len(quedan) + (1 if base and os.path.exists(base) else 0))


def n9(p, c):
    _cambiar(p, 'pruebas/prueba_extra.php', "<?php\nfile_put_contents('%s', 'ejecutado');\necho \"Resultado: 1 de 1\\n\";\n" % c)
    _agregar(p, 'ENTREGA/LISTA_ENTREGA.md', '- prueba: `php pruebas/prueba_extra.php`\n')
    ci, si, ii = H.inspeccionar(p)
    ca, sa, ia, _ = H.probar_aislado(p)
    bien = ii == ['[C] la prueba declarada «php pruebas/prueba_extra.php» no está en la lista cerrada: no se ejecuta'] \
        and ca == 0 and 'prueba_extra' not in sa and not os.path.exists(c)
    return bien, 'inspección: %s; pruebas aisladas: no se ejecutó prueba_extra; centinela: %s' % (
        ' · '.join(ii), 'creado' if os.path.exists(c) else 'no creado')


def n10(p, c):
    _cambiar(p, 'pruebas/prueba_garantias.php', "<?php\n$s = @fsockopen('1.1.1.1', 53, $e, $m, 3);\n"
             "$h = @fopen('/etc/shadow', 'r');\n"
             "echo 'Resultado: red=' . ($s ? 'SI' : 'NO') . ' admin=' . ($h ? 'SI' : 'NO') . \"\\n\";\n")
    ca, sa, ia, _ = H.probar_aislado(p)
    bien = ca == 0 and 'red=NO admin=NO' in sa and os.path.isfile('/etc/shadow')   # existe y es solo del administrador
    return bien, 'una prueba de la lista que intenta salir a la red y leer archivos del administrador: %s' % (
        [l for l in sa.split('\n') if 'prueba_garantias' in l] or ['(sin salida)'])[0].split('— ')[-1]


CASOS = [
    ('N1', 'Comando inyectado en la lista de entrega', n1),
    ('N2', 'Líneas maliciosas en la guía de instalación', n2),
    ('N3', 'src/mensajes.php con un efecto al incluirse', n3),
    ('N4', 'Rutas que salen del paquete', n4),
    ('N5', 'Enlace simbólico dentro del paquete', n5),
    ('N6', 'Pruebas en aislamiento con una cuenta de administrador', n6),
    ('N7', 'Una prueba de la lista cerrada que no termina', n7),
    ('N8', 'El paquete recibido no cambia y la copia descartable se borra', n8),
    ('N9', 'Una prueba fuera de la lista cerrada', n9),
    ('N10', 'Sin red y sin permisos de administrador durante las pruebas', n10),
]


def correr():
    res = []
    for cod, titulo, f in CASOS:
        tmp = tempfile.mkdtemp(prefix='ads_neg_')
        c = _centinela()
        try:
            p = os.path.join(tmp, 'paquete')
            shutil.copytree(A.MODELO, p, ignore=shutil.ignore_patterns('*.sqlite'))
            bien, det = f(p, c)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
            creado = os.path.exists(c)
            if creado:
                os.remove(c)
        res.append({'caso': cod, 'titulo': titulo, 'correcto': bool(bien) and not creado, 'detalle': det})
    return res


if __name__ == '__main__':
    r = correr()
    for x in r:
        print('%s %s %s — %s' % ('CORRECTO' if x['correcto'] else 'FALLA   ', x['caso'], x['titulo'], x['detalle']))
    print('Resultado: %d de %d pruebas negativas correctas' % (sum(x['correcto'] for x in r), len(r)))
    sys.exit(0 if all(x['correcto'] for x in r) else 1)
