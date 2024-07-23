### ENLACES DINÁMICOS Y ESTÁTICOS ###

# Enlaces Dinámicos (Dynamic Binding) y Enlaces Estáticos (Static Binding) son conceptos relacionados
# con el momento en que se determina a qué método o variable se refiere una llamada en tiempo de ejecución (dinámico)
# o en tiempo de compilación (estático).

# Enlace Estático:
# En lenguajes con enlace estático, el método o variable que se llama se determina en tiempo de compilación.
# Python no es un lenguaje estáticamente enlazado, pero podemos ilustrar este concepto con una estructura básica.

# Ejemplo (simulado):
class AnimalEstatico:
    def hacer_sonido(self):
        print("Sonido genérico")


class PerroEstatico(AnimalEstatico):
    def hacer_sonido(self):
        print("Guau")


# En un lenguaje con enlace estático, la llamada a `hacer_sonido` se determina en tiempo de compilación.
animal_estatico = AnimalEstatico()
animal_estatico.hacer_sonido()  # Salida: Sonido genérico

perro_estatico = PerroEstatico()
perro_estatico.hacer_sonido()   # Salida: Guau

# Python usa enlace dinámico, lo que significa que las decisiones de qué método llamar se toman en tiempo de ejecución.

# Enlace Dinámico:
# En Python, el método o variable que se llama se determina en tiempo de ejecución.
# Esto permite la flexibilidad de usar polimorfismo y herencia de manera efectiva.

# Ejemplo:


class AnimalDinamico:
    def hacer_sonido(self):
        print("Sonido genérico")


class PerroDinamico(AnimalDinamico):
    def hacer_sonido(self):
        print("Guau")

# En Python, la llamada al método `hacer_sonido` se resuelve en tiempo de ejecución.
def hacer_sonido_animal(animal):
    animal.hacer_sonido()


mi_animal = AnimalDinamico()
mi_perro = PerroDinamico()

hacer_sonido_animal(mi_animal)  # Salida: Sonido genérico
hacer_sonido_animal(mi_perro)   # Salida: Guau

# En este ejemplo, `hacer_sonido_animal` utiliza enlace dinámico para determinar qué método `hacer_sonido` llamar
# en función del objeto que se le pasa en tiempo de ejecución.

# Conclusión:
# Python usa enlace dinámico, lo que permite una mayor flexibilidad y el uso de técnicas como el polimorfismo y la herencia.
# El enlace estático se usa principalmente en lenguajes compilados y determina las referencias en tiempo de compilación.
