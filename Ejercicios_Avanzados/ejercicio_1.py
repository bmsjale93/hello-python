# EJERCICIO 1

"""
Hoy faltó el profesor de clases y los chicos se organizaron para hacer una clase de repaso. Uno de los alumnos va a ser
el profesor y otro va a ser el asistente.
a) Pedir la edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor.
b) El mayor es el profesor y el menor es el asistente. Mostrar en pantalla quién es el profesor y quién es el asistente.
"""

# Función para obtener el asistente y el profesor según la edad.
def obtener_compañero(cantidad_compañeros):
    
    # Creamos la lista con los compañeros
    compañeros = []
    
    # Ejecutamos un for para pedir la información de cada compañero
    for i in range(cantidad_compañeros):
        nombre = input("Ingresa el nombre del compañero: ")
        edad = int(input("Ingresa la edad del compañero: "))
        print("")
        compañero = (nombre, edad)
        
        # Agregamos la información a la lista
        compañeros.append(compañero)
    
    # Ordenándolos de menor a mayor según la edad.
    compañeros.sort(key=lambda x:x[1])
    
    # El compañero[x] devuelve una tupla con (nombre, edad) y después accedemos al nombre.
    asistente = compañeros[0][0] # Tras el orden, primer elementos por su nombre.
    profesor = compañeros[-1][0] # Tras el orden, último elemento por su nombre.
    return asistente, profesor

asistente, profesor = obtener_compañero(5)
print(f"El profesor es {profesor} y su asistente es {asistente}")