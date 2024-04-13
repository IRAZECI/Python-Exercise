#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
base = int(input("Digite a base:"))
expoente = int(input("Digite o expoente:"))

v_f = 0
expoente -= 1

for i in range(0,expoente):
    if i == 0:
        v_f = base * base
    else:
        v_f = v_f * base

print(v_f)
