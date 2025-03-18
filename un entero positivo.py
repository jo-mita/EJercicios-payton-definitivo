# Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Por favor, ingresa un número entero positivo: "))

# Verificar que el número ingresado sea positivo
if numero > 0:
    contador = 1  # Inicializar el contador en 1
    # Imprimir los números impares utilizando un bucle while
    while contador <= numero:
        print(contador)  # Imprimir el número impar actual
        contador += 2    # Incrementar el contador en 2 para obtener el siguiente impar
else:
    print("El número ingresado no es positivo. Por favor, intenta nuevamente.")