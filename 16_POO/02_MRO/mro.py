### MRO: METHOD RESOLUTION ORDER ###
# El MRO es el orden en el que se van a buscar los métodos en las clases padres.
# En Python, el MRO se calcula utilizando el algoritmo C3.
# El algoritmo C3 es un algoritmo de ordenamiento topológico.

class A:
    def hablar(self):
        print("Hablando desde la clase A")
        

class B(A):
    def hablar(self):
        print("Hablando desde la clase B")


class C(A):
    def hablar(self):
        print("Hablando desde la clase C")


class D(B, C):
    def hablar(self):
        print("Hablando desde la clase D")

# El orden de resolución de métodos (MRO) es el siguiente:
# D -> B -> C -> A
# Esto es porque la clase D hereda de B y C, y B y C heredan de A.
# En otras palabras, la clase D hereda de B, C y A.

d = D()
print(D.mro())