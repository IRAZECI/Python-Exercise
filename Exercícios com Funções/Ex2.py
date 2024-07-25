"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""


def n_esimo(numero):
    for numero in range(1,numero+1):
         print(numero,end="    ")


n = int(input("Insira um numero para realizar o teste da função:"))
n_esimo(n)