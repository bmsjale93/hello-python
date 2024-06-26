### VARIABLES ###
# Espacios que se almacenan en la memoria de nuestro programa
# Como indica su nombre, son variables, es decir, se pueden modificar
# Las variables se declaran con un nombre y un valor
# Las variables son modificables y pueden cambiar de valor

# EJEMPLO CON NÚMEROS
a = 5
b = 8
c = a + b

print(c)

# EJEMPLO CON PALABRAS
nombre = "Alejandro"
print(nombre)

# EJEMPLO CON MODIFICACIÓN DE VARIABLES
nombre = "Alejandro"
nombre = "Juan"
print(nombre)

# Los números pueden variar de valor
numero = 10
numero += 1
numero -= 5
print(numero)

# CONCATENACIÓN DE VARIABLES
nombre = "Alejandro"
bienvenida = "Hola, " + nombre + " ¿Cómo estás?"
print(bienvenida)

# La concatenación de variables deben ser del mismo tipo
# Esto no funcionará
# nombre = 5
# bienvenida = "Hola, " + nombre + " ¿Cómo estás?"
# print(bienvenida)

# USO DE F-STRINGS (convierte todo a string)
nombre = 5
bienvenida = f"Hola, {nombre} ¿Cómo estás?"
print(bienvenida)

# BORRAR VARIABLES
nombre = 5
bienvenida = f"Hola, {nombre} ¿Cómo estás?"
#del bienvenida  # Elimina la variable
print(bienvenida)

# Si borramos nombre después de haberlo usado en bienvenida, se imprimirá correctamente
nombre = "Alejandro"
bienvenida = f"Hola, {nombre} ¿Cómo estás?"
del nombre # Al borrarlo después de la concatenación, no afecta a la variable bienvenida
print(bienvenida)

# OPERADORES DE PERTENENCIA (in / not in)
nombre = "Alejandro"
bienvenida = f"Hola, {nombre} ¿Cómo estás?"
print("ola" in bienvenida)  # True
print("Pedro" in bienvenida)  # False
print("Pedro" not in bienvenida)  # True
print("hola" not in bienvenida)  # True, ya que es case sensitive

# Definiendo una variable con camelCase
nombreUsuario = "Alejandro"
print(nombreUsuario)

# Definiendo una variable con snake_case (recomendado)
nombre_usuario = "Alejandro"
print(nombre_usuario)
