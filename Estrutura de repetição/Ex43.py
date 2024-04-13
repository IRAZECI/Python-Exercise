#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
#Cachorro Quente 100     R$ 1,20
#Bauru Simples   101     R$ 1,30
#Bauru com ovo   102     R$ 1,50
#Hambúrguer      103     R$ 1,20
#Cheeseburguer   104     R$ 1,30
#Refrigerante    105     R$ 1,00

codigo = 0
q_100 = 0
q_101 = 0
q_102 = 0
q_103 = 0
q_104 = 0
q_105 = 0
valor_p_100 = 1.20
valor_p_101 = 1.30
valor_p_102 = 1.50
valor_p_103 = 1.20
valor_p_104 = 1.30
valor_p_105 = 1.00



print("_"*50)
while codigo >= 0:
    codigo = int(input("Insira o codigo do produto:"))
    
    if codigo > 0:
        quantidade = int(input("Digite a quantidade do produto:"))
    
    if codigo == 100:
        q_100 = quantidade
        
    if codigo == 101:
        q_101 = quantidade
        
    if codigo == 102:
        q_102 = quantidade
        
    if codigo == 103:
        q_103 = quantidade
        
    if codigo == 104:
        q_104 = quantidade
        
    if codigo == 105:
        q_105 = quantidade 
      

vt_100 = q_100 * valor_p_100
vt_101 = q_101 * valor_p_101
vt_102 = q_102 * valor_p_102
vt_103 = q_103 * valor_p_103
vt_104 = q_104 * valor_p_104
vt_105 = q_105 * valor_p_105

valor_total_geral = vt_100 + vt_101 + vt_102 + vt_103 + vt_104 + vt_105

print("_"*50)
print(f"Foram comprados {q_100} Cachorro Quentes.Valor total do item:{vt_100}")
print(f"Foram comprados {q_101} Bauru Simples.Valor total do item:{vt_101 }")
print(f"Foram comprados {q_102} Bauru com ovo .Valor total do item:{vt_102}")
print(f"Foram comprados {q_103} Hambúrguer.Valor total do item:{vt_103}")
print(f"Foram comprados {q_104} Cheeseburguer.Valor total do item:{vt_104}")
print(f"Foram comprados {q_105} Refrigerante.Valor total do item:{vt_105}")
print(f"VALOR TOTAL: {valor_total_geral}")

