import os
os.system("cls")

dinero_soles = float(input("Cantidad de dinero en soles: "))

billetes_200 = dinero_soles // 200
dinero_soles= dinero_soles % 200

billetes_100 = dinero_soles // 100
dinero_soles = dinero_soles % 100

billetes_50 = dinero_soles // 50
dinero_soles = dinero_soles % 50

biletes_20 = dinero_soles // 20
dinero_soles = dinero_soles % 20

billetes_10 = dinero_soles // 10
dinero_soles = dinero_soles % 10

billetes_5 = dinero_soles // 5
dinero_soles = dinero_soles % 5

billetes_2 = dinero_soles // 2
dinero_soles = dinero_soles % 2

billetes_1 = dinero_soles // 1
dinero_soles = dinero_soles % 1

print(f"Billetes de 200: {billetes_200}")
print(f"Billetes de 100: {billetes_100}")
print(f"Billetes de 50: {billetes_50}")
print(f"Billetes de 20: {biletes_20}")
print(f"Billetes de 10: {billetes_10}")
print(f"Billetes de 5: {billetes_5}")
print(f"Billetes de 2: {billetes_2}")
print(f"Billetes de 1: {billetes_1}")