#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
numero = int(input("Digite um numero inteiro:"))
conta = 1
primo = 0


if numero == 1:
    print(f'o numero {numero} não é primo')
    print(f'O numero é divisivel apenas por ele mesmo.')

while numero >= conta:
    if numero % conta == 0:
        primo += 1
        
    conta += 1

if primo == 2:
        print(f'o numero {numero} é primo')
if primo > 2:
        print(f'o numero {numero} não é primo')
        conta = 1
        while numero >= conta:
            if numero % conta == 0:
                if conta == 1:
                    print('O numero é divisivel por ',end='')
                else:
                    print(f'{conta}-',end='')

            conta += 1
        