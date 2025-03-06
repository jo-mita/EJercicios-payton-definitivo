#Número mayor entre dos
# Pide al usuario que ingrese dos números y determina cuál es el mayor o si son iguales.

# Solicitar la entrada de dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Determinar cuál es el mayor o si son iguales
if numero1 > numero2:
    print(f"El número mayor es: {numero1}")
elif numero2 > numero1:
    print(f"El número mayor es: {numero2}")
else:
    print("Los números son iguales.")