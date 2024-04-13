#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.


divida = float(input("Digite o valor da dívida:"))


for i in range(0,5):
    if i == 0:
        quantidade_parcelas = 1
        valor_juros = 0
        valor_parcelas = divida
        valor_divida = divida
    if i == 1:
        quantidade_parcelas = 3
        valor_juros = divida * 0.10
        valor_parcelas = (divida + valor_juros) / quantidade_parcelas
        valor_divida = divida + valor_juros
    if i == 2:
        quantidade_parcelas = 6
        valor_juros = divida * 0.15
        valor_parcelas =  (divida + valor_juros) / quantidade_parcelas
        valor_divida = divida + valor_juros
    if i == 3:
        quantidade_parcelas = 9
        valor_juros = divida * 0.20
        valor_parcelas =  (divida + valor_juros) / quantidade_parcelas
        valor_divida = divida + valor_juros
    if i == 4:
        quantidade_parcelas = 12
        valor_juros = divida * 0.25
        valor_parcelas =  (divida + valor_juros) / quantidade_parcelas
        valor_divida = divida + valor_juros


    print('Valor das dívidas | Valor dos juros | Quantidade de parcelas | Valor das parcelas')
    print(f"{valor_divida:.2f}               {valor_juros:.2f}               {quantidade_parcelas:.0f}                     {valor_parcelas:.2f}         ")
