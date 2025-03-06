#Número positivo, negativo o cero
 #Escribe un programa que solicite un número al usuario y determine si es positivo, negativo o cero.

#Solicitar un numero al usuario
numero = float(input("Ingrese un número: "))

# Determinar si el número es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")