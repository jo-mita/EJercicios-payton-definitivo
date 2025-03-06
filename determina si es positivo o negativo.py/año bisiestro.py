# Solicitar el año al usuario
anio = int(input("Ingrese un año: "))

# Determinar si el año es bisiesto
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    es_bisiesto = True
else:
    es_bisiesto = False

# Mostrar el resultado
if es_bisiesto:
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")