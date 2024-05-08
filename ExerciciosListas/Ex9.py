"""
Faça um Programa que leia um vetor A com 10 números inteiros, 
calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

vetor = []
soma = 0 

for i in range(0,2):
    vetor.append(int(input(f"Insira o {i+1}° vetor:")))
    
for i in vetor:
    i = i ** 2
    soma = i + soma   
    
print(f"Os elementos:{vetor}")
print(f"A soma dos quadrados dos elementos:{soma}")