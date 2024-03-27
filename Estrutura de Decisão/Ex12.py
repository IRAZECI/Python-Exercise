#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

valor_hora = float(input("Digite o valor ganho por hora:"))
quantidade_horas = int(input("Digite a quantidade de horas trabalhadas no mês:"))

salário_bruto = quantidade_horas * valor_hora
desconto_inss = 0.10
desconto_fgtf = 0.11

#Desconto ir: 
if  salário_bruto <= 1500:
      desconto_ir = 0.05
      descontado_ir = salário_bruto * desconto_ir

elif  salário_bruto <= 2500:    
      desconto_ir = 0.10
      descontado_ir = salário_bruto * desconto_ir

elif  salário_bruto > 2500:
      desconto_ir = 0.20
      descontado_ir = salário_bruto * desconto_ir

#Desconto inss:
descontado_inss = salário_bruto * desconto_inss
#Desconto fgtf:
descontado_fgtf = salário_bruto * desconto_fgtf
#Total Descontado:
total_Descontado = descontado_ir + descontado_inss + descontado_fgtf
#Salário Liquido:
salário_liquido = salário_bruto - total_Descontado

print(f"Total de descontos:{total_Descontado}")
print(F"Salário liquido:{salário_liquido}")