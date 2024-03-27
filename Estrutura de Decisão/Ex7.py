#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input("Digite o primeiro numero:"))
n2 = float(input("Digite o segundo numero:"))
n3 = float(input("Digite o terceiro numero:"))

if n1 > n2:
    maior_n = n1
    menor_n = n2
else:
    maior_n = n2
    menor_n = n1

if maior_n < n3:
    maior_n = n3
if menor_n > n3:
    menor_n = n3     



print(f"O maior numero é {maior_n:.1f}")
print(f"O menor numero é {menor_n:.1f}")