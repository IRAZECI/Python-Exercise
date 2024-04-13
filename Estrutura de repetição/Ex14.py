#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
conta_par = 0
conta_impar = 0

for i in range(0,10):
    if i == 0:
        numero = int(input("Digite um numero inteiro:"))
    else:
        numero = int(input("Digite outro numero inteiro:"))
    if numero % 2 == 0:
        conta_par += 1
    else:
        conta_impar +=1
else:
    print(f"Quantidade de numeros pares:{conta_par}")
    print(f"Quantidade de numeros pares:{conta_impar}")