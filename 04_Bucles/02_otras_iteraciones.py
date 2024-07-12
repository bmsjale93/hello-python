### OTRAS ITERACIONES ###

frutas = ['manzana', 'pera', 'mango', 'fresa', 'piña']

# Evitando comer una fruta con la sentencia continue
for fruta in frutas:
    if fruta == 'mango':
        continue    # Salta a la siguiente iteración
    print(f"Me voy a comer una {fruta}")

print("-------------------")

# Evitando que el bucle continue ejecutándose con la sentencia break
for fruta in frutas:
    if fruta == 'mango':
        break    # Salta fuera del bucle
    print(f"Me voy a comer una {fruta}")

print("Bucle Terminado")
print("-------------------")

# Si utilizamos break, también saltará un else
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == 'mango':
        break    # Salta fuera del bucle
else:
    print("Bucle Terminado") # Esto no se ejecutará
print("-------------------")


# RECORRER UNA CADENA DE TEXTO
cadena = "Hola Alex, ¿cómo estás?"

# Recorremos la cadena de texto letra por letra
for letra in cadena:
    print(letra)
    
print("-------------------")


# RECORRER UNA LISTA CON NÚMEROS
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numero in numeros:
    print(numero)

print("-------------------")

# Podemos realizar esta iteración for con una linea de código
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
print("-------------------")