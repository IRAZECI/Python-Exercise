""" 
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
"""

palavra = input("Digite o nome de usuário:")

palavra = palavra.upper()

palavra = list(palavra)

for nome in palavra:
    print(f"{nome}")