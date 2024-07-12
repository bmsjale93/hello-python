### AGREGAR TEXTO EN UN TXT ###
# Para agregar texto a un archivo de texto, se utiliza el método write() de la clase file.
# Este método permite escribir texto en un archivo de texto.
# Para agregar texto a un archivo de texto, se debe abrir el archivo en modo agregar (a).

archivo = "/Users/bmsjale/Desktop/GITHUB/hello-python/11_Archivos/texto_escrito.txt"

# Abrimos el archivo en modo escritura y codificación utf-8
with open(archivo, "a", encoding="utf-8") as archivo_escritura:
    # Agrega líneas de texto al final del archivo, cada vez que lo ejecute
    # volverá a agregar las mismas lineas una y otra vez.
    archivo_escritura.write("Estamos agregando nuevas lineas al archivo.\n")
    archivo_escritura.write("Funciona muy parecido a append().\n")
    archivo_escritura.write("Este es el final del archivo.\n")
    
    # También podemos usar un bucle para agregar varias lineas en el documento
    for i in range(5):
        archivo_escritura.write(f"Esta es la linea {i+1} del archivo.\n")
    print("Se han agregado las lineas al archivo.")

