#Faça um Programa que peça dois números e imprima o maior deles.

#coleta dados
n1 = float(input("Digite um numero:"))
n2 = float(input("Digite outro numero:"))

#Comparação
if(n1 > n2):
    print(f"O maior numero é {n1:.2f}")
else:
    print(f"O maior numero é {n2:.2f}")    

