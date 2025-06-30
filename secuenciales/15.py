import os
os.system("cls")

juan = int( input("Juan: "))
rosa = int( input("Rosa: "))
daniel_soles = int( input("Daniel: "))

daniel = daniel_soles / 3.00

capital_total = juan + rosa + daniel

pJuan = juan * 100 / capital_total 
pRosa = rosa * 100 / capital_total
pDaniel = daniel * 100 / capital_total 

print(f"Total de capital en dolares: {capital_total:.2f}")

print(f"% porcentaje de Juan: {pJuan:.2f}%")
print(f"% porcentaje de Rosa: {pRosa:.2f}%")
print(f"% porcentaje de Daniel: {pDaniel:.2f}%")
