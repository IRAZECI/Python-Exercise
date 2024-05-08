'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.'''

numeros = []
par = []
impar = []

for i in range(0,20):
    numeros.append(int(input("Insira o numero:")))
    
for i in numeros:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
        
        
print("_"*50)
print(f"Numeros: {numeros}")
print(f"Numeros pares: {par}")
print(f"Numeros impares: {impar}")
