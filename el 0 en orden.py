# Solicitar al usuario que ingrese un número entero
numero = int(input("Por favor, ingresa un número entero: "))

# Inicializar el contador en el número ingresado
contador = numero

# Imprimir los números en orden descendente hasta 0
while contador >= 0:
    print(contador)  # Imprimir el número actual
    contador -= 1    # Decrementar el contador en 1