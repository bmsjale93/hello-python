# POLIMORFISMO POR COERSIÓN ###

# El polimorfismo por coersión ocurre cuando los operadores o funciones son aplicados a diferentes tipos de datos
# y esos tipos son convertidos automáticamente a un tipo común para permitir la operación.
# Esto es común en lenguajes de programación que soportan la conversión implícita de tipos.

# Ejemplo sencillo:
# Supongamos que tenemos un entero y un flotante y los sumamos. Python convierte
# implícitamente el entero a flotante para realizar la operación.

# Sumando un entero y un flotante
entero = 5
flotante = 3.2
resultado = entero + flotante

print(f"Resultado de sumar un entero y un flotante: {resultado}")  # Salida: Resultado de sumar un entero y un flotante: 8.2

# Aquí, Python convierte el entero `5` a `5.0` para poder realizar la suma con `3.2`.
# Esta conversión implícita es un ejemplo de polimorfismo por coersión.

# Otro ejemplo es la concatenación de una cadena y un número.
# Necesitamos convertir explícitamente el número a cadena para evitar errores.

cadena = "El resultado es: "
numero = 10
resultado_concatenacion = cadena + str(numero)

print(resultado_concatenacion)  # Salida: El resultado es: 10

# En este caso, convertimos explícitamente el número a una cadena para realizar la concatenación.
# Aunque esto no es una conversión implícita, es una forma de coersión para permitir que la operación funcione.
