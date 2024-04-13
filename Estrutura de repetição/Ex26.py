#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
print('_'*30)
print("CALCULADOR DE VOTOS")
n_t_e = int(input("Digite o numero de eleitores:"))

c1 = 0
c2 = 0
c3 = 0

for c in range(1,n_t_e+1):
    voto = int(input("Digite o numero do candidato:"))
    
    if voto == 1:
        c1 += 1
    if voto == 2:
        c2 += 1
    if voto == 3:
        c3 += 1

print(f"Quantidade de votos total do 1° candidato:{c1}")
print(f"Quantidade de votos total do 2° candidato:{c2}")
print(f"Quantidade de votos total do 3° candidato:{c3}")


