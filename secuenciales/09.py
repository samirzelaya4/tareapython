import os
os.system("cls")

numero = int(input("Numero: "))

primer_cifra = numero // 1000
segunda_cifra = (numero // 100) % 10
tercera_cifra = (numero // 10) % 10
cuarta_cifra = numero % 10

Suma_cifras= primer_cifra + segunda_cifra + tercera_cifra + cuarta_cifra

print(f"Suma de las cifras: {Suma_cifras:.2f}")