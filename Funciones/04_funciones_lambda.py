### FUNCIONES LAMBDA ###
# Las funciones lambda son funciones anónimas que se pueden usar para simplificar el código
# Son funciones que se pueden definir en una sola línea
# No tienen un nombre asociado
# Se pueden asignar a una variable
# Se pueden pasar como argumentos de otras funciones
# Se pueden devolver como resultado de una función

# ESTRUCTURA DE UNA FUNCIÓN LAMBDA
# lambda argumentos: expresión
# Por ejemplo, una función que recibe un argumento y devuelve el doble de ese argumento sería:
# lambda x: x * 2

multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(5))

# Esto sería lo mismo que:
# def multiplicar_por_dos(x):
#     return x * 2

# APLICACIONES DE LAMBDA

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Creamos una función común que filtre los números pares
def es_par(num):
    if(num%2==0):
        return True
    
# Usando filter() con una función común
numeros_pares = filter(es_par, numero)
print(f"Resultado de función común:\t{list(numeros_pares)}")

# Ahora, crearemos lo mismo pero con Lambda
num_pares = filter(lambda num:num%2==0, numero)
print(f"Resultado de función lambda:\t{list(num_pares)}")