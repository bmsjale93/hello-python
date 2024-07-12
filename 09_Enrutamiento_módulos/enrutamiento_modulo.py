# Si el módulo estuviera dentro de una carpeta, la importación sería de la siguiente manera:
import funciones.saludar as m_saludar

# Si el módulo estuviera fuera, la importación sería de la siguiente manera:
# Con sys agregamos la ruta del módulo
import sys
sys.path.append("/Users/bmsjale/Desktop/GITHUB/hello-python/09.1_EnrutamientoPrueba")
import saludar as m_saludar

print(m_saludar.saludar("Alex"))