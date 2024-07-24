###  ABSTRACCIÓN: EJEMPLO 2 ###

# Definir una clase abstracta `FiguraGeometrica`
import math
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


# Implementar subclases `Circulo` y `Rectangulo`
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)


# Crear instancias de `Circulo` y `Rectangulo`
mi_circulo = Circulo(5)
mi_rectangulo = Rectangulo(4, 6)

# Calcular área y perímetro
# Salida: Área del círculo: 78.53981633974483
print(f"Área del círculo: {mi_circulo.area()}")
# Salida: Perímetro del círculo: 31.41592653589793
print(f"Perímetro del círculo: {mi_circulo.perimetro()}")

# Salida: Área del rectángulo: 24
print(f"Área del rectángulo: {mi_rectangulo.area()}")
# Salida: Perímetro del rectángulo: 20
print(f"Perímetro del rectángulo: {mi_rectangulo.perimetro()}")

# En este ejemplo:
# - `FiguraGeometrica` es una clase abstracta con métodos abstractos `area` y `perimetro`.
# - `Circulo` y `Rectangulo` son subclases que implementan estos métodos abstractos.

# La abstracción permite que las clases derivadas proporcionen implementaciones específicas de los métodos abstractos,
# mientras que la clase base define una interfaz común para todas las subclases.