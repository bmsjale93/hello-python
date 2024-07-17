### CREANDO CLASES Y OBJETOS ###

# Una clase es un molde para crear objetos. Los objetos son instancias de una clase.
# Las clases tienen atributos (características) y métodos (acciones).
# Para definir una clase, usamos la palabra reservada "class".
# Para crear un objeto de una clase, usamos la palabra reservada "self".

# CREANDO UNA CLASE Y UN OBJETO ESTÁTICOS
# Crearemos una clase para construir un tipo de teléfono. Este tendrá los datos estáticos.
class Celular():
    marca = "Samsung"
    modelo = "Galaxy A10"
    camara = "48MP"

# Instanciamos la clase
celular1 = Celular()
celular2 = Celular()
celular3 = Celular()
celular4 = Celular()

# Accedemos a los atributos de la clase llamando al objeto y el atributo
print("--------------------")
print(f"Con datos estáticos:\n{celular1.marca}\n{celular2.marca}\n{celular3.marca}\n{celular4.marca}")
print("--------------------")


# CREANDO CLASES Y OBJETOS ESTÁTICOS DINÁMICOS
class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
celular1 = Celular("Apple", "iPhone 12", "12MP")
celular2 = Celular("Samsung", "Galaxy A10", "48MP")
celular3 = Celular("Xiaomi", "Redmi Note 9", "48MP")
celular4 = Celular("Motorola", "Moto G9", "48MP")

print(f"Con datos dinámicos:\n{celular1.marca}\n{celular2.marca}\n{celular3.marca}\n{celular4.marca}")
print("--------------------")