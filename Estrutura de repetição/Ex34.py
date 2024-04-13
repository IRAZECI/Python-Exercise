#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
numero = int(input("Insira um numero:"))
div = 0

for c in range(1,numero+1):
    if numero % c == 0:
        div += 1 

if div == 2:
    print(f"O numero {numero} é primo.")
else:
    print(f"O numero {numero} não é primo.")

