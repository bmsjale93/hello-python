### DICCIONARIOS AVANZADOS ###

# Creando un diccionario con dict()
diccionario = dict(nombre="Alex", edad=30, ciudad="Sevilla")
print(diccionario)

# Con dict() podemos crear diccionarios vacíos
diccionario_vacio = dict()
print(diccionario_vacio)

# Las tuplas dentro de un diccionario pueden ser claves
# Sin embargo, las listas no pueden ser claves
diccionario_con_tupla = {(1, 2): "Hola", (3, 4): "Adiós"}
print(diccionario_con_tupla)

# Para añadir una lista como clave debemos utilizar frozenset()
diccionario_con_lista = {frozenset([1, 2]): "Hola", frozenset([3, 4]): "Adiós"}
print(diccionario_con_lista)

# Podemos crear diccionarios con fromkeys()
# Este método nos permite crear diccionarios con claves con valores por defecto (None)
diccionario_con_fromkeys = dict.fromkeys(["nombre", "edad", "ciudad"])
print(diccionario_con_fromkeys)

# Una particularidad de fromkeys() es que podemos asignar un valor por defecto
diccionario_con_fromkeys_valor = dict.fromkeys(["nombre", "edad", "ciudad"], "Desconocido")
print(diccionario_con_fromkeys_valor)