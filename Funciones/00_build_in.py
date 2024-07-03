### FUNCIONES BUILD IN ###
# Son funciones que ya vienen en python y que podemos utilizar sin necesidad de importar ninguna librería.

numeros = [4, 7, 14, 28, 42, 15]

# Buscamos el número más alto de la lista
numero_mas_alto = max(numeros)
print(f"El número más alto de la lista es: {numero_mas_alto}")

# Buscamos el número más pequeño de la lista
numero_mas_bajo = min(numeros)
print(f"El número más bajo de la lista es: {numero_mas_bajo}")

# Podemos redondear a 6 decimales
numero = 3.14159265359
numero_redondeado = round(numero, 6)
print(f"El número redondeado a 6 decimales es: {numero_redondeado}")

# Función bool() para convertir a booleano
# Retorna False si el valor es 0, None, False, "", [], {}, () o 0.0
# Retorna True en cualquier otro caso
resultado = bool(9)
print(f"El valor 9 convertido a booleano es: {resultado}")

# Función all() para verificar si todos los elementos de un iterable son verdaderos
# Retorna True si todos los elementos son verdaderos
# Retorna False si al menos uno es falso
numeros2 = [4, 0, 14, 28, 42, 15] # Al pasar un 0, el resultado será False
resultado_all = all(numeros2)
print(f"¿Todos los elementos de la lista son verdaderos?: {resultado_all}")

#La función sum() nos permite sumar todos los elementos de un iterable
suma = sum(numeros2)
print(f"La suma de todos los elementos de la lista es: {suma}")