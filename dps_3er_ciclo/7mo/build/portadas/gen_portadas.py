# -*- coding: utf-8 -*-
"""Portadas de Desarrollo Personal y Social (diseño común a 7.º, 8.º y 9.º; cambia el grado y el lema).
HTML + SVG de elaboración editorial (sin imágenes de terceros), rasterizado con Chromium (render.js) a PNG sin pérdida."""
import os, subprocess, sys
D = os.path.dirname(os.path.abspath(__file__)) + '/'
GRADO = sys.argv[1] if len(sys.argv) > 1 else '7.º'
LEMA = {'7.º': 'La escuela como una comunidad', '8.º': 'La escuela y su comunidad cercana', '9.º': 'La escuela como promotora del desarrollo comunitario'}[GRADO]
F = 'fonts/'
CSS = """
@font-face{font-family:'Merri';font-weight:700;src:url('%(f)su-4D0qyriQwlOrhSvowK_l5UcA6zuSYEqOzpPe3HOZJ5eX1WtLaQwmYiScCmDxhtNOKl8yDrOSAqEw.ttf');}
@font-face{font-family:'Mont';font-weight:400;src:url('%(f)sJTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCtr6Ew-.ttf');}
@font-face{font-family:'Mont';font-weight:600;src:url('%(f)sJTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCu170w-.ttf');}
@font-face{font-family:'Mont';font-weight:800;src:url('%(f)sJTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCvr70w-.ttf');}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:216mm;height:330mm}
body{background:#6A3E7A;color:#fff;font-family:'Mont',sans-serif;position:relative;overflow:hidden}
.top{position:absolute;top:0;left:0;right:0;height:19mm;background:#4E2C5B;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:11.5pt;letter-spacing:.6pt}
.bot{position:absolute;bottom:0;left:0;right:0;height:30mm;background:#4E2C5B;text-align:center;padding-top:8mm}
.bot .p{font-size:9.6pt;opacity:.9}
.bot .r{font-size:13pt;font-weight:800;margin-top:4mm}
.ser{font-family:'Merri';font-weight:700;text-align:center}
.pill{display:inline-block;background:#fff;color:#6A3E7A;font-weight:800;border-radius:9mm;padding:1.6mm 8mm;font-size:17pt}
.card{position:absolute;left:21mm;right:21mm;background:#fff;border-radius:6mm;color:#333;text-align:center}
.ltl{font-weight:800;color:#8E5BA6;font-size:11.5pt;letter-spacing:.4pt}
.h{font-weight:800;color:#6A3E7A}
.lin{width:62%%;height:1px;background:#E1D3EA;margin:5mm auto}
.lst{font-size:11.4pt;line-height:1.95;color:#444}
.comp{display:flex;gap:6mm;justify-content:center;margin-top:5mm}
.comp div{background:#F3ECF7;color:#6A3E7A;border-radius:4mm;padding:2.5mm 5mm;font-weight:800;font-size:10.5pt}
"""
def html(body):
    return '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>%s</body></html>' % (CSS % {'f': F}, body)

TOP = '<div class="top">EDUCACIÓN ESCOLAR BÁSICA &nbsp;·&nbsp; TERCER CICLO</div>'
BOT = '<div class="bot"><div class="p">Sigue el programa de estudio del Ministerio de Educación y Ciencias · Componente local</div><div class="r">República del Paraguay · 2026</div></div>'
TIT = '''<div style="position:absolute;top:34mm;left:0;right:0">
 <div class="ser" style="font-size:33pt;line-height:1.15">Desarrollo Personal<br>y Social</div>
 <div style="text-align:center;margin-top:5mm"><span class="pill">%s grado</span></div></div>''' % GRADO

# Ilustración: círculos de pertenencia (yo, mi grado, mi escuela, mi comunidad) con personas estilizadas y manos que se unen
def ilustracion():
    pers = ''
    import math
    colores = ['#F2C14E', '#7FC8A9', '#F49D8C', '#8EC5FC', '#FFFFFF', '#C9A7E0', '#F2C14E', '#7FC8A9', '#F49D8C', '#8EC5FC', '#C9A7E0', '#FFFFFF']
    for k in range(12):
        a = 2 * math.pi * k / 12 - math.pi / 2
        x, y = 300 + 205 * math.cos(a), 300 + 205 * math.sin(a)
        c = colores[k]
        pers += '<circle cx="%.1f" cy="%.1f" r="17" fill="%s"/><path d="M%.1f %.1f q24 -34 48 0 v14 h-48z" fill="%s"/>' % (x, y - 22, c, x - 24, y + 14, c)
    for k in range(6):
        a = 2 * math.pi * k / 6 - math.pi / 2 + 0.5
        x, y = 300 + 112 * math.cos(a), 300 + 112 * math.sin(a)
        c = colores[(k * 2 + 1) % 12]
        pers += '<circle cx="%.1f" cy="%.1f" r="14" fill="%s"/><path d="M%.1f %.1f q20 -28 40 0 v11 h-40z" fill="%s"/>' % (x, y - 18, c, x - 20, y + 12, c)
    return '''<svg viewBox="0 0 600 600" width="100%%" height="100%%">
 <circle cx="300" cy="300" r="290" fill="#7D4F8F"/>
 <circle cx="300" cy="300" r="250" fill="none" stroke="#B48CC8" stroke-width="3" stroke-dasharray="10 10"/>
 <circle cx="300" cy="300" r="160" fill="#8E5BA6"/>
 <circle cx="300" cy="300" r="62" fill="#F3ECF7"/>
 <text x="300" y="312" text-anchor="middle" font-family="Mont" font-weight="800" font-size="34" fill="#6A3E7A">Yo</text>
 %s
</svg>''' % pers

def libro():
    body = TOP + TIT + '''
<div style="position:absolute;top:96mm;left:38mm;width:140mm;height:140mm">%s</div>
<div style="position:absolute;top:243mm;left:0;right:0;text-align:center">
 <div style="font-weight:800;font-size:17pt">Libro del estudiante</div>
 <div class="comp"><div>Orientación Educacional y Vocacional</div><div>Proyecto Educativo Comunitario</div></div>
 <div style="font-size:11.4pt;opacity:.95;margin-top:4mm">Enfoque «Aprender Haciendo» &nbsp;·&nbsp; %s</div></div>''' % (ilustracion(), LEMA) + BOT
    return html(body)

def docente(titulo, lineas):
    body = TOP + TIT + '''
<div class="card" style="top:104mm;height:124mm;padding-top:14mm">
 <div class="ltl">MATERIAL EXCLUSIVO DEL DOCENTE</div>
 <div class="h" style="font-size:31pt;margin-top:6mm">%s</div>
 <div class="lin"></div>
 <div class="lst">%s</div></div>
<div style="position:absolute;top:240mm;left:0;right:0;text-align:center"><div class="comp"><div style="background:#fff">Orientación Educacional y Vocacional</div><div style="background:#fff">Proyecto Educativo Comunitario</div></div></div>''' % (titulo, '<br>'.join(lineas)) + BOT
    return html(body)

PIEZAS = {
 'portada_libro': libro(),
 'portada_plan_anual': docente('Plan anual', ['36 encuentros de 3 horas cátedra en dos etapas', '20 clases de Orientación y 7 talleres del proyecto', 'Capacidades, temas, indicadores de logro,', 'procedimientos e instrumentos de evaluación', 'Documento editable para adaptar a la institución']),
 'portada_planes': docente('Planes de clase', ['36 planes de 3 horas cátedra, editables', 'Inicio, desarrollo y cierre con tiempos', 'Recursos, procedimientos, instrumentos', 'y criterios de evaluación en cada plan', 'Incluye los 7 talleres del proyecto comunitario']),
 'portada_solucionario': docente('Solucionario docente', ['Respuestas esperadas y orientaciones de conducción', 'de las 20 clases y los 7 talleres del proyecto', 'Claves de las 7 evaluaciones de unidad y las 2 de etapa', 'Guía del Proyecto Educativo Comunitario, rúbricas', 'y listas de cotejo para valorar procesos y resultados']),
}
if __name__ == '__main__':
    for k, v in PIEZAS.items():
        open(D + k + '.html', 'w').write(v)
    subprocess.run(['node', D + 'render.js'] + list(PIEZAS), check=True, cwd=D)
    from PIL import Image
    for k in PIEZAS:
        Image.open(D + k + '.png').convert('RGB').save(D + k + '.png', optimize=True)
