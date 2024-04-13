#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
valor = 0
maior_valor = 0
menor_valor = 99999999999
soma = 0
numero = 0
conta = 1
sair = 0

while sair != 's':
    numero = int(input("Digite um conjunto de numeros:"))
    if conta == 4:
       conta = 0
       sair = str(input("Digite 's' para sair ou 'c' para continuar:"))

    if numero > maior_valor:
        maior_valor = numero

    if  numero < menor_valor:  
        menor_valor = numero

    soma = numero + soma
    
    conta += 1

print(f"O maior valor é:{maior_valor}")
print(f"O menor valor é:{menor_valor}")
print(f"A soma de todos os valores é:{soma}")