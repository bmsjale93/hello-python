### BUCLE WHILE ###
# El bucle while se ejecuta mientras una condición sea verdadera (se comprueba en cada vuelta).
# Los bucles while son útiles cuando no sabemos cuántas veces se repetirá un bloque de código.
# Si no están correctamente codificados, podemos crear bucles infinitos.

# Inicio del bucle while
#while condicion:
    # Código a ejecutar mientras la condición sea verdadera
    # ...
    # ...
    # Actualización de la condición
    # ...
    # ...
# Fin del bucle while

contador = 0

while contador < 10:
    print(f"El contador es: {contador}")
    contador += 1

print("Fin del bucle while")
