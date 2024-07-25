"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""
def n_termo(numero):
    print(f"{numero}   "*10)
    
                
numero = int(input("Digite o numero para o teste da função:"))

n_termo(numero)