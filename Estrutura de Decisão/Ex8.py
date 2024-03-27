#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input("Digite o valor do primeiro produto:"))
p2 = float(input("Digite o valor do segundo produto:"))
p3 = float(input("Digite o valor do terceiro produto:"))

if p1 > p2:
   maior_valor = p1
else:
   maior_valor = p2

if maior_valor < p3:
   maior_valor = p3

if maior_valor == p1:
   maior_pedido = "primeiro pedido"
elif maior_valor == p2:
    maior_pedido = "segundo pedido"
elif maior_valor == p3:
    maior_pedido = "terceiro pedido"
 
print(f"O produto indicado é o {maior_pedido} no valor de {maior_valor}.") 

