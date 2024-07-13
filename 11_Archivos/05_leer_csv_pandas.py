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

# Podemos acceder a la primera fila con head() y a la última con tail()
primera_fila = df.head(1)
print(primera_fila)
print("-------------------")

# También podemos acceder a las 3 primeras filas o las que queramos
primera_fila = df.head(3)
print(primera_fila)
print("-------------------")

# Por otro lado, podemos acceder a las 3 últimas filas o las que queramos
ultimas_filas = df.tail(3)
print(ultimas_filas)
print("-------------------")

# También podemos acceder a la cantidad de filas y columnas de un dataframe con la función shape
filas_y_columnas = df.shape
print(filas_y_columnas)
print("-------------------")

# Como devuelve una tupla, podemos desempaquetarla
filas, columnas = df.shape
print(f"Las filas totales son: {filas}\nLas columnas totales son: {columnas}")
print("-------------------")

# De forma más estadística, podemos utilizar la función describe()
estadisticas = df.describe()
print(estadisticas)
print("-------------------")

# SLICING
# Podemos seleccionar un rango de filas y columnas con slicing
cadena = "0123456789"
print(cadena[0:5])  # 01234
print("-------------------")

# Con el slicing podemos acceder a elementos específicos con loc[]
elemento_especifico = df.loc[0, 'nombre']
print(elemento_especifico)
print("-------------------")

# Otra forma de acceder a elementos específicos es con iloc[]
elemento_especifico = df.iloc[0, 0]
print(elemento_especifico)
print("-------------------")

# Además, podemos acceder a todas las filas de una columna específica
# De la siguiente forma, le decimos que acceda a todos los elementos de la columna 1
columna_especifica = df.iloc[:,1]
print(columna_especifica)
print("-------------------")

# También funciona al revés y podemos acceder a todas las columnas de una fila específica
fila_especifica = df.iloc[2,:]
print(fila_especifica)
print("-------------------")

# Podemos establecer condiciones, como seleccionar todas las filas donde la edad sea mayor a 25
condicion = df.loc[df["edad"]>25,:]
print(condicion)
print("-------------------")
