# Fuentes curriculares de las capacidades — DPS 7.º, 8.º y 9.º

Edición única adoptada para los tres grados: **Ministerio de Educación y Cultura (2014), Programa de Estudio: Desarrollo Personal y Social, Educación Escolar Básica.**

- Ficha de catalogación en la pág. 2. Autoridades: presidente Horacio Cartes, ministra Marta Lafuente.
- No se usa la edición anterior (autoridades Fernando Lugo / Luis A. Riart), que trae otras formulaciones.

Las copias están en esta carpeta.

| Grado | Archivo | SHA-256 | Págs. de «Capacidades para el … grado» | Cotejo |
|---|---|---|---|---|
| 7.º | `programa_DPS_7mo_MEC.pdf` (91 págs.). Copia de Drive `1EkkOgUbux0RQPwkw4GYGnUeDpb8_UldE` | `5b190e079c868cb0b894845c5ba6cc64b8783e8af85b4217d03bd5df0fb4ebe1` | 54-57 | 18 de 18 literales |
| 8.º | `programa_DPS_8vo_MEC_2014.pdf` (88 págs.). Copia de Drive `1kM6g3-Q-TYlzvEgJWak3ue-Ca7DUT2dB` | `574b24cf1bdebce316a8ac522e6ca469033d892a09508c69ef1dfba98523fbaf` | 54-56 | 20 de 20 literales, sin cambios |
| 9.º | `programa_DPS_9no_MEC_2014.pdf` (89 págs.). Copia de Drive `13I1buLKOknArJHMgxZ0ZOQGsmhitIdAI` | `4be02caec618229afebe7c91f779fc9fb9a80e046148c97a7d1cd002ceb7ba60` | 53-55 | 13 de 13 literales, tras corregir 4 (ver abajo) |

`programa_DPS_8vo_MEC_extracto_pags53-56.pdf` es el extracto que se usó primero en 8.º. Coincide con las mismas páginas del programa completo.

## Cómo se verifica

- **Control automático.** `edicion/verificar.py` comprueba, para cada grado, que cada capacidad de `edicion/config_grados.py` figure textualmente en las páginas indicadas del PDF. Al unir páginas quita el número de página, porque algunas capacidades quedan partidas entre dos páginas.
- **Resultado.** Ese control da 0 fallos en los tres grados (`verificacion/<grado>/CONTROLES.md`).
- **Otras citas del MEC.** El propósito del componente PEC y la frase «conforme necesidades entre Orientación y Proyecto Educativo Comunitario» figuran también textualmente en los programas de 8.º y 9.º.

## Correcciones de 9.º (cotejo con la edición 2014)

| N.º | Antes | Programa MEC 2014 (pág.) |
|---|---|---|
| 4 | «…para la acertada elección del Bachillerato.» | «…para la acertada elección del Bachillerato (ofertas educativas posteriores al tercer ciclo).» (53) |
| 6 | «Conoce la implicancia de la sexualidad como un todo y su enfoque desde la perspectiva de derecho.» | «Conoce la implicancia de la sexualidad como componente de la personalidad.» (54) |
| 7 | «…de los DD. HH. referentes a la no discriminación.» | «…de los DD. HH referentes a la no discriminación.» (54). Grafía de la fuente, sin punto después de «HH» |
| 11 | «…en su ámbito familiar, escolar y comunitario.» | «…en su ámbito familiar, escolar y en su comunidad.» (55) |

## Criterio de transcripción

- La capacidad oficial se cita tal como figura en el programa, incluida su grafía: «cohersivas» en 8.º, «DD. HH» en 9.º.
- En el texto editorial se usa la forma correcta («coercitivas»).
- El enfoque de derechos de la Clase 10 de 9.º se mantiene como desarrollo editorial del tema, sin atribuirlo a la capacidad oficial.
- Solo se normalizan los espacios dobles y se omiten los dos puntos con que el programa introduce la lista de contenidos.

## Vigencia

Esta carpeta fija la edición curricular usada en el proyecto. No certifica que ninguna resolución posterior haya modificado los programas: para afirmar su vigencia en 2026 hay que consultar la normativa por separado.
