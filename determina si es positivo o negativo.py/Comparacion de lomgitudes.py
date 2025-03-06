# Solicitar la entrada de tres longitudes
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

# Determinar si las longitudes pueden formar un triángulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    resultado = "Las longitudes pueden formar un triángulo."
else:
    resultado = "Las longitudes no pueden formar un triángulo."

# Mostrar el resultado
print(resultado)