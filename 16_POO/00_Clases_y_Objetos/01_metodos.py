### MÉTODOS EN CLASES ###

# LAS CLASES PUEDEN ALBERGAR MÉTODOS
class Celular:
    # El método __init__ es un método constructor que se ejecuta al instanciar la clase
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    # Los métodos llamar( y cortar() son métodos que simulan una acción
    def llamar(self):
        return f"Llamando desde un {self.modelo}"

    def cortar(self):
        return f"Cortando llamada desde un {self.modelo}"


celular1 = Celular("Apple", "iPhone 12", "12MP")
celular2 = Celular("Samsung", "Galaxy A10", "48MP")
celular3 = Celular("Xiaomi", "Redmi Note 9", "48MP")
celular4 = Celular("Motorola", "Moto G9", "48MP")

print(f"Realizando la acción de llamar y colgar:\n{celular1.llamar()}\n{celular1.cortar()}")
print("--------------------")