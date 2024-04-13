#Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("Digite um numero:"))
n2 = int(input("Digite outro numero:"))

n2 = n2 + 1
soma = 0

for i in range(n1,n2):
    soma = soma + i
    print(i)
else:
    print(soma)
        