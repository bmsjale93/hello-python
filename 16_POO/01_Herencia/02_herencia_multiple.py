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
        return f"Mi habilidad es {self.habilidad}"


# CLASE HIJA
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, trabajo, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.trabajo = trabajo
        self.salario = salario
        
    def presentarse(self):
        print(f"Hola, soy {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.trabajo}")
        
roberto = EmpleadoArtista("Roberto", 30, "Argentina", "Cantar", "Desarrollador", 50000)
roberto.presentarse()

# Como podemos saber si una clase es hija de otra clase?
herencia = issubclass(EmpleadoArtista, Persona)
print(herencia) # True

# Y si quereos saber si un objeto es una instancia de una clase?
instancia = isinstance(roberto, Persona)
print(instancia) # True