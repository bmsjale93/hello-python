### ESCRIBIR UN TXT ###
# Para escribir un archivo de texto, se utiliza el método write() de la clase file.
# Este método permite escribir texto en un archivo de texto.
# Para escribir un archivo de texto, se debe abrir el archivo en modo escritura (w).
# Si no encontrara el archivo, lo creará.

archivo = "/Users/bmsjale/Desktop/GITHUB/hello-python/11_Archivos/texto_escrito.txt"

# Abrimos el archivo en modo escritura y codificación utf-8
with open(archivo, "w", encoding="utf-8") as archivo_escritura:
    # Sobreescribimos el archivo
    archivo_escritura.write("Hola, este es un archivo de texto.\n")
    archivo_escritura.write("Aquí se pueden escribir varias líneas.\n")
    archivo_escritura.write("Este es el final del archivo.")
    
# Con writelines se pueden escribir varias líneas de texto a la vez
with open(archivo, "w", encoding="utf-8") as archivo_escritura:
    archivo_escritura.writelines(["Esta es una linea nueva de texto.\n", "Esta es otra linea de texto.\n"])
