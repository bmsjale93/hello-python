###  HERENCIA MÚLTIPLE ###
# La herencia múltiple es un tipo de herencia en la que una clase hija hereda de dos o más clases padres.
# La herencia múltiple permite a una clase hija heredar atributos y métodos de dos o más clases padres.
# La herencia múltiple se utiliza en lenguajes de programación como Python.

# CLASES PADRE
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"Hola, estoy hablando un poco...")
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        print(f"Mi habilidad es {self.habilidad}...")


# CLASE HIJA
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, trabajo, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.trabajo = trabajo
        self.salario = salario
        
