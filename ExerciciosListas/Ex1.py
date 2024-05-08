#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = []

for i in range(0,5):
    vetor.append(int(input(f'Insira {i+1}° numero ao vetor:')))
    
print(vetor)
    