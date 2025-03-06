#Mayor entre tres números
 #Pide al usuario tres números y muestra el mayor de ellos.


# Solicitar la entrada de tres números
numero1 = float(input("Ingrese el primer número: " ))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Determinar el número mayor
mayor = numero1  # Digamos que el primero es el mayor inicialmente

if numero2 > mayor:
    mayor = numero2
if numero3 > mayor:
    mayor = numero3
    
# Mostrar el número mayor
print(f"El número mayor es: {mayor}")