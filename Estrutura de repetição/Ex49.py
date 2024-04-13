#Faça um programa que mostre os n termos da Série a seguir.Imprima no final a soma da série.
#Imprima no final a soma da série.
n_termo = int(input("Digite o n termo da série:"))
n = 0
m = 0
conta = 0
n_termo = n_termo - 1
soma_n = 0
soma_m = 0


while n_termo >= n:
    
    if conta == 0:
        print('S = 1/1 +',end="")
        n = 1
        m = 1
    else:
        
     n = n + 1
     m = m + 2
    
     print(f" {n}/{m} + ",end='')
    
    soma_n = soma_n + n 
    soma_m = soma_m + m
    
    conta += 1
   
print(f"= {soma_n}/{soma_m}")