### CREANDO EXCEPCIONES PROPIAS ###

# Podemos crear nuestras propias excepciones, para ello debemos crear una clase que herede de Exception
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Error: {err}")

# Lanzando la excepción
raise MiExcepcion("Este es un error")

# Manejando la excepción
try:
    # raise es la palabra clave que se utiliza para lanzar una excepción
    raise MiExcepcion("Este es un error")
except:
    print("Error capturado")