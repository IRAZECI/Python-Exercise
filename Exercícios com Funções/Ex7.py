"""  
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a 
função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de 
prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser 
encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. 
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""

def valorpagamento(valorconta,n_d_atraso):
    if n_d_atraso == 0:
        multa = 0
    else:
        multa = (valorconta * 0.03) + (0.001*n_d_atraso)
        
    valor_total = valorconta + multa
    
    return valor_total

valor_conta = 1
dias_atraso = 0
conta = 0
valor_total = 0

while valor_conta != 0:
    print("_"*40)
    valor_conta = float(input("Insira o valor da parcela a ser paga:"))
    if valor_conta == 0:
        break
    dias_atraso = int(input("Insira a quantidade de dias atrasados:"))
    
    valor_pagamento = valorpagamento(valor_conta,dias_atraso)
    
    print(f"O valor total a ser pago sobre a prestação foi de: {valor_pagamento}")
    
    valor_total = valor_total + valor_pagamento
    conta += 1

print("_"*40)
print("RELATÓRIO DO DIA")
print(f"Quantidade de parcelas pagas:{conta}")
print(f"Valor total das prestações pagas no dia: {valor_total}")

    

    
    
    















