n1 = float(input("Insira o primeiro numero:"))
n2 = float(input("Insira o segundo numero:"))
pergunta = input("Qual operação deseja realizar:")


if pergunta == "soma" or "Soma":
    resultado = n1 + n2    

elif pergunta == "Subtração" or "subtração":
    resultado = n1 - n2     

elif pergunta == "Multiplicação" or "multiplicação":
    resultado = n1 * n2

elif pergunta == "divisão" or "Divisão":
    resultado = n1 / n2

if resultado % 2 == 0:
    resultado_1 = "Par"
else:
    resultado_1 = "Ímpar"

if resultado < 0:
    resultado_2 = "Negativo"
else:
    resultado_2 = "Positivo"

resultado_round = round(resultado)

if resultado_round == resultado:
    resultado_3 = "Inteiro"
else:
    resultado_3 = "Decimal"

print(f"Resultado da operação:{resultado}")
print(f"O resultado é {resultado_1},{resultado_2} e {resultado_3}")
