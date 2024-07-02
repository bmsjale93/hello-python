### ITERANDO SOBRE LISTAS o TUPLAS ###

animales = ["gato", "perro", "tigre", "leon"]
print("---------------------------")

# Iteramos sobre la lista de animales
for animal in animales:
    print(f"El animal ahora es: {animal}.")    
print("---------------------------")

# EJEMPLO 2: NÚMEROS
numeros = [52, 16, 14, 72]
for numero in numeros:
    resultado = numero * 10
    print(f"El número {numero} multiplicado por 10 es: {resultado}.")
print("---------------------------")

# Usando la función zip()
# La función zip() nos permite iterar sobre dos listas al mismo tiempo
for numero, animal in zip(numeros, animales):
    print(f"Recorriendo Lista 1: {numero}")
    print(f"Recorriendo Lista 2: {animal}")
print("---------------------------")

# Usando la función range()
# La función range() nos permite crear una lista de números
for num in range(5, 10):
    print(num)
print("---------------------------")

# Si solo ponemos un valor, se asume que el inicio es 0
for num in range(10):
    print(num)
print("---------------------------")

# Tambien podemos recorrer un rango utilizando len()
# len() toma como argumento una lista y devuelve la cantidad de elementos que tiene
# Esta forma de recorrer una lista NO es óptima
for num in range(len(numeros)):
    print(numeros[num])
print("---------------------------")

# La forma óptima de recorrer una lista es utilizando enumerate()
# Esta función nos devuelve el índice y el valor de cada elemento (tupla)
for num in enumerate(numeros):
    print(num)
print("---------------------------")

# Finalmente podemos utilizar el ELSE en un bucle
for numero in numeros:
    print(f"Ejecutando el último bucle, valor actual: {numero}")
else:
    print("El bucle ha finalizado.")

print("---------------------------")
