### SETTERS Y GETTERS ###

# Los setters y getters son métodos utilizados para controlar el acceso a los atributos de una clase.
# Los getters se utilizan para obtener el valor de un atributo y los setters para establecer o modificar el valor de un atributo.
# En Python, los setters y getters se implementan utilizando propiedades (properties) y el decorador `@property`.

# Ejemplo:

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
        self._nombre = nuevo_nombre

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


# Crear una instancia de la clase `Persona`
persona = Persona("Juan", 30)

# Utilizar los getters para obtener los valores de los atributos
print(persona.nombre)  # Salida: Juan
print(persona.edad)    # Salida: 30

# Utilizar los setters para establecer nuevos valores a los atributos
persona.nombre = "Pedro"
persona.edad = 35

# Verificar los nuevos valores utilizando los getters
print(persona.nombre)  # Salida: Pedro
print(persona.edad)    # Salida: 35

# Intentar establecer una edad no válida (esto lanzará una excepción)
try:
    persona.edad = -5
except ValueError as e:
    print(e)  # Salida: La edad debe ser positiva

# En este ejemplo:
# - `@property` define el getter de un atributo.
# - `@<nombre_atributo>.setter` define el setter de un atributo.
# Estos métodos permiten controlar cómo se acceden y modifican los atributos, añadiendo lógica adicional si es necesario.

# Otra forma de implementar getters y setters en Python es utilizando métodos tradicionales:
class PersonaAlt:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Método getter para `nombre`
    def get_nombre(self):
        return self._nombre

    # Método setter para `nombre`
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # Método getter para `edad`
    def get_edad(self):
        return self._edad

    # Método setter para `edad`
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser positiva")


# Crear una instancia de la clase `PersonaAlt`
persona_alt = PersonaAlt("Maria", 28)

# Utilizar los métodos getter y setter
print(persona_alt.get_nombre())  # Salida: Maria
print(persona_alt.get_edad())    # Salida: 28

persona_alt.set_nombre("Lucia")
persona_alt.set_edad(32)

print(persona_alt.get_nombre())  # Salida: Lucia
print(persona_alt.get_edad())    # Salida: 32

# En resumen, los setters y getters en Python son métodos que permiten controlar el acceso y modificación de los atributos
# de una clase, proporcionando una manera de añadir lógica adicional cuando se accede o se modifica un atributo.
