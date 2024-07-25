"""Nome na vertical em escada. Modifique o programa anterior de forma a mostrar 
o nome em formato de escada."""

palavra = input("Insira o nome de usuário:")

palavra = palavra.upper()

palavra = list(palavra)

nome_final = []

for nome in palavra:
    nome_final.append(nome)
    print("".join(nome_final))