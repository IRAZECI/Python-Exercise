#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
numero = int(input("Digite um numero inteiro:"))
conta = 1
primo = 0

if numero == 1:
    print(f'o numero {numero} não é primo')

while numero >= conta:
    if numero % conta == 0:
        primo += 1
    

    conta += 1

if primo == 2:
        print(f'o numero {numero} é primo')
if primo > 2:
        print(f'o numero {numero} não é primo')
