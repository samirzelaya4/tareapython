import os
os.system("cls")

base = int( input("Base: "))
altura = int( input("Altura: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"Area de un rectangulo: {area:.2f}")
print(f"Perimetro de un rectangulo: {perimetro:.2f}")