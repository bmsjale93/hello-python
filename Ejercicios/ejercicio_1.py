# EJERCICIO 1

"""
El curso realizado tiene una duración de 1.5 horas. Otros cursos tienen las siguientes duraciones:
- Mínimo: 2.5 horas
- Promedio: 4 horas
- Máximo: 7 horas

a) Diferencia en porcentaje entre el curso actual y:
- El más rápido de otros cursos.
- El más lento de otros cursos.
- El promedio de otros cursos.

b) Teniendo en cuenta que el promedio de CRUDO (tiempo inservible) es de 5 horas y con edición lo convierten
en 4 horas, y el de este video el CRUDO es de 3.5 horas y se redujo a 1.5 horas, ¿Qué porcentaje de material
inservible se reduce en:
- El promedio de los cursos.
- El curso actual.

c) Ver 10 horas de este curso, ¿A cuántas de otros cursos equivale? ¿Y al revés?
"""

# Promedio de Duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_actual = 1.5

# EJERCICIO A
# Diferencias de Duración
diferencia_con_min = 100 - curso_actual / otros_cursos_min * 100
diferencia_con_max = 100 - curso_actual * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - curso_actual / otros_cursos_promedio * 100

print("------------------------------")
print("Este curso dura:")
print(f" - un {diferencia_con_min}% menos que el más rápido de otros cursos.")
print(f" - un {diferencia_con_max}% menos que el más lento de otros cursos.")
print(f" - un {diferencia_con_promedio}% menos que el promedio de otros cursos.")
print("------------------------------")


# EJERCICIO B
# Duración de CRUDO
crudo_promedio = 5
crudo_curso = 3.5

# Calculamos el porcentaje de tiempo inservible removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_curso = 100 - curso_actual * 1000 // crudo_curso / 10

# Mostrando la cantidad de espacio vacio removido
print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacío.")
print(f"Este curso elimina un {tiempo_vacio_curso}% de tiempo vacío.")
print("------------------------------")


# EJERCICIO C
# Mostramos la diferencia si los cursos duraran 10 horas.
print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // curso_actual / 10} horas de otros cursos.")
print(f"Ver 10 horas de otros cursos equivale a ver {curso_actual * 100 // otros_cursos_promedio / 10} horas de este curso.")
print("------------------------------")
