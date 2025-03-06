#Clasificación de IMC

# Solicitar el peso y la altura
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Clasificar el IMC
if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc <= 24.9:
    clasificacion = "Normal"
elif 25 <= imc <= 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

# Mostrar el resultado
print(f"Su IMC es: {imc:.2f}")
print(f"Clasificación: {clasificacion}")