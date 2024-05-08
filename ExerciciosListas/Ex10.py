"""
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, 
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

vetor_1 = [1,3,5,7,9]
vetor_2 = [2,4,6,8,10]
vetor_3 = []


for a,b in zip(vetor_1,vetor_2):
    vetor_3.append(a)
    vetor_3.append(b)
              

print(vetor_3)