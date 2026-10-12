@@H2 Clase 17 — Medios de transmisión guiados
[[FICHA]]
Capacidad: Identifica las características principales de los medios de transmisión más utilizados.
Tema: Medios guiados: concepto, tipos, normativas, características y aplicación.
- Caracteriza el par trenzado, el coaxial y la fibra óptica.
- Interpreta las categorías del cable UTP y sus prestaciones.
- Selecciona el medio guiado adecuado para un escenario dado.
[[/FICHA]]
[[IMG T_image33.jpg|12.8]]
Figura 17.1 — Comparación de cables de cobre y fibra óptica.
## Qué es un medio guiado
Un medio guiado conduce la señal por un camino físico: un cable. Frente al aire, ofrece estabilidad, velocidad sostenida y previsibilidad; a cambio, exige instalar y mantener el tendido. Los tres medios guiados de las redes son el par trenzado, el coaxial y la fibra óptica.
[[CAJA Concepto clave — Categoría (UTP)]]
Clasificación normalizada del par trenzado que certifica hasta qué velocidad y frecuencia rinde el cable en el enlace completo. A mayor categoría, mejores prestaciones y mayor precio por metro.
[[/CAJA]]
## El par trenzado
Es el cable de red por excelencia: cuatro pares de cobre trenzados para reducir interferencias. U/UTP (frecuentemente llamado UTP) domina instalaciones comunes; variantes apantalladas se emplean cuando el entorno lo requiere. La categoría 5e soporta Gigabit Ethernet en canales de hasta 100 m. Categoría 6 mejora el margen y puede soportar 10GBASE-T en distancias reducidas según instalación y condiciones; categoría 6A está diseñada para soportar 10GBASE-T en el canal completo de 100 m.
[[CAJA Ejemplo — ¿Qué cable para el aula?]]
Para el aula del Instituto Ko'ẽju, Panambi especifica UTP categoría 6: el costo apenas supera al de la 5e y deja margen para la próxima década. ¿Fibra hasta cada puesto? Sería pagar troncal de operador para imprimir documentos: el informe lo descarta con la cuenta a la vista.
[[/CAJA]]
## El coaxial
El coaxial lleva un conductor central rodeado de aislante y una malla que lo blinda. Fue el cable de las primeras redes en bus y sobrevive en la TV por cable, las antenas y los tramos de cámaras de seguridad analógicas. En redes de datos nuevas ya no se instala.
[[TABLA]]
Medio | Velocidad práctica | Distancia por tramo | Aplicación típica
UTP cat. 5e | 1 Gb/s | 100 m | Instalaciones existentes
UTP cat. 6 | 1 Gb/s; 10 Gb/s en tramos reducidos | 100 m para 1 Gb/s; menor distancia para 10 Gb/s | Cableado horizontal con margen sobre Cat 5e
UTP cat. 6A | 10 Gb/s | 100 m | Instalaciones nuevas de 10GBASE-T
Coaxial | Según servicio | Cientos de metros | TV, antenas, cámaras
Fibra multimodo | 10 Gb/s o más | Cientos de metros | Troncales de edificio
Fibra monomodo | 10–100 Gb/s o más | Kilómetros | Operadores, larga distancia
[[/TABLA]]
## La fibra óptica
La fibra transmite pulsos de luz por un filamento de vidrio: inmune a las interferencias electromagnéticas, alcanza distancias de kilómetros y velocidades enormes. La multimodo cubre enlaces internos de edificios; la monomodo, las largas distancias de los operadores. Su costo y el equipamiento para empalmarla la reservan para troncales y enlaces entre edificios; el puesto de trabajo sigue siendo del UTP.
Mirá el corte de cada medio guiado: el par trenzado (cuatro pares de cobre), el coaxial (conductor, aislante y malla) y la fibra (vidrio que lleva luz). Abajo, qué velocidad garantiza cada categoría de UTP.
[[IMG T_image34.png|16.0]]
Figura 17.2 — Cortes del par trenzado, el coaxial y la fibra óptica.
[[CAJA En Paraguay — La fibra que cruza el país]]
La expansión de la fibra óptica cambió el mapa de la conectividad paraguaya: los operadores llevan fibra al hogar en las ciudades y la Red Troncal estatal, en modernización con COPACO y ANDE, extiende la capacidad hacia el interior. Sobre esos hilos de vidrio viaja hoy la mayor parte del tráfico nacional.
[[/CAJA]]
## Elegir el medio guiado: un criterio en tres preguntas
Para elegir el medio de un tramo, el técnico responde tres preguntas en orden. Primera: ¿qué distancia hay que cubrir? Si el canal supera los 100 metros, el par trenzado queda descartado para un tramo único. Segunda: ¿qué hay en el entorno? Motores, soldadoras, transformadores o cables de alta tensión cerca del recorrido aconsejan un cable apantallado o, mejor, fibra. Tercera: ¿qué velocidad hace falta hoy y en los próximos años? Para los puestos de un aula alcanza Gigabit; para el enlace entre edificios o entre switches conviene prever 10 Gb/s.
La fibra multimodo es la opción habitual entre edificios de un mismo predio; la monomodo, cuando las distancias crecen a kilómetros. En los dos casos se necesitan equipos con puertos o módulos de fibra en los extremos (por ejemplo, módulos SFP), que también se presupuestan.
[[CAJA Ejemplo — Unir la biblioteca con el edificio principal]]
El Instituto Ko'ẽju quiere conectar la biblioteca, que está en otro edificio del predio, con el rack principal. El recorrido medido por la canalización exterior es de 165 metros, y cerca del recorrido no hay fuentes de interferencia importantes.
Paso 1. Distancia: 165 m supera los 100 m del canal de par trenzado. Un único tramo de UTP no cumple la norma.
Paso 2. Alternativas: fibra multimodo entre los dos racks, o un switch intermedio a mitad de camino (lo que exige energía y un gabinete a la intemperie).
Paso 3. Velocidad: la fibra multimodo permite 10 Gb/s en ese largo, con margen para el futuro.
Paso 4. Decisión: fibra multimodo con un módulo SFP en cada switch, y documentación del tramo en la carpeta técnica.
[[/CAJA]]
Para el tramo exterior, además, se elige un cable apto para intemperie o se pasa por una cañería protegida: el sol y la humedad degradan la cubierta de un cable de interior en pocos años. Ese detalle también va en el presupuesto y en la carpeta técnica.
[[CAJA Errores frecuentes — Con los medios guiados]]
• Pensar que un cable más largo que 100 m «igual anda» y por lo tanto sirve.
• Usar cable UTP de exterior sin protección en recorridos al aire libre.
• Comprar fibra sin presupuestar los módulos o conversores de los extremos.
• Doblar la fibra o el UTP en ángulos cerrados al pasarlos por las canaletas.
[[/CAJA]]
## Actividades de aplicación
Marcá la opción correcta:
1. El trenzado de los pares del UTP sirve para:
    a) Endurecer el cable
    b) Cancelar interferencias
    c) Aumentar la distancia a kilómetros
    d) Transmitir luz
2. La categoría de UTP que sostiene 10 Gb/s en los 100 metros completos es la:
    a) 5e
    b) 6
    c) 6A
    d) 3
3. El medio inmune a las interferencias electromagnéticas es:
    a) El UTP
    b) El coaxial
    c) La fibra óptica
    d) El par telefónico
4. La fibra monomodo se aplica principalmente en:
    a) El puesto de trabajo
    b) Largas distancias de operadores
    c) Cables de impresora
    d) Redes en bus
Completá los espacios:
5. La sigla UTP indica par trenzado ________ blindaje.
6. El límite de distancia por tramo del par trenzado es de ________ metros.
7. La fibra ________ cubre los enlaces internos de un edificio.
Verdadero o falso (justificá las falsas):
8. (....) El coaxial es el medio recomendado para instalaciones de datos nuevas.
9. (....) La categoría 6 cuesta apenas más que la 5e y ofrece mejores márgenes.
10. (....) Conviene tender fibra óptica hasta cada puesto de trabajo de un aula.
Respondé y fundamentá:
11. Un taller metalúrgico con soldadoras quiere red cableada entre la oficina y el galpón. ¿Qué medio recomendás y por qué?
12. Justificá con dos argumentos por qué la categoría 6 es la elección estándar para una instalación nueva en 2026.
