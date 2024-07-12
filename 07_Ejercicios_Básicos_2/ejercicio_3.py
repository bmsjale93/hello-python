# EJERCICIO 3

"""
Escribir un programa que calcule la serie de Fibonacci hasta un número específico de términos.
Esto significa que, en vez de mostrar todos los números primos que hay desde el 2 hasta el número
que llamammos, tenemos que mostrar lo mismo pero la serie Fibonacci entre un rango determinado.
"""

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else: 
            fibonacci_lista.append(b)
            a,b = b,a+b

resultado = fibonacci(34)
print(resultado)