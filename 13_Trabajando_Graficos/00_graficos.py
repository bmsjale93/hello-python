### GRÁFICOS LINEALES ###
"""
EJERCICIO 1:
Planteamos un problema sencillo:
Entendemos que los pedos son un indicador de problemas estomacales, entonces, hemos creado
un detector de pedos y cada vez que nos tiramos un pedo, este se registra. Después de un tiempo, 
tengo un archivo CSV con dos columnas, una con la fecha y otra con la cantidad.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./pedos.csv")
# Creamos el Gráfico de Líneas con Seaborn
sns.lineplot(x="fecha", y="pedos", data=df)
# Creamos un punto en el gráfico
plt.plot("01-06", 16, "o")
# Mostramos el gráfico
plt.show()

"""
EJERCICIO 2:
Alejandro ya se graduó y está trabajando de programador pero, además de programador, tiene
otras fuentes de ingresos, lo que queda registrado en un CSV. Tenemos que mostrar los ingresos
utilizando un gráfico de barras.
"""

df = pd.read_csv("./ingresos.csv")

# Creamos el Gráfico de Líneas con Seaborn
sns.barplot(x="fuente", y="ingresos", data=df)

# Si queremos, podemos mostrar el total de ingresos
total_ingresos = df["ingresos"].sum()
print(f"Total de Ingresos: {total_ingresos}€")

# Mostramos el gráfico
plt.show()
