## IMPORTACIÓN DE MÓDULOS ##

# Los módulos son archivos que contienen definiciones y declaraciones de Python
# Los módulos pueden definir funciones, clases y variables
# Para usar un módulo, primero debemos importarlo
# import modulo_saludar as m_saludar

# Si queremos utilizar una o varias funciones de un módulo, podemos hacerlo de la siguiente manera:
from modulo_saludar import saludar as s_normal, saludar_raro as s_raro
import modulo_saludar as m_saludar

# También podríamos importar directamente todo el módulo
# from modulo_saludar import * (No recomendado)

# Creamos las variables con los saludos
saludo = s_normal("Alex")
saludo_raro = s_raro("Pedro")

# Mostramos los resultados
print(saludo)
print(saludo_raro)

# Para ver las propiedades y métodos de el namespace
#print(dir(m_saludar)

# Accedemos al nombre de este módulo
print(__name__)

# Accedemos al nombre del módulo que se está ejecutando
print(m_saludar.__name__)