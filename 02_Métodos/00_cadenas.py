### MÉTODOS DE CADENAS DE STRINGS ###
# Los métodos son funciones explícitas de un objeto
# Los métodos siguen la siguiente estructura:
# DATO.MÉTODO()

cadena1 = "Hola, soy Alex"
cadena2 = "155421484514948"
cadena3 = "HOLAMUNDO"


# DIR
# Nos devuelve una lista con todos los métodos disponibles para un objeto
#print(dir(cadena1)) # DIR se considera función, no método

# UPPER
# Convierte una cadena a mayúsculas
mayuscula = cadena1.upper()

# LOWER
# Convierte una cadena a minúsculas
minuscula = cadena1.lower()

# CAPITALIZE
# Convierte la primera letra de una cadena a mayúscula
capital = cadena1.capitalize()

# FIND
# Devuelve la posición de la primera ocurrencia de un carácter o cadena
# Devuelve la posición en la que encuentra la cadena
# Si no encuentra la cadena, devuelve -1
posicion = cadena1.find("Alex")
posicion2 = cadena1.find("hola") # Devuelve -1, ya que es case sensitive

#INDEX
# Realiza la misma función que FIND, pero si no encuentra la cadena, devuelve un error
index = cadena1.index("Alex")

# ISNUMERIC
# Devuelve True si la cadena es numérica, en otro caso devuelve False
numerico = cadena2.isnumeric() # Aunque sea un texto, isnumeric devuelve True si es un número

# ISALPHA
# Devuelve True si la cadena es alfanumérica, en otro caso devuelve False
alpha = cadena3.isalpha() # Sólo admite valores de la A a la Z, sin espacios ni números

# COUNT
# Devuelve el número de veces que se repite una cadena
contando = cadena1.count("o")

# LEN
# Devuelve la longitud de una cadena
longitud = len(cadena1) # Es una función, no un método

# STARTSWITH
# Devuelve True si la cadena empieza con una cadena específica
empieza_con = cadena1.startswith("Hola")

# ENDSWITH
# Devuelve True si la cadena termina con una cadena específica
termina_con = cadena1.endswith("Alex")

# REPLACE
# Reemplaza una cadena por otra
reemplazo = cadena1.replace("Alex", "Juan")

# SPLIT
# Divide una cadena en una lista de cadenas (matriz)
# Por defecto, divide por espacios
separar = cadena1.split(",")


# IMPRIMIR MÉTODOS
print(separar)
