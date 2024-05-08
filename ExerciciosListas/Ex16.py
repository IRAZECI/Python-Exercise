'''
Utilize uma lista para resolver o problema a seguir. 
Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, 
um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam 
salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, 
sem fazer vários ifs aninhados.
'''

quantidade_vendedores = int(input("Insira a quantidade de vendedores da loja:"))
valor_vendido = []
salario = []
faixa_salarial = {}
conta1 = 0
conta2 = 0
conta3 = 0
conta4 = 0
conta5 = 0
conta6 = 0
conta7 = 0
conta8 = 0
conta9 = 0

for i in range(0,quantidade_vendedores):
    valor_vendido.append(float(input(f"Insira o valor bruto vendido na semana pelo {i+1}°:")))

for v in valor_vendido:
    salario.append(200 + (v * 0.09))

for f in salario:
    if f > 200 and f < 299:
        conta1 +=1
        
    if f > 300 and f < 399:
        conta2 +=1
        
    if f > 400 and f < 499:
        conta3 +=1
        
    if f > 500 and f < 599:
        conta4 +=1
        
    if f > 600 and f < 699:
        conta5 +=1
        
    if f > 700 and f < 799:
        conta6 +=1
        
    if f > 800 and f < 899:
        conta7 +=1
        
    if f > 900 and f < 999:
        conta8 +=1
        
    if f > 1000 and f < 100000:
        conta9 +=1
        
        
    
print(f"Salários dos funcionarios:")
print( salario)
print(f" $200 - $299 -{conta1}- \n $300 - $399 -{conta2}- \n $400 - $499 -{conta3}- \n $500 - $599 -{conta4}- \n $600 - $699 -{conta5}- \n $700 - $799 -{conta6}-\n $800 - $899 -{conta7}-\n $900 - $999 -{conta8}-\n $1000 em diante -{conta9}-")




    
