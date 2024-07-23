### HERENCIAS - EJERCICIO 2 ###

"""
Ejercicio de Herencia y Uso de Super
------------------------------------
Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales: Persona y Estudiante.
La clase Persona tendrá los atributos de nombre y edad y un método que imprima el nombre y la edad de la persona.
La clase Estudiante heredará de la clase Persona y también tendrá un atributo adicional: grado y un método
que imprima el grado del estudiante.

Deberás utilizar super en el método de inicialización (init) para reutilizar el código de la clase padre (Persona).
Luego, crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus métodos para asegurarte
de que todo funciona correctamente.
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrar_grado(self):
        print(f"Grado: {self.grado}")

estudiante = Estudiante("Juan", "30", "Universidad")
print("--------------------")
print(" EJERCICIO 1 ")
print("--------------------")

estudiante.mostrar_datos()
estudiante.mostrar_grado()

"""
Ejercicio de Herencia Múltiple y MRO
------------------------------------
Imagina que estás modelando animales en un zoológico. Crear tres clases: "Animal", "Mamífero" y "Ave". La clase
"Animal" debe tener un método llamado "comer". La clase "Mamífero" debe tener un método llamado "amamantar" y la
clase "Ave" un método llamado "volar".

Ahora, crea una clase "Murciélago" que herede de "Mamífero" y "Ave", en ese orden, y por lo tanto debe ser capaz de
"amamantar" y "volar", además de "comer".

Finalmente, juega cn el orden de herencia de la clase "Murciélago" y observa cómo cambia el MRO y el comportamiento
de los métodos al usar super().
"""

class Animal:
    def comer(self):
        print("El animal está comiendo...")


class Ave(Animal):
    def volar(self):
        print("El animal está volando...")


class Mamifero(Animal):
    def amamantar(self):
        print("El animal está amamantando...")


class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()

print("--------------------")
print(" EJERCICIO 2 ")
print("--------------------")
murcielago.comer()
murcielago.amamantar()
murcielago.volar()

print(Murcielago.mro())