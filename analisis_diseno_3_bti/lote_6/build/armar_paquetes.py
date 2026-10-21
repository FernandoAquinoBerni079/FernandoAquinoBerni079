# -*- coding: utf-8 -*-
"""Arma los dos paquetes de la Unidad VI en lote_6/proyecto/, desde las fuentes del caso:
  - paquete_entrega_modelo/: copia NUEVA de la referencia docente v2 con SC-02 del lote 5 (decisión D-1, que no se
    modifica), con LEEME.txt y ENTREGA/*.md generados desde caso/entrega_u6.py (v1.1: sin comprobador dentro del
    paquete; la revisión la hacen las herramientas del docente de proyecto/herramientas/, fuera del paquete);
  - paquete_mbokaja/: el paquete del voluntario de la Práctica 17, con los cinco defectos de caso/mbokaja_u6.py.
El código copiado no se toca, salvo la prueba que cambia el defecto DM-3 en el paquete de Mbokaja.
corregir(carpeta) aplica la clave de la Práctica 17 a una copia (la usa build/reproducir.py, sobre carpetas temporales).
Uso: python3 lote_6/build/armar_paquetes.py"""
import os, sys, shutil
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
L6 = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(L6, 'caso'))
import entrega_u6 as E
import mbokaja_u6 as MB
PROY = os.path.join(L6, 'proyecto')
MODELO = os.path.join(PROY, 'paquete_entrega_modelo')
MBOKAJA = os.path.join(PROY, 'paquete_mbokaja')


def _copiar_codigo(destino):
    if os.path.exists(destino):
        shutil.rmtree(destino)
    shutil.copytree(E.ORIGEN, destino, ignore=shutil.ignore_patterns('*.sqlite', '*.sqlite-*', '__pycache__'))
    os.makedirs(os.path.join(destino, 'ENTREGA'), exist_ok=True)


def _escribir(carpeta, ruta, texto):
    open(os.path.join(carpeta, ruta), 'w', encoding='utf8').write(texto)


def modelo():
    _copiar_codigo(MODELO)
    for ruta, f in E.DOCUMENTOS.items():
        _escribir(MODELO, ruta, f())


def _logo(ruta):
    from PIL import Image, ImageDraw
    im = Image.new('RGB', (96, 96), (240, 236, 220))
    d = ImageDraw.Draw(im)
    d.rectangle((16, 30, 80, 78), outline=(120, 70, 30), width=3)
    d.polygon([(10, 32), (48, 10), (86, 32)], outline=(120, 70, 30))
    im.save(ruta, format='PNG', optimize=False)


def mbokaja():
    _copiar_codigo(MBOKAJA)
    cambiar = lambda t: t.replace(E.VERSION, MB.VERSION)
    for ruta, f in E.DOCUMENTOS.items():
        _escribir(MBOKAJA, ruta, cambiar(f()))
    _escribir(MBOKAJA, 'LEEME.txt', E.leeme_txt(MB.TITULO_LEEME, MB.VERSION))
    # DM-1: comando inexistente en la guía
    g = open(os.path.join(MBOKAJA, 'ENTREGA', 'INSTALAR.md'), encoding='utf8').read()
    _escribir(MBOKAJA, 'ENTREGA/INSTALAR.md', g.replace('```\nphp instalar.php\n```', '```\nphp instalar_base.php\n```', 1))
    # DM-2: datos de prueba que no están
    _escribir(MBOKAJA, 'ENTREGA/LISTA_ENTREGA.md', E.lista_md(E.ARCHIVOS_LISTA + [('datos/mbokaja_prueba.json',
                                                                                  'Datos de prueba de Mbokaja')], MB.VERSION))
    # DM-3: prueba vieja
    p = os.path.join(MBOKAJA, 'pruebas', 'prueba_contratos.php')
    src = open(p, encoding='utf8').read()
    assert MB.PRUEBA_VIEJA[0] in src
    _escribir(MBOKAJA, 'pruebas/prueba_contratos.php', src.replace(*MB.PRUEBA_VIEJA))
    # DM-4: imagen sin procedencia
    _logo(os.path.join(MBOKAJA, 'public', 'logo_mbokaja.png'))
    # DM-5: tarea de una pantalla que no existe
    E_TAREAS = E.TAREAS
    E.TAREAS = E_TAREAS + [MB.TAREA_FALSA]
    try:
        _escribir(MBOKAJA, 'ENTREGA/MANUAL.md', E.manual_md())
    finally:
        E.TAREAS = E_TAREAS


def corregir(carpeta):
    """La clave de la Práctica 17 (nivel 2), aplicada a una copia del paquete de Mbokaja."""
    def reemplazar(ruta, antes, despues):
        texto = open(ruta, encoding='utf8').read()
        assert antes in texto, (ruta, antes)
        open(ruta, 'w', encoding='utf8').write(texto.replace(antes, despues))
    reemplazar(os.path.join(carpeta, 'ENTREGA', 'INSTALAR.md'), 'php instalar_base.php', 'php instalar.php')
    open(os.path.join(carpeta, 'ENTREGA', 'LISTA_ENTREGA.md'), 'w', encoding='utf8').write(E.lista_md(None, MB.VERSION))
    reemplazar(os.path.join(carpeta, 'pruebas', 'prueba_contratos.php'), MB.PRUEBA_VIEJA[1], MB.PRUEBA_VIEJA[0])
    os.remove(os.path.join(carpeta, 'public', 'logo_mbokaja.png'))
    open(os.path.join(carpeta, 'ENTREGA', 'MANUAL.md'), 'w', encoding='utf8').write(E.manual_md())


if __name__ == '__main__':
    modelo()
    mbokaja()
    print('Paquetes armados en', PROY)
