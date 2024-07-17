### EJERCICIO 1 ###
"""
Para este primer ejercicio crearemos una clase llamada "Estudiante" que tendrá los siguientes atributos:
* Nombre
* Edad
* Grado
Además, le asignaremos un método o acción llamado "estudiar" que devolverá un mensaje con el 
nombre del estudiante y el grado que cursa. Debemos crear un objeto Estudiante y usar el método estudiar().
Se debe interacturar con el usuario para ingresar los datos del estudiante.
"""

# Creamos la clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print("Estudiando...")
    
nombre = input("Ingrese el nombre del estudiante: ")
edad = input("Ingrese la edad del estudiante: ")
grado = input("Ingrese el grado del estudiante: ")

# Creamos el objeto estudiante
estudiante = Estudiante(nombre, edad, grado)

# Mostramos el mensaje
print(f"""\nDATOS DEL ESTUDIANTE:
      ----------------------------------
      Nombre: {estudiante.nombre}
      Edad: {estudiante.edad}
      Grado: {estudiante.grado}
      ----------------------------------""")

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
        break