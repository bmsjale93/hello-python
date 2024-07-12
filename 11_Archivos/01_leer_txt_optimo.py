### LEER ARCHIVOS DE FORMA ÓPTIMA ###
# Para leer archivos de texto de forma óptima, se utiliza el método with open() as archivo.
# Este método permite abrir el archivo y cerrarlo automáticamente al finalizar el bloque de código.
# Al usar with open() as archivo, no es necesario cerrar el archivo con archivo.close().

# Establecemos la variable con la ruta del archivo para minimizar código
archivo = "/Users/bmsjale/Desktop/GITHUB/hello-python/11_Archivos/texto_lectura.txt"

# Abrimos el archivo con el método with open() as archivo
with open(archivo, encoding="utf-8") as archivo_abierto:
    # Leemos el archivo
    contenido = archivo_abierto.read()
    # Mostramos el contenido
    print("\nLeemos el archivo completo:")
    print("------------------------------")
    print(contenido)
    print("------------------------------\n")
