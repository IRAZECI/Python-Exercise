#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

print("_"*30)
q_cds = int(input("Digite a quantidade de cds na sua coleção:"))
valor_total = 0

for c in range(1,q_cds+1):
    v_cds = int(input(f"Digite o valor do {c}° cd:"))
    valor_total = valor_total + v_cds
    media_total = valor_total / q_cds

print("_"*30)
print(f"O valor total investido na coleção de cds foi de {valor_total} R$")
print("_"*30)
print(f"O valor médio investido por cd na coleção foi de {media_total} R$")
