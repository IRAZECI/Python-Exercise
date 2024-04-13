#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
n1 = int(input("Digite um numero inteiro que você deseja saber o fatorial:"))
n2 = 0
resul = 1


while n1 >= 0:
    n2 = n1 - 1
    resul = resul * n1
    if n1 > 1:
        print(f"{n1}.",end="")
    else:
        print(f"1={resul}")
        break
    n1 = n2

  

    
    

