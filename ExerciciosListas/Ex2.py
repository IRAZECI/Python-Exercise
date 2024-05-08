#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numero = []

for i in range(0,10):
    numero.append(float(input(f"Insira o {i+1}° numero:")))

print(numero[::-1])