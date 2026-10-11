# -*- coding: utf-8 -*-
"""Datos de los 36 Planes de Clase: parte de la versión original (planes_orig.json) y la sincroniza con el libro
unificado: material, tema, capacidad MEC e indicadores (iguales al Plan Anual), referencias a figuras renumeradas,
puntos de control vigentes de cada práctica y momentos propios para las 12 fichas de continuidad."""
import json, re
from build_libro import leer, titulo_de, FICHA_TRAS, B

PL0 = json.load(open(B + 'planes_orig.json'))

# Momentos propios de las fichas de continuidad (15 / 50 / 15 min)
FICHAS = {
 'A': (['Recuperación de la Clase 1 con una pregunta: «¿qué tres medidas hay que mirar antes de comprar un gabinete?».', 'Presentación del producto de la Ficha A (matriz de compatibilidad) y de su punto de control.'],
       ['Lectura guiada de «Lo que necesitás saber» y del modelo de matriz.', 'Armado de la matriz en Excel con el caso de la ficha y búsqueda del dato que respalda cada decisión en las fichas técnicas provistas.', 'Revisión docente por parejas: ninguna decisión sin evidencia.'],
       ['Puesta en común de una incompatibilidad detectada y del cambio mínimo que la resuelve.', 'Desafío opcional para quienes terminan antes.']),
 'B': (['Recuperación de la Clase 4: diferencia entre largo de ranura y carriles eléctricos.', 'Presentación del producto de la Ficha B y de su punto de control.'],
       ['Lectura de la ficha de placa provista y separación de «forma física» e «interfaz» en columnas.', 'Completamiento de los tres casos (PCIe x1, x16 y SSD M.2) citando la especificación en cada fila.', 'El docente corrige inferencias hechas por fotografía y pide el dato del manual.'],
       ['Puesta en común: por qué un M.2 que entra puede no funcionar.', 'Desafío opcional.']),
 'C': (['Recuperación de la Clase 5 con un cable USB-C sin rótulo: «¿qué podemos asegurar de él?».', 'Presentación de la ficha de puerto y de su punto de control.'],
       ['Relevamiento de un equipo o una ficha técnica con USB-C y completamiento de los campos confirmados.', 'Comparación con un puerto USB-A del mismo equipo.', 'Redacción de la conclusión de tres líneas sobre lo que no puede asegurarse mirando el conector.'],
       ['Lectura de dos conclusiones y corrección grupal de afirmaciones sin evidencia.', 'Desafío opcional: advertencia para un cliente.']),
 'D': (['Recuperación de las Clases 6 y 7: zócalo, chipset, tipo de memoria y ranuras.', 'Presentación del checklist de la Ficha D y de su punto de control.'],
       ['Trabajo con el equipo ficticio y la ficha del fabricante: completamiento del checklist con SÍ/NO y evidencia.', 'Redacción de la propuesta de ampliación de memoria con la cantidad de módulos justificada.', 'El docente verifica que nadie deduzca el tipo de memoria solo por la frecuencia.'],
       ['Puesta en común de dos propuestas y comparación 1 × 16 GB frente a 2 × 8 GB.', 'Desafío opcional.']),
 'E': (['Recuperación de la Clase 8: capacidad real, salud del disco y respaldo.', 'Presentación del plan de migración y de su punto de control.'],
       ['Cálculo de la capacidad mínima del destino con el margen libre pedido.', 'Elección entre SSD SATA y M.2 NVMe según la compatibilidad dada.', 'Redacción de los siete pasos de migración con la verificación de archivos.'],
       ['Revisión cruzada de los planes: ¿hay respaldo y verificación antes de retirar el disco anterior?', 'Desafío opcional.']),
 'F': (['Recuperación de la Clase 10: costo por página y costo total.', 'Presentación de la tabla de la Ficha F y de su punto de control.'],
       ['Carga de las dos impresoras con los datos del docente y cálculo del costo por página con fórmula.', 'Cálculo del consumo de 12 meses y del costo total del primer año.', 'Redacción de la recomendación de cuatro líneas basada en el volumen de uso.'],
       ['Puesta en común: ¿en qué volumen cambia la recomendación?', 'Desafío opcional: impresoras térmicas.']),
 'G': (['Recuperación de la Clase 12: función de la IP, la máscara, la puerta de enlace y el DNS.', 'Presentación de la secuencia de diagnóstico y de su punto de control.'],
       ['Ejecución de ipconfig /all y registro de los datos en la tabla.', 'Pruebas de ping autorizadas por el docente, en el orden de la secuencia, con el resultado y el diagnóstico probable de cada paso.', 'Se recuerda que no se modifica la configuración de la red escolar.'],
       ['Puesta en común: distinguir falla local, de salida y de nombres.', 'Desafío opcional.']),
 'H': (['Recuperación de la Clase 14: punto único de falla y topología física y lógica.', 'Presentación del diagrama de la Ficha H y de su punto de control.'],
       ['Dibujo de la red en PowerPoint con conectores anclados y marcado de los puntos únicos de falla.', 'Simulación de tres fallas (cable de una PC, switch, enlace al router) y registro de los servicios que se pierden.'],
       ['Puesta en común de una mejora de redundancia realista para una institución.', 'Desafío opcional.']),
 'I': (['Recuperación de las Clases 15 y 16: dimensionamiento del switch y lista de materiales.', 'Presentación de la lista de materiales de la Ficha I y de su punto de control.'],
       ['Cálculo de los puertos ocupados del caso con la reserva del 20 %.', 'Elección del switch y completamiento de los materiales pasivos.', 'Verificación de que cada punto del plano tenga su material.'],
       ['Puesta en común: un switch mayor o dos switches para 20 puestos.', 'Desafío opcional.']),
 'J': (['Recuperación de las Clases 17 y 19: categorías de cable y esquemas T568.', 'Presentación de la ficha de especificación y de su punto de control.'],
       ['Comparación de los dos casos (1 Gb/s en el aula y 10 Gb/s a 90 m) y elección de categoría.', 'Documentación del esquema de terminación adoptado.', 'Listado de lo que mide un certificador además de la continuidad.'],
       ['Puesta en común: el orden de colores no certifica el enlace.', 'Desafío opcional.']),
 'K': (['Recuperación de la Clase 18: bandas, canales y seguridad del Wi-Fi.', 'Presentación del relevamiento de la Ficha K y de su punto de control.'],
       ['Relevamiento de redes visibles (o datos simulados del docente) sin registrar contraseñas.', 'Comparación de 2,4 y 5 GHz sin suponer que una siempre es más rápida.', 'Redacción de la recomendación de ubicación y seguridad del access point.'],
       ['Puesta en común: qué información falta para recomendar 6 GHz en Paraguay.', 'Desafío opcional.']),
 'L': (['Recuperación de la Clase 20: CONATEL, homologación y abstracción, análisis y síntesis.', 'Presentación de la ficha de evidencia, del resumen ejecutivo y de su punto de control.'],
       ['Consulta del sitio oficial de CONATEL (o de las capturas provistas) y registro de cada afirmación con fuente y fechas.', 'Integración de la ficha al informe final como anexo.', 'Redacción del resumen ejecutivo de una página: necesidad, solución, verificaciones, costo y riesgos.'],
       ['Lectura de dos resúmenes ejecutivos: ¿un directivo puede decidir sin leer los anexos?', 'Desafío opcional.']),
}


def control(nombre):
    """Último punto de control de una práctica o ficha del libro."""
    L = leer(nombre)
    c = [l.split(':', 1)[1].strip() for l in L if l.startswith('Punto de control:')]
    return c[-1]


def figuras(t):
    # Numeración vieja de las figuras de clase (Figura N.k) → nueva (la fotografía es N.1; las figuras pasan a N.(k+1))
    def f(m):
        n, k = int(m.group(2)), int(m.group(3))
        return 'Figura %d.%d' % (n, k + 1)
    t = re.sub(r'(figura|Figura) (\d+)\.(\d+)', f, t)
    t = re.sub(r'figuras (\d+)\.(\d+) y (\d+)\.(\d+)', lambda m: 'Figuras %s.%d y %s.%d' % (m.group(1), int(m.group(2)) + 1, m.group(3), int(m.group(4)) + 1), t)
    return t


def limpiar(t):
    t = figuras(t)
    t = t.replace('Tomo del estudiante, ', 'Libro del estudiante, ').replace('Tomo del estudiante', 'Libro del estudiante')
    t = re.sub(r' · Cuaderno de Laboratorio, (Práctica \d+|Ficha [A-L])', r', \1', t)
    t = t.replace('Cuaderno de Laboratorio, ', 'Libro del estudiante, ').replace('del Cuaderno', 'del libro')
    t = t.replace('tomo del estudiante', 'libro del estudiante').replace('del tomo', 'del libro').replace('el tomo', 'el libro')
    return re.sub(r'\s+', ' ', t).strip()


ARREGLOS = {
 5: [('cálculo en Excel de la velocidad teórica de cada ranura PCIe 4.0, con gráfico comparativo', 'cálculo en Excel de la velocidad teórica de enlaces PCIe 3.0 y 5.0 con distinto número de carriles, con gráfico comparativo')],
 23: [('Resolución de la Práctica 14: estrella del aula con switch central, diez PC, impresora, access point y router, y señalamiento del punto único de falla.',
       'Resolución de la Práctica 14: estrella de la Farmacia Tajy con switch central, seis computadoras, impresora, access point y router, y señalamiento del punto único de falla.')],
 32: [('armado de la planilla de canales del aula con formato condicional', 'armado de la planilla de canales de la Farmacia Tajy con las dos condiciones de la norma y formato condicional')],
}


def planes(pa_rows):
    out = []
    for p0, r in zip(PL0, pa_rows):
        assert p0['idx'] == r['n']
        p = dict(idx=r['n'], unidad=p0['unidad'].replace('Redes de Computadoras', 'Redes de computadoras'))
        caps = [x[len('Capacidad MEC: «'):-1] for x in r['tema'] if x.startswith('Capacidad MEC: «')]
        p['capacidad'] = caps if caps else ['Capacidades de la Unidad %d (ver el Plan Anual, secuencias %s).' % (r['unidad'], '1 a 17' if r['unidad'] == 1 else '19 a 35')]
        p['indicadores'] = r['indicadores']
        p['tema'] = r['tema'][0]
        p['proc'], p['inst'] = r['proc'], r['inst']
        p['tiempos'] = p0['tiempos']
        p['criterios'] = [limpiar(x) for x in p0['criterios']]
        mom = {k: [limpiar(x) for x in v] for k, v in p0['momentos'].items()}
        for a, b in ARREGLOS.get(p['idx'], []):
            hit = False
            for k in mom:
                for i, x in enumerate(mom[k]):
                    if a in x:
                        mom[k][i] = x.replace(a, b); hit = True
            assert hit, (p['idx'], a)
        if r['tipo'] == 'C':
            n = int(re.match(r'Clase (\d+)', p['tema']).group(1))
            p['titulo'] = titulo_de(leer('tomo_clase%02d' % n)).split(' — ', 1)[1]
            p['material'] = 'Libro del estudiante · Clase %d y Práctica %d' % (n, n)
            cp = control('lab_practica%02d' % n)
            for i, x in enumerate(mom['Cierre']):
                if 'punto de control' in x:
                    mom['Cierre'][i] = re.sub(r'(punto de control)( de la práctica)?:? .*$', r'\1: «%s»' % cp.replace('\\', '\\\\'), x)
            p['recursos'] = limpiar(p0['recursos'])
        elif r['tipo'] == 'F':
            k = re.match(r'Ficha ([A-L])', p['tema']).group(1)
            p['titulo'] = titulo_de(leer('lab_ficha_' + k))
            p['material'] = 'Libro del estudiante · Ficha %s' % k
            ini, des, cie = FICHAS[k]
            mom = {'Inicio': ini, 'Desarrollo': des, 'Cierre': ['Comprobación del punto de control: «%s»' % control('lab_ficha_' + k)] + cie}
            p['recursos'] = 'Libro del estudiante, Ficha %s y clase de referencia · fichas técnicas y datos del caso provistos por el docente · Windows y Microsoft Office según corresponda. Si el laboratorio no está disponible, la ficha se resuelve en papel con un dossier impreso preparado por el docente.' % k
        else:
            p['titulo'] = p['tema']
            p['material'] = 'Libro del estudiante · %s' % p['tema'].split(' (')[0].split(' — ')[0]
            p['recursos'] = limpiar(p0['recursos'])
        p['momentos'] = mom
        out.append(p)
    return out
