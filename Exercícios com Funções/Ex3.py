"""
Faça um programa, com uma função que necessite de três argumentos, 
e que forneça a soma desses três argumentos.
"""

def funcao(a,b,c):
    r = a + b + c
    print(f"{a}+{b}+{c} = {r}")

a = int(input("Digite o 1° termo:"))

b = int(input("Digite o 2° termo:"))

c = int(input("Digite o 3° termo:"))

funcao(a,b,c)


