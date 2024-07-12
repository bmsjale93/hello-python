### CONJUNTOS AVANZADOS ###

# Creando un conjunto con set()
conjunto = set(["dato1", "dato2", "dato3", "dato4", "dato5"])
print(conjunto)

# Ahora, crearemos un conjunto cque tenga una tupla de datos
conjunto_con_tupla = (["dato1", "dato2", ("datolista1", "datolista2"), "dato4", "dato5"])
print(conjunto_con_tupla)

# Con una lista no funciona, ya que las listas son modificables y los conjuntos no pueden tener elementos modificables
#conjunto_con_lista= (["dato1", "dato2", ["datolista1", "datolista2"], "dato4", "dato5"])

# Metiendo un conjunto dentro de otro conjunto
conjunto1 = {"dato1", "dato2", "dato3"}
# conjunto2 = {conjunto, "dato4", "dato5"} # Esto no funcionará

# Pero si lo hacemos con un conjunto congelado, sí funcionará
# Para esto, utilizamos la función frozenset()

conjunto1 = frozenset(["dato1", "dato2", "dato3"]) # Esto crea un conjunto inmutable
conjunto2 = {conjunto1, "dato4", "dato5"} # Esto sí funcionará
print(conjunto2)

# TEORIA DE CONJUNTOS
# Comprobamos si un conjunto pertenece a otro
conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

# Verificamos si conjunto2 es subconjunto de conjunto1
resultado = conjunto2.issubset(conjunto1) # Devuelve True si conjunto2 es subconjunto de conjunto1
print(resultado)

# Otra forma de verificar si uno es subconjunto de otro
resultado = conjunto2 <= conjunto1 # Esto funciona exactamente igual
print(resultado)

# También podemos verificar si un conjunto es superconjunto de otro
resultado = conjunto1.issuperset(conjunto2) # Devuelve True si conjunto1 es superconjunto de conjunto2
print(resultado)

# Otra forma de verificar si uno es superconjunto de otro
resultado = conjunto1 >= conjunto2 # Esto funciona exactamente igual
print(resultado)

# Finalmente, podemos verificar si tienen elementos en común
resultado = conjunto1.isdisjoint(conjunto2) # Devuelve True si no tienen elementos en común
print(resultado)

# Unión de conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
union = conjunto1 | conjunto2
print(union)