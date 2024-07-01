### INPUTS PARA NÚMEROS ###

# Le pedimos un número al usuario
numero = input("Introduce un número: ")

# Esto nos devuelve un string, debemos convertirlo en un entero
numero = int(numero) * 2
print(f"Devolviendo un entero: {numero}")

# Si hacemos lo mismo pero no convertimos el string a entero, concatenará los dos strings
numero = input("Introduce un número: ")
numero = numero * 2
print(f"Devolviendo un string concatenado: {numero}") # El resultado será 3030

# También podemos convertir el número en un float
numero = input("Introduce un número: ")
numero = float(numero) * 2
print(f"Devolviendo un float: {numero}")
