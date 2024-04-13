#Faça um programa que calcule o mostre a média aritmética de N notas.

q_n = int(input("Digite a quantidade de notas que você deseja saber a media:"))
t_n = 0
notas = []

for c in range(1,q_n +1):
    n = int(input(f"Digite a {c} nota:"))                                                
    t_n = n + t_n 
    notas.append(n) 

media = t_n / q_n

print(f'Suas notas foram {notas}')
print(f'A media aritmética das notas foram {media}')
