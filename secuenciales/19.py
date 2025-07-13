import os
os.system("cls")

ventas = int( input("Ventas= "))

sueldo_basico = 500
comision = ventas * 0.09 

sueldo_bruto = sueldo_basico + comision
descuento = sueldo_bruto * 0.11
sueldo_neto = sueldo_bruto - descuento

print(f"Comision= {comision:.2f}")
print(f"Sueldo bruto= {sueldo_bruto:.2f}")
print(f"Descuento= {descuento:.2f}")
print(f"Sueldo neto= {sueldo_neto:.2f}")
