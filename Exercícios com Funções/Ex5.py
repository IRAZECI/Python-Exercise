"""
Faça um programa com uma função chamada somaImposto. 
A função possui dois parâmetros formais: taxaImposto, 
que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""

def somaimposta(taxaimposto,custo):
   valor_com_imposto = custo + ((taxaimposto * custo) / 100)
   print(valor_com_imposto)
   



somaimposta(10,200)
