### TIPO REAL Y TIPO DECLARADO ###

# Tipo Real (Actual Type) y Tipo Declarado (Declared Type) son conceptos que se refieren a la distinción
# entre el tipo de una variable que el compilador cree que tiene (tipo declarado) y el tipo que realmente tiene
# en tiempo de ejecución (tipo real).

# Python es un lenguaje dinámico, lo que significa que las variables no tienen un tipo declarado en el sentido tradicional.
# En lugar de ello, el tipo de una variable se determina en tiempo de ejecución.

# Ejemplo:

# No declaramos el tipo explícitamente en Python. Solo asignamos un valor a una variable.
x = 10          # Python asume que x es de tipo int (número entero)
print(type(x))  # Salida: <class 'int'>

x = "Hola"      # Ahora, x es de tipo str (cadena de texto)
print(type(x))  # Salida: <class 'str'>

# Aquí, el tipo real de `x` es int cuando le asignamos un número y str cuando le asignamos una cadena.
# Python no tiene un tipo declarado para `x`, el tipo se determina en tiempo de ejecución.

# En lenguajes estáticamente tipados, el tipo declarado se especifica en el momento de la declaración de la variable.

# Ejemplo en un lenguaje estáticamente tipado (no en Python):
# int x = 10;
# x = "Hola";  # Error: No se puede asignar un valor de tipo string a una variable de tipo int.

# En Python, debido a la naturaleza dinámica del lenguaje, no necesitamos especificar un tipo declarado.
# Las variables pueden cambiar su tipo durante la ejecución del programa.

# Ejemplo con clases:
class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"


# Podemos crear una variable `mi_animal` y asignarle un objeto `Perro`.
mi_animal = Perro()
print(mi_animal.hacer_sonido())  # Salida: Guau

# Luego, podemos asignarle un objeto `Gato` a la misma variable `mi_animal`.
mi_animal = Gato()
print(mi_animal.hacer_sonido())  # Salida: Miau

# En este ejemplo, `mi_animal` no tiene un tipo declarado específico. Su tipo real cambia en tiempo de ejecución
# dependiendo del objeto que se le asigne.