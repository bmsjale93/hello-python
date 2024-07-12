### CONDICIONALES ###
# Los condicionales son estructuras de control que permiten tomar decisiones en un programa.
# Estas decisiones se toman en base al resultado de una comparación.

# IF - ELSE
# El condicional if se ejecuta si la condición es verdadera
# El condicional else se ejecuta si la condición es falsa

# EJEMPLO DE USO
edad = 17

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    
# OTRO EJEMPLO
contraseña_almacenada = "AlejandroPython"
contraseña_escrita = "Alex"

if contraseña_almacenada == contraseña_escrita:
    print("Contraseña correcta. Iniciando sesión...")
else:
    print("Contraseña incorrecta. Inténtalo de nuevo")

#USO DE ELIF (ELSE IF)
ingreso_mensual = 10000

if ingreso_mensual > 1000:
    print("Eres clase media")
elif ingreso_mensual > 5000:
    print("Eres clase media-alta")
else:
    print("Eres clase baja")

# IF ANIDADOS
ingreso_mensual = 10000
gastos_mensuales = 5000

if ingreso_mensual > 5000:
    if ingreso_mensual - gastos_mensuales < 0:
        print("Estás gastando más de lo que ganas")
    elif ingreso_mensual - gastos_mensuales > 3000:
        print("Estás ahorrando mucho")
    else:
        print("Estás gastando demasiado")