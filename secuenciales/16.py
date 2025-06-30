import os
os.system("cls")

horas = int( input("Horas: "))
tarifas = int( input("tarifas: "))

sueldo_basico = horas * tarifas
sueldo_bruto = sueldo_basico + (sueldo_basico * 0.20)
sueldo_neto = sueldo_bruto - (sueldo_bruto * 0.10)

print(f"Sueldo basico: {sueldo_basico:.2f}")
print(f"Sueldo Bruto: {sueldo_bruto:.2f}")
print(f"Suelgo neto: {sueldo_neto:.2f}")
