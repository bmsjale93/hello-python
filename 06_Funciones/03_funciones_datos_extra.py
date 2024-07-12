### FUNCIONES CON DATOS EXTRA ###

print("-------------------")
def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultado = frase("Alex", "Delgado", "inteligente")
print(frase_resultado)
print("-------------------")

# Podemos forzar a que los argumentos sean pasados en el orden correcto
def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultado = frase(adjetivo="inteligente", nombre="Alex", apellido="Delgado")
print(frase_resultado)
print("-------------------")

# También podemos forzar los argumentos al pasar los parámetros
def frase(nombre, apellido, adjetivo = "tonto"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultado = frase("Alex", "Delgado")
print(frase_resultado)
print("-------------------")

# Estos parámetros que pasamos por la función serían los valores por defecto
# Esto podemos modificarlo en la llamada de la función
def frase(nombre, apellido, adjetivo="tonto"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultado = frase("Alex", "Delgado", "inteligente")
print(frase_resultado)
print("-------------------")
