#Clasificación de ángulos
 #Solicita al usuario el valor de un ángulo en grados y determina si es agudo (<90°), recto (90°), obtuso (>90° y <180°) o llano (180°).

# Solicitar el valor del ángulo
angulo = float(input("Ingrese el valor del ángulo en grados: "))

# Determinar la clasificación del ángulo
if angulo < 90:
    tipo_angulo = "Agudo"
elif angulo == 90:
    tipo_angulo = "Recto"
elif 90 < angulo < 180:
    tipo_angulo = "Obtuso"
elif angulo == 180:
    tipo_angulo = "Llano"
else:
    tipo_angulo = "Ángulo no válido (debe ser entre 0 y 180 grados)"

# Mostrar el resultado
print(f"El ángulo es: {tipo_angulo}" )