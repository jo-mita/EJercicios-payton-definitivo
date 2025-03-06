# Solicitar la temperatura en grados Celsius
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

# Evaluar la temperatura y mostrar el mensaje correspondiente
if temperatura < 0:
    mensaje = "Hace mucho frío"
elif 0 <= temperatura <= 20:
    mensaje = "Clima fresco"
elif 21 <= temperatura <= 30:
    mensaje = "Clima agradable"
else:
    mensaje = "Hace mucho calor"

# Mostrar el resultado
print(mensaje)