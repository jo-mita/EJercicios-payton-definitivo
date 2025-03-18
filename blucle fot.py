# Solicitar al usuario que ingrese un número
numero = int(input("Por favor, ingresa un número para ver su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar del número ingresado
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i  # Calcular el resultado de la multiplicación
    print(f"{numero} x {i} = {resultado}")  # Imprimir la multiplicación