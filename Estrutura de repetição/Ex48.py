#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

numero = int(input("Insira um numero:"))

numero = str(numero)

vetor_a = []

for e in numero:
    vetor_a.append(e)
    
print(vetor_a[::-1])