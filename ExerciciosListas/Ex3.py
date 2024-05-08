#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
soma = 0

for i in range(0,4):
    notas.append(float(input(f"Insira a {i+1}° nota:")))
    
for i in notas:
    soma = soma + i
    
media = soma / 4    
    
 
print(f"Notas:{notas}")
print(f"A media foi: {media}")
