import os
os.system("cls")

numero_1 = float(input("Ingrese el primer número: "))
numero_2 = float(input("Ingrese el segundo número: "))
numero_3 = float(input("Ingrese el tercer número: "))
numero_4 = float(input("Ingrese el cuarto número: "))
numero_5 = float(input("Ingrese el quinto número: "))

numeros = [numero_1,numero_2,numero_3,numero_4,numero_5]

numeros.sort()

mayor_1 = numeros[2]
mayor_2 = numeros[3]
mayor_3 = numeros[4]

promedio = (mayor_1 + mayor_2 + mayor_3) / 3

print(f"Los 3 numeros mayores: {mayor_1},{mayor_2},{mayor_3}")
print(f"promedio de los 3 numeros mayores: {promedio:.2f}")