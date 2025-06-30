import os
os.system("cls")

cateto_A = int( input("Cateto A: "))
cateto_B = int( input("Cateto B: "))

hipotenusa = (cateto_A ** 2 + cateto_B ** 2) ** 0.5

print(f"Hipotenusa: {hipotenusa:.2f}")