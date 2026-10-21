# -*- coding: utf-8 -*-
"""Manifiesto SHA-256 de planificacion/ (salvo el propio manifiesto y evidencias/salida_manifiesto_plan.txt) y huella de
las fuentes que leyó: los seis documentos de la colección v0.2 y su manifiesto.
Uso: python3 -B planificacion/build/manifiesto_plan.py  →  planificacion/MANIFIESTO_PLANIFICACION.json"""
import datetime, hashlib, json, os
AQUI = os.path.dirname(os.path.abspath(__file__)); PLAN = os.path.dirname(AQUI); ADS = os.path.dirname(PLAN)
SALIDA = os.path.join(PLAN, 'MANIFIESTO_PLANIFICACION.json')
EXCLUIR = {SALIDA, os.path.join(PLAN, 'evidencias', 'salida_manifiesto_plan.txt')}


def entrada(raiz, ruta):
    datos = open(os.path.join(raiz, ruta), 'rb').read()
    return {'ruta': ruta, 'bytes': len(datos), 'sha256': hashlib.sha256(datos).hexdigest()}


archivos = []
for d, carpetas, fs in os.walk(PLAN):
    carpetas[:] = sorted(c for c in carpetas if c != '__pycache__')
    for f in sorted(fs):
        r = os.path.join(d, f)
        if r not in EXCLUIR:
            archivos.append(entrada(PLAN, os.path.relpath(r, PLAN)))
fuentes = [entrada(ADS, 'coleccion/' + n + e) for n in ('ADS_3BTI_LIBRO_ANUAL_ESTUDIANTE_OFICIO_O3', 'ADS_3BTI_GUIA_DOCENTE_ANUAL_OFICIO_O3',
                                                      'ADS_3BTI_CUADERNO_ANUAL_PRACTICAS_OFICIO_O3') for e in ('.docx', '.pdf')]
fuentes.append(entrada(ADS, 'coleccion/MANIFIESTO_COLECCION.json'))
co = json.load(open(os.path.join(PLAN, 'CONTROLES_PLANIFICACION.json'), encoding='utf8'))
json.dump({'planificacion': 'ADS 3.º BTI — plan anual y 36 planes de clase, versión 0.1 para revisión',
           'fecha': datetime.date.today().isoformat(),
           'base': 'colección v0.2, commit 88c5cb5 (aprobada como base editorial estable para la planificación)',
           'estado': 'Para revisión. No definitiva hasta confirmar el encuadre institucional y la carga horaria. Sin validación '
                     'en aulas ni en Windows; no autorizada para la venta.',
           'controles': {'total': co['total'], 'fallos': len(co['fallos']), 'no_ejecutados': co['no_ejecutados']},
           'fuentes_leidas': fuentes, 'archivos': archivos},
          open(SALIDA, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('%d archivos de planificacion/ y %d fuentes' % (len(archivos), len(fuentes)))
