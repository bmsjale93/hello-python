### MÉTODOS PARA DICCIONARIOS ###

diccionario = {
    "nombre": "Alex",
    "apellido": "Delgado",
    "edad": 30,
}

# KEYS
# Devuelve una lista con las claves del diccionario
# También nos sirve para iterar sobre las claves
claves = diccionario.keys()

# GET
# Devuelve el valor de una clave específica
# Si la clave no existe, devuelve None
nombre = diccionario.get("nombre")

# POP
# Elimina un elemento de un diccionario por su clave
diccionario.pop("nombre")

# ITEMS
# Devuelve una lista con tuplas que contienen la clave y el valor
diccionario_iterable = diccionario.items()

# CLEAR
# Elimina todos los elementos de un diccionario
diccionario.clear()

# IMPRIMIR MÉTODOS
print(diccionario)
print(diccionario_iterable)
