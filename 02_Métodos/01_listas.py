### MÉTODOS DE LISTAS ###

# LIST
# Es una función que crea una lista a partir de un iterable
lista = list(["Hola", "Alex", 30]) # Un buen uso sería para crear una lista vacía
print(lista)

# LEN
# Es una función que devuelve la longitud de una lista
longitud = len(lista)

# APPEND
# Añade un elemento al final de una lista
lista.append("Python") # Añade "Python"

# EXTEND
# Añade varios elementos al final de una lista
lista.extend(["Java", "C++"]) # Añade "Java" y "C++"

# INSERT
# Añade un elemento en una posición específica
lista.insert(1, "C#") # Añade "C#" en la posición 1

# POP
# Elimina un elemento de una lista por su índice
lista.pop(1) # Elimina "C#"
lista.pop(-1) # Elimina el último elemento de la lista
lista.pop(-2)  # Elimina el penúltimo elemento, recorre la lista de forma inversa

# REMOVE
# Elimina un elemento de una lista por su valor
lista.remove("Alex") # Elimina "Alex"

# CLEAR
# Elimina todos los elementos de una lista
lista2 = list(["Hola", "Alex", "Python", "Java", "C++", "C#"])
lista2.clear()

# SORT
# Ordena una lista con valores numéricos o boleanos de menor a mayor (de forma ascendente)
lista3 = list([4, 2, True, False, False, 5, 1, 3, 0])
lista3.sort()

# También podemos ordenar una lista de forma descendente
lista4 = list([4, 2, True, False, False, 5, 1, 3, 0])
lista4.sort(reverse=True)

# REVERSE
# Invierte el orden de los elementos de una lista, no ordena, solo traspone
lista5 = list([1, 2, 3, "Marcos", 5])
lista5.reverse()


# IMPRIMIR MÉTODOS
print(lista)
print(lista2)
print(lista3)
print(lista4)
print(lista5)