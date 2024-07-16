### ANALIZANDO EXPRESIONES REGULARES ###

# PRIMERA EXPRESIÓN REGULAR
# Importamos el módulo re
import re

# Definimos el texto
text = "The quick brown fox jumps over the lazy dog"

# Definimos la expresión regular. La explicación es la siguiente:
    # ^: Coincide con el comienzo de una cadena.
    # The: Coincide con la cadena 'The'.
    # .*: Coincide con cualquier carácter excepto un carácter de nueva línea, 0 o más repeticiones.
    # dog$: Coincide con la cadena 'dog' al final de la cadena.
x = re.search("^The.*dog$", text)
print("--------------------")

# Comprobamos si hay coincidencias
if x:
    print("YES! We have a match!")
else:
    print("No match")

print("--------------------")

# SEGUNDA EXPRESIÓN REGULAR
# Definimos el texto
text = "La fecha es 23/06/2021 y el teléfono es +1-555-555-5555"

# Definimos el patrón a buscar. La explicación es la siguiente:
    # \d: Coincide con cualquier dígito.
    # {2}: Coincide con exactamente dos repeticiones del carácter anterior.
    # /: Coincide con el carácter '/'.
    # \d: Coincide con cualquier dígito.
    # {2}: Coincide con exactamente dos repeticiones del carácter anterior.
    # /: Coincide con el carácter '/'.
    # \d: Coincide con cualquier dígito.
    # {4}: Coincide con exactamente cuatro repeticiones del carácter anterior.
pattern = r"\d{2}/\d{2}/\d{4}"

# Reemplazaremos el patrón por otro texto.
replacement = "Fecha oculta"

# Reemplazaremos todas las apariciones del patrón en el texto.
new_text = re.sub(pattern, replacement, text)

# Mostramos el texto original y el texto modificado.
print(f"Texto original: {text}")
print(f"Texto modificado: {new_text}")
print("--------------------")


# TERCERA EXPRESIÓN REGULAR
# Definimos el texto
text = "Reemplazando todas las vocales por el asterisco"

# Reemplazaremos todas las vocales por el asterisco.
new_text = re.sub(r"[aeiou]", "*", text)

# Mostramos el texto original y el texto modificado.
print(f"Texto original: {text}")
print(f"Texto modificado: {new_text}")
print("--------------------")


# CUARTA EXPRESIÓN REGULAR
# Definimos el texto
email = "example@example.com"

# Patrón para buscar un email.
pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Comprobamos si el email es válido.
result = re.match(pattern, email)

if result:
    print("Email válido")
else:
    print("Email no válido")

print("--------------------")


# QUINTA EXPRESIÓN REGULAR
# Definimos el texto
text = "Este es un ejemplo de una página web: https://www.example.com y tambiém podemos visitar https://www.example2.com"

# Definimos el patrón a buscar.
pattern = "https://www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Buscamos todas las coincidencias del patrón en el texto.
result = re.findall(pattern, text)

# Mostramos las coincidencias.
print(f"Las coincidencias encontradas son: {result}")
print("--------------------")