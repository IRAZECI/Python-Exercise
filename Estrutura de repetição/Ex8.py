#Faça um programa que leia 5 números e informe a soma e a média dos números.

for n in range(1,6):
    numero = float(input("Digite o {}º número:".format(n)))
    if n == 1:
        soma = numero
    else:
        soma = soma + numero

media = soma / 5 

print("A soma total foi de {}".format(soma))
print(f"A média dos 5º numeros foi {media}")