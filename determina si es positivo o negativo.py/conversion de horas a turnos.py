#Conversión de horas a turnos
 #Pide la hora (0-23) y determina si es "Mañana" (6-11), "Tarde" (12-17), "Noche" (18-23) o "Madrugada" (0-5).

# Solicitar la hora
hora = int(input("Ingrese la hora (0-23): "))

# Determinar la parte del día
if 6 <= hora <= 11:
    parte_del_dia = "Mañana"
elif 12 <= hora <= 17:
    parte_del_dia = "Tarde"
elif 18 <= hora <= 23:
    parte_del_dia = "Noche"
elif 0 <= hora <= 5:
    parte_del_dia = "Madrugada"
else:
    parte_del_dia = "Hora no válida"

# Mostrar el resultado
print(f"Es {parte_del_dia}.")