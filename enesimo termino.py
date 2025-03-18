#Escribe un programa que imprima la serie de Fibonacci hasta el enésimo término, donde el valor de n lo ingresa el usuario, utilizando un bucle for.

# Solicitar al usuario que ingrese el número de términos
n = int(input("Por favor, ingresa el número de términos de la serie de Fibonacci: "))

# Inicializar los primeros términos de la serie
a, b = 0, 1

# Imprimir la serie de Fibonacci
print("Serie de Fibonacci:")
for _ in range(n):
    print(a)  # Imprimir el término actual
    a, b = b, a + b  # Actualizar los términos