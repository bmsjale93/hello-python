### POLIFORMISMO POR SOBRECARGA ###

# Polimorfismo por Sobrecarga en Python

# En muchos lenguajes de programación, la sobrecarga de métodos permite definir múltiples métodos con el mismo nombre
# pero con diferentes parámetros. Sin embargo, Python no soporta sobrecarga de métodos de la misma manera que otros lenguajes.
# En su lugar, podemos lograr un comportamiento similar utilizando argumentos por defecto o argumentos *args y **kwargs.

# Ejemplo sencillo:
# Definimos una clase `Calculadora` con un método `sumar` que puede aceptar dos o tres argumentos.

class Calculadora:
    def sumar(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

# Aquí, el método `sumar` se comporta de manera diferente según el número de argumentos proporcionados.
# Esto es un ejemplo de cómo se puede simular la sobrecarga de métodos en Python.

calc = Calculadora()

# Llamamos al método `sumar` con dos argumentos.
resultado1 = calc.sumar(2, 3)
# Salida: Resultado de sumar 2 y 3: 5
print(f"Resultado de sumar 2 y 3: {resultado1}")

# Llamamos al método `sumar` con tres argumentos.
resultado2 = calc.sumar(2, 3, 4)
# Salida: Resultado de sumar 2, 3 y 4: 9
print(f"Resultado de sumar 2, 3 y 4: {resultado2}")

# En este caso, aunque Python no permite sobrecarga de métodos de manera tradicional,
# logramos un comportamiento similar utilizando argumentos por defecto.
