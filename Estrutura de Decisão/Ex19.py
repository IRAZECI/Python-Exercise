#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
numero_inteiro = int(input("Digite um numero inteiro menor que 1000:"))
unidade = numero_inteiro // 1 % 10
dezena = numero_inteiro // 10 % 10
centena = numero_inteiro // 100 % 10

if unidade == 1:
    unidade_nome = "unidade"
else:
    unidade_nome = "unidades"

if dezena == 1:
    dezena_nome = "dezena"
else:
    dezena_nome = "dezenas"

if centena == 1:
    unidade_nome = "centena"
else:
    unidade_nome = "centenas"

if centena < 1:
    print(f"{dezena} {dezena_nome} e  {unidade} {unidade_nome}.")
else:
    print(f"{centena} {unidade_nome},{dezena} {dezena_nome} e  {unidade} {unidade_nome}.")
    
