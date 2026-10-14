# Entrega para auditoría — DPS 7.º y 8.º (commit `faa8ef9`)

Copias exactas de los seis archivos de cada grado del commit `faa8ef939dbdbd62cb0d18636fc4bdd4edb849c2` (rama `claude/libros-5z31jx`). No son una versión nueva: los originales siguen en `combos_2026/7mo/` y `combos_2026/8vo/` y no se modificaron.

El repositorio es público. Cada archivo se puede bajar entero por su enlace fijo al commit. Los que superan 2,8 MB están además divididos en partes de hasta 2.800.000 bytes en esta carpeta.

## Cómo reconstruir un archivo dividido

- Windows (cmd): `copy /b ARCHIVO.part01 + ARCHIVO.part02 + … ARCHIVO`
- macOS / Linux: `cat ARCHIVO.part* > ARCHIVO`
- Python: `open(nombre,"wb").write(b"".join(open(p,"rb").read() for p in sorted(partes)))`

Después, comprobar que el SHA-256 del archivo reconstruido coincide con el de la tabla (`certutil -hashfile ARCHIVO SHA256` en Windows; `shasum -a 256 ARCHIVO` en macOS). El detalle de cada parte, con su SHA-256, está en `MANIFIESTO_SHA256.json`.

## 7.º

| Archivo | Bytes | SHA-256 | Partes |
|---|---|---|---|
| [DPS_7mo_TOMO_INTEGRAL_PEC_OFICIO_2026.docx](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/faa8ef939dbdbd62cb0d18636fc4bdd4edb849c2/dps_3er_ciclo/combos_2026/7mo/DPS_7mo_TOMO_INTEGRAL_PEC_OFICIO_2026.docx) | 25121748 | `d2df859d7e6a07ee304541185b886710dbb58b1edd38c0af023617b8bcea50c2` | 9 |
| [DPS_7mo_TOMO_INTEGRAL_PEC_OFICIO_2026.pdf](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/faa8ef939dbdbd62cb0d18636fc4bdd4edb849c2/dps_3er_ciclo/combos_2026/7mo/DPS_7mo_TOMO_INTEGRAL_PEC_OFICIO_2026.pdf) | 5135403 | `e4df9beda9ce78a16de3c699bd9b877b754e22591112cf5f1cf19f33a607007d` | 2 |
| [DPS_7mo_PLAN_ANUAL_PEC_OFICIO_2026.docx](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/faa8ef939dbdbd62cb0d18636fc4bdd4edb849c2/dps_3er_ciclo/combos_2026/7mo/DPS_7mo_PLAN_ANUAL_PEC_OFICIO_2026.docx) | 182056 | `7a5a153f4b652b904c7a225b8e4ae9c84b08b9b2884ae62f006a9a830914f596` | — |
| [DPS_7mo_PLANES_DE_CLASE_PEC_OFICIO_2026.docx](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/faa8ef939dbdbd62cb0d18636fc4bdd4edb849c2/dps_3er_ciclo/combos_2026/7mo/DPS_7mo_PLANES_DE_CLASE_PEC_OFICIO_2026.docx) | 217453 | `36e109a303149634c97e87419ccf80d89a937a02aba61ff670edba5d1166fd14` | — |
| [DPS_7mo_SOLUCIONARIO_DOCENTE_PEC_OFICIO_2026.docx](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/faa8ef939dbdbd62cb0d18636fc4bdd4edb849c2/dps_3er_ciclo/combos_2026/7mo/DPS_7mo_SOLUCIONARIO_DOCENTE_PEC_OFICIO_2026.docx) | 199848 | `95edea28f7b22aa1e02a621290721dfd810e92a1287b4698f7129399894f81d9` | — |
| [DPS_7mo_SOLUCIONARIO_DOCENTE_PEC_OFICIO_2026.pdf](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/faa8ef939dbdbd62cb0d18636fc4bdd4edb849c2/dps_3er_ciclo/combos_2026/7mo/DPS_7mo_SOLUCIONARIO_DOCENTE_PEC_OFICIO_2026.pdf) | 419187 | `cf5078fd8a1c95ec7cc5f8acda1311ceae7b170dc2fd200c749d94d1730b2454` | — |

## 8.º

| Archivo | Bytes | SHA-256 | Partes |
|---|---|---|---|
| [DPS_8vo_TOMO_INTEGRAL_PEC_OFICIO_2026.docx](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/faa8ef939dbdbd62cb0d18636fc4bdd4edb849c2/dps_3er_ciclo/combos_2026/8vo/DPS_8vo_TOMO_INTEGRAL_PEC_OFICIO_2026.docx) | 7804997 | `2b6b61aeb682cec79a004b7c0a4bc9e06af498bc68c8430c9af174dd1a93cdb2` | 3 |
| [DPS_8vo_TOMO_INTEGRAL_PEC_OFICIO_2026.pdf](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/faa8ef939dbdbd62cb0d18636fc4bdd4edb849c2/dps_3er_ciclo/combos_2026/8vo/DPS_8vo_TOMO_INTEGRAL_PEC_OFICIO_2026.pdf) | 3191623 | `414e89de67ae799846caa786c41c19182788825e3c0e7af041bc41f657ee9f2c` | 2 |
| [DPS_8vo_PLAN_ANUAL_PEC_OFICIO_2026.docx](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/faa8ef939dbdbd62cb0d18636fc4bdd4edb849c2/dps_3er_ciclo/combos_2026/8vo/DPS_8vo_PLAN_ANUAL_PEC_OFICIO_2026.docx) | 181727 | `7dc6578c6c11dde8adccae76f4ea81b2d9380e70bc49efe872360cc08c0a3633` | — |
| [DPS_8vo_PLANES_DE_CLASE_PEC_OFICIO_2026.docx](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/faa8ef939dbdbd62cb0d18636fc4bdd4edb849c2/dps_3er_ciclo/combos_2026/8vo/DPS_8vo_PLANES_DE_CLASE_PEC_OFICIO_2026.docx) | 279421 | `fcba85f9019f0bf28c6340c6c64475c161b915d7ff935442b2e10b0b9adbb4e8` | — |
| [DPS_8vo_SOLUCIONARIO_DOCENTE_PEC_OFICIO_2026.docx](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/faa8ef939dbdbd62cb0d18636fc4bdd4edb849c2/dps_3er_ciclo/combos_2026/8vo/DPS_8vo_SOLUCIONARIO_DOCENTE_PEC_OFICIO_2026.docx) | 199060 | `f07aa97038efc645b878354155c5f74c01288dd50c5462765bb8e02e7170220b` | — |
| [DPS_8vo_SOLUCIONARIO_DOCENTE_PEC_OFICIO_2026.pdf](https://raw.githubusercontent.com/FernandoAquinoBerni079/FernandoAquinoBerni079/faa8ef939dbdbd62cb0d18636fc4bdd4edb849c2/dps_3er_ciclo/combos_2026/8vo/DPS_8vo_SOLUCIONARIO_DOCENTE_PEC_OFICIO_2026.pdf) | 482564 | `02631043280832703db914afe07f43f658de4b9c1fa79d677a41ba6c5a769a1b` | — |

No hay PDF del Plan Anual ni de los Planes de Clase, por indicación expresa.
