###  HERENCIA ###

#  La herencia es una de las características más importantes de la programación orientada a objetos.
#  Permite definir una nueva clase a partir de una clase existente.
#  La clase existente se llama clase base o clase padre.
#  La nueva clase se llama clase derivada o clase hija.

# LA CLASE HIJA HEREDA DE LA CLASE BASE
#  La clase hija hereda todos los atributos y métodos de la clase base.
#  La clase hija también puede agregar nuevos atributos y métodos.
#  La clase hija puede modificar los atributos y métodos de la clase base.

# LA HERENCIA Y SUS BENEFICIOS
#  La herencia permite reutilizar el código.
#  La herencia permite crear una jerarquía de clases.
#  La herencia permite crear clases más especializadas, generales abstractas o concretas.

# Para comenzar, crearemos una clase base llamada "Persona"
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Ahora, crearemos la clase hija llamada "Empleado" que hereda de la clase "Persona"
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
    def hablar(self):
        print(f"No me apetece hablar...")


#  Ahora, crearemos un objeto de la clase Empleado
empleado1 = Empleado("Juan", 30, "Argentina", "Desarrollador", 50000)
persona1 = Persona("Alex", 25, "España")

# Mostramos los datos del empleado
print("--------------------")
print(f"Nombre: {empleado1.nombre}\nEdad: {empleado1.edad}\nNacionalidad: {
      empleado1.nacionalidad}\nTrabajo: {empleado1.trabajo}\nSalario: ${empleado1.salario}")
print("--------------------")

# Mostramos los datos de la persona
print(f"Nombre: {persona1.nombre}\nEdad: {persona1.edad}\nNacionalidad: {persona1.nacionalidad}")
print("--------------------")

#  Llamamos al método hablar() de la clase Empleado
empleado1.hablar()
print("--------------------")

persona1.hablar()
print("--------------------")
