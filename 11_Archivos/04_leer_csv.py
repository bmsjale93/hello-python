### LEER ARCHIVOS CSV ###
# Para leer archivos CSV en Python, puedes usar el módulo incorporado csv.
# Este módulo permite tanto leer como escribir archivos CSV.
import csv

archivo = "/Users/bmsjale/Desktop/GITHUB/hello-python/11_Archivos/datos.csv"

with open(archivo) as archivo_csv:
    reader = csv.reader(archivo_csv)
    for row in reader:
        print(row)