# EJERCICIO 2

"""
Crearemos una función que al pasarle un número, nos genere números primos hasta llegar a ese número.
Por ejemplo, si le pasamos el número 15, nos pasaría el 1, el 3, el 7, el 11 y el 13.
"""

# Función que nos retorna si un número es primo o no
def es_primo(num):
    # Verificamos que el número que le pasamos no sea divisible por
    # ningún número entre 2 y ese mismo número -1.
    for i in range(2, num-1):
        # Si es divisible por algún número, retornamos False y terminamos el bucle.
        if num%i == 0: return False
    # Si termina el bucle, significa que no fue divisible, por lo que es Primo.
    return True

# Creamos una función que retorne una lista con todos los números primos.
def primos_hasta(num):
    # Creamos la lista
    primos = []
    for i in range(3, num+1):
        # Verificamos si el valor es primo.
        resultado = es_primo(i)
        # En caso de que sea, lo agregamos a la lista.
        if resultado == True: primos.append(i)
    # Devolvemos la lista
    return primos

# Creamos el resultado llamando a la función y lo mostramos.
resultado = primos_hasta(47)
print(resultado)