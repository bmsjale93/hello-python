# EJERCICIO 1

"""
Si decimos que cada persona promedio habla 2 palabras por segundo, resuelve:
a) Pedirle al usuario que diga cualquier texto real y:
    - Calcular cuánto tardaría en decir esa frase.
    - ¿Cuántas palabras dijo?
    
b) Si se tarda más de 1 minuto:
    - Decirle: "Demasiado contexto."
    
c) Dalto habla un 30% más rápido:
    - ¿Cuánto tardaría él en decirlo?
"""

# EJERCICIO A & B
frase = input("Introduce un texto y calcularemos cuánto tardarías si tuvieras que decirla en voz alta: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

print("-------------------------------")
print(f"Dijiste {cantidad_de_palabras} palabras.")

if cantidad_de_palabras > 120:  # 120 palabras equivale a un minuto hablando.
    print("Demasiado contexto rey, reduce.")
else:
    print(f"Tardarías {cantidad_de_palabras/2} segundos en decirla.")
    print(f"Dalto lo diría en {round(cantidad_de_palabras / 2 / 1.3, 2)} segundos.") # Round ayuda a redondear a 2 decimales -> round(valor, decimales)
    
print("-------------------------------")
