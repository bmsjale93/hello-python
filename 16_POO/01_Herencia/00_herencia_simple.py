###  HERENCIA MÚLTIPLE ###
# La herencia múltiple es un tipo de herencia en la que una clase hija hereda de dos o más clases padres.
# La herencia múltiple permite a una clase hija heredar atributos y métodos de dos o más clases padres.
# La herencia múltiple se utiliza en lenguajes de programación como Python.

# CLASE PADRE
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# CLASES HIJAS
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
    def hablar(self):
        print(f"Soy un empleado, me llamo {self.nombre}...")


class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

    def hablar(self):
        print(f"Soy un estudiante, me llamo {self.nombre}...")