"""
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, 
com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. 
Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4 
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos 
com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando 
completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
"""

matriz = [[8,3,4],\
          [1,5,9],\
          [6,7,2]]


def verificamatriz(matriz):
    if not matriz: #Verifica se a matriz está vazia
        return False
    
    n_l = len(matriz) #verifica o tamanho das colunas da matriz
    
    for n_c in matriz: #Itera sobre as linhas da matriz
        if len(n_c) != n_l:#Se a quantidade de colunas for diferente da quantidade de linhas retorna falso
            return False
        
    return True #Caso a matriz tenha o mesmo numero de linhas e colunas ela é um quadrado mágico


def somalinhas(matriz):
    somalinhas = [] #Cria uma variavel para guardar a soma das linhas
    soma = 0
    for i in matriz:   #Itera sobre as linhas da matriz
        for j in i:  #Itera sobre as colunas da matriz
            soma = soma + j #soma os valores das linhas
        somalinhas.append(soma) #acresenta na lista de soma
        soma = 0 #Zera a variavel soma para a proxíma operação
    
    for linhas in somalinhas:
        linha = somalinhas[0]
        if linhas == linha:
            pass
        else:
            return False
        
    return somalinhas
        

def somacolunas(matriz):
    tamanho = len(matriz)  #indicar tamanho das colunas (como é uma matriz quadrada perfeita linhas e colunas tem o mesmo tamanho)
    somacolunas = [0] * tamanho #Inicializar uma lista para armazenar as somas das colunas
   
    for linha in matriz:  #Itera sobre as linhas da matriz
     for c in range(tamanho): #Cria um range usando como base o tamanho das colunas
        somacolunas[c] += linha[c] #Usa o numero do rage para guiar a soma dos numeros da matriz indicando o índice certo 
    
    for colunas in somacolunas:
        coluna = somacolunas[0]
        if colunas == coluna:
            pass
        else:
            return False
            
    return somacolunas  




if verificamatriz(matriz) == True:
    if somalinhas(matriz) == False or somacolunas(matriz) == False:
     print("_"*30)
     print("A matriz não é um quadrado mágico.")
    else:
       linhas = somalinhas(matriz)
       colunas = somacolunas(matriz)
       print("_"*30)
       print("A matriz é um quadrado mágico.")
       print("_"*30)
       print(f"A somas de todas as linhas foram de:\n{linhas} respectivamente")
       print(f"A somas de todas as colunas foram de:\n{colunas} respectivamente")




