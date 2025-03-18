# Solicitar al usuario que ingrese un número entero no negativo
numero = int(input("Por favor, ingresa un número entero no negativo para calcular su factorial: "))

# Verificar que el número ingresado sea no negativo
if numero <0:
    print("El factorial no está definido para números negativos.")
else:
    factorial = 1  # Inicializar el factorial en 1
    contador = 1    # Inicializar el contador en 1

    # Calcular el factorial utilizando un bucle while
    while contador <= numero:
        factorial *= contador  # Multiplicar el factorial por el contador
        contador += 1          # Incrementar el contador en 1

    # Imprimir el resultado
    print(f"El factorial de {numero} es: {factorial}")
