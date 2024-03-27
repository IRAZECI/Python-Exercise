#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia = int(input("Digite o numero do dia da semana:"))

if dia == 1:
    dia_semana = "Domingo"
    
elif dia == 2:
    dia_semana = "Segunda"

elif dia == 3:
    dia_semana = "Terça"

elif dia == 4:
    dia_semana = "Quarta"

elif dia == 5:
    dia_semana = "Quinta"
    
elif dia == 6:
    dia_semana = "Sexta"

elif dia == 7:
    dia_semana = "Sábado"

else: 
    print("Valor inválido")
    dia_semana = "Erro 888"

print(f"Hoje é {dia_semana}")