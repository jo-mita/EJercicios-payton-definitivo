#Día de la semana
# Solicitar un número del 1 al 7
numero = int(input("Ingrese un número del 1 al 7: "))

# Determinar el día de la semana
if numero == 1:
    dia = "Lunes"
elif numero == 2:
    dia = "Martes"
elif numero == 3:
    dia = "Miércoles"
elif numero == 4:
    dia = "Jueves"
elif numero == 5:
    dia = "Viernes"
elif numero == 6:
    dia = "Sábado"
elif numero == 7:
    dia = "Domingo"
else:
    dia = "Número inválido. Debe estar entre 1 y 7."

# Mostrar el resultado
print(dia)