# -*- coding: utf-8 -*-
"""Arma analisis_diseno_3_bti/ENTREGA_COMERCIAL_FINAL/ desde edicion_v1_0/salida/ (documentos y cubiertas) y los recursos
digitales de los lotes, que solo se copian. No incluye datos reservados (DR, V6) ni archivos temporales.
Uso: python3 -B analisis_diseno_3_bti/edicion_v1_0/build/empaquetar.py   (después de documentos, plan y cubiertas)
"""
import json, os, re, shutil, sys
sys.dont_write_bytecode = True
import pymupdf
AQUI = os.path.dirname(os.path.abspath(__file__)); ED = os.path.dirname(AQUI); ADS = os.path.dirname(ED)
sys.path.insert(0, AQUI)
import cubiertas as CU
import textos_entrega as TX

SAL = os.path.join(ED, 'salida'); CUB = os.path.join(SAL, 'cubiertas')
ENT = os.path.join(ADS, 'ENTREGA_COMERCIAL_FINAL')
DATOS = json.load(open(os.path.join(ED, 'datos_edicion.json'), encoding='utf8'))
ORDEN = CU.ORDEN
CARPETA = {'libro': '01_LIBRO_DEL_ESTUDIANTE', 'cuaderno': '02_CUADERNO_DE_PRACTICAS', 'guia': '03_GUIA_DOCENTE_CON_SOLUCIONARIO',
           'plan_anual': '04_PLAN_ANUAL', 'planes': '05_PLANES_DE_CLASE'}
EDITABLE = {'guia', 'plan_anual', 'planes'}           # DOCX que se entregan para editar
RECURSOS = ['lote_4/proyecto', 'lote_5/proyecto', 'lote_5/caso', 'lote_6/proyecto', 'lote_6/caso', 'lote_6/instrumentos']
IGNORAR = shutil.ignore_patterns('__pycache__', '*.pyc', '*.sqlite', '*.sqlite3', '*.db', '*.bak', '*~', '.DS_Store',
                                 'dr.json', 'variantes_v6.json', 'comprobacion_*.txt')


def digital(clave):
    """Tapa + interior + contratapa, con marcadores, numeración de páginas del interior y metadatos."""
    P = CU.PRODUCTOS[clave]; base = P['archivo']
    interior = pymupdf.open(os.path.join(SAL, base + '.pdf'))
    d = pymupdf.open()
    d.insert_pdf(pymupdf.open(os.path.join(CUB, base + '_TAPA.pdf')))
    d.insert_pdf(interior)
    d.insert_pdf(pymupdf.open(os.path.join(CUB, base + '_CONTRATAPA.pdf')))
    toc = [[1, 'Tapa', 1]] + [[l, t, p + 1] for l, t, p in interior.get_toc()] + [[1, 'Contratapa', len(d)]]
    d.set_toc(toc)
    d.set_page_labels([{'startpage': 0, 'prefix': 'Tapa', 'style': ''},
                       {'startpage': 1, 'prefix': '', 'style': 'D', 'firstpagenum': 1},
                       {'startpage': len(d) - 1, 'prefix': 'Contratapa', 'style': ''}])
    d.set_metadata({'title': 'Análisis y Diseño de Sistemas — %s (edición comercial v1.0)' % P['nombre'],
                    'author': DATOS['titular'] or '', 'subject': '3.er Curso BTI · Plan Optativo · %s' % DATOS['anio'],
                    'keywords': 'análisis y diseño de sistemas; BTI; Plan Optativo; Paraguay', 'creator': '', 'producer': ''})
    ruta = os.path.join(SAL, base + '_DIGITAL.pdf')
    d.save(ruta, garbage=4, deflate=True, clean=True)
    return ruta


def copiar(origen, destino):
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    shutil.copy2(origen, destino)


def recursos(destino):
    for r in RECURSOS:
        shutil.copytree(os.path.join(ADS, r), os.path.join(destino, r), ignore=IGNORAR)
    open(os.path.join(destino, 'LEEME_RECURSOS.md'), 'w', encoding='utf8').write(
        '# Recursos digitales del proyecto — Análisis y Diseño de Sistemas, 3.º BTI (edición comercial v1.0)\n\n'
        'Las carpetas conservan la ruta que cita la guía docente (por ejemplo, `lote_4/proyecto/base_estudiante/`).\n\n'
        '| Carpeta | Contenido | Unidad |\n|---|---|---|\n'
        '| `lote_4/proyecto/base_estudiante/` | Base del proyecto que reciben los equipos | IV |\n'
        '| `lote_4/proyecto/referencia_docente/` | Referencia docente de la Unidad IV (reproduce la incidencia IN-02) | IV y V |\n'
        '| `lote_5/proyecto/` | Referencias docentes v2 y v2 con SC-02, cargador de datos de prueba y matriz | V |\n'
        '| `lote_5/caso/` | Datos de prueba ficticios y plantilla del conjunto reservado DR (sin datos) | V |\n'
        '| `lote_6/proyecto/` | Paquete de entrega modelo, paquete de Mbokaja (Práctica 17) y herramientas de revisión | VI |\n'
        '| `lote_6/caso/` | Fuentes del caso y plantilla de las variantes V6 (sin el banco reservado) | VI |\n'
        '| `lote_6/instrumentos/` | Planilla de tiempos del Encuentro 35 | VI |\n\n'
        '**No incluido, a propósito:** el conjunto reservado DR y el banco de variantes V6. Los genera cada docente con las '
        'plantillas y los guarda fuera de las carpetas del alumnado.\n\n'
        '**Requisitos:** PHP 8 con pdo_sqlite y un navegador; la institución los instala con sus licencias. Antes del Encuentro 19, '
        'hacer la prueba de campo E-1 a E-12 de la guía (Parte IV, sección 0.2): el entorno se probó en Linux, no en Windows.\n\n'
        '**Uso:** dentro de la institución adquirente, con fines educativos (ver «Condiciones de entrega y uso»). El código recibido '
        'de otros equipos se revisa primero con la inspección estática y se prueba solo en un equipo aislado.\n')


def cifras():
    C = {'anio': DATOS['anio'], 'titular': DATOS['titular'], 'isbn': DATOS['isbn'] or {}, 'paginas': {}, 'hojas': {}, 'lomo': {},
         'ref': {}, 'productos': {}}
    cub = json.load(open(os.path.join(CUB, 'cubiertas.json'), encoding='utf8'))
    for k in ORDEN:
        C['paginas'][k] = cub[k]['paginas_interior']; C['hojas'][k] = cub[k]['hojas']; C['lomo'][k] = cub[k]['lomo_mm']
        P = dict(CU.PRODUCTOS[k])
        P['destinatario'] = 'Estudiante' if k in ('libro', 'cuaderno') else 'Docente e institución'
        P['formatos'] = ('PDF de impresión (interior y cubierta), PDF digital' + (' y DOCX editable' if k in EDITABLE else ''))
        C['productos'][k] = P
    datos = json.load(open(os.path.join(AQUI, 'plan', 'datos_coleccion.json'), encoding='utf8'))
    C['ref'] = {k: v['pagina'] for k, v in datos['guia']['referencias'].items()}
    return C


def construir():
    if os.path.isdir(ENT):
        shutil.rmtree(ENT)            # la carpeta se regenera entera desde edicion_v1_0/salida
    C = cifras()
    dig = {k: digital(k) for k in ORDEN}
    est, doc, col, pre, qc = [os.path.join(ENT, x) for x in ('01_ESTUDIANTE', '02_DOCENTE', '03_COLECCION_COMPLETA',
                                                             '04_PRESENTACION_COMERCIAL', '05_CONTROL_DE_CALIDAD')]
    # 01 estudiante
    for k in ('libro', 'cuaderno'):
        copiar(dig[k], os.path.join(est, os.path.basename(dig[k])))
    TX.render('INSTRUCCIONES_ESTUDIANTE', 'Instrucciones para el estudiante', TX.instrucciones_estudiante(C), est)
    # 02 docente
    for k in ('guia', 'plan_anual', 'planes'):
        base = CU.PRODUCTOS[k]['archivo']
        copiar(dig[k], os.path.join(doc, os.path.basename(dig[k])))
        copiar(os.path.join(SAL, base + '.docx'), os.path.join(doc, base + '_EDITABLE.docx'))
    recursos(os.path.join(doc, 'RECURSOS_DIGITALES'))
    TX.render('INSTRUCCIONES_DOCENTE', 'Instrucciones para el docente', TX.instrucciones_docente(C), doc)
    # 03 colección completa: cada producto con sus archivos de impresión, digital y editable
    for k in ORDEN:
        base = CU.PRODUCTOS[k]['archivo']; dst = os.path.join(col, CARPETA[k])
        copiar(os.path.join(SAL, base + '.pdf'), os.path.join(dst, base + '_INTERIOR_IMPRESION.pdf'))
        copiar(os.path.join(CUB, base + '_CUBIERTA_IMPRESION.pdf'), os.path.join(dst, base + '_CUBIERTA_IMPRESION.pdf'))
        copiar(dig[k], os.path.join(dst, os.path.basename(dig[k])))
        copiar(os.path.join(SAL, base + '.docx'), os.path.join(dst, base + '_EDITABLE.docx'))
    copiar(os.path.join(est, 'INSTRUCCIONES_ESTUDIANTE.pdf'), os.path.join(col, 'INSTRUCCIONES_ESTUDIANTE.pdf'))
    copiar(os.path.join(doc, 'INSTRUCCIONES_DOCENTE.pdf'), os.path.join(col, 'INSTRUCCIONES_DOCENTE.pdf'))
    shutil.copytree(os.path.join(doc, 'RECURSOS_DIGITALES'), os.path.join(col, '06_RECURSOS_DIGITALES'))
    # 04 presentación comercial
    TX.render('DESCRIPCION_COMERCIAL_Y_FICHAS_TECNICAS', 'Descripción comercial y fichas técnicas', TX.fichas(C), pre)
    TX.render('PROPUESTA_DE_COMERCIALIZACION', 'Propuesta de comercialización', TX.propuesta(C), pre)
    TX.render('CONDICIONES_DE_ENTREGA_Y_USO', 'Condiciones de entrega y uso', TX.condiciones(C), pre)
    TX.render('LICENCIAS_Y_ATRIBUCIONES', 'Licencias y atribuciones', TX.licencias(C), pre)
    open(os.path.join(pre, 'TEXTO_WHATSAPP.txt'), 'w', encoding='utf8').write(TX.WHATSAPP)
    open(os.path.join(pre, 'TEXTO_REDES_SOCIALES.txt'), 'w', encoding='utf8').write(TX.REDES)
    pc = os.path.join(pre, 'PORTADAS_Y_CONTRAPORTADAS'); os.makedirs(pc, exist_ok=True)
    for f in sorted(os.listdir(CUB)):
        if f.endswith(('_TAPA.pdf', '_CONTRATAPA.pdf', '_TAPA.png')):
            copiar(os.path.join(CUB, f), os.path.join(pc, f))
    for k in ORDEN:   # vista previa de la contratapa
        base = CU.PRODUCTOS[k]['archivo']
        pymupdf.open(os.path.join(CUB, base + '_CONTRATAPA.pdf'))[0].get_pixmap(dpi=110).save(os.path.join(pc, base + '_CONTRATAPA.png'))
    # 05 control de calidad (los informes los completa auditoria_final.py)
    TX.render('DERECHOS_Y_REQUISITOS_LEGALES', 'Derechos y requisitos legales para la venta en Paraguay', TX.legal(C), qc)
    TX.render('INSTRUCCIONES_DE_IMPRESION', 'Instrucciones para la impresión', TX.impresion(C), qc)
    copiar(os.path.join(qc, 'DERECHOS_Y_REQUISITOS_LEGALES.pdf'), os.path.join(pre, 'DERECHOS_Y_REQUISITOS_LEGALES.pdf'))
    for dp, _, fs in os.walk(ENT):   # los DOCX de los textos de servicio solo son la fuente de sus PDF
        for f in fs:
            if f.endswith('.docx') and not f.endswith('_EDITABLE.docx'):
                os.remove(os.path.join(dp, f))
    json.dump(C, open(os.path.join(SAL, 'cifras_entrega.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    return C


if __name__ == '__main__':
    C = construir()
    n = sum(len(fs) for _, _, fs in os.walk(ENT))
    print('ENTREGA_COMERCIAL_FINAL: %d archivos' % n)
