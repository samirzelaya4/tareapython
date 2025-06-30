import os
os.system("cls")

primer_numero = int( input("Numero de 3 cifras: "))
segundo_numero = int(input("Numero de 3 cifras: "))

pN_1cifra = primer_numero // 100
pN_2cifra = (primer_numero // 10) % 10
pN_3cifra = primer_numero % 10

sN_1cifra = segundo_numero // 100
sN_2cifra = (segundo_numero // 10) % 10
sN_3cifra = segundo_numero % 10

numeros_intercambiadas_1 = (sN_3cifra * 100) + (pN_2cifra * 10) + sN_1cifra
numeros_intercambiadas_2 = (pN_3cifra * 100) + (sN_2cifra * 10) + pN_1cifra

print(f"Numeros intercambiadas {numeros_intercambiadas_1:.2f}")
print(f"Numeros intercambiadas {numeros_intercambiadas_2:.2f}")