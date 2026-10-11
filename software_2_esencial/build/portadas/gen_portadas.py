# -*- coding: utf-8 -*-
"""Genera los HTML de portada (libro, solucionario, plan anual, planes), contraportada y lámina,
y los rasteriza con Chromium (render.js) a JPG A4."""
import os, subprocess
D = '/home/claude/sw2/build/portadas/'
F = 'fonts/'
CSS = """
@font-face{font-family:'Merri';font-weight:700;src:url('%(f)su-4D0qyriQwlOrhSvowK_l5UcA6zuSYEqOzpPe3HOZJ5eX1WtLaQwmYiScCmDxhtNOKl8yDrOSAqEw.ttf');}
@font-face{font-family:'Mont';font-weight:400;src:url('%(f)sJTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCtr6Ew-.ttf');}
@font-face{font-family:'Mont';font-weight:600;src:url('%(f)sJTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCu170w-.ttf');}
@font-face{font-family:'Mont';font-weight:800;src:url('%(f)sJTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCvr70w-.ttf');}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:216mm;height:330mm}
body{background:#1B5E20;color:#fff;font-family:'Mont',sans-serif;position:relative;overflow:hidden}
.top{position:absolute;top:0;left:0;right:0;height:19mm;background:#123F16;display:flex;align-items:center;justify-content:center;
     font-weight:800;font-size:11.5pt;letter-spacing:.6pt}
.bot{position:absolute;bottom:0;left:0;right:0;height:30mm;background:#123F16;text-align:center;padding-top:8mm}
.bot .p{font-size:9.6pt;opacity:.9;font-weight:400}
.bot .r{font-size:13pt;font-weight:800;margin-top:4mm}
.ser{font-family:'Merri';font-weight:700;text-align:center}
.big{font-family:'Mont';font-weight:800;color:#F2C14E;text-align:center;letter-spacing:1pt}
.pill{display:inline-block;background:#fff;color:#1B5E20;font-weight:800;border-radius:9mm;padding:1.6mm 7mm;font-size:16pt}
.card{position:absolute;left:21mm;right:21mm;background:#fff;border-radius:6mm;color:#333;text-align:center}
.ltl{font-weight:800;color:#2E7D32;font-size:11.5pt;letter-spacing:.4pt}
.h{font-weight:800;color:#1B5E20}
.lin{width:62%%;height:1px;background:#C8E6C9;margin:5mm auto}
.lst{font-size:11.4pt;line-height:1.95;color:#444}
.acc{color:#2E7D32;font-size:10.8pt;margin-top:9mm}
"""


def html(body, css_extra=''):
    return '<!doctype html><html><head><meta charset="utf-8"><style>%s%s</style></head><body>%s</body></html>' % (CSS % {'f': F}, css_extra, body)


TOP = '<div class="top">BACHILLERATO TÉCNICO EN SERVICIOS &nbsp;·&nbsp; ESPECIALIDAD INFORMÁTICA</div>'
BOT = '<div class="bot"><div class="p">Programa de estudio del Ministerio de Educación y Ciencias · Diseño Curricular de Informática</div><div class="r">República del Paraguay · 2026</div></div>'
TIT = '''<div style="position:absolute;top:37mm;left:0;right:0">
 <div class="ser" style="font-size:27pt">Gabinete de Informática</div>
 <div class="big" style="font-size:62pt;margin-top:3mm">SOFTWARE</div>
 <div style="text-align:center;margin-top:3mm"><span class="pill">2.º Curso</span></div></div>'''


def libro():
    body = TOP + TIT + '''
<div style="position:absolute;top:116mm;left:24mm;right:24mm;height:122mm;border:3mm solid #fff;border-radius:5mm;background:#F4FBF5;overflow:hidden;background-image:url('foto_portada.jpg');background-size:cover;background-position:center"></div>
<div style="position:absolute;top:249mm;left:0;right:0;text-align:center">
 <div style="font-weight:800;font-size:17pt">Libro del estudiante con prácticas de laboratorio</div>
 <div style="font-size:11.4pt;opacity:.92;margin-top:3mm">Enfoque «Aprender Haciendo» &nbsp;·&nbsp; Windows 11 y Microsoft Office</div>
 <div style="font-size:11.4pt;opacity:.92;margin-top:2mm">Caso integrador: Servicio Técnico Panambi</div></div>''' + BOT
    return html(body)


def docente(titulo, lineas, acompana='Acompaña al libro del estudiante con prácticas de laboratorio'):
    body = TOP + TIT + '''
<div class="card" style="top:120mm;height:112mm;padding-top:14mm">
 <div class="ltl">MATERIAL DEL DOCENTE</div>
 <div class="h" style="font-size:31pt;margin-top:6mm">%s</div>
 <div class="lin"></div>
 <div class="lst">%s</div>
 <div class="acc">%s</div></div>''' % (titulo, '<br>'.join(lineas), acompana) + BOT
    return html(body)


def contra():
    def li(t):
        return '<div style="display:flex;gap:4mm;align-items:flex-start;margin:2.4mm 0"><span style="color:#F2C14E;font-size:14pt;line-height:1">●</span><span>%s</span></div>' % t
    body = '''
<div style="position:absolute;top:24mm;left:0;right:0;text-align:center">
 <div class="ser" style="font-size:27pt">Gabinete de Informática · Software</div>
 <div style="font-size:11.5pt;opacity:.9;margin-top:3mm">2.º Curso · Bachillerato Técnico en Servicios · Especialidad Informática</div></div>
<div style="position:absolute;top:64mm;left:22mm;right:22mm;font-size:12pt">
 <div style="color:#F2C14E;font-weight:800;font-size:17pt;margin-bottom:3mm">En este libro</div>
 %s
 <div style="color:#F2C14E;font-weight:800;font-size:17pt;margin:9mm 0 3mm">Para el docente</div>
 %s
</div>
<div style="position:absolute;top:238mm;left:30mm;right:30mm;height:30mm;background:#123F16;border-radius:5mm;text-align:center;padding-top:7mm">
 <div style="color:#F2C14E;font-weight:800;font-size:13.5pt">Enfoque «Aprender Haciendo»</div>
 <div style="font-size:11pt;margin-top:2mm">Caso integrador: Servicio Técnico Panambi</div></div>
<div class="bot" style="padding-top:12mm"><div class="r" style="margin:0">República del Paraguay · 2026</div></div>''' % (
        ''.join(li(t) for t in ['20 clases desarrolladas con ejemplos del caso integrador', '20 prácticas de laboratorio paso a paso (Windows 11 y Office)',
                                 '12 fichas de profundización para las semanas de continuidad', 'Prueba diagnóstica y 4 evaluaciones (2 de unidad y 2 de etapa)',
                                 'Proyecto Final Integrador para la Feria de Informática']),
        ''.join(li(t) for t in ['Solucionario docente con todas las respuestas', 'Plan anual de 36 encuentros (2 horas cátedra semanales)', '36 planes de clase listos para usar']))
    return html(body)


PIEZAS = {
 'portada_libro': libro(),
 'portada_solucionario': docente('Solucionario', ['Respuestas de las 20 clases, la prueba diagnóstica', 'y las 4 evaluaciones, con el desarrollo de los cálculos', 'Resultados esperados de las 20 prácticas y las 12 fichas', 'Errores frecuentes a vigilar en cada práctica', 'Orientaciones y rúbrica del Proyecto Final Integrador']),
 'portada_plan_anual': docente('Plan anual', ['36 encuentros de 2 horas cátedra en dos etapas', 'Temas, indicadores de logro, procedimientos', 'e instrumentos de evaluación por encuentro']),
 'portada_planes': docente('Planes de clase', ['36 planes de 2 horas cátedra, listos para usar', '20 clases, 12 fichas de continuación,', '2 evaluaciones de unidad y 2 de etapa', 'Capacidad, indicadores, momentos didácticos,', 'recursos y criterios de evaluación en cada plan']),
 'contraportada': contra(),
}

if __name__ == '__main__':
    for k, v in PIEZAS.items():
        open(D + k + '.html', 'w').write(v)
    subprocess.run(['node', D + 'render.js'] + list(PIEZAS), check=True, cwd=D)

    from PIL import Image
    for k in PIEZAS:
        Image.open(D + k + '.png').convert('RGB').save(D + k + '.jpg', quality=92)
