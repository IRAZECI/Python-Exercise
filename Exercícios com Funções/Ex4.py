"""
Faça um programa, com uma função que necessite de um argumento. 
A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, 
se seu argumento for zero ou negativo.    
"""
def p_n(argumento):
    if argumento > 0:
        print("P")
    elif argumento <= 0:
         print("N")
    


a = float(input("Insira o argumento:"))

p_n(a)