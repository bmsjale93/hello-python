### EXPRESIONES REGULARES ###
# Para empezar, importamos el módulo re
# Este módulo proporciona operaciones de coincidencia de expresiones regulares similares a las que se encuentran en Perl.

import re
texto = """Hola, mi nombre es Juan y mi número de teléfono es 123456789. ¿Cómo estás?
Esta es la segunda línea de texto.
Y esta es la tercera y última línea de texto."""

# Utilizamos la función search() para buscar un patrón en un texto
resultado = re.search("Hola", texto)

# Con findall podemos buscar todas las coincidencias de un patrón en un texto
# Podemos utilizar flags para ignorar mayúsculas y minúsculas
resultado2 = re.findall("Esta", texto, flags=re.IGNORECASE)

# Imprimimos el resultado
print("--------------------")
print(f"El primer resultado nos dice:\n{resultado}\n\nEl segundo resultado nos dice:\n{resultado2}")
print("--------------------")

# EXPRESIONES REGULARES

# \d: Coincide con cualquier dígito decimal; es equivalente a la clase [0-9].
# Con r podemos indicar que vamos a utilizar expresiones regulares
resultado = re.findall(r"\d", texto)
print(f"Resultado de buscar todos los dígitos en el texto:\n{resultado}")
print("--------------------")

# \D: Coincide con cualquier carácter que no sea un dígito decimal; es equivalente a la clase [^0-9].
resultado = re.findall(r"\D", texto)
print(f"Resultado de buscar todos los caracteres que no sean dígitos en el texto:\n{resultado}")

# \w: Coincide con cualquier carácter alfanumérico; es equivalente a la clase [a-zA-Z0-9_].
resultado = re.findall(r"\w", texto)
print(f"Resultado de buscar todos los caracteres alfanuméricos en el texto:\n{resultado}")
print("--------------------")

# \W: Coincide con cualquier carácter que no sea alfanumérico; es equivalente a la clase [^a-zA-Z0-9_].
resultado = re.findall(r"\W", texto)
print(f"Resultado de buscar todos los caracteres que no sean alfanuméricos en el texto:\n{resultado}")
print("--------------------")

# \s: Coincide con cualquier carácter de espacio en blanco; es equivalente a [ \t\n\r\f\v].
resultado = re.findall(r"\s", texto)
print(f"Resultado de buscar todos los caracteres de espacio en blanco en el texto:\n{resultado}")
print("--------------------")

# \S: Coincide con cualquier carácter que no sea un espacio en blanco; es equivalente a [^ \t\n\r\f\v].
resultado = re.findall(r"\S", texto)
print(f"Resultado de buscar todos los caracteres que no sean espacios en blanco en el texto:\n{resultado}")
print("--------------------")

# .: Coincide con cualquier carácter excepto un carácter de nueva línea.
resultado = re.findall(r".", texto)
print(f"Resultado de buscar todos los caracteres en el texto:\n{resultado}")
print("--------------------")

# \n: Coincide con un carácter de nueva línea.
resultado = re.findall(r"\n", texto)
print(f"Resultado de buscar todos los caracteres de nueva línea en el texto:\n{resultado}")
print("--------------------")

# ^: Coincide con el comienzo de una cadena. Con la flag re.M tratamos el texto como Multilínea
resultado = re.findall(r"^Hola", texto,flags=re.M)
print(f"Resultado de buscar 'Hola' al principio del texto:\n{resultado}")
print("--------------------")

# \: Cancela el significado especial de un carácter.
resultado = re.findall(r"\.", texto)
print(f"Resultado de buscar el punto en el texto:\n{resultado}")
print("--------------------")

# $: Coincide con el final de una cadena.
resultado = re.findall(r"texto\.$", texto)
print(f"Resultado de buscar 'texto.' al final del texto:\n{resultado}")
print("--------------------")

# *: Coincide con 0 o más repeticiones del carácter anterior.
resultado = re.findall(r"Esta*", texto)
print(f"Resultado de buscar 'Esta' o 'Estaa' en el texto:\n{resultado}")
print("--------------------")

# +: Coincide con 1 o más repeticiones del carácter anterior.
resultado = re.findall(r"Esta+", texto)
print(f"Resultado de buscar 'Esta' o 'Estaa' en el texto:\n{resultado}")
print("--------------------")

# ?: Coincide con 0 o 1 repetición del carácter anterior.
resultado = re.findall(r"Esta?", texto)
print(f"Resultado de buscar 'Esta' o 'Est' en el texto:\n{resultado}")
print("--------------------")

# {n}: Coincide exactamente con n repeticiones del carácter anterior.
resultado = re.findall(r"Esta{2}", texto)
print(f"Resultado de buscar 'Estaa' en el texto:\n{resultado}")
print("--------------------")

# {n,}: Coincide con n o más repeticiones del carácter anterior.
resultado = re.findall(r"Esta{1,}", texto)
print(f"Resultado de buscar 'Esta' o 'Estaa' en el texto:\n{resultado}")
print("--------------------")

# {,n}: Coincide con n o menos repeticiones del carácter anterior.
resultado = re.findall(r"Esta{,2}", texto)
print(f"Resultado de buscar 'Esta' o 'Est' en el texto:\n{resultado}")
print("--------------------")

# {n,m}: Coincide con al menos n y como máximo m repeticiones del carácter anterior.
resultado = re.findall(r"Esta{1,2}", texto)
print(f"Resultado de buscar 'Esta' o 'Estaa' en el texto:\n{resultado}")
print("--------------------")

# [abc]: Coincide con cualquiera de los caracteres a, b o c.
resultado = re.findall(r"[abc]", texto)
print(f"Resultado de buscar 'a', 'b' o 'c' en el texto:\n{resultado}")
print("--------------------")

# [^abc]: Coincide con cualquier carácter que no sea a, b o c.
resultado = re.findall(r"[^abc]", texto)
print(f"Resultado de buscar cualquier carácter que no sea 'a', 'b' o 'c' en el texto:\n{resultado}")
print("--------------------")

# |: Coincide con cualquiera de las expresiones a su izquierda o derecha.
resultado = re.findall(r"Hola|Juan", texto)
print(f"Resultado de buscar 'Hola' o 'Juan' en el texto:\n{resultado}")
print("--------------------")

# TRABAJANDO CON EXPRESIONES REGULAES
# Ahora, crearemos una cadea que busque un número, seguido de un punto y un espacio
resultado = re.findall(r"\d\.\s", texto)
print(f"Resultado de buscar un número, un punto y un espacio en el texto:\n{resultado}")
print("--------------------")

