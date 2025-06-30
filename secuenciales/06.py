import os
os.system("cls")

radio = int( input("Radio: "))
altura= int( input("Altura: "))

pi = 3.1416
area = 2 * pi * radio * (radio + altura)
volumen = pi * (radio ** 2) * altura

print(f"Area total del cilindro {area:.2f}")
print(f"Volumen total del cilindro {volumen:.2f}")