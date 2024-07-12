### DATOS COMPUESTOS ###
# Los datos compuestos son aquellos que pueden almacenar varios valores en una sola variable
# Los datos compuestos más comunes son las listas y las tuplas

# LISTAS
# Las listas son colecciones de datos ordenados y modificables
# Se definen con corchetes []

lista = ["Alejandro", "Delgado", True, 1.85]
print(lista)

# Accediendo a datos en la lista
lista = ["Alejandro", "Delgado", True, 1.85]
print(lista[1]) # Delgado

# Las listas son modificables
lista [0] = "Juan"
print(lista[0])  # Juan

# TUPLAS
# Las tuplas son colecciones de datos ordenados e inmutables
# Se definen con paréntesis ()

tupla = ("Alejandro", "Delgado", True, 1.85)
print(tupla[1]) # Delgado

# Las tuplas no se puede modificar
# tupla[0] = "Juan" # Esto no funcionará

# CONJUNTOS (set)
# Los conjuntos son colecciones de datos no ordenados y no indexados
# Se definen con llaves {}

conjunto = {"Alejandro", "Delgado", True, 1.85}
print(conjunto)

# No podemos modificar los elementos de un conjunto ni acceder a ellos
# Para acceder a los elementos de un conjunto, debemos utilizar un bucle
# conjunto[1] = "Pérez"   # Esto no funcionará
# print (conjunto[1])     # Esto no funcionará

# Si podemos redefinir el conjunto completo
conjunto = {"Juan", "Pérez", False, 1.75}
print(conjunto)

# No mostrará aquellos elementos que estén repetidos (los eliminará)
conjunto = {"Juan", "Pérez", False, 1.75, "Juan"}
print(conjunto)


# DICCIONARIO (dict)
# Los diccionarios son colecciones de datos no ordenados, modificables e indexados
# Se definen con llaves {} y pares clave : valor

diccionario = {
    "nombre": "Alejandro",
    "apellido": "Delgado",
    "casado": True,
    "altura": 1.85
}

print(diccionario)

# Podemos acceder a los elementos
print(diccionario["nombre"])  # Alejandro
print(diccionario["altura"] + 2) # 3.85
