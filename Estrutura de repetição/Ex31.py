#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
print("_"*30)
print("LOJAS TABAJARA")
valor = 1
c = 1
valor_total = 0
sair = 1


while sair != 0:
    while valor != 0:
       valor = float(input(f"Digite o valor do {c}° produto: R$"))
       valor_total = valor + valor_total
       c += 1

    valor = 1
    c = 1

    print("_"*30)    
    dinheiro = float(input("DINHEIRO: R$"))
    if dinheiro >= valor_total:
      troco = dinheiro - valor_total
    else:
      dinheiro = float(input("(INSIRA NOVAMENTE) DINHEIRO: R$"))
      troco = dinheiro - valor_total
 
    print("_"*30) 
    print(f"TROCO: R$ {troco}")

    dinheiro = 0
    troco = 0
    valor_total = 0
    

    sair = int(input("Digite 0 para sair ou 1 para continuar:"))





    



