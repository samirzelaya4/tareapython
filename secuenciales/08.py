import os
os.system("cls")

radio = int( input("Radio: "))
altura = int( input("Altura: "))
pi = 3.1416

area_base = pi * (radio ** 2)
area_lateral = 2 * pi * radio * altura
area_total = 2 * area_base * area_lateral

print(f"Area base: {area_base:.2f}")
print(f"Area lateral: {area_lateral:.2f}")
print(f"Area total: {area_total:.2f}")
