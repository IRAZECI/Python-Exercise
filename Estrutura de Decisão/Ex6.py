#Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input("Digite o primeiro numero:"))
n2 = float(input("Digite o segundo numero:"))
n3 = float(input("Digite o terceiro numero:"))


if n1 > n2:
   maior_n = n1
else:
    maior_n = n2

if maior_n < n3:
    maior_n = n3

print(f"O maior numero é:{maior_n:.1f}")    


