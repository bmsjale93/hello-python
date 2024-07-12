### LEER ARCHIVOS TXT ###
# Para leer un archivo de texto, se utiliza la función open() con el modo de lectura 'r'.
# Luego se puede leer el contenido del archivo con el método read().

# Creamos una función para abrir el archivo
def abrir_archivo():
    archivo = open(
        "/Users/bmsjale/Desktop/GITHUB/hello-python/11_Archivos/texto_lectura.txt", encoding="utf-8")
    return archivo

# Abrimos el archivo
archivo = abrir_archivo()
archivo_leido = archivo.read()
print(f"Leemos el archivo completo:\n{archivo_leido}")
print("-------------------")
# Cerramos el archivo
archivo.close()

# Leer linea por linea
archivo = abrir_archivo()
leer_lineas = archivo.readlines()
print(f"Leemos el archivo linea por linea:\n{leer_lineas}")
print("-------------------")
archivo.close()

# Leer una sola línea
archivo = abrir_archivo()
linea = archivo.readline()
print(f"Leemos la primera línea del archivo:\n{linea}")
print("-------------------")
archivo.close()

print(linea)