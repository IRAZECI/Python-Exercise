#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
print("-"*30)
print("Calcular faixa de idade")
q_p = int(input("Digite a quandidade de pessoas:"))
media = 0
faixa = 0
print("-"*30)

for c in range(1,q_p+1):
    i_p = int(input(f"Digite a idade da {c} pessoa:"))

    media = i_p + media
    faixa = media / q_p
    

if faixa < 25.26:
        print(f"A media de idade é {faixa}, pela media a turma é JOVEM")
elif faixa < 60:
        print(f"A media de idade é {faixa}, pela media a turma é ADULTA")
elif faixa > 60:
         print(f"A media de idade é {faixa}, pela media a turma é IDOSA")

print("-"*30)