### FUNCIONES CON ARGUMENTOS VARIABLES ###
# En python, podemos pasar un número variable de argumentos a una función

# Forma no óptima de sumar valores
def suma(a,b):
    return a + b

resultado = suma(5, 7)
print(resultado)

# También podríamos pasarle una lista, pero sigue sin ser óptimo
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados

resultado = suma([5, 7, 10, 15])
print(resultado)

# Para hacerlo de forma óptima, utilizamos *args
# Lo que hace *args es convertir los argumentos en una tupla
# *args siempre debe usarse al final de los argumentos
def suma (nombre, *numeros):
    return f"{nombre}, la suma de los números es: {sum(numeros)}"

resultado = suma("Alex", 5, 7, 10, 15)
print(resultado)

# Podemos adaptar la función no óptima anterior para que sea óptima
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5, 7, 10, 15])
print(resultado2)
