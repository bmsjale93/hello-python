### ABSTRACCIÓN ###

# La abstracción es un principio fundamental de la programación orientada a objetos que permite ocultar los detalles
# complejos de la implementación y mostrar solo la funcionalidad esencial de un objeto.
# Esto permite a los desarrolladores centrarse en lo que hace un objeto en lugar de cómo lo hace.

# En Python, la abstracción se logra mediante el uso de clases abstractas y métodos abstractos.
# Para crear clases y métodos abstractos, se utiliza el módulo `abc` (Abstract Base Classes).

from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años. ")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Estoy estudiando {self.actividad}")


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Actualmente, estoy trabajando en {self.actividad}")


alex = Estudiante("Alex", 30, "Masculino", "Programador")
pedro = Trabajador("Pedro", 28, "Masculino", "Programación")

alex.presentarse()
alex.hacer_actividad()
pedro.presentarse()
pedro.hacer_actividad()