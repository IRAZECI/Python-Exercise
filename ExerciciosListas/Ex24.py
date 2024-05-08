"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . 
Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e
uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
"""
import random

conta = 0
jogadas = []
numero_jogadas = 100
lado1 = []
lado2 = []
lado3 = []
lado4 = []
lado5 = []
lado6 = []
numero_aleatorio = 0




while conta <= numero_jogadas:
    jogadas.append(random.randint(1,6))
    conta += 1

for j in jogadas:
    if j == 1:
        lado1.append(j)
    if j == 2:
        lado2.append(j)
    if j == 3:
        lado3.append(j)
    if j == 4:
        lado4.append(j)
    if j == 5:
        lado5.append(j)
    if j == 6:
        lado6.append(j)

c_lado1 = 0
c_lado2 = 0
c_lado3 = 0
c_lado4 = 0
c_lado5 = 0
c_lado6 = 0


for j in lado1:
    c_lado1 += 1
for j in lado2:
    c_lado2 += 1
for j in lado3:
    c_lado3 += 1
for j in lado4:
    c_lado4 += 1
for j in lado5:
    c_lado5 += 1
for j in lado6:
    c_lado6 += 1
    
    
    
print("_"*40)  
print(f"O lado 1 do dado caiu {c_lado1} vezes")
print(f"O lado 2 do dado caiu {c_lado2} vezes")
print(f"O lado 3 do dado caiu {c_lado3} vezes")
print(f"O lado 4 do dado caiu {c_lado4} vezes")
print(f"O lado 5 do dado caiu {c_lado5} vezes")
print(f"O lado 6 do dado caiu {c_lado6} vezes")