import os
os.system("cls")

numero = int( input("Numero de 4 cifras: "))

primera_cifra = numero // 1000
segunda_cifra = (numero // 100) % 10
tercera_cifra = (numero // 10) % 10
cuarta_cifra = numero % 10

numero_al_revez = (cuarta_cifra * 1000) + (tercera_cifra * 100) + (segunda_cifra * 10) + primera_cifra 

print(f"Numero al revez: {numero_al_revez}")