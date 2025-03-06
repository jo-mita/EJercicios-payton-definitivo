#Cálculo de impuestos
 #Pide al usuario su salario mensual y aplica los siguientes impuestos:

# Solicitar el salario mensual
salario = float(input("Ingrese su salario mensual: "))

# Calcular el impuesto según el rango del salario
if salario < 10000:
    impuesto = 0
elif 10000 <= salario <= 30000:
    impuesto = salario * 0.10
else:
    impuesto = salario * 0.20

# Mostrar el resultado
print(f"El impuesto a pagar es: {impuesto:.2f}")
