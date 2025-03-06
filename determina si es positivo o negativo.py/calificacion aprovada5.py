#Calificación aprobatoria
 #Solicita la calificación de un estudiante (0-100) y determina si aprobó (mínimo 60) o reprobó.

# Solicitar la calificación del estudiante
calificacion = float(input("Ingrese la calificación del estudiante (0-100): "))

# Determinar si aprobó o reprobó
if calificacion >= 60:
    print("El estudiante aprobó.")
else:
    print("El estudiante reprobó.")
