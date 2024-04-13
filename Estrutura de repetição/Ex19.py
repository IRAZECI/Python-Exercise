#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

valor = 0
maior_valor = 0
menor_valor = 9999
soma = 0
numero = 0
conta = 1
sair = 0

while sair != 's':
    if numero == 0:
        numero = int(input("Digite um conjunto de numeros entre (0-1000):"))
        conta += 1
    
    while numero > 1000 or numero < 0:
        numero = int(input("Digite novamente um conjunto de numeros entre (0-1000):"))
        conta += 1
    numero = int(input("Digite um conjunto de numeros entre (0-1000):"))
    
    if conta == 4:
       sair = str(input("Digite 's' para sair ou 'c' para continuar:"))
       conta = 0
       

    if numero > maior_valor:
        maior_valor = numero

    if  numero < menor_valor:  
        menor_valor = numero

    soma = numero + soma
    
    conta += 1

print(f"O maior valor é:{maior_valor}")
print(f"O menor valor é:{menor_valor}")
print(f"A soma de todos os valores é:{soma}")