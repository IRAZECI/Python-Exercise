#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120 

fatorial = int(input("Digite o numero que você deseja fatorar:"))
c = fatorial
f = 1

print(f"Calculando {c}!")

while c > 0:
    print(f"{c}",end='')
    print('x' if c > 1 else '=',end='')
    f = f * c
    c -= 1
    
print(f"{f}")