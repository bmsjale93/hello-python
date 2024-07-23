### DUCK TYPING ###

# El concepto de Duck Typing en Python proviene de la expresión "Si parece un pato, nada como un pato y hace cuac como un pato,
# entonces probablemente sea un pato". En programación, esto significa que la validez de un objeto para una operación
# no se basa en su tipo, sino en si tiene los métodos o atributos necesarios para realizar esa operación.

# Ejemplo sencillo:
# Supongamos que tenemos dos clases, `Pato` y `Ganso`, ambas tienen un método `hacer_sonido`.

class Pato:
    def hacer_sonido(self):
        return "Cuac"

class Ganso:
    def hacer_sonido(self):
        return "Honk"

# Podemos definir una función que acepte cualquier objeto y llame a su método `hacer_sonido`.

def hacer_sonido_animal(animal):
    print(animal.hacer_sonido())

# Aquí, no nos importa de qué clase específica es el objeto `animal`, 
# solo necesitamos que tenga un método `hacer_sonido`.

mi_pato = Pato()
mi_ganso = Ganso()

hacer_sonido_animal(mi_pato)  # Salida: Cuac
hacer_sonido_animal(mi_ganso) # Salida: Honk

# En este ejemplo, `hacer_sonido_animal` funciona con cualquier objeto que tenga un método `hacer_sonido`.
# Esto es Duck Typing: el código funciona con cualquier objeto que "parezca un pato", es decir, que tenga los métodos
# necesarios, sin importar su tipo explícito.

# Otro ejemplo de Duck Typing es cuando utilizamos estructuras de datos integradas de Python.

def procesar_lista(lista):
    for elemento in lista:
        print(elemento)

# Podemos pasar una lista de enteros, cadenas o incluso una lista de objetos personalizados
# a la función `procesar_lista`.

enteros = [1, 2, 3]
cadenas = ["uno", "dos", "tres"]

procesar_lista(enteros)  # Salida: 1 2 3
procesar_lista(cadenas)  # Salida: uno dos tres

# En este caso, `procesar_lista` funciona con cualquier iterable,
# sin importar de qué tipo sean sus elementos, siempre que puedan ser iterados.