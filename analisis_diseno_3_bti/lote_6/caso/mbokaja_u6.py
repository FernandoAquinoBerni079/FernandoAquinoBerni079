# -*- coding: utf-8 -*-
"""Caso de transferencia de la Unidad VI — Escuela Básica Mbokaja (institución y personas ficticias).

Amplía, sin modificarlas, las fuentes de Mbokaja de los lotes 1 a 5 con los datos de la Práctica 17: un voluntario
preparó un paquete del sistema para la computadora donada (M-F7, sin internet), que el profesor del colegio vecino
instalará en su visita mensual (M-F9). El paquete tiene cinco defectos introducidos a propósito. v1.1 (auditoría del
lote 6): los detectan las herramientas del docente, que viven fuera del paquete: la inspección estática
(proyecto/herramientas/inspeccionar_entrega.php, bloques A a F, sin ejecutar nada) y las pruebas en aislamiento
(proyecto/herramientas/probar_en_aislamiento.php, lista cerrada, copia descartable). DEFECTOS es la clave: qué se
cambió, qué incoherencia produce, qué herramienta la informa y cómo se corrige. build/armar_paquetes.py los aplica sobre
una copia del paquete modelo; build/reproducir.py comprueba que las herramientas encuentren exactamente esas
incoherencias y que, corregidas, el paquete se instale siguiendo su guía.
Códigos nuevos: M-F13, MS-9, MS-10 y DM-1 a DM-5. Ninguno repite un código anterior."""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
ADS = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(ADS, 'lote_5', 'caso'))
import mbokaja_u5 as MB5

DATOS_TITULO = 'Datos nuevos de Mbokaja (caso de práctica, ficticio)'
DATOS = [
    ('M-F13', 'Un ex alumno voluntario preparó un paquete del sistema de préstamos para la computadora donada. Lo deja en '
              'un pendrive: el profesor del colegio vecino lo instalará en su próxima visita.'),
]
SITUACIONES_TITULO = 'Situaciones nuevas (caso de práctica, ficticio)'
SITUACIONES = [
    ('MS-9', 'El voluntario agregó a la pantalla un logo de la escuela que encontró en internet. No anotó de dónde lo sacó.'),
    ('MS-10', 'Mientras armaba el paquete, el voluntario actualizó el informe mensual con el mensaje de mes vacío, pero no '
              'actualizó todas las pruebas ni el manual.'),
]
VERSION = 'Entrega 0.9 (preparada por el voluntario para Mbokaja)'
TITULO_LEEME = 'Sistema de préstamos — PAQUETE PARA LA BIBLIOTECA DE MBOKAJA (preparado por un voluntario, ficticio)'

# (código, qué se cambió en el paquete, archivo, incoherencias que se tienen que informar, corrección, herramienta)
INSPECCION, AISLAMIENTO = 'inspección estática', 'pruebas en aislamiento'
DEFECTOS = [
    ('DM-1', 'La guía nombra un comando que no existe', 'ENTREGA/INSTALAR.md',
     ['[A] la guía usa «php instalar_base.php», pero no existe instalar_base.php en el paquete'],
     'Cambiar el comando del paso 2 por php instalar.php, el archivo que trae el paquete.', INSPECCION),
    ('DM-2', 'La lista de entrega incluye datos de prueba que no están', 'ENTREGA/LISTA_ENTREGA.md',
     ['[B] la lista de entrega incluye datos/mbokaja_prueba.json, que no está en el paquete'],
     'Quitar esa línea: el paquete usa los datos ficticios de src/datos_ejemplo.php. Si se quieren datos de Mbokaja, '
     'hay que agregarlos y probarlos antes de entregar.', INSPECCION),
    ('DM-3', 'Una prueba espera el comportamiento viejo del informe de un mes vacío (MS-10)', 'pruebas/prueba_contratos.php',
     ['[C] la prueba pruebas/prueba_contratos.php no terminó bien'],
     'Actualizar la prueba al comportamiento actual (ME-14 para el mes vacío): el código está bien y la prueba quedó vieja.',
     AISLAMIENTO),
    ('DM-4', 'Una imagen sin procedencia (MS-9)', 'public/logo_mbokaja.png',
     ['[D] public/logo_mbokaja.png no tiene su fila en la ficha de procedencia'],
     'Quitar la imagen: lo que no tiene licencia conocida no se incluye. Si la escuela tiene un logo propio, se agrega '
     'con su autor y su permiso en la ficha.', INSPECCION),
    ('DM-5', 'El manual describe una pantalla y un mensaje que el sistema no tiene', 'ENTREGA/MANUAL.md',
     ['[E] el manual nombra el mensaje ME-15, que el sistema no tiene',
      '[E] el manual describe public/reservas.php, que no está en el paquete'],
     'Quitar la tarea «Reservar un libro»: el sistema no tiene reservas. Si se quiere, es una solicitud de cambio.',
     INSPECCION),
]
TAREA_FALSA = ('T-09', 'Reservar un libro', 'Bibliotecaria', 'public/reservas.php',
               ['Escribí el código del lector y el del libro.', 'Apretá «Reservar».'],
               [('ME-15', 'La reserva quedó registrada.')])
PRUEBA_VIEJA = ("comprobar('SC-02: mes sin préstamos → correcto, ME-14, sin filas y total 0', $v['ok'] && $v['codigo'] === "
                "'ME-14' && $v['filas'] === array() && $v['total'] === 0);",
                "comprobar('Informe de un mes sin préstamos → correcto, sin mensaje, sin filas y total 0', $v['ok'] && "
                "$v['codigo'] === null && $v['filas'] === array() && $v['total'] === 0);")


def incoherencias_esperadas(herramienta=None):
    return sorted(i for d in DEFECTOS if herramienta in (None, d[5]) for i in d[3])


FUENTES = dict(DATOS + SITUACIONES)
FUENTES.update(MB5.FUENTES)
