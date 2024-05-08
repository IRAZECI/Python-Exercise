#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

caracteres = []
consoantes = 0

for i in range(0,10):
    caracteres.append(input("Insira um caracter:"))
    
for i in caracteres:
    if i == 'a' or i == "e" or i == "i" or i == "o" or i == 'u':
        consoantes += 1 

print(f"Caracters:{caracteres}")
print(f"Quantidade de consoantes: {consoantes}")

