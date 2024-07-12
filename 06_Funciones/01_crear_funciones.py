### CREANDO FUNCIONES ###
# Ahora vamos a crear nuestras propias funciones
# Para crear una función, utilizamos la palabra reservada "def"
# Después, el nombre de la función y los paréntesis

# Creamos una función simple que imprime un mensaje
def saludar():
    print("Hola Alex, ¿qué tal?")
    
saludar()

def espacio():
    print("-------------------")
    
espacio()

# Creamos una función con un parámetro
# Los parámetros son variables que se pasan a la función
def saludar(nombre):
    print(f"Hola {nombre}, ¿cómo te fue el día?")
    
saludar("Alex")
espacio()

# También podemos pasar más de un parámetro
# En este caso, pasamos un nombre y el sexo para redefinir la frase
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "reina"
        print(f"Hola {nombre}, ¿cómo te fue el día {adjetivo}?")
    elif sexo == "hombre":
        adjetivo = "titán"
        print(f"Hola {nombre}, ¿cómo te fue el día {adjetivo}?")
    else:
        adjetivo = "campeón"
        print(f"Hola {nombre}, ¿cómo te fue el día {adjetivo}?")

saludar("Alex", "HOMBRE")
espacio()

# Ahora, crearemos una función que nos retorne múltiples valores
def crear_contraseña_random(num):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña, num

# Desempaquetando la función para obtener los valores
password, primer_numero = crear_contraseña_random(453)
print(f"Tu contraseña es: {password}")
print(f"El número utilizado para crear la contraseña fue: {primer_numero}")
