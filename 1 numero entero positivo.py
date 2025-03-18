#1. Escribe un programa que pida al usuario que ingrese un número entero positivo. El programa debe mostrar todos los números del 1 hasta el número ingresado, uno por uno, utilizando un bucle while.

# Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Por favor, ingresa un número entero positivo: "))

# Verificar que el número ingresado sea positivo
if numero > 0:
    contador = 1  # Inicializar el contador en 1
    # Utilizar un bucle while para mostrar los números del 1 al número ingresado
    while contador <= numero:
        print(contador)  # Mostrar el número actual
        contador += 1  # Incrementar el contador en 1
else:
    print("El número ingresado no es positivo. Por favor, intenta nuevamente.")