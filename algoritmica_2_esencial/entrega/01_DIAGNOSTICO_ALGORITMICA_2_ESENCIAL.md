# 01_DIAGNOSTICO — Algorítmica 2.º Curso BTI · Edición Esencial Comercial 2026

Fecha: 03/10/2026 · Responsable: Claude (constructor) · Estado: diagnóstico previo a la construcción.

Este diagnóstico se hizo con el mismo protocolo que el piloto de Algorítmica 3.º. Además, desde el inicio aplica las decisiones que Fer tomó en las rondas v2 y v2.1 de ese piloto:

- capacidades textuales del MEC;
- puntos de control que no revelan el resultado;
- política de recuadros «En Paraguay»;
- PSeInt con perfil Flexible, verificado en ejecución;
- Access 2016 en castellano como referencia;
- formulario e informe del PFI como extensión recomendada;
- rúbrica analítica;
- sin símbolos que dependan de fuentes de emoji.

## 1. Paquete analizado

Versiones vigentes en Drive, carpeta `Algoritmica_2do_Curso`:

| Pieza | Archivo | Última modificación | Observación |
|---|---|---|---|
| Tomo | Algoritmica_2do_Curso_TOMO_COMPLETO.docx | 26/08/2026 22:38 | 8,1 MB: **excede el límite del conector de Drive** y no se pudo descargar. Se trabajó con el PDF de la misma edición (26/08/2026 22:34, 104 págs.) y con la exportación de texto del .docx. |
| Cuaderno | Algoritmica_2do_Curso_CUADERNO_PRACTICAS.docx | 26/08/2026 | 21 prácticas + Proyecto Final Integrador; 2 figuras (P.1 y P.2). |
| Solucionario | Algoritmica_2do_Curso_SOLUCIONARIO_DOCENTE.docx | 26/08/2026 | Respuestas de las actividades de clase, las evaluaciones y la rúbrica del PFI. **Sin soluciones de las prácticas**: solo hay notas para P14 y P21. |
| Plan Anual | Algoritmica_2do_Curso_PLAN_ANUAL.docx | 26/08/2026 | 36 encuentros / 144 HC. Las clases con continuación tienen filas de 8 h; las evaluaciones van sin número y el PFI tiene una fila propia. |
| Planes de Clase | — | — | **No hay Planes de Clase vigentes.** Solo existe PLANES_CLASE_BTI_ALGORITMICA2_2026.docx (03/03/2026), anterior al programa de mayo de 2026. |
| Programa | DISEÑO CURRICULAR DE INFORMATICA – MAYO 2026 | — | Algorítmica, Segundo curso, págs. 74–76; 4 HC semanales. |

Los originales no se modificaron.

**Figuras.** Las 20 figuras se extrajeron del PDF: son las secuencias JPEG que embebió LibreOffice, 1024 px de ancho. Al no disponer del .docx, no se puede garantizar que sean idénticas byte a byte a las del original. Para verificarlo hace falta la copia del .docx.

## 2. Cobertura del programa oficial (Segundo curso)

| Contenido del programa | Clase(s) | Estado |
|---|---|---|
| Conceptos (diagrama de flujo, pseudocódigo, programa, sistema). Tipo de datos | 1 | Cubierto. «Programa» y «sistema» se mencionan pero no se definen. |
| Estructuras básicas de control (secuencial, condicional, repetitiva) | 1–7 | Cubierto |
| Lenguaje de programación: comentarios, sangría, entrada y salida básica, **sentencia de color**, caracteres y operaciones básicas, variables, tipos de datos, **restricciones** | 1–7 (en PSeInt) | **Parcial**. Todo se trabaja en PSeInt, que es un intérprete de pseudocódigo y no un lenguaje de programación. No hay ningún contacto con un lenguaje real. Los comentarios aparecen sin explicarse. Faltan la «sentencia de color» y las restricciones (reglas de nombres y tipos). |
| Reglas generales del pseudocódigo. Banderas | 1, 7 | Cubierto. Las reglas generales están dispersas. |
| Arreglos uni- y multidimensionales: concepto, declaración, dimensionamiento | 8–10 | Cubierto |
| Ordenación: **burbuja optimizada**, selección | 11 | **Error**: el código presentado como «burbuja optimizada» no corta antes de tiempo (ver T1). El método de selección no tiene pseudocódigo. |
| Generación de números aleatorios | 12 | Cubierto |
| Subprogramas, alcance, procedimientos, funciones; parámetros; correspondencia actuales/formales; por valor y por referencia; variables locales y globales | 13–14 | Cubierto. No se aclara que PSeInt no tiene variables globales (ver T12). |
| Datos de tipo cadena: definición, operaciones, **relación**, funciones; caracteres individuales | 14 | **Parcial**: falta la relación (comparación de cadenas). |
| Archivos: concepto, características, tipos; memoria principal y secundaria; tiempos de acceso | 15 | Cubierto |
| Administración de archivos; operaciones; relación con el SO | 16 | Cubierto (con pseudocódigo conceptual; ver T11) |
| Mecanismos de seguridad; tipos de lectura y escritura; organización y acceso; buffers | 17 | Cubierto |
| Estructura visible del sistema de archivos | 18 | Cubierto |
| Filtros: concepto, características; localizar registros relacionados | 19 | Cubierto |
| Consultas: concepto, tipos; selección, paramétrica, totales, campos calculados | 20 | Cubierto |
| Referencias cruzadas; ejercicios | 21 | Cubierto |

**Conclusión:** las 21 clases cubren el programa con tres huecos, que se completan dentro de las clases existentes sin cambiar la estructura:

1. **Lenguaje de programación** (Clase 2). Se agrega «Del pseudocódigo al lenguaje»: comentarios, sangría, entrada y salida, restricciones de nombres y tipos, la noción de sentencia de color en los lenguajes que la tienen, y la exportación de PSeInt a Python, verificada.
2. **Burbuja optimizada y selección en pseudocódigo** (Clase 11).
3. **Relación entre cadenas** (Clase 14).

## 3. Capacidades de las fichas frente al programa

El programa tiene 14 capacidades para 2.º curso. Ninguna ficha las reproduce textualmente.

| Clase | Ficha actual | Capacidad textual del MEC que corresponde |
|---|---|---|
| 1 | «…planeamiento y **la** solución…» | Identifica estrategias para el planeamiento y solución de problemas con algoritmos. |
| 2–4 | «Aplica estructuras selectivas en la resolución…» (sin «anidadas») | 2: Utiliza un lenguaje de programación en la solución de problemas aplicando estructura de control · 3–5: Aplica estructuras selectivas anidadas en la resolución de problemas. |
| 6 | «…ciclos repetitivos y contadores.» | Resuelve problemas utilizando ciclos repetitivos, contadores, acumuladores y banderas. |
| 8–12 | Cinco reformulaciones distintas | Utiliza estructuras de datos estáticas (vectores y matrices) para el planeamiento y la solución de problemas de la vida diaria (lógico, matemático, comerciales, otros.) |
| 14 | «Aplica el pasaje de parámetros y las funciones de cadena…» | Aplica técnicas y procedimientos adecuados de modularización… · Identifica las funciones utilizadas con datos de tipo cadena. |
| 16–21 | Reformuladas («gestor», «los filtros y las consultas») | Textuales del programa (§3 de las notas) |

El Plan Anual resume las capacidades por unidad con redacción propia.

## 4. Extensión por clase

Se cuenta el desarrollo sin ficha ni actividades. Mínimo de la Edición Esencial para Media/BT: 750 palabras.

| Clase | Palabras | Figuras | | Clase | Palabras | Figuras |
|---|---|---|---|---|---|---|
| 1 | 991 | 1 | | 12 | 851 | **0** |
| 2 | 829 | **0** | | 13 | 769 | 1 |
| 3 | 796 | 1 | | 14 | 851 | 1 |
| 4 | 807 | **0** | | 15 | 951 | 1 |
| 5 | 769 | **0** | | 16 | 905 | **0** |
| 6 | 913 | 2 | | 17 | 1.101 | **0** |
| 7 | 784 | 1 | | 18 | **701** | 1 (+1 sin epígrafe) |
| 8 | 861 | 1 | | 19 | 969 | 2 |
| 9 | 779 | **0** | | 20 | 780 | 1 |
| 10 | 809 | 1 | | 21 | **722** | 1 |
| 11 | 817 | 2 | | | | |

- **Las Clases 18 y 21 están por debajo del mínimo.** La ampliación tiene que responder a contenido real, no a relleno: rutas y atajos del Explorador en la 18; diseño de la referencia cruzada en Access en la 21.
- **Siete clases no tienen ningún diagrama**: 2, 4, 5, 9, 12, 16 y 17. El estándar gráfico los exige en materias procedimentales.
- Cada clase tiene 12 actividades.

## 5. Prácticas: repeticiones y extensión

- **Las prácticas repiten el ejemplo resuelto de su clase.** Coincidencias exactas de datos y código:
  - P5: la clasificación 20.000/50.000 de la clase, con los mismos montos de prueba.
  - P6 y P7: la misma semana (420.000 … 300.000) y los mismos resultados.
  - P8 y P9: la misma semana y el mismo «sábado = 1.100.000».
  - P11: el mismo código de burbuja, no optimizado.
  - P13: la misma función CalcularTotal.
  - P14: **el mismo modelo de paso por referencia, copiado tal cual de la clase.**
  - P16: el mismo archivo de la semana.
  - P2 y P3: la misma regla de descuento.
- **Casi todas las prácticas tienen una sola actividad** de 2 a 5 pasos. Diez de ellas (P7, P10, P14 y P15–P21) tienen un encuentro propio de 4 HC según el Plan Anual, y su extensión no alcanza.
- **Todo el trabajo usa un único caso** (las mismas siete ventas de la semana del copetín). P19–P21 (tabla Bebidas) son la única excepción.

## 6. Respuestas reveladas

- **Puntos de control de las prácticas:** casi todos anuncian la salida exacta («Deberías ver: Total: 64800», «Producto 1: 55, Producto 2: 97…», «El vector ordenado debe quedar: 150, 110…»). Fer pidió que el resultado numérico quede solo en el solucionario.
- **Evaluaciones:**
  - E1 ítem 9: «probala con 60.000 **(resultado 54.000)**».
  - U2 ítem 7 y E2 ítem 5: «…qué producto queda primero **(Coquito=200)**».
  - E1 ítem 7 da los totales por fila que se piden calcular.
- **Evaluaciones que copian el ejemplo de la clase:** U1 ítems 5, 7 y 8; U2 ítems 5, 6, 8 y 9; U4 ítems 5, 7 y 8.

## 7. Errores conceptuales y técnicos

Todo el pseudocódigo del tomo y del cuaderno se ejecutó en **PSeInt 20250314 con el perfil Flexible**.

| N.º | Ubicación | Problema | Gravedad |
|---|---|---|---|
| T1 | Clase 11, P11, Fig. 2.3 | El código llamado «burbuja optimizada» hace siempre las 5 pasadas: no tiene la bandera que corta cuando una pasada no intercambia. El programa exige «burbuja optimizada». | Crítico |
| T2 | Clase 11 | El método de selección no tiene pseudocódigo, solo una tabla y una figura. | Mayor |
| T3 | Clase 2 (recuadro), Clases 2–5 | El tomo afirma que «las variables de dinero de este tomo son de tipo entero», pero calcula `monto - monto * 0.10`. Comprobado: con `Definir monto Como Entero` y monto = 55.555, PSeInt se detiene con «ERROR 314: No coinciden los tipos, el valor a asignar debe ser un entero». Las prácticas definen el monto como Real, así que hay incoherencia. | Mayor |
| T4 | Clase 2, «Errores frecuentes» | «Confundir = con <-: la condición asigna en vez de comparar». En PSeInt, dentro de una condición `=` siempre compara. El perfil Flexible además acepta `=` como asignación fuera de las condiciones. El error descrito no ocurre así. | Mayor |
| T5 | Clase 1 y Clase 19 | Dos recuadros «En Paraguay» afirman sin respaldo verificable que PSeInt es «la herramienta más usada» en los colegios técnicos del país y que Access es «el gestor más usado». | Mayor (política v2) |
| T6 | Clase 17 | «La Ley 6534/2020 de protección de datos personales…». Esa ley regula los **datos personales crediticios**, no la protección de datos personales en general. La cita es incorrecta. | Crítico (legal) |
| T7 | Clase 5 | El recuadro sobre los «tramos del impuesto a la renta personal» introduce contenido tributario sin verificar y ajeno a la clase. | Mayor (política legal) |
| T8 | P21 | Usa `IIf(...)` en la cuadrícula de diseño. En Access en castellano la función puede mostrarse como `SiInm`. | VERIFICACIÓN MANUAL |
| T9 | P19 | Crea los campos sin indicar el tipo de dato. En la vista Diseño Access propone Texto corto, y con STOCK como texto no aparece «Filtros de número»: la Actividad 2 falla siguiendo los pasos al pie de la letra. | Crítico (la práctica no funciona) |
| T10 | P19 | Para pasar a la vista Diseño Access exige guardar la tabla con un nombre, y la práctica no lo dice. Después se la menciona como «Bebidas». | Mayor |
| T11 | Clases 16–17, Ev. U3 | El pseudocódigo conceptual de archivos usa notaciones distintas en cada ejemplo («Escribir En Archivo:», «Escribir Archivo», «Leer Archivo linea», «MontoDe»). La advertencia «no ejecutar en PSeInt» está bien, pero hace falta una sola notación documentada. | Mayor |
| T12 | Clase 13 | Explica las variables globales sin aclarar que PSeInt no permite declararlas: cada SubProceso tiene sus propias variables. El estudiante no puede probar en PSeInt lo que lee. | Mayor |
| T13 | Clase 14 | No se trata la relación (comparación) entre cadenas. Comprobado en PSeInt: `"Zapallo" < "anana"` da VERDADERO, porque las mayúsculas van antes que las minúsculas. Es una fuente típica de errores. | Mayor (cobertura) |
| T14 | Clases 18, 19, 20 y 21 | Hay 4 imágenes sin epígrafe. Tres son cajas «Ejemplo» pegadas como imagen y una de ellas corta un párrafo («…cualquier categoría. [imagen] Un a consulta…», p. 94). La de la Clase 18 repite la Fig. 3.2. Además, las figuras se numeran por unidad (1.1–4.4), no por clase. | Mayor (maquetación) |
| T15 | Clase 4 / P4 | La clase usa la variable lógica `enBarrio = Verdadero` y la práctica, `enBarrio` 1/0. | Menor |
| T16 | Clase 9 | En el máximo, `segundo` empieza en 0: falla con datos negativos y no se advierte. Es correcto para ventas. | Menor |
| T17 | Plan Anual | Filas de 8 h, evaluaciones sin número, capacidades resumidas y procedimientos con la fórmula «Práctica N integrada…» en lugar de una actividad evaluable. | Mayor |
| T18 | Solucionario | No tiene soluciones de las 21 prácticas. | Crítico (falta una pieza) |
| T19 | Paquete | No hay Planes de Clase vigentes. | Crítico (falta una pieza) |
| T20 | Recuadros | 29 recuadros «En Paraguay». Solo algunos son específicos y verificables (RUC con dígito verificador; DNIT y comprobantes). La mayoría son generales: cajero automático, Explorador de Windows, supermercados. | Mayor (política v2) |
| T21 | Prueba diagnóstica | Correcta. Las respuestas del solucionario coinciden. | — |

**Pseudocódigo verificado en PSeInt (perfil Flexible):**
- Ejecutan y dan lo que dice el tomo: DescuentoPorMonto (54.000 / 24.000), Delivery, Vuelto, PromoCombo, MenuMostrador, el Mientras de la semana (2 días), MetaDelDia (3 ventas, 114.000), la validación con Repetir, CierreDeCaja (4 ventas, 120.000, promedio 30.000, y «No se cargaron ventas» con 0), el informe semanal (4.200.000 / 600.000 / 1.100.000 en la posición 6 / 300.000 en la posición 7), el segundo mejor día (850.000), la matriz (123/75/45, 243 en total), la facturación (1.284.000), la burbuja (200 123 90 75 60 45), Azar(900001)+300000 dentro del rango, el sistema de caja (54.000), por referencia (54.000) y por valor (60.000).
- Funciones de cadena: Subcadena «MIX»/«01», Longitud 6, Longitud(«María») 5, Mayusculas(«María») «MARÍA», Longitud(«Ramón») 5, Mayusculas(«Ramón») «RAMÓN», Concatenar «EMP-01», 5 letras «a» en «Sopa paraguaya».
- Índice fuera de rango: ERROR 303.

**Cálculos verificados:**
- Semana: 4.200.000; promedio 600.000.
- Matriz: 123 / 75 / 45 por fila y 55 / 53 / 58 / 77 por columna; 243 en total.
- Inventario: 798.000 (salado 426.000, dulce 100.000, bebida 272.000); stock 321.
- Referencias cruzadas: 3 / 4 y 2 / 2 / 1 / 2.
- Prácticas: P10 55 / 97 / 35 (187); P20 200.000 / 150.000; P21 1 / 2 / 1 / 1.

## 8. Caso Copetín Karumbé

Los números del caso cierran y se conservan. El problema es que todo el año gira sobre las mismas siete ventas y la misma tabla de siete productos.

Para la nueva edición:

- **Las clases conservan su semana de referencia.** Las prácticas usan datos nuevos: otra semana del copetín, una cantina escolar, una librería, un club, una biblioteca y una farmacia de barrio (estas últimas en la Unidad 4), sin repetir los ejemplos resueltos.
- **Montos:** se mantienen en guaraníes enteros. El descuento se calcula con `trunc` o con montos donde la división es exacta, y se explica por qué (T3).

## 9. Identidad visual

Algorítmica 1.º–3.º comparte la identidad **VERDE BTI** (#1B5E20 / #2E7D32) con acento ámbar, ya aprobada para 3.º. Las figuras del tomo están en esa paleta, así que se mantiene. No hay ilustración de portada propia: queda pendiente para Gemini, igual que en 3.º.

## 10. Plan de construcción

1. **Libro unificado** (Clase N → Práctica N) con correcciones T1–T16, capacidades textuales, recuadros según la política v2, ampliación de las Clases 18 y 21, y nuevos diagramas en las Clases 2, 4, 5, 9, 12, 16 y 17.
2. **21 prácticas reescritas** con datos nuevos, 2 o 3 actividades cada una, puntos de control sin resultado, transferencia entre pares donde haga falta, y todo el pseudocódigo ejecutado en PSeInt.
3. **Solucionario completo**: actividades, las 21 prácticas, evaluaciones y rúbrica analítica del PFI con los pesos actuales (30/25/20/15/10).
4. **Plan Anual de 36 filas** y **36 Planes de Clase** (pieza nueva), con la misma numeración.
5. **Auditoría automática** y NOTAS_PILOTO_ALGORITMICA_2_ESENCIAL_v1.
