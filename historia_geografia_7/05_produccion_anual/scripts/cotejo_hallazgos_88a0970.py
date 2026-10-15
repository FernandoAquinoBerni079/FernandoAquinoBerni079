# -*- coding: utf-8 -*-
"""Cotejo de los 18 hallazgos del dictamen de Work sobre 88a0970, contra los archivos anuales REGENERADOS.
Busca en el texto de los PDF (tomo, planes, solucionario) lo que cada corrección debe mostrar y lo que no debe quedar.
Uso: python3 scripts/cotejo_hallazgos_88a0970.py  →  cierre_88a0970/cotejo_hallazgos.json"""
import os, re, sys, json, importlib
import pymupdf

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
A = os.path.join(RAIZ, 'anual')


def texto(ruta):
    d = pymupdf.open(ruta)
    return [re.sub(r'\s+', ' ', p.get_text()) for p in d]


TOMO = texto(os.path.join(A, 'tomo', 'TOMO_ANUAL_oficio.pdf'))
PLAN = texto(os.path.join(A, 'planes', 'PLANES_ANUAL_A4.pdf'))
SOL = texto(os.path.join(A, 'solucionario', 'SOLUCIONARIO_ANUAL_A4.pdf'))
T, P, S = ' '.join(TOMO), ' '.join(PLAN), ' '.join(SOL)

res = {}
def chk(cod, desc, cond, paginas=None):
    res.setdefault(cod, []).append({'control': desc, 'resultado': 'correcto' if cond else 'FALLA', 'paginas': paginas or []})
    print(('CORRECTO ' if cond else 'FALLA    ') + '[%s] %s%s' % (cod, desc, ' (págs. %s)' % paginas if paginas else ''))

def pags(lista, patron):
    return [i + 1 for i, t in enumerate(lista) if re.search(patron, t)]

# BI-01
src = open(os.path.join(AQUI, 'figuras', 'bloque1.py'), encoding='utf8').read()
chk('BI-01', 'La Ficha B-1 usa el mapa con el nordeste de Asia y el control de encuadre de los cinco sitios',
    "mapa_mudo_poblamiento(geo, p(reg('ficha_B_mapa_mudo_america.png'" in src and "'Beringia': (-168.0, 66.0)" in src and "'Monte Verde': (-73.2, -41.5)" in src)
chk('BI-01', 'Epígrafe de la Ficha B-1 en el tomo', bool(pags(TOMO, 'nordeste de Asia para la consigna 1')), pags(TOMO, 'nordeste de Asia para la consigna 1'))
chk('BI-01', 'Plan 8: la Ficha B-1 sigue esencial con 30 minutos (20–50)', bool(re.search(r'20–50 Entrega la Ficha B-1', P)))
chk('BI-01', 'Consigna 1 y clave piden y ubican Beringia y Monte Verde',
    'marcá Beringia y Monte Verde' in T and 'Beringia entre Siberia y Alaska; Monte Verde en el sur de Chile' in S)
# BI-02
chk('BI-02', 'Clave: el 0 es origen de la escala, no año del calendario', 'no existió año 0 del calendario' in S and 'la línea empieza en el año 0' not in S)
chk('BI-02', 'Figura 5.2 y Ficha B-2 declaran el 0 como origen gráfico (texto en el código de las figuras)',
    'el 0 es origen gráfico, no año histórico' in src and 'El 0 es origen de la escala, no un año del calendario' in src)
# BI-03
chk('BI-03', 'White Sands: corroboración de 2023 en tomo y clave, sin «en discusión»',
    '2023' in T and 'polen' in T and 'corroborada en 2023' in S and 'en discusión' not in T + S, pags(TOMO, 'White Sands'))
chk('BI-03', 'Ítem 10 U1/Clase 4: no se afirma unanimidad', 'no equivale a unanimidad' in S)
# BI-04
chk('BI-04', 'U2 ítem 13: Monte Verde prueba presencia temprana; origen africano de la especie',
    'anterior a la cultura Clovis' in S and 'se originó en África' in S and 'Ameghino se equivocaba' not in S)
# BII-01
chk('BII-01', 'Integradora 1, ítem 15: ejemplo de resistencia dentro del período (1542-1543), sin Oberá 1579',
    'levantamientos de Aracaré y Tabaré entre 1542 y 1543' in S and 'rebelión de Oberá en 1579.»' not in S, pags(SOL, 'Aracaré y Tabaré entre 1542'))
# BII-02 y BII-03 (resueltos: no revertir)
chk('BII-02', 'Real Provisión: el segundo fragmento sigue declarado como adaptación escolar', bool(re.search(r'[Aa]daptaci[oó]n', ' '.join(TOMO[i - 1] for i in pags(TOMO, 'Real Provisión')))))
chk('BII-03', 'Tabaré sigue en 1543 dentro del ciclo 1542-1543', '1542' in T and '1543' in T and 'Tabaré' in T)
# BII-04
chk('BII-04', 'Integradora 1, ítem 14: gobernador y Cabildo distintos de los encomenderos', 'gobernador y Cabildo ejercían el gobierno colonial' in S)
# COM-01
for n, pts in ((18, 13), (30, 11), (35, 9), (36, 16)):
    chk('COM-01', 'Encuentro %d: el solucionario declara %d puntos compartidos' % (n, pts), ('Puntaje compartido: %d de los' % pts) in S)
chk('COM-01', 'Planes: no se promete «el peso de cada una»', 'muestra el peso de cada una' not in P)
# COM-02
chk('COM-02', 'Solucionario: sección «Referencias para el docente» con uso y estado de cada fuente',
    'Referencias para el docente' in S and 'Edición por cotejar' in S and 'Ley 6676/2020' in S, pags(SOL, 'Referencias para el docente'))
# COM-03 (menor; ver informe)
chk('COM-03', 'Matriz curricular: columna «Capacidades» ensanchada',
    "anchos = [0.9, 2.0, 4.4, 1.5, 2.5, 1.9, 2.4, 1.6, 9.9]" in open(os.path.join(AQUI, 'anuales.py'), encoding='utf8').read())
# BIII-01
chk('BIII-01', 'Tabla y clave: río Negro u Otuquis con Bolivia (38 km)', 'río Negro u Otuquis (con Bolivia, aprox. 38 km)' in T and 'Negro u Otuquis con Bolivia' in S,
    pags(TOMO, 'Negro u Otuquis'))
chk('BIII-01', 'Mapa: marca de confluencia aproximada y fuente MRE (sin trazar el cauce)',
    'Confluencia Negro/Otuquis (aprox.)' in open(os.path.join(AQUI, 'figuras', 'bloque3.py'), encoding='utf8').read())
chk('BIII-01', 'No se atribuye el Pilcomayo como límite con Bolivia', not re.search(r'Pilcomayo[^.,;]{0,30}(con|y) Bolivia', T + S))  # «entre los ríos Verde y Pilcomayo, y el tratado… con Bolivia» (Laudo Hayes) no es atribución de límite
# BIII-02
chk('BIII-02', 'Clase 11/12 y clave: sin la cadena universal por Santa Fe y Buenos Aires',
    'todo lo que el Paraguay vendía' not in T and 'Santa Fe y Buenos Aires → Potosí' not in P and 'pasaba por Asunción, Santa Fe y Buenos Aires hasta Potosí' not in S
    and 'redistribuía' in T)
chk('BIII-02', 'Esquema de la yerba: ramificación desde Santa Fe', "'Córdoba → Alto Perú (Potosí)'" in open(os.path.join(AQUI, 'figuras', 'bloque3.py'), encoding='utf8').read())
# BIII-03
chk('BIII-03', 'São Paulo en el planalto interior', 'planalto interior' in S and 'São Paulo en la costa atlántica' not in S)
# BIII-04
chk('BIII-04', 'Jamaica 1655: colonia española conquistada por Inglaterra', 'Jamaica, tomada por Inglaterra en 1655' in T)
# BIII-05
chk('BIII-05', 'Planes 20 y 27: variante 20 + 100 minutos con lo que pasa a casa', P.count('Variante si la devolución de la Evaluación') == 2)
# BIV-01
chk('BIV-01', 'Sin el mínimo de 400 mm ni la diferencia de 1.400 mm en tomo, planes y clave',
    not re.search(r'unos 400\b|400 mm|1\.400 mm|1\.600 mm', T + P + S))
chk('BIV-01', 'Diferencia de 1.200 mm en la clave y serie 1971-2000 declarada', 'Unos 1.200 mm' in S and bool(re.search(r'1971- ?2000', T)) and bool(re.search(r'1971- ?2000', P)))  # el PDF puede cortar «1971-»/«2000» en dos líneas
chk('BIV-01', 'Figura 19.3: fuente MADES y normales 1971-2000 (código de la figura)',
    'medias anuales para el período 1971-2000' in open(os.path.join(AQUI, 'figuras', 'bloque4.py'), encoding='utf8').read())
# AN-01
chk('AN-01', 'Mapa clave U3: franja inferior para la escala y espacio de leyenda (revisión visual en el informe)',
    'franja inferior libre para la escala' in open(os.path.join(AQUI, 'figuras', 'bloque2.py'), encoding='utf8').read())

# Puntajes de las ocho evaluaciones
tot = {}
for n in (5, 9, 17, 18, 25, 30, 35, 36):
    m = importlib.import_module('contenido.e%02d' % n)
    tot[n] = m.SOL.get('puntaje') if isinstance(m.SOL, dict) else None
chk('PUNTAJES', 'Totales de las ocho evaluaciones: %s' % tot, sorted(tot.values()) == sorted([23, 22, 25, 28, 25, 28, 25, 28]))

total = sum(len(v) for v in res.values()); mal = sum(1 for v in res.values() for x in v if x['resultado'] != 'correcto')
print('\nResultado: %d correctos, %d fallos' % (total - mal, mal))
os.makedirs(os.path.join(RAIZ, 'cierre_88a0970'), exist_ok=True)
json.dump({'correctos': total - mal, 'fallos': mal, 'controles': res}, open(os.path.join(RAIZ, 'cierre_88a0970', 'cotejo_hallazgos.json'), 'w', encoding='utf8'),
          ensure_ascii=False, indent=1)
sys.exit(1 if mal else 0)
