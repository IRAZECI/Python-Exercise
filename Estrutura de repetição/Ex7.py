#Faça um programa que leia 5 números e informe o maior número.

peso = 0

#Coletar os dados usando for/ range e comparar para saber qual é o maior
for n in range(1,6):
    numero = float(input(f"Digite o {n}ª numero:"))
    if n == 1:
       maior = numero
    else: 
        if numero > maior:
            maior = numero

print("O maior numero é {}".format(maior))
        

