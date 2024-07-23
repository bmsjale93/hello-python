### POLIFORMISMO DE HERENCIA ###

# El polimorfismo de herencia es una característica de la programación orientada a objetos
# que permite que una subclase herede métodos y propiedades de una superclase y,
# a la vez, tenga sus propias implementaciones específicas de esos métodos.

# Ejemplo sencillo:
# Supongamos que tenemos una clase `Animal` con un método `hacer_sonido`.
# Luego, creamos dos subclases, `Perro` y `Gato`, que heredan de `Animal`
# y cada una tiene su propia implementación del método `hacer_sonido`.

class Animal:
    def hacer_sonido(self):
        pass  # Método vacío que será sobrescrito en las subclases

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Aquí, `Perro` y `Gato` heredan de `Animal` pero cada uno sobrescribe
# el método `hacer_sonido` con su propia implementación.

# Ahora podemos crear una lista de animales y llamar al método `hacer_sonido`
# en cada uno, independientemente de su tipo específico.

animales = [Perro(), Gato()]

for animal in animales:
    print(animal.hacer_sonido())

# Salida:
# Guau
# Miau

# En este caso, `Perro` y `Gato` son tratados como `Animal` debido a la herencia,
# pero cada uno ejecuta su propia versión del método `hacer_sonido` gracias al polimorfismo.
