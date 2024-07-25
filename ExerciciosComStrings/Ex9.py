"""
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato
xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos 
verificadores edos caracteres de formatação.
"""
import sys

def verificacpf(n1,n2,n3,n4):
    verifica = 0
    if len(n1) == 3:
        verifica += 1
    if len(n2) == 3:
        verifica += 1
    if len(n3) == 3:
        verifica += 1
    if len(n4) == 2:
        verifica += 1
        
    if verifica == 4:
        return "válido"
    else:
        return "inválido"


print("--Verificação de CPF--")
cpf = input("insira seu número de CPF:")
p = cpf.count(".")
t = cpf.count("-")


if p != 2:
    print("----CPF INVÁLIDO----")
    sys.exit(0)
elif t != 1:
    print("----CPF INVÁLIDO----")
    sys.exit(0)
    


n_1 , n_2 , n_3  = cpf.split(".")
 
     
n_4 = n_3.split("-")
n_3 = n_4[0]
n_4 = n_4[1]
n_4 = str(n_4)

verifica = verificacpf(n_1,n_2,n_3,n_4)

print("--RESULTADO--")
print(f"O numero de CPF inserido é {verifica}.")

