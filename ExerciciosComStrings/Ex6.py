"""
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e 
imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""

def mesporextenso(mes):
    if mes == 1:
        m = "janeiro"
    elif mes == 2:
        m =  "fevereiro"
    elif mes == 3:
        m =  "março"
    elif mes == 4:
        m =  "abril"
    elif mes == 5:
        m =  "maio"
    elif mes == 6:
        m =  "junho"
    elif mes == 7:
        m =  "julho"
    elif mes == 8:
        m =  "agosto"
    elif mes == 9:
        m =  "semtembro"
    elif mes == 10:
        m =  "outubro"
    elif mes == 11:
        m =  "novembro"
    elif mes == 12:
        m =  "dezembro"
    
    return m
    

print("_"*30)
Data = input("Insira sua data de nascimento:")

d,m,a = Data.split("/")
m = int(m)
m = mesporextenso(m)

print("_"*30)
print(f"Você nasceu em  {d} de {m} de {a}.")