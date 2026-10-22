# Proyecto del lote 5 (Unidad V)

Todo lo que está acá trabaja sobre **copias**: no modifica la base de la clase, ni `lote_4/proyecto/`, ni las
referencias. Datos ficticios. Entorno de las pruebas registradas: contenedor Linux de construcción (no es una
computadora escolar ni Windows; las pruebas de campo E-1 a E-12 siguen pendientes).

| Carpeta | Para qué | Quién la usa |
|---|---|---|
| `cargador_dp/` | `cargar_dp.php` crea una copia descartable de una base con el conjunto de prueba DP (`dp.json`), comprueba el estado esperado e informa una huella reproducible. Se niega a sobrescribir una carpeta existente. | Equipos y docente |
| `matriz/` | `ejecutar_matriz.php` corre la matriz del equipo modelo (C-01 a C-20) sobre una copia con DP; `integracion.php`, los permisos de la Tabla 11.3, la persistencia entre procesos. | Docente y auditoría |
| `referencia_docente_v2/` | Copia de la referencia del lote 4 con la corrección de IN-02 y su prueba `pruebas/prueba_in02.sh`. | Docente (solución completa) |
| `referencia_docente_v2_sc02/` | La v2 más el cambio aprobado SC-02 (ME-14, informe de un mes vacío). | Docente (solución completa) |
| `DIFERENCIAS_v2.md` | Diff de cada archivo que cambia en las dos copias. | Docente y auditoría |

El conjunto **reservado DR** no está en el repositorio: es exclusivo del docente. `lote_5/caso/dr_plantilla.py`
tiene solo su estructura y un generador que escribe fuera del repositorio.

Para reproducir todas las pruebas: `python3 lote_5/build/reproducir.py` (desde `analisis_diseno_3_bti/`).
