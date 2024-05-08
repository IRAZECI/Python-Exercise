'''
Faça um Programa que leia um vetor de 5 números inteiros, 
mostre a soma, 
a multiplicação 
e os números.
'''

numeros_inteiros = []
soma = 0
multi = 1

for i in range(0,5):
    numeros_inteiros.append(int(input(f"Insira o {i+1}° numero:")))

for s in numeros_inteiros:
    soma = soma + s 

for m in numeros_inteiros:
    multi = multi * m
    


print(f"Numeros:{numeros_inteiros}")
print(f"Soma dos numeros:{soma}")
print(f"Multiplicação dos numeros:{multi}")