# Herramientas del docente para revisar un paquete de entrega (Capítulo 17)

Estas herramientas viven **fuera** de los paquetes que se revisan. Un paquete recibido de otro equipo, o de alguien
ajeno a la clase, es código desconocido: no se ejecuta para decidir si es confiable.

## 1. Inspección estática (siempre primero)

    php inspeccionar_entrega.php <carpeta del paquete>

Esta herramienta solo lee texto y nombres de archivo. No ejecuta, no incluye y no interpreta ningún archivo del
paquete.

| Bloque | Qué revisa |
|---|---|
| A | Cada comando de la guía tiene una forma conocida y nombra un archivo que existe en el paquete. |
| B | Cada archivo de la lista de entrega está en el paquete. No hay rutas que salgan del paquete ni enlaces simbólicos. |
| C | Cada prueba declarada es `php pruebas/<nombre>.php` y está en la lista cerrada. No se ejecuta. |
| D | Cada recurso de `public/` que no es código tiene su procedencia. |
| E | Cada mensaje y cada pantalla del manual existen. Los mensajes se leen como texto. |
| F | Todos los documentos declaran la misma versión. |

## 2. Pruebas funcionales, solo en aislamiento

    php probar_en_aislamiento.php <carpeta del paquete> [--limite=SEGUNDOS]

**Lista cerrada.** La herramienta solo ejecuta las pruebas de su lista cerrada (`prueba_contratos`,
`prueba_garantias` y `prueba_respaldo`). Arma ella misma cada comando, sin pasar por la consola del sistema, y nunca
ejecuta un texto escrito en el paquete.

**Cómo se protege:**
- trabaja en una copia descartable, que borra al terminar;
- corre con un entorno mínimo y con un tiempo límite por prueba;
- se niega a correr con una cuenta de administrador o si el paquete tiene enlaces simbólicos.

**Procedimiento.** Las pruebas se corren siempre así:
1. **Primero la inspección estática.** Si informa un enlace simbólico o una ruta fuera del paquete, no se sigue.
2. **Equipo aislado.** Se usa una computadora o máquina virtual de pruebas, sin datos de la institución ni de personas, y
   **sin red** (cable y wifi desconectados). En Linux también sirve un espacio de red aislado (`unshare -n`).
3. **Cuenta estándar.** Se usa una cuenta sin permisos de administrador. En Windows, la herramienta pide confirmarlo con
   `--cuenta-sin-permisos-de-administrador`.
4. **Copia descartable.** El paquete se copia a una carpeta descartable. La herramienta hace además su propia copia y la
   borra.
5. **Registro.** Se anota el resultado, el equipo, el sistema y las versiones, como en el acta de entrega.
6. **Limpieza.** Al terminar, se borra la carpeta descartable. Si se usó una máquina virtual, se vuelve a su estado
   inicial.

La instalación del Encuentro 34 por otro equipo sigue las mismas condiciones: cuenta estándar, carpeta descartable,
datos ficticios.

## Estado

Las dos herramientas se probaron solo en el entorno de construcción del lote:
- Linux, PHP 8.3.6;
- una cuenta sin privilegios (`nobody`);
- un espacio de red aislado.

En Windows y en los laboratorios escolares siguen **pendientes**.
