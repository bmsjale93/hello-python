"""
Tenemos dos listas con nombres y apellidos, tenemos que escribir los datos en un archivo de texto
óptima utilizando un bucle for. 
"""

nombre = ["Alex", "Juan", "Pedro", "Jesus", "Maria", "Ana"]
apellidos = ["Garcia", "Perez", "Lopez", "Gonzalez", "Rodriguez", "Fernandez"]

# Registrar la información en un archivo TXT de forma óptima
with open("nombres_y_apellidos.txt", "w") as archivo:
    archivo.writelines("Los datos son:\n\n")
    # Se puede escribir en una sola línea
    #[archivo.writelines(f"Nombre: {n}\nApellido: {a}\n--------------------\n") for n, a in zip(nombre, apellidos)]
    
    # O se puede escribir en varias líneas, dejamos esta por comprensión
    for n, a in zip(nombre, apellidos):
        archivo.writelines(f"Nombre: {n}\nApellido: {a}\n--------------------\n")