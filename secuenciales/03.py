import os
os.system("cls")

kilometros = float( input("kilometros: "))
pies = float( input("Pies: "))
millas = float( input("Millas: "))

metros_kilometros = kilometros * 1000.0
metros_pies = pies / 3.2808
metros_millas = millas * 1609

metros_total = metros_kilometros + metros_pies + metros_millas

yardas = metros_total / 0.9144
print(f"Total en metros {metros_total:.2f}")
print(f"Total en yardas {yardas:.2f}")
