# Piloto C, versión 2.1 — Adenda

**Corrección única.** La fusión de los encuentros 9 y 10 de Work, encuentro 8 del plan de 28, ahora conserva una representación simplificada del **proceso actual**: un diagrama de 5 a 7 pasos del préstamo y la devolución, con los problemas del dossier marcados, en aprox. 1 HC de análisis. Le siguen el proceso propuesto y los tres casos de uso con un flujo alternativo cada uno. Así se mantiene la evidencia esencial de C4: proceso actual y propuesto, casos de uso y excepciones.

**Horas y totales.** El reparto del encuentro no cambia (A 4, D 1), así que los totales siguen iguales:
- análisis 37 HC;
- diseño 24;
- programación 16;
- verificación 30;
- documentación 7;
- gestión 4;
- evaluación 22.

**Control nuevo en `distribucion.py`.** La fusión 9+10 debe mencionar proceso actual, proceso propuesto y casos de uso. Si no, el script falla.

**Evidencia:**
- `distribucion_36.csv` es idéntico al de la v2;
- en `tablas_generadas.md` cambia solo la fila del encuentro 8 del plan de 28 (comparación con `diff`).

**Archivos sin cambios:** los de `../v2/`.
