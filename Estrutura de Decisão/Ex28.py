tipo_carne = input("Digite o tipo da carne desejada ('fd' para file Duplo),('a' para alcatra)e('p' para picanha):")
quantidade_carne = float(input("Digite a quantidade em kg desejados:"))
tem_cartao = input("Digite sim se tiver o cartão da loja:")

valor_kilo = 0

if tipo_carne == "fd" and quantidade_carne <= 5:
    tipo_carne_nome = "file Duplo"
    valor_kilo = 4.90
    valor_total = (valor_kilo * quantidade_carne) 
if tipo_carne == "fd" and quantidade_carne > 5:
    tipo_carne_nome = "file Duplo"
    valor_kilo = 5.80
    valor_total = (valor_kilo * quantidade_carne) 
if tipo_carne == "a" and quantidade_carne <= 5:
    tipo_carne_nome = "alcatra"
    valor_kilo = 5.90
    valor_total = (valor_kilo * quantidade_carne) 
if tipo_carne == "a" and quantidade_carne > 5:
    tipo_carne_nome = "alcatra"
    valor_kilo = 6.80
    valor_total = (valor_kilo * quantidade_carne) 
if tipo_carne == "p" and quantidade_carne <= 5:
    tipo_carne_nome = "picanha"
    valor_kilo = 6.90
    valor_total = (valor_kilo * quantidade_carne) 
if tipo_carne == "p" and quantidade_carne > 5:
    tipo_carne_nome = "picanha"
    valor_kilo = 7.80
    valor_total = (valor_kilo * quantidade_carne) 

if tem_cartao == "sim":
    forma_pagamento = "cartão"
    valor_desconto = valor_total * 0.05
    Valor_pagar = valor_total - valor_desconto
else:
     forma_pagamento = "dinheiro"
     valor_desconto = 0
     Valor_pagar = valor_total

print("---NOTA FISCAL---")
print(f"Tipo de carne:{tipo_carne_nome}")
print(f"Quantidade de carne:{quantidade_carne:.2f}")
print(f"Valor total:{valor_total:.2f}R$")
print(f"Forma de pagamento:{forma_pagamento}")
print(f"Valor do desconto de:{valor_desconto:.2f}")
print(f"Valor a pagar:{Valor_pagar:.2f}")

