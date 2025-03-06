# calculadora de Descuento

# Solicitar el precio del producto
precio = float(input("Ingrese el precio del producto: "))

# Calcular el descuento según el precio
if precio < 50:
    descuento = 0
elif 50 <= precio <= 100:
    descuento = precio * 0.05
else:
    descuento = precio * 0.10

# Calcular el precio final
precio_final = precio - descuento

# Mostrar el resultado
print(f"Descuento aplicado: {descuento:.2f}")
print(f"Precio final: {precio_final:.2f}")