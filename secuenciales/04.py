import os
os.system("cls")

pies = int( input("Pies: "))
pulgadas = int( input("Pulgadas: "))

pulgadas_total = pies * 12 + pulgadas

centimetros = pulgadas_total * 2.54

metros = centimetros / 100.0

print(f"estatura en metros {metros:.2f}")