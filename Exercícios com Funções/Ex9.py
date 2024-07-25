"""Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. 
Por exemplo: 127 -> 721."""

def reverso(numero):
    numero_n = str(numero)
    return numero_n[::-1]


n = input("Insira um numero:")
numero_final = reverso(n)

print(f"Numero inteiro ao contrario:{numero_final}")