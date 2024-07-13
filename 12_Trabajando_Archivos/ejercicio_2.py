"""
EJERCICIO 1
Cambiar el tipo de datos de una columna.
"""
import pandas as pd
df = pd.read_csv('./datos.csv')

# Cambiamos el tipo de dato de una columna, en este caso edad lo pasamos a string
df["edad"] = df["edad"].astype(str)
print(df["edad"])
print(type(df["edad"][0]))

# También podemos reemplazar valores
df["nombre"].replace("Alex", "Alejandro", inplace=True)
print(df["nombre"])
print("-----------------------------------")

"""
EJERCICIO 2
Si tenemos un archivo donde faltan o sobran datos, como podemos eliminar esas filas con datos faltantes.
"""
df = pd.read_csv('./datos_malo.csv')
print("Leyendo el CSV sin limpiar:\n")
print(df)
print("-----------------------------------")
df = df.dropna()
print("Leyendo el CSV limpio:\n")
print(df)
print("-----------------------------------")

"""
EJERCICIO 3
En nuestro archivo, tenemos filas que están repetidas varias veces, como podemos eliminar esas filas duplicadas.
"""
df = pd.read_csv('./datos_filas_duplicadas.csv')
print("Leyendo el CSV con filas repetidas:\n")
print(df)
print("-----------------------------------")
df = df.drop_duplicates()
print("Leyendo el CSV limpio:\n")
print(df)
print("-----------------------------------")

"""
EJERCICIO 4
En el archivo con las filas duplicadas, guardalo una vez limpio en un nuevo archivo CSV.
"""
df.to_csv("datos_limpios.csv", index=False)
