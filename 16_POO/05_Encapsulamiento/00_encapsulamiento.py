### ENCAPSULAMIENTO EN PYTHON ###

# El encapsulamiento es un principio fundamental de la programación orientada a objetos
# que restringe el acceso directo a algunos de los componentes de un objeto.
# Esto significa que los detalles internos del objeto están ocultos del mundo exterior
# y solo se puede interactuar con ellos a través de métodos públicos.

# En Python, el encapsulamiento se logra mediante convenciones de nombres:
# - Atributos y métodos que comienzan con un guion bajo (_) son considerados "protegidos".
# - Atributos y métodos que comienzan con dos guiones bajos (__) son "privados".

# Ejemplo de encapsulamiento con atributos y métodos públicos, protegidos y privados.

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca             # Atributo público
        self._modelo = modelo          # Atributo protegido
        self.__velocidad = 0           # Atributo privado

    def acelerar(self, incremento):
        self.__velocidad += incremento  # Método público que accede a un atributo privado
        return self.__velocidad

    def _detener(self):
        self.__velocidad = 0            # Método protegido que accede a un atributo privado
        return self.__velocidad

    def __mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self._modelo}, Velocidad: {self.__velocidad}"

    def mostrar_info_publico(self):
        return self.__mostrar_info()    # Método público que accede a un método privado


# Crear una instancia de la clase `Coche`
mi_coche = Coche("Toyota", "Corolla")

# Acceso a atributos y métodos públicos
print(mi_coche.marca)                # Salida: Toyota
print(mi_coche.acelerar(50))         # Salida: 50

# Acceso a atributos y métodos protegidos (no recomendado, pero posible)
print(mi_coche._modelo)              # Salida: Corolla
print(mi_coche._detener())           # Salida: 0

# Intento de acceso a atributos y métodos privados (producirá un error)
# print(mi_coche.__velocidad)        # AttributeError
# print(mi_coche.__mostrar_info())   # AttributeError

# Acceso a métodos privados a través de un método público
# Salida: Marca: Toyota, Modelo: Corolla, Velocidad: 0
print(mi_coche.mostrar_info_publico())

# Aunque los atributos y métodos privados están "ocultos", en realidad,
# Python usa un mecanismo llamado name mangling para renombrarlos internamente.
# Esto se puede ver si accedemos al nombre "mangleado":

# Salida: 0 (acceso directo no recomendado)
print(mi_coche._Coche__velocidad)
# Salida: Marca: Toyota, Modelo: Corolla, Velocidad: 0
print(mi_coche._Coche__mostrar_info())

# Conclusión:
# El encapsulamiento ayuda a proteger los datos internos de un objeto y define una interfaz clara
# para interactuar con él. En Python, aunque no se puede restringir completamente el acceso a los
# atributos y métodos, se puede usar convenciones de nombres y name mangling para indicar
# que ciertos componentes no deberían ser accedidos directamente desde fuera de la clase.
