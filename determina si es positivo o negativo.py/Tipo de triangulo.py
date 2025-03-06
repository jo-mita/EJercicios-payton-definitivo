#Tipo de triángulo
 #Pide tres longitudes y determina si el triángulo es equilátero, isósceles o escaleno.
#Evaluación de temperatura

# Solicitar la entrada de tres longitudes
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

# Verificar si pueden formar un triángulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    # Determinar el tipo de triángulo
    if lado1 == lado2 == lado3:
        tipo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
else:
    tipo = "No se puede formar un triángulo."

# Mostrar el resultado
print(f"El triángulo es: {tipo}")