### ITERANDO SOBRE DICCIONARIOS ###

diccionario = {
    "nombre": "Alex",
    "apellido": "Delgado",
    "edad": 30,
    "ciudad": "Sevilla"
}

# Para iterar sobre las claves
for clave in diccionario:
    print(f"La clave es: {clave}")
print("---------------------------")

#Para iterar sobre los valores, utilizamos el método items()
for datos in diccionario.items():
    clave = datos[0]
    valor = datos[1]
    print(f"La clave es: {clave} y el valor es: {valor}")

print("---------------------------")

# Otra forma de hacerlo es desempaquetando la tupla
for clave, valor in diccionario.items():
    print(f"La clave es: {clave} y el valor es: {valor}")