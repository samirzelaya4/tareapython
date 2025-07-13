import os
os.system("cls")

donacion = int( input("donacion = "))

centro_salud = donacion * 0.25
comedor_infantil = donacion * 0.35
escuela_infantil = donacion * 0.25
asilo_ancianos = donacion - (centro_salud + comedor_infantil + escuela_infantil)

print(f"Centro de salud= {centro_salud:.2f}")
print(f"Comedor infantil= {comedor_infantil:.2f}")
print(f"Escuela infantil= {escuela_infantil:.2f}")
print(f"Asilo de ancianos= {asilo_ancianos:.2f}")
