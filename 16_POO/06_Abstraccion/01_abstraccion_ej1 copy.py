###  ABSTRACCIÓN: EJEMPLO 1 ###

# Definir una clase abstracta `Animal`
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

    def dormir(self):
        print("El animal está durmiendo")

# La clase `Animal` no puede ser instanciada directamente porque contiene métodos abstractos.
# Las subclases de `Animal` deben implementar los métodos abstractos.
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Crear instancias de `Perro` y `Gato`
mi_perro = Perro()
mi_gato = Gato()

# Llamar a los métodos implementados
print(mi_perro.hacer_sonido())  # Salida: Guau
print(mi_gato.hacer_sonido())   # Salida: Miau

# Llamar al método no abstracto definido en la clase base
mi_perro.dormir()  # Salida: El animal está durmiendo
mi_gato.dormir()   # Salida: El animal está durmiendo

# Intentar instanciar la clase `Animal` directamente producirá un error
# animal = Animal()  # TypeError: Can't instantiate abstract class Animal with abstract methods hacer_sonido

# En este ejemplo:
# - `Animal` es una clase abstracta que define un método abstracto `hacer_sonido`.
# - `Perro` y `Gato` son subclases que implementan el método abstracto `hacer_sonido`.

# La abstracción permite definir una interfaz común para un conjunto de clases y garantizar que cada clase
# implemente esa interfaz. Esto ayuda a reducir la complejidad del código y a mejorar la mantenibilidad.