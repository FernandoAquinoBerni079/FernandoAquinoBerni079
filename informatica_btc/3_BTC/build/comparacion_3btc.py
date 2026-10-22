# -*- coding: utf-8 -*-
"""PDF de aprobación de 3.º BTC: las 20 figuras, R1 → R3, con decisión y motivo.
Uso: python3 comparacion_3btc.py <carpeta Antes_R1 de las figuras de 3.º>"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(os.path.dirname(BASE), 'build_comun'))
import comparacion as C

ANT = sys.argv[1]; FIG = os.path.join(BASE, 'figuras_R3')
F = [
    (1, 'Módulos del sistema', 'Clase 1 · Práctica 1', 'Propuesta incorporada sin cambios.', 'Mismo modelo de cuatro módulos y base compartida; aclara que los nombres varían según el programa.'),
    (2, 'Alta de la empresa', 'Clase 2 · Práctica 2', 'Propuesta incorporada; en R3, la nota «Esquema de laboratorio…» sale de la imagen y pasa al pie de figura.', 'La nota medía 6 pt impresa. Datos iguales a la ficha del caso.'),
    (3, 'Usuarios y permisos', 'Clase 3 · Práctica 3', 'Propuesta incorporada sin cambios.', 'Coincide celda por celda con la tabla de permisos de la clase.'),
    (4, 'Niveles del plan de cuentas', 'Clase 4 · Práctica 4', 'Propuesta incorporada sin cambios.', 'El conector une 1.1 y 1.2 al Activo; códigos iguales al plan.'),
    (5, 'Del comprobante al asiento', 'Clase 5 · Práctica 5', 'Propuesta incorporada sin cambios.', 'Distingue el control aritmético del control de contenido.'),
    (6, 'Documento electrónico', 'Clase 5', 'Propuesta incorporada sin cambios; pie actualizado.', 'Distingue DE, DTE y KuDE, y la entrega según el receptor.'),
    (7, 'Saldos iniciales', 'Clase 6 · Práctica 6', 'Propuesta incorporada sin cambios.', '8 + 22 + 25 + 9 = 64 millones contra Capital.'),
    (8, 'Diez asientos', 'Clase 7 · Práctica 7', 'Propuesta incorporada: las barras pasan a tabla.', 'La tabla trae los diez totales exactos (143.899.700); las barras R1 redondeaban.'),
    (9, 'Mayor de Caja', 'Clase 8 · Práctica 8', 'Propuesta incorporada sin cambios.', 'Movimientos, sumas y saldo idénticos al CSV.'),
    (10, 'Balance de comprobación', 'Clase 9 · Práctica 9', 'Propuesta incorporada sin cambios.', 'Dos igualdades con los importes del caso.'),
    (11, 'Estado de Resultados', 'Clase 10', 'Propuesta incorporada: la cascada pasa a operaciones.', 'Operaciones exactas, más fáciles de leer que la cascada.'),
    (12, 'Balance General', 'Clase 10 · Práctica 10', 'Propuesta incorporada sin cambios.', '75.441.300 = 8.941.300 + 66.500.000, por cuenta.'),
    (13, 'Píxeles y tamaño de impresión', 'Clase 11 · Práctica 11', 'Propuesta incorporada sin cambios.', '8.640.000 bytes ≈ 8,24 MiB; 20,32 cm a 300 ppi.'),
    (14, 'Capas', 'Clase 13 · Práctica 13', 'Propuesta incorporada sin cambios.', 'Mismas cuatro capas que la tabla de la clase.'),
    (15, 'Retoque', 'Clase 14 · Práctica 14', 'Propuesta incorporada (efecto ilustrativo).', 'Íconos de proceso; respeta el límite ético de la clase.'),
    (16, 'Filtros', 'Clase 15 · Práctica 15', 'Propuesta incorporada (efectos ilustrativos); pie corregido.', 'Son esquemas, no resultados reales de un filtro, y así se rotulan.'),
    (17, 'Salidas del pack', 'Clase 17 · Práctica 17', 'Propuesta corregida: ícono genérico de celular en lugar del logotipo de una red social.', 'Evitar marcas comerciales; medidas iguales a la tabla de la clase.'),
    (18, 'Anatomía de una página web', 'Clase 18 · Práctica 18', 'Propuesta corregida: globo genérico y «Pedí por mensaje» en lugar del logotipo de mensajería.', 'Evitar marcas comerciales; la figura dice «esquema, no sitio publicado».'),
    (19, 'Mapa del sitio', 'Clase 19 · Práctica 19', 'Propuesta incorporada; en R3, «Mensajería» en lugar de «WhatsApp» y nota «Esquema didáctico…» más grande.', 'Evitar el nombre de una aplicación comercial (el tomo dice «ícono de mensajería»); la nota medía 6,4 pt.'),
    (20, 'Ciclo de una promoción digital', 'Clase 20 · Práctica 20', 'Reconstruida en vector con los datos del caso.', 'La propuesta tenía errores de render («San Ḃlas», «maestro ercapas») y logotipos comerciales.'),
]
paginas = [dict(codigo='Figura %d' % n, titulo='%s (%s)' % (t, u), antes=os.path.join(ANT, 'Figura_%02d.png' % n),
                despues=os.path.join(FIG, 'R3_Figura_%02d.png' % n), rot_antes='R1', rot_despues='R3 (propuesta para aprobar)',
                cambio=c, motivo=m) for n, t, u, c, m in F]
salida = os.path.join(BASE, 'COMPARACION_PARA_APROBACION_3BTC.pdf')
print(C.armar(paginas, salida, 'Informática 3.º BTC · Comparación para aprobación · R1 → R3 · 22 de octubre de 2026'), 'páginas →', salida)
