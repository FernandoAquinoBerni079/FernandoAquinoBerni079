# -*- coding: utf-8 -*-
"""NOTAS_PILOTO_ALGORITMICA_2_ESENCIAL_v1.md: hallazgos del diagnóstico, corrección aplicada, archivo/página y estado."""
import json, re
from estructura import cargar
import ediciones, practicas, evaluaciones
_p, C, _e, U = cargar(); ediciones.aplicar(C); ediciones.fig_refs(C)
J = json.load(open('/home/claude/alg2/build/indice_libro.json')); PG = {t: p for (n, t), p in zip(J['entradas'], J['paginas'])}
def pc(n): return [p for t, p in PG.items() if t.startswith('Clase %d —' % n)][0]
def pp(n): return [p for t, p in PG.items() if t.startswith('Práctica %d —' % n)][0]
def pe(i): return PG[[e for e in evaluaciones.EV if e['id'] == i][0]['titulo']]
LIB, SOL, PA, PL = 'Libro', 'Solucionario', 'Plan Anual', 'Planes de Clase'
AUD = open('/home/claude/alg2/build/auditoria_resultado.txt').read().splitlines()[1]
R = []
def r(h, c, a, e='CORREGIDO'): R.append((h, c, a, e))

r('Las 21 fichas parafraseaban las capacidades del programa.', 'Capacidades reproducidas textualmente del programa MEC (Diseño Curricular de Informática, mayo 2026, págs. 74–76); la Clase 14 lleva sus dos capacidades (modularización y cadenas). Indicadores sin cambios.', '%s, fichas de las 21 clases; %s; %s' % (LIB, PA, PL))
r('El Plan Anual no aclaraba la naturaleza de los indicadores.', 'Nota acordada en el piloto: «Las capacidades se reproducen textualmente del programa MEC vigente. Los indicadores de logro de este plan son operativizaciones observables…». 2.º no tiene capacidad conductual en el programa: no se agrega una transversal.', '%s, pág. 2' % PA)
r('Faltaban contenidos del programa: comentarios, sangría, sentencia de color, restricciones del lenguaje.', 'Nueva sección «Del pseudocódigo al lenguaje de programación» con el mismo algoritmo en PSeInt y en Python (exportado con PSeInt y verificado) y tabla de equivalencias.', '%s, Clase 2, págs. %d–%d' % (LIB, pc(2), pp(2) - 1))
r('Conceptos «programa» y «sistema» del programa no definidos.', 'Definidos en la Clase 1.', '%s, Clase 1, pág. %d' % (LIB, pc(1)))
r('T1: el código de la «burbuja optimizada» no tenía bandera: nunca cortaba antes.', 'Reemplazado por la versión con la bandera hubo (Repetir … Hasta Que NO hubo O i > 5); 4 pasadas en lugar de 5, verificado.', '%s, Clase 11, pág. %d' % (LIB, pc(11)))
r('T2: el método de selección se explicaba sin pseudocódigo.', 'Pseudocódigo del método de selección agregado (verificado en PSeInt).', '%s, Clase 11' % LIB)
r('T3: montos Entero con 10 % de descuento no exacto detienen PSeInt (ERROR 314).', 'Recuadro «En Paraguay — guaraníes sin céntimos» con trunc/redon; los ejemplos usan montos donde el 10 % es exacto; Práctica 2 lo hace experimentar en el desafío.', '%s, Clase 2 y Práctica 2' % LIB)
r('T4: fila «Confundir = con <-» de la tabla de errores incorrecta para el perfil Flexible.', 'Fila corregida.', '%s, Clase 2' % LIB)
r('T5: superlativos no verificables («la más usada»…).', 'Reemplazados por formulaciones neutras.', '%s, Clases 12, 18 y 20' % LIB)
r('T6/T7: recuadros con la Ley 6534/2020 (es de datos crediticios) y tramos de IRP.', 'Eliminados.', '%s, Unidad 3' % LIB)
r('T8: IIf/SiInm en Access.', 'Se usa SiInm(condición;sí;no) en la cuadrícula y se aclara que la vista SQL muestra IIf.', '%s, Clase 21 y Práctica 21' % LIB, 'CORREGIDO — pendiente de verificación manual en Access')
r('T9/T10: la práctica de Access no fijaba tipos de datos ni pedía guardar la tabla con nombre.', 'Práctica 19 con diseño explícito (Texto corto / Número Entero largo, clave principal) y paso «Guardá la tabla con el nombre Articulos».', '%s, Práctica 19, pág. %d' % (LIB, pp(19)))
r('T11: notación de archivos inconsistente (Escribir En Archivo, Cerrar…).', 'Notación conceptual única de la Unidad 3 documentada en un Concepto clave: Abrir … Para Lectura/Escritura/Agregar, Escribir Archivo, Leer Archivo, FinDeArchivo, Cerrar Archivo.', '%s, Clase 16, pág. %d' % (LIB, pc(16)))
r('T12: se hablaba de variables globales, que PSeInt no tiene.', 'Aclaración con ejemplo ejecutado (dentro: 99 / fuera: 5).', '%s, Clase 13' % LIB)
r('T13: faltaba la relación (comparación) entre cadenas.', 'Sección «Comparar cadenas: la relación entre textos» con resultados verificados en PSeInt ("Zapallo" < "anana", "10" < "9") y recuadro de errores frecuentes.', '%s, Clase 14' % LIB)
r('T14: tres imágenes sin epígrafe y un párrafo partido por una imagen.', 'Imágenes retiradas; párrafo reparado; toda figura numerada por clase (N.M), anunciada en el texto y con epígrafe.', LIB)
r('Siete clases sin ninguna figura (2, 4, 5, 9, 12, 16, 17).', 'Siete diagramas nuevos (Si simple, condición compuesta, Si anidado frente a Segun, recorrido del máximo, rango de Azar, modos de apertura, buffer). Las 17 figuras originales se conservan byte a byte.', '%s, Figuras 2.1, 4.1, 5.1, 9.1, 12.1, 16.1, 17.1' % LIB)
r('T15: envío con enBarrio 1/0 en lugar de una variable lógica.', 'Condiciones con variables lógicas (Verdadero/Falso) en clase, práctica y evaluaciones.', LIB)
r('T16: segundo <- 0 sin justificar.', 'Nota que explica por qué funciona aquí (ventas no negativas) y qué hacer si no.', '%s, Clase 9' % LIB)
r('Clases 18 y 21 por debajo de 750 palabras.', 'Ampliadas: propiedades de un archivo y búsqueda con comodines (18); referencia cruzada en Access paso a paso con rutas de Access 2016 (21).', '%s, Clases 18 y 21' % LIB)
r('Carpeta raíz del caso mezclada (C:\\Copetin y C:\\Karumbe).', 'Unificada en C:\\Karumbe.', '%s, Clase 18' % LIB)
r('T20: 29 recuadros «En Paraguay», la mayoría genéricos.', 'Política del piloto: se conservan 2 con contenido paraguayo concreto (guaraníes sin céntimos; el RUC); el resto pasa a «Ejemplo cotidiano» o «Aplicación profesional», se integra como texto o se elimina. No se inventaron datos.', LIB)
r('Access: «la versión más usada» y rutas sin versión.', 'Una sola referencia general a Access 2016 en castellano; rutas de menú del asistente de referencias cruzadas según la documentación oficial.', '%s, Clase 19' % LIB, 'CORREGIDO — pendiente de verificación manual de rótulos de interfaz')
r('Las actividades copiaban los ejemplos resueltos (misma semana, mismo vector, mismo código MIX-01).', '75 de 252 actividades reescritas con datos nuevos: semana 2 (4.480.000), matriz de bebidas (181 unidades; 1.313.000), vector del ranking unid2, códigos SOP-07/COC-12, consultas nuevas sobre la tabla Productos. Respuestas recalculadas.', '%s, Actividades de aplicación; %s, Primera parte' % (LIB, SOL))
r('Prácticas del cuaderno: una actividad, mismos datos que la clase y «Deberías ver: …» en el punto de control.', '21 prácticas nuevas en la Librería escolar Arandu (2 actividades; 3 en las 10 que continúan en encuentro propio), puntos de control que contrastan con lo anticipado sin revelar cifras, transferencia y revisión entre pares solo en 7, 10 y 14.', '%s, Prácticas 1–21' % LIB)
r('El código de las prácticas no estaba verificado.', 'Los 37 programas de las Prácticas 1–14 se ejecutaron en PSeInt 20250314 (perfil Flexible); la auditoría los re-ejecuta y compara con el solucionario. Hallazgos documentados: un SubProceso sin parámetros no lleva paréntesis; una variable no puede llamarse igual que el algoritmo (ERROR 48).', 'pseint/*.psc; %s, Segunda parte' % SOL)
r('Evaluaciones con la respuesta en la consigna (E1-9 «(resultado 54.000)», U2-7 y E2-5 «(Coquito=200)») y datos de los ejemplos de clase.', 'Seis evaluaciones con la misma ubicación, alcance y forma (3 + 6 ítems), datos propios (heladería Yvoty, fotocopiadora Ñandutí) y sin resultados en las consignas.', '%s, págs. %d, %d, %d, %d, %d, %d' % (LIB, pe('U1'), pe('U2'), pe('E1'), pe('U3'), pe('U4'), pe('E2')))
r('T18: el solucionario no traía respuestas de las prácticas.', 'Resultado esperado y errores frecuentes de las 21 prácticas y de las 3 transferencias; claves de las 6 evaluaciones (21 puntos).', SOL)
r('PFI: figura del flujograma con texto cortado y superpuesto; rúbrica holística.', 'Flujograma redibujado (Figura PFI.1); rúbrica analítica con los mismos criterios y pesos 30/25/20/15/10 y niveles 100/60/30/0 %; extensión recomendada con la fórmula acordada (tabla Ventas y ticket en archivo).', '%s, Proyecto Final Integrador; %s' % (LIB, SOL))
r('T17: Plan Anual con el PFI en una sola fila de 12 h y referencias al Cuaderno.', '36 filas (una por encuentro), 18 por etapa, PFI en tres talleres; procedimientos e instrumentos únicos; remite al libro.', PA)
r('T19: no había Planes de Clase vigentes de 2.º.', '36 planes nuevos (21 clases, 10 continuaciones, 3 talleres, 2 integradoras) derivados del libro y del Plan Anual; hora cátedra de 40 min declarada; alternativa en papel en los planes con equipamiento.', PL)
r('E2 declaraba «Unidades 1 a 4».', 'Se respeta el alcance vigente; las capacidades listadas son las que efectivamente evalúan sus ítems.', '%s; %s' % (PA, PL))
