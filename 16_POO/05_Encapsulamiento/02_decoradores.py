### DECORADORES EN PYTHON ###

# Los decoradores en Python son una herramienta poderosa y flexible para modificar el comportamiento de funciones o métodos.
# Un decorador es una función que recibe otra función como argumento y devuelve una nueva función con un comportamiento modificado.

# Ejemplo básico de un decorador:
def mi_decorador(funcion):
    def nueva_funcion(*args, **kwargs):
        print("Llamada a la función decorada")
        resultado = funcion(*args, **kwargs)
        print("Función decorada ha terminado")
        return resultado
    return nueva_funcion

# Usamos el decorador con una función:


@mi_decorador
def di_hola():
    print("¡Hola!")


# Llamamos a la función decorada:
di_hola()
# Salida:
# Llamada a la función decorada
# ¡Hola!
# Función decorada ha terminado

# En este ejemplo:
# 1. `mi_decorador` es la función decoradora que recibe `di_hola` como argumento.
# 2. `nueva_funcion` es la función interna que añade el comportamiento adicional.
# 3. Usamos `@mi_decorador` antes de la definición de `di_hola` para aplicar el decorador.

# Decoradores con argumentos:
# Los decoradores también pueden aceptar argumentos si están anidados dentro de otra función.
def decorador_con_argumentos(mensaje):
    def mi_decorador(funcion):
        def nueva_funcion(*args, **kwargs):
            print(mensaje)
            resultado = funcion(*args, **kwargs)
            print("Función decorada ha terminado")
            return resultado
        return nueva_funcion
    return mi_decorador

# Usamos el decorador con argumentos:
@decorador_con_argumentos("Llamada a la función decorada con mensaje personalizado")
def di_adios():
    print("¡Adiós!")

# Llamamos a la función decorada:
di_adios()
# Salida:
# Llamada a la función decorada con mensaje personalizado
# ¡Adiós!
# Función decorada ha terminado


# Decoradores para métodos de clases:
# Los decoradores pueden ser usados también para métodos dentro de clases.
class MiClase:
    @mi_decorador
    def metodo_decorado(self):
        print("Método decorado dentro de la clase")

# Creamos una instancia de la clase y llamamos al método decorado:
objeto = MiClase()
objeto.metodo_decorado()
# Salida:
# Llamada a la función decorada
# Método decorado dentro de la clase
# Función decorada ha terminado


# Decoradores incorporados:
# Python incluye algunos decoradores incorporados como `@staticmethod`, `@classmethod` y `@property`.
class OtraClase:
    contador = 0

    @classmethod
    def incrementar_contador(cls):
        cls.contador += 1
        return cls.contador

# Usamos el decorador `@classmethod` para definir un método de clase que puede modificar la variable de clase `contador`.


# Llamamos al método de clase:
print(OtraClase.incrementar_contador())  # Salida: 1
print(OtraClase.incrementar_contador())  # Salida: 2


# Decoradores anidados y múltiples decoradores:
# Podemos anidar decoradores y usar múltiples decoradores en una sola función.
def decorador_1(funcion):
    def nueva_funcion_1(*args, **kwargs):
        print("Decorador 1 antes de la función")
        resultado = funcion(*args, **kwargs)
        print("Decorador 1 después de la función")
        return resultado
    return nueva_funcion_1

def decorador_2(funcion):
    def nueva_funcion_2(*args, **kwargs):
        print("Decorador 2 antes de la función")
        resultado = funcion(*args, **kwargs)
        print("Decorador 2 después de la función")
        return resultado
    return nueva_funcion_2

@decorador_1
@decorador_2
def funcion_decorada():
    print("Función decorada")

# Llamamos a la función con múltiples decoradores:
funcion_decorada()
# Salida:
# Decorador 1 antes de la función
# Decorador 2 antes de la función
# Función decorada
# Decorador 2 después de la función
# Decorador 1 después de la función

# En resumen, los decoradores en Python son una manera de añadir o modificar el comportamiento de funciones o métodos.
# Son una herramienta poderosa que permite escribir código más limpio, reutilizable y modular.