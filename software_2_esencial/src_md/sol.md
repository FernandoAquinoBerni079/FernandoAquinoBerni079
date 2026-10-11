## Presentación
Este solucionario es material exclusivo del docente. Contiene, con la misma numeración del libro del estudiante, las respuestas de las actividades de aplicación de las 20 clases, las orientaciones para corregir la prueba diagnóstica y las claves de las dos evaluaciones de unidad y de las dos integradoras de etapa, con el desarrollo de sus casos.
Incluye además, para cada una de las 20 prácticas y de las 12 fichas de profundización (A a L), el resultado esperado y los errores frecuentes que conviene vigilar durante la sesión, y cierra con la rúbrica analítica y las orientaciones del Proyecto Final Integrador. El libro del estudiante no contiene respuestas: los puntos de control de las prácticas permiten verificar el trabajo sin revelar el resultado.
Las capacidades de cada ficha se reproducen textualmente del programa del MEC; los indicadores de logro son operativizaciones observables. Cada pieza tiene sus propios datos para que las respuestas no se copien de los ejemplos: el aula, la secretaría, la biblioteca y otros ambientes del Instituto Ko'ẽju en las clases, la Farmacia Tajy en las Prácticas 14 a 19 y otros clientes en las evaluaciones. Todas las cifras se verificaron por cálculo antes de la edición. Los datos técnicos y regulatorios están actualizados a octubre de 2026 y deben volver a verificarse por modelo y fecha.
# Prueba diagnóstica — Orientaciones de corrección
• Consigna 1: se espera monitor/teclado/mouse/gabinete/impresora con función correcta; anticipa la Unidad 1 (el estudiante que solo nombra 'la CPU' para todo necesita refuerzo de vocabulario).
• Consigna 2: hardware = lo físico, software = los programas; una confusión acá pide reforzar la base antes de la clase 3.
• Consigna 3: bit < byte < megabyte < gigabyte; errores anticipan dificultades con capacidades de discos y memorias (clases 7-9).
• Consigna 4: Falso — es de salida; mide la noción de flujo de datos.
• Consigna 5: compartir recursos/información; cualquier ejemplo válido (Wi-Fi de la casa, impresora compartida) anticipa la Unidad 2.
• Consigna 6: releva experiencia previa real con redes; respuestas ricas (nombre de red, contraseña, router) permiten armar parejas de apoyo en las prácticas.
# Primera parte — Clases y prácticas
## Clase 1 — El gabinete de la computadora
Opción correcta: 1) b · 2) c · 3) c · 4) b
Completar: 5) gabinete · 6) factor / forma · 7) completa
V-F: 8) F — No procesa datos: aloja, protege y ventila los componentes que sí lo hacen. 9) V 10) F — Una mala ventilación eleva la temperatura interna y acorta la vida de todos los componentes.
11) Orientación: Debe mencionar la compatibilidad con la placa madre y la fuente; ejemplo válido: una placa ATX no entra en una torre mini que solo admite micro-ATX y mini-ITX.
12) Orientación: Torre mini/SFF o todo-en-uno; advertir la menor capacidad de ampliación y la importancia de la ventilación en espacios cerrados.
Práctica 1 — Resultado esperado: ficha de 2×6 (o 2×7 con el desafío) con datos coherentes con msinfo32. Errores frecuentes: confundir modelo del sistema con nombre del equipo en red; registrar la RAM en MB sin convertir a GB; abrir el gabinete (no corresponde en esta materia).
## Clase 2 — La fuente de alimentación
Opción correcta: 1) b · 2) c · 3) b · 4) a
Completar: 5) 220 · 6) VSB (standby) · 7) modular
V-F: 8) F — Una etiqueta comercial puede ser engañosa; 80 PLUS certifica eficiencia energética, no la potencia sostenida ni la calidad total de la fuente. Para validar la potencia se revisan especificaciones y ensayos confiables del modelo. 9) V 10) F — 12,4 V está dentro del rango 11,4–12,6 V (±5 %).
11) Orientación: Debe relacionar voltajes fuera de tolerancia, mala filtración de picos y potencia insuficiente con reinicios y daños en placa, discos y procesador.
12) Orientación: Menor desperdicio de energía y calor, con potencial reducción del consumo eléctrico. No otorgar puntaje a la afirmación «80 PLUS garantiza los watts»: la certificación evalúa eficiencia y no sustituye la verificación de potencia, protecciones y calidad del modelo.
Práctica 2 — Resultado esperado: tabla con rangos 11,40–12,60 / 4,75–5,25 / 3,14–3,47 / 4,75–5,25 calculados con fórmula; casos: 12,7 V en +12 → NO (supera 12,60); 4,9 V en +5 → SÍ; 3,1 V en +3,3 → NO (está por debajo de 3,14). Desafío: desvíos ≈ +5,8 %, −2,0 % y −6,1 %. Errores frecuentes: usar coma/punto decimal inconsistente; escribir los rangos a mano en vez de con fórmula; comparar la medición con el nominal y no con el rango.
## Clase 3 — La placa madre
Opción correcta: 1) b · 2) c · 3) c · 4) b
Completar: 5) buses · 6) DIMM · 7) chipset
V-F: 8) F — Cada placa admite solo la familia de procesadores compatible con su zócalo y chipset. 9) V 10) V
11) Orientación: Porque define el procesador (zócalo), la memoria (tipo y cantidad de ranuras), el almacenamiento (SATA/M.2) y el gabinete (factor de forma). Dos ejemplos cualesquiera bien fundados.
12) Orientación: Compatibilidad de zócalo/chipset con el procesador previsto y disponibilidad de soporte/repuestos; también ranuras suficientes para la memoria y el disco planeados.
Práctica 3 — Resultado esperado: mapa con cinco dispositivos reales coherentes con el equipo y datos de placa/BIOS correctos. Errores frecuentes: copiar el nombre de la categoría en vez del dispositivo; confundir el adaptador de red cableado con el inalámbrico.
## Clase 4 — Slots de expansión
Opción correcta: 1) b · 2) c · 3) b · 4) b
Completar: 5) PCI / Express · 6) carril (lane) · 7) apagado
V-F: 8) F — Las generaciones son compatibles: funciona, pero a la velocidad de la ranura más vieja. 9) V 10) V
11) Orientación: Debe relacionar el volumen de datos gráficos (resolución, cuadros por segundo) con el ancho de banda: 16 carriles en paralelo frente al carril único que le alcanza al sonido.
12) Orientación: Tarjeta mal asentada (seguro sin encastrar), ranura o contactos sucios, falta del conector de energía adicional de la tarjeta; dos causas razonables valen.
Práctica 4 — Resultado esperado: PCIe 3.0 → 1 / 2 / 8 / 16 GB/s y PCIe 5.0 → 4 / 8 / 32 / 64 GB/s para x1, x2, x8 y x16, con fórmulas que usan referencias absolutas ($F$1, $F$2); gráfico de columnas agrupadas con las dos series; adaptadores del equipo bien identificados. Desafío: PCIe 4.0 → 2 / 4 / 16 / 32 GB/s; la 4.0 necesita la mitad de carriles que la 3.0 para el mismo ancho de banda. Errores frecuentes: escribir los totales a mano; olvidar los signos $ al arrastrar la fórmula.
## Clase 5 — Puertos de conexión
Opción correcta: 1) b · 2) c · 3) a · 4) b
Completar: 5) VGA · 6) Universal · 7) salida
V-F: 8) V 9) F — USB 2.0 llega a 480 Mb/s; USB 3.2 va de 5 a 20 Gb/s: es mucho más rápido. 10) F — Se parecen, pero el RJ-45 es más ancho y tiene 8 contactos.
11) Orientación: Adaptador/conversor activo VGA a HDMI, agregar una tarjeta de video con HDMI, o renovar el equipo; debe comparar costo y limitaciones.
12) Orientación: Estabilidad y menor latencia del medio cableado, menos interferencias y cortes; el Wi-Fi se reserva para donde no llega el cable.
Práctica 5 — Resultado esperado: inventario coherente con el equipo del laboratorio (típico: USB-A frontales y traseros, HDMI o VGA, RJ-45, jacks de audio) y TOTAL con =SUMA. Errores frecuentes: contar dos veces los puertos ocupados; escribir el total a mano.
## Clase 6 — El microprocesador
Opción correcta: 1) b · 2) b · 3) c · 4) b
Completar: 5) central / proceso · 6) gigahertz · 7) TDP
V-F: 8) F — El rendimiento depende también de núcleos, generación y caché; un chip nuevo a menos GHz puede rendir más. 9) V 10) F — Se sobrecalienta en segundos: el disipador con pasta térmica es obligatorio.
11) Orientación: Subir GHz indefinidamente genera calor y consumo inmanejables; varios núcleos reparten tareas en paralelo y rinden más con menos calor.
12) Orientación: Gama media actual (4-6 núcleos), justificando por núcleos/hilos para multitarea y generación reciente; frecuencia y caché como apoyo.
Práctica 6 — Resultado esperado: datos del equipo coherentes con el Administrador de tareas y comparativa con G./núcleo calculado por fórmula. Errores frecuentes: confundir procesadores lógicos con núcleos; dividir precio entre hilos en vez de núcleos sin aclararlo.
## Clase 7 — Las memorias
Opción correcta: 1) c · 2) b · 3) b · 4) b
Completar: 5) caché · 6) SO · 7) firmware (UEFI/BIOS)
V-F: 8) V 9) F — Es al revés: la jerarquía es más rápida cuanto más cerca de la CPU (caché > RAM > almacenamiento). 10) V
11) Orientación: La RAM se llena y el sistema recurre al almacenamiento (mucho más lento) como memoria auxiliar; la solución razonable es ampliar RAM verificando tipo, ranuras y máximo de la placa.
12) Orientación: Ventaja: doble canal (casi duplica el ancho de banda). Desventaja: ocupa ambas ranuras y una ampliación futura obliga a reemplazar módulos.
Práctica 7 — Resultado esperado: lectura coherente con el equipo (capacidad, uso, velocidad y ranuras) y presupuesto con =SUMA y moneda en guaraníes. La compatibilidad del módulo debe justificarse con fabricante/modelo del equipo o placa y su especificación de memoria; la velocidad observada no basta para identificar DDR3/DDR4/DDR5. Errores frecuentes: confundir Disponible con Total; inferir la generación DDR solo por MHz/MT/s; proponer un módulo incompatible.
## Clase 8 — Almacenamiento: discos duros y SSD
Opción correcta: 1) b · 2) b · 3) b · 4) b
Completar: 5) 7.200 · 6) flash · 7) HDD
V-F: 8) F — Es al revés: al no tener partes móviles, el SSD resiste mejor los golpes. 9) V 10) F — Es memoria permanente: conserva los datos sin energía; la que se borra es la RAM.
11) Orientación: SSD (NVMe) para sistema y programas + HDD de gran capacidad para el archivo histórico; puede sumar respaldo externo. Justificar velocidad/costo por GB.
12) Orientación: El almacenamiento es el eslabón lento de la jerarquía: si tarda en entregar datos, la CPU espera; el arranque y la carga de programas dependen de él.
Práctica 8 — Resultado esperado: tabla coherente con el equipo; el tipo de medio debe coincidir con lo que informa el Optimizador. Errores frecuentes: confundir espacio usado con libre; ejecutar Optimizar en vez de Analizar sin indicación del docente.
## Clase 9 — Lectoras de CD, DVD y Blu-ray
Opción correcta: 1) b · 2) c · 3) c · 4) b
Completar: 5) azul · 6) R · 7) 150
V-F: 8) F — La 'x' no se compara entre formatos: DVD 16x ≈ 22,2 MB/s supera a CD 52x ≈ 7,8 MB/s. 9) V 10) F — Se registra como marcas físicas que un láser lee; lo magnético es el disco duro.
11) Orientación: 1) Leerlos con unidad (externa USB) verificando cada disco; 2) migrar el contenido a almacenamiento moderno con estructura de carpetas y respaldo; 3) verificar la copia y recomendar política de respaldo futura.
12) Orientación: Marcas más pequeñas y pistas más juntas caben en la misma superficie: más datos por disco (CD→DVD→Blu-ray).
Práctica 9 — Resultado esperado (61 GB en H1, unidades decimales): CD 88 discos y ≈ 2,2 h; DVD 13 discos y ≈ 0,8 h; Blu-ray 3 discos y ≈ 0,5 h, con REDONDEAR.MAS y referencias absolutas a $H$1; al cambiar H1 todo se recalcula. Diapositiva con la tabla pegada. Errores frecuentes: escribir el tamaño dentro de cada fórmula en lugar de referenciar H1; mezclar GB decimales con el factor 1.024; redondear discos hacia abajo.
## Clase 10 — Impresoras
Opción correcta: 1) c · 2) b · 3) b · 4) b
Completar: 5) dpi · 6) multifunción · 7) térmica
V-F: 8) F — El costo real está en los insumos: se compara el costo por página y el ciclo mensual. 9) V 10) F — No usa tinta: imprime por calor sobre papel térmico.
11) Orientación: Térmica para tickets (velocidad, sin tinta) + matriz de punto para el papel químico autocopiativo; justificar por insumo y uso.
12) Orientación: Ejemplo válido: cartucho de G. 250.000 que rinde 200 páginas = G. 1.250/pág. contra tóner de G. 600.000 que rinde 3.000 = G. 200/pág.
Práctica 10 — Resultado esperado: costo por página G. 700 (inyección) vs. G. 200 (láser); costo mensual de 1.200 páginas G. 840.000 vs. G. 240.000; la láser conviene. Desafío: recupera la diferencia de equipos en 800.000 ÷ 600.000 ≈ 1,3 meses. Errores frecuentes: invertir la división del costo por página; olvidar el formato de moneda.
## Clase 11 — La red de computadoras
Opción correcta: 1) b · 2) b · 3) b · 4) b
Completar: 5) pares · 6) medio · 7) cliente / servidor
V-F: 8) F — Sin protocolo común no hay comunicación posible: el protocolo es constitutivo de la red. 9) V 10) F — También comparten archivos, impresoras y respaldos dentro de la propia red local.
11) Orientación: Compartir una sola impresora, carpeta común/respaldo centralizado, administración y cobro centralizados, una única salida a internet controlada; tres cualesquiera bien explicados.
12) Orientación: Administración y seguridad centralizadas, control de usuarios y permisos, respaldo único, escala mejor con muchos equipos.
Práctica 11 — Resultado esperado: tabla coherente con la red real del laboratorio y párrafo con recursos compartidos verificables. Errores frecuentes: confundir el nombre del equipo con el nombre de la red; escribir 'internet' como único recurso compartido.
## Clase 12 — Protocolos y estándares
Opción correcta: 1) b · 2) a · 3) b · 4) b
Completar: 5) DHCP · 6) máscara · 7) cifrada
V-F: 8) V 9) F — Son privadas: se usan dentro de redes locales y el router las traduce hacia afuera. 10) F — Para entrega completa y en orden corresponde TCP; UDP sirve donde la velocidad importa más que la garantía.
11) Orientación: DNS traduce el nombre a IP; IP encamina los paquetes; TCP asegura la entrega; HTTP/HTTPS transporta el contenido (HTTPS cifrado). Secuencia coherente con tres o más protocolos.
12) Orientación: Si la IP cambia, los equipos que la tienen configurada la 'pierden'; una dirección fija garantiza que siempre se la encuentre en el mismo lugar.
Práctica 12 — Resultado esperado: cinco datos coherentes e interpretaciones correctas. La pertenencia a la misma red se justifica usando IP + máscara; solo con 255.255.255.0 (/24) es válido comprobar que coincidan los tres primeros octetos. Errores frecuentes: leer el adaptador inactivo o virtual; confundir DNS con puerta de enlace; aplicar el atajo de /24 a cualquier máscara. Desafío: nslookup usa DNS. Si el equipo muestra una dirección 169.254.x.x (enlace local) o no tiene IPv4, el resultado correcto es registrar la anomalía y avisar al docente, sin modificar la configuración.
## Clase 13 — Redes por alcance: LAN, MAN y WAN
Opción correcta: 1) b · 2) c · 3) b · 4) b
Completar: 5) local · 6) PAN · 7) telecomunicaciones
V-F: 8) V — En general sí, por las distancias cortas y el medio propio; una medición real depende también de la carga y del equipo. 9) V 10) F — Los enlaces WAN pertenecen a los operadores: se contratan, no se administran en propiedad.
11) Orientación: LAN del aula → router/salida contratada → WAN del proveedor y enlaces internacionales (troncales/submarinos) → LAN o red del centro de datos destino.
12) Orientación: Una MAN; contrataría los enlaces de fibra (u otro medio) entre los edificios, manteniendo cada sucursal su LAN propia.
Práctica 13 — Resultado esperado: puerta de enlace reconocida como destino local (habitualmente 1 salto y demora baja) y trazado remoto documentado con los valores realmente observados. Si ping no recibe respuesta, registrar «sin respuesta ICMP»; no concluir que el sitio está caído. En tracert, * significa que ese salto no respondió a esa sonda, no necesariamente que el enlace esté roto. La latencia remota suele ser mayor, pero no es una regla absoluta. Error frecuente: convertir valores típicos en resultados obligatorios.
## Clase 14 — Topologías de red
Opción correcta: 1) c · 2) b · 3) a · 4) b
Completar: 5) bus · 6) árbol · 7) único
V-F: 8) V 9) F — Pueden diferir: una red cableada en estrella con un hub en el centro se comporta lógicamente como un bus. 10) F — Es la más cara en cableado y puertos; se reserva para enlaces críticos que exigen redundancia.
11) Orientación: Bus: (a) puede afectar al troncal según el corte, (b) el corte del troncal tumba todo. Estrella: (a) cae solo esa estación, (b) la caída del switch tumba todo. Conclusión: la estrella aísla fallas de estación.
12) Orientación: En el centro: switch de calidad (o segundo switch/puertos de reserva) y protección eléctrica del rack, porque su caída afecta a toda la red; los cables individuales solo afectan a un equipo.
Práctica 14 — Resultado esperado: estrella de la Farmacia Tajy con el switch en el centro, Caja-1 a Caja-4, Depósito, Administración, Impresora y Access point unidos al switch, y el Router arriba; todos con Conector recto anclado. El punto único de falla resaltado es el switch (si cae, ningún puesto se comunica); la caída del router solo corta internet. En el desafío, el switch del depósito cuelga del switch principal y forma un árbol. Errores frecuentes: usar Línea en vez de Conector recto; señalar el router como único punto de falla de la red local.
## Clase 15 — Equipos de red
Opción correcta: 1) b · 2) c · 3) b · 4) b
Completar: 5) de velocidad · 6) DHCP · 7) ONT
V-F: 8) V 9) F — Ese es el rol del router; el switch conmuta dentro de la propia red local. 10) V
11) Orientación: El switch es el portero que entrega sobres entre oficinas del edificio (LAN); el router es la oficina de correos que decide cómo enviar lo que va a otros edificios (otras redes).
12) Orientación: Access point cableado hasta el depósito (mejor rendimiento, requiere cable) vs. repetidor a mitad de camino (fácil, pero reduce el ancho de banda); elegir según posibilidad de cablear.
Práctica 15 — Resultado esperado: bocas ocupadas 6 PC + impresora + access point + enlace al router = 9; con 20 % de reserva, 9 × 1,2 = 10,8 → 11; el de 8 puertos se descarta. Se espera elegir el de 16 puertos con PoE, porque el access point del techo se alimenta por el cable; se acepta el de 16 sin PoE si se presupuesta un inyector. Desafío: con dos cajas más, 11 × 1,2 = 13,2 → 14 puertos: el switch de 16 sigue sirviendo. Errores frecuentes: olvidar el access point o el enlace al router; ignorar la alimentación del access point.
## Clase 16 — Materiales de red
Opción correcta: 1) b · 2) b · 3) b · 4) b
Completar: 5) 305 · 6) cords · 7) rack
V-F: 8) F — Cables, conectores y remates de mala calidad producen fallas intermitentes difíciles de diagnosticar. 9) V 10) F — Se diseña para durar años sin tocarse; los cambios se hacen sobre los patch cords.
11) Orientación: El tendido fijo queda protegido y estable; los extremos reemplazables (cordones) absorben el desgaste; los cambios y diagnósticos se hacen en el rack sin tocar paredes.
12) Orientación: 5 rosetas/jacks, patch panel (8+ bocas), 11 patch cords (5 × 2 + 1 enlace switch↔router), cable UTP según distancias, canaletas, rack chico, etiquetas; cantidades coherentes con 5 puntos.
Práctica 16 — Resultado esperado: cable 7 + 11 + 14 + 19 + 23 + 28 + 41 + 52 = 195 m; con 10 %, ≈ 214,5 m → 1 caja de 305 m; 8 rosetas con jack; patch panel de al menos 8 bocas (12 o 16 con reserva); patch cords 8 × 2 + 1 = 17; switch con 9 puertos ocupados. Subtotales y total por fórmula. Errores frecuentes: contar un solo patch cord por punto; olvidar el enlace switch–router; escribir el total a mano.
## Clase 17 — Medios de transmisión guiados
Opción correcta: 1) b · 2) c · 3) c · 4) b
Completar: 5) sin · 6) 100 · 7) multimodo
V-F: 8) F — Ya no se instala en redes de datos nuevas; quedó para TV, antenas y cámaras analógicas. 9) V 10) F — El costo no se justifica: el UTP resuelve el puesto; la fibra se reserva para troncales y enlaces largos.
11) Orientación: Fibra óptica (o al menos par blindado FTP/STP en tramos cortos): la soldadura genera interferencia electromagnética intensa y la fibra es inmune; el UTP común sufriría errores.
12) Orientación: Margen de prestaciones (1 Gb/s holgado, 10 Gb/s en tramos cortos) por una diferencia de precio menor, y vida útil: el cableado fijo dura años y recablear cuesta más que la diferencia de categoría.
Práctica 17 — Resultado esperado: (1) consultorio a 45 m → UTP cat. 6; (2) lavandería con motores a 70 m → fibra o par trenzado apantallado, por la interferencia; (3) sucursales a 230 m → fibra (supera los 100 m); (4) cámaras analógicas existentes → mantener el coaxial. La fórmula marca SÍ solo en el escenario 3. Errores frecuentes: elegir UTP para 230 m; blindar sin una fuente de interferencia que lo justifique.
## Clase 18 — Medios de transmisión no guiados
Opción correcta: 1) a · 2) c · 3) b · 4) b
Completar: 5) 11 · 6) 7 · 7) espectro
V-F: 8) F — No hay una regla absoluta: el rendimiento depende también del estándar Wi-Fi, el ancho de canal, la interferencia, la distancia y el equipo cliente; 5 GHz suele ofrecer más capacidad, pero menos alcance. 9) F — Es limitado: el Estado lo administra, con bandas de uso libre regulado y bandas licitadas. 10) F — La complementa: su rol es llegar donde la infraestructura terrestre no llega.
11) Orientación: Satélite LEO; advertir costo del servicio/equipo y sensibilidad al clima (además de depender de un único proveedor).
12) Orientación: El cable garantiza velocidad estable por puesto; el aire se comparte y sufre interferencias; el Wi-Fi sirve a los dispositivos móviles mientras las terminales fijas van cableadas.
Práctica 18 — Resultado esperado: cinco redes con SSID, canal y seguridad; la banda se registra solo si el sistema o el listado de referencia la informa de forma verificable. Si no aparece, escribir «no determinada»: el número de canal por sí solo no distingue siempre 2,4/5/6 GHz en equipos modernos. La recomendación debe considerar congestión, alcance y compatibilidad. Errores frecuentes: inferir banda solo por canal; confundir canal con intensidad de señal.
## Clase 19 — Cableado estructurado
Opción correcta: 1) b · 2) a · 3) b · 4) b
Completar: 5) canal · 6) 90 · 7) certificación
V-F: 8) F — La norma garantiza prestaciones: superar los 100 m degrada la señal aunque haya enlace. 9) V 10) F — Une pisos el backbone o cableado vertical; el área de trabajo es la roseta y el cordón del usuario.
11) Orientación: Explicar que el panel protege el tendido fijo, ordena, permite cambios sin tocar paredes y es requisito de una instalación normalizada; el 'ahorro' se paga en cada mantenimiento.
12) Orientación: Al cliente le garantiza las prestaciones contratadas por enlace; al instalador le documenta que entregó según norma, deslindando fallas futuras ajenas a la instalación.
Práctica 19 — Resultado esperado: canales de 14, 17, 22, 25, 30, 36, 48 y 60 m, todos SÍ; el punto de prueba (93 m fijos, 98 m de canal) marca NO porque supera los 90 m de tendido fijo, aunque el canal no llegue a 100 m. Desafío: el menor margen es el del punto de 55 m (100 − 60 = 40 m). Errores frecuentes: verificar solo el canal y olvidar el límite del tendido fijo; aplicar el formato condicional a toda la hoja.
## Clase 20 — CONATEL y el marco regulatorio
Opción correcta: 1) b · 2) a · 3) b · 4) b
Completar: 5) Telecomunicaciones · 6) Frecuencias · 7) homologación
V-F: 8) V 9) F — Son de uso libre regulado: tienen reglas de potencia y los equipos deben estar homologados. 10) F — Corresponde a CONATEL como ente regulador; los operadores son los fiscalizados.
11) Orientación: Es un recurso limitado y compartido: sin ordenamiento, las transmisiones se interferirían entre sí (ejemplo: dos radios en la misma frecuencia, potencias excesivas en canales Wi-Fi); el Plan de Frecuencias y la fiscalización lo evitan.
12) Orientación: Plano de topología, plan de direcciones IP, lista de equipos y materiales con presupuesto, verificación de canales (100 m) y consideraciones regulatorias (homologación/Wi-Fi); acepta orden libre.
Práctica 20 — Resultado esperado: ficha de CONATEL con la misión citada textual, fuente y fecha de consulta; informe técnico de la Farmacia Tajy con sus seis secciones (topología de la Práctica 14, switch de la 15, materiales de la 16, canales de la 19, plan de direcciones y marco regulatorio), resumen de riesgos y conclusión. El plan de direcciones es propio de la farmacia; por ejemplo, red 10.20.5.0/24, puerta de enlace 10.20.5.1, impresora fija 10.20.5.30 y DHCP de 10.20.5.100 a 10.20.5.199 (se acepta cualquier red privada coherente, con la impresora fuera del rango del DHCP). Errores frecuentes: pegar la configuración del equipo del laboratorio como si fuera la de la farmacia; mezclar datos del Instituto Ko'ẽju; parafrasear la misión sin comillas ni fuente.
# Segunda parte — Evaluaciones
## Evaluación de la Unidad 1 — Componentes básicos de una computadora
Opción correcta: 1) b · 2) b · 3) b · 4) c · 5) b · 6) c
Completar: 7) 5 · 8) DIMM · 9) M.2 · 10) rendimiento (en páginas)
V-F: 11) V 12) F — Es al revés: el SSD no tiene partes móviles y resiste mejor. 13) V 14) F — Usa tóner; la tinta líquida corresponde a la inyección.
15) Orientación: Debe interpretar: placa mini-ITX (equipo compacto, pocas ranuras para ampliar); 8 núcleos/16 hilos, holgado para tareas administrativas; 1 × 16 GB DDR5: capacidad suficiente, pero con un solo módulo no hay doble canal (sería mejor 2 × 8 GB); SSD SATA de 1 TB: mucha capacidad y arranque rápido frente a un HDD, aunque menos veloz que un NVMe; fuente 450 W 80 Plus Bronze: eficiencia certificada y potencia suficiente para un equipo sin tarjeta de video, a confirmar en la especificación. Valorar la interpretación, no la repetición.
16) Orientación: Costo real = equipo + insumos en el tiempo; con volumen mensual, el menor costo por página (tóner de alto rendimiento) recupera la diferencia inicial; se espera un razonamiento numérico aunque sea aproximado.
## Evaluación integradora de la 1.ª etapa
Opción correcta: 1) b · 2) b · 3) b · 4) b · 5) c
Completar: 6) chipset · 7) hilos · 8) caché
V-F: 9) V 10) F — Cada formato tiene su propia base: DVD 16x supera a CD 52x. 11) V
Desarrollo del caso: a) 280.000 + 390.000 + 720.000 + 1.150.000 + 480.000 + 430.000 = G. 3.450.000. b) 3.450.000 × 10 = G. 34.500.000. c) No conviene: se pierde el doble canal (cae el ancho de banda de memoria) y 8 GB dejan sin margen la multitarea del aula; el ahorro se paga en rendimiento. d) Ejemplos válidos: placa micro-ATX ↔ gabinete torre media (factor de forma), procesador ↔ zócalo/chipset de la placa, DDR4 ↔ ranuras DIMM del tipo correcto, NVMe ↔ conector M.2 disponible.
## Evaluación de la Unidad 2 — Redes de computadoras
Opción correcta: 1) b · 2) c · 3) c · 4) b · 5) b · 6) c
Completar: 7) DHCP · 8) patch cords (cordones) · 9) CONATEL · 10) T568B
V-F: 11) V 12) F — No existe una regla absoluta «5 GHz = más velocidad». En general 2,4 GHz propaga más lejos y 5 GHz ofrece más capacidad/canales, pero el rendimiento depende también del estándar, ancho de canal, interferencia, MIMO, distancia y cliente. 13) F — Esa es la función del router/gateway; el switch conmuta dentro de la LAN. 14) V
15) Orientación: ONT (adapta la fibra del proveedor), router (puerta de enlace, DHCP, firewall), switch de 8 puertos o más (5 puestos + access point + enlace al router = 7 bocas, más reserva), access point (Wi-Fi de pacientes, separado de la red de trabajo si es posible); valorar funciones correctas y dimensionamiento.
16) Orientación: El canal incluye los cordones de ambos extremos (90 + 10); superarlo degrada la señal y las prestaciones de la categoría aunque el enlace 'funcione': fallas intermitentes y velocidad inferior a la contratada.
## Evaluación integradora de la 2.ª etapa
Opción correcta: 1) b · 2) b · 3) c · 4) b · 5) c
Completar: 6) redes · 7) Wi-Fi · 8) backbone
V-F: 9) V — Es uno de los tres rangos privados de la RFC 1918 (10.0.0.0/8, 172.16.0.0/12 y 192.168.0.0/16). 10) V 11) F — No se mezclan al azar: en cada enlace directo los dos extremos se terminan con el mismo esquema, y conviene usar y documentar un esquema uniforme en toda la instalación.
Desarrollo del caso: a) Con la ampliación: 13 PC + impresora + 2 access points + enlace al router = 17 bocas; el switch de 16 no alcanza. Soluciones válidas: reemplazarlo por uno de 24 puertos (recomendable, con reserva) o sumar un segundo switch unido al primero. b) Canal = 47 + 3 + 2 = 52 m: el tendido fijo (47 m) no supera 90 m y el canal no supera 100 m; cumple, con 48 m de margen. c) Actuó DHCP; con ipconfig se ve que los tres primeros números (192.168.10) coinciden con los de la impresora (192.168.10.20) bajo la máscara 255.255.255.0; se confirma con ping 192.168.10.20. d) Se elige el modelo homologado; se verifica en el sitio oficial de CONATEL con el modelo exacto y se registra en la carpeta técnica el modelo, la referencia consultada y la fecha de consulta.
# Tercera parte — Fichas de profundización A–L
Estas claves son orientativas pero técnicas: cuando una decisión depende de una ficha de fabricante, el estudiante debe citar la evidencia utilizada.
## Ficha A — Compatibilidad gabinete · placa madre · fuente
Debe comprobarse factor de forma de placa y gabinete, formato/espacio de la fuente, conectores y potencia requerida. Una decisión sin especificación no se considera verificada.
## Ficha B — PCIe y M.2: formato, generación y carriles
Separar siempre «formato» de «interfaz». PCIe: indicar generación + carriles; M.2: indicar si el zócalo/módulo soporta SATA o PCIe/NVMe y la key correspondiente. Entrar físicamente no demuestra compatibilidad funcional.
## Ficha C — USB-C no es una velocidad
Respuesta esperada: USB-C solo identifica el conector reversible. La velocidad y funciones dependen del estándar/controlador/cable; se acepta «no indicado» cuando la ficha del fabricante no lo declara.
## Ficha D — CPU, RAM y placa: cadena de compatibilidad
La propuesta debe citar zócalo/chipset/BIOS cuando corresponda, tipo DDR, capacidad máxima y ranuras. No aceptar inferencias del tipo «3200 = DDR4» sin identificación del modelo o especificación.
## Ficha E — Almacenamiento y migración segura
1 TB al 55 % ≈ 550 GB de datos. Con al menos 20 % libre, el mínimo es 550 ÷ 0,80 = 687,5 GB (se acepta 688 GB o más); 660 GB no cumple (110 ÷ 660 ≈ 16,7 % libre). Los SSD de 1 TB cumplen; SATA o NVMe según la compatibilidad dada. Debe existir respaldo, copia, verificación y conservación temporal del origen antes de borrar/reutilizar.
## Ficha F — Costo total de impresión
Costo/página = costo del insumo ÷ rendimiento. Costo anual aproximado = equipo + consumibles necesarios para el volumen anual (+ mantenimiento si el caso lo da). La recomendación debe usar costo total y volumen.
## Ficha G — Diagnóstico IP paso a paso
Si hay ping a una IP pública pero falla un nombre, la conectividad IP existe y el problema probable es resolución DNS/configuración DNS. No modificar parámetros sin autorización.
## Ficha H — Topologías modernas y dominios de falla
Cable de una PC: cae esa estación. Switch: cae la LAN conectada a él. Enlace al router: la LAN local puede seguir funcionando pero se pierde acceso a otras redes/internet. El hub histórico sí comparte medio; el switch moderno no se comporta como bus lógico compartido normal.
## Ficha I — Dimensionamiento y BOM de una red pequeña
Para 12 PC + impresora + 2 AP + uplink = 16 puertos ocupados; con reserva, un switch de 24 puertos es una elección típica. Se aceptan otras topologías si la cuenta y la justificación son correctas.
## Ficha J — Cat 6, Cat 6A y T568: especificar sin simplificar
Aula 1 Gb/s: Cat 6 es suficiente (Cat 5e también puede cumplir, pero Cat 6 ofrece margen). 10 Gb/s a 90 m: elegir Cat 6A. T568A/T568B se documenta; mismo esquema en ambos extremos para un enlace directo convencional. Un certificador mide parámetros de desempeño, no solo continuidad/orden.
## Ficha K — Wi-Fi: cobertura, rendimiento y seguridad
La respuesta debe considerar cobertura, interferencia, generación Wi‑Fi, ancho de canal, clientes y seguridad. WPA2/WPA3 según compatibilidad. No aceptar «6 GHz es siempre más rápido» sin condiciones.
## Ficha L — CONATEL y expediente técnico verificable
Cada afirmación regulatoria debe incluir fuente oficial y fecha. Ejemplo verificable: CONATEL comunicó el lanzamiento oficial de 5G el 18/12/2025; sus registros posteriores deben consultarse por fecha antes de afirmar operadores o bandas vigentes. Paso 6 (resumen ejecutivo): una página con necesidad, solución, verificaciones, costo y riesgos, que permita decidir sin leer los anexos.
# Proyecto Final Integrador — Rúbrica analítica y orientaciones
Rúbrica analítica de evaluación (los pesos suman 100 %). Cada criterio se califica en uno de cuatro niveles: Logrado, 100 % del peso; En proceso, 60 %; Inicial, 30 %; No presentado, 0 %. Cada descriptor dice qué evidencia observable corresponde al nivel.
[[TABLA]]
Criterio (peso) | Logrado (100 %) | En proceso (60 %) | Inicial (30 %) | No presentado (0 %)
Ficha técnica y plano completos y verificables (25 %) | 25 pts. Ficha del equipo con cada componente justificado por su función y presupuesto con fórmulas; plano con topología, direcciones, materiales y canales verificados. | 15 pts. Ficha y plano completos, pero falta justificar dos o tres decisiones o alguna verificación. | 7,5 pts. Falta una de las dos piezas o la mitad de las verificaciones. | 0 pts. No entrega ficha ni plano.
Aplicación de los contenidos del año (25 %) | 25 pts. Aplica correctamente compatibilidad de componentes, dimensionamiento de switch, regla de los 100 metros y homologación, con cálculos sin errores. | 15 pts. Aplica la mayoría de los criterios; hay un error de cálculo o un criterio sin aplicar. | 7,5 pts. Aplica pocos criterios o con errores que cambian la decisión. | 0 pts. No hay evidencia de aplicación.
Integración interdisciplinaria (20 %) | 20 pts. Los puestos, equipos y red coinciden con el sistema de las otras materias (algoritmo, base de datos, presupuesto). | 12 pts. La integración existe, pero hay una incoherencia menor (por ejemplo, un puesto de más o de menos). | 6 pts. La especificación no se relaciona con el sistema de las otras materias. | 0 pts. No hay integración.
Presentación en la feria (15 %) | 15 pts. Explica con claridad el plano y la ficha, responde preguntas técnicas y usa vocabulario preciso. | 9 pts. Explica con claridad, pero duda en las preguntas técnicas. | 4,5 pts. Lee sin explicar o confunde conceptos. | 0 pts. No presenta.
Trabajo en equipo (15 %) | 15 pts. Roles definidos y cumplidos; cada integrante explica su aporte; registro de avances completo. | 9 pts. Roles definidos, pero el aporte es desparejo. | 4,5 pts. El trabajo recae en uno o dos integrantes. | 0 pts. No hay evidencia de trabajo en equipo.
[[/TABLA]]
Puntaje total: suma de los cinco criterios (máximo 100 puntos).
### Orientaciones
• Lanzar el proyecto al inicio de la 2.ª etapa, cuando la Unidad 2 arranca: cada práctica de la unidad produce una pieza reutilizable del proyecto.
• Coordinar con los docentes de Algorítmica, Laboratorio, Hardware y Matemática para que todos los equipos trabajen el mismo emprendimiento por equipo.
• Exigir coherencia transversal: los puestos del plano de red deben coincidir con los del presupuesto y con los del sistema que presentan las otras materias.
• En la ficha técnica, valorar la justificación de cada componente por su función en el sistema (por ejemplo, impresora térmica para los tickets), no la potencia porque sí.
• La verificación de homologación puede documentarse con una captura o cita del sitio de CONATEL con fecha de consulta.
