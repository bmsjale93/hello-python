# Métodos Dunder o Especiales en Python

# Los métodos Dunder (Double UNDERscore) o especiales son métodos que tienen un propósito especial en Python.
# Estos métodos están rodeados por dos guiones bajos (por ejemplo, `__init__`) y permiten definir comportamientos específicos
# para objetos y clases. Son una parte fundamental del protocolo de clases en Python y se usan para sobrecargar
# operadores, inicializar objetos, definir representaciones, entre otros.

# Aquí hay algunos métodos Dunder comunes y su uso:

# 1. `__init__(self, ...)`: Método constructor, se llama cuando se crea una instancia de la clase.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# Crear una instancia de `Persona`
persona = Persona("Juan", 30)
print(persona.nombre)  # Salida: Juan
print(persona.edad)    # Salida: 30


# 2. `__str__(self)`: Define la representación en cadena de un objeto, usada por `str()` y `print()`.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

# Crear una instancia de `Persona`
persona = Persona("Juan", 30)
print(persona)  # Salida: Persona(nombre=Juan, edad=30)


# 3. `__repr__(self)`: Define la representación oficial de un objeto, usada por `repr()` y en la consola.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"

# Crear una instancia de `Persona`
persona = Persona("Juan", 30)
print(repr(persona))  # Salida: Persona('Juan', 30)


# 4. `__len__(self)`: Define el comportamiento de la función `len()`.
class Contenedor:
    def __init__(self, elementos):
        self.elementos = elementos

    def __len__(self):
        return len(self.elementos)

# Crear una instancia de `Contenedor`
contenedor = Contenedor([1, 2, 3, 4])
print(len(contenedor))  # Salida: 4


# 5. `__getitem__(self, key)`: Define el comportamiento de acceso a elementos, como `obj[key]`.
class Contenedor:
    def __init__(self, elementos):
        self.elementos = elementos

    def __getitem__(self, index):
        return self.elementos[index]


# Crear una instancia de `Contenedor`
contenedor = Contenedor([1, 2, 3, 4])
print(contenedor[1])  # Salida: 2


# 6. `__setitem__(self, key, value)`: Define el comportamiento de asignación a elementos, como `obj[key] = value`.
class Contenedor:
    def __init__(self, elementos):
        self.elementos = elementos

    def __setitem__(self, index, value):
        self.elementos[index] = value

# Crear una instancia de `Contenedor`
contenedor = Contenedor([1, 2, 3, 4])
contenedor[1] = 20
print(contenedor[1])  # Salida: 20


# 7. `__delitem__(self, key)`: Define el comportamiento de eliminación de elementos, como `del obj[key]`.
class Contenedor:
    def __init__(self, elementos):
        self.elementos = elementos

    def __delitem__(self, index):
        del self.elementos[index]

# Crear una instancia de `Contenedor`
contenedor = Contenedor([1, 2, 3, 4])
del contenedor[1]
print(contenedor.elementos)  # Salida: [1, 3, 4]


# 8. `__iter__(self)`: Define el comportamiento de iteración, como en un bucle `for`.
class Contenedor:
    def __init__(self, elementos):
        self.elementos = elementos

    def __iter__(self):
        return iter(self.elementos)


# Crear una instancia de `Contenedor`
contenedor = Contenedor([1, 2, 3, 4])
for elemento in contenedor:
    print(elemento)
# Salida:
# 1
# 2
# 3
# 4


# 9. `__call__(self, ...)`: Permite que un objeto sea llamado como una función.
class Saludo:
    def __init__(self, nombre):
        self.nombre = nombre

    def __call__(self, saludo):
        return f"{saludo}, {self.nombre}!"

# Crear una instancia de `Saludo`
saludar = Saludo("Juan")
print(saludar("Hola"))  # Salida: Hola, Juan!


# 10. `__eq__(self, other)`: Define el comportamiento del operador de igualdad (`==`).
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, other):
        return self.nombre == other.nombre and self.edad == other.edad

# Crear instancias de `Persona`
persona1 = Persona("Juan", 30)
persona2 = Persona("Juan", 30)
persona3 = Persona("Pedro", 25)

print(persona1 == persona2)  # Salida: True
print(persona1 == persona3)  # Salida: False