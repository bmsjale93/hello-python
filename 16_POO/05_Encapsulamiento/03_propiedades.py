### PROPIEDADES ###

# Las propiedades en Python permiten gestionar el acceso a los atributos de una clase
# mediante métodos que se comportan como si fueran atributos.
# Esto permite definir comportamientos personalizados para la obtención, establecimiento y eliminación de atributos,
# mientras que se mantiene una interfaz simple y limpia para el usuario de la clase.

# Ejemplo de propiedades con `@property`, `@<propiedad>.setter` y `@<propiedad>.deleter`:

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido
        self._edad = edad      # Atributo protegido

    # Getter para `nombre`
    @property
    def nombre(self):
        return self._nombre

    # Setter para `nombre`
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str):
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena")

    # Getter para `edad`
    @property
    def edad(self):
        return self._edad

    # Setter para `edad`
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser positiva")

    # Deleter para `edad`
    @edad.deleter
    def edad(self):
        del self._edad


# Crear una instancia de la clase `Persona`
persona = Persona("Juan", 30)

# Utilizar el getter para obtener el valor del atributo `nombre`
print(persona.nombre)  # Salida: Juan

# Utilizar el setter para establecer un nuevo valor al atributo `nombre`
persona.nombre = "Pedro"
print(persona.nombre)  # Salida: Pedro

# Utilizar el getter para obtener el valor del atributo `edad`
print(persona.edad)  # Salida: 30

# Utilizar el setter para establecer un nuevo valor al atributo `edad`
persona.edad = 35
print(persona.edad)  # Salida: 35

# Intentar establecer un valor no válido al atributo `edad` (esto lanzará una excepción)
try:
    persona.edad = -5
except ValueError as e:
    print(e)  # Salida: La edad debe ser positiva

# Utilizar el deleter para eliminar el atributo `edad`
del persona.edad

# Intentar acceder al atributo `edad` después de eliminarlo (esto lanzará un AttributeError)
try:
    print(persona.edad)
except AttributeError as e:
    print(e)  # Salida: 'Persona' object has no attribute '_edad'

# En este ejemplo:
# - `@property` define el getter para el atributo.
# - `@<propiedad>.setter` define el setter para el atributo.
# - `@<propiedad>.deleter` define el deleter para el atributo.

# Las propiedades permiten añadir lógica adicional al acceder o modificar los atributos
# sin cambiar la forma en que se usan esos atributos desde fuera de la clase.
# Esto ayuda a mantener el encapsulamiento y proporciona una interfaz limpia para el usuario de la clase.

# Ejemplo con cálculo dinámico de una propiedad:


class Rectangulo:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def area(self):
        return self._ancho * self._alto

    @property
    def perimetro(self):
        return 2 * (self._ancho + self._alto)


# Crear una instancia de la clase `Rectangulo`
rectangulo = Rectangulo(4, 5)

# Acceder a las propiedades `area` y `perimetro`
print(f"Área: {rectangulo.area}")         # Salida: Área: 20
print(f"Perímetro: {rectangulo.perimetro}")  # Salida: Perímetro: 18

# En este ejemplo, `area` y `perimetro` son propiedades calculadas dinámicamente,
# y su valor se calcula cada vez que se accede a ellas, sin necesidad de métodos adicionales.