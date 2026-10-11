@@H1 Práctica 13 — Redes por alcance: LAN, MAN y WAN
Nombre y Apellido: _______________________________  Curso: ______  Fecha: ____ / ____ / ____
Competencia de la práctica: Medir con ping y tracert cómo crecen la demora y los saltos al alejarse el destino.
Para esta práctica, tené a mano la Figura 13.1 de la Clase 13.
## Lo que necesitás saber
• ping mide la demora (en milisegundos) cuando el destino responde a ICMP; un tiempo de espera agotado no demuestra por sí solo que el sitio esté caído. tracert lista saltos de la ruta, pero algunos equipos pueden no responder y mostrar * sin que el tránsito esté interrumpido.
• Comparar un destino cercano (la puerta de enlace) con uno lejano muestra la diferencia LAN/WAN en números.
## Actividades
Actividad 1 — Objetivo: Medir la demora hacia la propia red y hacia internet.
[[CAJA Ejemplo — Modelo a reproducir]]
Registro: destino, demora promedio en ms. Destinos: la puerta de enlace (anotada en la Práctica 12) y un sitio nacional (por ejemplo mec.gov.py).
[[/CAJA]]
   1. Abrí el Símbolo del sistema (Windows + R → cmd).
   2. Escribí ping seguido de la dirección de tu puerta de enlace y presioná Enter.
   3. Anotá el tiempo promedio que informa el resumen final.
   4. Repetí con ping mec.gov.py. Si responde, anotá el promedio; si aparece «Tiempo de espera agotado» o equivalente, registrá «sin respuesta ICMP» y continuá.
   5. Compará los resultados: la puerta de enlace local suele tener demora baja. El destino remoto puede tardar más, pero no lo des por obligatorio; interpretá lo que realmente mediste.
Punto de control: Tenés registrados los dos resultados (promedio o «sin respuesta ICMP») y distinguís la medición local de la remota sin afirmar que un bloqueo de ICMP sea una caída del sitio.
Actividad 2 — Objetivo: Contar los saltos del camino con tracert y volcarlo a Excel.
[[CAJA Ejemplo — Modelo a reproducir]]
Tabla: Destino | Saltos | Demora promedio (ms) | ¿LAN o WAN? Filas: puerta de enlace y sitio nacional.
[[/CAJA]]
   1. En el cmd escribí tracert mec.gov.py y presioná Enter (puede tardar).
   2. Contá las líneas numeradas que aparezcan. Si una línea muestra *, anotala como «sin respuesta de ese salto»; no la marques automáticamente como enlace roto.
   3. Ejecutá tracert hacia tu puerta de enlace y contá los saltos; en una red local típica será 1.
   4. Cargá la tabla del modelo en Excel con los datos medidos.
   5. Guardá como Alcances_[apellido].xlsx.
Punto de control: La puerta de enlace se reconoce como destino local y el trazado remoto queda documentado con sus saltos y posibles *; la conclusión se basa en los datos observados.
[[CAJA Desafío final (si terminás antes)]]
Ejecutá tracert hacia un sitio alojado en otro continente, compará saltos y demora con el sitio nacional y escribí una conclusión de una línea.
[[/CAJA]]
