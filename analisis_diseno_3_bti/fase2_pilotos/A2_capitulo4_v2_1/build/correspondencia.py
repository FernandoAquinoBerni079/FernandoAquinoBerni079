# -*- coding: utf-8 -*-
"""Correspondencia entre los 15 requisitos del catálogo (Tabla 4.3) y sus criterios de aceptación.
Origen de cada criterio:
  MODELO      resuelto en el libro del estudiante (se indica dónde);
  ESTUDIANTE  lo escribe el estudiante en una actividad; acá va la respuesta esperada;
  DOCENTE     criterio de referencia para el docente: no figura en el libro. Sirve para corregir el
              catálogo de cada equipo o para proponerlo como actividad adicional."""

CORRESPONDENCIA = [
    ('RF-01', 'DOCENTE', 'Guía (referencia)',
     'Dado un ejemplar disponible y un lector activo sin préstamos, cuando la bibliotecaria registra el préstamo con '
     'fecha de salida 2 de marzo, entonces la lista de préstamos activos muestra ese ejemplar por su código, ese lector '
     'y esa fecha.'),
    ('RF-02', 'MODELO', 'Tabla 4.5',
     'Dado un préstamo registrado el 2 de marzo con el plazo de RN-03, cuando se consulta su vencimiento, entonces '
     'figura el 9 de marzo.'),
    ('RF-03', 'DOCENTE', 'Guía (referencia)',
     'Dado un ejemplar con un préstamo activo, cuando se registra su devolución indicando el código del ejemplar, '
     'entonces se cierra ese préstamo, con la fecha de devolución, y el ejemplar vuelve a figurar como disponible.'),
    ('RF-04', 'MODELO', 'Ejemplo resuelto 4.3 (CA-04)',
     'Dado un ejemplar con un préstamo activo, cuando se intenta registrar otro préstamo de ese ejemplar, entonces el '
     'sistema rechaza la operación, muestra el motivo y el ejemplar sigue teniendo un solo préstamo activo, el original.'),
    ('RF-05', 'ESTUDIANTE', 'Encuentro 8, Actividad 2',
     'Dado un lector con el máximo vigente de préstamos activos (dos, según RN-02), cuando se intenta registrarle otro, '
     'entonces el sistema lo rechaza, muestra el motivo y el lector sigue con dos préstamos activos.'),
    ('RF-06', 'ESTUDIANTE', 'Encuentro 8, Actividad 2',
     'Dado un lector inactivo, cuando se intenta registrarle un préstamo, entonces se rechaza con el motivo y no se crea '
     'ningún préstamo.'),
    ('RF-07', 'MODELO', 'Tabla 4.5',
     'Dado un título con un ejemplar disponible y otro prestado, cuando un lector sin sesión lo consulta, entonces ve '
     '«1 disponible» y ningún nombre de lector.'),
    ('RF-08', 'DOCENTE', 'Guía (referencia)',
     'Dados tres ejemplares prestados a tres lectores distintos, cuando la bibliotecaria consulta los préstamos activos, '
     'entonces ve, para cada ejemplar, el nombre del lector que lo tiene.'),
    ('RF-09', 'MODELO', 'Tabla 4.5',
     'Dado un mes con préstamos de tres cursos, cuando se pide el informe de ese mes, entonces aparece cada curso con su '
     'cantidad y la suma coincide con el total de préstamos del mes.'),
    ('RF-10', 'DOCENTE', 'Guía (referencia)',
     'Dado un lector con dos préstamos en el historial, cuando se lo inactiva, entonces deja de figurar entre los '
     'lectores habilitados y sus dos préstamos siguen en el historial.'),
    ('RNF-01', 'MODELO', 'Ejemplo resuelto 4.4, paso 4',
     'Dada la bibliotecaria después de una práctica guiada de 30 minutos (a confirmar con ella), cuando registra tres '
     'préstamos y dos devoluciones de una lista preparada, entonces completa las cinco operaciones sin pedir ayuda y '
     'sin errores de carga.'),
    ('RNF-02', 'DOCENTE', 'Guía (referencia)',
     'Dada una persona sin sesión de bibliotecaria, cuando intenta registrar o devolver un préstamo, entonces la '
     'operación se rechaza y no se crea ni se modifica ningún préstamo.'),
    ('RNF-03', 'ESTUDIANTE', 'Encuentro 8, Actividad 5 (Desafío)',
     'Dado un préstamo activo de un lector, cuando una persona sin sesión consulta el catálogo y busca ese título, '
     'entonces ve la cantidad de ejemplares disponibles y no ve el nombre, el curso ni el código del lector.'),
    ('RS-01', 'MODELO', 'Tabla 4.5',
     'Dada la computadora de la biblioteca desconectada de internet, cuando se registra un préstamo y una devolución, '
     'entonces ambas operaciones se completan y quedan guardadas.'),
    ('RS-02', 'DOCENTE', 'Guía (referencia)',
     'Dada la lista de componentes necesarios para instalar y usar el sistema, cuando se revisa la licencia de cada '
     'uno, entonces ninguno exige pago ni suscripción.'),
]

ETIQUETA = {'MODELO': 'Modelo resuelto en el libro', 'ESTUDIANTE': 'Trabajo del estudiante',
            'DOCENTE': 'Referencia para el docente'}
