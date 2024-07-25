#Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

nome = input("Insira seu nome:")

nome = list(nome)


for i in range(len(nome)):
    if i == 0:
        print("".join(nome))
    else:
        del nome[-1]
        print("".join(nome))