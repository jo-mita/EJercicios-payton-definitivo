#Clasificación de números

# Solicitar la entrada de tres números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Contar la cantidad de positivos, negativos y ceros
positivos = sum(1 for num in (numero1, numero2, numero3) if num > 0)
negativos = sum(1 for num in (numero1, numero2, numero3) if num < 0)
ceros = sum(1 for num in (numero1, numero2, numero3) if num == 0)

# Determinar la clasificación
if ceros > 0:
    clasificacion = "Hay ceros"
elif positivos == 3:
    clasificacion = "Todos los números son positivos"
elif negativos == 3:
    clasificacion = "Todos los números son negativos"
else:
    clasificacion = "Números mixtos"

# Mostrar el resultado
print(clasificacion)