### EXCEPCIONES ###
# Las excepciones son errores que ocurren durante la ejecución de un programa.

# Creamos una función que sume dos números
def sumar_dos():
    # Iniciamos un bucle infinito
    while True:
        # Pedimos los números al usuario
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        # Intentamos convertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
        # Si lanzo una excepción pedirle que reingrese los datos
        except Exception as e:
            print("Error: Ingrese un número válido")
            print(f"Error: {e}")
        # Si todo salió bien, terminamos el bucle.
        else:
            break
        finally:
            print("Operación realizada")
    # Retornamos el resultado
    return resultado

print(sumar_dos())