### OPERADORES DE COMPARACIÓN ###

# IGUALDAD
# Compara si dos valores son iguales
es_igual_que = 5 == 6 # False

# DISTINTO
# Compara si dos valores son distintos
es_distinto_que = 5 != 6 # True

# MAYOR QUE
# Compara si un valor es mayor que otro
es_mayor_que = 5 > 6 # False

# MENOR QUE
# Compara si un valor es menor que otro
es_menor_que = 5 < 6 # True

# MAYOR O IGUAL QUE
# Compara si un valor es mayor o igual que otro
es_mayor_o_igual_que = 5 >= 6 # False

# MENOR O IGUAL QUE
# Compara si un valor es menor o igual que otro
es_menor_o_igual_que = 5 <= 6 # True

# MOSTRAR LOS RESULTADOS
print(es_igual_que) # False
print(es_distinto_que) # True
print(es_mayor_que) # False
print(es_menor_que) # True
print(es_mayor_o_igual_que) # False
print(es_menor_o_igual_que) # True

# CÁLCULOS COMBINADOS
a = 5
b = 10
c = 20
comparacion = a + b == c
print(comparacion) # False

# COMPARAR USUARIO
contraseña_almacenada = "AlejandroPython"
contraseña_escrita = "Alex"
print(contraseña_almacenada == contraseña_escrita) # False