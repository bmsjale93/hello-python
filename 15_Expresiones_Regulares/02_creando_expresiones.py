### CREANDO EXPRESIONES REGULARES ###

# Para este ejercicio, detectaremos un número CABA y lo ocultaremos
import re

# Definimos el texto
texto = "Hola Pedro, mi número es: +54 11 4321-4321"

# Creamos el patrón para detectar un número de CABA
pattern = r"\+\d{2}\s\d{2}\s\d{4}-\d{4}"

# Reemplazaremos el número por otro texto
reemplazo = re.sub(pattern, "(Número oculto)", texto)

# Mostramos el texto original y el texto modificado
print(f"Texto original: {texto}")
print(f"Texto modificado: {reemplazo}")