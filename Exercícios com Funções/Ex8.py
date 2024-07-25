"""Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado."""

def quan_dig(numero_int):
    numero_int = str(numero_int)
    tamanho = len(numero_int)
    return tamanho

numero = int(input("Digite um numero inteiro:"))

quantidade = quan_dig(numero)

print(f"A quantidade de dígitos do numero inteiro é de {quantidade}")