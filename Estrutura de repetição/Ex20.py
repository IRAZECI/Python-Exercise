#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes 
#e limitando o fatorial a números inteiros positivos e menores que 16.

sair = 0
n = 0
conta = 0
f = 1


while sair != 's':
    
    if conta == 0:
       n = int(input('Insira um número positivo até 16 para calcular a fatorial:'))
       conta += 1
    
    while n > 16 or n <= 0:
        n = int(input('Digite novamente,apenas numeros positivos até 16:'))

    

    while n > 0:
        f = n * f
        print(f"{n}",end='')
        if n == 1:
            print(f"={f}",end='\n')
        else:
            print('x',end='')
        n -= 1

    if conta == 1:
        sair = str(input("Digite 's' para sair 'c' para continuar:"))
        conta = 0
        f = 1

    conta += 1

