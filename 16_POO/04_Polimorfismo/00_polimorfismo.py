### POLIFORMISMO ##

# El polimorfismo es un concepto de la programación orientada a objetos
# que permite que objetos de diferentes clases sean tratados como objetos
# del mismo tipo a través de una interfaz común.

# Ejemplo sencillo:
# Supongamos que tenemos una clase `Perro` y una clase `Gato`.
# Ambas clases tienen un método `hacer_sonido`.

class Perro:
    def hacer_sonido(self):
        return "Guau"

class Gato:
    def hacer_sonido(self):
        return "Miau"

# Aunque `Perro` y `Gato` son clases diferentes, ambas tienen el método `hacer_sonido`.
# Esto nos permite tratar instancias de ambas clases de la misma manera.
def hacer_sonido_animal(animal):
    print(animal.hacer_sonido())

# Podemos crear instancias de `Perro` y `Gato` y pasarlas a la función `hacer_sonido_animal`.
mi_perro = Perro()
mi_gato = Gato()

hacer_sonido_animal(mi_perro)  # Salida: Guau
hacer_sonido_animal(mi_gato)   # Salida: Miau

# Aquí es donde entra en juego el polimorfismo:
# La función `hacer_sonido_animal` puede aceptar cualquier objeto que tenga un método `hacer_sonido`,
# sin importar de qué clase específica sea ese objeto.
