import os
os.system("cls")

articulos_comprados = int( input("Cantidad: "))
precio = float( input("Precio: "))

importe_compra = articulos_comprados * precio

descuento1 = importe_compra * 0.15
subtotal = importe_compra - descuento1

descuento2 = subtotal * 0.15

descuento_total = descuento1 + descuento2

importe_final = importe_compra - descuento_total

print(f"importe de a¿la compra: {importe_compra:.2f}")
print(f"Descuento total: {descuento_total:.2f}")
print(f"Importe a pagar: {importe_final:.2f}")