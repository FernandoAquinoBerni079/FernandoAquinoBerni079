# Guía de redacción — Desarrollo Personal y Social 7.º · Edición Esencial Comercial 2026 (versión candidata con PEC)

Lectura obligatoria para cada redactor antes de escribir. La arquitectura anual está en `../build/curriculo.py` (fuente única: números de encuentro, tipo, capacidades, títulos y origen en el paquete anterior).

## 1. Qué estamos haciendo

Reconstruimos el combo de 7.º grado (libro del estudiante, solucionario, Plan Anual y Planes de Clase) en formato oficio, **sin empezar de cero**: el texto del libro anterior es la base y se conserva lo valioso (párrafos, ejemplos, personajes, actividades, figuras). Se amplía porque el libro anterior quedó **demasiado sintetizado** (≈ 400–500 palabras por clase) y se integra el **Componente Proyecto Educativo Comunitario (PEC)**.

Destinataria: una profesora con 3 HC semanales de Desarrollo Personal y Social (36 encuentros de 3 HC = 108 HC; 1 HC = 40 min, 3 HC = 120 min) que necesita un material completo para todo el año.

Fuentes de lectura (no se modifican):
- Libro anterior por secciones: `/home/claude/dps7/orig_secc/*.md` (marcado: `[[FICHA]]`, `[[CAJA]] texto / texto`, `[[TABLA]]`, `[[IMG imageN.png]]`).
- Solucionario anterior: `/home/claude/dps7/fuente_orig/sol7.md`.
- Planes de clase anteriores: `/home/claude/dps7/orig_planes/planNN.md`.
- Programa MEC de 7.º (texto): `/home/claude/dps/prog7.txt` (capacidades en las líneas ≈ 1415–1600; orientaciones metodológicas ≈ 1600–2050; componente PEC y Esquema de Proyecto ≈ 2051–2200; evaluación ≈ 2200–2300).

## 2. Voz y registro

- Español rioplatense-paraguayo con **voseo** («pensá», «observá», «sos», «tenés»). Como el libro anterior, el texto le habla al estudiante de vos («Empezás el tercer ciclo…»). Nunca tuteo.
- Comillas angulares «…». Sin emojis. **Prohibidos los símbolos ✓ ✗ ✅ ✔** y similares.
- Párrafos de 3 a 5 líneas; oraciones claras para adolescentes de 12–13 años; explicación, no enunciado: si se introduce un concepto, se dice qué es, cómo se reconoce, para qué sirve y se muestra en una situación.
- Contexto paraguayo real (escuela, barrio, familia, guaraní cuando suma), sin nombrar ciudades, departamentos ni instituciones reales en los casos.
- Personajes del libro (se conservan): **Belén, Rodrigo, Dahiana y Matías**, compañeros de 7.º grado. Para el PEC, el colegio de los personajes es el **«Colegio Arasa Poty»**, institución ficticia (decirlo una vez en el Taller PEC 1).
- Ninguna aprobación ni certificación del MEC: el libro «sigue el programa de estudio del MEC», nunca «aprobado por».

## 3. Cuidado de temas sensibles y privacidad (no negociable)

- «Mirate» es privado: no lleva nota, no se expone, no se corrige. Ninguna consigna evaluable puede exigir revelar experiencias, datos familiares, de salud, sexualidad o violencia propios. Las evaluaciones usan **casos ficticios**.
- Ante violencia, abuso o riesgo: adulto de confianza, orientación del colegio, CODENI de la municipalidad, **Fono Ayuda 147** (gratuito, del Ministerio de la Niñez y la Adolescencia), **911** ante peligro inmediato. No agregar otros números ni leyes nuevas sin fuente.
- Normas que se pueden citar (verificadas, ya presentes en la serie): Constitución Nacional; Código de la Niñez y la Adolescencia (Ley N.º 1680/2001); Ley General de Educación (Ley N.º 1264/1998); Ley N.º 4633/2012 contra el acoso escolar; Declaración Universal de Derechos Humanos (1948); Convención sobre los Derechos del Niño (1989). **Eliminar** afirmaciones con fecha que no podamos respaldar (por ejemplo, el «proyecto de ley 2026 del MINNA y el MITIC» del libro anterior).
- Seguridad en el PEC: nada de obras físicas, herramientas peligrosas, residuos peligrosos, salidas sin autorización escrita de la dirección y de las familias, manejo de dinero sin supervisión docente, contacto con desconocidos por redes, ni fotografías de personas sin consentimiento. Proyectos de bajo costo.

## 4. Capacidades e indicadores

- La **capacidad se copia literal** de `curriculo.CAP[k]` (copiar y pegar, sin «mejorar»). Si una clase trabaja dos capacidades, van dos líneas `Capacidad:`.
- El **tema** puede redactarse editorialmente, pero tiene que corresponder a los temas MEC de esa capacidad (`curriculo.TEMAS_MEC`).
- **Tres indicadores de logro** por clase, observables (lo que el estudiante hace), uno por línea. Se pueden mantener o mejorar los del libro anterior.
- En los talleres PEC no hay capacidades propias del componente: la ficha muestra el **propósito literal** del componente (lo pone el constructor), la **etapa del proyecto**, las **capacidades del área vinculadas** (literal, las que indica `curriculo.py`) y tres **indicadores de logro de elaboración editorial**.

## 5. Formato del archivo fuente del libro: `fuente/tomo/eNN.md` (NN = n.º de encuentro, dos dígitos)

```
@@ENC 05
[[FICHA]]
Capacidad: <literal>
Tema: <tema>
- <indicador 1>
- <indicador 2>
- <indicador 3>
[[/FICHA]]
<párrafo de apertura con la situación de los personajes>
## <Subtítulo de sección>
<párrafo>
<párrafo>
<párrafo que anuncia la figura: «Observá la figura 4.1: …»>
[[IMG image4.png|12]]
Figura 4.1 — <epígrafe del libro anterior>.
[[TABLA]]
Encabezado 1 | Encabezado 2
celda | celda
[[/TABLA]]
[[CAJA ejemplo]]
<texto del ejemplo; puede tener varios párrafos, uno por línea>
[[/CAJA]]
[[CAJA concepto]]
<definición operativa de 2 o 3 líneas>
[[/CAJA]]
[[CAJA paraguay]]
<anclaje paraguayo>
[[/CAJA]]
### Actividades
Pensá y respondé:
1. <consigna abierta>
[[RENGLONES 3]]
2. <opción múltiple>
    a) …
    b) …
    c) …
    d) …
3. Escribí V (verdadero) o F (falso) en cada afirmación:
    a) … ____
    b) … ____
    c) … ____
[[CAJA mirate]]
Estas preguntas son tuyas. No tienen respuesta correcta y no llevan nota: te ayudan a conocerte. Respondelas con sinceridad.
6. …
[[RENGLONES 3]]
7. …
[[RENGLONES 3]]
[[/CAJA]]
En grupo:
8. <dinámica>
```

Reglas del marcado:
- Una línea = un párrafo. `## ` = subtítulo de sección; `### Actividades` abre el bloque de actividades (en las evaluaciones, `### Parte 1 — …`).
- Cajas: `ejemplo` («Ejemplo —»), `concepto` («Concepto clave —»), `paraguay` («En Paraguay —»), `cuidado` («Para cuidarte —», avisos de seguridad o de derivación), `mirate` («Mirate — para pensar sobre vos»), `taller` («Actividad práctica —», consigna extendida de práctica), `bitacora` («Para la bitácora del proyecto —», solo PEC), `neutra` (sin prefijo).
- `[[RENGLONES n]]` agrega n renglones para escribir (usalo después de cada consigna abierta del libro: 2 a 5 según la extensión esperada).
- Opciones con 4 espacios y `a) `…`d) `. **Las opciones múltiples tienen 4 opciones y una sola correcta**; repartí la correcta entre a, b, c y d (no siempre la misma letra).
- Figuras: las del libro anterior se conservan **en su clase**, con el mismo archivo `imageN.png` y el epígrafe renumerado como «Figura K.1» (K = n.º de clase). Siempre con un párrafo previo que la anuncie. Ancho sugerido 11–14 cm. Si necesitás una figura nueva, poné `[[IMG nueva_<nombre>.png|12]]` + epígrafe y describila en `fuente/PEDIDOS_FIGURAS.md` (qué debe mostrar, textos exactos): la dibuja el constructor. Máximo una figura nueva por clase.
- Numeración de consignas continua dentro de cada encuentro.
- Sin códigos internos visibles (nada de «e05», «C-01», «image4»).

## 6. Extensión y anatomía de una clase temática (Componente Orientación)

- **Desarrollo en prosa ≥ 800 palabras** (sin contar ficha, cajas ni actividades); total de la clase con cajas y actividades ≈ 1.300–1.900 palabras. Cuatro o cinco secciones `##`.
- Cada clase lleva: apertura con los personajes; secciones conceptuales explicadas; la figura del libro anterior; **una tabla**; una caja `ejemplo`; una caja `concepto`; una caja `paraguay` (o `cuidado` si el tema lo pide); y actividades: **Pensá y respondé** (5 consignas: 2 abiertas, 2 opción múltiple, 1 V/F de 3 afirmaciones), **Mirate** (2 consignas privadas), **En grupo** (1 dinámica concreta, realizable en el aula en 20–30 min, con producto visible).
- Si `curriculo.py` indica que el encuentro absorbe una «Continuación práctica» del paquete anterior, su actividad se integra como sección `## Actividad práctica: …` o caja `taller` dentro de la clase (no se pierde).
- La clase tiene que poder hacerse en 120 minutos y un estudiante que faltó tiene que poder estudiar de ella.
- Vincular con el proyecto comunitario cuando sea natural (una línea o una consigna), sin forzar.

## 7. Evaluaciones de unidad (`@@ENC NN` de tipo E)

- Empiezan con `@@ENC NN`. El constructor pone la banda, el título y la línea «Nombre y Apellido / Curso / Fecha».
- Primera línea: «Puntaje total: 30 puntos. Leé cada consigna con atención.» (puntaje sugerido; la escala la fija la institución).
- `### Parte 1 — Comprensión` (opción múltiple y V/F; ≈ 12 puntos), `### Parte 2 — Analizá la situación` (2 casos ficticios con preguntas abiertas; ≈ 12 puntos), `### Parte 3 — Tu posición` (1 consigna argumentativa sobre un caso ficticio, sin exigir datos personales; ≈ 6 puntos). Indicar el puntaje de cada consigna entre paréntesis al final: «(2 puntos)».
- 9 a 12 consignas, todas trazables a los indicadores de las fichas de la unidad. Renglones reales para las abiertas.
- Nada de claves en el libro.

## 8. Solucionario: `fuente/sol/eNN.md`

Mismo marcado. Para cada clase:
```
@@ENC 05
## Propósito y conducción
<cómo conducir los tres momentos, qué enfatizar, errores frecuentes de los estudiantes, cómo cuidar el clima>
## Respuestas esperadas
1. <ideas clave esperadas; para opción múltiple: «Respuesta: c) …» y por qué>
2. …
## Mirate
<cómo acompañar sin corregir; señales de alerta y derivación>
## En grupo: criterios de valoración
[[TABLA]]
Criterio | Logrado | En proceso | No logrado
…
[[/TABLA]]
```
Para cada evaluación: `## Clave de corrección` (tabla Consigna | Respuesta o ideas esperadas | Puntaje), `## Criterios para las respuestas abiertas` (rúbrica breve), `## Recuperación` (qué reforzar).
No imponer respuestas únicas en consignas abiertas: dar ideas esperadas y criterios.

## 9. Plan de clase: `fuente/planes/eNN.json`

```json
{
  "inicio": {"min": 20, "acts": ["…", "…"]},
  "desarrollo": {"min": 80, "acts": ["…", "…", "…"]},
  "cierre": {"min": 20, "acts": ["…", "…"]},
  "recursos": "Libro del estudiante (Clase 4, figura 4.1 y tabla …); …",
  "procedimientos": "<una oración, ÚNICA en todo el año>",
  "instrumentos": "<una oración, ÚNICA en todo el año>",
  "criterios": ["<criterio observable>", "<criterio>", "<criterio>"],
  "observacion": "<opcional, para el Plan Anual>"
}
```
- Los minutos suman **120**. Las actividades citan lo que hay en el libro (secciones, figuras, consignas por número) y describen qué hace el docente y qué hacen los estudiantes.
- La capacidad, el tema y los indicadores **no se escriben acá**: el constructor los lee de la ficha del libro.
- `procedimientos` e `instrumentos` alimentan el Plan Anual y tienen que ser **distintos en cada encuentro** (variá: lista de cotejo, rúbrica analítica, escala de estimación, registro anecdótico, portafolio, coevaluación, autoevaluación con criterios, bitácora, informe, mapa conceptual evaluado, resolución de caso, prueba escrita de unidad…). En las evaluaciones, nombrá la unidad en ambos campos.

## 10. Controles que va a correr el constructor

Capacidades literales; 3 indicadores; ≥ 800 palabras de prosa por clase (≥ 900 en talleres PEC); 4 opciones con una correcta; correcta repartida; V/F con clave; figura anunciada; voseo (sin «piensa», «observa», «escribe», «tú», «tienes»…); sin ✓ ✗; minutos = 120; procedimientos e instrumentos únicos; correspondencia de cada consigna del libro con su respuesta en el solucionario (misma numeración).
