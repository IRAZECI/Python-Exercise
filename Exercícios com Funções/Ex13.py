"""
13.Desenha moldura. Construa uma função que desenhe um retângulo usando os caracterer #. 
Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo 
igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para 
valores dentro da faixa de forma elegante.
"""
def valor_por_omissao(Linhas):
    if Linhas=='' or Linhas == 0:
        return int(1)
    elif Linhas > 20:
       Linhas = 20
       return Linhas
    else:
        return Linhas

def valor_por_omissao_2(Colunas):
    if Colunas=='' or Colunas == 0:
        return int(1)
    elif Colunas > 20:
       Colunas = 20
       return Colunas
    else:
        return Colunas


def moldura(colunas,linhas):  
    l = 0
    while l < linhas:
      
      c = 0
      
      while c < colunas:
        print("#",end="")
        c += 1
      
      l += 1
      
      print()
      
    return "" 

c = int(input("Diga quantos colunas, entre 1 e 20:"))
l = int(input("Diga quantos linhas, entre 1 e 20:"))
   
c_f = valor_por_omissao(c)
l_f = valor_por_omissao_2(l)

    
moldura_final = moldura(c_f,l_f)

print(moldura_final)