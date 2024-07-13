### LEER CSV CON PANDAS ###
# Pandas es una librería de Python que proporciona estructuras de datos y herramientas de análisis de datos.
# Pandas es una librería de código abierto que proporciona estructuras de datos de alto rendimiento y fácil de usar.
# Es una de las librerías más populares para trabajar con datos tabulares.
# Pandas es especialmente útil para trabajar con datos estructurados.

import pandas as pd

# Usando la función read_csv() de pandas, podemos leer un archivo CSV.
# Usamos DF para referirnos a un DataFrame, que es una estructura de datos de Pandas (parecido a una hoja de cálculo)
df = pd.read_csv('./datos.csv')
print(df)
print("-------------------")

# También podemos pedir una columna específica
print(df['nombre'])
print("-------------------")

# Podemos modificar el nombre de las cabeceras cuando leemos un archivo
df = pd.read_csv('./datos.csv', header=None, names=['name', 'lastname', 'age'])
print(df)
print("-------------------")

# Podemos ordenar el dataframe por la edad
df = pd.read_csv('./datos.csv')
df_ordenado = df.sort_values("edad")
print(df_ordenado)
print("-------------------")

# Ordenándolo de forma descendente
df_ordenado = df.sort_values("edad", ascending=False)
print(df_ordenado)
print("-------------------")

# CONCATENAR DATAFRAMES
# Podemos concatenar dos dataframes con la función concat()
df = pd.read_csv('./datos.csv')
df2 = pd.read_csv('./datos.csv')
df_concatenado = pd.concat([df, df2])
print(df_concatenado)
print("-------------------")



# SLICING
# Podemos seleccionar un rango de filas y columnas con slicing
cadena = "0123456789"
print(cadena[0:5])  # 01234

